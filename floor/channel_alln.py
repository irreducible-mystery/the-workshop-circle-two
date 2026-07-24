"""Bench 3, TOWARD ALL n — the full theorem's three pillars, each checked.

(1) THE ALGEBRA'S TRUE SIZE IS CATALAN. The collective (exchangeable)
    dynamics at n uses is the commutant of U^{(x)n} — spanned by the n!
    permutation operators. But for qubits the span is far smaller: its
    dimension is the CATALAN number C_n (Schur-Weyl / Temperley-Lieb),
    verified here by exact Gram rank for n = 2..6:
        permutations 2, 6, 24, 120, 720  ->  dimensions 2, 5, 14, 42, 132.
    The gap is the world refusing representations that need more room than
    two dimensions allow (the vanishing antisymmetrizers, generalized) —
    the algebra of lawful collective process is exponentially smaller than
    the group of rearrangements.

(2) THE MECHANISM AT n = 4. The algebra-defined collective dynamics
    (pseudo-inverse projection onto the 24 dependent permutation operators,
    dimension 14, no integral anywhere) equals the sampled Haar mixture of
    memoryless unitary quadruples — symmetry manufactures the hidden
    memoryless law at four uses, as it did at two and three.

(3) THE WINDOW LAW — where the bench corrected the builder AGAIN. Watching
    a k-use window of the n-use Dicke process, the distance to the nearest
    memoryless mixture is pure combinatorics (hypergeometric vs binomial).
    The builder guessed n*T_k -> k(k-1)/4 (quadratic in the window). The
    numbers said otherwise: 1/2, 3/4, 3/4, 5/4 for k = 2,3,4,5 — with a
    parity quirk (k = 3 and k = 4 share a constant). Deriving to first
    order in 1/n gives the TRUE law, then verified here to 0.2%:
        n * T_k(n)  ->  c_k = (1/2) E_binom | k/2 - 2(j - k/2)^2 |,
    which grows LINEARLY in k for large windows (a chi-square first
    moment), not quadratically. T_2(n) = 1/(2(n-1)) exactly, as before.
    By the constant-channel lemma (bench 3.3), every statement is a
    diamond-norm law about dynamics, unchanged.

Status: (1),(3) exact; (2) exact algebra vs Monte Carlo at sampling error.
"""
import numpy as np
from itertools import permutations
from math import comb

rng = np.random.default_rng(555)


def perm_op(sigma, n, d=2):
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


def catalan_law(say):
    line = []
    for n in range(2, 7):
        Ps = np.stack([perm_op(s, n).flatten()
                       for s in permutations(range(n))])
        G = Ps @ Ps.T
        w = np.linalg.eigvalsh(G)
        rank = int(np.sum(w > 1e-9 * w.max()))
        cat = comb(2 * n, n) // (n + 1)
        line.append(f"n={n}: {len(Ps)} perms -> dim {rank} (C_{n}={cat})")
        assert rank == cat
    say("  the algebra's true size, by exact Gram rank:")
    for l in line:
        say(f"    {l}")
    say("  -> Catalan, not factorial: the lawful collective algebra is")
    say("     exponentially smaller than the group of rearrangements.")


def mechanism_n4(say, N=20000):
    perms = list(permutations(range(4)))
    Ps = [perm_op(s, 4) for s in perms]
    G = np.array([[np.trace(a.T @ b) for b in Ps] for a in Ps]).real
    Gi = np.linalg.pinv(G)

    def twirl_exact(X):
        c = np.array([np.trace(P.T.conj() @ X) for P in Ps])
        return sum(co * P for co, P in zip(Gi @ c, Ps))

    Gm = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
    X = Gm @ Gm.conj().T
    X = X / np.trace(X)
    acc = np.zeros((16, 16), dtype=complex)
    for _ in range(N):
        U = haar(2)
        W = np.kron(np.kron(U, U), np.kron(U, U))
        acc += W @ X @ W.conj().T
    dev = np.linalg.norm(acc / N - twirl_exact(X))
    say(f"  mechanism at n = 4: algebraic projection (24 dependent operators,")
    say(f"  dimension 14) vs sampled mixture of memoryless unitary quadruples")
    say(f"  ({N} draws): deviation {dev:.4f} — sampling error only.")
    assert dev < 0.06


def window_law(say):
    def T_k(n, k):
        K = n // 2
        tv = 0.0
        for j in range(k + 1):
            H = comb(K, j) * comb(n - K, k - j) / comb(n, k)
            B = comb(k, j) / 2 ** k
            tv += abs(H - B)
        return tv / 2

    for n in [16, 64, 256, 1024, 4096]:
        assert abs(2 * (n - 1) * T_k(n, 2) - 1) < 1e-12
    say("  window law (exact combinatorics, hypergeometric vs binomial):")
    say("    k = 2: T_2(n) = 1/(2(n-1)) exactly — the old law re-derived.")

    def c_theory(k):
        return sum(comb(k, j) / 2 ** k * abs(k / 2 - 2 * (j - k / 2) ** 2)
                   for j in range(k + 1)) / 2

    n = 65536
    line = []
    for k in [2, 3, 4, 5]:
        val = n * T_k(n, k)
        target = c_theory(k)
        line.append(f"k={k}: n*T_k = {val:.4f} (c_k = {target:.4f})")
        assert abs(val - target) < 0.002 * max(target, 1)
    say("    " + "   ".join(line))
    say("    (builder's guess k(k-1)/4 was WRONG — the true constants carry a")
    say(f"     parity quirk and grow linearly: c_10 = {c_theory(10):.3f}, "
        f"c_20 = {c_theory(20):.3f}, c_40 = {c_theory(40):.3f})")
    say("  -> T_k(n) ~ c_k/n with c_k = (1/2)E|k/2 - 2(j-k/2)^2|: linear in")
    say("     the window, inverse in the history; by the constant-channel")
    say("     lemma this is a diamond-norm law about the PROCESS, unchanged.")


def demonstrate(say):
    catalan_law(say)
    mechanism_n4(say)
    window_law(say)
    say("  moral: the road to all n, surveyed: the algebra is Catalan-sized,")
    say("         the symmetry->mixture mechanism holds at every n tested, and")
    say("         lawfulness has an exact price at every window. The theorem's")
    say("         three pillars, each standing in its lane.")


if __name__ == "__main__":
    demonstrate(print)
