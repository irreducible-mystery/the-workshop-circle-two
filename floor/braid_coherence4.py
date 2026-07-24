"""Bench 7, ABOVE INTERCHANGE — sixteen routes, one matrix.

The tetrahedron level, approached honestly: at four strands, the coherence
ABOVE Yang-Baxter and far-commutation becomes visible. This bench builds
the 4-strand Fibonacci representation from nothing but the golden F and
the hexagon's R-phases, and checks the whole ladder:

(1) THE REPRESENTATION EXISTS AND IS UNITARY. Fusion-path bases: the
    charge-tau sector is 3-dimensional, the charge-1 sector 2-dimensional
    (Fibonacci numbers counting the paths). B1, B2, B3 built by F-conjugation;
    all unitary to 1e-12.

(2) THE TWO-CELL RELATIONS. Far-commutation B1 B3 = B3 B1 (interchange in
    braid clothing) and BOTH Yang-Baxter relations, at machine zero.

(3) THE THREE-CELL COHERENCE: SIXTEEN ROUTES, ONE MATRIX. The longest
    permutation of four strands has exactly 16 reduced words; by
    Matsumoto-Tits, any two are connected by YB and far-commutation moves.
    All 16 positive-braid lifts are evaluated: one and the same matrix, in
    both sectors, to 1e-12. The 2-coherences close into 3-coherences with
    no new witness needed at the representation level — the tetrahedron's
    shadow. (The full weak version — surfaces braiding surfaces, the
    Zamolodchikov equation as the movie-move coherence — is the tower's
    genuine next floor; cited, not faked.)

(4) THE CENTER READS THE CHARGE. The full twist (B1 B2 B3)^4 generates the
    center of the braid group; on each sector it must act as a scalar if
    the sector is irreducible — and it does, to 1e-12, with DIFFERENT
    phases in the charge-1 and charge-tau sectors. The most global element
    of the braid group measures the most global quantum number: the loop
    around everything reads what everything amounts to.

Status: exact.
"""
import numpy as np
from itertools import permutations as _perms

ONE, TAU = 0, 1
PHI = (1 + np.sqrt(5)) / 2
FG = np.array([[1 / PHI, 1 / np.sqrt(PHI)], [1 / np.sqrt(PHI), -1 / PHI]])
R1, RT = np.exp(4j * np.pi / 5), np.exp(-3j * np.pi / 5)
RPH = {ONE: R1, TAU: RT}


def fuse(a, b):
    if a == ONE:
        return (b,)
    if b == ONE:
        return (a,)
    return (ONE, TAU)


def sector_states(t):
    out = []
    for x1 in fuse(TAU, TAU):
        for x2 in fuse(x1, TAU):
            if t in fuse(x2, TAU):
                out.append((x1, x2))
    return out


def Fblock(d):
    """F(tau,tau,tau; d) as a dict-of-dicts over internal labels."""
    if d == ONE:
        return {TAU: {TAU: 1.0}}
    return {x: {y: FG[x, y] for y in (ONE, TAU)} for x in (ONE, TAU)}


def build_generators(t):
    S = sector_states(t)
    n = len(S)
    idx = {s: i for i, s in enumerate(S)}
    B1 = np.zeros((n, n), dtype=complex)
    for s in S:
        B1[idx[s], idx[s]] = RPH[s[0]]
    # B2: F-move on the first triple, braid (2,3) in channel u, move back
    B2 = np.zeros((n, n), dtype=complex)
    for (x1, x2) in S:
        Fb = Fblock(x2)
        for x1p in (ONE, TAU):
            if (x1p, x2) not in idx:
                continue
            amp = 0.0 + 0.0j
            for u in fuse(TAU, TAU):
                if u in Fb.get(x1, {}) and u in Fb.get(x1p, {}):
                    amp += Fb[x1][u] * RPH[u] * Fb[x1p][u]
            B2[idx[(x1p, x2)], idx[(x1, x2)]] = amp
    # B3: F-move on (x1, tau, tau) at total t, braid (3,4) in channel w
    B3 = np.zeros((n, n), dtype=complex)
    for (x1, x2) in S:
        if x1 == TAU:
            Fb = Fblock(t)          # F(tau,tau,tau; t) with left charge tau
            for x2p in (ONE, TAU):
                if (x1, x2p) not in idx:
                    continue
                amp = 0.0 + 0.0j
                for w in fuse(TAU, TAU):
                    if w in Fb.get(x2, {}) and w in Fb.get(x2p, {}):
                        amp += Fb[x2][w] * RPH[w] * Fb[x2p][w]
                B3[idx[(x1, x2p)], idx[(x1, x2)]] = amp
        else:                        # x1 = 1: (34) channel w forced by t
            w = t
            B3[idx[(x1, x2)], idx[(x1, x2)]] = RPH[w]
    return S, [B1, B2, B3]


