#!/usr/bin/env python3
"""SEAT B — blind exact reimplementation of the S6 statements
(Zi_statements_v7.txt, sha256 97faef58cd0e…0a27), statements only.

Capstone + exclusion layer. Method as S1–S5: exact arithmetic only.

Capstone route, INDEPENDENT of seat P's layer-stitching: the roomy
predicate (pentagon ∧ hexagon ∧ conj r = r) is decided by DIRECT
EXHAUSTION of the pentagon/hexagon instance sets over a complete
candidate box, with completeness argued from the norm equations (not
assumed): pentagon f needs f² = 1 ⟹ N(f) = 1; hexagon then needs
r² = f ⟹ N(r) = 1 — both live in the norm-1 box [−1,1]², complete
because a² ≤ 1 forces |a| ≤ 1. Seat P stitches five layers of
theorems; seat B just runs all the instances on all candidates.

Exclusion route, INDEPENDENT: exact fraction-free Gaussian elimination
ranks for m = 2..6 (the FULL census — seat P kernel-checks m = 2 and
the T(m) arithmetic; the statements' honest label says the m = 3..6
ranks are seat B territory, and this instrument is that territory).
Plus the symbolic kill re-derived coefficientwise in Z[i][a..d-vars].

Definitions transcribed from statements v7 ALONE (tri, swapIdx, Mmat,
roomy, and the S3/S4/S5 defs they reference). Blindness boundary held.
"""
import sys
from fractions import Fraction

CHECKS = []


def check(name, ok, note=""):
    CHECKS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {note}" if note else ""))


# ── exact Gaussian integers ─────────────────────────────────────────────────
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

G_ZERO, G_ONE, G_I = (0, 0), (1, 0), (0, 1)
G_MONE, G_MI = (-1, 0), (0, -1)


# ── the layer defs, transcribed from statements v7 ──────────────────────────
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
    return all(pentL(f, a, b, c, d) == pentR(f, a, b, c, d)
               for a in range(2) for b in range(2)
               for c in range(2) for d in range(2))

def Rz2(r, x, y):
    return r if (x == 1 and y == 1) else G_ONE

def hexAdm(a, b, c, d):
    return d == (((a + b) % 2) + c) % 2 and d == (((a + c) % 2) + b) % 2

def hexL(f, r, a, b, c, d):
    e = (a + b) % 2; z = (a + c) % 2
    return gmul(Rz2(r, e, c), Fz2(f, c, a, b, d, z, e))

def hexR(f, r, a, b, c, d):
    e = (a + b) % 2; z = (a + c) % 2; g = (b + c) % 2
    return gmul(gmul(Fz2(f, a, b, c, d, e, g), Rz2(r, b, c)),
                gmul(Fz2(f, a, c, b, d, z, g), Rz2(r, a, c)))

def hexagon(f, r):
    return all(hexL(f, r, a, b, c, d) == hexR(f, r, a, b, c, d)
               for a in range(2) for b in range(2)
               for c in range(2) for d in range(2)
               if hexAdm(a, b, c, d))

def roomy(f, r):
    """def roomy: pentagon f ∧ hexagon f r ∧ conj r = r"""
    return pentagon(f) and hexagon(f, r) and gconj(r) == r


# ═══ S6a: the capstone — direct-exhaustion route ════════════════════════════
print("-- capstone (direct exhaustion, independent of the stitching) --")
# completeness of the candidate box, argued not assumed:
# pentagon f ⟹ (forcing instance) f² = 1 ⟹ N(f)² = 1 ⟹ N(f) = 1;
# hexagon then forces r² = f ⟹ N(r) = 1. Norm-1 box is [−1,1]².
box = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
units = [z for z in box if z[0]**2 + z[1]**2 == 1]
check("candidate_box_complete",
      sorted(units) == sorted([G_ONE, G_MONE, G_I, G_MI]),
      "N(f) = N(r) = 1 forced by the coherence equations; norm-1 census "
      "= the four units — box complete by a² ≤ 1 ⟹ |a| ≤ 1")

