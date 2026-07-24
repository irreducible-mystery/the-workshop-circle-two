"""Bench 7, FLATLAND — the tower's next weakness, located in space itself.

The interchange bench ended on a promise: one level up, interchange is the
witness that can never be strictified. This bench finds out WHERE that
weakness has content — and the answer is geometric: exactly in two
dimensions. (Baez-Dolan stabilization: monoidal -> braided -> symmetric;
each extra dimension of room resumes the Eckmann-Hilton collapse one
notch. Braiding — weak interchange — is nontrivial precisely where there
is no room to walk around.)

Claims checked:

(1) IN 2D, THE TWO EXCHANGES ARE PROVABLY DISTINCT. Clockwise and
    counterclockwise exchange of two particles differ by a topological
    invariant: the relative winding. Computed here: +pi vs -pi; the
    composite loop (one exchange, then the other reversed) winds exactly
    2*pi. Rigidity, tested honestly: along 20 random smooth deformation
    FAMILIES verified collision-free at every intermediate stage, the
    winding stays 2*pi to 1e-9. And the toll is exhibited: push the
    deformation THROUGH a collision (the family watched passing within
    0.02 of coincidence) and the winding jumps by exactly 2*pi, to 0.
    The obstruction cannot be wiggled away — only collided away.
    Braiding is protected by the rule that worldlines do not touch.

(2) IN 3D, AN EXPLICIT HOMOTOPY KILLS THE DISTINCTION. The family
    v_s(t) = cos(pi t) e1 + sin(pi t)(cos(pi s) e2 + sin(pi s) e3)
    connects counterclockwise (s=0) to clockwise (s=1) exchange with
    |v_s(t)| = 1 EVERYWHERE — verified on a 200 x 200 grid: the two
    worldline exchanges are the same move once there is a third
    direction to swing through. No collision, no obstruction.

(3) THEREFORE: in d >= 3 any exchange representation obeys R = R^{-1},
    so R^2 = 1 and exchange eigenvalues are +-1 — bosons and fermions
    only. The golden braiding fails this loudly: |r1^2 - 1| = 1.176,
    ||B1^2 - I|| = 1.9 — the Fibonacci anyon cannot survive a third
    dimension. Anyons are exiles of flatland; the tower's mandatory
    weakness is a fact about ROOM.

Status: winding and homotopy exact-numerical; the representation-theoretic
consequence is the standard argument, its premises machine-checked.
"""
import numpy as np

rng = np.random.default_rng(21)

PHI = (1 + np.sqrt(5)) / 2
FG = np.array([[1 / PHI, 1 / np.sqrt(PHI)], [1 / np.sqrt(PHI), -1 / PHI]])
R1, RT = np.exp(4j * np.pi / 5), np.exp(-3j * np.pi / 5)


def winding(w):
    """Total accumulated angle of a discretized planar path (radians)."""
    return float(np.sum(np.angle(w[1:] / w[:-1])))


def demonstrate(say):
    # (1) 2D: the invariant, and its rigidity
    t = np.linspace(0, 1, 2001)
    ccw = np.exp(1j * np.pi * t)          # relative coordinate, ccw exchange
    cw = np.exp(-1j * np.pi * t)          # cw exchange
    w_ccw, w_cw = winding(ccw), winding(cw)
    composite = np.concatenate([ccw, cw[::-1]])
    W = winding(composite)
    say(f"  2D: relative winding — ccw {w_ccw / np.pi:+.4f} pi, "
        f"cw {w_cw / np.pi:+.4f} pi;")
    say(f"      composite loop winds {W / np.pi:.4f} pi (nonzero -> the two")
    say(f"      exchanges are NOT deformable into each other).")
    assert abs(w_ccw - np.pi) < 1e-6 and abs(w_cw + np.pi) < 1e-6
    assert abs(W - 2 * np.pi) < 1e-6
    lam = np.linspace(0, 1, 41)
    worst = 0.0
    trials = 0
    while trials < 20:
        c = 0.15 * (rng.normal(size=4) + 1j * rng.normal(size=4))
        bump = sum(ck * np.sin((k + 1) * np.pi * t) for k, ck in enumerate(c))
        clear = min(min(np.abs(ccw + l * bump).min(),
                        np.abs(cw + l * bump).min()) for l in lam)
        if clear < 0.05:
            continue                    # family not collision-free; resample
        trials += 1
        wp = np.concatenate([ccw + bump, (cw + bump)[::-1]])
        worst = max(worst, abs(winding(wp) - 2 * np.pi))
    say(f"      rigidity: 20 deformation families, each verified collision-")
    say(f"      free at every stage — winding drifts by at most {worst:.1e}.")
    assert worst < 1e-9
    # the toll: push the deformation THROUGH a collision
    bump_x = -1.5j * np.sin(np.pi * t)
    approach = min(np.abs(ccw + l * bump_x).min() for l in lam)
    wx = np.concatenate([ccw + bump_x, (cw + bump_x)[::-1]])
    Wx = winding(wx)
    say(f"      the toll: a deformation passing within {approach:.3f} of")
    say(f"      coincidence — winding jumps to {Wx / np.pi:.4f} pi. The")
    say(f"      obstruction yields only to collision; braiding is protected")
    say(f"      by the rule that worldlines do not touch.")
    assert approach < 0.02 and abs(Wx) < 1e-6

    # (2) 3D: the explicit homotopy
    s = np.linspace(0, 1, 200)
    tt = np.linspace(0, 1, 200)
    S, T = np.meshgrid(s, tt, indexing="ij")
    v1 = np.cos(np.pi * T)
    v2 = np.sin(np.pi * T) * np.cos(np.pi * S)
    v3 = np.sin(np.pi * T) * np.sin(np.pi * S)
    norms = np.sqrt(v1 ** 2 + v2 ** 2 + v3 ** 2)
    say(f"  3D: explicit homotopy ccw -> cw, swinging through the third")
    say(f"      direction: min |v_s(t)| over a 200x200 grid = "
        f"{norms.min():.6f} — collision-free everywhere. The two exchanges")
    say(f"      are one move, given room.")
    assert abs(norms.min() - 1.0) < 1e-12

    # (3) the golden braiding is exiled to flatland
    gap1 = abs(R1 ** 2 - 1)
    B1 = np.diag([R1, RT])
    gapB = np.linalg.norm(B1 @ B1 - np.eye(2))
    say(f"  consequence: in d >= 3, R = R^-1 forces R^2 = 1 (bosons/fermions")
    say(f"      only). Fibonacci: |r1^2 - 1| = {gap1:.3f}, ||B1^2 - I|| = "
        f"{gapB:.3f}")
    say(f"      — the golden braiding cannot survive a third dimension.")
    assert gap1 > 1.0 and gapB > 1.0
    say("  moral: Eckmann-Hilton resumes with every extra dimension of room")
    say("         (monoidal -> braided -> symmetric). Weak interchange has")
    say("         content exactly where there is no room to walk around:")
    say("         the anyon is an exile of flatland, and the tower's next")
    say("         weakness turns out to be a fact about space.")


if __name__ == "__main__":
    demonstrate(print)