def reduced_words(perm):
    if perm == tuple(range(len(perm))):
        return [[]]
    out = []
    for i in range(len(perm) - 1):
        if perm[i] > perm[i + 1]:
            q = list(perm)
            q[i], q[i + 1] = q[i + 1], q[i]
            for rest in reduced_words(tuple(q)):
                out.append(rest + [i])
    return out


def demonstrate(say):
    results = {}
    for t, name in [(TAU, "charge-tau"), (ONE, "charge-1")]:
        S, B = build_generators(t)
        n = len(S)
        for M in B:
            assert np.linalg.norm(M @ M.conj().T - np.eye(n)) < 1e-12
        fc = np.linalg.norm(B[0] @ B[2] - B[2] @ B[0])
        yb1 = np.linalg.norm(B[0] @ B[1] @ B[0] - B[1] @ B[0] @ B[1])
        yb2 = np.linalg.norm(B[1] @ B[2] @ B[1] - B[2] @ B[1] @ B[2])
        assert fc < 1e-12 and yb1 < 1e-12 and yb2 < 1e-12
        words = reduced_words((3, 2, 1, 0))
        assert len(words) == 16
        mats = []
        for wrd in words:
            M = np.eye(n, dtype=complex)
            for i in wrd:
                M = M @ B[i]
            mats.append(M)
        spread = max(np.linalg.norm(m - mats[0]) for m in mats)
        FT = np.linalg.matrix_power(B[0] @ B[1] @ B[2], 4)
        comm = max(np.linalg.norm(FT @ M - M @ FT) for M in B)
        lam = np.trace(FT) / n
        scal = np.linalg.norm(FT - lam * np.eye(n))
        results[name] = (n, spread, comm, lam, scal)
        say(f"  {name} sector (dim {n}): generators unitary; far-commutation "
            f"{fc:.1e},")
        say(f"    Yang-Baxter {max(yb1, yb2):.1e}; sixteen reduced words of the")
        say(f"    longest braid -> one matrix (spread {spread:.1e});")
        say(f"    full twist: commutes with all B_i ({comm:.1e}), scalar "
            f"{lam:+.4f} (dev {scal:.1e})")
        assert spread < 1e-12 and comm < 1e-12 and scal < 1e-10
        assert abs(abs(lam) - 1) < 1e-10
    l1 = results["charge-1"][3]
    lt = results["charge-tau"][3]
    say(f"  the center reads the charge: full-twist phases differ by "
        f"{abs(np.angle(lt / l1)):.4f} rad")
    assert abs(l1 - lt) > 0.5
    say("  moral: dims 2 and 3 — Fibonacci numbers counting fusion paths;")
    say("         Tits' theorem witnessed: every route through the relations")
    say("         lands on one matrix, so the 2-coherences close with no new")
    say("         witness HERE — while the genuinely weak floor above")
    say("         (surfaces braiding surfaces, Zamolodchikov) stays open,")
    say("         named and unfaked. And the loop around everything reads")
    say("         what everything amounts to.")


if __name__ == "__main__":
    demonstrate(print)
