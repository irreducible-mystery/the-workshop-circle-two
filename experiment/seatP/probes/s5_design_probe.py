#!/usr/bin/env python3
"""S5 design probe — the twist layer. Confirm the classification BEFORE
writing Lean. Sources: bench lines 37, 197-199 (theta_f = R = -1,
nu = R*theta = +1); certificate G1g (theta = R abelian, the two
nu-ledgers, the fork on semions), G5 (spin-statistics seed, fusion
matrix, D^2 = 2); CHARTER.md flag 3 (name the two ledgers apart)."""

def gmul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])

def gconj(z):
    return (z[0], -z[1])

ONE, MONE, I, MI = (1, 0), (-1, 0), (0, 1), (0, -1)
CATALOG = {"boson": (ONE, ONE), "fermion": (ONE, MONE),
           "semion": (MONE, I), "anti-semion": (MONE, MI)}  # name: (F, R)

# 1) twist = R (abelian): theta_a = R(a,a); per-particle values
theta = {n: r for n, (f, r) in CATALOG.items()}
print("theta:", theta)
assert theta["boson"] == ONE and theta["fermion"] == MONE
assert theta["semion"] == I and theta["anti-semion"] == MI

# 2) the two nu-ledgers
nuFS = {n: gmul(r, theta[n]) for n, (f, r) in CATALOG.items()}   # R*theta
nuML = {n: gmul(r, gconj(theta[n])) for n, (f, r) in CATALOG.items()}  # R*conj(theta)
print("nu_FS (R*theta):      ", nuFS)
print("nu_ML (R*conj(theta)):", nuML)
# survivors agree at +1; semions diverge: FS = -1, ML = +1
assert nuFS["boson"] == nuFS["fermion"] == ONE
assert nuML["boson"] == nuML["fermion"] == ONE
assert nuFS["semion"] == nuFS["anti-semion"] == MONE
assert nuML["semion"] == nuML["anti-semion"] == ONE
agree = [n for n in CATALOG if nuFS[n] == nuML[n]]
diverge = [n for n in CATALOG if nuFS[n] != nuML[n]]
print(f"fork nest: agree {len(agree)} {agree} + diverge {len(diverge)} {diverge} = 4")
assert len(agree) == 2 and len(diverge) == 2

# 3) fork locus = the real locus: R*theta = R*conj(theta) iff theta real
#    (for unit R; at R = 0 both sides vanish — the unit hypothesis is
#    load-bearing, a control)
for n, (f, r) in CATALOG.items():
    assert (nuFS[n] == nuML[n]) == (theta[n][1] == 0), n
print("fork locus == real locus: confirmed on all 4")
# control: r = 0 collapses the fork even for non-real theta
assert gmul((0, 0), I) == gmul((0, 0), gconj(I)) == (0, 0)
print("control: R = 0 collapses the fork (unit hypothesis load-bearing)")

# 4) ribbon on the Z2 fusion: twist as the diagonal of the R-symbol,
#    tw(a) = Rz2(r, a, a); fusion a x b = (a+b)%2;
#    ribbon: tw((a+b)%2) = tw(a) * tw(b) * R(a,b)^2
def Rz2(r, x, y):
    return r if (x == 1 and y == 1) else ONE

for name, (f, r) in CATALOG.items():
    for a in range(2):
        for b in range(2):
            lhs = Rz2(r, (a+b) % 2, (a+b) % 2)
            rab = Rz2(r, a, b)
            rhs = gmul(gmul(Rz2(r, a, a), Rz2(r, b, b)), gmul(rab, rab))
            assert lhs == rhs, (name, a, b, lhs, rhs)
print("ribbon identity holds on all 4 particles x 4 fusion cells")
# classification of the 4 cells: (0,0),(0,1),(1,0) read trivially;
# (1,1) forces tw(0) = tw(1)^2 R(1,1)^2 i.e. 1 = r^4 — nest 3 + 1 = 4
# symbolic check that the forcing cell is exactly r^4 = 1:
for name, (f, r) in CATALOG.items():
    r4 = gmul(gmul(r, r), gmul(r, r))
    assert r4 == ONE, name
print("forcing cell: r^4 = 1 for all four catalog units (from r^2 = f, f^2 = 1)")

# 5) spin-statistics seed + fusion matrix (G5)
Nf = [[0, 1], [1, 0]]
Nf2 = [[sum(Nf[i][k]*Nf[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert Nf2 == [[1, 0], [0, 1]]
assert all(x*x - 1 == (x-1)*(x+1) for x in range(-5, 6))  # char poly factorization
print("N_f^2 = I; char poly x^2-1 = (x-1)(x+1); d = 1, D^2 = 1+1 = 2")

# 6) negative control: a WRONG twist (theta = f instead of R) breaks the
#    semion's nu_ML ledger — theta_semion would be -1 (real), fork closes
wrong_theta = {n: f for n, (f, r) in CATALOG.items()}
wrong_nuML = {n: gmul(r, gconj(wrong_theta[n])) for n, (f, r) in CATALOG.items()}
assert wrong_nuML["semion"] == MI != ONE  # i * (-1) = -i: ledger visibly broken
print("control: theta = F (wrong) gives semion nu_ML = -i, not +1 — bites")

print("\nALL DESIGN FACTS CONFIRMED — classification for S5:")
print("  twist = R diagonal; fork nest 2+2 = 4; fork locus = real locus;")
print("  ribbon nest 3+1 = 4 per particle, forcing cell r^4 = 1;")
print("  spin-statistics seed nu = +1 on survivors; N_f^2 = I, D^2 = 2")
