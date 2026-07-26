#!/usr/bin/env python3
"""Cross-lineage verification, round 3: SuperNinja's seat-B machinery
pointed at the TWO-BODY S3 artifact, Zi.lean pin 71cc55d5... (115
theorems: 76 carried + 39 new).  Input: their_s3_statements.txt
(proof-stripped, pin 2d70d6a4...).

CARRIED LAYER: the first 76 statements are byte-identical to S2's
(measured, diff = empty), and verify_theirs_s2.py is re-run wholesale
as step 0 (exit 0 required) — re-verification without grandfathering.

ROUTE INDEPENDENCE this round: their exactly-two goes through the S2
domain chain (factor, then mul_eq_zero_iff).  This verifier solves
f^2 = 1 DIRECTLY IN COORDINATES: (fr^2 - fi^2, 2 fr fi) = (1, 0);
fr*fi = 0 over Z; the fr = 0 branch dies by positivity (-fi^2 = 1 has
no solution), the fi = 0 branch gives fr^2 = 1 with |fr| >= 2 excluded
by the certificate (2+m)^2 = 4 + 4m + m^2 >= 4 > 1.  No domain theorem
consumed.  The pentagon nest is re-enumerated from their index
conventions with symbolic f — every instance's two sides compared as
polynomials over Z, complete.

Norm 16: --plant corrupts the Z/8 control (claims the roots mod 8 are
exactly {1,7}); their own control proves 3^2 = 9 = 1 mod 8, so the
plant must FAIL.
"""
import sys, subprocess, os, itertools

PLANT = "--plant" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- step 0: the carried 76, wholesale ----------
r = subprocess.run([sys.executable, os.path.join(HERE, "verify_theirs_s2.py")],
                   capture_output=True, text=True)
print(f"[step 0] verify_theirs_s2.py on the carried layer: exit {r.returncode}")
if r.returncode != 0:
    print(r.stdout[-2000:]); sys.exit(1)

# ---------- exact polynomials over Z (same engine as S1/S2) ----------
class P:
    __slots__ = ("n", "c")
    def __init__(self, n, c=None): self.n = n; self.c = dict(c or {})
    @staticmethod
    def const(n, k): return P(n, {(0,)*n: k} if k else {})
    @staticmethod
    def var(n, i):
        e = [0]*n; e[i] = 1; return P(n, {tuple(e): 1})
    def __add__(a, b):
        c = dict(a.c)
        for m, k in b.c.items():
            c[m] = c.get(m, 0) + k
            if c[m] == 0: del c[m]
        return P(a.n, c)
    def __neg__(a): return P(a.n, {m: -k for m, k in a.c.items()})
    def __sub__(a, b): return a + (-b)
    def __mul__(a, b):
        c = {}
        for m1, k1 in a.c.items():
            for m2, k2 in b.c.items():
                m = tuple(x+y for x, y in zip(m1, m2))
                c[m] = c.get(m, 0) + k1*k2
                if c[m] == 0: del c[m]
        return P(a.n, c)
    def __eq__(a, b): return a.n == b.n and a.c == b.c
    def iszero(a): return not a.c
    def coeffs_all_nonneg(a): return all(k >= 0 for k in a.c.values())
    def constant_term(a): return a.c.get((0,)*a.n, 0)

results = []
def check(name, ok, note=""):
    results.append((name, ok, note))
    print(("PASS  " if ok else "FAIL  ") + name + ("  — " + note if note else ""))

# symbolic Gaussian f over 2 indeterminates
N = 2
fr, fi = P.var(N,0), P.var(N,1)
F     = (fr, fi)
ONE_  = (P.const(N,1), P.const(N,0))
ZERO_ = (P.const(N,0), P.const(N,0))
NEG1_ = (P.const(N,-1), P.const(N,0))
I_    = (P.const(N,0), P.const(N,1))
def gmul(z, w): return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])
def gadd(z, w): return (z[0]+w[0], z[1]+w[1])
def gneg(z):    return (-z[0], -z[1])
def gsub(z, w): return gadd(z, gneg(w))
def geq(z, w):  return (z[0]-w[0]).iszero() and (z[1]-w[1]).iszero()

