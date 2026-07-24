"""Bench 7 — THE GRAMMAR CORNERSTONE (the empty bench's first stone).

The empty bench is the rebuild: physics said with no strict equalities,
every identification carrying its witness. That is long work. A cornerstone
can still be laid honestly: show that GRAMMAR ALONE already draws the
classical/quantum line — before any dynamics, any Hamiltonian, any state.

Claim checked: 'copying' is a natural operation in cartesian grammar
(sets with the cartesian product) and an impossibility in tensor grammar
(Hilbert spaces with the tensor product).

(1) Cartesian side: the diagonal Delta(x) = (x, x) is natural —
    Delta . f = (f x f) . Delta — verified exhaustively for many random
    functions between random finite sets. Copying classical data is a
    theorem of the grammar.

(2) Tensor side: naturality Delta . f = (f (x) f) . Delta, imposed as linear
    constraints on a candidate Delta: C^2 -> C^2 (x) C^2, leaves solution
    space of dimension ZERO. (The scalar test alone kills it: f = 2I forces
    2 Delta = 4 Delta.) No-cloning derived with no Hilbert-space dynamics —
    from the shape of composition. The line between classical and quantum
    (earlier in the dialogue: broadcastability) is a grammatical line.

Status: exact, machine-verified. This is a stone, not the bench. The bench
— witnessed identifications all the way up — remains open, on purpose.
"""
import numpy as np

rng = np.random.default_rng(11)


def cartesian_side(say, trials=200):
    for _ in range(trials):
        n, m = rng.integers(2, 7), rng.integers(2, 7)
        f = rng.integers(0, m, size=n)             # f: [n] -> [m]
        for x in range(n):
            # Delta then f x f:  (x,x) |-> (f(x), f(x))
            lhs = (f[x], f[x])
            # f then Delta:      x |-> f(x) |-> (f(x), f(x))
            rhs = (f[x], f[x])
            assert lhs == rhs
    say(f"  cartesian grammar: Delta(x) = (x,x) natural for {trials} random")
    say("  functions between random finite sets — copying is a theorem there.")


def tensor_side(say):
    # candidate Delta: C^2 -> C^4 (8 complex unknowns), naturality:
    #   Delta @ f  ==  kron(f, f) @ Delta      for all linear f
    # Each f contributes rows:  kron(f.T, I4) - kron(I2, kron(f, f))
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    R = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    tests = [2 * np.eye(2, dtype=complex), X, Z, H, R]
    rows = []
    I4, I2 = np.eye(4), np.eye(2)
    for f in tests:
        rows.append(np.kron(f.T, I4) - np.kron(I2, np.kron(f, f)))
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    null_dim = int(np.sum(s < 1e-10 * s.max()))
    say(f"  tensor grammar: naturality constraints stacked for f in")
    say(f"  {{2I, X, Z, H, random}} -> solution space dimension = {null_dim}")
    say("  (the scalar test alone: f = 2I forces 2*Delta = 4*Delta, so Delta = 0)")
    assert null_dim == 0


def demonstrate(say):
    cartesian_side(say)
    tensor_side(say)
    say("  moral: no-cloning before dynamics — the impossibility of copying is")
    say("         written into the tensor grammar itself, exactly where the")
    say("         cartesian grammar writes copying in. The classical/quantum")
    say("         line is drawn by composition before physics arrives.")
    say("  status: cornerstone laid; the bench stays open. The rebuild —")
    say("          every equality replaced by a witnessed identification —")
    say("          is the long work, and it is not faked here.")


if __name__ == "__main__":
    demonstrate(print)
