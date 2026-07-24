"""Bench 2 (x) 3 — TIME: the contextual fraction of DYNAMICS.

The dial, applied to the play itself. Contexts here are not spatial
arrangements of measurements but TEMPORAL ones: a single qubit precesses,
and we measure it at two of three times {t1, t2, t3}. Each pair of times is
a context; the question 'is there a global section?' becomes 'is there a
joint distribution over definite TRAJECTORIES q1, q2, q3 reproducing every
context?' — Leggett-Garg's macrorealism, run through the sheaf machinery.

Claims checked (empirical model computed by direct density-matrix
simulation of the measure-evolve-measure protocol, not from formulas):

(1) Marginals agree across contexts (no-signaling in time) — the model is
    a well-formed presheaf; the only question is gluing.
(2) The LP dial prices the dynamics: CF(theta) matches the exact 3-cycle
    law max(0, (LG - 1)/2), LG = the largest of the four odd-sign
    Leggett-Garg facets (e.g. <Q1Q2> + <Q2Q3> - <Q1Q3>), to 1e-6 across
    the sweep; CF = 0 in the scripted region, CF = 1/4 exactly at
    theta = pi/3 — one quarter of the precessing qubit's temporal behavior
    cannot be simulated by ANY mixture of definite histories.
(3) Decoherence is the dial's enemy, with an exact threshold — and the
    bench corrected its builder here. Dephasing between measurements does
    NOT touch the adjacent-time correlations (those are population terms);
    it only degrades the skip-the-middle context, c13 = cos^2(theta)
    - eta*sin^2(theta). Hence at theta = pi/3 the exact dial law is
    CF(eta) = max(0, 3(eta - 1/3)/8), and the resource dies at eta* = 1/3
    exactly — located by LP bisection to 1e-6, against the builder's wrong
    first guess. Coherence needs to survive only the UNMEASURED stretch.

Honesty clause: as always with Leggett-Garg, the experimental reading needs
the noninvasive-measurability assumption (the 'clumsiness' loophole); the
mathematical statement — no joint trajectory law reproduces the model —
is exact and is what the LP prices.

Status: exact (LP + closed forms agree; model from simulation).
"""
import numpy as np
from itertools import product as iproduct
from scipy.optimize import linprog

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PROJ = {+1: (I2 + Z) / 2, -1: (I2 - Z) / 2}


def evolve(rho, theta, eta):
    U = np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * X
    rho = U @ rho @ U.conj().T
    off = rho - np.diag(np.diag(rho))
    return np.diag(np.diag(rho)) + eta * off        # z-dephasing strength eta


def model(theta, eta):
    """Empirical model: contexts {12},{23},{13}; P(q_a, q_b) by simulation."""
    out = {}
    for (a, b), steps_before, steps_between in [((1, 2), 0, 1), ((2, 3), 1, 1),
                                                ((1, 3), 0, 2)]:
        table = {}
        for qa, qb in iproduct([+1, -1], repeat=2):
            rho = I2 / 2
            for _ in range(steps_before):
                rho = evolve(rho, theta, eta)
            p_a = float(np.real(np.trace(PROJ[qa] @ rho)))
            rho = PROJ[qa] @ rho @ PROJ[qa]
            rho = rho / max(np.real(np.trace(rho)), 1e-15)
            for _ in range(steps_between):
                rho = evolve(rho, theta, eta)
            p_b = float(np.real(np.trace(PROJ[qb] @ rho)))
            table[(qa, qb)] = p_a * p_b
        out[(a, b)] = table
    return out


def cf_lp(m):
    assignments = list(iproduct([+1, -1], repeat=3))
    rows, caps = [], []
    for (a, b), table in m.items():
        for o, e in table.items():
            rows.append([1.0 if (g[a - 1], g[b - 1]) == o else 0.0
                         for g in assignments])
            caps.append(e)
    res = linprog(c=[-1.0] * 8, A_ub=np.array(rows), b_ub=np.array(caps),
                  bounds=[(0, None)] * 8, method="highs")
    assert res.status == 0
    return max(0.0, 1.0 + res.fun)


def corr(table):
    return sum(qa * qb * p for (qa, qb), p in table.items())


def K3(m):
    return corr(m[(1, 2)]) + corr(m[(2, 3)]) - corr(m[(1, 3)])


def lg_max(m):
    """Max over the four odd-sign 3-cycle (Leggett-Garg) facets."""
    c12, c23, c13 = corr(m[(1, 2)]), corr(m[(2, 3)]), corr(m[(1, 3)])
    return max(c12 + c23 - c13, c12 - c23 + c13,
               -c12 + c23 + c13, -c12 - c23 - c13)


def demonstrate(say):
    # (1) presheaf well-formedness: marginals agree across contexts
    m = model(np.pi / 3, 1.0)
    p2_from12 = sum(m[(1, 2)][(q1, +1)] for q1 in (+1, -1))
    p2_from23 = sum(m[(2, 3)][(+1, q3)] for q3 in (+1, -1))
    assert abs(p2_from12 - p2_from23) < 1e-12
    say("  temporal contexts {t1t2},{t2t3},{t1t3} from direct simulation;")
    say("  no-signaling in time verified — a well-formed presheaf over histories.")

    # (2) the dial over precession angle
    line = []
    for theta in [0.4, np.pi / 3, 1.6, 2.2, 2.8]:
        mm = model(theta, 1.0)
        cf = cf_lp(mm)
        predicted = max(0.0, (lg_max(mm) - 1.0) / 2.0)
        assert abs(cf - predicted) < 1e-6
        line.append(f"theta={theta:.2f}: CF={cf:.4f}")
    say("  the dial over the dynamics: " + "   ".join(line))
    cf_star = cf_lp(model(np.pi / 3, 1.0))
    assert abs(cf_star - 0.25) < 1e-9
    say(f"  exact 3-cycle law CF = max(0,(LG-1)/2), LG over all four facets,")
    say(f"  matched to 1e-6 everywhere;")
    say(f"  peak CF = {cf_star:.6f} = 1/4 at theta = pi/3: one quarter of the")
    say(f"  precessing qubit's temporal behavior is unscriptable by trajectories.")

    # (3) decoherence: exact dial law and threshold by LP
    for eta in [0.4, 0.6, 0.8, 1.0]:
        cf = cf_lp(model(np.pi / 3, eta))
        assert abs(cf - max(0.0, 3 * (eta - 1 / 3) / 8)) < 1e-9
    lo, hi = 0.05, 1.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if cf_lp(model(np.pi / 3, mid)) > 1e-12:
            hi = mid
        else:
            lo = mid
    eta_star = (lo + hi) / 2
    say(f"  dephasing dial law CF(eta) = 3(eta - 1/3)/8 verified by LP;")
    say(f"  the resource dies at eta* = {eta_star:.6f} (exactly 1/3) — dephasing")
    say(f"  never touches adjacent-time correlations, only the unmeasured stretch;")
    say(f"  the builder's first guess (sqrt(3)-1) was WRONG and the bench said so.")
    assert abs(eta_star - 1 / 3) < 1e-6
    say("  moral: histories, not just tables, refuse gluing — and the refusal")
    say("         is priced. The play is unscripted by a measured fraction,")
    say("         and decoherence buys the script back at a known, exact rate.")


if __name__ == "__main__":
    demonstrate(print)
