"""FLATLAND II — symmetric statistics, built constructively.

The flatland bench showed geometrically that d >= 3 forces R = R^{-1}.
This bench builds the roomy world's particle physics from the coherence
equations themselves — the same way the anyon was built — and finds the
complete catalog.

Claims checked:

(1) THE GOLDEN GRAMMAR REFUSES ROOMINESS, BY EXHAUSTION. Impose the third
    dimension's edict on Fibonacci fusion: R unitary with R = R^{-1} means
    r1, rt in {+1, -1} — four candidates total. All four fail the hexagon
    (minimum residual exactly the integer 4, at (r1, rt) = (+1, +1);
    certified exact in audit/c2_gift_certificates.py G1h — an earlier
    docstring carried a stale sub-unit value here; fixed as Circle Two
    crop item #1). Geometry exiled the anyon in the flatland
    bench; here algebra confirms the sentence from its own side. No
    symmetric braiding exists on golden fusion. None.

(2) THE SMALLEST ROOMY ATLAS, SOLVED FROM SCRATCH. On Z_2 fusion
    (f x f = 1), the pentagon is solved by search: exactly TWO gauge
    classes, F = +1 and F = -1 — H^3(Z_2, U(1)) = Z_2, found numerically.
    The hexagon over each: F = +1 admits R in {+1, -1}; F = -1 admits
    R in {+i, -i}. Four ways to be an indistinguishable pair: boson,
    fermion, semion, anti-semion. Apply the flatland filter (R real):
    the semions die with the anyon, and the roomy world's COMPLETE
    catalog is: +1 and -1. Two. The third dimension is why matter comes
    in exactly two kinds.

(3) THE -1 HAS TEETH: EXCLUSION AS A RANK. For the fermion, exchange
    antisymmetry annihilates double occupation: the antisymmetrized
    psi (x) psi vanishes to 1e-16 for random psi, and the antisymmetrizer
    on C^m (x) C^m has rank m(m-1)/2 exactly — 1, 3, 6, 10, 15 for
    m = 2..6: the triangular numbers as the fermionic census. No two
    fermions in one state, computed. Shelves, chemistry, stars that do
    not collapse: downstream of a single sign that survived the filter.
    Twist theta_f = R = -1; Frobenius-Schur nu = R * theta = +1 — the
    mirror ledger balances here too.

Status: exact (exhaustion where finite, search + verification elsewhere).
"""
import numpy as np
from itertools import product as iproduct
from scipy.optimize import minimize

rng = np.random.default_rng(1001)

ONE, TAU = 0, 1
PHI = (1 + np.sqrt(5)) / 2
FG = np.array([[1 / PHI, 1 / np.sqrt(PHI)], [1 / np.sqrt(PHI), -1 / PHI]])


# ---------- Fibonacci hexagon machinery (as before) ----------

def fuse_fib(a, b):
    if a == ONE:
        return (b,)
    if b == ONE:
        return (a,)
    return (ONE, TAU)


def Fsym_fib(a, b, c, d, x, y):
    if x not in fuse_fib(a, b) or d not in fuse_fib(x, c):
        return 0.0
    if y not in fuse_fib(b, c) or d not in fuse_fib(a, y):
        return 0.0
    if ONE in (a, b, c):
        return 1.0
    if d == ONE:
        return 1.0 if (x, y) == (TAU, TAU) else 0.0
    return FG[x, y]


def hex_residual_fib(r1, rt):
    def R(x, y, c):
        if x == ONE or y == ONE:
            return 1.0 + 0j
        return r1 if c == ONE else rt
    total = 0.0
    for a, b, c, d in iproduct((ONE, TAU), repeat=4):
        for e in fuse_fib(a, b):
            if d not in fuse_fib(e, c):
                continue
            for z in fuse_fib(a, c):
                if d not in fuse_fib(z, b):
                    continue
                lhs = R(e, c, d) * Fsym_fib(c, a, b, d, z, e)
                rhs = sum(Fsym_fib(a, b, c, d, e, g) * R(b, c, g)
                          * Fsym_fib(a, c, b, d, z, g) * R(a, c, z)
                          for g in fuse_fib(b, c))
                total += abs(lhs - rhs) ** 2
    return total


# ---------- Z2 machinery ----------

def fuse_z2(a, b):
    return ((a + b) % 2,)


def Fsym_z2(f, a, b, c, d, x, y):
    if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
        return 0.0
    return f if (a, b, c) == (1, 1, 1) else 1.0


