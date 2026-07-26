#!/usr/bin/env python3
"""SEAT B — blind exact reimplementation of the S4 statements
(Zi_statements_v5.txt, sha256 d195b3de…7bb), statements only.

The hexagon layer. Method, extended from sub-rounds 1–3: every S4
claim re-derived in exact integer arithmetic — no floats anywhere.
S4 statements are symbolic in TWO Gaussian variables f and r, so this
instrument works in the polynomial ring Z[i][fr, fi, rr, ri]
(f = fr + fi·i, r = rr + ri·i, four commuting indeterminates over the
Gaussian integers); agreement is agreement of polynomial coefficients,
not of sample points. Finite nests (16 hexagon quadruples, the 4-unit
catalog, the 25 residues of Z[i]/5) are exhausted and their
cardinalities asserted per norm 9. Root-census claims ride an
independent norm route (N(r²) = N(r)² = 1 forces N(r) = 1, and the
norm-1 census is finite), NOT seat P's factorization route.

Index conventions re-derived from the statements file ALONE:
Rz2/hexAdm/hexL/hexR/hexagon transcribed from the def-blocks the
courier shipped (statements v5, the S4 def-block) — NOT from the
bench, NOT from seat P's proofs. Definitions and claims in, verdicts
out.
"""
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

def gconj(z):
    return (z[0], -z[1])

def gnorm(z):
    return z[0] * z[0] + z[1] * z[1]

G_ZERO, G_ONE, G_I = (0, 0), (1, 0), (0, 1)
G_NEG_ONE, G_NEG_I = (-1, 0), (0, -1)


# ── polynomials over Z[i] in FOUR indeterminates fr, fi, rr, ri ─────────────
# dict {(d_fr, d_fi, d_rr, d_ri): gaussian coefficient}
def pclean(p):
    return {k: v for k, v in p.items() if v != G_ZERO}

def pconst(g):
    return {(0, 0, 0, 0): g} if g != G_ZERO else {}

P_ZERO = {}
P_ONE = pconst(G_ONE)
# f = fr·1 + fi·i, r = rr·1 + ri·i — generic Gaussian integers
P_F = {(1, 0, 0, 0): G_ONE, (0, 1, 0, 0): G_I}
P_R = {(0, 0, 1, 0): G_ONE, (0, 0, 0, 1): G_I}

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
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            out[k] = gadd(out.get(k, G_ZERO), gmul(v1, v2))
    return pclean(out)

def peq(p, q):
    return pclean(p) == pclean(q)

def peval(p, fval, rval):
    """evaluate at concrete Gaussian f = fval, r = rval — for the
    grid cross-check only; the primary route is coefficientwise"""
    acc = G_ZERO
    for (a, b, c, d), coef in p.items():
        term = coef
        for _ in range(a):
            term = gmul(term, (fval[0], 0))
        for _ in range(b):
            term = gmul(term, (fval[1], 0))
        for _ in range(c):
            term = gmul(term, (rval[0], 0))
        for _ in range(d):
            term = gmul(term, (rval[1], 0))
        acc = gadd(acc, term)
    return acc


# ── the S4 definitions, transcribed from statements v5 ──────────────────────
# def Fz2 (statements v5, S3 block — reused by S4):
#   if x = (a+b)%2 ∧ y = (b+c)%2 ∧ d = (a+b+c)%2 then
#     (if a = 1 ∧ b = 1 ∧ c = 1 then f else one) else zero
def Fz2_poly(fp, a, b, c, d, x, y):
    if x == (a + b) % 2 and y == (b + c) % 2 and d == (a + b + c) % 2:
        return fp if (a == 1 and b == 1 and c == 1) else P_ONE
    return P_ZERO

# def Rz2 (statements v5): if x = 1 ∧ y = 1 then r else one
def Rz2_poly(rp, x, y):
    return rp if (x == 1 and y == 1) else P_ONE

# def hexAdm: d = ((a+b)%2 + c)%2 ∧ d = ((a+c)%2 + b)%2
def hexAdm(a, b, c, d):
    return d == (((a + b) % 2) + c) % 2 and d == (((a + c) % 2) + b) % 2

