#!/usr/bin/env python3
"""S6 design probe — capstone (a) + exclusion layer (b).
Sources: S3/S4/S5 theorem inventory (pentagon_exactly_two,
pentagon_hexagon_iff_R_sq_F, R_over_boson/semion_class, flatland_filter,
conj_fixed_iff_real, nu_survivors); certificate G1f (antisymmetrizer
ranks 1,3,6,10,15 = m(m-1)/2; M = I-S with M^2 = 2M, tr M = m^2-m,
rank = tr/2; symmetrizer control m(m+1)/2; symbolic Pauli kill);
bench lines 30-36, 185-196."""
from fractions import Fraction

def gmul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])

def gconj(z):
    return (z[0], -z[1])

ONE, MONE, I, MI = (1, 0), (-1, 0), (0, 1), (0, -1)

# ── (a) CAPSTONE: pentagon(f) ∧ r²=f ∧ conj r = r ⟺ (f,r) ∈ {(1,1),(1,−1)} ──
# forward: pentagon ⟹ f ∈ {1,−1}; case f=1: r²=1 ⟹ r ∈ {1,−1}, both real ✓
#          case f=−1: r²=−1 ⟹ r ∈ {i,−i}, conj r = r fails both ⟹ empty
# backward: both survivors satisfy all three, trivially
survivors = []
for f in [ONE, MONE]:
    # roots of r² = f among all Gaussians with |re|,|im| <= 2 (units suffice
    # but sweep wider to confirm no strays in the box)
    for a in range(-3, 4):
        for b in range(-3, 4):
            r = (a, b)
            if gmul(r, r) == f and gconj(r) == r:
                survivors.append((f, r))
assert survivors == [((1, 0), (-1, 0)), ((1, 0), (1, 0))] or \
       sorted(survivors) == sorted([(ONE, ONE), (ONE, MONE)]), survivors
print(f"capstone survivors: {sorted(survivors)} — exactly the two, count = 2")
# nu rider: R·θ = R·R = f = +1 on both survivors
for f, r in survivors:
    assert gmul(r, r) == ONE
print("capstone nu rider: nuFS = r² = f = +1 on both survivors")

# ── (b) EXCLUSION: exact integer ranks via the trace certificate ────────────
# M = I − SWAP on Z^(m²); M² = 2M; tr M = m² − m; rank = tr/2 = m(m−1)/2
def build_M_S(m):
    n = m * m
    M = [[0]*n for _ in range(n)]
    S = [[0]*n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            M[i*m+j][i*m+j] += 1
            M[i*m+j][j*m+i] -= 1
            S[i*m+j][j*m+i] = 1
    return M, S

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

def rank_exact(M):
    A = [[Fraction(x) for x in row] for row in M]
    n, rank, col = len(A), 0, 0
    for col in range(n):
        piv = next((r for r in range(rank, n) if A[r][col] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(n):
            if r != rank and A[r][col] != 0:
                fct = A[r][col] / A[rank][col]
                A[r] = [a - fct*b for a, b in zip(A[r], A[rank])]
        rank += 1
    return rank

ranks, sranks = [], []
for m in range(2, 7):
    n = m*m
    M, S = build_M_S(m)
    P = [[M[i][j] + 2*S[i][j] for j in range(n)] for i in range(n)]  # I+S
    M2 = matmul(M, M)
    assert all(M2[i][j] == 2*M[i][j] for i in range(n) for j in range(n))
    assert sum(M[i][i] for i in range(n)) == m*m - m
    ranks.append(rank_exact(M))
    sranks.append(rank_exact(P))
assert ranks == [1, 3, 6, 10, 15]
assert sranks == [3, 6, 10, 15, 21]
print(f"antisym ranks m=2..6: {ranks} = m(m-1)/2 (triangular numbers)")
print(f"sym ranks (control):  {sranks} = m(m+1)/2; sums {[r+s for r,s in zip(ranks,sranks)]} = m²")

# triangular recurrence + closed form, the Lean-shaped facts:
T = lambda m: m*(m-1)//2
assert [T(m) for m in range(2, 7)] == ranks
assert all(T(m+1) == T(m) + m for m in range(1, 10))
assert all(2*T(m) == m*(m-1) for m in range(0, 10))
print("T(m) = m(m-1)/2: values, recurrence T(m+1)=T(m)+m, 2T = m(m-1) — all exact")

# symbolic Pauli kill over Zi: components of antisymmetrized psi⊗psi are
# psi_i psi_j − psi_j psi_i = 0 by mul_comm — Lean shape:
# ∀ x y : Zi, sub (mul x y) (mul y x) = zero. Plus the m=2 concrete block:
# M(2) on Z⁴ has rows [0,0,0,0],[0,1,-1,0],[0,-1,1,0],[0,0,0,0] — rank 1,
# image spanned by (0,1,-1,0)
M2x, _ = build_M_S(2)
print(f"M(2) rows: {M2x}")
assert M2x == [[0,0,0,0],[0,1,-1,0],[0,-1,1,0],[0,0,0,0]]
assert rank_exact(M2x) == 1
# action on (a,b)⊗(c,d) = (ac, ad, bc, bd): M v = (0, ad−bc, bc−ad, 0)
# — the determinant appears; kill iff ad = bc iff vectors parallel
print("M(2)(psi⊗phi) = (0, ad−bc, bc−ad, 0): the 2x2 determinant — kill ⟺ parallel")

# boson control: symmetrized psi⊗psi = 2·(products) ≠ 0 for psi = (1,1):
pp = [1*1, 1*1, 1*1, 1*1]
symm = [pp[0]+pp[0], pp[1]+pp[2], pp[2]+pp[1], pp[3]+pp[3]]
assert any(x != 0 for x in symm)
print("boson control: symmetrized (1,1)⊗(1,1) = (2,2,2,2) ≠ 0 — no exclusion for +1")

print("\nALL S6 DESIGN FACTS CONFIRMED")
