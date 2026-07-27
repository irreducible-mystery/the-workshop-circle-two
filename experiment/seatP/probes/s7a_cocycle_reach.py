#!/usr/bin/env python3
"""
S7a COCYCLE-CORRECTED REACH PROBE.  NO LEAN.

Correction to the first two probes: the canon's normalized 3-cochain is
NOT an arbitrary function (Z2)^3 -> units.  The kernel's `Fz2` (Zi.lean
line ~521) HARDCODES the F-symbol so the ONLY free slot is (1,1,1) |-> f;
every admissible slot with a 0 argument is forced to `one`.  The pentagon
(cocycle) condition then forces f^2 = 1.  So:

  - a NORMALIZED representative = the shape `Fz2 f`, one free unit f;
  - a COCYCLE = a cochain satisfying the pentagon relation;
  - the SLICE LEMMA ("every class has a normalized representative")
    = every cocycle is cohomologous (differs by a coboundary d.eta)
      to some `Fz2 f`.

This probe measures, over a chosen unit group:
  (C1) which cochains are cocycles (satisfy the pentagon relation);
  (C2) the coboundary subgroup d(gauges);
  (C3) cocycles / coboundaries = H^3-like classes (finite);
  (C4) does every cocycle class contain an Fz2-normalized rep? (SLICE LEMMA)
  (C5) how many classes, and the F(1,1,1) values -> "exactly two?"

We reuse the kernel's EXACT pentagon plumbing (Fz2/pentL/pentR) so the
measurement is faithful to seat P's statement, transcribed here in Python
(reading the STATEMENT shape is permitted; this is not seat B's proof).
"""

import itertools

Z2 = (0, 1)
TRIPLES = list(itertools.product(Z2, repeat=3))      # 8 cochain slots
PAIRS = list(itertools.product(Z2, repeat=2))         # 4 gauge slots
QUADS = list(itertools.product(Z2, repeat=4))         # 16 pentagon instances
ZERO_SLOTS = [(a, b, c) for (a, b, c) in TRIPLES if 0 in (a, b, c)]
SLOT111 = (1, 1, 1)


def make(order):
    return list(range(order))


# --- coboundary (gauge) action, additive exponents mod `order` -------------
def deta(eta, a, b, c, mod):
    return (eta[(b, c)] + eta[(a, (b + c) % 2)]
            - eta[((a + b) % 2, c)] - eta[(a, b)]) % mod


def act(eta, F, mod):
    return {t: (F[t] + deta(eta, *t, mod)) % mod for t in TRIPLES}


# --- the pentagon relation on a GENERAL cochain F --------------------------
# The kernel writes the pentagon multiplicatively via Fz2; for a general
# cochain F (a full function on TRIPLES, no hardcoding) the standard 3-cocycle
# (pentagon) condition, additive in exponents mod `order`, is:
#   F(b,c,d) - F(a+b,c,d) + F(a,b+c,d) - F(a,b,c+d) + F(a,b,c) = 0
# (the associativity 5-term relation; XOR is the Z2 group op).
def is_cocycle(F, mod):
    for a, b, c, d in QUADS:
        s = (F[(b, c, d)]
             - F[((a + b) % 2, c, d)]
             + F[(a, (b + c) % 2, d)]
             - F[(a, b, (c + d) % 2)]
             + F[(a, b, c)]) % mod
        if s != 0:
            return False
    return True


# --- the Fz2-normalized shape: 1 on every zero slot, free at (1,1,1) -------
def Fz2_cochain(fexp):
    F = {t: 0 for t in TRIPLES}
    F[SLOT111] = fexp % 4  # exponent; caller ensures within group
    return F


def all_gauges(units):
    for vals in itertools.product(units, repeat=len(PAIRS)):
        yield dict(zip(PAIRS, vals))


def all_cochains(units):
    for vals in itertools.product(units, repeat=len(TRIPLES)):
        yield dict(zip(TRIPLES, vals))


