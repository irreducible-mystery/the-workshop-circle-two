"""Seat P design probe (not a verification instrument): the hexagon
8-instance classification from bench plumbing (hex_residual_z2, line 124)
with f, R symbolic — polynomials in two variables over Z, coeff dicts
keyed (deg_f, deg_R)."""
import itertools

ONE = {(0, 0): 1}
Fv = {(1, 0): 1}
Rv = {(0, 1): 1}
ZERO = {}

def pmul(p, q):
    out = {}
    for k1, a in p.items():
        for k2, b in q.items():
            k = (k1[0] + k2[0], k1[1] + k2[1])
            out[k] = out.get(k, 0) + a * b
    return {k: v for k, v in out.items() if v}

def Fz2(a, b, c, d, x, y):
    if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
        return ZERO
    return Fv if (a, b, c) == (1, 1, 1) else ONE

def Rs(x, y):
    return Rv if (x, y) == (1, 1) else ONE

kinds = {}
n_adm = 0
for a, b, c, d in itertools.product((0, 1), repeat=4):
    e = (a + b) % 2
    z = (a + c) % 2
    if d != (e + c) % 2 or d != (z + b) % 2:
        continue
    n_adm += 1
    g = (b + c) % 2
    lhs = pmul(Rs(e, c), Fz2(c, a, b, d, z, e))
    rhs = pmul(pmul(Fz2(a, b, c, d, e, g), Rs(b, c)),
               pmul(Fz2(a, c, b, d, z, g), Rs(a, c)))
    if lhs == rhs:
        k = "R_eq_R" if lhs == Rv else ("one_eq_one" if lhs == ONE else f"OTHER-eq {lhs}")
    elif lhs == Fv and rhs == pmul(pmul(Fv, Fv), pmul(Rv, Rv)):
        k = "forcing"
    else:
        k = f"OTHER lhs={lhs} rhs={rhs}"
    kinds.setdefault(k, []).append((a, b, c, d))

print(f"admissible: {n_adm} of 16")
for k, v in kinds.items():
    print(f"{k} ({len(v)}): {v}")
assert n_adm == 8
assert len(kinds["one_eq_one"]) == 5 and len(kinds["R_eq_R"]) == 2
assert [q[:3] for q in kinds["forcing"]] == [(1, 1, 1)]
print("MATCHES CERTIFICATE G1d: (5, 2, 1, 0) over 8 admissible; forcing at (1,1,1), d =", kinds["forcing"][0][3])
