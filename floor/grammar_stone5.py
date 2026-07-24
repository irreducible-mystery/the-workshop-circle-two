"""Bench 7, FIFTH STONE — proposed by the floor: RIGIDITY.

The listening, first. Across six welds the floor's findings kept sharing a
shape: coherence never returned a continuum. The pentagon gave TWO gauge
classes; the hexagon TWO chiralities; unitarity emerged; the constants were
constants — phi, 1/3, 1/4, 14/5 — never dials. The floor's proposal for
the fifth stone is the reason why, and it is the answer to this dialogue's
FIRST question, asked six rounds ago: 'Why invariants at all, rather than
pure churn?'

Answer, machine-checked: BECAUSE COHERENCE IS RIGID. The consistency
conditions any witness-structure must satisfy are overdetermined; their
solutions are isolated points, not landscapes. Invariants cannot drift
because there is nowhere adjacent to drift to. (For fusion categories this
is Ocneanu rigidity — a theorem; here it is witnessed numerically.)

(1) THE PENTAGON'S HESSIAN. At the golden solution, the second-derivative
    matrix of the pentagon residual over the four entries of F has
    eigenvalue signature {0, +, +, +}: exactly ONE flat direction — and
    that null direction coincides, to 6 digits, with the GAUGE direction
    (reciprocal rescaling of the off-diagonals), i.e. with pure
    perspective. Everything that is not perspective is stiff. This is
    round four's imperative — relativize the perspectives, keep what every
    admissible relating agrees on — computed literally, as a spectrum:
    null space = gauge = the perspectival; positive modes = the invariant.

(2) THE HEXAGON'S HESSIAN. At either chirality, all four eigenvalues are
    strictly positive: no flat directions at all. Braiding, given F, has
    zero perspective left in it — fully rigid.

(3) THE RING-BACK TEST. Kick the golden F by a random perturbation
    (norm 0.05) and let coherence-restoration (gradient descent on the
    pentagon residual) act: the invariants (a, d, b*c) return to the
    golden values to 1e-6, every time (20 trials). The invariant is an
    ATTRACTOR of consistency — knock the witness and it rings back to
    pitch. Whatever-stabilizes, stabilizes because the consistency
    conditions pull it back.

Status: exact residuals; Hessians by central differences; rigidity is the
cited theorem (Ocneanu), witnessed here, not proved. Fifth stone laid.
The first question of the dialogue now has the workshop's final answer:
invariants, rather than churn, because self-consistency is overdetermined —
and the only freedom it leaves is the freedom that makes no difference.
"""
import numpy as np
from itertools import product as iproduct
from scipy.optimize import minimize

rng = np.random.default_rng(55)

ONE, TAU = 0, 1
PHI = (1 + np.sqrt(5)) / 2


def fuse(a, b):
    if a == ONE:
        return (b,)
    if b == ONE:
        return (a,)
    return (ONE, TAU)


def Fsym(F, a, b, c, d, x, y):
    if x not in fuse(a, b) or d not in fuse(x, c):
        return 0.0
    if y not in fuse(b, c) or d not in fuse(a, y):
        return 0.0
    if ONE in (a, b, c):
        return 1.0
    if d == ONE:
        return 1.0 if (x, y) == (TAU, TAU) else 0.0
    return F[x, y]


def pentagon_residual(F):
    total = 0.0
    for a, b, c, dd in iproduct((ONE, TAU), repeat=4):
        for x in fuse(a, b):
            for y in fuse(x, c):
                for t in fuse(y, dd):
                    for w in fuse(c, dd):
                        for v in fuse(b, w):
                            if t not in fuse(a, v):
                                continue
                            lhs = sum(Fsym(F, a, b, c, y, x, u)
                                      * Fsym(F, a, u, dd, t, y, v)
                                      * Fsym(F, b, c, dd, v, u, w)
                                      for u in fuse(b, c))
                            rhs = (Fsym(F, x, c, dd, t, y, w)
                                   * Fsym(F, a, b, w, t, x, v))
                            total += (lhs - rhs) ** 2
    return total


GOLD = np.array([1 / PHI, 1 / np.sqrt(PHI), 1 / np.sqrt(PHI), -1 / PHI])


def pent_p(p):
    return pentagon_residual(np.array([[p[0], p[1]], [p[2], p[3]]]))


