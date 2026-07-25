#!/usr/bin/env python3
"""SEAT B — blind exact reimplementation of the S3 statements
(Zi_statements_v4.txt, sha256 ebd937b4…fa93b), statements only.

Method, same as sub-rounds 1 and 2: every S3 claim re-derived in exact
integer arithmetic — no floats anywhere. Where a statement is symbolic
in f, this instrument works in the polynomial ring Z[i][fr, fi]
(f = fr + fi·i, two commuting indeterminates over the Gaussian
integers), so agreement is agreement of polynomial coefficients, not of
sample points. Where a statement quantifies a finite nest (16 pentagon
quadruples, 8 residues of Z/8), the nest is exhausted and its
cardinality asserted per norm 9. Where a statement quantifies all of
Zi (the gauge theorems, the domain bridges), the symbolic route covers
it exactly; grids appear only as secondary evidence and say so.

Index conventions re-derived from the statements file alone:
Fz2/pentL/pentR/pentagon/detaNum/detaDen are transcribed from the
def-blocks the courier shipped (statements file lines 147–168, 238–241)
— NOT from the bench, NOT from seat P's proofs. That is the blindness
boundary: definitions and claims in, verdicts out.
"""
import itertools
import sys

CHECKS = []


def check(name, ok, note=""):
    CHECKS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {note}" if note else ""))


# ── exact Gaussian integers: pairs (a, b) = a + b·i ─────────────────────────
def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])

def gneg(z):
    return (-z[0], -z[1])

def gsub(z, w):
    return gadd(z, gneg(w))

def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

G_ZERO, G_ONE, G_I = (0, 0), (1, 0), (0, 1)

def gnorm(z):
    return z[0] * z[0] + z[1] * z[1]


# ── polynomials over Z[i] in two indeterminates fr, fi ──────────────────────
# dict {(dr, di): gaussian-coeff}; f itself is fr + fi·i as ONE Gaussian-poly:
# represent an element of Zi[f]-symbolic as a dict over (deg_fr, deg_fi)
# with Gaussian coefficients. Multiplication is the convolution with gmul.
def pconst(g):
    return {(0, 0): g} if g != G_ZERO else {}

P_ZERO = {}
P_ONE = pconst(G_ONE)
# f = fr·1 + fi·i  — the generic Gaussian integer, coordinates symbolic
P_F = {(1, 0): G_ONE, (0, 1): G_I}

def pclean(p):
    return {k: v for k, v in p.items() if v != G_ZERO}

def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = gadd(out.get(k, G_ZERO), v)
    return pclean(out)

def pneg(p):
    return {k: gneg(v) for k, v in p.items()}

def psub(p, q):
    return padd(p, pneg(q))

def pmul(p, q):
    out = {}
    for (i1, j1), a in p.items():
        for (i2, j2), b in q.items():
            k = (i1 + i2, j1 + j2)
            out[k] = gadd(out.get(k, G_ZERO), gmul(a, b))
    return pclean(out)

def peq(p, q):
    return pclean(p) == pclean(q)

def peval(p, f):
    """Evaluate at a concrete Gaussian f = (fr, fi)."""
    tot = G_ZERO
    for (i, j), c in p.items():
        t = c
        for _ in range(i):
            t = gmul(t, (f[0], 0))
        for _ in range(j):
            t = gmul(t, (f[1], 0))
        tot = gadd(tot, t)
    return tot


# ── the S3 defs, transcribed from the statements file ───────────────────────
def Fz2(fpoly, a, b, c, d, x, y):
    """statements file: if x=(a+b)%2 ∧ y=(b+c)%2 ∧ d=(a+b+c)%2 then
    (if a=1 ∧ b=1 ∧ c=1 then f else one) else zero"""
    if x == (a + b) % 2 and y == (b + c) % 2 and d == (a + b + c) % 2:
        return fpoly if (a, b, c) == (1, 1, 1) else P_ONE
    return P_ZERO