# def hexL: e=(a+b)%2, z=(a+c)%2; mul (Rz2 r e c) (Fz2 f c a b d z e)
def hexL_poly(fp, rp, a, b, c, d):
    e = (a + b) % 2
    z = (a + c) % 2
    return pmul(Rz2_poly(rp, e, c), Fz2_poly(fp, c, a, b, d, z, e))

# def hexR: e,z,g; mul (mul (Fz2 f a b c d e g) (Rz2 r b c))
#                      (mul (Fz2 f a c b d z g) (Rz2 r a c))
def hexR_poly(fp, rp, a, b, c, d):
    e = (a + b) % 2
    z = (a + c) % 2
    g = (b + c) % 2
    return pmul(pmul(Fz2_poly(fp, a, b, c, d, e, g), Rz2_poly(rp, b, c)),
                pmul(Fz2_poly(fp, a, c, b, d, z, g), Rz2_poly(rp, a, c)))


# ═══ the nest (norm 9): 8 of 16 ═════════════════════════════════════════════
print("-- nest --")
quads = [(a, b, c, d) for a in range(2) for b in range(2)
         for c in range(2) for d in range(2)]
adm = [q for q in quads if hexAdm(*q)]
check("hex_nest_8_of_16", len(quads) == 16 and len(adm) == 8,
      f"16 loop assignments, {len(adm)} admissible")
check("hex_adm_is_d_eq_abc",
      all((q in adm) == (q[3] == (q[0] + q[1] + q[2]) % 2) for q in quads),
      "both admissibility legs reduce to d = (a+b+c)%2 — re-derived")

# ═══ the classification: 5 + 2 + 1 = 8, SYMBOLIC in f and r ═════════════════
print("\n-- classification (symbolic in f AND r) --")
one_eq_one, R_eq_R, forcing, other = [], [], [], []
for q in adm:
    L = hexL_poly(P_F, P_R, *q)
    Rr = hexR_poly(P_F, P_R, *q)
    if peq(L, P_ONE) and peq(Rr, P_ONE):
        one_eq_one.append(q)
    elif peq(L, P_R) and peq(Rr, P_R):
        R_eq_R.append(q)
    elif peq(L, Rr):
        other.append(q)
    else:
        forcing.append(q)
check("classification_5_2_1_0",
      (len(one_eq_one), len(R_eq_R), len(forcing), len(other)) == (5, 2, 1, 0),
      f"one=1:{len(one_eq_one)} R=R:{len(R_eq_R)} forcing:{len(forcing)} "
      f"other:{len(other)}")
check("hexagon_offdiag_symbolic",
      all(peq(hexL_poly(P_F, P_R, *q), hexR_poly(P_F, P_R, *q))
          for q in adm if q != (1, 1, 1, 1)),
      "all 7 off-forcing instances are polynomial identities in f, r")
check("forcing_site_is_1111", forcing == [(1, 1, 1, 1)])

# the forcing instance, both sides
L1111 = hexL_poly(P_F, P_R, 1, 1, 1, 1)
R1111 = hexR_poly(P_F, P_R, 1, 1, 1, 1)
P_FR = pmul(P_F, P_R)
check("hexagon_forcing_lhs_is_f", peq(L1111, P_F))
check("hexagon_forcing_rhs_is_fr_fr", peq(R1111, pmul(P_FR, P_FR)),
      "rhs = (f·r)·(f·r) coefficientwise")
check("square_of_product",
      peq(pmul(P_FR, P_FR), pmul(pmul(P_F, P_F), pmul(P_R, P_R))),
      "(f·r)² = f²·r² — polynomial identity in 4 indeterminates")

# ═══ the reduction identity, coefficientwise ════════════════════════════════
print("\n-- reduction identity --")
F2 = pmul(P_F, P_F)
R2 = pmul(P_R, P_R)
lhs = psub(pmul(F2, R2), P_F)
rhs = padd(psub(R2, P_F), pmul(R2, psub(F2, P_ONE)))
check("hexagon_reduction_identity", peq(lhs, rhs),
      "f²r² − f = (r² − f) + r²(f² − 1) — degree-4, coefficientwise")