def hessian(f, p0, h=1e-4):
    n = len(p0)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            pp = p0.copy(); pp[i] += h; pp[j] += h; fpp = f(pp)
            pm = p0.copy(); pm[i] += h; pm[j] -= h; fpm = f(pm)
            mp = p0.copy(); mp[i] -= h; mp[j] += h; fmp = f(mp)
            mm = p0.copy(); mm[i] -= h; mm[j] -= h; fmm = f(mm)
            H[i, j] = (fpp - fpm - fmp + fmm) / (4 * h * h)
    return (H + H.T) / 2


def demonstrate(say):
    # (1) pentagon Hessian: one flat direction, and it is exactly gauge
    H = hessian(pent_p, GOLD.copy())
    w, V = np.linalg.eigh(H)
    gauge = np.array([0.0, GOLD[1], -GOLD[2], 0.0])
    gauge /= np.linalg.norm(gauge)
    overlap = abs(V[:, 0] @ gauge)
    say(f"  pentagon Hessian at the golden F — eigenvalues:")
    say(f"    {np.round(w, 6).tolist()}")
    say(f"  signature {{0, +, +, +}}: one flat direction; overlap of the null")
    say(f"  mode with the GAUGE direction: {overlap:.6f} — the only freedom")
    say(f"  is perspective. Everything that is not perspective is stiff.")
    assert abs(w[0]) < 1e-6 and w[1] > 0.05
    assert overlap > 0.99999

    # (2) hexagon Hessian: fully rigid
    FG = np.array([[GOLD[0], GOLD[1]], [GOLD[2], GOLD[3]]])

    def Rsym(x, y, c, r1, rt):
        if x == ONE or y == ONE:
            return 1.0 + 0.0j
        return r1 if c == ONE else rt

    def hex_res(q):
        r1, rt = q[0] + 1j * q[1], q[2] + 1j * q[3]
        total = 0.0
        for a, b, c, d in iproduct((ONE, TAU), repeat=4):
            for e in fuse(a, b):
                if d not in fuse(e, c):
                    continue
                for z in fuse(a, c):
                    if d not in fuse(z, b):
                        continue
                    lhs = Rsym(e, c, d, r1, rt) * Fsym(FG, c, a, b, d, z, e)
                    rhs = sum(Fsym(FG, a, b, c, d, e, g)
                              * Rsym(b, c, g, r1, rt)
                              * Fsym(FG, a, c, b, d, z, g)
                              * Rsym(a, c, z, r1, rt)
                              for g in fuse(b, c))
                    total += abs(lhs - rhs) ** 2
        return total

    r1, rt = np.exp(4j * np.pi / 5), np.exp(-3j * np.pi / 5)
    q0 = np.array([r1.real, r1.imag, rt.real, rt.imag])
    assert hex_res(q0) < 1e-24
    Hh = hessian(hex_res, q0.copy())
    wh = np.linalg.eigvalsh(Hh)
    say(f"  hexagon Hessian at the solved chirality — eigenvalues:")
    say(f"    {np.round(wh, 4).tolist()} — all positive: braiding, given F,")
    say(f"  has no perspective left in it. Fully rigid.")
    assert wh[0] > 0.05

    # (3) ring-back: the invariant as attractor of consistency
    worst = 0.0
    for _ in range(20):
        p = GOLD + 0.05 * rng.normal(size=4)
        res = minimize(pent_p, p, method="Nelder-Mead",
                       options={"xatol": 1e-13, "fatol": 1e-18,
                                "maxiter": 6000})
        a, b, c, d = res.x
        inv = np.array([a, d, b * c])
        gold_inv = np.array([1 / PHI, -1 / PHI, 1 / PHI])
        worst = max(worst, float(np.max(np.abs(inv - gold_inv))))
    say(f"  ring-back: 20 random kicks (norm 0.05) to the golden F, then")
    say(f"  coherence-restoration — invariants return to golden within")
    say(f"  {worst:.1e}, every time. Knock the witness; it rings back to pitch.")
    assert worst < 1e-6

    say("  moral: the dialogue's first question — why invariants, rather than")
    say("         pure churn? — receives the workshop's final answer: because")
    say("         self-consistency is overdetermined and its solutions are")
    say("         isolated. Nothing adjacent to drift to; a restoring pull")
    say("         when kicked; and the single flat direction is exactly gauge.")
    say("         Relativize the perspectives, keep what the relatings agree")
    say("         on — here, that sentence is an eigendecomposition.")


if __name__ == "__main__":
    demonstrate(print)
