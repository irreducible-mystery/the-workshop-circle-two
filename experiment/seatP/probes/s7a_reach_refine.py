#!/usr/bin/env python3
"""
[SUPERSEDED BY s7a_cocycle_reach.py -- kept for record.]  Like the first
probe, this enumerated arbitrary cochains, so its "naive slice lemma FALSE"
counts (64/65536 over Z4; 8/256 over Z2) are for the WRONG object.  The
cocycle-correct probe shows the slice lemma is TRUE over both unit groups.
Kept as the diagnostic trail showing why the object matters.
------------------------------------------------------------------------
S7a REACH REFINEMENT -- given the design probe's finding that the NAIVE
slice lemma is FALSE over Z[i] units (only 64/65536 cochains normalize),
characterize the reachable set precisely and find the SHARPEST TRUE
statement that is in zero-import reach.  NO LEAN.  Measurement for the
CHARGE's "sharpest reachable fragment" (HANDOFF sec 5, norm 6).

Findings to establish:
  R1  the image of the coboundary map d : gauges -> cochains is a
      SUBGROUP; its size is the count of cochains gauge-equivalent to the
      trivial one.  Over a DIVISIBLE unit group (U(1)) d is onto the
      normalizable cochains; over Z[i] units (Z4, NOT divisible) it is a
      proper subgroup -- THIS is why the naive lemma fails.
  R2  the exact obstruction: which cochains normalize, stated as a
      linear condition mod 4 (a decidable predicate -> zero-import).
  R3  the RESTRICTED slice lemma that IS true: "every cochain in the
      subgroup <image of d + normalized slice> has a normalized
      representative" -- trivially the reachable set; sharpen to the
      honest content.
  R4  the F=+-1 REAL sub-question: restrict to the SIGN unit group
      {1,-1} = Z2 (the real units, the canon's actual "F = +-1").  Over
      Z2 does every cochain normalize, and is the slice count exactly 2?
      THIS is the fragment that matches the canon's "exactly two".
"""

import itertools

Z2 = (0, 1)
TRIPLES = list(itertools.product(Z2, repeat=3))
PAIRS = list(itertools.product(Z2, repeat=2))
ZERO_SLOTS = [(a, b, c) for (a, b, c) in TRIPLES if 0 in (a, b, c)]
SLOT111 = (1, 1, 1)


def make(order):
    """unit group Z_order (additive exponents); order=4 -> Z[i] units,
       order=2 -> real signs {1,-1}."""
    return list(range(order))


def deta(eta, a, b, c, mod):
    return (eta[(b, c)] + eta[(a, (b + c) % 2)]
            - eta[((a + b) % 2, c)] - eta[(a, b)]) % mod


def act(eta, F, mod):
    return {t: (F[t] + deta(eta, *t, mod)) % mod for t in TRIPLES}


def is_normalized(F):
    return all(F[t] == 0 for t in ZERO_SLOTS)


def all_gauges(units):
    for vals in itertools.product(units, repeat=len(PAIRS)):
        yield dict(zip(PAIRS, vals))


def all_cochains(units):
    for vals in itertools.product(units, repeat=len(TRIPLES)):
        yield dict(zip(TRIPLES, vals))


def analyze(order):
    units = make(order)
    gauges = list(all_gauges(units))
    label = "Z[i] units (Z4)" if order == 4 else f"Z{order}"
    print("=" * 70)
    print(f"UNIT GROUP = {label}   |units|={order}   gauges={len(gauges)}   "
          f"cochains={order**8}")
    print("=" * 70)

    # normalizable set + slice values
    normalizable = 0
    total = 0
    slice_vals = set()
    slice_reps = set()
    for F in all_cochains(units):
        total += 1
        for eta in gauges:
            G = act(eta, F, order)
            if is_normalized(G):
                normalizable += 1
                slice_vals.add(G[SLOT111])
                slice_reps.add(tuple(G[t] for t in TRIPLES))
                break
    print(f"  normalizable cochains: {normalizable}/{total}  "
          f"({'ALL' if normalizable == total else 'PROPER SUBSET'})")
    print(f"  distinct normalized reps: {len(slice_reps)}")
    print(f"  F(1,1,1) values on the slice: {sorted(slice_vals)} "
          f"=> {len(slice_vals)} classes on the (1,1,1) axis")

    # coboundary image size (orbit of the trivial cochain)
    trivial = {t: 0 for t in TRIPLES}
    image = set(tuple(act(eta, trivial, order)[t] for t in TRIPLES)
                for eta in gauges)
    print(f"  |image of d| (coboundaries) = {len(image)}")

    # obstruction: characterize normalizable cochains as a subgroup and
    # give its index (the "H^3-like" quotient we can actually see).
    norm_subgroup = set()
    for F in all_cochains(units):
        for eta in gauges:
            if is_normalized(act(eta, F, order)):
                norm_subgroup.add(tuple(F[t] for t in TRIPLES))
                break
    idx = (order**8) // max(len(norm_subgroup), 1)
    print(f"  |normalizable subgroup| = {len(norm_subgroup)}  "
          f"index in all cochains = {idx}")
    return {"order": order, "normalizable": normalizable, "total": total,
            "slice_classes": len(slice_vals), "image": len(image),
            "norm_subgroup": len(norm_subgroup), "index": idx}


def main():
    print("\n########## R1-R3: Z[i] units (order 4) ##########\n")
    r4 = analyze(4)
    print("\n########## R4: REAL signs {1,-1} = Z2 (order 2) ##########\n")
    r2 = analyze(2)

    print("\n" + "=" * 70)
    print("SHARPEST REACHABLE FRAGMENT (for the CHARGE)")
    print("=" * 70)
    print("  * Z[i] units: naive slice lemma FALSE (normalizable = "
          f"{r4['normalizable']}/{r4['total']}); the coboundary image is a "
          "PROPER subgroup because Z4 is NOT divisible.")
    print("  * REAL signs Z2: normalizable = "
          f"{r2['normalizable']}/{r2['total']}; slice classes on the (1,1,1) "
          f"axis = {r2['slice_classes']}.")
    if r2['normalizable'] == r2['total'] and r2['slice_classes'] == 2:
        print("  * => OVER THE REAL SIGN GROUP {1,-1}, THE SLICE LEMMA IS "
              "TRUE and yields EXACTLY TWO classes.  THIS is the honest, "
              "zero-import-reachable fragment that matches the canon's "
              "'F = +-1'.  It is a finite `decide` proposition.")
    else:
        print("  * => even over Z2 the naive lemma needs care; see counts.")
    print("  * The full H^3(Z2,U(1))=Z2 sentence needs a DIVISIBLE unit "
          "group (U(1)); that is NOT zero-import representable. Measured "
          "impossibility for U(1); measured POSSIBILITY for the real-sign "
          "fragment. Adjudicator decides which the register's exclusion "
          "asks for (norm 6, norm 15).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
