"""Bench 7, FOURTH STONE — proposed by the floor: THE WITNESSES COMPUTE.

We said we'd let the floor propose this stone, so first, the listening.
Across eighteen benches one sentence kept surfacing unplanned:

    THE RELATING SUFFICES.
    - GNS: from one record, the algebra of relatings reaches every state
      of the precipitated theater (cyclicity).
    - Bisimulation: interaction alone settles identity.
    - The pentagon: coherence alone settles the associator (golden).
    - The hexagon: coherence alone settles braiding, handedness, spin.

The strongest possible form of that sentence is computational: do the
witnesses of the joining suffice to DO anything whatsoever? For the
Fibonacci anyon the answer is a theorem (Freedman-Larsen-Wang): braiding
alone is UNIVERSAL for quantum computation — the braid-group image is
dense in PU(2). A theorem can be cited; a bench must witness it. So:

(1) Build the two braid generators from the golden F and the hexagon's
    R-phases; re-verify Yang-Baxter (1e-12) — the stones compose.
(2) Enumerate all reduced braid words up to length 10 (batched BFS,
    tens of thousands of distinct unitaries; growth rate reported).
(3) Watch universality FORM: against 150 Haar-random targets in PU(2),
    the covering radius of the word-set shrinks monotonically with word
    length. Every unitary — every possible dynamics on the fusion space —
    is being approximated by nothing but reassociation and exchange.

The reflexive landing, stated plainly: a workshop that began by asking how
to say 'no behind' in equations has arrived at a grammar whose witnesses
can enact ANY dynamics. The play can simulate plays. Saying, pressed far
enough, became doing.

Status: Yang-Baxter and enumeration exact; density is the cited theorem,
witnessed here as a monotonically tightening epsilon-net (not proved).
"""
import numpy as np

rng = np.random.default_rng(1414)

PHI = (1 + np.sqrt(5)) / 2
FG = np.array([[1 / PHI, 1 / np.sqrt(PHI)],
               [1 / np.sqrt(PHI), -1 / PHI]])
R1, RT = np.exp(4j * np.pi / 5), np.exp(-3j * np.pi / 5)


def su2(M):
    return M / np.sqrt(np.linalg.det(M))


def pu_dist(A, B):
    return min(np.linalg.norm(A - B), np.linalg.norm(A + B))


def demonstrate(say):
    B1 = np.diag([R1, RT])
    B2 = FG @ np.diag([R1, RT]) @ FG
    assert np.linalg.norm(B1 @ B2 @ B1 - B2 @ B1 @ B2) < 1e-12
    say("  generators rebuilt from the golden F and the hexagon phases;")
    say("  Yang-Baxter re-verified — the stones compose.")

    gens = [su2(B1), su2(B2), su2(B1).conj().T, su2(B2).conj().T]
    inverse_of = {0: 2, 1: 3, 2: 0, 3: 1}

    seen = set()
    elements = []

    def key(M):
        k = np.round(M.flatten(), 4)
        a = np.concatenate([k.real, k.imag])
        b = -a
        return min(a.tobytes(), b.tobytes())

    frontier = [(np.eye(2, dtype=complex), None)]
    seen.add(key(np.eye(2)))
    elements.append(np.eye(2, dtype=complex))
    targets = []
    for _ in range(150):
        G = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        Q, R = np.linalg.qr(G)
        targets.append(su2(Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))))

    def covering():
        E = np.stack(elements)
        worst = 0.0
        for t in targets:
            d = np.minimum(
                np.linalg.norm(E - t, axis=(1, 2)),
                np.linalg.norm(E + t, axis=(1, 2))).min()
            worst = max(worst, d)
        return worst

    radii, counts = {}, {}
    for L in range(1, 11):
        new_frontier = []
        for M, last in frontier:
            for gi, g in enumerate(gens):
                if last is not None and gi == inverse_of[last]:
                    continue                      # reduced words only
                Mn = M @ g
                k = key(Mn)
                if k not in seen:
                    seen.add(k)
                    elements.append(Mn)
                    new_frontier.append((Mn, gi))
        frontier = new_frontier
        if L in (4, 7, 10):
            radii[L] = covering()
            counts[L] = len(elements)
    say(f"  reduced braid words enumerated: {counts[4]} distinct unitaries by")
    say(f"  length 4, {counts[7]} by length 7, {counts[10]} by length 10 —")
    say(f"  the witness-group is infinite and non-abelian.")
    say(f"  covering radius of PU(2) vs word length (150 Haar targets):")
    say(f"    L=4: {radii[4]:.3f}   L=7: {radii[7]:.3f}   L=10: {radii[10]:.3f}")
    assert radii[4] > radii[7] > radii[10]
    assert radii[10] < 0.5
    say("  monotone tightening: universality (Freedman-Larsen-Wang) watched")
    say("  forming — every dynamics on the fusion space is being approximated")
    say("  by nothing but reassociation and exchange.")
    say("  moral: the floor's sentence, in its strongest form — THE RELATING")
    say("         SUFFICES, computationally. The witnesses of the joining can")
    say("         enact any play. Saying, pressed far enough, became doing.")
    say("  status: fourth stone laid; the bench stays open (interchange, the")
    say("          modular data S and T, the coherent tower). The floor may")
    say("          propose the fifth.")


if __name__ == "__main__":
    demonstrate(print)