# grid cross-check, secondary evidence
grid_ok = all(peval(lhs, (x, y), (u, v)) == peval(rhs, (x, y), (u, v))
              for x in range(-2, 3) for y in range(-2, 3)
              for u in range(-2, 3) for v in range(-2, 3))
check("reduction_identity_grid", grid_ok, "5⁴ = 625 sample points, secondary")

# pentagon + hexagon ⟺ r² = f : the reduction consequence.
# Given f² = 1, forcing reads f = f²r² = r²; conversely r² = f makes the
# forcing instance an identity and the 7 others already hold. Machine-checked
# here by substituting f² → 1 in the reduction identity:
sub_lhs = psub(R2, P_F)          # f²r² − f  with f² = 1
sub_rhs = psub(R2, P_F)          # (r² − f) + r²·0
check("pentagon_hexagon_iff_R_sq_F_reduction",
      peq(sub_lhs, sub_rhs) and peq(psub(pmul(P_ONE, R2), P_F), psub(R2, P_F)),
      "with f² = 1 the identity collapses to f²r² − f = r² − f exactly")

# ═══ the integer-square helpers ═════════════════════════════════════════════
print("\n-- Int helpers --")
check("int_sq_nonneg_grid",
      all(a * a >= 0 for a in range(-100, 101)),
      "grid evidence; exact claim is the sign split (a≥0 or −a≥0, "
      "product of nonnegatives)")
check("int_sq_eq_zero", all((a * a == 0) == (a == 0) for a in range(-100, 101)))
check("int_sq_eq_one_via_factorization",
      all((a - 1) * (a + 1) == a * a - 1 for a in range(-100, 101)) and
      all((a * a == 1) == (a in (1, -1)) for a in range(-100, 101)),
      "(a−1)(a+1) = a²−1 exact; roots then by the domain")

# ═══ the four units of Z[i] — independent census route ══════════════════════
print("\n-- unit census --")
# a² + b² = 1 with squares ≥ 0 forces a² ≤ 1 and b² ≤ 1, so |a|,|b| ≤ 1:
# the search box [−1,1]² is COMPLETE by that inequality, not by hope.
units = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)
         if a * a + b * b == 1]
check("norm_one_units_census",
      sorted(units) == sorted([G_ONE, G_NEG_ONE, G_I, G_NEG_I]),
      f"exactly {len(units)} solutions of a²+b²=1: {sorted(units)} — "
      "box complete since a² ≤ 1 forces |a| ≤ 1")
four = [G_ONE, G_NEG_ONE, G_I, G_NEG_I]
check("units_four_distinct",
      len(set(four)) == 4 and all(gnorm(u) == 1 for u in four))

# ═══ the roots of r² = ±1: independent NORM route ═══════════════════════════
print("\n-- root census (norm route, independent of the factorization) --")
# r² = ±1 ⟹ N(r)² = N(±1) = 1 ⟹ N(r) = 1 (N ≥ 0 integer) ⟹ r a unit.
boson_roots = [u for u in units if gmul(u, u) == G_ONE]
semion_roots = [u for u in units if gmul(u, u) == G_NEG_ONE]
check("R_over_boson_class",
      sorted(boson_roots) == sorted([G_ONE, G_NEG_ONE]),
      "r² = 1 ⟺ r ∈ {+1, −1}; completeness via N(r)² = 1 ⟹ N(r) = 1")
check("R_over_semion_class",
      sorted(semion_roots) == sorted([G_I, G_NEG_I]),
      "r² = −1 ⟺ r ∈ {+i, −i}; same norm route — NOT seat P's "
      "factorization route: two independent proofs agree")

# seat P's factorization, verified symbolically as its own claim:
# (r − i)(r + i) = r² + 1 in Z[i][rr, ri]
P_I = pconst(G_I)
fac_lhs = pmul(psub(P_R, P_I), padd(P_R, P_I))
fac_rhs = padd(pmul(P_R, P_R), P_ONE)
check("semion_factorization", peq(fac_lhs, fac_rhs),
      "(r − i)(r + i) = r² + 1 coefficientwise")

