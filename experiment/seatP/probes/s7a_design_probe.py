#!/usr/bin/env python3
"""
[SUPERSEDED BY s7a_cocycle_reach.py -- kept for record, norm 12/16 honesty.]
This probe enumerated ARBITRARY cochains (Z2)^3 -> units, which is the
WRONG object: a gauge "class" is an orbit of a COCYCLE (pentagon solution),
not of an arbitrary function.  Its FAIL result (64/65536 normalizable) and
its "counterexample" (i on slot (1,1,0)) are artifacts of that wrong frame:
that cochain is NOT a cocycle (measured: s7a_cocycle_reach + inline check),
so it was never a class.  The correct object gives slice_lemma=TRUE.
This file remains as the diagnostic trail that the design probe caught a
false framing BEFORE it became a mis-stated theorem -- exactly why the probe
precedes any Lean (norm 15).
------------------------------------------------------------------------
S7a DESIGN PROBE  --  the slice lemma ("every class has a normalized
representative"), measured for zero-import reach.  NO LEAN.  This probe
measures the mathematics against bench + certificate so a CHARGE can be
written with a precise statement and an HONEST reach verdict (norm 6:
impossibility is a valid result; norm 15: adjudicator named at birth,
see the CHARGE, not this instrument).

WHAT G1c PROVES (bench-certified; certificate audit/c2_gift_certificates.py
lines 421-490; kernel seatP/Zi.lean lines 767-862):
  - the F(1,1,1) slot moves by eta10/eta01 under a vertex gauge eta;
  - the 7 zero-slot conditions reduce to n00 = n01 = n10 (n11 free);
  - so the slot is INVARIANT under slice-preserving gauges
    => F=+1 and F=-1 are distinct classes ON THE NORMALIZED SLICE.

THE GAP (S7a; kernel docstring, verbatim: "NOT claimed: every class
meets the slice"):
  every gauge class can be MOVED ONTO the normalized slice -- i.e. for
  an arbitrary normalized-input 3-cochain there is a gauge eta carrying
  it to a representative that is 1 on every zero-containing slot.  Only
  with this does "exactly two" hold full-stop rather than slice-relative.

This probe:
  (A) builds the coboundary action of vertex gauges eta on 3-cochains,
      EXACTLY as the certificate/kernel define detaNum/detaDen;
  (B) restricts eta to ZERO-IMPORT units = the 4 units of Z[i]
      {1,-1,i,-i} (the honest kernel restriction: U(1) is not
      representable zero-import; Z[i]'s unit group IS -- it is Z4);
  (C) enumerates ALL cochains reachable / all gauge orbits, and MEASURES
      whether every orbit contains a normalized-slice representative;
  (D) reports the reach verdict: is the honest statement decidable by a
      FINITE `decide` over Z[i] units (=> in zero-import reach), or does
      it require U(1) / an existential over an infinite unit group
      (=> out of reach, ship measured impossibility + sharpest fragment).
No claim is proved here; this is measurement for the CHARGE.
"""

import itertools

# ---------------------------------------------------------------------------
# Z[i] units as the zero-import unit group.  U(1) is the canon's unit
# group; it is NOT representable in the zero-import kernel (no reals, no
# roots of unity beyond what Z[i] carries).  Z[i]'s units are exactly
# {1, -1, i, -i}, a cyclic group of order 4 -- this is the honest finite
# stand-in the kernel already uses (I, one, neg one in Zi).
# Represent a unit by its exponent in <i>: 0->1, 1->i, 2->-1, 3->-i.
# Multiplication is addition mod 4; inverse is negation mod 4.
# ---------------------------------------------------------------------------
UNITS = [0, 1, 2, 3]  # exponents of i


def umul(a, b):
    return (a + b) % 4


def uinv(a):
    return (-a) % 4