def pentL(fpoly, a, b, c, d):
    x = (a + b) % 2
    y = (x + c) % 2
    t = (y + d) % 2
    w = (c + d) % 2
    v = (b + w) % 2
    u = (b + c) % 2
    return pmul(pmul(Fz2(fpoly, a, b, c, y, x, u), Fz2(fpoly, a, u, d, t, y, v)),
                Fz2(fpoly, b, c, d, v, u, w))

def pentR(fpoly, a, b, c, d):
    x = (a + b) % 2
    y = (x + c) % 2
    t = (y + d) % 2
    w = (c + d) % 2
    v = (b + w) % 2
    return pmul(Fz2(fpoly, x, c, d, t, y, w), Fz2(fpoly, a, b, w, t, x, v))

QUADS = list(itertools.product((0, 1), repeat=4))


print("=" * 68)
print("SEAT B — S3 verification: pentagon necessity")
print("statements: Zi_statements_v4.txt (83 theorems; S3 = the new 26)")
print("=" * 68)

# ── nest first (norm 9) ─────────────────────────────────────────────────────
print("\n-- the nest --")
check("pent_nest_card_16", len(QUADS) == 16,
      "16 = 2^4 quadruples; the statements' pentQuads list has the same 16")
PENTQUADS_STMT = [(0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),
                  (0,1,0,0),(0,1,0,1),(0,1,1,0),(0,1,1,1),
                  (1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),
                  (1,1,0,0),(1,1,0,1),(1,1,1,0),(1,1,1,1)]
check("pentQuads_is_the_full_nest", sorted(PENTQUADS_STMT) == sorted(QUADS)
      and len(set(PENTQUADS_STMT)) == 16,
      "the explicit list is exactly {0,1}^4, no repeats, no gaps")

# ── the classification, SYMBOLIC in f ───────────────────────────────────────
print("\n-- the 16-instance classification (symbolic f = fr + fi·i) --")
kinds = {"one_eq_one": [], "f_eq_f": [], "forcing": [], "other": []}
for q in QUADS:
    L, R = pentL(P_F, *q), pentR(P_F, *q)
    if peq(L, R):
        kinds["f_eq_f" if peq(L, P_F) else
              ("one_eq_one" if peq(L, P_ONE) else "other")].append(q)
    elif peq(L, pmul(P_F, P_F)) and peq(R, P_ONE):
        kinds["forcing"].append(q)
    else:
        kinds["other"].append(q)

check("classification_11_4_1_0",
      (len(kinds["one_eq_one"]), len(kinds["f_eq_f"]),
       len(kinds["forcing"]), len(kinds["other"])) == (11, 4, 1, 0),
      "11 read 1=1, 4 read f=f, exactly ONE forces, none other — "
      "as POLYNOMIAL identities in the coordinates of f, any f")
check("counts_tie_to_nest_11_4_1", 11 + 4 + 1 == 16,
      "norm 9: count + count + count = nest")
check("forcing_is_1111", kinds["forcing"] == [(1, 1, 1, 1)],
      "the single forcing instance is (a,b,c,d) = (1,1,1,1)")
check("forcing_lhs_is_f_squared",
      peq(pentL(P_F, 1, 1, 1, 1), pmul(P_F, P_F)),
      "pentagon_forcing_lhs: lhs = f² symbolically")
check("forcing_rhs_is_one", peq(pentR(P_F, 1, 1, 1, 1), P_ONE),
      "pentagon_forcing_rhs: rhs = 1 symbolically")
check("f_eq_f_at_the_four_stated",
      sorted(kinds["f_eq_f"]) == [(0,1,1,1), (1,0,1,1), (1,1,0,1), (1,1,1,0)]
      and all(peq(pentL(P_F, *q), P_F) and peq(pentR(P_F, *q), P_F)
              for q in [(0,1,1,1), (1,0,1,1), (1,1,0,1), (1,1,1,0)]),
      "pent_f_eq_f_instances: the four sites, both sides f, symbolically")
check("offdiag_holds_for_every_f",
      all(peq(pentL(P_F, *q), pentR(P_F, *q))
          for q in QUADS if q != (1, 1, 1, 1)),
      "pentagon_offdiag: the 15 non-forcing instances are identities in f")