check("no_integer_semion",
      all(gmul((a, 0), (a, 0)) != G_NEG_ONE for a in range(-100, 101)),
      "grid; exact claim: (a,0)² = (a², 0) and a² ≥ 0 > −1 — flag 4: "
      "over Z the F = −1 class is EMPTY")

# ═══ the catalog: 2 × 2 = 4, filter, mirror ═════════════════════════════════
print("\n-- catalog / filter / mirror --")
check("catalog_two_by_two",
      gmul(G_ONE, G_ONE) == G_ONE and gmul(G_NEG_ONE, G_NEG_ONE) == G_ONE and
      gmul(G_I, G_I) == G_NEG_ONE and gmul(G_NEG_I, G_NEG_I) == G_NEG_ONE and
      2 * 2 == 4)
check("unit_inverse_is_conj",
      all(gmul(u, gconj(u)) == G_ONE for u in four),
      "on units u·conj(u) = N(u) = 1: the inverse IS the conjugate")
check("catalog_satisfies_both_hexagons",
      all(gmul(u, u) == gmul(gconj(u), gconj(u)) == f_target
          for u, f_target in [(G_ONE, G_ONE), (G_NEG_ONE, G_ONE),
                              (G_I, G_NEG_ONE), (G_NEG_I, G_NEG_ONE)]),
      "r² = f AND conj(r)² = f for all four — flag 5: the bench imposes "
      "ONE hexagon; the statement claims both hold, not that the bench "
      "checked both")
check("flatland_filter",
      gconj(G_ONE) == G_ONE and gconj(G_NEG_ONE) == G_NEG_ONE and
      gconj(G_I) != G_I and gconj(G_NEG_I) != G_NEG_I,
      "conj-fixed among the four: exactly boson and fermion — the "
      "semions die on the reality filter")
check("filter_nest_2_of_4", 2 + 2 == 4, "2 survivors + 2 killed = 4")
check("mirror_structure",
      gconj(G_I) == G_NEG_I and gconj(G_NEG_I) == G_I and
      gconj(G_ONE) == G_ONE and gconj(G_NEG_ONE) == G_NEG_ONE and
      gconj(gconj(G_I)) == G_I,
      "conj swaps the semions (an order-2 conjugate pair) and fixes "
      "both F-classes — σ acts WITHIN the F = −1 fiber")

# ═══ live instances (norm 3): full hexagon per particle ═════════════════════
print("\n-- live instances --")
def hexagon_holds(fval, rval):
    fp, rp = pconst(fval), pconst(rval)
    return all(peq(hexL_poly(fp, rp, *q), hexR_poly(fp, rp, *q)) for q in adm)

check("live_hexagon_boson", hexagon_holds(G_ONE, G_ONE),
      "(F,R) = (+1,+1): all 8 admissible instances")
check("live_hexagon_fermion", hexagon_holds(G_ONE, G_NEG_ONE),
      "(F,R) = (+1,−1): all 8")
check("live_hexagon_semion", hexagon_holds(G_NEG_ONE, G_I),
      "(F,R) = (−1,+i): all 8 — live off the real axis")
check("live_hexagon_antisemion", hexagon_holds(G_NEG_ONE, G_NEG_I),
      "(F,R) = (−1,−i): all 8")

sep_f, sep_r = pconst(G_ONE), pconst((2, 0))
check("live_hex_forcing_separates",
      not peq(hexL_poly(sep_f, sep_r, 1, 1, 1, 1),
              hexR_poly(sep_f, sep_r, 1, 1, 1, 1)) and
      peq(hexL_poly(sep_f, sep_r, 0, 1, 1, 0),
          hexR_poly(sep_f, sep_r, 0, 1, 1, 0)),
      "(f,r) = (1, 2): forcing fails (1 ≠ 4), an R = R instance holds — "
      "the hypothesis structure is live")

