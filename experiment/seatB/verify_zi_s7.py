#!/usr/bin/env python3
"""SEAT B — blind exact reimplementation of the S7 statements
(Zi_statements_v8.txt), statements only.

The S7a slice lemma, over the units of Z[i].

ROUTE, INDEPENDENT OF SEAT P'S (charge §5.3 requires it). Seat P could
not brute-force: 4^8 = 65536 cochains is far outside `decide`'s kernel
budget, so seat P proved the lemma STRUCTURALLY — an explicit gauge read
off the cochain's own values, plus a parametrization of the cocycles by
three units, plus small `decide` nests over 64 triples and 4-fold gauge
sweeps.

Seat B does the thing seat P could not: DIRECT EXHAUSTION. All 65536
unit-valued cochains are enumerated, the cocycles among them found by
running all 16 pentagon instances, the 256 gauges applied to build the
orbits, and the orbit partition computed outright. The counts 32 / 16 / 2
and the slice lemma itself then fall out of the partition, with no
appeal to seat P's parametrization, witnesses, or nests. Only after
that is seat P's claimed structure checked AGAINST the exhaustion.

Exact arithmetic throughout (F1): Gaussian integers as (re, im) pairs.
No floats, no exponent encodings — units are the ring elements
themselves, so the check is over the same objects the kernel states.

Definitions transcribed from statements v8 ALONE (isUnit, unitCochain,
cocycle3, Fnorm, detaNum, detaDen, sliceGauge, cochainOf, unitsZi,
slotList, cocycleTriples, gaugeFn, cobVec, cobReps, controlCochainA, and
the S3 defs Fz2/pentL/pentR/pentagon they reference). Blindness boundary
held: no proof body was read.
"""
import itertools
import sys

CHECKS = []


def check(name, ok, note=""):
    CHECKS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {note}" if note else ""))


# ── exact Gaussian integers ─────────────────────────────────────────────────
def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gconj(z):
    return (z[0], -z[1])


def normSq(z):
    return z[0] * z[0] + z[1] * z[1]


G_ZERO, G_ONE, G_I = (0, 0), (1, 0), (0, 1)
G_MONE, G_MI = (-1, 0), (0, -1)