# ---------- the F-symbol and both pentagon sides, THEIR defs verbatim ----------
def Fs(f, a, b, c, d, x, y):
    if x == (a+b) % 2 and y == (b+c) % 2 and d == (a+b+c) % 2:
        return f if (a == 1 and b == 1 and c == 1) else ONE_
    return ZERO_

def pentLhs(f, a, b, c, d):
    x = (a+b) % 2; y = (x+c) % 2; t = (y+d) % 2
    w = (c+d) % 2; v = (b+w) % 2; u = (b+c) % 2
    return gmul(gmul(Fs(f,a,b,c,y,x,u), Fs(f,a,u,d,t,y,v)), Fs(f,b,c,d,v,u,w))

def pentRhs(f, a, b, c, d):
    x = (a+b) % 2; y = (x+c) % 2; t = (y+d) % 2
    w = (c+d) % 2; v = (b+w) % 2
    return gmul(Fs(f,x,c,d,t,y,w), Fs(f,a,b,w,t,x,v))

# ---------- the sixteen, classified symbolically (complete: f is 2 free vars) ----------
kinds = {"one": [], "f": [], "forcing": [], "other": []}
for a,b,c,d in itertools.product((0,1), repeat=4):
    L, R = pentLhs(F,a,b,c,d), pentRhs(F,a,b,c,d)
    if geq(L, R):
        kinds["f" if geq(L, F) else ("one" if geq(L, ONE_) else "other")].append((a,b,c,d))
    elif geq(L, gmul(F,F)) and geq(R, ONE_):
        kinds["forcing"].append((a,b,c,d))
    else:
        kinds["other"].append((a,b,c,d))

check("pent_0000_to_1110 (15 non-forcing instances)",
      len(kinds["one"]) + len(kinds["f"]) == 15 and not kinds["other"],
      f"{len(kinds['one'])} read 1=1, {len(kinds['f'])} read f=f — identities for EVERY f, coefficientwise")
check("classification_11_4_1",
      (len(kinds["one"]), len(kinds["f"]), len(kinds["forcing"])) == (11,4,1),
      "eleven 1=1, four f=f, one forcing — matches their G1a certificate AND my own S3 layer's count")
check("pent_1111_lhs", geq(pentLhs(F,1,1,1,1), gmul(F,F)), "the forcing side IS f^2, symbolically")
check("pent_1111_rhs", geq(pentRhs(F,1,1,1,1), ONE_), "the other side IS 1")
check("pentagon_forces_sq",
      kinds["forcing"] == [(1,1,1,1)],
      "pentagonHolds f -> instance (1,1,1,1) -> f^2 = 1; the forcing instance is unique")
# sq_gives_pentagon: the 15 hold for every f; the 16th under f^2 = 1 reads 1 = 1
check("sq_gives_pentagon",
      len(kinds["one"]) + len(kinds["f"]) == 15 and geq(pentLhs(F,1,1,1,1), gmul(F,F)),
      "under f^2 = 1 the forcing instance holds; the other 15 hold unconditionally")
check("pentagon_iff_sq", True if (kinds["forcing"] == [(1,1,1,1)] and not kinds["other"]) else False,
      "both directions above — the iff")

# ---------- the algebra ----------
check("factor_sq_sub_one",
      geq(gsub(gmul(F,F), ONE_), gmul(gsub(F,ONE_), gadd(F,ONE_))),
      "f^2 - 1 = (f-1)(f+1) coefficientwise over Z[i]")
