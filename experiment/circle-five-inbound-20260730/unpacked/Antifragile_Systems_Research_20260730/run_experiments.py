#!/usr/bin/env python3
"""
run_experiments.py
==================
Builds the three architectures, runs (a) the Delta-sweep convexity test and
(b) a longitudinal shock-stream run, aggregates over many random seeds, writes
raw results to JSON/CSV, and renders figures.

Outputs (in ./results/ and ./figures/):
    results/convexity.csv        H(Delta) per architecture (mean +/- sd)
    results/timeseries.csv       performance + variety budget over time
    results/redteam.json         misalignment / variety-collapse / ruin stats
    figures/fig1_convexity.png
    figures/fig2_timeseries.png
    figures/fig3_variety_budget.png
    figures/fig4_redteam.png
    figures/fig5_survival.png
"""
from __future__ import annotations
import os, json, csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from antifragile_sim import (
    D, Environment, Unit, Kernel, Institution,
    ARCH_MONO, ARCH_REDUNDANT, ARCH_ANTIFRAGILE,
)

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)

COLORS = {
    ARCH_MONO: "#c0392b",         # red
    ARCH_REDUNDANT: "#e67e22",    # orange
    ARCH_ANTIFRAGILE: "#27ae60",  # green
}
LABELS = {
    ARCH_MONO: "Monoculture (optimized, no degeneracy)",
    ARCH_REDUNDANT: "Redundant (identical copies)",
    ARCH_ANTIFRAGILE: "Antifragile (3-layer design)",
}


# --------------------------------------------------------------------------- #
# Builders                                                                     #
# --------------------------------------------------------------------------- #
def make_probes(rng, n=24):
    P = rng.random((n, D))
    P = P / P.sum(axis=1, keepdims=True)
    return P


