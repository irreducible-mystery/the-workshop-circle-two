"""Bench 4 — THE FIXED POINT.

Claims checked:
(1) Renormalization: 'things' are fixed points of a coarse-graining relation.
    1D Ising decimation (EXACT): K' = (1/2) ln cosh 2K — every finite coupling
    flows to nothing: the known absence of a 1D phase transition, re-derived by
    iteration. 2D Migdal–Kadanoff (APPROXIMATE, honestly labeled):
    K' = (1/2) ln cosh 4K — a nontrivial fixed point K*, one relevant
    direction, a watershed between two destinies, and the exponent nu read off
    the eigenvalue of the relating at its own fixed point.
(2) Lawvere's positive diagonal, executable: a quine — a sentence that is its
    own fixed point under 'being run' — verified by running it.

Status: (1) exact / approximate as labeled; (2) exact.
"""
import io
import numpy as np
from contextlib import redirect_stdout


def logcosh(x):
    x = abs(x)
    return x + np.log1p(np.exp(-2 * x)) - np.log(2.0)


def rg_1d(K):
    return 0.5 * logcosh(2 * K)


def rg_mk2d(K):
    return 0.5 * logcosh(4 * K)


QUINE = "s = 's = %r\\nprint(s %% s)'\nprint(s % s)"


def demonstrate(say):
    K, flow = 2.0, []
    for _ in range(14):
        flow.append(K)
        K = rg_1d(K)
    say("  1D exact decimation from K=2.0: "
        + " -> ".join(f"{k:.3g}" for k in flow[:7]) + f" -> ... -> {K:.1e}")
    assert K < 1e-5

    lo, hi = 0.05, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if rg_mk2d(mid) - mid < 0:
            lo = mid
        else:
            hi = mid
    Kstar = (lo + hi) / 2
    lam = 2 * np.tanh(4 * Kstar)
    nu = np.log(2) / np.log(lam)
    say(f"  2D Migdal-Kadanoff: nontrivial fixed point K* = {Kstar:.4f}")
    say(f"  (Onsager exact K_c = 0.4407 — the MK scheme is approximate, as labeled)")
    say(f"  relevant eigenvalue lambda = {lam:.4f} -> nu = ln b / ln lambda = {nu:.3f}"
        f"  (exact 2D: nu = 1)")
    assert abs(rg_mk2d(Kstar) - Kstar) < 1e-9
    assert 0.29 < Kstar < 0.32 and 1.28 < nu < 1.40

    up, dn = Kstar + 0.02, Kstar - 0.02
    for _ in range(60):
        up = rg_mk2d(up)
        if up > 25:
            break
    for _ in range(260):
        dn = rg_mk2d(dn)
    say(f"  watershed: K*+0.02 flows to strong coupling (order); "
        f"K*-0.02 flows to {dn:.1e} (nothing)")
    say("  — one relevant direction, two destinies, and the 'thing' here is the")
    say("  universality class: the occupant washed out, the role remaining.")
    assert up > 25 and dn < 1e-6

    buf = io.StringIO()
    with redirect_stdout(buf):
        exec(QUINE, {})
    assert buf.getvalue() == QUINE + "\n"
    say("  quine verified: a sentence equal to its own output when run —")
    say("  the diagonal argument caught behaving as a fixed point, not a paradox.")


if __name__ == "__main__":
    demonstrate(print)