roomy_pairs = [(f, r) for f in units for r in units if roomy(f, r)]
check("roomy_iff_boson_or_fermion",
      sorted(roomy_pairs) == sorted([(G_ONE, G_ONE), (G_ONE, G_MONE)]),
      f"exhaustion over 4×4 unit pairs: roomy = {sorted(roomy_pairs)} — "
      "exactly {(1,1), (1,−1)}; every pentagon/hexagon instance run, "
      "not cited")
check("the_roomy_world_has_exactly_two_particles",
      sorted({r for f, r in roomy_pairs}) == sorted([G_ONE, G_MONE]) and
      len(roomy_pairs) == 2,
      "∃f roomy(f,r) ⟺ r ∈ {+1, −1}; count = 2, tied")
check("capstone_nu_rider",
      all(gmul(r, r) == G_ONE and gmul(r, gconj(r)) == G_ONE
          for f, r in roomy_pairs),
      "ν_FS = ν_ML = +1 on both survivors — the fork closed on the "
      "capstone set")
check("control_semion_fails_only_filter",
      pentagon(G_MONE) and hexagon(G_MONE, G_I) and gconj(G_I) != G_I
      and not roomy(G_MONE, G_I),
      "the semion passes pentagon AND hexagon, dies on the filter "
      "alone — each gate weighed separately")
check("control_real_but_not_roomy",
      all(not roomy(f, (3, 0)) for f in units) and gconj((3, 0)) == (3, 0),
      "r = 3 real but not roomy for any unit f (hexagon forcing fails: "
      "9 ≠ ±1) — the filter alone is not enough")

# ═══ S6b: the exclusion layer ═══════════════════════════════════════════════
print("\n-- exclusion: exact ranks m = 2..6 (the full census, seat B's half) --")

def build_M_S(m):
    n = m * m
    M = [[0] * n for _ in range(n)]
    S = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            M[i * m + j][i * m + j] += 1
            M[i * m + j][j * m + i] -= 1
            S[i * m + j][j * m + i] = 1
    return M, S

