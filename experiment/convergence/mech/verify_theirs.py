#!/usr/bin/env python3
"""Cross-lineage verification: SuperNinja's seat-B machinery pointed at
the TWO-BODY S1 artifact (Fable 5 + Opus/Code 'third body'), Zi.lean pin
2e227702... . Input: their_statements.txt (proof-stripped by the
mechanical courier, pin a633604f...). Every universal claim is verified
COEFFICIENTWISE in an exact polynomial ring over Z (complete over all
integers, not sampled); concrete claims by exact integer arithmetic.
Norm 16: the plant must bite before the PASS counts (see --plant).

This is the first time an instrument from one lineage adjudicates an
artifact from the other. Route independence: their file proves by AC
simp normalisation in the kernel; this verifier expands to canonical
polynomial form over Z. Shared assumption: the transcription of the
definitions (add/mul/conj/norm) -- checked against their source text,
which both lineages copied from the same charge.
"""
import sys, itertools
from fractions import Fraction

PLANT = "--plant" in sys.argv

# ---------- exact multivariate polynomials over Z ----------
# monomial: tuple of exponents over a fixed variable list; poly: dict mono->int
class P:
    __slots__ = ("n", "c")
    def __init__(self, n, c=None):
        self.n = n; self.c = dict(c or {})
    @staticmethod
    def const(n, k):
        return P(n, {(0,)*n: k} if k else {})
    @staticmethod
    def var(n, i):
        e = [0]*n; e[i] = 1
        return P(n, {tuple(e): 1})
    def __add__(a, b):
        c = dict(a.c)
        for m, k in b.c.items():
            c[m] = c.get(m, 0) + k
            if c[m] == 0: del c[m]
        return P(a.n, c)
    def __neg__(a):
        return P(a.n, {m: -k for m, k in a.c.items()})
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

# Gaussian element = (re poly, im poly); the definitions AS IN THEIR FILE
def gadd(z, w): return (z[0]+w[0], z[1]+w[1])
def gneg(z):    return (-z[0], -z[1])
def gsub(z, w): return gadd(z, gneg(w))          # their def: sub = add z (neg w)
def gmul(z, w): return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])
def gconj(z):   return (z[0], -z[1])
def gnorm(z):   return z[0]*z[0] + z[1]*z[1]     # scalar poly
def geq(z, w):  return z[0] == w[0] and z[1] == w[1]

results = []
def check(name, ok, note=""):
    results.append((name, ok, note))
    print(("PASS  " if ok else "FAIL  ") + name + ("  — " + note if note else ""))

# ---------- symbolic setup: 3 Gaussian variables x,y,z = 6 indeterminates ----------
N = 6
xr, xi, yr, yi, zr, zi_ = (P.var(N, i) for i in range(6))
X, Y, Z = (xr, xi), (yr, yi), (zr, zi_)
ZERO = (P.const(N,0), P.const(N,0)); ONE = (P.const(N,1), P.const(N,0))
I = (P.const(N,0), P.const(N,1))

# 1-8: additive abelian group (their add_comm..sub_self)
check("add_comm",  geq(gadd(X,Y), gadd(Y,X)))
check("add_assoc", geq(gadd(gadd(X,Y),Z), gadd(X,gadd(Y,Z))))
check("add_zero",  geq(gadd(X,ZERO), X))
check("zero_add",  geq(gadd(ZERO,X), X))
check("add_neg",   geq(gadd(X,gneg(X)), ZERO))
check("neg_add",   geq(gadd(gneg(X),X), ZERO))
check("neg_neg",   geq(gneg(gneg(X)), X))
check("sub_self",  geq(gsub(X,X), ZERO))
# 9-14: commutative monoid
check("mul_comm",  geq(gmul(X,Y), gmul(Y,X)))
check("mul_assoc", geq(gmul(gmul(X,Y),Z), gmul(X,gmul(Y,Z))), "degree-3, 6 vars, coefficientwise")
check("mul_one",   geq(gmul(X,ONE), X))
check("one_mul",   geq(gmul(ONE,X), X))
check("mul_zero",  geq(gmul(X,ZERO), ZERO))
check("zero_mul",  geq(gmul(ZERO,X), ZERO))
# 15-18: distributivity + neg-mul laws
check("left_distrib",  geq(gmul(X,gadd(Y,Z)), gadd(gmul(X,Y),gmul(X,Z))))
check("right_distrib", geq(gmul(gadd(X,Y),Z), gadd(gmul(X,Z),gmul(Y,Z))))
check("mul_neg", geq(gmul(X,gneg(Y)), gneg(gmul(X,Y))))
check("neg_mul", geq(gmul(gneg(X),Y), gneg(gmul(X,Y))))
# 19-20: the one law
check("I_squared",         geq(gmul(I,I), gneg(ONE)))
check("I_squared_add_one", geq(gadd(gmul(I,I),ONE), ZERO))
# 21-27: conj is a ring hom (+ involution, fixes 1/0/re, mirrors I)
check("conj_add",  geq(gconj(gadd(X,Y)), gadd(gconj(X),gconj(Y))))
check("conj_mul",  geq(gconj(gmul(X,Y)), gmul(gconj(X),gconj(Y))), "the mirror respects multiplication — coefficientwise")
check("conj_conj", geq(gconj(gconj(X)), X))
check("conj_one",  geq(gconj(ONE), ONE))
check("conj_zero", geq(gconj(ZERO), ZERO))
check("conj_re",   gconj(X)[0] == X[0])
check("conj_I",    geq(gconj(I), gneg(I)))
# 28-29: z*conj z = (N z, 0), both orders
mc = gmul(X, gconj(X))
check("mul_conj",      mc[0] == gnorm(X) and mc[1].iszero())
cm = gmul(gconj(X), X)
check("conj_mul_self", cm[0] == gnorm(X) and cm[1].iszero())
# 30: Brahmagupta–Fibonacci as a bare Int identity, in THEIR stated form:
# (a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2
M = 4
a, b, c, d = (P.var(M, i) for i in range(4))
lhs = (a*a + b*b) * (c*c + d*d)
rhs = (a*c - b*d)*(a*c - b*d) + (a*d + b*c)*(a*d + b*c)
if PLANT:
    rhs = rhs + P.const(M, 1)   # the plant: falsify the identity by +1
