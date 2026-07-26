"""Seat P design probe (NOT a verification instrument — seat B stays blind):
reconstruct the 16-instance pentagon classification from the bench plumbing
(floor/symmetric_statistics.py line 108, pent_residual_z2) with f symbolic,
to know the concrete kind of each instance before writing the Lean.
Polynomials in f over Z as coefficient tuples (c0, c1, c2, ...)."""
import itertools

ONE = (1,)
F = (0, 1)
ZERO = (0,)

def pmul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)

def Fz2(a, b, c, d, x, y):
    if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
        return ZERO
    return F if (a, b, c) == (1, 1, 1) else ONE

kinds = {}
for a, b, c, dd in itertools.product((0, 1), repeat=4):
    x = (a + b) % 2
    y = (x + c) % 2
    t = (y + dd) % 2
    w = (c + dd) % 2
    v = (b + w) % 2
    u = (b + c) % 2
    lhs = pmul(pmul(Fz2(a, b, c, y, x, u), Fz2(a, u, dd, t, y, v)),
               Fz2(b, c, dd, v, u, w))
    rhs = pmul(Fz2(x, c, dd, t, y, w), Fz2(a, b, w, t, x, v))
    if lhs == rhs == ONE:
        k = "one_eq_one"
    elif lhs == rhs == F:
        k = "f_eq_f"
    elif lhs == (0, 0, 1) and rhs == ONE:
        k = "forcing"
    else:
        k = f"OTHER lhs={lhs} rhs={rhs}"
    kinds.setdefault(k, []).append((a, b, c, dd))

for k, v in kinds.items():
    print(f"{k} ({len(v)}): {v}")
assert set(kinds) == {"one_eq_one", "f_eq_f", "forcing"}
assert len(kinds["one_eq_one"]) == 11 and len(kinds["f_eq_f"]) == 4
assert kinds["forcing"] == [(1, 1, 1, 1)]
print("MATCHES CERTIFICATE: (11, 4, 1, 0), forcing at (1,1,1,1)")