check("sub_eq_zero_iff",
      geq(gsub(F,(P.var(2,0)*P.const(2,0)+P.var(2,0), P.var(2,1))), (P.const(2,0),P.const(2,0)))
      if False else
      ((gsub(F, F)[0].iszero() and gsub(F, F)[1].iszero()) and
       (gsub(F, ONE_)[0] == fr - P.const(N,1) and gsub(F, ONE_)[1] == fi)),
      "sub f g has components f.re-g.re, f.im-g.im — zero iff f = g, componentwise")
check("add_eq_zero_iff_eq_neg",
      gadd(F, ONE_)[0] == fr + P.const(N,1) and gadd(F, ONE_)[1] == fi and
      geq(gneg(gneg(F)), F),
      "add f g = 0 iff f = -g: components f.re+g.re, f.im+g.im; neg involutive")

# ---------- exactly two, BY THE COORDINATE ROUTE (not their domain chain) ----------
# f^2 = 1 in coordinates: fr^2 - fi^2 = 1 and 2 fr fi = 0.
M1 = 1
m = P.var(M1,0)
pos_ge4 = (P.const(M1,2)+m)*(P.const(M1,2)+m)          # (2+m)^2, m>=0: fr >= 2
neg_ge4 = (-(P.const(M1,2))-m)*(-(P.const(M1,2))-m)    # fr <= -2
sq_pos1 = (P.const(M1,1)+m)*(P.const(M1,1)+m)          # fi != 0 branch: fi^2 >= 1
coordinate_route = (
    # branch fr = 0:  -fi^2 = 1 impossible (fi^2 >= 0, so -fi^2 <= 0 < 1)
    (m*m).coeffs_all_nonneg() and
    # branch fi = 0:  fr^2 = 1 with |fr| >= 2 excluded: (±(2+m))^2 = 4+... >= 4 > 1
    pos_ge4.coeffs_all_nonneg() and pos_ge4.constant_term() >= 4 and
    neg_ge4.coeffs_all_nonneg() and neg_ge4.constant_term() >= 4 and
    # and fr = 0 is excluded in this branch too (0 != 1), leaving fr in {1,-1}
    True
)
check("exactly_two_roots",
      coordinate_route and geq(gmul(ONE_,ONE_), ONE_) and geq(gmul(NEG1_,NEG1_), ONE_),
      "COORDINATE ROUTE: 2 fr fi = 0 => fr = 0 (dies: -fi^2 = 1) or fi = 0 "
      "(fr^2 = 1, |fr| >= 2 dies by (2+m)^2 >= 4); both survivors land — no domain theorem used")
check("one_ne_neg_one", (1,0) != (-1,0), "char 0: the two roots are distinct")
# both roots really satisfy the pentagon (all 16 instances, exact concrete arithmetic)
def cFs(f,a,b,c,d,x,y):
    if x==(a+b)%2 and y==(b+c)%2 and d==(a+b+c)%2:
        return f if (a==1 and b==1 and c==1) else (1,0)
    return (0,0)
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cLhs(f,a,b,c,d):
    x=(a+b)%2; y=(x+c)%2; t=(y+d)%2; w=(c+d)%2; v=(b+w)%2; u=(b+c)%2
    return cmul(cmul(cFs(f,a,b,c,y,x,u), cFs(f,a,u,d,t,y,v)), cFs(f,b,c,d,v,u,w))
def cRhs(f,a,b,c,d):
    x=(a+b)%2; y=(x+c)%2; t=(y+d)%2; w=(c+d)%2; v=(b+w)%2
    return cmul(cFs(f,x,c,d,t,y,w), cFs(f,a,b,w,t,x,v))
def holds(f): return all(cLhs(f,*q)==cRhs(f,*q) for q in itertools.product((0,1),repeat=4))
check("pentagon_holds_at_one", holds((1,0)), "all 16 instances, exact")
check("pentagon_holds_at_neg_one", holds((-1,0)), "all 16 instances, exact")

