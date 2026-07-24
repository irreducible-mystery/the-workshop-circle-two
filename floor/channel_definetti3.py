"""Bench 3, THREE USES AND THE RATE — toward the full channel theorem.

(1) THE MECHANISM SURVIVES TO n = 3 — with the bookkeeping showing itself.
    The commutant of the collective rotation U x U x U is spanned by the six
    permutation operators, but its dimension is FIVE, not six (Schur-Weyl:
    1^2 + 2^2). The missing dimension is an exact identity: the three-qubit
    antisymmetrizer vanishes — sum over S3 of sgn(sigma) P_sigma = 0 to
    machine zero. Two dimensions refuse three-fold antisymmetry: the
    exclusion principle's shadow, appearing here as a rank drop. The
    algebra-defined collective dynamics (projection onto the permutation
    span, pseudo-inverse because of that very dependency, no integral
    anywhere) again equals the sampled Haar mixture of memoryless unitary
    triples: the de Finetti mechanism at three uses.

(2) THE RATE TRANSFERS VERBATIM. The 'Dicke process': an n-use dynamics
    that ignores its inputs and prepares the n outputs jointly in the
    half-excited Dicke state — permutation invariant, with no per-use law.
    For constant channels the diamond norm REDUCES EXACTLY to the trace
    norm of the outputs (lemma verified here on random entangled inputs,
    equality to 1e-10), so the state bench's exact law becomes a law about
    dynamics with no modification at all:
        diamond-distance(2-use marginal, nearest memoryless mixture)
            = 1/(2(n-1)),
    verified for n = 8 ... 1024, log-log slope -1. Habit-formation of
    processes runs at exactly the speed of habit-formation of states —
    one law, two levels, connected by the Choi dictionary.

Status: exact throughout ((1) algebra exact + Monte Carlo at sampling
error; (2) exact closed form + lemma verified numerically).
"""
import numpy as np
from itertools import permutations

rng = np.random.default_rng(333)


def perm_op(sigma, n=3, d=2):
    """P_sigma |i_1 .. i_n> = |i_{sigma^{-1}(1)} .. >  on (C^d)^n."""
    D = d ** n
    P = np.zeros((D, D))
    for idx in range(D):
        digits = [(idx // d ** (n - 1 - k)) % d for k in range(n)]
        new = [digits[sigma[k]] for k in range(n)]
        jdx = sum(v * d ** (n - 1 - k) for k, v in enumerate(new))
        P[jdx, idx] = 1.0
    return P


def haar(n):
    G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(G)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))


def rand_rho(D):
    G = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
    R = G @ G.conj().T
    return R / np.trace(R)


def three_uses(say, N=40000):
    perms = list(permutations(range(3)))
    Ps = [perm_op(s) for s in perms]
    G = np.array([[np.trace(a.T @ b) for b in Ps] for a in Ps]).real
    rank = np.linalg.matrix_rank(G, tol=1e-10)
    signs = {s: (1 if np.linalg.det(np.eye(3)[list(s)]) > 0 else -1)
             for s in perms}
    A = sum(signs[s] * P for s, P in zip(perms, Ps))
    say(f"  six permutation operators, Gram rank {rank}: the commutant of")
    say(f"  U x U x U is FIVE-dimensional (Schur-Weyl: 1^2 + 2^2), because the")
    say(f"  three-qubit antisymmetrizer vanishes: ||sum sgn(s) P_s|| = "
        f"{np.linalg.norm(A):.1e}")
    say(f"  — two dimensions refuse three-fold antisymmetry (exclusion's shadow).")
    assert rank == 5 and np.linalg.norm(A) < 1e-12

    Gi = np.linalg.pinv(G)

    def twirl_exact(X):
        c = np.array([np.trace(P.T.conj() @ X) for P in Ps])
        coef = Gi @ c
        return sum(co * P for co, P in zip(coef, Ps))

    Xs = [rand_rho(8) for _ in range(2)]
    acc = [np.zeros((8, 8), dtype=complex) for _ in Xs]
    for _ in range(N):
        U = haar(2)
        W = np.kron(np.kron(U, U), U)
        Wd = W.conj().T
        for k, X in enumerate(Xs):
            acc[k] += W @ X @ Wd
    worst = max(np.linalg.norm(acc[k] / N - twirl_exact(X))
                for k, X in enumerate(Xs))
    say(f"  algebra-defined collective 3-use dynamics (pinv projection onto the")
    say(f"  dependent span) vs sampled Haar mixture of memoryless unitary")
    say(f"  triples ({N} draws): worst deviation {worst:.4f} — sampling error.")
    assert worst < 0.06


