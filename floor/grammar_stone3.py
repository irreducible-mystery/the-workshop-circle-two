"""Bench 7, THIRD STONE — the associator, and Mac Lane's pentagon solved.

The rebuild's program: let even the JOINING be witnessed rather than strict.
When reassociating (a(bc))d vs ((ab)c)d is not an equality but a morphism —
the associator F — Mac Lane's pentagon is the coherence loop it must close.
This stone takes the simplest nontrivial fusion grammar, the Fibonacci rule
(tau x tau = 1 + tau), builds the pentagon from fusion trees, and checks:

(1) STRICTNESS IS IMPOSSIBLE. The identity associator (F = I) FAILS the
    pentagon: residual > 0.3. In this grammar the joining cannot be strict;
    witnesses are mandatory, not optional. (The skeleton refuses to
    strictify — weakness is a fact about the world of this rule, not a
    stylistic choice.)

(2) COHERENCE CONJURES THE GOLDEN RATIO. Solving the pentagon equations
    numerically from scratch (80 random starts, no solution assumed):
    every unitarity-compatible solution is gauge-equivalent to
        F = [[1/phi, 1/sqrt(phi)], [1/sqrt(phi), -1/phi]],  phi = (1+sqrt5)/2,
    verified to satisfy ALL pentagon instances to 1e-12, with F orthogonal
    (F F^T = I) — the witness preserves the record. Non-unitary solution
    families exist (the Yang-Lee shadow); demanding unitary witnesses
    selects the golden joining uniquely among the found solutions.

(3) THE JOINING HAS A SPECTRUM. The fusion matrix of tau is [[0,1],[1,1]];
    its Perron eigenvalue — the quantum dimension of tau — is phi itself
    (checked). And this witness-algebra is physics: adding the hexagon
    gives braiding phases e^{+-4pi i/5} — the Fibonacci anyon, universal
    for topological quantum computation. Coherence, asked politely for its
    solutions, answers with a particle.

A second pentagon, as promised: after KCBS's, Mac Lane's.

Status: exact where checked (pentagon residuals, orthogonality, Perron
root); the solver is numerical but its solutions are verified to 1e-12.
Fourth stone onward: the hexagon, interchange, the full coherent tower.
"""
import numpy as np
from itertools import product as iproduct

rng = np.random.default_rng(1618)

ONE, TAU = 0, 1
PHI = (1 + np.sqrt(5)) / 2


def fuse(a, b):
    if a == ONE:
        return (b,)
    if b == ONE:
        return (a,)
    return (ONE, TAU)


def Fsym(F, a, b, c, d, x, y):
    """F-move amplitude [ (ab)_x c -> a (bc)_y ] at total charge d.
    Zero if invalid; trivial (=1) if any of a,b,c is the vacuum."""
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
    """Sum of squared pentagon violations over all external charges and
    internal labelings. Both paths ((ab)c)d -> a(b(cd))."""
    total = 0.0
    for a, b, c, dd in iproduct((ONE, TAU), repeat=4):
        for x in fuse(a, b):
            for y in fuse(x, c):
                for t in fuse(y, dd):
                    for w in fuse(c, dd):
                        for v in fuse(b, w):
                            if t not in fuse(a, v):
                                continue
                            lhs = 0.0
                            for u in fuse(b, c):
                                lhs += (Fsym(F, a, b, c, y, x, u)
                                        * Fsym(F, a, u, dd, t, y, v)
                                        * Fsym(F, b, c, dd, v, u, w))
                            rhs = (Fsym(F, x, c, dd, t, y, w)
                                   * Fsym(F, a, b, w, t, x, v))
                            total += (lhs - rhs) ** 2
    return total


def demonstrate(say):
    # (1) strictness impossible
    strict = pentagon_residual(np.eye(2))
    say(f"  strict associator (F = identity): pentagon residual {strict:.4f} > 0")
    say(f"  — in the Fibonacci grammar the joining CANNOT be strict; the witness")
    say(f"  is mandatory. Weakness is a fact, not a style.")
    assert strict > 0.3

    # (2) solve the pentagon from scratch
    from scipy.optimize import minimize

    def obj(p):
        return pentagon_residual(np.array([[p[0], p[1]], [p[2], p[3]]]))

    found = []
    for _ in range(80):
        res = minimize(obj, rng.uniform(-1.8, 1.8, size=4), method="Nelder-Mead",
                       options={"xatol": 1e-13, "fatol": 1e-18, "maxiter": 6000})
        if res.fun < 1e-13:
            found.append(res.x)
    assert found, "no pentagon solutions found"
    golden = np.array([[1 / PHI, 1 / np.sqrt(PHI)],
                       [1 / np.sqrt(PHI), -1 / PHI]])
    assert pentagon_residual(golden) < 1e-24
    # gauge freedom rescales the off-diagonals reciprocally (b,c) -> (lb, c/l):
    # the gauge INVARIANTS of a solution are (a, d, p = b*c).
    classes = {}
    for p in found:
        a, b, c, d = p
        classes.setdefault((round(a, 6), round(d, 6), round(b * c, 6)),
                           []).append(p)
    say(f"  pentagon solved from scratch: {len(found)} converged runs fall into")
    say(f"  {len(classes)} gauge classes (invariants a, d, b*c):")
    golden_classes, stray_classes = [], []
    for (a, d, prod), members in sorted(classes.items()):
        unitarizable = (abs(a + d) < 1e-5 and prod > 0
                        and abs(a * a + prod - 1) < 1e-5)
        tag = "unitarizable" if unitarizable else "non-unitary (Yang-Lee shadow)"
        say(f"    a={a:+.6f}  d={d:+.6f}  b*c={prod:+.6f}   [{tag}]  "
            f"x{len(members)}")
        (golden_classes if unitarizable else stray_classes).append((a, d, prod))
    assert golden_classes, "no unitarizable pentagon solution found"
    for (a, d, prod) in golden_classes:
        assert abs(a - 1 / PHI) < 1e-5 and abs(prod - 1 / PHI) < 1e-5
        Ffix = np.array([[a, np.sqrt(prod)], [np.sqrt(prod), d]])
        assert pentagon_residual(Ffix) < 1e-10
        assert np.linalg.norm(Ffix @ Ffix.T - np.eye(2)) < 1e-5
    say(f"  every unitarizable class IS the golden associator:")
    say(f"    F = [[1/phi, 1/sqrt(phi)], [1/sqrt(phi), -1/phi]],  "
        f"phi = {PHI:.6f}")
    say(f"  (golden pentagon residual {pentagon_residual(golden):.1e}; "
        f"F F^T = I — the witness")
    say(f"   preserves the record. The non-unitary strays are the Yang-Lee")
    say(f"   shadow; demanding unitary witnesses selects the golden joining.)")

    # (3) the joining has a spectrum
    N_tau = np.array([[0.0, 1.0], [1.0, 1.0]])
    dq = float(np.linalg.eigvalsh(N_tau).max())
    say(f"  quantum dimension of tau = Perron root of [[0,1],[1,1]] = "
        f"{dq:.6f} = phi")
    assert abs(dq - PHI) < 1e-12
    say("  moral: ask only that the joining be coherently witnessed, and the")
    say("         equations answer with the golden ratio — and, with the hexagon")
    say("         added, with a particle (the Fibonacci anyon, universal for")
    say("         topological computation). The associator is not bookkeeping;")
    say("         coherence has a spectrum. Third stone laid; bench open.")


if __name__ == "__main__":
    demonstrate(print)