# `unitsZi` — transcribed
UNITS = [G_ONE, G_I, G_MONE, G_MI]
# `slotList` — transcribed
SLOTS = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
         (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
PAIRS = list(itertools.product((0, 1), repeat=2))
QUADS = list(itertools.product((0, 1), repeat=4))


def isUnit(z):
    return normSq(z) == 1


# ── the S7 defs, transcribed from statements v8 ─────────────────────────────
def cocycle_instance(F, a, b, c, d):
    """the body of `cocycle3`, one quadruple"""
    lhs = gmul(gmul(F[(b, c, d)], F[(a, (b + c) % 2, d)]), F[(a, b, c)])
    rhs = gmul(F[((a + b) % 2, c, d)], F[(a, b, (c + d) % 2)])
    return lhs == rhs


def is_cocycle(F):
    return all(cocycle_instance(F, *q) for q in QUADS)


def Fnorm(f, a, b, c):
    return f if (a == 1 and b == 1 and c == 1) else G_ONE


def detaNum(eta, a, b, c):
    return gmul(eta[(b, c)], eta[(a, (b + c) % 2)])


def detaDen(eta, a, b, c):
    return gmul(eta[((a + b) % 2, c)], eta[(a, b)])


def sliceGauge(F):
    return {(0, 0): G_ONE, (1, 1): G_ONE,
            (1, 0): F[(1, 0, 0)], (0, 1): gconj(F[(0, 0, 1)])}


def cochainOf(p, q, s):
    return {(1, 1, 1): s, (1, 0, 1): gmul(q, p), (1, 1, 0): gconj(p),
            (0, 1, 1): gconj(q), (1, 0, 0): p, (0, 0, 1): q,
            (0, 0, 0): G_ONE, (0, 1, 0): G_ONE}


def normalizes(F, eta, f):
    """the slot equation of `slice_lemma_over_zi_units`, cleared form"""
    return all(gmul(F[t], detaNum(eta, *t)) == gmul(Fnorm(f, *t), detaDen(eta, *t))
               for t in SLOTS)


# the S3 defs the strengthened headline references
def Fz2(f, a, b, c, d, x, y):
    if x == (a + b) % 2 and y == (b + c) % 2 and d == (a + b + c) % 2:
        return f if (a == 1 and b == 1 and c == 1) else G_ONE
    return G_ZERO


def pentL(f, a, b, c, d):
    x = (a + b) % 2; y = (x + c) % 2; t = (y + d) % 2
    w = (c + d) % 2; v = (b + w) % 2; u = (b + c) % 2
    return gmul(gmul(Fz2(f, a, b, c, y, x, u), Fz2(f, a, u, d, t, y, v)),
                Fz2(f, b, c, d, v, u, w))


def pentR(f, a, b, c, d):
    x = (a + b) % 2; y = (x + c) % 2; t = (y + d) % 2
    w = (c + d) % 2; v = (b + w) % 2
    return gmul(Fz2(f, x, c, d, t, y, w), Fz2(f, a, b, w, t, x, v))


def pentagon(f):
    return all(pentL(f, *q) == pentR(f, *q) for q in QUADS)


print("=" * 68)
print("SEAT B / S7 — the slice lemma over the units of Z[i]")
print("route: DIRECT EXHAUSTION of all 65536 cochains and their orbits")
print("=" * 68)

# ═══ 1. the exhaustion ══════════════════════════════════════════════════════
print("\n-- the exhaustion (seat B's own route) --")

all_cochains = [dict(zip(SLOTS, v)) for v in itertools.product(UNITS, repeat=8)]
check("exhaustion_box_complete", len(all_cochains) == 4 ** 8,
      f"4^8 = {4 ** 8} unit-valued cochains enumerated; the box is the whole "
      "unit-valued cochain space, so nothing is sampled")

cocycles = [F for F in all_cochains if is_cocycle(F)]
key = lambda F: tuple(F[t] for t in SLOTS)
cocycle_keys = set(key(F) for F in cocycles)
check("s7_nest_cocycles_32", len(cocycles) == 32,
      f"{len(cocycles)} cochains satisfy all 16 pentagon instances — found by "
      "running the relation, not by any parametrization")

gauges = [dict(zip(PAIRS, v)) for v in itertools.product(UNITS, repeat=4)]
check("gauge_box_complete", len(gauges) == 256, "4^4 = 256 vertex gauges")


def act(eta, F):
    """F · (d eta), with the division exact because every value is a unit"""
    return {t: gmul(gmul(F[t], detaNum(eta, *t)), gconj(detaDen(eta, *t)))
            for t in SLOTS}


trivial = {t: G_ONE for t in SLOTS}
coboundaries = set(key(act(eta, trivial)) for eta in gauges)
check("s7_nest_coboundaries_16", len(coboundaries) == 16,
      f"the 256 gauges produce {len(coboundaries)} distinct coboundaries")
check("coboundaries_are_cocycles", coboundaries <= cocycle_keys,
      "d(gauges) ⊆ cocycles — d² = 0, the faithfulness check")

seen, orbits = set(), []
for F in cocycles:
    if key(F) in seen:
        continue
    orbit = set(key(act(eta, F)) for eta in gauges)
    seen |= orbit
    orbits.append(orbit)
check("s7_nest_classes_2", len(orbits) == 2,
      f"the 32 cocycles fall into {len(orbits)} gauge orbits")
check("orbits_partition_the_cocycles",
      sum(len(o) for o in orbits) == 32 and seen == cocycle_keys,
      f"orbit sizes {sorted(len(o) for o in orbits)}; 16 + 16 = 32, and the "
      "orbits exhaust the cocycles — the nest ties")

# ═══ 2. THE SLICE LEMMA, from the partition alone ═══════════════════════════
print("\n-- the slice lemma, read off the orbit partition --")

norm_shapes = {u: key(dict(zip(SLOTS, [Fnorm(u, *t) for t in SLOTS])))
               for u in UNITS}
with_norm = [o for o in orbits if any(s in o for s in norm_shapes.values())]
check("slice_lemma_over_zi_units", len(with_norm) == len(orbits) == 2,
      f"{len(with_norm)}/{len(orbits)} orbits contain an Fnorm f "
      "representative — EVERY class meets the normalized slice")

labels = sorted(u for u in UNITS if any(norm_shapes[u] in o for o in orbits))
check("exactly_two_over_zi_units", labels == sorted([G_ONE, G_MONE]),
      f"the labels reached are {labels} = {{+1, −1}} — exactly two classes, "
      "and the two are the pentagon's own two (S3)")
check("normalized_reps_satisfy_S3_pentagon", all(pentagon(u) for u in labels),
      "each reached representative satisfies the S3 `pentagon` predicate — "
      "the strengthened headline's bridge back to the original object")
check("control_labels_are_not_all_units",
      not pentagon(G_I) and not pentagon(G_MI) and G_I not in labels,
      "i and −i are units but are NOT reached and do NOT satisfy the "
      "pentagon — the label set is a result, not the unit set restated")

# ═══ 3. seat P's claimed STRUCTURE, checked against the exhaustion ══════════
print("\n-- seat P's structure, checked against seat B's exhaustion --")

for nm, slot, want in [
        ("cocycle_at_000", (0, 0, 0), lambda F: G_ONE),
        ("cocycle_at_010", (0, 1, 0), lambda F: G_ONE)]:
    check(nm, all(F[slot] == want(F) for F in cocycles),
          f"slot {slot} is forced to 1 on all {len(cocycles)} cocycles")

check("cocycle_at_110", all(gmul(F[(1, 0, 0)], F[(1, 1, 0)]) == G_ONE
                            for F in cocycles),
      "F(1,0,0)·F(1,1,0) = 1 on every cocycle")
check("cocycle_at_011", all(gmul(F[(0, 1, 1)], F[(0, 0, 1)]) == G_ONE
                            for F in cocycles),
      "F(0,1,1)·F(0,0,1) = 1 on every cocycle")
check("cocycle_at_101", all(F[(1, 0, 1)] == gmul(F[(0, 0, 1)], F[(1, 0, 0)])
                            for F in cocycles),
      "F(1,0,1) = F(0,0,1)·F(1,0,0) on every cocycle")
check("cocycle_011_eq_conj", all(F[(0, 1, 1)] == gconj(F[(0, 0, 1)])
                                 for F in cocycles), "F(0,1,1) = conj F(0,0,1)")
check("cocycle_110_eq_conj", all(F[(1, 1, 0)] == gconj(F[(1, 0, 0)])
                                 for F in cocycles), "F(1,1,0) = conj F(1,0,0)")

flabel = lambda F: gmul(gmul(F[(1, 1, 1)], F[(1, 0, 0)]), F[(0, 0, 1)])
check("cocycle_f_sq_one",
      all(gmul(flabel(F), flabel(F)) == G_ONE for F in cocycles),
      "f = F(1,1,1)·F(1,0,0)·F(0,0,1) squares to 1 on every cocycle")

# the parametrization, both directions and injectivity
param = {}
for p, q, s in itertools.product(UNITS, UNITS, UNITS):
    f = gmul(gmul(s, p), q)
    if gmul(f, f) == G_ONE:
        param[(p, q, s)] = key(cochainOf(p, q, s))
check("s7_nest_cocycles_32_triples", len(param) == 32,
      f"{len(param)} of 4³ = 64 parameter triples satisfy (s·p·q)² = 1")
check("cochainOf_is_cocycle",
      all(is_cocycle(cochainOf(*t)) for t in param),
      "BACKWARD: every admitted triple really is a cocycle — so 32 is a "
      "count, not an upper bound")
check("cocycle_is_cochainOf",
      all(key(F) == key(cochainOf(F[(1, 0, 0)], F[(0, 0, 1)], F[(1, 1, 1)]))
          for F in cocycles),
      "FORWARD: every cocycle IS cochainOf of its own three values")
check("cochainOf_injective", len(set(param.values())) == len(param) == 32,
      "distinct triples give distinct cochains — the count cannot overcount")
check("parametrization_is_exact", set(param.values()) == cocycle_keys,
      "the parametrized set EQUALS the exhaustively-found cocycle set")

# seat P's explicit witness, checked on every cocycle
bad = [F for F in cocycles if not normalizes(F, sliceGauge(F), flabel(F))]
check("sliceGauge_normalizes_every_cocycle", not bad,
      f"seat P's explicit gauge — read off F, never searched for — normalizes "
      f"{len(cocycles) - len(bad)}/{len(cocycles)} cocycles at all 8 slots")
check("sliceGauge_is_unit_valued",
      all(all(isUnit(v) for v in sliceGauge(F).values()) for F in cocycles),
      "the constructed gauge lands in the units, as the lemma claims")

# the S3 tie
check("Fnorm_eq_Fz2",
      all(Fnorm(f, a, b, c)
          == Fz2(f, a, b, c, (a + b + c) % 2, (a + b) % 2, (b + c) % 2)
          for f in UNITS for (a, b, c) in SLOTS),
      "Fnorm IS the kernel's Fz2 on its admissible slots — the normalized "
      "representative is S3's own object, not a look-alike")

# the coboundary nest, seat P's two halves
def gaugeFn(g):
    w, x, y, z = g
    return {(0, 0): w, (0, 1): x, (1, 0): y, (1, 1): z}


def cobVec(g):
    e = gaugeFn(g)
    return tuple(gmul(detaNum(e, *t), gconj(detaDen(e, *t))) for t in SLOTS)


check("s7_coboundary_reduces_to_normal_form",
      all(cobVec(g) == cobVec((G_ONE, gmul(g[1], gconj(g[0])),
                               gmul(g[2], gconj(g[0])), G_ONE))
          for g in itertools.product(UNITS, repeat=4)),
      "every gauge has the coboundary of its normalized form (η00 rescales, "
      "η11 cancels) — all 256 checked")
reps = {(x, y): cobVec((G_ONE, x, y, G_ONE)) for x in UNITS for y in UNITS}
check("s7_cobReps_distinct", len(set(reps.values())) == len(reps) == 16,
      "the 16 normalized gauges give 16 DISTINCT coboundaries")
check("cobReps_are_the_whole_subgroup",
      set(reps.values()) == set(cobVec(g) for g in itertools.product(UNITS, repeat=4))
      == coboundaries,
      "reduction + distinctness give exactly the 16 found by exhaustion")

# ═══ 4. the negative controls ═══════════════════════════════════════════════
print("\n-- negative controls (norm 5), re-run independently --")

controlA = {t: (G_I if t == (1, 1, 0) else G_ONE) for t in SLOTS}
check("control_A_unit_valued", all(isUnit(v) for v in controlA.values()),
      "the witness is unit-valued — it fails as a COCYCLE, not as a cochain")
check("control_A_not_a_cocycle", not is_cocycle(controlA),
      "i at (1,1,0) is NOT a cocycle — so it was never a class; the two "
      "SUPERSEDED probes' 'counterexample' dies here")
hits = sum(1 for g in itertools.product(UNITS, repeat=4) for f in UNITS
           if normalizes(controlA, gaugeFn(g), f))
check("control_A_never_normalized", hits == 0,
      f"{hits}/1024 (gauge, f) pairs normalize it — the cocycle hypothesis is "
      "load-bearing, not decorative")

ctlB = cochainOf(G_I, G_ONE, G_I)
idg = {pr: G_ONE for pr in PAIRS}
check("control_B_is_a_genuine_cocycle", is_cocycle(ctlB),
      "cochainOf(i, 1, i) IS a cocycle — so control B isolates the GAUGE")
check("control_B_identity_gauge_fails", not normalizes(ctlB, idg, G_MONE),
      "the identity gauge does NOT normalize it (it fails already at the "
      "(1,0,0) slot)")
check("live_slice_gauge_normalizes",
      normalizes(ctlB, sliceGauge(ctlB), G_MONE)
      and flabel(ctlB) == G_MONE,
      "the SAME cochain IS normalized by the gauge the lemma constructs, "
      "onto f = −1 — the content is the construction, not the shape")
check("live_gaussian_cocycle_off_slice",
      ctlB[(1, 0, 0)] == G_I and sliceGauge(ctlB)[(1, 0)] == G_I != G_ONE,
      "the witness sits off the real axis AND off the slice, and its gauge "
      "is not the identity — the lemma is exercised where it has work to do")
check("live_both_classes_inhabited",
      is_cocycle(cochainOf(G_ONE, G_ONE, G_ONE))
      and is_cocycle(cochainOf(G_ONE, G_ONE, G_MONE)),
      "both classes are inhabited by named cocycles — the guarded ∀ is not "
      "vacuous")

# ═══ 5. the label audit (norm 6) ════════════════════════════════════════════
print("\n-- label audit (norm 6): the name must not overreach --")
import os
KERNEL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "seatP", "Zi.lean")
try:
    src = open(KERNEL, encoding="utf-8").read()
    s7 = src[src.index("S7 — THE SLICE LEMMA"):]
    names = [ln.split()[1] for ln in s7.split("\n") if ln.startswith("theorem ")]
    check("label_no_U1_in_theorem_names",
          not any("U1" in n or "u1" in n for n in names),
          f"none of the {len(names)} S7 theorem names says U(1)")
    check("label_says_zi_units",
          "over the units of Z[i]" in s7 or "over the units of ℤ[i]" in s7,
          "the section says 'over the units of Z[i]' in its own prose")
    check("label_records_U1_out_of_reach",
          "not representable" in s7 and "U(1)" in s7,
          "the section RECORDS that the continuous U(1) version is out of "
          "zero-import reach, rather than quietly omitting it")