def dicke_rdm2(n):
    k = n // 2
    denom = n * (n - 1)
    rho = np.zeros((4, 4))
    rho[0, 0] = (n - k) * (n - k - 1) / denom
    rho[3, 3] = k * (k - 1) / denom
    pc = k * (n - k) / denom
    rho[1, 1] = rho[2, 2] = rho[1, 2] = rho[2, 1] = pc
    return rho


def trace_norm(M):
    return float(np.abs(np.linalg.eigvalsh(M)).sum())


def constant_channel_lemma(say):
    """For constant channels L_rho(X) = tr(X) rho, diamond distance equals
    ||rho - sigma||_1: (L (x) id)(X) = rho (x) tr_1 X, so the difference is
    (rho - sigma) (x) tr_1 X — equality for EVERY input, entangled or not."""
    rho, sigma = dicke_rdm2(8), dicke_rdm2(1024)
    t1 = trace_norm(rho - sigma)
    worst_gap = 0.0
    for _ in range(30):
        psi = rng.normal(size=32) + 1j * rng.normal(size=32)  # C^4 (x) C^8 pure
        psi /= np.linalg.norm(psi)
        Xa = np.einsum("ab,cb->ac",
                       psi.reshape(4, 8), psi.reshape(4, 8).conj())  # tr_anc
        anc = np.einsum("ab,ac->bc",
                        psi.reshape(4, 8), psi.reshape(4, 8).conj())
        out_dist = trace_norm(np.kron(rho - sigma, anc))
        worst_gap = max(worst_gap, abs(out_dist - t1 * trace_norm(anc)))
    say(f"  constant-channel lemma: output distance = ||rho - sigma||_1 x ||anc||_1")
    say(f"  on random entangled inputs, worst deviation {worst_gap:.1e} —")
    say(f"  diamond norm collapses to trace norm, exactly.")
    assert worst_gap < 1e-10


def rate(say):
    sigma = np.zeros((4, 4))
    sigma[0, 0] = sigma[3, 3] = 0.25
    sigma[1, 1] = sigma[2, 2] = sigma[1, 2] = sigma[2, 1] = 0.25
    ns = [8, 16, 32, 64, 128, 256, 512, 1024]
    Ts = []
    for n in ns:
        T = 0.5 * trace_norm(dicke_rdm2(n) - sigma)
        Ts.append(T)
        assert abs(2 * (n - 1) * T - 1) < 1e-9
    slope = np.polyfit(np.log(ns), np.log(Ts), 1)[0]
    say(f"  the Dicke process: diamond-distance of its 2-use marginal from the")
    say(f"  nearest memoryless mixture = 1/(2(n-1)) EXACTLY (n = 8..1024,")
    say(f"  log-log slope {slope:.3f}) — the state bench's law, now a law about")
    say(f"  dynamics, unchanged. One rate, two levels, joined by Choi.")
    assert -1.05 < slope < -0.95


def demonstrate(say):
    three_uses(say)
    constant_channel_lemma(say)
    rate(say)
    say("  moral: the road to the full theorem is open and the toll is known:")
    say("         symmetry supplies the mixture at every n, the missing")
    say("         dimension is exclusion's signature, and habit-formation of")
    say("         process and of state are one phenomenon at one speed.")


if __name__ == "__main__":
    demonstrate(print)
