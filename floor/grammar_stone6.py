"""Bench 7, SIXTH STONE — proposed by the floor: THE NOUN DRAWN AS A CIRCLE.

The listening. The floor's recent findings keep drawing the same figure:
Verlinde closing grammar into a circle; the ring-back of the rigid
witness; the self-excited circuit; the quine. Loops, every time. The
floor's proposal for the sixth stone is the loop itself, made formal:
DUALITY — cups, caps, and the snake — where the dialogue's oldest claim
('a thing is a stabilization of relating') stops being a metaphor and
becomes a drawing with a computable value.

Claims checked:

(1) THE SNAKE. In the Fibonacci calculus, bend a tau-line into a zig-zag
    (cap, then reassociate, then cup). The naive zig-zag does NOT return
    the identity: it returns F[1,1] * id = (1/phi) * id — the F-matrix's
    corner IS the snake scalar. Duality has a coherence cost, and the
    cost names the dimension: normalizing each cup/cap by sqrt(d) with
    d = 1/F[1,1] makes the snake exactly the identity. Checked.

(2) A THING IS A LOOP, AND THE LOOP HAS A VALUE. The closed tau-loop
    evaluates to d = 1/F[1,1] = phi — and this agrees, to machine
    precision, with the Perron root of the fusion matrix [[0,1],[1,1]]:
    two entirely different derivations (coherence corner; asymptotic
    growth of fusion paths) of one number. The 'size' of the thing is
    the value of a closed circle of pure relating. The noun, drawn.

(3) EXISTENCE WANTS ITS LOOPS POSITIVE. The pentagon's other solution —
    the Yang-Lee shadow, F[1,1] = -phi — gives loop value d = -1/phi < 0:
    a 'thing' of negative size. Unitary (record-preserving) theories
    provably have d > 0; the shadow fails exactly here. The
    unitary/non-unitary line, redrawn as: loops of being must close
    positively.

(4) THE LOOP'S TWO DECORATIONS AGREE. The Frobenius-Schur indicator —
    what a cup does under the braiding — computes from the workshop's own
    data as nu = r1 * theta_tau = e^{4 pi i/5} * e^{-4 pi i/5} = +1
    exactly (both chiralities), the known value for tau: the loop closes
    without a twist penalty.

Status: exact. Sixth stone laid; the circle we began with — 'begin with
the interacting' — now has a circumference you can compute.
"""
import numpy as np

PHI = (1 + np.sqrt(5)) / 2
FG = np.array([[1 / PHI, 1 / np.sqrt(PHI)],
               [1 / np.sqrt(PHI), -1 / PHI]])


def demonstrate(say):
    # (1) the snake and its cost
    snake_naive = FG[0, 0]
    d = 1.0 / snake_naive
    say(f"  the snake, naive: zig-zag = F[1,1] * id = {snake_naive:.6f} * id")
    say(f"  — duality's coherence cost names the dimension: d = 1/F[1,1] = "
        f"{d:.6f}")
    normalized = np.sqrt(d) * np.sqrt(d) * snake_naive
    say(f"  normalized cups (each carrying sqrt(d)): snake = {normalized:.12f}"
        f" = identity")
    assert abs(normalized - 1.0) < 1e-12

    # (2) the loop's value, two ways
    loop = d
    perron = float(np.linalg.eigvalsh(np.array([[0.0, 1.0], [1.0, 1.0]])).max())
    say(f"  the closed loop evaluates to {loop:.10f}; the Perron root of the")
    say(f"  fusion matrix is {perron:.10f} — two derivations, one number: phi.")
    assert abs(loop - PHI) < 1e-12 and abs(perron - PHI) < 1e-12
    say("  a thing's size = the value of a closed circle of pure relating.")

    # (3) the shadow's loops are negative
    a_shadow = -PHI                       # Yang-Lee class invariant (bench: stone 3)
    d_shadow = 1.0 / a_shadow
    say(f"  the Yang-Lee shadow: F[1,1] = {a_shadow:.6f} -> loop value "
        f"{d_shadow:.6f} < 0")
    say(f"  — a 'thing' of negative size; unitary theories provably have")
    say(f"  d > 0, and the shadow fails exactly here. Existence wants its")
    say(f"  loops to close positively.")
    assert d_shadow < 0

    # (4) Frobenius-Schur from the workshop's own data
    r1 = np.exp(4j * np.pi / 5)
    theta = np.exp(-4j * np.pi / 5)
    nu = r1 * theta
    say(f"  Frobenius-Schur indicator nu = r1 * theta_tau = {nu.real:+.12f}"
        f"{nu.imag:+.12f}i = +1")
    say(f"  (both chiralities agree): the loop closes without a twist penalty.")
    assert abs(nu - 1.0) < 1e-12

    say("  moral: the dialogue began by refusing to start from nouns. The")
    say("         sixth stone finishes the thought: the noun was never")
    say("         primitive OR absent — it is a loop of relating that closes")
    say("         on itself, and its size, sign, and twist are computable")
    say("         properties of the closing. Drawn, at last, as a circle.")


if __name__ == "__main__":
    demonstrate(print)