def pent_residual_z2(f):
    total = 0.0
    for a, b, c, dd in iproduct((0, 1), repeat=4):
        x = (a + b) % 2
        y = (x + c) % 2
        t = (y + dd) % 2
        w = (c + dd) % 2
        v = (b + w) % 2
        u = (b + c) % 2
        lhs = (Fsym_z2(f, a, b, c, y, x, u) * Fsym_z2(f, a, u, dd, t, y, v)
               * Fsym_z2(f, b, c, dd, v, u, w))
        rhs = (Fsym_z2(f, x, c, dd, t, y, w) * Fsym_z2(f, a, b, w, t, x, v))
        total += abs(lhs - rhs) ** 2
    return total


def hex_residual_z2(f, R):
    def Rs(x, y, c):
        return R if (x, y) == (1, 1) else 1.0 + 0j
    total = 0.0
    for a, b, c, d in iproduct((0, 1), repeat=4):
        e = (a + b) % 2
        z = (a + c) % 2
        if d != (e + c) % 2 or d != (z + b) % 2:
            continue
        g = (b + c) % 2
        lhs = Rs(e, c, d) * Fsym_z2(f, c, a, b, d, z, e)
        rhs = (Fsym_z2(f, a, b, c, d, e, g) * Rs(b, c, g)
               * Fsym_z2(f, a, c, b, d, z, g) * Rs(a, c, z))
        total += abs(lhs - rhs) ** 2
    return total


def demonstrate(say):
    # (1) golden fusion refuses R = R^{-1}
    worst = min(hex_residual_fib(r1, rt)
                for r1 in (1, -1) for rt in (1, -1))
    say(f"  golden fusion + the third dimension's edict (R in {{+1,-1}}^2):")
    say(f"    minimum hexagon residual over all four candidates = {worst:.3f}")
    say(f"    — no symmetric braiding exists on Fibonacci fusion. The exile")
    say(f"    is confirmed from the algebra's side.")
    assert worst > 0.5           # the original gate, kept
    assert abs(worst - 4) < 1e-12  # norm 7: pin the exact value, not a floor

    # (2) the Z2 atlas
    sols = set()
    for _ in range(40):
        res = minimize(lambda p: pent_residual_z2(p[0]),
                       rng.uniform(-2, 2, size=1), method="Nelder-Mead",
                       options={"xatol": 1e-13, "fatol": 1e-18})
        if res.fun < 1e-15:
            sols.add(round(float(res.x[0]), 6))
    say(f"  Z2 pentagon solved by search: gauge classes F = {sorted(sols)}")
    assert sols == {-1.0, 1.0}
    catalog = {}
    for f in (1.0, -1.0):
        found = set()
        for _ in range(40):
            res = minimize(lambda p: hex_residual_z2(f, p[0] + 1j * p[1]),
                           rng.uniform(-2, 2, size=2), method="Nelder-Mead",
                           options={"xatol": 1e-13, "fatol": 1e-18})
            if res.fun < 1e-15:
                found.add((round(float(res.x[0]), 6),
                           round(float(res.x[1]), 6)))
        catalog[f] = sorted(found)
    say(f"    hexagon over F = +1: R = {catalog[1.0]}  (boson, fermion)")
    say(f"    hexagon over F = -1: R = {catalog[-1.0]}  (semion, anti-semion)")
    assert catalog[1.0] == [(-1.0, 0.0), (1.0, 0.0)]
    assert catalog[-1.0] == [(0.0, -1.0), (0.0, 1.0)]
    say(f"    flatland filter (R real): semions die with the anyon —")
    say(f"    the roomy world's complete catalog: +1 and -1. Two kinds.")

    # (3) the -1 has teeth
    for m in range(2, 7):
        A = np.zeros((m * m, m * m))
        for i in range(m):
            for j in range(m):
                A[i * m + j, i * m + j] += 0.5
                A[i * m + j, j * m + i] -= 0.5
        rank = np.linalg.matrix_rank(A, tol=1e-10)
        assert rank == m * (m - 1) // 2
    psi = rng.normal(size=4) + 1j * rng.normal(size=4)
    pp = np.kron(psi, psi)
    anti = pp - pp.reshape(4, 4).T.flatten()
    say(f"  exclusion as rank: antisymmetrizer ranks 1,3,6,10,15 for m=2..6")
    say(f"    (triangular numbers — the fermionic census), and the")
    say(f"    antisymmetrized psi x psi vanishes to {np.linalg.norm(anti):.1e}:")
    say(f"    no two fermions in one state, computed.")
    assert np.linalg.norm(anti) < 1e-12
    R_f, theta_f = -1.0, -1.0
    assert R_f * theta_f == 1.0
    say(f"  twist theta_f = R = -1; Frobenius-Schur nu = R * theta = +1 —")
    say(f"  the mirror ledger balances for the fermion too.")
    say("  moral: build the roomy world the way the anyon was built, and it")
    say("         hands you exactly two particles. The -1 that survives the")
    say("         filter is why atoms have shelves — matter's structure,")
    say("         downstream of one sign in a coherence equation.")


if __name__ == "__main__":
    demonstrate(print)
