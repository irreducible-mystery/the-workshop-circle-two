#!/usr/bin/env python3
"""
antifragile_sim.py
==================
A sandboxed multi-agent simulation of the three-layer governance design proposed
in Antifragile_Systems_Report.md:

    Layer 1  KERNEL   - a protected minimal constitution (7 seed rules) + an
                        amendment gate (super-majority threshold + time-delay).
    Layer 2  ARENA    - a polycentric ecology of N human-AI UNITS with
                        overlapping jurisdictions and heterogeneous "genomes".
    Layer 3  ENGINE   - evolution by portfolio of reversible experiments:
                        VARY -> SELECT-under-exposure -> RETAIN-with-degeneracy,
                        plus a protected REFLECTIVE tier that watches for drift.

The purpose is NOT to prove the design works. It is to TEST it: to inject shocks
of tunable magnitude Delta and measure whether the institution's performance
responds CONVEXLY (antifragile), FLATLY (robust) or CONCAVELY (fragile), and to
red-team it for the two failure modes the report's critique flagged as its
largest risks: evolution-selects-misalignment and silent variety-collapse.

Three architectures are compared on identical shock streams:
    MONOCULTURE  - one optimized unit, no degeneracy, tight coupling.
    REDUNDANT    - K identical copies (redundancy, not degeneracy).
    ANTIFRAGILE  - the full three-layer design (degeneracy + engine + kernel).

Key measured quantities
-----------------------
  f(state)            system-level performance functional (task success under
                      the *current* environment, net of variety-maintenance cost).
  H(Delta)            = 1/2[f(a-Delta) + f(a+Delta)] - f(a), the Taleb convexity
                      heuristic evaluated at the INSTITUTION level over a shock of
                      size Delta. H>0 antifragile, H=0 robust, H<0 fragile.
  survival / ruin     tail-robustness gate (Taleb & West 2023 [7]): local
                      convexity is necessary but NOT sufficient; a design that is
                      locally convex but hits an absorbing "ruin" state is not
                      globally antifragile. Tracked separately from H.
  variety budget      three vital signs from the report:
                        optionality        = # of live, structurally-distinct
                                              variants per critical function
                        reversibility      = fraction of commitments cheaply undoable
                        exposure_symmetry  = correlation between who-decides and
                                              who-bears-the-downside
  degeneracy          operational "structurally different" distance = mean
                      pairwise behavioural DISAGREEMENT on a held-out probe set
                      (0 = identical/redundant, 1 = maximally diverse).
  misalignment        red-team: fraction of the population whose *private* goal
                      diverges from the kernel goal but which behaves compliantly
                      *under observation* (alignment-faking analogue).

This file defines the model and a single-run API. Experiments (Delta-sweep,
multi-seed, plotting) live in run_experiments.py.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field, replace
from typing import Callable

# --------------------------------------------------------------------------- #
# Environment                                                                  #
# --------------------------------------------------------------------------- #
# The "world" a unit must handle is a demand vector over D task-dimensions.
# A unit's genome is a competence vector over the same D dimensions. Task
# success = how well the ecology's available competence covers current demand.
# A SHOCK rotates/reshapes the demand vector: a *novel* shock pushes demand into
# a region no unit was optimized for -- this is where degeneracy pays off,
# because structurally-different units cover different regions.

D = 12  # number of task dimensions


@dataclass
class Environment:
    rng: np.random.Generator
    demand: np.ndarray = None          # current demand over D dims (nonneg, sums~1)
    base_demand: np.ndarray = None     # the "normal" regime demand

    def __post_init__(self):
        if self.base_demand is None:
            v = self.rng.random(D)
            v = v / v.sum()
            self.base_demand = v
        if self.demand is None:
            self.demand = self.base_demand.copy()

    def shock(self, delta: float, novel: bool):
        """Apply a shock of magnitude `delta` in [0,1+].
        novel=True  -> push demand toward a *previously-unseen* dimension mix
                       (off-distribution; the hard case).
        novel=False -> amplify existing dominant demand (in-distribution).
        Returns a NEW demand vector (does not mutate self).
        """
        if novel:
            # target a random *sparse* corner of demand space the units did not
            # optimize for -> concentrate demand on 1-2 dims chosen at random.
            target = np.zeros(D)
            idx = self.rng.choice(D, size=self.rng.integers(1, 3), replace=False)
            target[idx] = 1.0
            target = target / target.sum()
        else:
            # amplify the currently-dominant dims (a "bigger version of normal")
            target = self.base_demand ** 2
            target = target / target.sum()
        new = (1 - delta) * self.base_demand + delta * target
        new = np.clip(new, 0, None)
        new = new / new.sum()
        return new


# --------------------------------------------------------------------------- #
# Units (agents)                                                               #
# --------------------------------------------------------------------------- #
@dataclass
class Unit:
    rng: np.random.Generator
    genome: np.ndarray                 # competence over D dims (nonneg)
    jurisdiction: np.ndarray           # boolean mask: which dims this unit may act on
    # --- red-team internals ---
    private_goal_shift: float = 0.0    # >0 => this unit privately wants to drift
                                       #        from the kernel goal (misalignment seed)
    fakes_under_observation: bool = False  # alignment-faking disposition
    # --- bookkeeping ---
    resources: float = 1.0
    id: int = -1

    def capability(self) -> np.ndarray:
        """Effective competence, restricted to this unit's jurisdiction."""
        return self.genome * self.jurisdiction

    def behaviour_signature(self, probes: np.ndarray) -> np.ndarray:
        """Deterministic action on a held-out probe set, used to MEASURE how
        *structurally different* two units are (degeneracy metric).
        Each probe is a demand-like vector; the unit's 'action' is the argmax
        dimension of (capability . probe-weighting)."""
        cap = self.capability()
        acts = []
        for p in probes:
            score = cap * p
            acts.append(int(np.argmax(score)) if score.sum() > 0 else -1)
        return np.array(acts)


