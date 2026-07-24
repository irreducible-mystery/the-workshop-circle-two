#!/usr/bin/env python3
"""c2_gift_certificates.py — CIRCLE TWO CHARTER AUDIT: every number and every
design element the symmetric-world charter will carry, certified in exact
arithmetic before a single Lean line is written.

CIRCLE ONE proved flatland braids in exactly two ways (golden and Yang-Lee,
Galois conjugates).  CIRCLE TWO is to prove the roomy world holds exactly two
particles (boson and fermion) — the Z2 atlas over Z[i], complete.  The bench
is symmetric_statistics.py.  This script certifies:

  G0  the ground: the three benches re-run green (subprocess, artifact-faithful).
  G1  the bench's claims, upgraded to exact arithmetic:
      pentagon for Z2 fusion = 16 instances = 11 (1=1) + 4 (f=f) + 1 forcing
      (f^2 = 1); hexagon = 8 instances = 5 (1=1) + 2 (R=R) + 1 forcing
      (f = f^2 R^2, i.e. R^2 = F per class); the numeric search reproduced
      seed-exactly and characterized exactly; gauge invariance of the (1,1,1)
      slot; the flatland filter killing the semions; exclusion ranks
      1,3,6,10,15 as INTEGER matrix ranks (not floats); twist -1, nu +1;
      the golden negative control with an interval-certified exact residual.
  G2  the ring: Z[i] as int pairs; ring laws + Brahmagupta-Fibonacci
      SYMBOLICALLY (dict-polynomials over Z, not spot checks); the domain
      by mod-4 descent: squares mod 4 = {0,1}, the 16-case decide over
      (Z/4)^2, the halving step, torsion-freeness, the conj(z)*z = N(z) chain.
  G3  exactly-two, four designs: (a) pentagon necessity (any comm ring:
      pentagon <=> F^2 = 1; domain => exactly two); (b) hexagon necessity
      (R^2 = F per class; domain => exactly two per class; both hexagons);
      (c) the filter as a GALOIS statement (conj-fixed points; on units,
      R real <=> conj R = R <=> R^2 = 1 <=> R = R^-1); (d) catalog
      completeness by the norm argument (solutions are units, units are 4,
      catalog = 2 x 2 = 4, filtered to 2) — every count tied to its nest.
  G4  the mirror: conj = the sigma of this circle; semions swapped, classes
      fixed, norms 1.
  G5  the spin-statistics seed: theta = R, theta_f = -1, nu = +1 survivors;
      d = 1 for everything (NO order/Perron machinery needed — stated
      honestly); what Circle One machinery transfers.
  G6  Lean cost, calibrated on Circle One blocks RE-MEASURED FROM THE TREE
      (mod-11 386/47, order-d_tau 1140/102, coker 220/22), with the
      antisymmetrizer matrix sizes computed and the risky section flagged.

HOUSE RULES.  Every load-bearing check is exact (int / Fraction / symbolic
dict-polynomial / rational interval).  Floats appear ONLY in the quarantined
weld blocks that tie the exact objects back to the bench's float pathway
(marked FLOAT-WELD, never load-bearing) and in the seed-exact reproduction
of the bench's numeric search (FLOAT-REPRO — a reproduction of record).
At least one negative control per family.  One PASS/FAIL line per check;
any FAIL exits 1.

Standalone:  python3 c2_gift_certificates.py

CIRCLE TWO ROUND 1 REVISION (the builder, 2026-07-24), of the certified
original whose couriered hash was
db474c4c94f0aef8a47e6ed6c584c49ba505e30aeb1499424dfe056506023ea7:
  - WORKSHOP and LEAN are env-overridable (C2_WORKSHOP, C1_LEAN), so the
    instrument can run against Circle Two's tree from any layout: point
    C2_WORKSHOP at the directory holding the benches and C1_LEAN at the
    Circle One lean tree (needed only by the G6 calibrators).
  - G1h: the stale-docstring check `G1h_docstring_053_is_stale` is
    REPLACED by `G1h_docstring_carries_exact_4` — crop item #1 fixed the
    bench docstring (0.53 -> exactly 4), and per norm 13 the check that
    documented the discrepancy flips in the same stroke.
  Instrument-change protocol (norm 16): after revision the script was
  re-run on the fixed tree (pass, exit 0) and against a planted
  re-introduction of "0.53" (fail, exit 1).
"""

import itertools
import os
import subprocess
import sys
from fractions import Fraction

WORKSHOP = os.environ.get("C2_WORKSHOP", "/home/claude/workshop")
LEAN = os.environ.get("C1_LEAN", os.path.join(WORKSHOP, "lean"))
sys.path.insert(0, WORKSHOP)

FAILED = []
N_CHECK = 0


def check(name, ok, detail=""):
    global N_CHECK
    N_CHECK += 1
    line = ("PASS  " if ok else "FAIL  ") + name
    if detail:
        line += "  --  " + detail
    print(line)
    if not ok:
        FAILED.append(name)


def info(msg):
    print("      " + msg)


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


# ═════════════════════════════════════════════════════════════════════════
#  Shared exact machinery
# ═════════════════════════════════════════════════════════════════════════

