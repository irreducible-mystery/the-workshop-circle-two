"""Bench 2, STRETCHED — THE DIAL: the contextual fraction.

The first sheaf bench found the refusal (0 of 512 global valuations). The
cohomology bench gave it an address (the class in coker(M) = Z_2). This bench
gives it a PRICE: the contextual fraction (Abramsky-Barbosa-Mansfield) — the
minimum weight of a model that cannot be simulated by any mixture of global
scripts, computed by linear programming over all deterministic assignments.

Claims checked:
(1) The magic square's empirical model has CF = 1 exactly: maximally
    contextual — no fraction of it is scripted. (LP over 512 assignments.)
(2) Under noise, the resource is a dial with an exact law: mixing with the
    uniform model, CF(eps) = 1 - 3*eps, hitting zero at eps = 1/3. The
    square's contextuality is worth exactly three times its noise.
(3) Gradation is real: the KCBS pentagon (5 qutrit projectors, adjacent ones
    orthogonal — built and verified) is contextual but NOT maximally:
    CF = 2*sqrt(5) - 4 ~ 0.472, matching its Bell-type violation
    (sum p_i = sqrt(5) vs classical 2 vs algebraic 5/2) — the LP value and
    the closed form agree to 1e-6.

Status: exact (LP is exact-in-principle; agreement with closed forms checked).
The obstruction has become a dial: address -> price -> gauge.
"""
import numpy as np
from itertools import product as iproduct
from scipy.optimize import linprog


def ncf_lp(n_vars, context_rows, caps):
    res = linprog(c=[-1.0] * n_vars, A_ub=np.array(context_rows),
                  b_ub=np.array(caps), bounds=[(0, None)] * n_vars,
                  method="highs")
    assert res.status == 0
    return -res.fun


# ---------- the square ----------

def square_cf(eps):
    """CF of (1-eps)*quantum + eps*uniform for the magic square scenario."""
    cells = [(r, c) for r in range(3) for c in range(3)]
    idx = {cell: i for i, cell in enumerate(cells)}
    contexts = [[(r, c) for c in range(3)] for r in range(3)] + \
               [[(r, c) for r in range(3)] for c in range(3)]
    signs = [+1, +1, +1, +1, +1, -1]
    assignments = list(iproduct([+1, -1], repeat=9))
    rows, caps = [], []
    for C, sign in zip(contexts, signs):
        for o in iproduct([+1, -1], repeat=3):
            parity_ok = (o[0] * o[1] * o[2] == sign)
            e = (1 - eps) * (0.25 if parity_ok else 0.0) + eps / 8
            rows.append([1.0 if all(g[idx[cell]] == o[k]
                                    for k, cell in enumerate(C)) else 0.0
                         for g in assignments])
            caps.append(e)
    return max(0.0, 1.0 - ncf_lp(len(assignments), rows, caps))


# ---------- the pentagon (KCBS) ----------

def kcbs_model(say):
    th = np.arccos(np.sqrt(np.cos(np.pi / 5) / (1 + np.cos(np.pi / 5))))
    vs = []
    for i in range(5):
        phi = 4 * np.pi * i / 5
        vs.append(np.array([np.cos(th), np.sin(th) * np.cos(phi),
                            np.sin(th) * np.sin(phi)]))
    psi = np.array([1.0, 0.0, 0.0])
    for i in range(5):
        assert abs(vs[i] @ vs[(i + 1) % 5]) < 1e-9      # adjacent orthogonal
    ps = [float((psi @ v) ** 2) for v in vs]
    say(f"  pentagon built: adjacent projectors orthogonal (checked); "
        f"p_i = {ps[0]:.4f} each,")
    say(f"    sum p_i = {sum(ps):.4f} = sqrt(5) "
        f"(classical ceiling 2, algebraic 5/2)")
    assert abs(sum(ps) - np.sqrt(5)) < 1e-9
    return ps


def kcbs_cf(ps):
    assignments = list(iproduct([0, 1], repeat=5))
    rows, caps = [], []
    for i in range(5):
        j = (i + 1) % 5
        table = {(1, 0): ps[i], (0, 1): ps[j],
                 (0, 0): 1 - ps[i] - ps[j], (1, 1): 0.0}
        for o, e in table.items():
            rows.append([1.0 if (g[i], g[j]) == o else 0.0
                         for g in assignments])
            caps.append(e)
    return 1.0 - ncf_lp(len(assignments), rows, caps)


def demonstrate(say):
    cf0 = square_cf(0.0)
    say(f"  square: contextual fraction CF = {cf0:.6f} — maximal; no fraction")
    say(f"    of the model is scripted. (The Z_2 address, now priced at 1.)")
    assert abs(cf0 - 1.0) < 1e-7

    say("  the dial: mix with uniform noise, CF(eps) computed by LP:")
    line = []
    for eps in [0.0, 0.05, 0.10, 0.20, 1 / 3, 0.40]:
        cf = square_cf(eps)
        line.append(f"eps={eps:.2f}: {cf:.4f}")
        assert abs(cf - max(0.0, 1 - 3 * eps)) < 1e-6
    say("    " + "   ".join(line))
    say("    exact law recovered: CF(eps) = 1 - 3*eps, dead at eps = 1/3 —")
    say("    the square's contextuality is worth exactly three times its noise.")

    ps = kcbs_model(say)
    cfk = kcbs_cf(ps)
    closed = 2 * np.sqrt(5) - 4
    say(f"  pentagon: CF = {cfk:.6f}; closed form 2*sqrt(5) - 4 = {closed:.6f}")
    assert abs(cfk - closed) < 1e-6
    assert 0.0 < cfk < 1.0
    say("  moral: the obstruction is now a gauge, not a verdict — address")
    say("         (Z_2 class), then price (CF = 1), now a dial (0.472, and a")
    say("         death at eps = 1/3). Graded resource, exactly measured.")


if __name__ == "__main__":
    demonstrate(print)
