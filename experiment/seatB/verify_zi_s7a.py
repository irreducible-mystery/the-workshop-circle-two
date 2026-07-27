#!/usr/bin/env python3
"""SEAT B — blind exact reimplementation of the S7a statements
(Zi_statements_v8.txt, sha256 914a80d58d71…d5b5), statements only.

The S7a layer: the reachable core of "every class meets the normalized
slice." Seat P proves it in Lean via `decide` over the finite unit group
and the 8 live slots. Seat B re-derives every S7a claim INDEPENDENTLY in
exact Python — the unit group {1,i,-1,-i}, the 8 live slots, and the
256-gauge slice iff — never reading seat P's proof route, only the
statements. Exact integer arithmetic throughout; no floats.

Blindness boundary held: definitions (Zi mul/normSq/conj, detaNum/detaDen,
Fz2's admissibility mask, unitList, s7aLiveSlots) transcribed from the v8
statements ALONE. Seat B does not know HOW seat P discharged the goals —
only WHAT was claimed.
"""
import sys

CHECKS = []


def check(name, ok, note=""):
    CHECKS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {note}" if note else ""))


# ── exact Gaussian integers (transcribed from v8 defs) ──────────────────
def gmul(z, w):
    # def mul (z w) := ⟨z.re*w.re - z.im*w.im, z.re*w.im + z.im*w.re⟩
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gneg(z):
    return (-z[0], -z[1])


def normSq(z):
    return z[0] * z[0] + z[1] * z[1]


ONE = (1, 0)
NEGONE = (-1, 0)
I = (0, 1)
NEGI = (0, -1)

# def unitList : List Zi := [one, neg one, I, neg I]
unitList = [ONE, NEGONE, I, NEGI]


# ── S7a.1  s7a_units_have_norm_one : ∀ u ∈ unitList, normSq u = 1 ────────
check("s7a_units_have_norm_one",
      all(normSq(u) == 1 for u in unitList),
      "every listed unit has norm 1")


# ── S7a.2  s7a_units_complete : normSq u = 1 → u ∈ unitList ──────────────
# Blind completeness: exhaust the norm-1 locus over the only box that can
# hold it. normSq (a,b) = a²+b² = 1 forces a²≤1 and b²≤1 ⇒ a,b ∈ {-1,0,1}.
# So the search box [-1,1]² is COMPLETE (argued, not assumed).
norm1 = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if normSq((a, b)) == 1]
check("s7a_units_complete",
      set(norm1) == set(unitList) and len(norm1) == 4,
      f"norm-1 locus in complete box = {sorted(norm1)}")


# ── S7a.3  s7a_unit_alphabet_nest : Nodup ∧ length = 4 ───────────────────
check("s7a_unit_alphabet_nest",
      len(set(unitList)) == 4 and len(unitList) == 4,
      "4 distinct units")


# ── the 8 live slots (transcribed from s7aLiveSlots def) ────────────────
# (List.range 2).flatMap a => flatMap b => map c => (a,b,c)
s7aLiveSlots = [(a, b, c) for a in range(2) for b in range(2) for c in range(2)]

check("s7a_live_slot_count", len(s7aLiveSlots) == 8, "8 live (a,b,c) slots")

free = [s for s in s7aLiveSlots if s[0] == 1 and s[1] == 1 and s[2] == 1]
check("s7a_free_slot_count", len(free) == 1, "exactly (1,1,1) free")

pinned = [s for s in s7aLiveSlots if not (s[0] == 1 and s[1] == 1 and s[2] == 1)]
check("s7a_pinned_slot_count", len(pinned) == 7, "7 slots pinned by normalization")


# ── the coboundary at (1,1,1): detaNum/detaDen (transcribed from Zi.lean
#    defs carried in the statements). At (a,b,c)=(1,1,1):
#      detaNum = eta(b,c)·eta(a,(b+c)%2) = eta(1,1)·eta(1,0)
#      detaDen = eta((a+b)%2,c)·eta(a,b) = eta(0,1)·eta(1,1)
def detaNum_111(eta):
    return gmul(eta(1, 1), eta(1, 0))


def detaDen_111(eta):
    return gmul(eta(0, 1), eta(1, 1))


def make_eta(n00, n01, n10, n11):
    def eta(a, b):
        if a == 0 and b == 0:
            return n00
        if a == 0 and b == 1:
            return n01
        if a == 1 and b == 0:
            return n10
        return n11
    return eta


# ── S7a.7  s7a_unit_slice_iff_symmetric : over ALL 4⁴ unit gauges,
#    (detaNum(1,1,1) = detaDen(1,1,1)) ↔ (n01 = n10). Full finite sweep. ─
iff_holds = True
witness_true = 0   # count gauges where slot fixed
witness_sym = 0    # count gauges with n01=n10
for n00 in unitList:
    for n01 in unitList:
        for n10 in unitList:
            for n11 in unitList:
                eta = make_eta(n00, n01, n10, n11)
                fixed = (detaNum_111(eta) == detaDen_111(eta))
                symm = (n01 == n10)
                if fixed:
                    witness_true += 1
                if symm:
                    witness_sym += 1
                if fixed != symm:
                    iff_holds = False
check("s7a_unit_slice_iff_symmetric", iff_holds,
      f"256 gauges swept; slot-fixed⇔symmetric (fixed={witness_true}, sym={witness_sym})")


# ── S7a.8  s7a_unit_slice_orbit_closed : n01=n10 → slot fixed ───────────
orbit_closed = True
for n00 in unitList:
    for n01 in unitList:
        for n10 in unitList:
            for n11 in unitList:
                if n01 == n10:
                    eta = make_eta(n00, n01, n10, n11)
                    if detaNum_111(eta) != detaDen_111(eta):
                        orbit_closed = False
check("s7a_unit_slice_orbit_closed", orbit_closed,
      "every symmetric unit gauge fixes the (1,1,1) slot")


# ── S7a.9  s7a_live_unit_gauge : η11=i, else 1 — fixes slot, ≠ id, unit ─
eta_live = lambda a, b: I if (a == 1 and b == 1) else ONE
check("s7a_live_unit_gauge",
      detaNum_111(eta_live) == detaDen_111(eta_live)
      and eta_live(1, 1) != ONE
      and normSq(eta_live(1, 1)) == 1,
      "η11=i is a live non-identity slice-fixing unit gauge")


# ── S7a.10 s7a_control_asymmetric_unit_moves_slot : η01=i else 1 MOVES ──
eta_ctrl = lambda a, b: I if (a == 0 and b == 1) else ONE
check("s7a_control_asymmetric_unit_moves_slot",
      detaNum_111(eta_ctrl) != detaDen_111(eta_ctrl) and I != ONE,
      "asymmetric unit gauge genuinely moves the slot")


# ── S7a.11 s7a_nonunit_outside_alphabet : ⟨2,0⟩ has norm 4, ∉ unitList ──
check("s7a_nonunit_outside_alphabet",
      normSq((2, 0)) != 1 and (2, 0) not in unitList,
      "the impossibility marker: ⟨2,0⟩ (norm 4) is outside the unit locus")


# ── verdict ─────────────────────────────────────────────────────────────
n = len(CHECKS)
passed = sum(1 for _, ok in CHECKS if ok)
print("-" * 60)
print(f"SEAT B (S7a): {passed}/{n} checks pass")
if passed == n:
    print("RESULT: PASS — every S7a statement independently reproduced.")
    sys.exit(0)
else:
    print("RESULT: FAIL")
    sys.exit(1)