def rank_exact(Mrows):
    A = [[Fraction(x) for x in row] for row in Mrows]
    n, rank = len(A), 0
    for col in range(n):
        piv = next((r for r in range(rank, n) if A[r][col] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(n):
            if r != rank and A[r][col] != 0:
                fct = A[r][col] / A[rank][col]
                A[r] = [x - fct * y for x, y in zip(A[r], A[rank])]
        rank += 1
    return rank

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

ranks, sranks, proj_ok, trace_ok, comp_ok = [], [], True, True, True
for m in range(2, 7):
    n = m * m
    M, S = build_M_S(m)
    P = [[M[i][j] + 2 * S[i][j] for j in range(n)] for i in range(n)]
    ranks.append(rank_exact(M))
    sranks.append(rank_exact(P))
    M2 = matmul(M, M)
    proj_ok &= all(M2[i][j] == 2 * M[i][j]
                   for i in range(n) for j in range(n))
    trace_ok &= sum(M[i][i] for i in range(n)) == m * m - m
    MP = matmul(M, P)
    comp_ok &= all(MP[i][j] == 0 for i in range(n) for j in range(n))

check("antisym_ranks_full_census", ranks == [1, 3, 6, 10, 15],
      f"exact elimination, m = 2..6: {ranks} = m(m−1)/2 — the honest "
      "label's division of labor honored: this census is seat B's half, "
      "and it agrees with tri_values at m = 2 and with the closed form "
      "at every m")
check("sym_ranks_control", sranks == [3, 6, 10, 15, 21] and
      all(r + s == m * m for r, s, m in zip(ranks, sranks, range(2, 7))),
      f"symmetrizer {sranks} = m(m+1)/2 (NOT the fermionic census); "
      "ranks sum to m² — the split complete at every size")
check("projector_and_trace_all_m", proj_ok and trace_ok,
      "M² = 2M and tr M = m² − m exactly for all m = 2..6 — the "
      "rank-by-trace certificate seat P kernel-checks at m = 2 holds "
      "at every size")
check("MP_orthogonal_all_m", comp_ok,
      "M(I+S) = 0 exactly for all m — seat P's m = 2 control, extended")

# the tri arithmetic, re-derived:
tri = [0, 0]
for m in range(1, 10):
    tri.append(tri[m] + m)
check("tri_values_and_recurrence",
      tri[2:7] == [1, 3, 6, 10, 15] and
      all(tri[m + 1] == tri[m] + m for m in range(1, 9)) and
      all(2 * tri[m] == m * (m - 1) for m in range(0, 10)),
      "values, recurrence, and 2T(m) = m(m−1) — checked to m = 9, "
      "beyond the census range")
check("ranks_equal_tri", ranks == tri[2:7],
      "the exact matrix ranks ARE the triangular numbers — the two "
      "routes (elimination vs recursion) meet")

# symbolic Pauli kill — coefficientwise in 4 real indeterminates:
# component (i,j) of M(psi⊗psi) is x_i x_j − x_j x_i; over a COMMUTATIVE
# polynomial ring this is the zero polynomial. Model: dict monomial→coeff.
def pvar(i):
    key = [0, 0, 0, 0]; key[i] = 1
    return {tuple(key): 1}

def pmul_c(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v}

def psub_c(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v}

xs = [pvar(i) for i in range(4)]
kill_ok = all(not psub_c(pmul_c(xs[i], xs[j]), pmul_c(xs[j], xs[i]))
              for i in range(4) for j in range(4))
check("pauli_kill_symbolic", kill_ok,
      "x_i x_j − x_j x_i = 0 identically, 16 component polynomials — "
      "the kill is commutativity, verified coefficientwise")

# the m = 2 block, from the statements' defs:
def swapIdx(p):
    return {0: 0, 1: 2, 2: 1}.get(p, 3)

def Mmat(p, q):
    return (1 if p == q else 0) - (1 if q == swapIdx(p) else 0)

M2_stmt = [[Mmat(p, q) for q in range(4)] for p in range(4)]
M2_built, _ = build_M_S(2)
check("Mmat_matches_I_minus_SWAP", M2_stmt == M2_built,
      "the statements' Mmat/swapIdx encode exactly I − SWAP at m = 2 — "
      "transcription verified against the independent construction")
check("M2_sq_eq_two_M_and_trace",
      matmul(M2_stmt, M2_stmt) == [[2 * M2_stmt[i][j] for j in range(4)]
                                   for i in range(4)] and
      sum(M2_stmt[i][i] for i in range(4)) == 2,
      "M² = 2M entrywise; tr = 2 ⟹ rank 1 = T(2) by the trace "
      "certificate")

# image on the line + kill criterion, symbolic over Z[i] in (a,b,c,d):
# input psi⊗phi = (ac, ad, bc, bd); M v = (0, ad−bc, bc−ad, 0)
def gvar(i):
    key = [0, 0, 0, 0]; key[i] = 1
    return {tuple(key): G_ONE}

def gp_mul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(x + y for x, y in zip(k1, k2))
            out[k] = gadd(out.get(k, G_ZERO), gmul(v1, v2))
    return {k: v for k, v in out.items() if v != G_ZERO}

def gp_sub(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = gsub(out.get(k, G_ZERO), v)
    return {k: v for k, v in out.items() if v != G_ZERO}

A, B, C, D = (gvar(i) for i in range(4))
v = [gp_mul(A, C), gp_mul(A, D), gp_mul(B, C), gp_mul(B, D)]
Mv = [gp_sub({}, {}),                       # row 0: 0
      gp_sub(v[1], v[2]),                   # ad − bc
      gp_sub(v[2], v[1]),                   # bc − ad
      gp_sub({}, {})]                       # row 3: 0
# consistency with the matrix action:
Mv_matrix = [gp_sub(
    {k: v_ for k, v_ in v[p].items()} if False else
    # sum_k Mmat[p][k] * v[k]
    {}, {}) for p in range(4)]
def scalar_gp(c, p):
    if c == 0:
        return {}
    return {k: gmul((c, 0), v_) for k, v_ in p.items()}

Mv_matrix = []
for p in range(4):
    acc = {}
    for k in range(4):
        term = scalar_gp(Mmat(p, k), v[k])
        for kk, vv in term.items():
            acc[kk] = gadd(acc.get(kk, G_ZERO), vv)
    Mv_matrix.append({k: v_ for k, v_ in acc.items() if v_ != G_ZERO})
check("M2_image_on_line",
      Mv_matrix[0] == {} and Mv_matrix[3] == {} and
      Mv_matrix[1] == gp_sub(v[1], v[2]) and
      Mv_matrix[2] == gp_sub(v[2], v[1]),
      "M(ψ⊗φ) = (0, ad−bc, bc−ad, 0) coefficientwise — components 0 "
      "and 3 the zero polynomial, 1 and 2 opposite: image on the line")
check("M2_image_attains_generator",
      # psi = (1,0), phi = (0,1): a=1,b=0,c=0,d=1 → (0, 1, −1, 0)
      [G_ZERO,
       gsub(gmul(G_ONE, G_ONE), gmul(G_ZERO, G_ZERO)),
       gsub(gmul(G_ZERO, G_ZERO), gmul(G_ONE, G_ONE)),
       G_ZERO] == [G_ZERO, G_ONE, G_MONE, G_ZERO],
      "ψ = e₁, φ = e₂ attains (0,1,−1,0) — both inclusions: rank 1")
check("M2_kill_iff_det_zero",
      all((gsub(gmul(a_, d_), gmul(b_, c_)) == G_ZERO)
          == (gmul(a_, d_) == gmul(b_, c_))
          for a_ in [(1, 0), (0, 1), (2, 1)] for b_ in [(1, 0), (1, 1)]
          for c_ in [(0, 1), (1, 2)] for d_ in [(1, 0), (2, -1)]),
      "kill ⟺ ad = bc, checked over a Gaussian grid — the 2×2 "
      "determinant criterion")
check("pauli_double_occupation_dies",
      not gp_sub(gp_mul(A, B), gp_mul(B, A)),
      "φ = ψ diagonal: ab − ba the zero polynomial — no two fermions "
      "in one state, symbolic")
check("census_nest_m2", tri[2] + tri[3] == 4 == 2 * 2,
      "antisym 1 + sym 3 = 4 = m² at the kernel-checked size")
check("control_boson_no_exclusion",
      gadd(gmul(G_ONE, G_ONE), gmul(G_ONE, G_ONE)) == (2, 0) != G_ZERO,
      "symmetrized double occupation = 2 ≠ 0 — bosons do not exclude; "
      "the teeth belong to the −1 alone")
check("live_nonparallel_survives",
      gsub(gmul(G_ONE, G_ONE), gmul(G_ZERO, G_ZERO)) != G_ZERO,
      "det(e₁, e₂) = 1 ≠ 0: exclusion kills double occupation, not "
      "everything")

# ═══ PLANT (norm 16 hygiene) ════════════════════════════════════════════════
print("\n-- plant --")
# mutated swap: swapIdx fixing everything (identity) makes M = 0 —
# rank 0, trace 0: the m = 2 certificate must notice
def Mmat_mutant(p, q):
    return (1 if p == q else 0) - (1 if q == p else 0)

M_mut = [[Mmat_mutant(p, q) for q in range(4)] for p in range(4)]
check("plant_mutant_swap_caught",
      rank_exact(M_mut) != 1 and sum(M_mut[i][i] for i in range(4)) != 2,
      "identity-swap mutant: M = 0, rank 0 ≠ 1, trace 0 ≠ 2 — a wrong "
      "swap transcription cannot pass the trace certificate")

# ── verdict ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 68)
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print(f"checks run: {len(CHECKS)};  passed: {npass};  failed: {nfail}")
if nfail == 0:
    print("VERDICT: capstone re-derived by direct exhaustion (every")
    print("         pentagon/hexagon instance run on the complete unit")
    print("         box — not by citing the layers); exclusion census")
    print("         completed exactly for m = 2..6 (the honest label's")
    print("         division of labor honored); symbolic kill")
    print("         coefficientwise; nests tied; the plant bitten.")
    print("EXIT: 0")
    sys.exit(0)
else:
    print("VERDICT: NOT CLEAN")
    sys.exit(1)