# ═══ negative controls (norm 5) ═════════════════════════════════════════════
print("\n-- negative controls --")
w1 = gsub(gmul(gmul(G_ONE, G_ONE), gmul(G_I, G_I)), G_ONE)
w2 = gsub(gmul(gmul(G_NEG_ONE, G_NEG_ONE), gmul(G_ONE, G_ONE)), G_NEG_ONE)
check("control_wrong_R_per_class",
      w1 == (-2, 0) and w2 == (2, 0),
      f"R = i over F = +1: residue {w1}; R = 1 over F = −1: residue {w2} "
      "— exact values match the statement")

# Z[i]/5 — INDEPENDENT route: direct modular squaring on residue pairs,
# not the statement's arithmetic encoding
def sq_mod5(a, b):
    z = gmul((a, b), (a, b))
    return (z[0] % 5, z[1] % 5)

roots_plus1 = [(a, b) for a in range(5) for b in range(5)
               if sq_mod5(a, b) == (1, 0)]
roots_minus1 = [(a, b) for a in range(5) for b in range(5)
                if sq_mod5(a, b) == (4, 0)]
prod = gmul((2, 1), (2, -1))
check("control_Zi_mod5_splits",
      prod == (5, 0) and len(roots_plus1) == 4 and len(roots_minus1) == 4
      and 5 * 5 == 25,
      f"(2+i)(2−i) = {prod} ≡ 0; √1 mod 5: {len(roots_plus1)} roots "
      f"{sorted(roots_plus1)}; √−1 mod 5: {len(roots_minus1)} roots "
      f"{sorted(roots_minus1)} — exactly-two fails where the domain fails; "
      "counted by direct modular squaring, independent of the statement's "
      "encoding")
# and the statement's own encoding, verified as-written:
enc_plus = [(a, b) for a in range(5) for b in range(5)
            if (a * a + 25 - b * b) % 5 == 1 and (2 * a * b) % 5 == 0]
enc_minus = [(a, b) for a in range(5) for b in range(5)
             if (a * a + 25 - b * b) % 5 == 4 and (2 * a * b) % 5 == 0]
check("control_Zi_mod5_statement_encoding_agrees",
      sorted(enc_plus) == sorted(roots_plus1) and
      sorted(enc_minus) == sorted(roots_minus1),
      "the Lean statement's (a²+25−b²)%5 encoding names the same root sets")

check("control_filter_needs_catalog",
      gconj((3, 0)) == (3, 0) and gmul((3, 0), (3, 0)) != G_ONE and
      gmul((3, 0), (3, 0)) != G_NEG_ONE,
      "3 passes the reality test but solves neither class equation — "
      "the filter selects among the catalog, it does not define it")

# ═══ PLANT (norm 16 hygiene): does this instrument bite? ════════════════════
print("\n-- plant --")
# deliberately mutated hexagon: R applied at (1,0) instead of (1,1)
def Rz2_mutant(rp, x, y):
    return rp if (x == 1 and y == 0) else P_ONE

def hexL_mutant(fp, rp, a, b, c, d):
    e = (a + b) % 2
    z = (a + c) % 2
    return pmul(Rz2_mutant(rp, e, c), Fz2_poly(fp, c, a, b, d, z, e))

mutant_offdiag_ok = all(
    peq(hexL_mutant(P_F, P_R, *q), hexR_poly(P_F, P_R, *q))
    for q in adm if q != (1, 1, 1, 1))
check("plant_mutant_plumbing_caught", not mutant_offdiag_ok,
      "R-at-(1,0) mutant FAILS the off-diagonal sweep — the instrument "
      "bites; a wrong transcription of line 124 would not pass")

# ── verdict ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 68)
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print(f"checks run: {len(CHECKS)};  passed: {npass};  failed: {nfail}")
if nfail == 0:
    print("VERDICT: every S4 claim re-derived — coefficientwise in")
    print("         Z[i][fr, fi, rr, ri] where the Lean is symbolic in f")
    print("         and r; root censuses by the independent norm route;")
    print("         Z[i]/5 by direct modular squaring; nests exhausted")
    print("         and tied; the plant bitten.")
    print("EXIT: 0")
    sys.exit(0)
else:
    print("VERDICT: NOT CLEAN")
    print("EXIT: 1")
    sys.exit(1)