# ---- sparse multivariate polynomials over Z (genuinely symbolic) ----------
class P:
    """Polynomial in n named variables, dict {exp-tuple: int coeff}."""

    def __init__(self, n, d=None):
        self.n = n
        self.d = {k: v for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def const(n, c):
        return P(n, {tuple([0] * n): c} if c else {})

    @staticmethod
    def var(n, i):
        e = [0] * n
        e[i] = 1
        return P(n, {tuple(e): 1})

    def __add__(s, o):
        d = dict(s.d)
        for k, v in o.d.items():
            d[k] = d.get(k, 0) + v
        return P(s.n, d)

    def __neg__(s):
        return P(s.n, {k: -v for k, v in s.d.items()})

    def __sub__(s, o):
        return s + (-o)

    def __mul__(s, o):
        d = {}
        for k1, v1 in s.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                d[k] = d.get(k, 0) + v1 * v2
        return P(s.n, d)

    def __eq__(s, o):
        return s.n == o.n and s.d == o.d

    def is_zero(s):
        return not s.d

    def subst_var(s, i, j):
        """Rename variable i to variable j (exponents merge)."""
        d = {}
        for k, v in s.d.items():
            k2 = list(k)
            k2[j] += k2[i]
            k2[i] = 0
            k2 = tuple(k2)
            d[k2] = d.get(k2, 0) + v
        return P(s.n, d)

    def __repr__(s):
        return f"P{s.d}"


# ---- Gaussian numbers: pairs (re, im), exact (int or Fraction) ------------
def gadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def gsub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def gmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def gconj(u):
    return (u[0], -u[1])


def gnorm(u):
    return u[0] * u[0] + u[1] * u[1]


def gpow(u, k):
    r = (1, 0)
    for _ in range(k):
        r = gmul(r, u)
    return r


G_ZERO, G_ONE, G_I = (0, 0), (1, 0), (0, 1)
G_MONE, G_MI = (-1, 0), (0, -1)


# ---- exact rank over Q (Fraction Gaussian elimination) --------------------
def rank_exact(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    m = len(A[0]) if n else 0
    rank = 0
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        rank += 1
    return rank


# ---- rational intervals (for the golden control's exact nonzero-ness) -----
class IV:
    """Closed rational interval [lo, hi], exact endpoint arithmetic."""

    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(s, o):
        return IV(s.lo + o.lo, s.hi + o.hi)

    def __sub__(s, o):
        return IV(s.lo - o.hi, s.hi - o.lo)

    def __mul__(s, o):
        c = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return IV(min(c), max(c))

    def mid(s):
        return float((s.lo + s.hi) / 2)


# ═════════════════════════════════════════════════════════════════════════
section("G0 — THE GROUND: the benches re-run green (subprocess, artifact-faithful)")
# ═════════════════════════════════════════════════════════════════════════

for bench, must in [
    ("symmetric_statistics.py",
     ["gauge classes F = [-1.0, 1.0]",
      "hexagon over F = +1: R = [(-1.0, 0.0), (1.0, 0.0)]",
      "flatland filter (R real): semions die",
      "antisymmetrizer ranks 1,3,6,10,15",
      "twist theta_f = R = -1"]),
    ("flatland.py", ["composite loop winds 2.0000 pi",
                     "R = R^-1 forces R^2 = 1"]),
    ("grammar_stone8.py", ["2 pi about any axis lifts to -I",
                           "nu = +1, all"]),
]:
    try:
        r = subprocess.run([sys.executable, bench], cwd=WORKSHOP,
                           capture_output=True, text=True, timeout=600)
        ok = r.returncode == 0 and all(m in r.stdout for m in must)
        check(f"G0_{bench}_green", ok,
              f"exit {r.returncode}; key lines present: "
              f"{[m in r.stdout for m in must]}")
    except Exception as e:
        check(f"G0_{bench}_green", False, repr(e))

# ═════════════════════════════════════════════════════════════════════════
section("G1a — PENTAGON FOR Z2 FUSION, exact: 16 instances, one forcing")
# ═════════════════════════════════════════════════════════════════════════
# The bench's F-symbol on Z2 fusion (a x b = a+b mod 2), gauge-fixed so the
# only free slot is F(1,1,1) =: f.  We recompute every pentagon instance the
# bench sums, as a POLYNOMIAL in f over Z (n=1 variable), using the bench's
# index plumbing verbatim (pent_residual_z2).

f_ = P.var(1, 0)
one_ = P.const(1, 1)
zero_ = P.const(1, 0)


def Fz2_poly(a, b, c, d, x, y):
    """Bench Fsym_z2 with a symbolic f."""
    if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
        return zero_
    return f_ if (a, b, c) == (1, 1, 1) else one_


pent_kinds = {"one_eq_one": [], "f_eq_f": [], "forcing": [], "other": []}
for a, b, c, dd in itertools.product((0, 1), repeat=4):
    x = (a + b) % 2
    y = (x + c) % 2
    t = (y + dd) % 2
    w = (c + dd) % 2
    v = (b + w) % 2
    u = (b + c) % 2
    lhs = (Fz2_poly(a, b, c, y, x, u) * Fz2_poly(a, u, dd, t, y, v)
           * Fz2_poly(b, c, dd, v, u, w))
    rhs = Fz2_poly(x, c, dd, t, y, w) * Fz2_poly(a, b, w, t, x, v)
    if lhs == rhs:
        pent_kinds["f_eq_f" if lhs == f_ else
                   ("one_eq_one" if lhs == one_ else "other")].append((a, b, c, dd))
    elif lhs == f_ * f_ and rhs == one_:
        pent_kinds["forcing"].append((a, b, c, dd))
    else:
        pent_kinds["other"].append((a, b, c, dd))

check("G1a_pentagon_16_instances_classified",
      (len(pent_kinds["one_eq_one"]), len(pent_kinds["f_eq_f"]),
       len(pent_kinds["forcing"]), len(pent_kinds["other"])) == (11, 4, 1, 0),
      "nest 16 = 2^4 label assignments (a,b,c,d): 11 instances read 1=1, "
      "4 read f=f, exactly ONE forces — no admissibility zeros on the path")
check("G1a_forcing_instance_is_1111_f2_eq_1",
      pent_kinds["forcing"] == [(1, 1, 1, 1)],
      "the single forcing instance is (a,b,c,d)=(1,1,1,1): lhs=f^2, rhs=1; "
      "PENTAGON FOR Z2 <=> f^2 = 1, over ANY commutative ring "
      "(the other 15 are ring identities)")

# the bench residual, reimplemented EXACTLY (Fractions), against (f^2-1)^2
def pent_residual_exact(f):
    """Bench pent_residual_z2 verbatim, Fraction arithmetic, |x|^2 = x^2."""
    def F(a, b, c, d, x, y):
        if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
            return Fraction(0)
        return f if (a, b, c) == (1, 1, 1) else Fraction(1)
    total = Fraction(0)
    for a, b, c, dd in itertools.product((0, 1), repeat=4):
        x = (a + b) % 2
        y = (x + c) % 2
        t = (y + dd) % 2
        w = (c + dd) % 2
        v = (b + w) % 2
        u = (b + c) % 2
        lhs = F(a, b, c, y, x, u) * F(a, u, dd, t, y, v) * F(b, c, dd, v, u, w)
        rhs = F(x, c, dd, t, y, w) * F(a, b, w, t, x, v)
        total += (lhs - rhs) ** 2
    return total


pts = [Fraction(p) for p in (2, -3, 1, -1, 0)] + [Fraction(1, 2), Fraction(5, 3)]
check("G1a_bench_residual_IS_(f2-1)^2",
      all(pent_residual_exact(f) == (f * f - 1) ** 2 for f in pts),
      "bench pent_residual_z2 reimplemented in Fractions equals (f^2-1)^2 "
      "at 7 exact points incl. both roots — the search was hunting the "
      "roots of (f^2-1)^2, nothing else")
check("G1a_roots_pm1_and_controls",
      pent_residual_exact(Fraction(1)) == 0
      and pent_residual_exact(Fraction(-1)) == 0
      and pent_residual_exact(Fraction(2)) == 9
      and pent_residual_exact(Fraction(1, 2)) == Fraction(9, 16),
      "f=+1, f=-1 give residual 0 exactly; NEGATIVE CONTROLS: f=2 -> 9, "
      "f=1/2 -> 9/16, both nonzero exactly")

# wrong-F in Z[i]: f = i fails the pentagon (Gaussian-exact)
fi2 = gmul(G_I, G_I)
check("G1a_control_f_eq_i_fails_pentagon",
      fi2 == (-1, 0) and gsub(fi2, G_ONE) == (-2, 0),
      "NEGATIVE CONTROL (Gaussian): f=i has f^2-1 = -2-0i != 0 — a unit of "
      "Z[i] that still fails the pentagon; residual |f^2-1|^2 = 4")

# ═════════════════════════════════════════════════════════════════════════
section("G1b — THE SEARCH, reproduced seed-exactly and characterized exactly")
# ═════════════════════════════════════════════════════════════════════════
# FLOAT-REPRO block (quarantined): the bench 'solved by search' — 40
# Nelder-Mead restarts, starts ~ uniform[-2,2], seed 1001, accept residual
# < 1e-15, round to 6 dp.  We reproduce that exact search (same seed, same
# draw order) and state what it could ever find (exact: roots of (f^2-1)^2).

try:
    import numpy as np
    from scipy.optimize import minimize
    import symmetric_statistics as S

    demo_lines = []
    S.demonstrate(demo_lines.append)   # in-process green re-run (all asserts)
    check("G1b_inprocess_demonstrate_green", len(demo_lines) >= 15,
          f"{len(demo_lines)} say-lines, every bench assert passed in-process")

    r = np.random.default_rng(1001)    # fresh generator, bench's seed
    sols, conv = set(), 0
    for _ in range(40):
        x0 = r.uniform(-2, 2, size=1)
        res = minimize(lambda p: S.pent_residual_z2(p[0]), x0,
                       method="Nelder-Mead",
                       options={"xatol": 1e-13, "fatol": 1e-18})
        if res.fun < 1e-15:
            conv += 1
            sols.add(round(float(res.x[0]), 6))
    check("G1b_pentagon_search_reproduced",
          sols == {-1.0, 1.0},
          f"search space: f real, 40 restarts from uniform[-2,2] (seed 1001, "
          f"first 40 draws of the stream); {conv}/40 restarts converged "
          f"below 1e-15; solution set found = {sorted(sols)} — exactly the "
          "two exact roots, no third")
    catalog = {}
    for fval in (1.0, -1.0):
        found = set()
        for _ in range(40):
            x0 = r.uniform(-2, 2, size=2)
            res = minimize(lambda p: S.hex_residual_z2(fval, p[0] + 1j * p[1]),
                           x0, method="Nelder-Mead",
                           options={"xatol": 1e-13, "fatol": 1e-18})
            if res.fun < 1e-15:
                found.add((round(float(res.x[0]), 6), round(float(res.x[1]), 6)))
        catalog[fval] = sorted(found)
    check("G1b_hexagon_searches_reproduced",
          catalog[1.0] == [(-1.0, 0.0), (1.0, 0.0)]
          and catalog[-1.0] == [(0.0, -1.0), (0.0, 1.0)],
          f"over F=+1: R = {catalog[1.0]} (boson, fermion); over F=-1: "
          f"R = {catalog[-1.0]} (semion, anti-semion) — 40+40 restarts, "
          "R complex (2 real params), same stream continuation as the bench")
    info("NOTE: the bench's pentagon search space is f REAL (1 parameter), "
         "not U(1); harmless — the exact certificate (G1a/G3a) covers any "
         "commutative ring, and 'exhaustive' is earned there, not by "
         "Nelder-Mead restarts.  Charter should say 'search + exact "
         "verification'.")
except Exception as e:
    check("G1b_search_reproduction", False, repr(e))

# ═════════════════════════════════════════════════════════════════════════
section("G1c — GAUGE: the (1,1,1) slot is invariant, so the two classes are real")
# ═════════════════════════════════════════════════════════════════════════
# Vertex gauge on normalized 3-cochains: eta : Z2 x Z2 -> units, acting by
# the coboundary  (d eta)(a,b,c) = eta(b,c) * eta(a+b,c)^-1 * eta(a,b+c)
# * eta(a,b)^-1.  Symbolically (4 variables n00,n01,n10,n11, denominators
# cleared):

nv = 4
n00, n01, n10, n11 = (P.var(nv, i) for i in range(nv))
eta = {(0, 0): n00, (0, 1): n01, (1, 0): n10, (1, 1): n11}


def deta_frac(a, b, c):
    """(d eta)(a,b,c) as (numerator, denominator) polynomial pair."""
    num = eta[(b, c)] * eta[(a, (b + c) % 2)]
    den = eta[((a + b) % 2, c)] * eta[(a, b)]
    return num, den


num111, den111 = deta_frac(1, 1, 1)
check("G1c_slot_moves_by_n10_over_n01",
      num111 == n11 * n10 and den111 == n01 * n11,
      "(d eta)(1,1,1) = [eta11*eta10]/[eta01*eta11] = eta10/eta01 "
      "symbolically — the raw gauge motion of the F(1,1,1) slot")

# normalization-preserving gauges: (d eta) = 1 at every zero-containing slot
conds = []
for a, b, c in itertools.product((0, 1), repeat=3):
    if (a, b, c) == (1, 1, 1):
        continue
    num, den = deta_frac(a, b, c)
    conds.append(((a, b, c), num, den))
# the conditions num = den, reduced: check they force n10 = n01 = n00
forces = {(1, 0, 0): (n00, n10), (0, 0, 1): (n01, n00),
          (1, 1, 0): (n10, n00), (0, 1, 1): (n00, n01),
          (1, 0, 1): (n01, n10)}
red_ok = True
for (abc, num, den) in conds:
    if abc in forces:
        x, y = forces[abc]
        # num = den  <=>  x = y after cancelling the common factor:
        # verify num * y == den * x  (cleared form of num/den = x/y... both
        # orders checked to be safe)
        red_ok &= (num * y == den * x)
    else:
        red_ok &= (num == den)  # identically 1
check("G1c_slice_preserving_gauges_characterized",
      red_ok,
      "the 7 zero-slot conditions reduce, symbolically, to "
      "n00 = n01 = n10 (n11 FREE); 2 of the 7 are automatic")
# under those conditions the slot motion n10/n01 = 1: substitute n01 -> n10
# (vars: 0=n00, 1=n01, 2=n10, 3=n11) in the cleared fraction and compare
check("G1c_slot_invariant_under_slice_gauges",
      num111.subst_var(1, 2) == den111.subst_var(1, 2)
      and num111 != den111,
      "with n01 = n10 the motion eta10/eta01 = 1: F(1,1,1) is a gauge "
      "INVARIANT of the normalized slice (and n11, the one free vertex "
      "gauge, moves nothing) => F=+1 and F=-1 are genuinely distinct "
      "classes; with G1a: exactly two.  [The remaining step to the full "
      "H^3(Z2,U(1)) = Z2 sentence — 'every class has a normalized "
      "representative' — is standard but NOT bench-certified: flag for "
      "charter wording.]")

# ═════════════════════════════════════════════════════════════════════════
section("G1d — HEXAGON FOR Z2, exact: 8 instances, one forcing, R^2 = F")
# ═════════════════════════════════════════════════════════════════════════
# Polynomials in (f, R): n=2 variables.
nfr = 2
fF = P.var(nfr, 0)
RR = P.var(nfr, 1)
one2 = P.const(nfr, 1)
zero2 = P.const(nfr, 0)


def Fz2_fr(a, b, c, d, x, y):
    if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
        return zero2
    return fF if (a, b, c) == (1, 1, 1) else one2


def Rs_fr(x, y):
    return RR if (x, y) == (1, 1) else one2


hex_kinds = {"one_eq_one": [], "R_eq_R": [], "forcing": [], "other": []}
n_loop = 0
for a, b, c, d in itertools.product((0, 1), repeat=4):
    n_loop += 1
    e = (a + b) % 2
    z = (a + c) % 2
    if d != (e + c) % 2 or d != (z + b) % 2:
        continue
    g = (b + c) % 2
    lhs = Rs_fr(e, c) * Fz2_fr(c, a, b, d, z, e)
    rhs = (Fz2_fr(a, b, c, d, e, g) * Rs_fr(b, c)
           * Fz2_fr(a, c, b, d, z, g) * Rs_fr(a, c))
    if lhs == rhs:
        hex_kinds["R_eq_R" if lhs == RR else
                  ("one_eq_one" if lhs == one2 else "other")].append((a, b, c))
    elif lhs == fF and rhs == fF * fF * RR * RR:
        hex_kinds["forcing"].append((a, b, c))
    else:
        hex_kinds["other"].append((a, b, c))

check("G1d_hexagon_8_instances_classified",
      n_loop == 16
      and (len(hex_kinds["one_eq_one"]), len(hex_kinds["R_eq_R"]),
           len(hex_kinds["forcing"]), len(hex_kinds["other"])) == (5, 2, 1, 0),
      "nest: 16 loop assignments, 8 admissible (d = a+b+c forced), of which "
      "5 read 1=1, 2 read R=R, exactly ONE forces")
check("G1d_forcing_instance_is_111",
      hex_kinds["forcing"] == [(1, 1, 1)],
      "the single forcing instance is (a,b,c)=(1,1,1): f = f^2 R^2; with "
      "the pentagon (f^2=1) this is exactly R^2 = f: "
      "R^2 = +1 over F=+1, R^2 = -1 over F=-1 — the bench's four particles")

# f = f^2 R^2  simplifies to R^2 = f modulo f^2 = 1: symbolic witness
lhs_forced = fF * fF * RR * RR - fF
witness = (RR * RR - fF) + (RR * RR) * (fF * fF - one2)
check("G1d_reduction_identity",
      lhs_forced == witness,
      "f^2 R^2 - f == (R^2 - f) + R^2 (f^2 - 1) as polynomials over Z — "
      "so pentagon (f^2=1) + hexagon (f^2R^2=f) <=> R^2 = f, in ANY "
      "commutative ring")


# bench hex residual, exact Gaussian-Fraction reimplementation
def hex_residual_exact(f, R):
    """Bench hex_residual_z2 verbatim; f, R Gaussian pairs; |w|^2 exact."""
    def F(a, b, c, d, x, y):
        if x != (a + b) % 2 or y != (b + c) % 2 or d != (a + b + c) % 2:
            return (Fraction(0), Fraction(0))
        return f if (a, b, c) == (1, 1, 1) else (Fraction(1), Fraction(0))

    def Rs(x, y):
        return R if (x, y) == (1, 1) else (Fraction(1), Fraction(0))

    total = Fraction(0)
    for a, b, c, d in itertools.product((0, 1), repeat=4):
        e = (a + b) % 2
        z = (a + c) % 2
        if d != (e + c) % 2 or d != (z + b) % 2:
            continue
        g = (b + c) % 2
        lhs = gmul(Rs(e, c), F(c, a, b, d, z, e))
        rhs = gmul(gmul(F(a, b, c, d, e, g), Rs(b, c)),
                   gmul(F(a, c, b, d, z, g), Rs(a, c)))
        dif = gsub(lhs, rhs)
        total += gnorm(dif)
    return total


gpts = [((Fraction(1), Fraction(0)), (Fraction(1, 2), Fraction(1, 3))),
        ((Fraction(-1), Fraction(0)), (Fraction(2), Fraction(-1))),
        ((Fraction(3), Fraction(2)), (Fraction(0), Fraction(1))),
        ((Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1)))]
ok_weld = True
for f, R in gpts:
    lhs_val = gsub(gmul(gmul(f, f), gmul(R, R)), f)      # f^2R^2 - f
    ok_weld &= (hex_residual_exact(f, R) == gnorm(lhs_val))
check("G1d_bench_residual_IS_|f2R2-f|^2", ok_weld,
      "bench hex_residual_z2 reimplemented exactly equals |f^2R^2 - f|^2 at "
      "4 Gaussian-rational points (incl. the semion, residual 0)")

# the four catalog entries satisfy BOTH hexagons exactly; controls fail
catalog4 = [((1, 0), (1, 0), "boson"), ((1, 0), (-1, 0), "fermion"),
            ((-1, 0), (0, 1), "semion"), ((-1, 0), (0, -1), "anti-semion")]
both_ok = True
for f, R, name in catalog4:
    h1 = gsub(gmul(gmul(f, f), gmul(R, R)), f)           # R-hexagon
    Rinv = gconj(R)                                      # unit => R^-1 = conj
    h2 = gsub(gmul(gmul(f, f), gmul(Rinv, Rinv)), f)     # R^-1-hexagon
    both_ok &= (h1 == G_ZERO and h2 == G_ZERO and gmul(R, Rinv) == G_ONE)
check("G1d_catalog4_satisfies_BOTH_hexagons", both_ok,
      "boson/fermion/semion/anti-semion each satisfy the R-hexagon AND the "
      "R^-1-hexagon exactly (bench imposes only one; on units the second "
      "is equivalent — the charter may impose both at no extra root cost)")
check("G1d_controls_wrong_R_per_class",
      gsub(gmul(gmul(G_ONE, G_ONE), gmul(G_I, G_I)), G_ONE) == (-2, 0)
      and gsub(gmul(gmul(G_MONE, G_MONE), gmul(G_ONE, G_ONE)), G_MONE) == (2, 0),
      "NEGATIVE CONTROLS: R=i over F=+1 leaves f^2R^2-f = -2 != 0; R=1 over "
      "F=-1 leaves +2 != 0 — the classes do not accept each other's particles")

# ═════════════════════════════════════════════════════════════════════════
section("G1e — THE FLATLAND FILTER, exact: semions die, two survive")
# ═════════════════════════════════════════════════════════════════════════

survivors = [(f, R, n) for f, R, n in catalog4 if gconj(R) == R]
check("G1e_filter_kills_semions",
      [n for _, _, n in survivors] == ["boson", "fermion"]
      and gconj(G_I) == G_MI and gconj(G_MI) == G_I,
      "conj(R) = R (i -> -i) holds for R = +1, -1 and fails for R = +i, -i: "
      "survivors exactly {boson, fermion}; nest 2 of 4")
check("G1e_control_semion_fails_filter",
      gconj(G_I) != G_I,
      "NEGATIVE CONTROL: R = +i has conj(R) = -i != R — the semion is "
      "Galois-moved, not Galois-fixed; it cannot pass a reality filter")

# ═════════════════════════════════════════════════════════════════════════
section("G1f — EXCLUSION AS RANK, exact integers: 1, 3, 6, 10, 15")
# ═════════════════════════════════════════════════════════════════════════
# Bench: A = (I - SWAP)/2 on C^m (x) C^m, float SVD rank.  Here: M = I - S
# INTEGER matrix (M = 2A, same rank), exact Fraction elimination.

ranks, sranks, msizes = [], [], []
proj_ok, trace_ok, comp_ok = True, True, True
for m in range(2, 7):
    n = m * m
    msizes.append(n)
    Mm = [[0] * n for _ in range(n)]
    Sm = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            Mm[i * m + j][i * m + j] += 1
            Mm[i * m + j][j * m + i] -= 1
            Sm[i * m + j][j * m + i] = 1
    # exact rank
    ranks.append(rank_exact(Mm))
    Pm = [[Mm[i][j] + 2 * Sm[i][j] for j in range(n)] for i in range(n)]  # I + S
    sranks.append(rank_exact(Pm))
    # M^2 = 2M exactly (integer matmul)
    M2 = [[sum(Mm[i][k] * Mm[k][j] for k in range(n)) for j in range(n)]
          for i in range(n)]
    proj_ok &= all(M2[i][j] == 2 * Mm[i][j] for i in range(n) for j in range(n))
    trace_ok &= (sum(Mm[i][i] for i in range(n)) == m * m - m)
    # (I-S) + (I+S) = 2I and (I-S)(I+S) = 0
    MP = [[sum(Mm[i][k] * Pm[k][j] for k in range(n)) for j in range(n)]
          for i in range(n)]
    comp_ok &= all(MP[i][j] == 0 for i in range(n) for j in range(n))
    comp_ok &= all(Mm[i][j] + Pm[i][j] == (2 if i == j else 0)
                   for i in range(n) for j in range(n))

check("G1f_antisymmetrizer_ranks_exact",
      ranks == [1, 3, 6, 10, 15],
      f"rank_Q(I - SWAP) on Z^(m^2) for m=2..6 = {ranks} = m(m-1)/2, the "
      f"triangular numbers; matrix sizes {msizes} = m^2; EXACT Fraction "
      "elimination, no float, no tolerance (bench used SVD tol 1e-10)")
check("G1f_idempotent_certificate",
      proj_ok and trace_ok and ranks == [(m * m - m) // 2 for m in range(2, 7)],
      "M = I-S satisfies M^2 = 2M and tr M = m^2 - m exactly; rank = tr/2 — "
      "the Lean-friendly certificate: P = M/2 idempotent, rank = trace")
check("G1f_symmetrizer_control_and_complement",
      sranks == [3, 6, 10, 15, 21] and comp_ok
      and all(r + s == n for r, s, n in zip(ranks, sranks, msizes)),
      f"NEGATIVE CONTROL: symmetrizer ranks {sranks} = m(m+1)/2 (NOT the "
      "fermionic census); (I-S)(I+S) = 0 and (I-S)+(I+S) = 2I exactly; "
      "ranks sum to m^2 — the two-sided split is complete")

# double occupation: symbolic annihilation + boson control
nx = 4
xs = [P.var(nx, i) for i in range(nx)]
anti_sym_zero = all((xs[i] * xs[j] - xs[j] * xs[i]).is_zero()
                    for i in range(nx) for j in range(nx))
check("G1f_pauli_kill_symbolic",
      anti_sym_zero,
      "M(psi x psi) has components psi_i psi_j - psi_j psi_i = 0 "
      "IDENTICALLY (symbolic, 4 variables): the antisymmetrized double "
      "occupation vanishes for every psi, not just sampled ones")
psi = [(Fraction(3, 2), Fraction(-1, 3)), (Fraction(2), Fraction(5, 7)),
       (Fraction(-4, 5), Fraction(1)), (Fraction(0), Fraction(-2, 9))]
pp = [gmul(psi[i], psi[j]) for i in range(4) for j in range(4)]
anti = [gsub(pp[i * 4 + j], pp[j * 4 + i]) for i in range(4) for j in range(4)]
symm = [gadd(pp[i * 4 + j], pp[j * 4 + i]) for i in range(4) for j in range(4)]
check("G1f_pauli_kill_exact_gaussian_psi",
      all(x == G_ZERO for x in anti) and any(x != G_ZERO for x in symm),
      "exact Gaussian-rational psi: antisymmetrized psi x psi = 0 EXACTLY "
      "(bench: 3.2e-16 float); NEGATIVE CONTROL: symmetrized psi x psi != 0 "
      "— bosons do NOT exclude; the teeth belong to the -1 alone")

# FLOAT-WELD: numpy rank agrees with exact rank (not load-bearing)
try:
    wr = []
    for m in range(2, 7):
        A = np.zeros((m * m, m * m))
        for i in range(m):
            for j in range(m):
                A[i * m + j, i * m + j] += 0.5
                A[i * m + j, j * m + i] -= 0.5
        wr.append(int(np.linalg.matrix_rank(A, tol=1e-10)))
    check("G1f_FLOATWELD_bench_rank_path", wr == ranks,
          f"bench's np.linalg.matrix_rank pathway returns {wr} — agrees with "
          "the exact ranks (weld only; the certificate is the exact one)")
except Exception as e:
    check("G1f_FLOATWELD_bench_rank_path", False, repr(e))

# ═════════════════════════════════════════════════════════════════════════
section("G1g — TWIST AND FROBENIUS-SCHUR, exact integers")
# ═════════════════════════════════════════════════════════════════════════

theta = {"boson": G_ONE, "fermion": G_MONE, "semion": G_I, "anti-semion": G_MI}
Rsym = {"boson": G_ONE, "fermion": G_MONE, "semion": G_I, "anti-semion": G_MI}
check("G1g_twist_eq_R_theta_f_minus1",
      all(theta[n] == Rsym[n] for n in theta) and theta["fermion"] == G_MONE,
      "theta = R for every Z2 particle (abelian: theta_a = R(a,a)); "
      "theta_fermion = -1 exactly — the sign that builds shelves")
nu_Rtheta = {n: gmul(Rsym[n], theta[n]) for n in theta}
nu_Rconj = {n: gmul(Rsym[n], gconj(theta[n])) for n in theta}
check("G1g_nu_survivors_plus1",
      nu_Rtheta["boson"] == G_ONE and nu_Rtheta["fermion"] == G_ONE
      and nu_Rconj["boson"] == G_ONE and nu_Rconj["fermion"] == G_ONE,
      "nu = R*theta = +1 for BOTH survivors (boson 1*1, fermion (-1)(-1)); "
      "the R*conj(theta) ledger agrees on the survivors (theta real)")
check("G1g_convention_fork_on_semions_FLAGGED",
      nu_Rtheta["semion"] == G_MONE and nu_Rconj["semion"] == G_ONE,
      "DISCREPANCY FLAG: on semions the two ledgers diverge: R*theta = -1 "
      "(the true Frobenius-Schur indicator — SU(2)_1's spin-1/2 is "
      "pseudo-real) vs stone8's R*conj(theta) = +1 (spin-statistics "
      "co-sign, identically +1 whenever theta = R).  Both benches are "
      "internally consistent; the CHARTER must name the two ledgers apart "
      "off the real locus")

# ═════════════════════════════════════════════════════════════════════════
section("G1h — THE GOLDEN CONTROL, exact: no symmetric braiding on Fibonacci")
# ═════════════════════════════════════════════════════════════════════════
# Bench claim (1): impose R in {+1,-1}^2 on golden fusion; all four fail the
# hexagon.  Exact home: Q[s]/(s^4 - s^2 - 1), s = sqrt(phi); F entries
# 1/phi = s^2-1, 1/sqrt(phi) = s^3-s, -1/phi = 1-s^2 — all in the ring.

def sred(c):
    """Reduce coefficient list (deg <= 6) mod s^4 = s^2 + 1."""
    c = list(c) + [Fraction(0)] * (7 - len(c))
    for e in range(6, 3, -1):
        v = c[e]
        if v:
            c[e] = Fraction(0)
            c[e - 2] += v
            c[e - 4] += v
    return tuple(c[:4])


def smul(a, b):
    c = [Fraction(0)] * 7
    for i in range(4):
        for j in range(4):
            c[i + j] += a[i] * b[j]
    return sred(c)


def sadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def ssub(a, b):
    return tuple(x - y for x, y in zip(a, b))


S_ZERO = (Fraction(0),) * 4
S_ONE = sred([Fraction(1)])
INV_PHI = (Fraction(-1), Fraction(0), Fraction(1), Fraction(0))    # s^2 - 1
INV_SQPHI = (Fraction(0), Fraction(-1), Fraction(0), Fraction(1))  # s^3 - s
S_S = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
check("G1h_ring_anchors",
      smul(S_S, INV_SQPHI) == S_ONE
      and smul(sadd(INV_PHI, S_ONE), INV_PHI) == S_ONE
      and smul(S_S, S_S) == sadd(INV_PHI, S_ONE),
      "in Q[s]/(s^4-s^2-1): s*(s^3-s) = 1 (so 1/sqrt(phi) = s^3-s), "
      "phi*(1/phi) = 1 with phi = s^2, 1/phi = s^2-1 — the F-matrix entries "
      "are ring elements, exactly")

FGx = [[INV_PHI, INV_SQPHI], [INV_SQPHI, tuple(-x for x in INV_PHI)]]
ONEf, TAUf = 0, 1


def fuse_fib(a, b):
    if a == ONEf:
        return (b,)
    if b == ONEf:
        return (a,)
    return (ONEf, TAUf)


def Fsym_fib_exact(a, b, c, d, x, y):
    if x not in fuse_fib(a, b) or d not in fuse_fib(x, c):
        return S_ZERO
    if y not in fuse_fib(b, c) or d not in fuse_fib(a, y):
        return S_ZERO
    if ONEf in (a, b, c):
        return S_ONE
    if d == ONEf:
        return S_ONE if (x, y) == (TAUf, TAUf) else S_ZERO
    return FGx[x][y]


def hex_residual_fib_exact(r1, rt):
    """Bench hex_residual_fib verbatim; r1, rt in {+1,-1} (rational)."""
    def Rx(x, y, c):
        if x == ONEf or y == ONEf:
            return S_ONE
        return sred([Fraction(r1 if c == ONEf else rt)])
    total = S_ZERO
    for a, b, c, d in itertools.product((ONEf, TAUf), repeat=4):
        for e in fuse_fib(a, b):
            if d not in fuse_fib(e, c):
                continue
            for z in fuse_fib(a, c):
                if d not in fuse_fib(z, b):
                    continue
                lhs = smul(Rx(e, c, d), Fsym_fib_exact(c, a, b, d, z, e))
                rhs = S_ZERO
                for g in fuse_fib(b, c):
                    rhs = sadd(rhs, smul(smul(Fsym_fib_exact(a, b, c, d, e, g),
                                              Rx(b, c, g)),
                                         smul(Fsym_fib_exact(a, c, b, d, z, g),
                                              Rx(a, c, z))))
                dif = ssub(lhs, rhs)
                total = sadd(total, smul(dif, dif))   # real => |.|^2 = (.)^2
    return total


# pin s = sqrt(phi) in a rational interval by exact bisection of s^4-s^2-1
def pchar(x):
    return x ** 4 - x ** 2 - 1


lo, hi = Fraction(127, 100), Fraction(128, 100)
assert pchar(lo) < 0 < pchar(hi)
for _ in range(60):
    mid = (lo + hi) / 2
    if pchar(mid) < 0:
        lo = mid
    else:
        hi = mid
sIV = IV(lo, hi)
powsIV = [IV(1), sIV, sIV * sIV, sIV * sIV * sIV]


def elemIV(e):
    t = IV(0)
    for c, pw in zip(e, powsIV):
        t = t + IV(c) * pw
    return t


res_exact = {}
for r1 in (1, -1):
    for rt in (1, -1):
        res_exact[(r1, rt)] = hex_residual_fib_exact(r1, rt)
all_nonzero = all(elemIV(v).lo > 0 for v in res_exact.values())
min_pair = min(res_exact, key=lambda k: elemIV(res_exact[k]).mid())
min_val = res_exact[min_pair]
check("G1h_all_four_candidates_fail_EXACTLY",
      all_nonzero,
      "hexagon residual for (r1,rt) in {+1,-1}^2, computed in "
      "Q[s]/(s^4-s^2-1): all four are > 0 by rational INTERVAL certificate "
      "(s pinned to width < 1e-17 by exact bisection) — no symmetric "
      "braiding exists on golden fusion; the exile is exact, not 1e-9")
check("G1h_min_residual_exceeds_bench_gate",
      elemIV(min_val).lo > Fraction(1, 2),
      f"minimum over the four = candidate {min_pair}, exact value "
      f"{tuple(str(c) for c in min_val)} (coords in basis 1,s,s^2,s^3) "
      f"~ {elemIV(min_val).mid():.6f} > 1/2, the bench's assert gate")
is_exactly_4 = (min_val == (Fraction(4), Fraction(0), Fraction(0), Fraction(0)))
info(f"exact minimum residual = {tuple(str(c) for c in min_val)}"
     + ("  — EXACTLY the integer 4" if is_exactly_4 else
        f"  ~ {elemIV(min_val).mid():.9f}"))
info("CROP ITEM #1 (fixed, Circle Two round 1): an earlier docstring "
     "said 'minimum residual 0.53'; the exact minimum is the integer 4 "
     "and the docstring now says so.  The check below gates the fix.")
# FLOAT-WELD: exact residuals match the bench float function
try:
    wok = all(abs(elemIV(res_exact[k]).mid()
                  - float(S.hex_residual_fib(k[0], k[1]))) < 1e-6
              for k in res_exact)
    check("G1h_FLOATWELD_bench_fib_residuals", wok,
          "the four exact residuals match the bench's float "
          "hex_residual_fib to < 1e-6 (weld only)")
except Exception as e:
    check("G1h_FLOATWELD_bench_fib_residuals", False, repr(e))
bench_txt = open(os.path.join(WORKSHOP, "symmetric_statistics.py")).read()
check("G1h_docstring_carries_exact_4",
      is_exactly_4 and "0.53" not in bench_txt
      and "exactly the integer 4" in bench_txt,
      "CROP ITEM #1 gate: the exact minimum IS the integer 4 (interval-"
      "certified above), the bench docstring now carries it, and the stale "
      "'0.53' is gone.  Sites enumerated per norm 13: the docstring, "
      "charter flag 1, this check, and the round-1 letter")

# ═════════════════════════════════════════════════════════════════════════
section("G2 — THE RING Z[i]: symbolic laws, Brahmagupta, the mod-4 descent")
# ═════════════════════════════════════════════════════════════════════════
# Z[i] as integer pairs (a,b) = a + b*i, (a,b)(c,d) = (ac-bd, ad+bc).
# Symbolic layer: 6 variables a,b,c,d,e,g for three generic elements.

n6 = 6
va, vb, vc, vd, ve, vg = (P.var(n6, i) for i in range(n6))
U = (va, vb)
V = (vc, vd)
W = (ve, vg)


def pgmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def pgadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def pgeq(u, v):
    return (u[0] - v[0]).is_zero() and (u[1] - v[1]).is_zero()


check("G2_i_squared_is_minus_one",
      gmul(G_I, G_I) == (-1, 0),
      "(0,1)^2 = (-1,0): i^2 = -1 in the pair encoding — the ring's one law")
check("G2_ring_laws_symbolic",
      pgeq(pgmul(pgmul(U, V), W), pgmul(U, pgmul(V, W)))
      and pgeq(pgmul(U, V), pgmul(V, U))
      and pgeq(pgmul(U, pgadd(V, W)), pgadd(pgmul(U, V), pgmul(U, W))),
      "mul assoc, mul comm, distributivity: POLYNOMIAL IDENTITIES in 6 "
      "variables over Z — true in every commutative ring, no spot checks")
NU = U[0] * U[0] + U[1] * U[1]
NV = V[0] * V[0] + V[1] * V[1]
PRODN = pgmul(U, V)
check("G2_brahmagupta_fibonacci_symbolic",
      (NU * NV - (PRODN[0] * PRODN[0] + PRODN[1] * PRODN[1])).is_zero(),
      "(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2 as a polynomial identity "
      "— the norm N(a+bi) = a^2+b^2 is multiplicative, symbolically")
CU = (U[0], -U[1])
CV = (V[0], -V[1])
check("G2_conj_is_a_ring_hom_symbolic",
      pgeq(pgmul(CU, CV), (pgmul(U, V)[0], -pgmul(U, V)[1]))
      and pgeq(pgadd(CU, CV), (pgadd(U, V)[0], -pgadd(U, V)[1])),
      "conj(uv) = conj(u)conj(v) and conj(u+v) = conj(u)+conj(v) "
      "symbolically; conj(conj(u)) = u trivially — the sigma of Circle Two")
ZC = pgmul(U, CU)
check("G2_z_times_conj_is_norm_symbolic",
      (ZC[0] - NU).is_zero() and ZC[1].is_zero(),
      "z * conj(z) = (N(z), 0) symbolically — the norm as a ring element, "
      "the engine of the domain proof")

# ---- THE DESCENT CERTIFICATE ---------------------------------------------
check("G2_squares_mod_4",
      sorted({(x * x) % 4 for x in range(4)}) == [0, 1],
      "nest 4 = |Z/4|: squares mod 4 are exactly {0, 1} "
      "(0,2 -> 0; 1,3 -> 1)")
hits = [(a, b) for a in range(4) for b in range(4) if (a * a + b * b) % 4 == 0]
check("G2_16_case_decide",
      hits == [(0, 0), (0, 2), (2, 0), (2, 2)]
      and all((a % 2, b % 2) == (0, 0) for a, b in hits),
      "nest 16 = |(Z/4)^2|: N = a^2+b^2 = 0 mod 4 for exactly 4 of 16 "
      "residue pairs — precisely those with a, b BOTH EVEN; 12 fail.  "
      "This is Circle One's 16-case 2-adic decide, one prime, SIMPLER "
      "(2 coordinates, not 4)")
check("G2_control_mod2_insufficient",
      (1 * 1 + 1 * 1) % 2 == 0 and (1 % 2, 1 % 2) != (0, 0),
      "NEGATIVE CONTROL: the mod-2 analogue FAILS — (1,1) has N = 2 = 0 "
      "mod 2 with both coordinates odd; the modulus 4 is load-bearing "
      "(2 ramifies in Z[i]: 2 = -i(1+i)^2)")
desc_ok = all((abs(a // 2) + abs(b // 2) < abs(a) + abs(b))
              for a in range(-20, 21, 2) for b in range(-20, 21, 2)
              if (a, b) != (0, 0))
check("G2_descent_step_strictly_decreases",
      desc_ok,
      "for (a,b) both even, nonzero: |a/2|+|b/2| < |a|+|b| (box |a|,|b| "
      "<= 20 exhaustive; generally halving a nonzero even integer strictly "
      "shrinks |.|) — the strong-induction measure decreases")
check("G2_norm_zero_forces_zero",
      all((a * a + b * b != 0) for a in range(-30, 31) for b in range(-30, 31)
          if (a, b) != (0, 0)),
      "N(z) = 0 => z = 0 (box |a|,|b| <= 30 exhaustive; the descent gives "
      "it unboundedly: N=0 => N=0 mod 4 => both even => halve, repeat).  "
      "NOTE HONESTLY: Lean's Int order gives a one-line alternative "
      "(a^2 >= 0, sum zero => each zero); the descent is the "
      "pattern-preserving route and stays order-free like Circle One")
P0 = P.const(n6, 0)
check("G2_torsion_free",
      all(not (n * a == 0 and a != 0)
          for n in range(-9, 10) if n != 0 for a in range(-9, 10))
      and pgeq(pgmul((va, P0), (vc, vd)), (va * vc, va * vd)),
      "n * w = 0 with n != 0 integer => w = 0, coordinatewise (Z is a "
      "domain — Lean core Int.mul_eq_zero; box |n|,|a| <= 9 witnessed); "
      "and the scalar action IS multiplication by (n,0): "
      "(n,0)*(c,d) = (nc, nd) symbolically")
# domain, demonstrated on a box + the chain
box = range(-6, 7)
no_zd = True
elems = [(a, b) for a in box for b in box]
nz = [z for z in elems if z != (0, 0)]
for z in nz:
    for w in nz:
        if gmul(z, w) == (0, 0):
            no_zd = False
check("G2_no_zero_divisors_box",
      no_zd,
      "nest 168^2 ordered pairs of nonzero elements with |coords| <= 6: "
      "no product vanishes.  THE CHAIN (each link certified above): "
      "z*w = 0 => conj(z)*z*w = 0 => (N(z),0)*w = 0 => N(z)*w_k = 0 with "
      "N(z) != 0 => w = 0.  Z[i] IS A DOMAIN — same shape as Circle One's "
      "2-adic descent, one prime instead of two")

# ═════════════════════════════════════════════════════════════════════════
section("G3 — EXACTLY-TWO, four designs, each count tied to its nest")
# ═════════════════════════════════════════════════════════════════════════

# (a) pentagon side ---------------------------------------------------------
f1 = P.var(1, 0)
check("G3a_factorization_symbolic",
      (f1 * f1 - P.const(1, 1)) == (f1 - P.const(1, 1)) * (f1 + P.const(1, 1)),
      "f^2 - 1 = (f-1)(f+1) as polynomials over Z — with G1a: pentagon "
      "<=> (f-1)(f+1) = 0; in a DOMAIN: f = +1 or f = -1.  EXACTLY TWO "
      "needs only (i) the 16-instance derivation (any comm ring), (ii) the "
      "domain property, (iii) 1 != -1 (char != 2; Z[i] has char 0)")
check("G3a_both_roots_land",
      gmul(G_ONE, G_ONE) == G_ONE and gmul(G_MONE, G_MONE) == G_ONE
      and G_ONE != G_MONE,
      "F = +1 and F = -1 both satisfy F^2 = 1 in Z[i], and they are "
      "distinct: at least two, and by the domain at most two — EXACTLY TWO "
      "pentagon classes")
z8 = [x for x in range(8) if (x * x) % 8 == 1]
check("G3a_control_Z8_four_roots",
      z8 == [1, 3, 5, 7],
      "NEGATIVE CONTROL (non-domain): in Z/8, f^2 = 1 has FOUR solutions "
      "{1,3,5,7} — exactly-two is a DOMAIN theorem, not arithmetic luck")

# (b) hexagon side ----------------------------------------------------------
def gpoly_mul(p, q):
    """Univariate polynomials with Gaussian coefficients (lists, low deg first)."""
    out = [G_ZERO] * (len(p) + len(q) - 1)
    for i, ci in enumerate(p):
        for j, cj in enumerate(q):
            out[i + j] = gadd(out[i + j], gmul(ci, cj))
    return out


R_minus_i = [G_MI, G_ONE]   # -i + R
R_plus_i = [G_I, G_ONE]     # +i + R
check("G3b_semion_factorization_over_Zi",
      gpoly_mul(R_minus_i, R_plus_i) == [G_ONE, G_ZERO, G_ONE],
      "(R - i)(R + i) = R^2 + 1 with GAUSSIAN coefficients, exactly — the "
      "F = -1 class's quadratic factors over Z[i] (it does NOT factor over "
      "Z, where R^2 = -1 has no root: next check); with the domain, "
      "R^2 = -1 => R = i or R = -i")
check("G3b_R2_eq_f_roots_exact",
      gmul(G_I, G_I) == G_MONE and gmul(G_MI, G_MI) == G_MONE
      and gmul(G_ONE, G_ONE) == G_ONE and gmul(G_MONE, G_MONE) == G_ONE
      and G_I != G_MI,
      "over F=+1: (+1)^2 = (-1)^2 = +1; over F=-1: (+i)^2 = (-i)^2 = -1; "
      "the two roots per class are distinct — at least two per class")
check("G3b_no_integer_semion",
      all(x * x != -1 for x in range(-50, 51)),
      "R^2 = -1 has no solution in Z (box exhaustive; generally x^2 >= 0): "
      "the semion class requires the imaginary unit — the ROOMY catalog "
      "over Z would be 2 classes x (2,0) particles")
zi5 = [(a, b) for a in range(5) for b in range(5)]


def g5mul(u, v):
    w = gmul(u, v)
    return (w[0] % 5, w[1] % 5)


sq1_5 = [z for z in zi5 if g5mul(z, z) == (1, 0)]
sqm1_5 = [z for z in zi5 if g5mul(z, z) == (4, 0)]
check("G3b_control_Zi_mod5_splits",
      g5mul((2, 1), (2, 4)) == (0, 0) and (2, 1) != (0, 0) and (2, 4) != (0, 0)
      and len(sq1_5) == 4 and len(sqm1_5) == 4
      and gmul((2, 1), (2, -1)) == (5, 0),
      "NEGATIVE CONTROL (the chartered one): (2+i)(2-i) = 5 exactly, so in "
      "Z[i]/5 the classes split — zero divisors exhibited, and "
      f"nest 25 = 5^2 elements: #sqrt(1) = {len(sq1_5)} = "
      f"{sorted(sq1_5)}, #sqrt(-1) = {len(sqm1_5)} = {sorted(sqm1_5)} — "
      "FOUR per class, exactly-two FAILS without the domain")

# (c) the filter as a Galois statement --------------------------------------
fix_defect = (CU[0] - U[0], CU[1] - U[1])
check("G3c_fixed_ring_is_Z_symbolic",
      fix_defect[0].is_zero() and fix_defect[1] == P.const(n6, -2) * vb
      and all(not (2 * b == 0 and b != 0) for b in range(-50, 51)),
      "conj(u) - u = (0, -2b) SYMBOLICALLY: conj-fixedness <=> 2b = 0 "
      "<=> b = 0 (torsion-freeness again, box witnessed): Fix(conj) = Z "
      "inside Z[i] — 'R real' IS 'R Galois-fixed', the same move as "
      "Circle One's sigma")
units4 = [G_ONE, G_MONE, G_I, G_MI]
inv_by_conj = all(gmul(u, gconj(u)) == G_ONE for u in units4)
equiv_ok = all((gconj(u) == u) == (gmul(u, u) == G_ONE) for u in units4)
check("G3c_on_units_filter_equals_flatland_edict",
      inv_by_conj and equiv_ok,
      "for every unit u: u * conj(u) = N(u) = 1, so u^-1 = conj(u); hence "
      "R = R^-1 (flatland's edict, R^2 = 1) <=> conj(R) = R (the Galois "
      "filter) — checked on all 4 units; the geometric filter and the "
      "Galois filter are ONE statement on the unit group")
check("G3c_conj_transports_solutions",
      all(gmul(gconj(R), gconj(R)) == gconj(f) and gconj(f) == f
          for f, R, _ in catalog4),
      "conj is a ring hom fixing F (= +-1 real), so R^2 = F => "
      "conj(R)^2 = F: conjugation permutes each hexagon fiber — verified "
      "on all four catalog entries")

# (d) catalog completeness by the norm argument -----------------------------
sols_sq = {}
for target, tname in [(G_ONE, "+1"), (G_MONE, "-1")]:
    sols_sq[tname] = [u for u in units4 if gmul(u, u) == target]
norms_units = [gnorm(u) for u in units4]
unit_enum = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)
             if a * a + b * b == 1]
check("G3d_units_are_exactly_four",
      sorted(unit_enum) == sorted([(-1, 0), (0, -1), (0, 1), (1, 0)])
      and norms_units == [1, 1, 1, 1]
      and all(a * a > 1 for a in range(-30, 31) if abs(a) >= 2),
      "N(u) = 1 <=> a^2+b^2 = 1; |a| >= 2 => a^2 >= 4 > 1 (box witness), "
      "so |a|,|b| <= 1 and the enumeration is COMPLETE: units of Z[i] = "
      "{1, -1, i, -i}, four, each of norm 1")
check("G3d_solutions_are_units_norm_argument",
      all(gnorm(R) ** 2 == gnorm(gmul(R, R)) == 1 for _, R, _ in catalog4)
      and [n * n for n in range(10) if n * n == 1] == [1],
      "R^2 = +-1 => N(R)^2 = N(R^2) = N(+-1) = 1 (multiplicativity, "
      "certified symbolically in G2) => N(R) = 1 (the only nonneg integer "
      "with n^2 = 1) => R is a unit: the catalog search space collapses to "
      "4 elements WITHOUT any box — completeness is norm-powered")
check("G3d_catalog_2x2_filtered_to_2",
      sols_sq["+1"] == [G_ONE, G_MONE] and sols_sq["-1"] == [G_I, G_MI]
      and len(catalog4) == 4
      and [n for _, _, n in survivors] == ["boson", "fermion"],
      "nests: 2 pentagon classes (roots of f^2-1) x 2 particles per class "
      "(roots of R^2 = F among the 4 units) = 4 catalog entries "
      "{(1,1),(1,-1),(-1,i),(-1,-i)}; Galois filter conj(R) = R leaves "
      "EXACTLY 2: boson (1,1) and fermion (1,-1).  The Z2 atlas, complete")

# ═════════════════════════════════════════════════════════════════════════
section("G4 — THE MIRROR: conj is this circle's sigma")
# ═════════════════════════════════════════════════════════════════════════

check("G4_semions_are_conjugate_pair",
      gconj(G_I) == G_MI and gconj(G_MI) == G_I
      and gconj(gconj(G_I)) == G_I,
      "conj(+i) = -i and conj(-i) = +i: the semion and anti-semion are "
      "each other's Galois conjugates — exactly the golden/Yang-Lee "
      "pattern of Circle One, one level down")
check("G4_classes_conj_fixed_action_within_fibers",
      gconj(G_ONE) == G_ONE and gconj(G_MONE) == G_MONE
      and gconj(G_ONE) != G_MONE,
      "both F-classes are conj-FIXED (F = +-1 real), so conjugation acts "
      "WITHIN each hexagon fiber: trivially on {+1,-1} over F=+1, swapping "
      "{+i,-i} over F=-1.  (Structural note vs Circle One: there sigma "
      "moved BETWEEN the pentagon classes phi <-> -1/phi; here the "
      "pentagon data is rational and the swap lives inside the F=-1 fiber)")
check("G4_norms_all_one",
      [gnorm(x) for x in (G_ONE, G_MONE, G_I, G_MI)] == [1, 1, 1, 1]
      and all(gnorm(gconj(u)) == gnorm(u) for u in units4),
      "N(+1) = N(-1) = N(+i) = N(-i) = 1 and N(conj z) = N(z): all four "
      "particles are units on the mirror's axis of norm 1")
check("G4_control_fake_mirror_fails",
      not pgeq(pgmul((va, vb + vb), (vc, vd + vd)),
               (pgmul(U, V)[0], pgmul(U, V)[1] + pgmul(U, V)[1])),
      "NEGATIVE CONTROL: the fake mirror (a,b) -> (a,2b) is NOT "
      "multiplicative (symbolic non-identity): being a ring hom is what "
      "lets conj transport solutions; not every relabeling is a mirror")

# ═════════════════════════════════════════════════════════════════════════
section("G5 — SPIN-STATISTICS SEED + what transfers from Circle One")
# ═════════════════════════════════════════════════════════════════════════

Nf = [[0, 1], [1, 0]]
Nf2 = [[sum(Nf[i][k] * Nf[k][j] for k in range(2)) for j in range(2)]
       for i in range(2)]
check("G5_quantum_dimensions_all_one",
      Nf2 == [[1, 0], [0, 1]],
      "fusion matrix N_f = [[0,1],[1,0]] satisfies N_f^2 = I exactly: "
      "char poly x^2 - 1 = (x-1)(x+1), Perron root 1 = d_f; d_1 = 1; "
      "global dim D^2 = 1^2 + 1^2 = 2.  HONEST NOTE: every quantum "
      "dimension is the integer 1 — NO decidable order, NO Perron block, "
      "NO Z[phi] analogue is needed in Circle Two; the d_tau machinery "
      "(1140 lines) has no counterpart here and its absence is a feature")
check("G5_twist_and_nu_ledger",
      theta["fermion"] == G_MONE
      and gmul(Rsym["fermion"], theta["fermion"]) == G_ONE
      and gmul(Rsym["boson"], theta["boson"]) == G_ONE,
      "theta = R (abelian), theta_f = -1, nu = R*theta = +1 for both "
      "survivors — the seed of the spin-statistics theorem, exact")
info("TRANSFERS VERBATIM from Circle One: (1) the RING-LAYER pattern "
     "(hand-rolled pairs + reduction law; Z[i] is Z5's little sibling — "
     "2 coordinates, i^2 = -1 instead of the cyclotomic relation); "
     "(2) the DESCENT pattern (16-case decide + strong induction + "
     "torsion-freeness => domain; ONE descent here, C1 needed two — no "
     "41-adic, since no sqrt(phi) layer, no K at all); (3) the CONJ "
     "pattern (sigma2/conj -> Gaussian conj; hom lemmas + fixed-ring + "
     "solution transport); (4) the EXACTLY-TWO pattern (quadratic + "
     "domain => two roots).  NOT needed: the decidable order (PosP), "
     "Perron, jets/Hessian, the K = ring-extension layer.")

# ═════════════════════════════════════════════════════════════════════════
section("G6 — LEAN COST, calibrated on re-measured Circle One blocks")
# ═════════════════════════════════════════════════════════════════════════

try:
    src = open(os.path.join(LEAN, "Anyon.lean"), encoding="utf-8").read().splitlines()
    L1 = next(i for i, l in enumerate(src) if "THE MOD-11 CLOSURE" in l) - 1
    L2 = next(i for i, l in enumerate(src) if "ROUND 5 — THE DECIDABLE ORDER" in l) - 1
    b1, b2 = src[L1:L2], src[L2:]
    t1 = sum(1 for l in b1 if l.startswith("theorem "))
    t2 = sum(1 for l in b2 if l.startswith("theorem "))
    cal_ok1 = (len(b1), t1) == (386, 47) and (len(b2), t2) == (1140, 102)
    check("G6_calibrators_remeasured_anyon", cal_ok1,
          f"mod-11 block {len(b1)} lines / {t1} theorems "
          f"(= {len(b1)/max(t1,1):.1f} l/t); order+d_tau block {len(b2)} / "
          f"{t2} (= {len(b2)/max(t2,1):.1f} l/t) — re-measured from the "
          "tree with r7's own cut, matching the chartered 386/47, 1140/102")
except Exception as e:
    check("G6_calibrators_remeasured_anyon", False, repr(e))

try:
    import difflib
    import re

    def decls(path):
        txt = open(path, encoding="utf-8").read()
        # strip block and line comments (r8s_k1's method, simplified)
        out, i, depth, n = [], 0, 0, len(txt)
        while i < n:
            if txt.startswith('/-', i):
                depth += 1
                i += 2
                continue
            if depth and txt.startswith('-/', i):
                depth -= 1
                i += 2
                continue
            if depth:
                out.append('\n' if txt[i] == '\n' else ' ')
                i += 1
                continue
            if txt.startswith('--', i):
                j = txt.find('\n', i)
                i = n if j < 0 else j
                continue
            out.append(txt[i])
            i += 1
        t = ''.join(out)
        return [(k, nm) for k, nm in re.findall(
            r'^(theorem|def)\s+([A-Za-z0-9_\'.]+)', t, re.M)]

    old_p = os.path.join(LEAN, "archive/src-round7/MagicSquare.lean")
    new_p = os.path.join(LEAN, "MagicSquare.lean")
    oldd, newd = decls(old_p), decls(new_p)
    oldset = {nm for _, nm in oldd}
    newthm = [nm for k, nm in newd if k == 'theorem' and nm not in oldset]
    sm = difflib.SequenceMatcher(None,
                                 open(old_p).read().splitlines(),
                                 open(new_p).read().splitlines())
    inserts = [j2 - j1 for tag, i1, i2, j1, j2 in sm.get_opcodes()
               if tag == 'insert']
    check("G6_calibrator_remeasured_coker",
          len(newthm) == 22 and max(inserts, default=0) == 220,
          f"coker section: one pure {max(inserts, default=0)}-line insertion, "
          f"{len(newthm)} new theorems (= {max(inserts,default=0)/22:.1f} l/t) "
          "— matches the chartered 220/22")
except Exception as e:
    check("G6_calibrator_remeasured_coker", False, repr(e))

sizes = {m: m * m for m in range(2, 7)}
check("G6_antisymmetrizer_sizes",
      list(sizes.values()) == [4, 9, 16, 25, 36]
      and [2 * m * (m - 1) for m in range(2, 7)] == [4, 12, 24, 40, 60],
      "matrix sizes m^2 x m^2: 4,9,16,25,36 (top: 36x36 with 60 nonzero "
      "entries); a raw kernel decide of M^2 = 2M at m=6 is 36^3 = 46,656 "
      "integer mult-adds WITHOUT native_decide (C1 policy: none) — "
      "borderline; the generic index proof needs no decide at all")

info("")
info("COST ESTIMATE (calibrated 8.2-11.2 lines/theorem, C1 measured):")
info("  S1 Z[i] ring layer (pairs, CommRing, conj hom, N, Brahmagupta,")
info("     units):                              ~35 thm  ~300 ln  (250-350)")
info("  S2 domain by mod-4 descent (16-case decide, halving induction,")
info("     torsion-free, no-zero-divisors):     ~20 thm  ~200 ln  (150-250)")
info("     [C1 needed TWO descents (2-adic + 41-adic); C2 needs ONE]")
info("  S3 pentagon necessity (16-instance bash, pentagon <=> F^2=1 over")
info("     any CommRing, slot gauge-invariance): ~18 thm ~160 ln  (130-220)")
info("  S4 hexagon necessity (8-instance bash, + pentagon <=> R^2 = F,")
info("     second hexagon on units):            ~15 thm  ~140 ln  (110-190)")
info("  S5 exactly-two + catalog completeness (factor+domain roots,")
info("     solutions-are-units, units=4, 2x2=4 -> 2): ~25 thm ~230 ln (180-300)")
info("  S6 Galois filter/mirror (fixed ring, filter <=> R=R^-1 on units,")
info("     fiber action, semion swap):          ~12 thm  ~110 ln  (90-150)")
info("  S7 EXCLUSION RANKS (M = I-S over Z, M^2 = 2M generic, image basis")
info("     {e_ij - e_ji : i<j}, card = C(m,2) = 1,3,6,10,15, psi-x-psi kill;")
info("     m = 2..6 instances):                 ~30 thm  ~350 ln  (250-450)")
info("     <<< THE RISKY SECTION: 'matrix rank' has no mathlib-free")
info("     off-the-shelf.  RECOMMENDED SHAPE: idempotent + explicit image")
info("     basis + Fintype.card (rank never mentioned, the numbers 1,3,6,")
info("     10,15 arrive as cardinalities).  A literal fraction-free-")
info("     elimination rank certificate would add +300-500 ln and new")
info("     machinery; a raw 36x36 decide without native_decide may not")
info("     reduce in kernel-acceptable time.  Budget the reformulation. >>>")
info("  S8 spin-statistics seed + dims (theta = R, nu = +1, d = 1, D^2 = 2,")
info("     NO order module):                    ~8 thm   ~70 ln   (50-100)")
info("  ------------------------------------------------------------------")
info("  CORE TOTAL:  ~163 theorems, ~1,560 lines  (range 1,200-2,000)")
info("  = about 1.4 d_tau-blocks; sections S1-S6+S8 are one comfortable")
info("  C1-cadence round (~130 thm / ~1,200 ln); S7 is its own focused")
info("  half-round.  Cheaper than Circle One round-for-round: one ring,")
info("  one descent, no order, no jets, dims all 1.")

# ═════════════════════════════════════════════════════════════════════════
section("SUMMARY")
# ═════════════════════════════════════════════════════════════════════════
print(f"checks run: {N_CHECK};  failed: {len(FAILED)}")
if FAILED:
    for f in FAILED:
        print("  FAILED:", f)
    print("VERDICT: NOT CLEAN — do not charter until repaired.")
    sys.exit(1)
print("VERDICT: every certificate exact, every control negative, every count")
print("tied to its nest.  The Circle Two charter's numbers are sound.")