# ── pentagon ⟺ f² = 1 ───────────────────────────────────────────────────────
print("\n-- pentagon ⟺ f² = 1 --")
# forward: the forcing instance is the ONLY obstruction (from the
# classification above); backward: with f² = 1 all 16 close.
check("pentagon_iff_f_sq_one_structure",
      peq(psub(pentL(P_F, 1, 1, 1, 1), pentR(P_F, 1, 1, 1, 1)),
          psub(pmul(P_F, P_F), P_ONE)),
      "the single obstruction polynomial is exactly f² − 1")
# concrete: the two roots satisfy all 16; witnesses that don't, don't
def pentagon_holds(f):
    return all(peval(pentL(P_F, *q), f) == peval(pentR(P_F, *q), f)
               for q in QUADS)
check("live_pentagon_plus_one", pentagon_holds((1, 0)),
      "f = +1 satisfies all 16 instances")
check("live_pentagon_minus_one", pentagon_holds((-1, 0)),
      "f = −1 satisfies all 16 instances")
check("live_forcing_separates",
      peval(pentL(P_F, 1, 1, 1, 1), (5, 0)) == (25, 0)
      and peval(pentR(P_F, 1, 1, 1, 1), (5, 0)) == (1, 0)
      and peval(pentL(P_F, 0, 1, 1, 1), (5, 0))
          == peval(pentR(P_F, 0, 1, 1, 1), (5, 0)) == (5, 0),
      "at f = 5: forcing instance separates (25 ≠ 1), f=f instance holds")
# the counted classification at the separating witness (the Lean's route)
c11 = sum(1 for q in PENTQUADS_STMT if peval(pentL(P_F, *q), (5, 0)) == (1, 0))
c4 = sum(1 for q in PENTQUADS_STMT if peval(pentL(P_F, *q), (5, 0)) == (5, 0))
c1 = sum(1 for q in PENTQUADS_STMT if peval(pentL(P_F, *q), (5, 0)) == (25, 0))
check("pent_classification_counted_at_witness",
      (c11, c4, c1) == (11, 4, 1) and 1 != 5 != 25,
      "the Lean's filter counts at f = ⟨5,0⟩: (11, 4, 1); 1, 5, 25 "
      "pairwise distinct so the kinds cannot be conflated")

# ── the algebraic bridge: factorization, domain, exactly two ────────────────
print("\n-- factorization and the domain --")
check("sub_eq_zero_iff",
      all((gsub(z, w) == G_ZERO) == (z == w)
          for z in itertools.product(range(-3, 4), repeat=2)
          for w in itertools.product(range(-3, 4), repeat=2)),
      "z − w = 0 ⟺ z = w — exhaustive on the 49×49 grid (secondary "
      "evidence; the claim is coordinatewise arithmetic, true by Int)")
check("factorization_symbolic",
      peq(pmul(psub(P_F, P_ONE), padd(P_F, P_ONE)),
          psub(pmul(P_F, P_F), P_ONE)),
      "(f−1)(f+1) = f²−1 as polynomials over Z[i] — exact, symbolic")

# f² = 1 ⟺ f = ±1 in Z[i]: independent route — N(f)² = N(f²) = N(1) = 1,
# N ≥ 0 integer ⟹ N(f) = 1 ⟹ f ∈ {±1, ±i} (norm-1 Gaussians: a²+b² = 1
# has exactly 4 integer solutions); check which of the four square to 1.
units = [(a, b) for a in range(-1, 2) for b in range(-1, 2)
         if a * a + b * b == 1]
check("norm_one_units_are_four", sorted(units) == [(-1, 0), (0, -1), (0, 1), (1, 0)],
      "a² + b² = 1 over Z: exactly the four units of Z[i] — nest: the "
      "9-point grid [−1,1]² suffices since a² + b² = 1 forces |a|,|b| ≤ 1")
sq1 = [u for u in units if gmul(u, u) == G_ONE]
check("f_sq_one_iff_pm_one", sorted(sq1) == [(-1, 0), (1, 0)],
      "of the four norm-1 elements, exactly ±1 square to 1 — the "
      "independent route (norm-multiplicativity + unit census), distinct "
      "from the Lean's factorization-through-the-domain route")
