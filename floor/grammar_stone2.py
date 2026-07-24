"""Bench 7, SECOND STONE — witnessed identity has curvature.

The rebuild's thesis: replace strict equality by identification-with-witness.
The first stone showed grammar drawing the classical/quantum line. This stone
shows why proof-relevance is PHYSICS, in the smallest possible case.

Two rays in Hilbert space that are 'the same state up to phase' are not
equal; they are identified, and the identification carries a witness (the
phase). Claims checked:

(1) Compose canonical witnesses (Pancharatnam: choose the phase making the
    overlap real positive) around a closed loop of states. Strict grammar
    says: equal, equal, equal — nothing happened. Witnessed grammar composes
    the witnesses and gets a NONTRIVIAL loop witness: arg of the Bargmann
    invariant <psi1|psi2><psi2|psi3><psi3|psi1>. For the Bloch octant
    (|0>, |+>, |+i>): loop witness = pi/4 exactly (checked to 1e-12).

(2) The loop witness is CURVATURE: for geodesic triangles on the Bloch
    sphere, |loop witness| = (solid angle)/2 — verified against l'Huilier's
    theorem for 30 random triangles to 1e-8, with the octant anchoring the
    orientation (witness = +sgn * Omega/2 for our traversal convention),
    and reversal of the loop conjugating the witness (checked).

(3) Path-dependence, i.e. the torsor: the witness identifying |0> with |+>
    directly differs from the witness composed via |+i> by exactly the loop
    witness. There is no canonical identity between distinct rays — only a
    U(1)-torsor of identifications, and the discrepancy around loops is the
    geometric phase.

This phase is not bookkeeping: Pancharatnam measured it in interferometers
in 1956; Berry derived it dynamically in 1984. The equals sign was hiding a
connection. Status: exact, machine-verified. Two stones now; bench open.
"""
import numpy as np

rng = np.random.default_rng(5)


def ket(n):
    """Bloch unit vector -> spinor."""
    th = np.arccos(np.clip(n[2], -1, 1))
    ph = np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def bargmann(k1, k2, k3):
    return np.vdot(k1, k2) * np.vdot(k2, k3) * np.vdot(k3, k1)


def solid_angle(n1, n2, n3):
    """l'Huilier's theorem from geodesic side lengths."""
    a = np.arccos(np.clip(n2 @ n3, -1, 1))
    b = np.arccos(np.clip(n1 @ n3, -1, 1))
    c = np.arccos(np.clip(n1 @ n2, -1, 1))
    s = (a + b + c) / 2
    t = np.tan(s / 2) * np.tan((s - a) / 2) * np.tan((s - b) / 2) \
        * np.tan((s - c) / 2)
    return 4 * np.arctan(np.sqrt(max(t, 0.0)))


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def demonstrate(say):
    # (1) the octant loop
    nz, nx, ny = np.eye(3)[2], np.eye(3)[0], np.eye(3)[1]
    k0, kx, ky = ket(nz), ket(nx), ket(ny)
    B = bargmann(k0, kx, ky)
    assert abs(B - (1 + 1j) / 4) < 1e-12
    assert abs(np.angle(B) - np.pi / 4) < 1e-12
    say("  octant loop |0> -> |+> -> |+i> -> |0>: strict grammar reports")
    say("  'same ray, same ray, same ray'; witnessed grammar composes the")
    say(f"  witnesses and gets e^(i pi/4): loop witness = {np.angle(B):.6f} "
        f"= pi/4 exactly.")

    # (2) curvature: |loop witness| = solid angle / 2, orientation anchored
    om = solid_angle(nz, nx, ny)
    assert abs(om - np.pi / 2) < 1e-12
    worst = 0.0
    for _ in range(30):
        ns = [v / np.linalg.norm(v) for v in rng.normal(size=(3, 3))]
        sgn = np.sign(np.linalg.det(np.array(ns)))
        pred = wrap(sgn * solid_angle(*ns) / 2)
        got = np.angle(bargmann(*[ket(n) for n in ns]))
        worst = max(worst, abs(wrap(got - pred)))
    say(f"  curvature: loop witness = +/- (solid angle)/2 — l'Huilier check on")
    say(f"  30 random Bloch triangles, worst deviation {worst:.2e}")
    assert worst < 1e-8
    Brev = bargmann(k0, ky, kx)
    assert abs(Brev - np.conj(B)) < 1e-12
    say("  reversing the loop conjugates the witness (checked): orientation is real.")

    # (3) the torsor: identifications are path-dependent
    w_direct = np.angle(np.vdot(kx, k0))
    w_via = np.angle(np.vdot(ky, k0)) + np.angle(np.vdot(kx, ky))
    gap = wrap(w_via - w_direct)
    assert abs(gap - np.angle(B)) < 1e-12
    say(f"  torsor: identifying |0> with |+> directly vs via |+i> — the two")
    say(f"  witnesses disagree by exactly the loop witness ({gap:.6f} = pi/4).")
    say("  moral: identity, made proof-relevant, secretes curvature. The")
    say("         geometric phase is what the equals sign was erasing —")
    say("         Pancharatnam measured it (1956) before Berry derived it (1984).")
    say("  status: second stone laid; the bench stays open — coherence all the")
    say("          way up (associators, interchange, the full rebuild) remains.")


if __name__ == "__main__":
    demonstrate(print)