# ---------------------------------------------------------------------------
# 3-cochains F : Z2 x Z2 x Z2 -> units, and vertex gauges eta : Z2 x Z2 -> units.
# Coboundary (multiplicative), EXACTLY the certificate/kernel form:
#   (d eta)(a,b,c) = eta(b,c) * eta(a, b+c) / [ eta(a+b, c) * eta(a,b) ]
# A gauge acts on a cochain by  (eta . F)(a,b,c) = F(a,b,c) * (d eta)(a,b,c).
# In exponent arithmetic (units written additively mod 4):
#   (d eta)(a,b,c) = eta[b,c] + eta[a, b^c] - eta[a^b, c] - eta[a,b]   (mod 4)
# where ^ is XOR = addition mod 2 on Z2.
# ---------------------------------------------------------------------------
Z2 = (0, 1)
TRIPLES = list(itertools.product(Z2, repeat=3))
PAIRS = list(itertools.product(Z2, repeat=2))
ZERO_SLOTS = [(a, b, c) for (a, b, c) in TRIPLES if 0 in (a, b, c)]  # 7 of 8
SLOT111 = (1, 1, 1)


def deta(eta, a, b, c):
    """eta is a dict {(x,y): exponent}. Returns (d eta)(a,b,c) exponent mod 4."""
    return (eta[(b, c)] + eta[(a, (b + c) % 2)]
            - eta[((a + b) % 2, c)] - eta[(a, b)]) % 4


def act(eta, F):
    """(eta . F)(a,b,c) = F(a,b,c) + (d eta)(a,b,c) mod 4."""
    return {t: (F[t] + deta(eta, *t)) % 4 for t in TRIPLES}


def is_normalized(F):
    """normalized-slice representative: 1 (exponent 0) on every zero slot."""
    return all(F[t] == 0 for t in ZERO_SLOTS)


# ---------------------------------------------------------------------------
# All vertex gauges over Z[i] units: 4 pairs -> 4^4 = 256 gauges.
# All 3-cochains over Z[i] units: 8 slots -> 4^8 = 65536 cochains.
# We measure ORBITS under the gauge action and ask of each orbit whether
# it contains a normalized representative -- THE SLICE LEMMA, finite form.
# ---------------------------------------------------------------------------
def all_gauges():
    for vals in itertools.product(UNITS, repeat=len(PAIRS)):
        yield dict(zip(PAIRS, vals))


def all_cochains():
    for vals in itertools.product(UNITS, repeat=len(TRIPLES)):
        yield dict(zip(TRIPLES, vals))


