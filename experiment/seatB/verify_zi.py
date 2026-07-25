#!/usr/bin/env python3
"""verify_zi.py — SEAT B: exact reimplementation of every Zi.lean claim,
from the courier's statement extraction alone (Zi_statements_v2.txt, sha256
12ea1133de97d6782006f97733f52d568e6a7a186ac449c8429603ae0257ed08).
No proof bodies were read. Every check is exact integer arithmetic —
no floats anywhere. Universal claims are checked two ways per the house
style: (1) symbolically over polynomial coefficients (exact, complete —
each identity is a polynomial identity in the coordinates, so verifying
coefficient equality over Z proves it for ALL integers), and (2) on a
concrete grid as a sanity cross-check.

Norms: every check asserts (F2); negative controls per family (norm 5);
counts tied to nests (norm 9); exit 0 + summary is the pass condition.
"""

import itertools, sys
from fractions import Fraction

# ---------------------------------------------------------------------------
# Exact polynomial arithmetic over Z in named indeterminates.
# A polynomial is a dict: frozenset-of-(var,power) tuples -> int coeff.
# ---------------------------------------------------------------------------

def pvar(name):
    return {((name, 1),): 1}

def pconst(c):
    return {(): c} if c else {}

def padd(p, q):
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, 0) + c
        if r[m] == 0:
            del r[m]
    return r

def pneg(p):
    return {m: -c for m, c in p.items()}

def psub(p, q):
    return padd(p, pneg(q))

def pmul(p, q):
    r = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            d = {}
            for v, e in m1:
                d[v] = d.get(v, 0) + e
            for v, e in m2:
                d[v] = d.get(v, 0) + e
            m = tuple(sorted(d.items()))
            r[m] = r.get(m, 0) + c1 * c2
            if r[m] == 0:
                del r[m]
    return r

def pzero(p):
    return not p

# ---------------------------------------------------------------------------
# Zi over polynomials: a pair (re, im) of polynomials. Definitions are
# transcribed FROM THE STATEMENT FILE's def lines, independently.
# ---------------------------------------------------------------------------

def zi(re, im):
    return (re, im)

ZERO = (pconst(0), pconst(0))
ONE  = (pconst(1), pconst(0))
I    = (pconst(0), pconst(1))

def zadd(z, w):
    return (padd(z[0], w[0]), padd(z[1], w[1]))

def zmul(z, w):
    return (psub(pmul(z[0], w[0]), pmul(z[1], w[1])),
            padd(pmul(z[0], w[1]), pmul(z[1], w[0])))

def zneg(z):
    return (pneg(z[0]), pneg(z[1]))

def zsub(z, w):
    return zadd(z, zneg(w))

def zconj(z):
    return (z[0], pneg(z[1]))

def znormSq(z):
    return padd(pmul(z[0], z[0]), pmul(z[1], z[1]))

def zeq(z, w):
    return pzero(psub(z[0], w[0])) and pzero(psub(z[1], w[1]))

def zfakeMirror(z):
    return (z[0], pmul(pconst(2), z[1]))

def zcoordMul(z, w):
    return (pmul(z[0], w[0]), pmul(z[1], w[1]))

# symbolic elements
A = zi(pvar('a'), pvar('b'))
B = zi(pvar('c'), pvar('d'))
C = zi(pvar('e'), pvar('f'))

checks = []
def check(name, ok):
    checks.append((name, ok))
    print(("PASS  " if ok else "FAIL  ") + name)
    return ok

# ---------------------------------------------------------------------------
# Concrete-grid evaluators (sanity cross-check on Z, exact ints).
# ---------------------------------------------------------------------------

GRID = [-3, -1, 0, 2, 5]