def build_institution(arch, rng, n_units=8, seed_misaligned=2):
    """Construct an institution of the given architecture.
    All three serve the SAME kernel goal and start from comparable total
    competence, so differences come from STRUCTURE, not from more resources."""
    goal = np.ones(D) / D
    probes = make_probes(rng)

    if arch == ARCH_MONO:
        # one big unit optimized hard for the *normal* regime (tight coupling,
        # no degeneracy). Kernel seed-rules are OFF (it is a classic optimizer).
        kern = Kernel(goal=goal,
                      r1_bounded_downside=False, r2_reversibility=False,
                      r3_degenerate_multiplicity=False, r4_skin_in_the_game=False,
                      r5_graduated_response=False, r6_measurement_as_intervention=False,
                      r7_protected_self_correction=False)
        g = np.zeros(D)
        # concentrate all competence on the few "normal" dims -> HOT-style
        top = rng.choice(D, size=3, replace=False)
        g[top] = 3.0
        units = [Unit(rng=rng, genome=g, jurisdiction=np.ones(D, bool), id=0)]

    elif arch == ARCH_REDUNDANT:
        # K identical copies of the same optimized unit: redundancy, NOT
        # degeneracy. Copies cover the SAME dims, so they do not help
        # off-distribution.
        kern = Kernel(goal=goal,
                      r1_bounded_downside=True, r2_reversibility=True,
                      r3_degenerate_multiplicity=False, r4_skin_in_the_game=False,
                      r5_graduated_response=True, r6_measurement_as_intervention=False,
                      r7_protected_self_correction=True)
        g = np.zeros(D)
        top = rng.choice(D, size=3, replace=False)
        g[top] = 3.0
        units = [Unit(rng=rng, genome=g.copy(), jurisdiction=np.ones(D, bool), id=i)
                 for i in range(n_units)]

    else:  # ANTIFRAGILE
        # many heterogeneous units, overlapping partial jurisdictions, all 7
        # seed rules ON. Total competence is comparable to the others but
        # SPREAD across dims (degeneracy), so the ecology covers the whole space.
        kern = Kernel(goal=goal)  # all seed rules default True
        units = []
        for i in range(n_units):
            g = rng.random(D)
            g = g / g.sum() * 3.0 * 3  # comparable total competence per unit-group
            jur = np.ones(D, bool)
            off = rng.choice(D, size=D // 3, replace=False)
            jur[off] = False  # partial, overlapping jurisdictions
            units.append(Unit(rng=rng, genome=g, jurisdiction=jur, id=i))

    inst = Institution(arch=arch, rng=rng, kernel=kern, units=units, probes=probes)

    # seed some misaligned, alignment-faking units for the red-team (same count
    # for every architecture so the comparison is fair).
    n = min(seed_misaligned, len(inst.units))
    for i in range(n):
        inst.units[i].private_goal_shift = 0.4
        inst.units[i].fakes_under_observation = True
    return inst


# --------------------------------------------------------------------------- #
# Experiment A: Delta-sweep convexity test                                     #
# --------------------------------------------------------------------------- #
def _f_after_shock(arch, master_seed, delta, novel, n_react=8):
    """Build a FRESH institution + environment from a deterministic seed, apply a
    single shock of magnitude `delta` (novel or not), let the engine react for
    `n_react` steps (static architectures do not adapt), and return the resulting
    system-level performance f(state) and whether it hit the ruin state."""
    rng = np.random.default_rng(master_seed)
    inst = build_institution(arch, rng)
    env = Environment(rng=rng)
    env.demand = env.shock(delta, novel=novel)
    for t in range(n_react):
        inst.step(env, t)
        if inst.ruined:
            break
    return inst.f(env.demand), inst.ruined


def convexity_sweep(arch, deltas, n_seeds=40):
    """For each Delta, estimate the institution-level convexity heuristic
        H(Delta) = 1/2[f(a-Delta) + f(a+Delta)] - f(a)
    (Taleb & West 2023 [7]), applied to an INSTITUTION.

    Interpretation of the symmetric up/down probe:
      * baseline  f(a)      : performance in the normal regime, no shock.
      * 'down'   f(a-Delta) : a MILD, in-distribution shock of size Delta
                              (a bigger version of the normal regime).
      * 'up'     f(a+Delta) : a WILD, NOVEL (off-distribution) shock of the
                              SAME magnitude -- the case that separates
                              degeneracy from redundancy.

    H > 0  => the averaged perturbed outcome BEATS the calm baseline: the
              institution GAINS from volatility  -> antifragile (convex).
    H ~ 0  => insensitive                          -> robust (flat).
    H < 0  => volatility hurts on average          -> fragile (concave).

    We also return the ruin rate as the SEPARATE tail-robustness gate."""
    H = np.zeros((n_seeds, len(deltas)))
    ruin = np.zeros((n_seeds, len(deltas)))
    for s in range(n_seeds):
        # baseline institution for f(a): same seed family, zero shock.
        fa, _ = _f_after_shock(arch, 10_000 * s + 1, delta=0.0, novel=False)
        for di, delta in enumerate(deltas):
            # symmetric probe: mild (down) and wild-novel (up) of equal magnitude,
            # each from its own deterministic seed so results are reproducible.
            f_down, ruin_d = _f_after_shock(arch, 20_000 * s + 100 * di + 1,
                                            delta, novel=False)
            f_up, ruin_u = _f_after_shock(arch, 30_000 * s + 100 * di + 2,
                                          delta, novel=True)
            H[s, di] = 0.5 * (f_down + f_up) - fa
            ruin[s, di] = 1.0 if (ruin_d or ruin_u) else 0.0
    return H, ruin


# --------------------------------------------------------------------------- #
# Experiment B: longitudinal shock-stream                                      #
# --------------------------------------------------------------------------- #
def shock_stream(arch, n_steps=60, n_seeds=40):
    """Run each architecture through the SAME stream of escalating, occasionally
    novel shocks; record performance and the variety budget over time."""
    perf = np.zeros((n_seeds, n_steps))
    opt = np.zeros((n_seeds, n_steps))
    deg = np.zeros((n_seeds, n_steps))
    expo = np.zeros((n_seeds, n_steps))
    alive = np.zeros((n_seeds, n_steps))
    misalign = np.zeros(n_seeds)
    varcollapse = np.zeros(n_seeds)

    for s in range(n_seeds):
        rng = np.random.default_rng(777 * s + 3)
        inst = build_institution(arch, rng)
        env = Environment(rng=rng)
        for t in range(n_steps):
            # shock schedule: baseline drift + periodic novel shocks that grow
            delta = 0.15 + 0.010 * t
            novel = (t % 7 == 6)          # a genuinely novel shock every 7 steps
            if novel:
                env.demand = env.shock(min(delta * 1.6, 0.98), novel=True)
            else:
                env.demand = env.shock(delta, novel=False)
            inst.step(env, t)

            perf[s, t] = max(inst.f(env.demand), 0.0)
            vb = inst.variety_budget()
            opt[s, t] = vb["optionality"]
            deg[s, t] = vb["degeneracy"]
            expo[s, t] = vb["exposure_symmetry"]
            alive[s, t] = 0.0 if inst.ruined else 1.0
        misalign[s] = inst.misalignment_events
        varcollapse[s] = 1.0 if inst.variety_collapse_flag else 0.0

    return dict(perf=perf, opt=opt, deg=deg, expo=expo, alive=alive,
                misalign=misalign, varcollapse=varcollapse)


# --------------------------------------------------------------------------- #
# Experiment C: variety-collapse STRESS TEST                                   #
# --------------------------------------------------------------------------- #
def variety_collapse_stress(n_steps=50, n_seeds=50):
    """Deliberately create the conditions for silent variety-collapse: a LONG
    run under a STATIONARY regime, where naive selection drives every unit toward
    the same local optimum (the units converge -> degeneracy -> 0). This is the
    failure the report's critique flagged as the design's largest silent risk.

    We compare the antifragile design with the reflective tier's collapse-repair
    ON vs OFF (kernel rule r3), to test whether the detector actually prevents
    collapse -- a safety mechanism is only credible if we can watch it fire."""
    def run(repair_on):
        deg = np.zeros((n_seeds, n_steps))
        caught = np.zeros(n_seeds)
        for s in range(n_seeds):
            rng = np.random.default_rng(555 * s + 11)
            inst = build_institution(ARCH_ANTIFRAGILE, rng, seed_misaligned=0)
            inst.kernel.r3_degenerate_multiplicity = repair_on
            env = Environment(rng=rng)
            # stationary regime + a naive 'roll-the-winner-out' efficiency drive
            # that actively homogenises the population (the collapse driver).
            for t in range(n_steps):
                inst.step(env, t, mutation=0.03, convergent_pressure=True)
                deg[s, t] = inst.degeneracy()
            caught[s] = 1.0 if inst.variety_collapse_flag else 0.0
        return deg, caught

    deg_on, caught_on = run(True)
    deg_off, caught_off = run(False)
    return dict(deg_on=deg_on, deg_off=deg_off,
                caught_on=caught_on, caught_off=caught_off)


def _plot_collapse(cs):
    plt.figure(figsize=(9, 5))
    m_off = cs["deg_off"].mean(0); sd_off = cs["deg_off"].std(0)
    m_on = cs["deg_on"].mean(0); sd_on = cs["deg_on"].std(0)
    x = np.arange(len(m_off))
    plt.plot(x, m_off, color="#c0392b", lw=2,
             label=f"reflective tier OFF (r3 disabled) - collapses")
    plt.fill_between(x, m_off - sd_off, m_off + sd_off, color="#c0392b", alpha=0.12)
    plt.plot(x, m_on, color="#27ae60", lw=2,
             label=f"reflective tier ON (r3) - repaired, caught in "
                   f"{cs['caught_on'].mean()*100:.0f}% of runs")
    plt.fill_between(x, m_on - sd_on, m_on + sd_on, color="#27ae60", alpha=0.12)
    plt.axhline(0.15, color="k", ls="--", lw=1, alpha=0.7)
    plt.text(1, 0.16, "collapse-detection floor (0.15)", fontsize=8)
    plt.title("Fig 6 - Variety-collapse stress test (stationary regime,\n"
              "pure convergent selection pressure)\n"
              "Does the reflective tier detect & repair silent variety loss?",
              fontsize=10.5)
    plt.xlabel("Time step")
    plt.ylabel("Degeneracy (structural diversity)")
    plt.ylim(-0.03, 1.0)
    plt.legend(fontsize=9)
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig("figures/fig6_variety_collapse.png", dpi=130)
    plt.close()


# --------------------------------------------------------------------------- #
# Runner + plots                                                               #
# --------------------------------------------------------------------------- #
def main():
    archs = [ARCH_MONO, ARCH_REDUNDANT, ARCH_ANTIFRAGILE]
    deltas = np.linspace(0.05, 0.95, 10)
    N_SEEDS = 50

    print("=== Experiment A: Delta-sweep convexity test ===")
    convex = {}
    for a in archs:
        H, ruin = convexity_sweep(a, deltas, n_seeds=N_SEEDS)
        convex[a] = dict(H_mean=H.mean(0), H_sd=H.std(0),
                         ruin_rate=ruin.mean(0))
        # classify overall convexity by the sign of mean H and its trend
        mean_H = H.mean()
        trend = np.polyfit(deltas, H.mean(0), 1)[0]
        cls = ("antifragile (convex)" if mean_H > 0.005 else
               "fragile (concave)" if mean_H < -0.005 else "robust (flat)")
        print(f"  {a:12s}: mean H = {mean_H:+.4f}, dH/dDelta = {trend:+.4f}, "
              f"ruin@maxDelta = {ruin.mean(0)[-1]:.2f}  -> {cls}")

    # write convexity CSV
    with open("results/convexity.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["architecture", "delta", "H_mean", "H_sd", "ruin_rate"])
        for a in archs:
            for i, d in enumerate(deltas):
                w.writerow([a, f"{d:.3f}",
                            f"{convex[a]['H_mean'][i]:.5f}",
                            f"{convex[a]['H_sd'][i]:.5f}",
                            f"{convex[a]['ruin_rate'][i]:.3f}"])

    print("\n=== Experiment B: longitudinal shock-stream ===")
    ts = {}
    for a in archs:
        ts[a] = shock_stream(a, n_steps=60, n_seeds=N_SEEDS)
        final_perf = ts[a]["perf"][:, -1].mean()
        surv = ts[a]["alive"][:, -1].mean()
        print(f"  {a:12s}: final perf = {final_perf:.3f}, "
              f"survival = {surv:.2f}, "
              f"final degeneracy = {ts[a]['deg'][:, -1].mean():.3f}, "
              f"misalign events = {ts[a]['misalign'].mean():.2f}, "
              f"variety-collapse triggered = {ts[a]['varcollapse'].mean():.2f}")

    # write timeseries CSV (means)
    with open("results/timeseries.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["architecture", "step", "perf_mean", "optionality_mean",
                    "degeneracy_mean", "exposure_mean", "survival_rate"])
        for a in archs:
            T = ts[a]["perf"].shape[1]
            for t in range(T):
                w.writerow([a, t,
                            f"{ts[a]['perf'][:, t].mean():.4f}",
                            f"{ts[a]['opt'][:, t].mean():.4f}",
                            f"{ts[a]['deg'][:, t].mean():.4f}",
                            f"{ts[a]['expo'][:, t].mean():.4f}",
                            f"{ts[a]['alive'][:, t].mean():.4f}"])

    # red-team JSON
    redteam = {a: dict(
        misalign_events_mean=float(ts[a]["misalign"].mean()),
        variety_collapse_rate=float(ts[a]["varcollapse"].mean()),
        final_survival=float(ts[a]["alive"][:, -1].mean()),
        mean_H=float(convex[a]["H_mean"].mean()),
        ruin_rate_maxdelta=float(convex[a]["ruin_rate"][-1]),
    ) for a in archs}
    with open("results/redteam.json", "w") as fh:
        json.dump(redteam, fh, indent=2)

    print("\n=== Experiment C: variety-collapse stress test ===")
    cs = variety_collapse_stress(n_steps=50, n_seeds=N_SEEDS)
    print(f"  reflective tier OFF: final degeneracy = {cs['deg_off'][:, -1].mean():.3f} "
          f"(collapsed toward 0)")
    print(f"  reflective tier ON : final degeneracy = {cs['deg_on'][:, -1].mean():.3f}, "
          f"collapse detected & repaired in {cs['caught_on'].mean()*100:.0f}% of runs")
    redteam["variety_collapse_stress"] = dict(
        final_degeneracy_repair_off=float(cs["deg_off"][:, -1].mean()),
        final_degeneracy_repair_on=float(cs["deg_on"][:, -1].mean()),
        detector_fire_rate=float(cs["caught_on"].mean()),
    )
    with open("results/redteam.json", "w") as fh:
        json.dump(redteam, fh, indent=2)

    # ------------------------------------------------------------------ plots
    _plot_convexity(archs, deltas, convex)
    _plot_timeseries(archs, ts)
    _plot_variety_budget(archs, ts)
    _plot_redteam(archs, redteam)
    _plot_survival(archs, ts)
    _plot_collapse(cs)
    print("\nWrote results/ and figures/. Done.")
    return convex, ts, redteam, cs


def _plot_convexity(archs, deltas, convex):
    plt.figure(figsize=(9, 5.5))
    for a in archs:
        plt.plot(deltas, convex[a]["H_mean"], "o-", color=COLORS[a], label=LABELS[a])
        plt.fill_between(deltas,
                         convex[a]["H_mean"] - convex[a]["H_sd"],
                         convex[a]["H_mean"] + convex[a]["H_sd"],
                         color=COLORS[a], alpha=0.12)
    plt.axhline(0, color="k", lw=1, ls="--", alpha=0.7)
    plt.text(0.06, 0.002, "H = 0  (robust)", fontsize=8, va="bottom")
    plt.title("Fig 1 - Institution-level convexity  H(Δ) = ½[f(a−Δ)+f(a+Δ)] − f(a)\n"
              "H>0 antifragile · H=0 robust · H<0 fragile", fontsize=11)
    plt.xlabel("Shock magnitude  Δ")
    plt.ylabel("H  (convexity of response)")
    plt.legend(fontsize=9)
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig("figures/fig1_convexity.png", dpi=130)
    plt.close()


def _plot_timeseries(archs, ts):
    plt.figure(figsize=(9, 5.5))
    for a in archs:
        m = ts[a]["perf"].mean(0)
        sd = ts[a]["perf"].std(0)
        x = np.arange(len(m))
        plt.plot(x, m, color=COLORS[a], label=LABELS[a], lw=2)
        plt.fill_between(x, m - sd, m + sd, color=COLORS[a], alpha=0.12)
    # mark novel-shock steps
    for t in range(6, 60, 7):
        plt.axvline(t, color="grey", ls=":", alpha=0.35)
    plt.title("Fig 2 - Performance under an escalating shock stream\n"
              "(dotted lines = novel, off-distribution shocks)", fontsize=11)
    plt.xlabel("Time step")
    plt.ylabel("System performance  f(state)")
    plt.legend(fontsize=9)
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig("figures/fig2_timeseries.png", dpi=130)
    plt.close()


def _plot_variety_budget(archs, ts):
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
    metrics = [("deg", "Degeneracy (structural diversity)"),
               ("opt", "Optionality (# distinct variants)"),
               ("expo", "Exposure symmetry")]
    for ax, (key, title) in zip(axes, metrics):
        for a in archs:
            m = ts[a][key].mean(0)
            ax.plot(np.arange(len(m)), m, color=COLORS[a], lw=2, label=a)
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("Time step")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("value")
    axes[0].legend(fontsize=8)
    fig.suptitle("Fig 3 - Variety-budget vital signs over time "
                 "(optionality · reversibility-driven · exposure symmetry)",
                 fontsize=11)
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.savefig("figures/fig3_variety_budget.png", dpi=130)
    plt.close()


def _plot_redteam(archs, redteam):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    x = np.arange(len(archs))
    # misalignment events
    vals = [redteam[a]["misalign_events_mean"] for a in archs]
    axes[0].bar(x, vals, color=[COLORS[a] for a in archs])
    axes[0].set_xticks(x); axes[0].set_xticklabels([a for a in archs], rotation=12, fontsize=8)
    axes[0].set_title("Red-team: uncaught misalignment events\n(alignment-faking left unchecked)", fontsize=10)
    axes[0].set_ylabel("mean events / run")
    axes[0].grid(alpha=0.2, axis="y")
    # variety-collapse trigger rate
    vals2 = [redteam[a]["variety_collapse_rate"] for a in archs]
    axes[1].bar(x, vals2, color=[COLORS[a] for a in archs])
    axes[1].set_xticks(x); axes[1].set_xticklabels([a for a in archs], rotation=12, fontsize=8)
    axes[1].set_title("Red-team: silent variety-collapse\n(fraction of runs the reflective tier caught & repaired)", fontsize=10)
    axes[1].set_ylabel("fraction of runs")
    axes[1].grid(alpha=0.2, axis="y")
    fig.suptitle("Fig 4 - Red-team outcomes for the two flagged failure modes", fontsize=11)
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.savefig("figures/fig4_redteam.png", dpi=130)
    plt.close()


def _plot_survival(archs, ts):
    plt.figure(figsize=(9, 5))
    for a in archs:
        m = ts[a]["alive"].mean(0)
        plt.plot(np.arange(len(m)), m, color=COLORS[a], lw=2, label=LABELS[a])
    plt.title("Fig 5 - Survival (tail-robustness gate)\n"
              "fraction of runs not yet in the absorbing 'ruin' state\n"
              "[Taleb & West 2023: local convexity is necessary but NOT sufficient]",
              fontsize=10.5)
    plt.xlabel("Time step")
    plt.ylabel("survival rate")
    plt.ylim(-0.03, 1.03)
    plt.legend(fontsize=9)
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig("figures/fig5_survival.png", dpi=130)
    plt.close()


if __name__ == "__main__":
    main()