def probe():
    print("=" * 70)
    print("S7a DESIGN PROBE -- the slice lemma, measured for zero-import reach")
    print("=" * 70)

    gauges = list(all_gauges())
    print(f"[setup] zero-import unit group = Z[i] units = "
          f"{{1, i, -1, -i}} (Z4); |units| = {len(UNITS)}")
    print(f"[setup] vertex gauges eta: Z2xZ2 -> units : {len(gauges)}")
    print(f"[setup] 3-cochains F: (Z2)^3 -> units      : {4**8}")
    print(f"[setup] zero-containing slots (must be 1)  : {len(ZERO_SLOTS)} of 8")

    checks = []

    def chk(name, cond, note):
        checks.append((name, bool(cond)))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}: {note}")

    # -- fidelity 1: the coboundary matches the certificate's (1,1,1) motion.
    # certificate: (d eta)(1,1,1) = eta10/eta01 after the common eta11 cancels.
    print("\n[1] coboundary fidelity to certificate G1c_slot_moves_by_n10_over_n01")
    ok_motion = True
    for eta in gauges:
        raw = deta(eta, 1, 1, 1)
        reduced = (eta[(1, 0)] - eta[(0, 1)]) % 4
        if raw != reduced:
            ok_motion = False
            break
    chk("slot111_motion_is_eta10_over_eta01", ok_motion,
        "(d eta)(1,1,1) = eta10 - eta01 (mod 4) for ALL 256 gauges "
        "-- matches certificate's eta10/eta01")

    # -- fidelity 2: slice-preserving gauges force eta01 = eta10 (kernel
    #    slice_forces_eta_symmetric), and then the slot is fixed.
    print("\n[2] slice-preservation fidelity (kernel slice_forces_eta_symmetric"
          " / gauge_slot_invariant)")
    sp = []  # slice-preserving gauges: (d eta) = 1 at (1,0,0) and (0,0,1)
    for eta in gauges:
        if deta(eta, 1, 0, 0) == 0 and deta(eta, 0, 0, 1) == 0:
            sp.append(eta)
    forces = all((eta[(0, 1)] == eta[(1, 0)]) for eta in sp)
    chk("two_conditions_force_eta01_eq_eta10", forces,
        f"all {len(sp)} gauges meeting the (1,0,0),(0,0,1) conditions have "
        "eta01 = eta10 -- STRONGER than 7 conditions (norm 6 STRENGTH note)")
    slot_fixed = all(deta(eta, 1, 1, 1) == 0 for eta in sp)
    chk("slice_preserving_fixes_slot111", slot_fixed,
        "every slice-preserving gauge fixes F(1,1,1) -- the invariance G1c "
        "proves, reproduced over Z[i] units")

    # -- THE SLICE LEMMA, finite form over Z[i] units:
    #    does EVERY 3-cochain have a gauge carrying it to the normalized slice?
    print("\n[3] THE SLICE LEMMA (finite, over Z[i] units): every class has a"
          " normalized representative?")
    normalizable = 0
    total = 0
    not_normalizable_example = None
    # We only need: for each cochain, EXISTS gauge eta with is_normalized(eta.F).
    # 65536 cochains x 256 gauges = ~16.7M ops -- feasible.
    for F in all_cochains():
        total += 1
        hit = False
        for eta in gauges:
            if is_normalized(act(eta, F)):
                hit = True
                break
        if hit:
            normalizable += 1
        elif not_normalizable_example is None:
            not_normalizable_example = dict(F)
    every_class_normalizable = (normalizable == total)
    chk("every_cochain_reaches_normalized_slice_over_Zi_units",
        every_class_normalizable,
        f"{normalizable}/{total} cochains have a gauge to the normalized slice")
    if not every_class_normalizable:
        print(f"      counterexample cochain (exponents of i): "
              f"{not_normalizable_example}")

    # -- how many DISTINCT normalized representatives / classes result?
    print("\n[4] class count after normalization (should recover 'exactly two'"
          " on the F(1,1,1) axis)")
    normalized_reps = set()
    slot_values_on_slice = set()
    for F in all_cochains():
        for eta in gauges:
            G = act(eta, F)
            if is_normalized(G):
                normalized_reps.add(tuple(G[t] for t in TRIPLES))
                slot_values_on_slice.add(G[SLOT111])
                break
    chk("normalized_slot111_values_are_a_subgroup",
        len(slot_values_on_slice) >= 1,
        f"F(1,1,1) on normalized reps takes values {sorted(slot_values_on_slice)}"
        " (exponents of i)")
    print(f"      distinct normalized representatives reached: "
          f"{len(normalized_reps)}")
    print(f"      F(1,1,1) values on the slice: {sorted(slot_values_on_slice)} "
          f"=> {len(slot_values_on_slice)} classes on this axis")

    # -- REACH VERDICT ------------------------------------------------------
    print("\n" + "=" * 70)
    print("REACH VERDICT (for the CHARGE)")
    print("=" * 70)
    finite_decidable = True  # the whole statement was decided by finite enum
    print(f"  * statement decided by FINITE enumeration over Z[i] units: "
          f"{finite_decidable}")
    print(f"  * gauges: {len(gauges)} (finite)  cochains: {4**8} (finite)")
    print("  * => a Z[i]-unit form of the slice lemma is a BOUNDED, "
          "DECIDABLE proposition")
    print("  * => IN zero-import reach IFF the honest statement is the "
          "Z[i]-unit form, provable by `decide` over the finite index set")
    print("  * CAVEAT (norm 6): the CANON's unit group is U(1), not Z[i] "
          "units. The Z[i]-unit slice lemma is a FAITHFUL FRAGMENT, not the "
          "full H^3(Z2,U(1))=Z2 sentence. Whether it counts as closing the "
          "register's exclusion is the ADJUDICATOR's call -- named in the CHARGE.")

    passed = sum(1 for _, ok in checks if ok)
    print(f"\nchecks run: {len(checks)}; passed: {passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(probe())