def analyze(order):
    units = make(order)
    gauges = list(all_gauges(units))
    label = "Z[i] units (Z4)" if order == 4 else f"Z{order} (real signs)"
    print("=" * 70)
    print(f"UNIT GROUP = {label}   gauges={len(gauges)}   cochains={order**8}")
    print("=" * 70)

    checks = []

    def chk(name, cond, note):
        checks.append((name, bool(cond)))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}: {note}")

    # C1: cocycles
    cocycles = [F for F in all_cochains(units) if is_cocycle(F, order)]
    cocy_keys = set(tuple(F[t] for t in TRIPLES) for F in cocycles)
    print(f"  cocycles (pentagon solutions): {len(cocycles)}")

    # C2: coboundary subgroup
    trivial = {t: 0 for t in TRIPLES}
    cobound = set(tuple(act(eta, trivial, order)[t] for t in TRIPLES)
                  for eta in gauges)
    print(f"  coboundaries |d(gauges)|: {len(cobound)}")

    # sanity: coboundaries are cocycles
    cob_are_cocy = cobound.issubset(cocy_keys)
    chk("coboundaries_are_cocycles", cob_are_cocy,
        "d(gauges) subset cocycles (d^2 = 0, faithfulness check)")

    # C3: H^3-like classes = cocycles / coboundaries
    # orbit of each cocycle under the gauge action
    seen = set()
    classes = []
    for F in cocycles:
        key = tuple(F[t] for t in TRIPLES)
        if key in seen:
            continue
        orbit = set()
        for eta in gauges:
            orbit.add(tuple(act(eta, F, order)[t] for t in TRIPLES))
        seen |= orbit
        classes.append(orbit)
    print(f"  gauge classes of cocycles (H^3-like): {len(classes)}")

    # C4: SLICE LEMMA -- does every class contain an Fz2-normalized rep?
    fz2_shapes = set(tuple(Fz2_cochain(u)[t] for t in TRIPLES) for u in units)
    classes_with_norm = 0
    for orbit in classes:
        if orbit & fz2_shapes:
            classes_with_norm += 1
    slice_lemma = (classes_with_norm == len(classes))
    chk("every_cocycle_class_has_Fz2_normalized_rep", slice_lemma,
        f"{classes_with_norm}/{len(classes)} classes contain an Fz2 f shape "
        "(THE SLICE LEMMA)")

    # C5: class count and F(1,1,1) values on the normalized reps
    slice_vals = set()
    for orbit in classes:
        for rep in (orbit & fz2_shapes):
            # rep is a tuple over TRIPLES; find the (1,1,1) index
            idx = TRIPLES.index(SLOT111)
            slice_vals.add(rep[idx])
    print(f"  F(1,1,1) values on normalized reps: {sorted(slice_vals)} "
          f"=> {len(slice_vals)} classes on that axis")
    chk("normalized_class_count", len(slice_vals) >= 1,
        f"{len(slice_vals)} normalized classes on the (1,1,1) axis")

    passed = sum(1 for _, ok in checks if ok)
    print(f"  --> checks {passed}/{len(checks)}")
    return {"order": order, "cocycles": len(cocycles),
            "coboundaries": len(cobound), "classes": len(classes),
            "slice_lemma": slice_lemma, "slice_vals": sorted(slice_vals),
            "slice_class_count": len(slice_vals)}


def main():
    print("\n########## Z[i] units (order 4) ##########\n")
    r4 = analyze(4)
    print("\n########## REAL signs {1,-1} = Z2 (order 2) ##########\n")
    r2 = analyze(2)

    print("\n" + "=" * 70)
    print("SLICE-LEMMA REACH VERDICT (cocycle-correct; for the CHARGE)")
    print("=" * 70)
    for r in (r4, r2):
        grp = "Z[i] units" if r["order"] == 4 else "real signs Z2"
        print(f"  [{grp}] cocycles={r['cocycles']} coboundaries="
              f"{r['coboundaries']} classes={r['classes']} "
              f"slice_lemma={'TRUE' if r['slice_lemma'] else 'FALSE'} "
              f"classes_on_axis={r['slice_class_count']} "
              f"F111_vals={r['slice_vals']}")
    print("\n  Interpretation for the reach verdict is written in the CHARGE,")
    print("  not asserted here (norm 15: the adjudicator, named there, rules).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