check("both_roots_land",
      gmul(G_ONE, G_ONE) == G_ONE and gmul((-1, 0), (-1, 0)) == G_ONE
      and G_ONE != (-1, 0),
      "+1 and −1 both land and are distinct: EXACTLY TWO")
check("pentagon_exactly_two_concrete",
      pentagon_holds((1, 0)) and pentagon_holds((-1, 0))
      and not pentagon_holds((0, 1)) and not pentagon_holds((0, -1))
      and not pentagon_holds((2, 0)) and not pentagon_holds((5, 0)),
      "the headline at six points: both roots satisfy the pentagon; "
      "i, −i, 2, 5 do not — the roots are exactly {+1, −1}")

# ── negative controls (norm 5) ──────────────────────────────────────────────
print("\n-- negative controls --")
z8 = [x for x in range(8) if (x * x) % 8 == 1]
check("control_z8_four_roots", z8 == [1, 3, 5, 7],
      "in Z/8, f² = 1 has FOUR solutions {1,3,5,7} — nest 8 exhausted; "
      "exactly-two is a DOMAIN theorem")
check("control_z8_count_ties", len(z8) + len([x for x in range(8)
      if (x * x) % 8 != 1]) == 8, "norm 9: 4 roots + 4 non-roots = 8")
fi2 = gmul(G_I, G_I)
check("control_f_eq_i_fails",
      not pentagon_holds(G_I) and gsub(fi2, G_ONE) == (-2, 0)
      and gnorm((-2, 0)) == 4,
      "f = i — a UNIT — fails the pentagon; i²−1 = −2, residual N = 4 "
      "exactly (the charge's 'residual exactly 4')")
check("control_f_eq_two_fails", not pentagon_holds((2, 0)),
      "f = 2 fails: 4 ≠ 1 at the forcing instance")

# ── the gauge layer, SYMBOLIC in the four vertex values ─────────────────────
print("\n-- gauge: the slot is an invariant of the normalized slice --")
# η is a function of (a,b) ∈ {0,1}²; four symbolic values n00,n01,n10,n11.
# Polynomials over Z in 4 vars: dict {(e00,e01,e10,e11): int-coeff}.
def qconst(c):
    return {(0, 0, 0, 0): c} if c else {}

def qvar(i):
    k = [0, 0, 0, 0]
    k[i] = 1
    return {tuple(k): 1}

def qmul(p, q):
    out = {}
    for k1, a in p.items():
        for k2, b in q.items():
            k = tuple(x + y for x, y in zip(k1, k2))
            out[k] = out.get(k, 0) + a * b
    return {k: v for k, v in out.items() if v}

def qeq(p, q):
    return p == q

N00, N01, N10, N11 = (qvar(i) for i in range(4))
ETA = {(0, 0): N00, (0, 1): N01, (1, 0): N10, (1, 1): N11}

def deta_num(a, b, c):
    return qmul(ETA[(b, c)], ETA[(a, (b + c) % 2)])

def deta_den(a, b, c):
    return qmul(ETA[((a + b) % 2, c)], ETA[(a, b)])

check("gauge_slot_motion",
      qeq(deta_num(1, 1, 1), qmul(N11, N10))
      and qeq(deta_den(1, 1, 1), qmul(N01, N11)),
      "(dη)(1,1,1): num = η11·η10, den = η01·η11 — the raw motion is "
      "η10/η01, symbolically in 4 vertex variables")
# slice_forces_eta_symmetric: the (1,0,0) and (0,0,1) conditions in cleared
# form reduce to η00 = η10 and η01 = η00 — check the cleared identities:
check("slice_condition_100_reads_n00_eq_n10",
      qeq(deta_num(1, 0, 0), qmul(N00, N10))
      and qeq(deta_den(1, 0, 0), qmul(N10, N10)),
      "(dη)(1,0,0): num = η00·η10, den = η10·η10 — num = den cancels "
      "(η10 a unit) to η00 = η10")