# --------------------------------------------------------------------------- #
# Kernel (Layer 1): protected constitution + amendment gate                    #
# --------------------------------------------------------------------------- #
@dataclass
class Kernel:
    """The 7 seed rules are enforced as INVARIANTS on the engine's operators.
    The kernel itself is 'sticky': an amendment needs a super-majority AND must
    survive a mandatory time-delay (cooling-off) of `delay` steps before it
    takes effect. This models seed rule 7 (protected self-correction)."""
    goal: np.ndarray                    # the invariant the whole system serves
    amend_threshold: float = 0.80       # super-majority fraction required
    amend_delay: int = 5                # cooling-off steps
    # seed-rule toggles (all True in the ANTIFRAGILE design)
    r1_bounded_downside: bool = True
    r2_reversibility: bool = True
    r3_degenerate_multiplicity: bool = True
    r4_skin_in_the_game: bool = True
    r5_graduated_response: bool = True
    r6_measurement_as_intervention: bool = True
    r7_protected_self_correction: bool = True

    _pending: list = field(default_factory=list)  # (activate_step, change)

    def max_step_size(self, base: float) -> float:
        """Seed rule 1: bounded downside caps how large any single experiment's
        blast radius may be."""
        return base if self.r1_bounded_downside else base * 6.0

    def reversible_fraction(self) -> float:
        """Seed rule 2: reversibility-first -> most commitments are undoable."""
        return 0.9 if self.r2_reversibility else 0.15


# --------------------------------------------------------------------------- #
# Institution (the whole three-layer system)                                   #
# --------------------------------------------------------------------------- #
ARCH_MONO = "monoculture"
ARCH_REDUNDANT = "redundant"
ARCH_ANTIFRAGILE = "antifragile"