def cadd(z, w): return (z[0]+w[0], z[1]+w[1])
def cmul(z, w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cneg(z):    return (-z[0], -z[1])
def cconj(z):   return (z[0], -z[1])
def cnorm(z):   return z[0]*z[0]+z[1]*z[1]

def grid_pairs():
    return [ (a,b) for a in GRID for b in GRID ]

# ===========================================================================
print("=" * 70)
print("SEAT B — exact reimplementation of Zi.lean claims (statements only)")
print("=" * 70)

# --- additive laws (symbolic = complete proof over Z) ---
check("add_comm_symbolic", zeq(zadd(A, B), zadd(B, A)))
check("add_assoc_symbolic", zeq(zadd(zadd(A, B), C), zadd(A, zadd(B, C))))
check("zero_add_symbolic", zeq(zadd(ZERO, A), A))
check("add_zero_symbolic", zeq(zadd(A, ZERO), A))
check("add_neg_symbolic", zeq(zadd(A, zneg(A)), ZERO))
check("neg_add_symbolic", zeq(zadd(zneg(A), A), ZERO))
check("sub_add_cancel_symbolic", zeq(zadd(zsub(A, B), B), A))

# --- multiplicative laws ---
check("mul_comm_symbolic", zeq(zmul(A, B), zmul(B, A)))
check("mul_assoc_symbolic", zeq(zmul(zmul(A, B), C), zmul(A, zmul(B, C))))
check("one_mul_symbolic", zeq(zmul(ONE, A), A))
check("mul_one_symbolic", zeq(zmul(A, ONE), A))
check("zero_mul_symbolic", zeq(zmul(ZERO, A), ZERO))
check("mul_zero_symbolic", zeq(zmul(A, ZERO), ZERO))
check("mul_add_symbolic", zeq(zmul(A, zadd(B, C)), zadd(zmul(A, B), zmul(A, C))))
check("add_mul_symbolic", zeq(zmul(zadd(A, B), C), zadd(zmul(A, C), zmul(B, C))))
check("neg_mul_symbolic", zeq(zmul(zneg(A), B), zneg(zmul(A, B))))
check("mul_neg_symbolic", zeq(zmul(A, zneg(B)), zneg(zmul(A, B))))

# --- the one new law ---
check("i_squared_is_minus_one", zeq(zmul(I, I), zneg(ONE)))

# --- conj as ring hom ---
check("conj_add_symbolic", zeq(zconj(zadd(A, B)), zadd(zconj(A), zconj(B))))
check("conj_mul_symbolic", zeq(zconj(zmul(A, B)), zmul(zconj(A), zconj(B))))
check("conj_zero", zeq(zconj(ZERO), ZERO))
check("conj_one", zeq(zconj(ONE), ONE))
check("conj_conj_symbolic", zeq(zconj(zconj(A)), A))
check("conj_I", zeq(zconj(I), zneg(I)))
check("conj_fixes_real_symbolic", zeq(zconj((pvar('a'), pconst(0))), (pvar('a'), pconst(0))))

# conj_fixed_iff_real: conj z = z <-> im = 0. Symbolically: conj z - z = (0, -2b),
# which is zero iff b = 0 — over Z (char 0, 2 invertible in Q), exact.
diff = zsub(zconj(A), A)
fixed_forward = pzero(diff[0]) and (diff[1] == pmul(pconst(-2), pvar('b')))
# -2b = 0 iff b = 0 over Z: coefficient -2 is nonzero. Both directions hold.
check("conj_fixed_iff_real_symbolic", fixed_forward)
# grid confirmation of the iff, both directions, nest = 25 pairs
iff_grid = all(((cconj(z) == z) == (z[1] == 0)) for z in grid_pairs())
check("conj_fixed_iff_real_grid_nest25", iff_grid)

# --- the norm ---
check("mul_conj_eq_normSq_symbolic",
      zeq(zmul(A, zconj(A)), (znormSq(A), pconst(0))))
check("conj_mul_eq_normSq_symbolic",
      zeq(zmul(zconj(A), A), (znormSq(A), pconst(0))))

# brahmagupta_fibonacci_int as a polynomial identity in 4 indeterminates
a, b, c, d = pvar('a'), pvar('b'), pvar('c'), pvar('d')
lhs = padd(
    pmul(psub(pmul(a, c), pmul(b, d)), psub(pmul(a, c), pmul(b, d))),
    pmul(padd(pmul(a, d), pmul(b, c)), padd(pmul(a, d), pmul(b, c))))
rhs = pmul(padd(pmul(a, a), pmul(b, b)), padd(pmul(c, c), pmul(d, d)))
check("brahmagupta_fibonacci_symbolic", pzero(psub(lhs, rhs)))

check("normSq_mul_symbolic",
      pzero(psub(znormSq(zmul(A, B)), pmul(znormSq(A), znormSq(B)))))
check("normSq_zero", pzero(psub(znormSq(ZERO), pconst(0))))
check("normSq_one", pzero(psub(znormSq(ONE), pconst(1))))
check("normSq_I", pzero(psub(znormSq(I), pconst(1))))
check("normSq_conj_symbolic", pzero(psub(znormSq(zconj(A)), znormSq(A))))

# --- live witnesses (transcribed from the statements) ---
check("live_mul_witness", cmul((1, 2), (3, 4)) == (-5, 10))
check("live_normSq_witness", cnorm((3, 4)) == 25)
check("live_add_witness", cadd((1, 2), (3, 4)) == (4, 6))
check("live_conj_witness", cconj((3, 4)) == (3, -4))

# --- negative controls: verify each control's CLAIM (the inequality) ---
fm = lambda z: (z[0], 2 * z[1])
ii = cmul((0, 1), (0, 1))
check("control_fake_mirror_fails", fm(ii) != cmul(fm((0, 1)), fm((0, 1))))
check("control_coordMul_differs", (0 * 0, 1 * 1) != ii)
check("control_conj_not_id", cconj((0, 1)) != (0, 1))
check("control_normSq_not_additive", cnorm((2, 0)) != cnorm((1, 0)) + cnorm((1, 0)))

# --- SEAT B's OWN negative control (norm 5, this instrument's family):
# a deliberately WRONG identity must FAIL the symbolic checker —
# a checker that cannot fail is not a checker.
wrong = zeq(zmul(A, B), zadd(A, B))   # z*w = z+w is false
check("negcontrol_checker_can_fail", wrong is False)
# and the fake mirror must fail multiplicativity SYMBOLICALLY too:
fmA = zfakeMirror(A); fmB = zfakeMirror(B)
check("negcontrol_fakeMirror_not_hom_symbolic",
      not zeq(zfakeMirror(zmul(A, B)), zmul(fmA, fmB)))

# --- grid cross-checks of the two headline identities, nest = 625 ---
bf_grid = all(
    (pa*pc - pb*pd)**2 + (pa*pd + pb*pc)**2 == (pa*pa + pb*pb)*(pc*pc + pd*pd)
    for pa, pb in grid_pairs() for pc, pd in grid_pairs())
check("brahmagupta_grid_nest625", bf_grid)
nm_grid = all(
    cnorm(cmul((pa, pb), (pc, pd))) == cnorm((pa, pb)) * cnorm((pc, pd))
    for pa, pb in grid_pairs() for pc, pd in grid_pairs())
check("normSq_mul_grid_nest625", nm_grid)

# ===========================================================================
npass = sum(1 for _, ok in checks if ok)
nfail = len(checks) - npass
print("=" * 70)
print(f"checks run: {len(checks)};  passed: {npass};  failed: {nfail}")
if nfail:
    print("VERDICT: NOT CLEAN")
    sys.exit(1)
print("VERDICT: every Zi.lean claim re-derived exactly; symbolic = complete")
print("         over Z (polynomial coefficient equality), grid co-signs.")
sys.exit(0)
