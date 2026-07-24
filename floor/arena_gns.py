"""Bench 1 — THE ARENA.

Claim checked: the state space is not given in advance; it precipitates from
the algebra of relatings plus one record of relating (the GNS construction).
Same algebra, different record -> different-sized theater. A mixed record
precipitates a doubled theater carrying a mirror cast (a nontrivial commutant
— the thermofield-double structure, in miniature).

Status: exact theorem, machine-verified in finite dimension.
"""
import numpy as np

rng = np.random.default_rng(7)


def matrix_basis(n):
    B = []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n), dtype=complex)
            E[i, j] = 1.0
            B.append(E)
    return B


def rand_element(n):
    return rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))


def gns(rho, tol=1e-10):
    """Precipitate (dim, pi, Omega, Gram spectrum) from the record
    omega(a) = Tr(rho a) on the algebra A = M_n. Relatings first;
    the theater is derived."""
    n = rho.shape[0]
    B = matrix_basis(n)
    d = len(B)
    G = np.array([[np.trace(rho @ Bk.conj().T @ Bl) for Bl in B] for Bk in B])
    G = (G + G.conj().T) / 2
    w, V = np.linalg.eigh(G)
    keep = w > tol * max(w.max(), 1.0)
    W = V[:, keep] / np.sqrt(w[keep])
    dim = W.shape[1]
    E = [sum(W[k, a] * B[k] for k in range(d)) for a in range(dim)]

    def ip(x, y):
        return np.trace(rho @ x.conj().T @ y)

    def pi(a):
        return np.array([[ip(E[b], a @ E[c]) for c in range(dim)]
                         for b in range(dim)])

    Omega = np.array([ip(E[b], np.eye(n)) for b in range(dim)])
    return dim, pi, Omega, np.sort(w[keep])[::-1]


def commutant_dim(mats):
    """Dimension of {C : [C, M] = 0 for all M} — the mirror cast."""
    dim = mats[0].shape[0]
    I = np.eye(dim)
    M = np.vstack([np.kron(I, A) - np.kron(A.T, I) for A in mats])
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-8 * max(s.max(), 1.0)))


def demonstrate(say):
    n = 2
    B = matrix_basis(n)
    psi = np.array([1.0, 0.0], dtype=complex)
    rho_pure = np.outer(psi, psi.conj())
    rho_mixed = np.eye(2, dtype=complex) / 2
    results = {}
    for name, rho in [("pure record ", rho_pure), ("mixed record", rho_mixed)]:
        dim, pi, Omega, spec = gns(rho)
        # the precipitate really is a *-representation with cyclic record vector
        for _ in range(5):
            a, b = rand_element(n), rand_element(n)
            assert np.linalg.norm(pi(a @ b) - pi(a) @ pi(b)) < 1e-8
            assert np.linalg.norm(pi(a.conj().T) - pi(a).conj().T) < 1e-8
            assert abs(np.vdot(Omega, pi(a) @ Omega) - np.trace(rho @ a)) < 1e-8
        span = np.array([pi(Bk) @ Omega for Bk in B])
        assert np.linalg.matrix_rank(span, tol=1e-8) == dim
        cdim = commutant_dim([pi(Bk) for Bk in B])
        results[name] = (dim, cdim)
        say(f"  {name}: theater dim {dim}, mirror-cast (commutant) dim {cdim}, "
            f"Gram spectrum {np.round(spec, 3).tolist()}")
    assert results["pure record "] == (2, 1)
    assert results["mixed record"] == (4, 4)
    p = 0.05
    dim, _, _, spec = gns(np.diag([p, 1 - p]).astype(complex))
    say(f"  barely-mixed record (p={p}): theater dim {dim}, Gram spectrum "
        f"{np.round(spec, 3).tolist()} — the extra directions are sediment-thin")
    assert dim == 4
    say("  moral: same algebra of relatings, different record -> different theater;")
    say("         homomorphism, adjoints, cyclicity, and the record itself all")
    say("         reproduced inside the precipitated arena. The stage is sediment.")


if __name__ == "__main__":
    demonstrate(print)