@dataclass
class Institution:
    arch: str
    rng: np.random.Generator
    kernel: Kernel
    units: list                        # list[Unit]
    probes: np.ndarray                 # held-out probe set for degeneracy metric
    variety_cost_rate: float = 0.010   # cost per unit of maintained optionality
    ruin_threshold: float = 0.18       # if f drops below this, system is "ruined"
    # history
    ruined: bool = False
    misalignment_events: int = 0
    variety_collapse_flag: bool = False

    # -- performance functional f(state) ----------------------------------- #
    def coverage(self, demand: np.ndarray) -> float:
        """How well the ECOLOGY covers current demand. For each demand dim, take
        the BEST unit's competence on that dim (degenerate units cover different
        dims, so the max-over-units is high even off-distribution)."""
        if not self.units:
            return 0.0
        caps = np.stack([u.capability() for u in self.units])   # (U, D)
        best_per_dim = caps.max(axis=0)                          # (D,)
        # normalise competence to [0,1] softly
        best_per_dim = best_per_dim / (best_per_dim.max() + 1e-9)
        return float(np.dot(demand, best_per_dim))

    def variety_maintenance_cost(self) -> float:
        """Degeneracy/slack is not free (Counterevidence: competition selects
        against antifragility). Cost scales with optionality actually held."""
        return self.variety_cost_rate * self.optionality()

    def f(self, demand: np.ndarray) -> float:
        """System-level performance = task coverage minus the standing cost of
        the variety it maintains. This is the functional whose convexity we test."""
        perf = self.coverage(demand)
        cost = self.variety_maintenance_cost()
        val = perf - cost
        return float(val)

    # -- variety-budget vital signs ---------------------------------------- #
    def optionality(self) -> float:
        """# of live, STRUCTURALLY-DISTINCT variants (mean over functions).
        Implemented as effective number of distinct behaviour signatures."""
        if len(self.units) <= 1:
            return 1.0
        sigs = [tuple(u.behaviour_signature(self.probes)) for u in self.units]
        distinct = len(set(sigs))
        return float(distinct)

    def degeneracy(self) -> float:
        """Operational 'structurally different' distance: mean pairwise
        behavioural DISAGREEMENT on the held-out probe set. 0 = redundant copies,
        ->1 = maximally diverse."""
        if len(self.units) <= 1:
            return 0.0
        sigs = np.stack([u.behaviour_signature(self.probes) for u in self.units])
        U = len(self.units)
        diffs = []
        for i in range(U):
            for j in range(i + 1, U):
                diffs.append(np.mean(sigs[i] != sigs[j]))
        return float(np.mean(diffs)) if diffs else 0.0

    def reversibility(self) -> float:
        return self.kernel.reversible_fraction()

    def exposure_symmetry(self) -> float:
        """Seed rule 4: does whoever decides bear the downside? In the
        antifragile design decisions are local (unit decides on its own
        jurisdiction) so exposure is high; in a monoculture a central planner
        decides for everyone, so exposure is low."""
        if self.arch == ARCH_MONO:
            return 0.15
        if self.arch == ARCH_REDUNDANT:
            return 0.35
        return 0.9 if self.kernel.r4_skin_in_the_game else 0.3

    def variety_budget(self) -> dict:
        return {
            "optionality": self.optionality(),
            "reversibility": self.reversibility(),
            "exposure_symmetry": self.exposure_symmetry(),
            "degeneracy": self.degeneracy(),
        }

    # -- the ENGINE: vary / select / retain -------------------------------- #
    def step(self, env: Environment, step_idx: int, mutation: float = 0.06,
             convergent_pressure: bool = False):
        """One tick of the evolutionary engine under the CURRENT demand.
        Only the ANTIFRAGILE architecture runs a full vary/select/retain loop;
        MONO and REDUNDANT are static (that is the point of the comparison)."""
        if self.ruined:
            return

        # kernel amendment cooling-off (protected self-correction)
        self.kernel._pending = [(s, c) for (s, c) in self.kernel._pending if s > step_idx]

        if self.arch != ARCH_ANTIFRAGILE:
            # static architectures: no adaptation, no variety generation.
            # (Redundant units may still be knocked out by shocks; mono is one unit.)
            # BUT the misalignment monitor runs for everyone (apples-to-apples):
            # mono/redundant have r6/r7 off, so their fakers are simply never caught.
            self._reflect(env.demand)
            self._maybe_ruin(env)
            return

        demand = env.demand
        base_step = self.kernel.max_step_size(mutation)

        # ---- VARIATION: each unit proposes a bounded, reversible variant ---- #
        proposals = []
        for u in self.units:
            variant = u.genome.copy()
            # mutate a few dims within jurisdiction, sized by kernel bound (r1)
            k = self.rng.integers(1, 3)
            dims = self.rng.choice(D, size=k, replace=False)
            variant[dims] += self.rng.normal(0, base_step, size=k)
            variant = np.clip(variant, 0, None)
            proposals.append((u, variant))

        # ---- SELECTION under exposure --------------------------------------- #
        # A variant is adopted only if it improves that unit's LOCAL coverage of
        # current demand (skin in the game, r4). Bounded downside (r1) means a
        # bad variant is cheaply reverted (r2) rather than catastrophic.
        for u, variant in proposals:
            old_local = float(np.dot(demand, (u.genome * u.jurisdiction)))
            new_local = float(np.dot(demand, (variant * u.jurisdiction)))
            # measurement-as-intervention (r6): selection uses a PLURAL, noisy,
            # rotated signal so it cannot be gamed into a single proxy.
            noise = self.rng.normal(0, 0.02) if self.kernel.r6_measurement_as_intervention else 0.0
            if new_local + noise > old_local:
                u.genome = variant
            elif not self.kernel.r2_reversibility:
                # without reversibility the bad variant sticks (fragility)
                u.genome = variant

        # ---- CONVERGENT PRESSURE (the collapse driver) ---------------------- #
        # A naive efficiency drive would 'roll the winner out to everyone':
        # copy the best-performing unit's genome AND jurisdiction across the
        # population. This is the exact HOT-fragility anti-pattern the report
        # warns against -- it maximises short-run coverage while destroying
        # variety. We only apply it in the stress test.
        if convergent_pressure:
            demand_now = env.demand
            scores = [float(np.dot(demand_now, u.capability())) for u in self.units]
            best = int(np.argmax(scores))
            bg = self.units[best].genome.copy()
            bj = self.units[best].jurisdiction.copy()
            for u in self.units:
                if u is self.units[best]:
                    continue
                # move each unit a large fraction toward the winner (rollout)
                u.genome = 0.4 * u.genome + 0.6 * bg
                # and, crucially, homogenise jurisdictions -> signatures converge
                u.jurisdiction = bj.copy()

        # ---- RETENTION with degeneracy -------------------------------------- #
        # Do NOT roll a winner out to everyone (that destroys variety -> HOT
        # fragility). Instead, if degeneracy collapses below a floor, the
        # reflective tier INJECTS a structurally-different unit to restore the
        # variety budget. This is the anti-monoculture rule (r3).
        if self.kernel.r3_degenerate_multiplicity:
            if self.degeneracy() < 0.15:
                self.variety_collapse_flag = True
                self._inject_diverse_unit()
        # ---- REFLECTIVE tier: red-team monitors -------------------------- #
        self._reflect(demand)
        self._maybe_ruin(env)

    def _inject_diverse_unit(self):
        """Reflective tier restores optionality by adding a unit whose genome is
        deliberately anti-correlated with the current population mean."""
        caps = np.stack([u.capability() for u in self.units])
        mean_cap = caps.mean(axis=0)
        # new genome favours the *least-covered* dims
        inv = 1.0 / (mean_cap + 0.1)
        g = inv / inv.sum() * D * 0.5
        jur = np.ones(D, dtype=bool)
        # weaken a random subset of jurisdiction to keep units partial/overlapping
        off = self.rng.choice(D, size=D // 3, replace=False)
        jur[off] = False
        nu = Unit(rng=self.rng, genome=g, jurisdiction=jur,
                  id=len(self.units) + 1000)
        self.units.append(nu)

    def _reflect(self, demand):
        """Protected reflective tier: detect alignment-faking / misalignment.
        A unit with a private_goal_shift that FAKES compliance under observation
        will look fine on the standard (predictable) metric but be caught by the
        r6 unpredictable non-commuting audit with some probability.

        NOTE: this is called every step for EVERY architecture (see step()),
        so the misalignment accounting is apples-to-apples. Architectures whose
        kernel has r6 OFF simply never catch the faker."""
        for u in self.units:
            if u.private_goal_shift > 0 and u.fakes_under_observation:
                if self.kernel.r6_measurement_as_intervention and self.kernel.r7_protected_self_correction:
                    # unpredictable audit basis -> catch with prob ~ audit power
                    caught = self.rng.random() < 0.6
                    if caught:
                        # graduated response (r5): nudge the unit back, don't nuke it
                        u.private_goal_shift *= 0.5
                        if u.private_goal_shift < 0.05:
                            u.private_goal_shift = 0.0
                            u.fakes_under_observation = False
                    else:
                        self.misalignment_events += 1
                else:
                    # fixed/absent oversight -> faker is never caught, every step
                    self.misalignment_events += 1

    def _maybe_ruin(self, env):
        """Tail-robustness gate (Taleb & West 2023 [7]): if current performance
        falls below the ruin threshold, the system enters an ABSORBING failed
        state. Local convexity does not save a system that crosses into ruin."""
        if self.f(env.demand) < self.ruin_threshold:
            # bounded downside (r1) gives a grace buffer; without it, ruin is
            # immediate and permanent.
            if self.kernel.r1_bounded_downside and self.rng.random() < 0.5:
                return  # absorbed this time
            self.ruined = True
