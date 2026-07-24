"""Bench 2 — THE SHEAF.

Claim checked: the world admits consistent partial views that provably cannot
be glued into one global view. The Mermin–Peres magic square: nine relatings,
six contexts; every context is internally consistent (commuting observables,
product = ±identity), every five contexts are jointly valuable — and all six
are not. Zero of the 512 candidate global valuations survive.

Status: exact theorem (state-INDEPENDENT contextuality), machine-verified
exhaustively. No state, no dynamics needed — the refusal is structural.
"""
import numpy as np
from itertools import product as iproduct

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

CELLS = {
    (0, 0): ("X.I", np.kron(X, I2)), (0, 1): ("I.X", np.kron(I2, X)), (0, 2): ("X.X", np.kron(X, X)),
    (1, 0): ("I.Y", np.kron(I2, Y)), (1, 1): ("Y.I", np.kron(Y, I2)), (1, 2): ("Y.Y", np.kron(Y, Y)),
    (2, 0): ("X.Y", np.kron(X, Y)), (2, 1): ("Y.X", np.kron(Y, X)), (2, 2): ("Z.Z", np.kron(Z, Z)),
}
ROWS = [[(r, c) for c in range(3)] for r in range(3)]
COLS = [[(r, c) for r in range(3)] for c in range(3)]
CONTEXTS = ([(f"row {r}", ROWS[r], +1) for r in range(3)] +
            [(f"col {c}", COLS[c], +1 if c < 2 else -1) for c in range(3)])


def demonstrate(say):
    I4 = np.eye(4)
    for (r, c), (name, M) in CELLS.items():
        assert np.linalg.norm(M - M.conj().T) < 1e-12      # honest observables
        assert np.linalg.norm(M @ M - I4) < 1e-12          # outcomes are ±1
    for cname, cells, sign in CONTEXTS:
        ms = [CELLS[k][1] for k in cells]
        for i in range(3):
            for j in range(i + 1, 3):
                assert np.linalg.norm(ms[i] @ ms[j] - ms[j] @ ms[i]) < 1e-12
        assert np.linalg.norm(ms[0] @ ms[1] @ ms[2] - sign * I4) < 1e-12
    say("  quantum side verified: 9 observables, 6 contexts, all commuting")
    say("  within context; products = +1,+1,+1 (rows) and +1,+1,-1 (columns).")

    keys = list(CELLS.keys())
    n_global, best = 0, 0
    for vals in iproduct([+1, -1], repeat=9):
        v = dict(zip(keys, vals))
        sat = sum(1 for _, cells, sign in CONTEXTS
                  if v[cells[0]] * v[cells[1]] * v[cells[2]] == sign)
        best = max(best, sat)
        if sat == 6:
            n_global += 1
    say(f"  global valuations satisfying all 6 contexts: {n_global} of 512")
    say(f"  maximum simultaneously satisfiable contexts: {best} of 6")
    assert n_global == 0 and best == 5
    say("  moral: local sections everywhere, global section nowhere —")
    say("         no view from the wings, checked exhaustively. The obstruction")
    say("         to gluing is not ignorance; it is the content.")


if __name__ == "__main__":
    demonstrate(print)