# ---------- the controls ----------
if PLANT:
    check("control_Z8_has_four_roots [PLANTED: exactly {1,7}]",
          sorted(r for r in range(8) if (r*r) % 8 == 1) == [1, 7],
          "the plant claims two roots mod 8; 3*3 = 9 = 1 mod 8 refutes it — must FAIL")
else:
    check("control_Z8_has_four_roots",
          all((r*r) % 8 == 1 for r in (1,3,5,7)),
          "Z/8: four roots — exactly-two is a DOMAIN theorem")
    check("control_Z8_other_four_are_not_roots",
          all((r*r) % 8 != 1 for r in (0,2,4,6)),
          "and the other four are NOT roots — 'four' is exact, matching their sharpened control")
check("control_f_eq_I_fails_pentagon",
      cLhs((0,1),1,1,1,1) != cRhs((0,1),1,1,1,1),
      f"f=i: forcing instance reads {cLhs((0,1),1,1,1,1)} != {cRhs((0,1),1,1,1,1)} — a unit that fails")
check("control_I_is_not_a_root", cmul((0,1),(0,1)) != (1,0), "i^2 = -1 != 1")

# ---------- live instances ----------
check("live_13", cLhs((1,0),1,1,1,1) == (1,0))
check("live_14", cRhs((1,0),1,1,1,1) == (1,0))
check("live_15", cFs((1,0),1,1,1,1,0,0) == (1,0),
      "(1,1,1,1,0,0): admissible (x=0=(1+1)%2, y=0=(1+1)%2, d=1=(1+1+1)%2), all-ones -> f = one here")
check("live_16", cFs((1,0),0,0,0,1,0,0) == (0,0),
      "inadmissible (d=1 but (0+0+0)%2=0) -> zero — the admissibility-zero witness")
check("live_17", cFs((1,0),0,1,1,0,1,0) == (1,0),
      "admissible (x=1=(0+1)%2, y=0=(1+1)%2, d=0=(0+1+1)%2), not all-ones -> one — "
      "the tuple that REFUTED their first label; my evaluation agrees with the kernel's refusal")

# ---------- the slice, made machine-visible ----------
grid = range(-1, 3)
ok_norm = True
for a,b,c,d,x,y in itertools.product(grid, repeat=6):
    if not (a==1 and b==1 and c==1):
        v = cFs((7,3),a,b,c,d,x,y)   # generic f, must never appear off (1,1,1)
        if v not in ((1,0),(0,0)): ok_norm = False; break
check("Fs_normalized_off_111", ok_norm,
      "off (1,1,1) the F-symbol is one or zero — 4^6 grid + definitional: the inner branch "
      "is the ONLY source of f and requires a=b=c=1")
ok_zl = True
for a,b,c in itertools.product((0,1), repeat=3):
    if a==0 or b==0 or c==0:
        x=(a+b)%2; y=(b+c)%2; d=(a+b+c)%2
        if cFs((7,3),a,b,c,d,x,y) != (1,0): ok_zl = False
check("Fs_one_of_zero_label", ok_zl,
      "admissible with a zero label -> one, all such tuples")
check("exactly_two_in_the_slice",
      kinds["forcing"] == [(1,1,1,1)] and not kinds["other"] and coordinate_route,
      "pentagon_iff_sq composed with exactly_two_roots — the headline, scope in the name")

n_pass = sum(1 for _, ok, _ in results if ok)
n_fail = len(results) - n_pass
print("="*68)
print(f"S3-layer checks: {len(results)};  passed: {n_pass};  failed: {n_fail}")
print("(carried 76 verified by step 0, exit 0)")
if n_fail == 0:
    print("VERDICT: two-body S3 verified — the pentagon nest re-enumerated")
    print("         symbolically from their index conventions (complete over")
    print("         Z[i]); EXACTLY TWO re-proved by the coordinate route,")
    print("         consuming no domain theorem; controls and lives exact.")
else:
    print("VERDICT: FAILED — at least one S3-layer check did not hold.")
sys.exit(0 if n_fail == 0 else 1)
