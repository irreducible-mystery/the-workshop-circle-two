"""Bench 2, DEEPENED — COHOMOLOGY.

Two claims, both checked:

(1) The obstruction to a global view is not a failure of search; it is a
    computable algebraic object. The Mermin-Peres square becomes a linear
    system over GF(2): contexts x cells, incidence matrix M, twist vector b
    (+1 contexts -> 0, the -1 context -> 1). A global valuation exists iff
    Mx = b is solvable. It is not — and the *class* of b in coker(M) is the
    obstruction: coker(M) is computed to be Z_2, the class of b is its
    nonzero element, and the witnessing cocycle y (yM = 0, y.b = 1) is
    exhibited: the cover's fundamental cycle evaluates the twist to 1.
    No coboundary can kill it. The obstruction is content, with an address.

(2) The performance exceeds every script, quantitatively. As a cooperation
    game (Alice fills a row, Bob a column, they must agree where they cross),
    every deterministic script — all 64 x 64 of them — tops out at 8/9.
    The performance (shared |Phi+> x |Phi+>, Alice measures her row triple,
    Bob his transposed column triple) scores exactly 1: computed exactly from
    the Born rule and confirmed over 10,000 sampled rounds.

Status: exact; exhaustive where finite, machine-verified throughout.
"""
import numpy as np
from itertools import product as iproduct

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

CELL_OPS = [[np.kron(X, I2), np.kron(I2, X), np.kron(X, X)],
            [np.kron(I2, Y), np.kron(Y, I2), np.kron(Y, Y)],
            [np.kron(X, Y), np.kron(Y, X), np.kron(Z, Z)]]
COL_SIGNS = [+1, +1, -1]

rng = np.random.default_rng(99)


# ---------- (1) the obstruction as algebra ----------

def gf2_rank(A):
    A = A.copy() % 2
    r = 0
    rows, cols = A.shape
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c]), None)
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] ^= A[r]
        r += 1
    return r


def obstruction(say):
    # M: 6 contexts (3 rows then 3 cols) x 9 cells; b: the twist
    M = np.zeros((6, 9), dtype=np.int64)
    for r in range(3):
        for c in range(3):
            cell = 3 * r + c
            M[r, cell] = 1          # row context r
            M[3 + c, cell] = 1      # col context c
    b = np.array([0, 0, 0, 0, 0, 1], dtype=np.int64)  # only col 2 is twisted
    rk = gf2_rank(M)
    rk_aug = gf2_rank(np.hstack([M, b[:, None]]))
    say(f"  linear system over GF(2): rank M = {rk}, rank [M|b] = {rk_aug} "
        f"-> {'solvable' if rk == rk_aug else 'UNSOLVABLE'}")
    assert rk == 5 and rk_aug == 6
    coker_dim = 6 - rk
    say(f"  obstruction group coker(M) ≅ Z_2^{coker_dim} = Z_2; "
        f"class of b = the nonzero element")
    y = np.ones(6, dtype=np.int64)
    assert not (y @ M % 2).any() and (y @ b) % 2 == 1
    say("  witnessing cocycle y = (1,1,1,1,1,1): y·M = 0 and y·b = 1 —")
    say("  the fundamental cycle of the cover evaluates the twist to 1;")
    say("  no coboundary reaches it. The obstruction has an address.")
    assert coker_dim == 1


# ---------- (2) the game the world wins ----------

def classical_value():
    # Alice: any row-filling with each row product +1 (4 per row -> 64)
    # Bob:   any col-filling with col products (+1, +1, -1)   (64)
    def fillings(sign):
        out = []
        for v in iproduct([1, -1], repeat=3):
            if v[0] * v[1] * v[2] == sign:
                out.append(v)
        return out
    row_opts = fillings(+1)
    col_opts = {c: fillings(COL_SIGNS[c]) for c in range(3)}
    best = 0
    for A in iproduct(row_opts, repeat=3):          # A[r][c]
        for B0 in col_opts[0]:
            for B1 in col_opts[1]:
                for B2 in col_opts[2]:
                    B = (B0, B1, B2)                # B[c][r]
                    wins = sum(1 for r in range(3) for c in range(3)
                               if A[r][c] == B[c][r])
                    best = max(best, wins)
    return best  # out of 9


def joint_projectors(ops, parity):
    """Rank-1 joint eigenprojectors of three commuting ±1 observables whose
    product is parity * I."""
    out = []
    I4 = np.eye(4)
    for s in iproduct([1, -1], repeat=3):
        if s[0] * s[1] * s[2] != parity:
            continue
        P = I4
        for sk, O in zip(s, ops):
            P = P @ (I4 + sk * O) / 2
        out.append((s, P))
    return out


def quantum_value(say, rounds=10000):
    # |Psi> = |Phi+>_{A1B1} x |Phi+>_{A2B2}, qubit order (A1 A2 B1 B2):
    psi = np.zeros((2, 2, 2, 2), dtype=complex)
    for i in range(2):
        for j in range(2):
            psi[i, j, i, j] = 0.5
    psi = psi.reshape(16)
    exact_ok = True
    total_fail = 0
    for r in range(3):
        arow = joint_projectors(CELL_OPS[r], +1)
        for c in range(3):
            bcol = joint_projectors([CELL_OPS[k][c].T for k in range(3)],
                                    COL_SIGNS[c])
            probs, agree = [], []
            for sA, PA in arow:
                for sB, PB in bcol:
                    p = float(np.real(np.vdot(psi, np.kron(PA, PB) @ psi)))
                    probs.append(p)
                    agree.append(sA[c] == sB[r])
            p_win = sum(p for p, a in zip(probs, agree) if a)
            exact_ok &= abs(p_win - 1.0) < 1e-10
            # sampled rounds for this (r, c)
            n_rc = rounds // 9
            pr = np.clip(np.array(probs), 0, None)
            pr = pr / pr.sum()
            draws = rng.choice(len(probs), size=n_rc, p=pr)
            total_fail += sum(1 for d in draws if not agree[d])
    say(f"  performance: exact Born success = 1.0 on all 9 questions: {exact_ok}")
    say(f"  sampled rounds: {9 * (rounds // 9)} played, {total_fail} failures")
    assert exact_ok and total_fail == 0


def demonstrate(say):
    obstruction(say)
    best = classical_value()
    say(f"  every deterministic script (64 x 64, exhausted): best = {best}/9")
    assert best == 8
    quantum_value(say)
    say("  moral: the missing global section is measured, not mourned — the")
    say("         class in coker(M) prices it, and the performance banks the")
    say("         difference: 8/9 is the ceiling for scripts; the play scores 1.")


if __name__ == "__main__":
    demonstrate(print)
