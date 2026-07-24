"""Bench 7 continued — THE HEXAGON: the anyon, braided.

The pentagon fixed the associator; the hexagon is the coherence loop that
fixes BRAIDING — how the witness of reassociation meshes with the witness
of exchange. Given the golden F (and nothing else), this bench:

(1) Solves the hexagon equations from scratch — unknown braiding phases
    R^{tt}_1 = r1, R^{tt}_t = rt entered as free COMPLEX numbers, modulus
    unconstrained. Finding: exactly TWO solution clusters — the two
    chiralities, complex-conjugate mirror twins — and |r| = 1 EMERGES
    rather than being imposed: coherence alone makes the braiding unitary.
    The phases are the famous ones: r1 = e^{+-4 pi i/5}, rt = e^{-+3 pi i/5},
    obeying r1 = rt^2. (Precision owed to the third body's correction C2:
    the equation ADMITS both hands — what is true, and now Lean-provable via
    the forcing quadratic's negative discriminant, is that no solution is
    its own mirror, so every solution COMMITS to a handedness. The equation
    offers both hands and insists you take one; it does not take one for you.)

(2) Builds the braid generators on the 2-dim fusion space V^{tttt...}:
    B1 = diag(r1, rt), B2 = F diag(r1, rt) F, and verifies the braid
    relation (Yang-Baxter) B1 B2 B1 = B2 B1 B2 to 1e-12, and that
    B1 B2 != B2 B1 — the representation is non-abelian: braiding DOES
    something that depends on order. Also the second hexagon (clockwise
    braiding, R -> R^{-1}): residual at machine zero.

(3) Computes the topological spin from the ribbon formula
    theta_t = (1/phi)(r1 + phi*rt): |theta_t| = 1 and theta_t = e^{-+4 pi i/5}
    — the Fibonacci anyon's twist. The witness-algebra is a particle's.

Status: exact; the solver is numerical but solutions verified to 1e-12.
"""
import numpy as np
from itertools import product as iproduct
from scipy.optimize import minimize

rng = np.random.default_rng(477)

ONE, TAU = 0, 1
PHI = (1 + np.sqrt(5)) / 2
FG = np.array([[1 / PHI, 1 / np.sqrt(PHI)],
               [1 / np.sqrt(PHI), -1 / PHI]])


def fuse(a, b):
    if a == ONE:
        return (b,)
    if b == ONE:
        return (a,)
    return (ONE, TAU)


def Fsym(a, b, c, d, x, y):
    if x not in fuse(a, b) or d not in fuse(x, c):
        return 0.0
    if y not in fuse(b, c) or d not in fuse(a, y):
        return 0.0
    if ONE in (a, b, c):
        return 1.0
    if d == ONE:
        return 1.0 if (x, y) == (TAU, TAU) else 0.0
    return FG[x, y]


def Rsym(x, y, c, r1, rt):
    """Braiding phase for the pair (x, y) fusing to c."""
    if x == ONE or y == ONE:
        return 1.0 + 0.0j
    return r1 if c == ONE else rt


def hexagon_residual(r1, rt, conj=False):
    """Both chirality-equations share this form; conj=True runs the second
    hexagon (clockwise braiding, R -> R^{-1} = conjugate for phases)."""
    if conj:
        r1, rt = np.conj(r1), np.conj(rt)
    total = 0.0
    for a, b, c, d in iproduct((ONE, TAU), repeat=4):
        for e in fuse(a, b):
            if d not in fuse(e, c):
                continue
            for z in fuse(a, c):
                if d not in fuse(z, b):
                    continue
                lhs = Rsym(e, c, d, r1, rt) * Fsym(c, a, b, d, z, e)  # inverse F-move
                rhs = 0.0 + 0.0j
                for g in fuse(b, c):
                    rhs += (Fsym(a, b, c, d, e, g)
                            * Rsym(b, c, g, r1, rt)
                            * Fsym(a, c, b, d, z, g)   # F^{-1} = F^T entry
                            * Rsym(a, c, z, r1, rt))
                total += abs(lhs - rhs) ** 2
    return total


def demonstrate(say):
    # (1) solve from scratch, modulus free
    def obj(p):
        return hexagon_residual(p[0] + 1j * p[1], p[2] + 1j * p[3])

    found = []
    for _ in range(60):
        res = minimize(obj, rng.uniform(-1.5, 1.5, size=4),
                       method="Nelder-Mead",
                       options={"xatol": 1e-13, "fatol": 1e-18,
                                "maxiter": 6000})
        if res.fun < 1e-15:
            found.append(res.x)
    assert found, "no hexagon solutions found"
    clusters = {}
    for p in found:
        r1, rt = p[0] + 1j * p[1], p[2] + 1j * p[3]
        clusters.setdefault((round(r1.real, 5), round(r1.imag, 5),
                             round(rt.real, 5), round(rt.imag, 5)),
                            []).append((r1, rt))
    say(f"  hexagon solved from scratch ({len(found)} converged runs):")
    sols = []
    for key, members in sorted(clusters.items()):
        r1, rt = members[0]
        sols.append((r1, rt))
        say(f"    r1 = {r1:+.6f}  rt = {rt:+.6f}   |r1| = {abs(r1):.6f}  "
            f"|rt| = {abs(rt):.6f}   x{len(members)}")
    assert len(clusters) == 2, "expected exactly two chiralities"
    target = np.exp(4j * np.pi / 5), np.exp(-3j * np.pi / 5)
    for r1, rt in sols:
        assert abs(abs(r1) - 1) < 1e-6 and abs(abs(rt) - 1) < 1e-6
        assert abs(r1 - rt ** 2) < 1e-6
        match = (abs(r1 - target[0]) < 1e-4 and abs(rt - target[1]) < 1e-4) or \
                (abs(r1 - np.conj(target[0])) < 1e-4
                 and abs(rt - np.conj(target[1])) < 1e-4)
        assert match
        assert hexagon_residual(r1, rt, conj=True) < 1e-12
    say("  exactly two chiralities — complex-conjugate mirror twins; |r| = 1")
    say("  EMERGED (never imposed): coherence alone unitarizes the braiding.")
    say("  r1 = e^(+-4 pi i/5), rt = e^(-+3 pi i/5), with r1 = rt^2; the")
    say("  second (clockwise) hexagon closes at machine zero as well.")

    # (2) braid generators and Yang-Baxter
    r1, rt = target
    B1 = np.diag([r1, rt])
    B2 = FG @ np.diag([r1, rt]) @ FG
    yb = np.linalg.norm(B1 @ B2 @ B1 - B2 @ B1 @ B2)
    comm = np.linalg.norm(B1 @ B2 - B2 @ B1)
    say(f"  braid relation B1 B2 B1 = B2 B1 B2: residual {yb:.1e}")
    say(f"  non-abelian: ||[B1, B2]|| = {comm:.3f} — order of exchange matters.")
    assert yb < 1e-12 and comm > 0.5

    # (3) topological spin
    theta = r1 / PHI + rt
    say(f"  twist theta_t = r1/phi + rt = {theta:+.6f}, |theta| = "
        f"{abs(theta):.6f} = e^(-4 pi i/5)")
    assert abs(theta - np.exp(-4j * np.pi / 5)) < 1e-10
    say("  moral: the pentagon chose the size of the witness (phi); the hexagon")
    say("         chooses its handedness and spin. Coherence, pressed twice,")
    say("         specifies a particle completely — the Fibonacci anyon, braided.")


if __name__ == "__main__":
    demonstrate(print)