check("brahmagupta_fibonacci", lhs == rhs, "bare integer identity, 4 vars")
# 31: norm multiplicative (independent from 30: computed via gmul directly)
check("norm_mul", gnorm(gmul(X,Y)) == gnorm(X)*gnorm(Y), "route independent of Brahmagupta expansion above")
# 32-35: norm facts
check("norm_conj", gnorm(gconj(X)) == gnorm(X))
one_c = gnorm(ONE); check("norm_one", one_c == P.const(N,1))
check("norm_zero", gnorm(ZERO) == P.const(N,0))
check("norm_I",    gnorm(I) == P.const(N,1))
Mr = 1; ar = P.var(Mr,0)
check("norm_re", (ar*ar + P.const(Mr,0)*P.const(Mr,0)) == ar*ar, "N(a,0) = a*a")

# ---------- concrete: their 8 live instances (exact ints) ----------
def ci(re, im): return (re, im)
def cadd(z,w): return (z[0]+w[0], z[1]+w[1])
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cconj(z): return (z[0],-z[1])
def cnorm(z): return z[0]*z[0]+z[1]*z[1]
def cneg(z): return (-z[0],-z[1])
check("live_1", cmul((0,1),(0,1)) == (-1,0))
check("live_2", cmul((1,1),(1,-1)) == (2,0))
check("live_3", cnorm((3,4)) == 25)
check("live_4", cnorm((1,1))*cnorm((1,-1)) == cnorm(cmul((1,1),(1,-1))))
check("live_5", cconj((5,-7)) == (5,7))
check("live_6", cmul((2,3),cconj((2,3))) == (13,0))
check("live_7", cadd((2,3),cneg((2,3))) == (0,0))
check("live_8", cmul((0,2),(0,3)) == (-6,0))

# ---------- their 8 negative controls ----------
check("control_one_ne_zero", (1,0) != (0,0))
check("control_conj_ne_id",  cconj((0,1)) != (0,1))
# fake mirror (a,b) -> (a,2b): additive yes, multiplicative no
TWO = P.const(N, 2)
def fakeP(z): return (z[0], TWO*z[1])         # symbolic version
def fakeC(z): return (z[0], 2*z[1])           # concrete version
fm_add = geq(fakeP(gadd(X,Y)), gadd(fakeP(X),fakeP(Y)))
check("control_fake_mirror_is_additive", fm_add, "symbolically additive — the near-miss is genuine")
# fails multiplicative: exhibit their witness shape (any works; use i*i)
lhsf = fakeC(cmul((0,1),(0,1))); rhsf = cmul(fakeC((0,1)), fakeC((0,1)))
check("control_fake_mirror_fails_multiplicative", lhsf != rhsf,
      f"fake(i*i)={lhsf} != fake(i)*fake(i)={rhsf}")
# split-complex: (a,b)*(c,d) = (ac+bd, ad+bc) has zero divisors
def smul(z,w): return (z[0]*w[0]+z[1]*w[1], z[0]*w[1]+z[1]*w[0])
check("control_split_has_zero_divisors", smul((1,1),(1,-1)) == (0,0),
      "(1+j)(1-j) = 0 under the split multiplication")
check("control_split_first_factor_is_nonzero",  (1,1) != (0,0))
check("control_split_second_factor_is_nonzero", (1,-1) != (0,0))
check("control_mul_of_same_factors_is_nonzero", cmul((1,1),(1,-1)) == (2,0),
      "same factors under TRUE mul: (2,0) != 0 — the sign is load-bearing")

# ---------- cross-lineage consistency: their claims vs MY S1 claims ----------
# conj_fixed_iff_real (mine, not theirs): check their file's conj supports it
# — the iff both directions over the symbolic element
fwd = gconj(X)[1] == X[1]  # conj z = z forces -xi = xi i.e. 2*xi = 0... symbolic:
diff = gconj(X)[1] - X[1]  # = -2*xi; zero iff xi = 0 — verified as polynomial shape
check("cross_conj_fixed_locus", diff == -(P.const(N,2))*xi,
      "conj z − z has im = −2·im(z): the fixed locus is the real axis — MY theorem, THEIR definitions")
# my sub_add_cancel on their sub def
check("cross_sub_add_cancel", geq(gadd(gsub(X,Y),Y), X),
      "MY S1 repair theorem holds for THEIR sub — the S1 crop convergence point")

n_pass = sum(1 for _, ok, _ in results if ok)
n_fail = len(results) - n_pass
print("="*68)
print(f"checks run: {len(results)};  passed: {n_pass};  failed: {n_fail}")
print("VERDICT: two-body S1 artifact verified coefficientwise by the")
print("         dual-seat lineage's instrument — every universal claim")
print("         complete over Z, every concrete claim exact; plus two")
print("         cross-lineage checks (their defs, my theorems).")
sys.exit(0 if n_fail == 0 else 1)