except Exception as exc:                                  # pragma: no cover
    check("label_audit_ran", False, f"could not read kernel: {exc}")

# ═══ PLANT (norm 16 hygiene) ════════════════════════════════════════════════
print("\n-- plant --")
# A plant must RE-RUN the real check on poisoned data and see it go red.
# (An earlier draft of this block asserted `poisoned != cocycle_keys`, which
# is true by construction — a check that cannot fail is not a check, norm 7.
# Caught here, in this file, before it shipped; recorded rather than quietly
# swapped.)

# (a) delete a cocycle from the class set, then re-run the partition tie
poisoned_cocycles = cocycles[1:]
p_keys = set(key(F) for F in poisoned_cocycles)
p_seen, p_orbits = set(), []
for F in poisoned_cocycles:
    if key(F) in p_seen:
        continue
    o = set(key(act(eta, F)) for eta in gauges)
    p_seen |= o
    p_orbits.append(o)
p_tie = (sum(len(o) for o in p_orbits) == 32 and p_seen == p_keys)
check("plant_deleted_cocycle_caught", not p_tie,
      f"one cocycle deleted: the orbits still cover {len(p_seen)} keys but the "
      f"set has {len(p_keys)} — `orbits_partition_the_cocycles` goes RED, as it "
      "must")