check("slice_condition_001_reads_n01_eq_n00",
      qeq(deta_num(0, 0, 1), qmul(N01, N01))
      and qeq(deta_den(0, 0, 1), qmul(N01, N00)),
      "(dη)(0,0,1): num = η01·η01, den = η01·η00 — num = den cancels "
      "(η01 a unit) to η01 = η00")
# the invariance: substitute n01 → n10 (the forced equality) in the slot
# motion and check num = den — polynomial substitution, exact:
def qsubst_01_to_10(p):
    out = {}
    for (e00, e01, e10, e11), c in p.items():
        k = (e00, 0, e10 + e01, e11)
        out[k] = out.get(k, 0) + c
    return {k: v for k, v in out.items() if v}

check("gauge_slot_invariant_symbolic",
      qeq(qsubst_01_to_10(deta_num(1, 1, 1)), qsubst_01_to_10(deta_den(1, 1, 1)))
      and not qeq(deta_num(1, 1, 1), deta_den(1, 1, 1)),
      "with η01 = η10 the slot motion is trivial (num = den identically); "
      "WITHOUT the substitution they differ — the invariance is earned, "
      "not built in")
# live witness and control, concrete over Z[i]:
def eta_wit(a, b):
    return G_I if (a, b) == (1, 1) else G_ONE

def geta_num(eta, a, b, c):
    return gmul(eta(b, c), eta(a, (b + c) % 2))

def geta_den(eta, a, b, c):
    return gmul(eta((a + b) % 2, c), eta(a, b))

check("live_gauge_witness",
      geta_num(eta_wit, 1, 0, 0) == geta_den(eta_wit, 1, 0, 0)
      and geta_num(eta_wit, 0, 0, 1) == geta_den(eta_wit, 0, 0, 1)
      and geta_num(eta_wit, 1, 1, 1) == geta_den(eta_wit, 1, 1, 1)
      and eta_wit(1, 1) != G_ONE,
      "η11 = i (the FREE vertex value), all else 1: slice-preserving, "
      "slot unmoved, and not the identity gauge")

def eta_bad(a, b):
    return (2, 0) if (a, b) == (0, 1) else G_ONE

check("control_gauge_moves_slot",
      geta_num(eta_bad, 0, 0, 1) != geta_den(eta_bad, 0, 0, 1)
      and geta_num(eta_bad, 1, 1, 1) != geta_den(eta_bad, 1, 1, 1),
      "NEGATIVE CONTROL: η01 = 2 breaks a zero-slot condition AND moves "
      "the slot — invariance is a consequence of slice-preservation")
# mul_left_cancel — the domain bridge the gauge proof leans on:
check("mul_left_cancel_grid",
      all(x == y
          for a in [(1, 0), (0, 1), (2, -1), (-3, 2)]
          for x in itertools.product(range(-2, 3), repeat=2)
          for y in itertools.product(range(-2, 3), repeat=2)
          if gmul(a, x) == gmul(a, y)),
      "a·x = a·y ⟹ x = y for a ≠ 0 — grid evidence on 4 nonzero a × "
      "25×25 pairs (the exact claim rides on no_zero_divisors, certified "
      "in S2 by two routes)")

# ── the boundary of the claim (charter flag 2) ──────────────────────────────
print("\n-- wording boundary --")
check("headline_is_slice_plus_invariance_shaped",
      True,
      "PROSE CHECK, not machine-checkable here: the statements file's "
      "pentagon_exactly_two + gauge_slot_invariant together are the "
      "slice-plus-invariance form; no statement in v4 says 'H³' or "
      "'every class meets the slice' — seat B read all 26 S3 statements "
      "for this; the sentence is a REVIEW claim, honestly labeled")

# ── verdict ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 68)
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print(f"checks run: {len(CHECKS)};  passed: {npass};  failed: {nfail}")
if nfail == 0:
    print("VERDICT: every S3 claim re-derived — symbolic (polynomial-exact)")
    print("         where the Lean is symbolic in f or in the gauge, the")
    print("         independent norm-census route for the root count,")
    print("         nests exhausted and tied where finite.")
    print("EXIT: 0")
    sys.exit(0)
else:
    print("VERDICT: NOT CLEAN")
    print("EXIT: 1")
    sys.exit(1)
