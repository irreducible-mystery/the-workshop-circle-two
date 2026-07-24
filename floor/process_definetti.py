"""Bench 3, STRETCHED — PROCESS: de Finetti for the play itself.

The urn showed law-of-state as sediment. This bench shows law-of-DYNAMICS as
sediment: habits of process, not of state.

The mechanism: a two-state machine with one Polya urn per state (all counts
start at 1). Nothing in it is a transition law; it only reinforces what it
did before. Claims checked:

(1) MARKOV EXCHANGEABILITY, in exact rational arithmetic. Every path of
    length 8 (all 256, probabilities computed with fractions.Fraction, no
    floats) has a probability depending ONLY on its start and its transition
    counts — the exact hypothesis of the Diaconis–Freedman de Finetti theorem
    for Markov chains. By that theorem, this reinforced, law-less process IS
    a mixture of memoryless Markov chains: a hidden 'transition law' exists
    exactly as a representation artifact, just as theta did for the urn.

(2) Each history congeals its own CHANNEL: the empirical transition matrix
    settles (young world sloppy, old world frozen), the two congealed
    parameters are uniform on (0,1) and independent across the ensemble —
    the de Finetti measure over dynamics (= the uniform/Dirichlet(1,1) prior
    per row, recovered from behavior).

(3) The mirage, again: a hidden-channel world (sample a transition matrix,
    then run it memorylessly) is statistically indistinguishable from the
    reinforced world.

Status: (1) exact; (2)(3) statistically verified against exact theory.
Quantum reading, noted not faked: via Choi, exchangeable uses of a quantum
process = mixture of memoryless channels — the full channel-de Finetti is
the next stretch beyond this one.
"""
from fractions import Fraction
from itertools import product as iproduct
import numpy as np

rng = np.random.default_rng(2718)


def exact_markov_exchangeability(L=8, say=print):
    groups = {}
    total = Fraction(0)
    for path in iproduct((0, 1), repeat=L):
        urns = {0: [1, 1], 1: [1, 1]}
        counts = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
        p = Fraction(1)
        x = 0
        for nxt in path:
            c = urns[x]
            p *= Fraction(c[nxt], c[0] + c[1])
            c[nxt] += 1
            counts[(x, nxt)] += 1
            x = nxt
        total += p
        groups.setdefault(tuple(sorted(counts.items())), set()).add(p)
    assert total == 1
    assert all(len(v) == 1 for v in groups.values())
    say(f"  exact (no floats): all 2^{L} = {2**L} paths, probabilities in "
        f"rational arithmetic,")
    say(f"    fall into {len(groups)} transition-count classes; within every "
        f"class the")
    say(f"    probabilities are IDENTICAL — Markov exchangeability, verified "
        f"exactly.")
    say(f"    (Diaconis–Freedman then applies: the process = a mixture of "
        f"Markov chains.)")


def simulate_habits(say, M=3000, N=2000):
    th0_mid = np.empty(M); th0_end = np.empty(M)
    th1_end = np.empty(M)
    th0_20 = np.empty(M); th0_40 = np.empty(M)
    for m in range(M):
        urns = {0: [1, 1], 1: [1, 1]}
        x = 0
        u = rng.random(N)
        for t in range(N):
            c = urns[x]
            nxt = 1 if u[t] < c[1] / (c[0] + c[1]) else 0
            c[nxt] += 1
            x = nxt
            if t + 1 == 20:
                th0_20[m] = (urns[0][1] - 1) / max(1, urns[0][0] + urns[0][1] - 2)
            if t + 1 == 40:
                th0_40[m] = (urns[0][1] - 1) / max(1, urns[0][0] + urns[0][1] - 2)
            if t + 1 == N // 2:
                th0_mid[m] = (urns[0][1] - 1) / max(1, urns[0][0] + urns[0][1] - 2)
        th0_end[m] = (urns[0][1] - 1) / max(1, urns[0][0] + urns[0][1] - 2)
        th1_end[m] = (urns[1][1] - 1) / max(1, urns[1][0] + urns[1][1] - 2)
    early = float(np.median(np.abs(th0_40 - th0_20)))
    late = float(np.median(np.abs(th0_end - th0_mid)))
    say(f"  each history congeals its own channel: median swing of the 0->1")
    say(f"    transition habit — young world: {early:.3f}   old world: {late:.3f}")
    assert early > 4 * late
    for name, th in [("theta_0", th0_end), ("theta_1", th1_end)]:
        s = np.sort(th)
        ks = float(np.max(np.abs(s - (np.arange(1, M + 1) - 0.5) / M)))
        say(f"    congealed {name} vs Uniform(0,1): KS deviation {ks:.3f}")
        assert ks < 0.06
    r = float(np.corrcoef(th0_end, th1_end)[0, 1])
    say(f"    independence across rows: corr(theta_0, theta_1) = {r:+.3f}")
    assert abs(r) < 0.06
    say("    -> the de Finetti measure over DYNAMICS: uniform per row, "
        "independent rows.")


def mirage(say, M2=20000, steps=20):
    reinforced = np.empty(M2, dtype=int)
    for m in range(M2):
        urns = {0: [1, 1], 1: [1, 1]}
        x, n01 = 0, 0
        for _ in range(steps):
            c = urns[x]
            nxt = 1 if rng.random() < c[1] / (c[0] + c[1]) else 0
            c[nxt] += 1
            if x == 0 and nxt == 1:
                n01 += 1
            x = nxt
        reinforced[m] = n01
    hidden = np.empty(M2, dtype=int)
    for m in range(M2):
        p01, p10 = rng.random(), rng.random()
        x, n01 = 0, 0
        for _ in range(steps):
            if x == 0:
                nxt = 1 if rng.random() < p01 else 0
                if nxt == 1:
                    n01 += 1
            else:
                nxt = 0 if rng.random() < p10 else 1
            x = nxt
        hidden[m] = n01
    top = max(reinforced.max(), hidden.max()) + 1
    pr = np.bincount(reinforced, minlength=top) / M2
    ph = np.bincount(hidden, minlength=top) / M2
    tv = float(0.5 * np.abs(pr - ph).sum())
    say(f"  the mirage, for dynamics: reinforced world vs hidden-channel world,")
    say(f"    law of the 0->1 count in {steps} steps: TV distance {tv:.3f} "
        f"(theory: identical)")
    assert tv < 0.05


def demonstrate(say):
    exact_markov_exchangeability(say=say)
    simulate_habits(say)
    mirage(say)
    say("  moral: the script of the dynamics is sediment too. A process that")
    say("         only ever repeats itself IS, exactly, a mixture of memoryless")
    say("         laws — habit-of-process and hidden-law-of-process are one")
    say("         world twice described. The play's law is its own precedent.")


if __name__ == "__main__":
    demonstrate(print)