# (b) mislabel the normal form: move the free slot from (1,1,1) to (1,1,0)
def Fnorm_mislabelled(f, a, b, c):
    return f if (a == 1 and b == 1 and c == 0) else G_ONE


def normalizes_mis(F, eta, f):
    return all(gmul(F[t], detaNum(eta, *t))
               == gmul(Fnorm_mislabelled(f, *t), detaDen(eta, *t))
               for t in SLOTS)


broken = [F for F in cocycles if not normalizes_mis(F, sliceGauge(F), flabel(F))]
blind = [F for F in cocycles if flabel(F) == G_ONE]
check("plant_mislabelled_Fnorm_caught",
      len(broken) == 16 and all(flabel(F) == G_MONE for F in broken),
      f"free slot moved to (1,1,0): the slot equation fails on "
      f"{len(broken)}/{len(cocycles)} cocycles — a mislabelled normal form "
      "cannot pass. It bites on EXACTLY the 16 whose label is −1, and is "
      f"blind on the {len(blind)} whose label is +1, because Fnorm(+1) is "
      "all-ones at every slot and moving its free slot changes nothing. "
      "Recorded rather than rounded off: this plant's reach is half the "
      "cocycles by construction, and the half it cannot reach is the half "
      "where there is nothing to mislabel")

# ── verdict ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 68)
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print(f"checks run: {len(CHECKS)};  passed: {npass};  failed: {nfail}")
if nfail == 0:
    print("VERDICT: the slice lemma re-derived by DIRECT EXHAUSTION of all")
    print("         65536 unit-valued cochains and their 256-gauge orbits —")
    print("         not by seat P's parametrization, witnesses, or `decide`")
    print("         nests. 32 cocycles / 16 coboundaries / 2 classes, all")
    print("         three matching the design probe. Seat P's structure then")
    print("         checked AGAINST that exhaustion and found exact. Both")
    print("         negative controls re-run; label audit clean; plants bitten.")
    print("EXIT: 0")
    sys.exit(0)
else:
    print("VERDICT: NOT CLEAN")
    sys.exit(1)
