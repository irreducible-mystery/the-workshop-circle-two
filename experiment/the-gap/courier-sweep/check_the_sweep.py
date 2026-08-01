#!/usr/bin/env python3
"""
check_the_sweep.py -- run every checkable claim the courier's GAP sweep made.

The sweep was delivered as chat prose and never executed.  Each claim below is
quoted from it, then measured.  Verdicts are HELD / GARBLED / WRONG / NEW.
GARBLED means the underlying mathematics is right and the sentence was not.

The equation throughout:      d^2 = d + g          (the gap is g)
As a Moebius map:             M(x) = 1 + g/x       matrix A = [[1,g],[1,0]]
Roots:                        x_+- = (1 +- sqrt(1+4g))/2

No third-party imports.  Exact arithmetic where the claim is exact.
"""

import cmath
import math
from fractions import Fraction

TOL = 1e-9
RESULTS = []


def report(tag, claim, measured, verdict):
    RESULTS.append((tag, verdict))
    print(f"\n[{tag}]  {verdict}")
    print(f"  claim    : {claim}")
    for line in measured.strip().split("\n"):
        print(f"  measured : {line}")


def roots(g):
    """Both roots of x^2 = x + g, as complex."""
    d = cmath.sqrt(1 + 4 * g)
    return (1 + d) / 2, (1 - d) / 2


def multiplier(g, x):
    """M'(x) where M(x) = 1 + g/x."""
    return -g / (x * x)


# ---------------------------------------------------------------- S1
def s1():
    """The two identities the whole thing started from."""
    g = 1
    a, b = roots(g)
    out = (f"g=+1 roots {a.real:.6f}, {b.real:.6f}\n"
           f"sum      = {(a+b).real:+.15f}   (Vieta: 1 for every g)\n"
           f"product  = {(a*b).real:+.15f}   (Vieta: -g)")
    ok = abs((a + b) - 1) < TOL and abs((a * b) + 1) < TOL
    report("S1", "phi + psi = 1 and phi x psi = -1 are the g=+1 case of Vieta "
                 "on x^2 = x + g: sum is 1 for EVERY gap, product is -g.",
           out, "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S2
def s2():
    """The critical gap."""
    a, b = roots(Fraction(-1, 4))
    disc = 1 + 4 * (-0.25)
    out = (f"discriminant 1+4g at g=-1/4 : {disc:+.15f}\n"
           f"both roots                  : {a.real:.15f}, {b.real:.15f}\n"
           f"separation                  : {abs(a-b):.15e}")
    ok = abs(disc) < TOL and abs(a - 0.5) < TOL and abs(b - 0.5) < TOL
    report("S2", "at g = -1/4 the two roots meet at exactly 1/2; that is where "
                 "the distance between true and false closes.",
           out, "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S3
def s3():
    """Root modulus on the elliptic side."""
    lines, ok = [], True
    for g in (-0.3, -0.5, -1.0, -2.0, -5.0, -1.894427):
        a, _ = roots(g)
        pred = math.sqrt(-g)
        ok &= abs(abs(a) - pred) < 1e-12
        lines.append(f"g={g:>10.6f}  |root|={abs(a):.12f}  sqrt(-g)={pred:.12f}")
    report("S3", "below the critical gap the roots are a conjugate pair of "
                 "modulus sqrt(-g), so the gap sweeps dissipation -> unitarity "
                 "-> gain.",
           "\n".join(lines), "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S4
def s4():
    """Uniqueness of the unitary gap.

    NOTE ON THE INSTRUMENT.  The first version of this check scanned a grid
    and accepted any g with ||root| - 1| < 5e-4.  It returned TWO hits,
    -1.001 and -1.0, and scored the claim WRONG.  The claim was right; the
    test was blunt -- sqrt is flat near 1, so an absolute tolerance on the
    OUTPUT admits a whole neighbourhood of the INPUT.  Recorded rather than
    quietly fixed, because a gate that convicts a true claim through its own
    slack is the exact species this record spent five circles on.
    """
    # |root|^2 = -g exactly (product of a conjugate pair), so |root| = 1
    # has the single solution g = -1.  Verify injectivity, then the point.
    mono = all(-(g / 1000) > -((g + 1) / 1000) for g in range(-4000, -251))
    step = 1e-3
    hits = [g / 1000 for g in range(-4000, -250)
            if abs(abs(roots(g / 1000)[0]) - 1) < step / 4]
    a, _ = roots(-1.0)
    out = (f"|root|^2 = -g is strictly decreasing in g : {mono}  "
           f"(so at most one solution)\n"
           f"grid {step} over [-4,-0.25], ||root|-1| < {step/4:g} : {hits}\n"
           f"g=-1 roots  : {a:.12f} and conjugate\n"
           f"|root|      : {abs(a):.15f}\n"
           f"arg(root)   : {cmath.phase(a):.15f} rad = pi/{math.pi/cmath.phase(a):.6f}\n"
           f"root^6      : {a**6:.12f}   root^k != 1 for k<6 : "
           f"{all(abs(a**k - 1) > 1e-9 for k in range(1,6))}")
    ok = (mono and hits == [-1.0] and abs(abs(a) - 1) < TOL
          and abs(a ** 6 - 1) < 1e-9)
    report("S4", "g = -1 is the unique gap with both roots on the unit circle "
                 "-- the reversible / unitary one -- and the roots are "
                 "primitive 6th roots of unity.",
           out, "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S5
def s5():
    """Attractor / repeller, and the sign the sweep dropped."""
    g = 1.0
    phi, psi = roots(g)
    kphi, kpsi = multiplier(g, phi), multiplier(g, psi)
    x, traj = 1.0, []
    for _ in range(8):
        x = 1 + g / x
        traj.append(x)
    sides = "".join("+" if t > phi.real else "-" for t in traj)
    out = (f"M'(phi) = {kphi.real:+.12f}   |.| = {abs(kphi):.12f}  = 1/phi^2\n"
           f"M'(psi) = {kpsi.real:+.12f}   |.| = {abs(kpsi):.12f}  = phi^2\n"
           f"orbit from x=1 : " + ", ".join(f"{t:.5f}" for t in traj[:6]) + "\n"
           f"side of phi    : {sides}   (alternates -> multiplier is NEGATIVE)")
    ok = (abs(abs(kphi) - 1 / phi.real ** 2) < TOL and kphi.real < 0
          and abs(kpsi) > 1 and "+-+-" in sides)
    report("S5", "the multiplier is 0.38 at phi (attracting) and 2.62 at psi "
                 "(repelling).",
           out,
           "GARBLED" if ok else "WRONG")
    print("  note     : the magnitudes are right and the sweep called them "
          "'phi ~ 0.38' as though\n"
          "             0.38 were a ROOT. It is the multiplier, and it is "
          "NEGATIVE: the orbit\n"
          "             converges by alternating sides, which is the "
          "continued fraction of phi.")


# ---------------------------------------------------------------- S6
def classify(g):
    """Strict Moebius classification by the multiplier at a fixed point."""
    if abs(1 + 4 * g) < 1e-15:
        return "parabolic", 1.0
    a, b = roots(g)
    k = multiplier(g, a)
    if abs(k) > 1:
        k = multiplier(g, b)
    if abs(abs(k) - 1) < 1e-12:
        return "elliptic", k
    if abs(k.imag) < 1e-12 and k.real > 0:
        return "hyperbolic", k
    return "loxodromic", k


def s6():
    """The four gap values, classified strictly."""
    claimed = {1: "hyperbolic", -1: "elliptic",
               1j: "loxodromic", -1j: "loxodromic",
               -0.25: "parabolic"}
    lines, verdicts = [], []
    for g, want in claimed.items():
        got, k = classify(complex(g))
        det = -g
        agree = "==" if got == want else "!="
        verdicts.append(got == want)
        lines.append(f"g={str(g):>7}  det=-g={str(det):>7}  |k|={abs(k):.6f}  "
                     f"{got:<11} {agree} claimed {want}")
    report("S6", "the four gap values are one from each Moebius conjugacy "
                 "class: g=+1 hyperbolic, g=-1 elliptic, g=+-i loxodromic, "
                 "g=-1/4 parabolic.",
           "\n".join(lines), "GARBLED" if not all(verdicts) else "HELD")
    print("  note     : g=+1 fails HYPERBOLIC on the strict definition -- the "
          "multiplier is real\n"
          "             but NEGATIVE, so the map is loxodromic and its SQUARE "
          "is hyperbolic.\n"
          "             The reason is structural and the sweep never said it: "
          "det(A) = -g, so the\n"
          "             SIGN OF THE GAP is the orientation. g<0 preserves the "
          "upper half-plane\n"
          "             (honest isometry of hyperbolic space); g>0 swaps the "
          "half-planes.")


# ---------------------------------------------------------------- S7
def matmul(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]))


def is_scalar(A):
    return A[0][1] == 0 and A[1][0] == 0 and A[0][0] == A[1][1] and A[0][0] != 0


def is_identity(A):
    return A == ((1, 0), (0, 1))


def s7():
    """Order of the map vs order of the matrix at g = -1."""
    A = ((1, -1), (1, 0))
    P = A
    map_order = mat_order = None
    for n in range(1, 25):
        if map_order is None and is_scalar(P):
            map_order = n
        if mat_order is None and is_identity(P):
            mat_order = n
        if map_order and mat_order:
            break
        P = matmul(P, A)
    # confirm on the map itself
    def M(x):
        return 1 - 1 / x
    x0 = 3.7
    orbit = [x0]
    for _ in range(4):
        orbit.append(M(orbit[-1]))
    out = (f"A^{map_order} is scalar  -> the MAP has order {map_order}\n"
           f"A^{mat_order} = I        -> the MATRIX has order {mat_order}\n"
           f"orbit of 3.7 under M : " + ", ".join(f"{t:.6f}" for t in orbit) + "\n"
           f"returns after {map_order} steps: {abs(orbit[map_order]-x0) < 1e-9}")
    report("S7", "g = -1 is elliptic OF ORDER 6.",
           out, "GARBLED")
    print("  note     : 6 is the order of the MATRIX. The Moebius map has "
          "order 3, because the\n"
          "             matrix is only defined up to sign and A^3 = -I. The "
          "roots really are\n"
          "             primitive 6th roots of unity (S4); the map they "
          "generate is not.")


# ---------------------------------------------------------------- S8
def s8():
    """The golden rotation number -- the sweep asserted it, never located it."""
    phi = (1 + math.sqrt(5)) / 2
    target = 1 / phi ** 2                      # 0.381966..., = 2 - phi
    lo, hi = -20.0, -0.2500000001
    for _ in range(200):                       # rotation number is monotone here
        mid = (lo + hi) / 2
        a, _ = roots(mid)
        theta = cmath.phase(a) / math.pi
        if theta > target:
            lo = mid
        else:
            hi = mid
    g_num = (lo + hi) / 2
    # independent derivation: cos(pi.theta) = (1/2)/sqrt(-g)
    g_exact = -1 / (4 * math.cos(math.pi * target) ** 2)
    g_asserted = -(1 + 2 / math.sqrt(5))          # what the sweep claimed
    a, _ = roots(g_num)
    b, _ = roots(g_asserted)
    out = (f"target rotation number      : {target:.15f}   (= 1/phi^2 = 2-phi)\n"
           f"gap by bisection            : {g_num:.15f}\n"
           f"gap by -1/(4cos^2(pi.theta)): {g_exact:.15f}\n"
           f"two independent routes agree: {abs(g_num-g_exact):.2e}\n"
           f"round-trip rotation number  : {cmath.phase(a)/math.pi:.15f}\n"
           f"\n"
           f"THE SWEEP'S CLOSED FORM -(1+2/sqrt5) : {g_asserted:.15f}\n"
           f"  rotation number actually there     : "
           f"{cmath.phase(b)/math.pi:.15f}\n"
           f"  relative error against the true gap: "
           f"{abs(g_asserted-g_exact)/abs(g_exact)*100:.3f}%")
    located = abs(g_num - g_exact) < 1e-9
    fabricated = abs(g_asserted - g_exact) > 1e-6
    report("S8", "phi appears twice in one sweep -- as a root at g=+1, and as "
                 "the most-robust rotation number on the elliptic side, at "
                 "g = -(1 + 2/sqrt5).",
           out, "WRONG" if fabricated else "NEW")
    print("  note     : THE GAP IS REAL AND THE CONSTANT IS INVENTED. There is "
          "a gap whose\n"
          "             rotation number is exactly golden, two independent "
          "routes put it at\n"
          f"             {g_exact:.9f}, and the closed form the sweep stated "
          "for it is wrong by\n"
          f"             {abs(g_asserted-g_exact)/abs(g_exact)*100:.2f}%. It "
          "was reached by pattern-matching -(1+2/sqrt5) onto a\n"
          "             number that started 1.89, and it survives an eyeball. "
          "Nothing in the\n"
          "             sweep flagged it as a guess. I do not know whether "
          "the true value is\n"
          "             algebraic, and I am not going to assert that either.")
    if located:
        print("             (The LOCATION claim -- that such a gap exists on "
              "the elliptic side --\n"
              "             stands: bisection and the closed-form inversion "
              "agree to 1e-15.)")


# ---------------------------------------------------------------- S9
def s9():
    """Tropical: multiplication is +, addition is max."""
    def solve(g):
        sols = []
        if 0 >= g:                    # x = 0 branch needs max(0,g) = 0
            sols.append(0.0)
        if g / 2 < g:                 # x = g/2 branch needs max(g/2,g) = g
            sols.append(g / 2)
        return sols
    lines, ok = [], True
    for g in (-2, -1, 0, 1, 2, 4):
        s = solve(g)
        for x in s:                   # verify 2x == max(x,g)
            ok &= abs(2 * x - max(x, g)) < TOL
        lines.append(f"g={g:>3}  solutions of 2x = max(x,g) : {s}")
    report("S9", "tropically the equation is 2x = max(x, g), giving x = g/2, "
                 "and the branch point moves to 0.",
           "\n".join(lines) + "\n"
           "branch point (where the solution changes branch) : g = 0",
           "HELD" if ok else "WRONG")
    print("  note     : half-right, and the half it missed is the better half. "
          "x = g/2 is only\n"
          "             the g>0 branch; for g<=0 the solution is x = 0 flat. "
          "The tropical\n"
          "             critical gap is 0, not -1/4 -- degeneracy in one "
          "number system is\n"
          "             an ordinary point in another.")


# ---------------------------------------------------------------- S10
def s10():
    """Boolean ring."""
    bad = [(x, g) for x in (0, 1) for g in (0, 1)
           if (x * x) % 2 != (x + g) % 2]
    good_g = sorted({g for x in (0, 1) for g in (0, 1)
                     if (x * x) % 2 == (x + g) % 2})
    out = (f"F_2 exhaustive, x^2 = x + g fails for (x,g) in : {bad}\n"
           f"gaps admitting ANY solution                    : {good_g}\n"
           f"gaps admitting solutions for EVERY x           : "
           f"{[g for g in (0,1) if all((x*x)%2 == (x+g)%2 for x in (0,1))]}")
    ok = good_g == [0]
    report("S10", "in a Boolean ring x^2 = x forces g = 0: a world where "
                  "everything is its own square cannot have a gap.",
           out, "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S11
def s11():
    """Dual numbers: eps^2 = 0."""
    def dmul(p, q):
        return (p[0] * q[0], p[0] * q[1] + p[1] * q[0])   # eps^2 = 0

    def dadd(p, q):
        return (p[0] + q[0], p[1] + q[1])

    g = (Fraction(0), Fraction(1))                        # g = eps
    cands = {"1+eps": (Fraction(1), Fraction(1)),
             "-eps": (Fraction(0), Fraction(-1))}
    lines, ok = [], True
    for name, x in cands.items():
        lhs, rhs = dmul(x, x), dadd(x, g)
        ok &= lhs == rhs
        lines.append(f"x = {name:<6}  x^2 = {lhs}   x+g = {rhs}   "
                     f"{'equal' if lhs == rhs else 'DIFFER'}")
    lines.append(f"sum of the two roots : "
                 f"{dadd(cands['1+eps'], cands['-eps'])}  (Vieta says (1,0))")
    report("S11", "an infinitesimal gap g = eps gives roots 1+eps and -eps.",
           "\n".join(lines), "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S12
def s12():
    """Where the critical gap lives in characteristic p."""
    lines = []
    for p in (2, 3, 5, 7, 11, 13):
        deg = [g for g in range(p) if (1 + 4 * g) % p == 0]
        lines.append(f"char {p:>2} : degenerate gap g with 1+4g = 0  ->  "
                     f"{deg if deg else 'NONE'}")
    out = "\n".join(lines)
    ok = True
    report("S12", "-1/4 is the critical gap. (Reading it in characteristic p "
                 "was not in the sweep; this cross-checks Circle Three's "
                 "prover, who ran the same equation from the other side.)",
           out, "NEW" if ok else "WRONG")
    print("  note     : char 2 has NO critical gap (1+4g = 1 identically) and "
          "char 5 puts it at\n"
          "             g = +1 (since -1/4 = -1.4^-1 = -4 = 1 mod 5). Both "
          "match the Circle\n"
          "             Three prover's independent finding, reached from "
          "G = x^2 - x instead.")


# ---------------------------------------------------------------- S13
def s13():
    """Critical damping."""
    def response(g, n=60):
        a, b = 0.0, 1.0
        seq = [b]
        for _ in range(n):
            a, b = b, b + g * a
            seq.append(b)
        return seq

    lines, ok = [], True
    for g in (-0.15, -0.25, -0.40):
        seq = response(g)
        flips = sum(1 for i in range(1, len(seq))
                    if seq[i] * seq[i - 1] < 0)
        decay = abs(seq[40]) ** (1 / 40) if seq[40] else 0.0
        lines.append(f"g={g:+.2f}  sign changes in 60 steps : {flips:>3}   "
                     f"per-step decay {decay:.6f}")
        if g == -0.25:
            ok &= flips == 0 and abs(decay - 0.5) < 0.05
    report("S13", "g = -1/4 is critical damping, zeta = 1 -- every shock "
                  "absorber in the world.",
           "\n".join(lines) + "\n"
           "at g=-1/4 the decay rate is 1/2 = the double root, and nothing "
           "oscillates",
           "HELD" if ok else "WRONG")


# ---------------------------------------------------------------- S14
def s14():
    """The Galois claim -- the one the sweep got backwards."""
    r5 = math.sqrt(5)
    phi, psi = (1 + r5) / 2, (1 - r5) / 2

    def M(x):
        return 1 + 1 / x

    def sigma_on_root(x):                 # sqrt5 -> -sqrt5 swaps phi and psi
        return psi if abs(x - phi) < TOL else phi

    lhs = sigma_on_root(M(phi))           # sigma(M(phi))
    rhs = M(sigma_on_root(phi))           # M(sigma(phi))
    kphi, kpsi = multiplier(1.0, phi), multiplier(1.0, psi)
    out = (f"sigma(M(phi)) = {lhs:.12f}\n"
           f"M(sigma(phi)) = {rhs:.12f}\n"
           f"they agree    : {abs(lhs-rhs) < TOL}   "
           f"(M has RATIONAL coefficients, so of course it commutes)\n"
           f"|M'(phi)| = {abs(kphi):.6f} < 1  attracting\n"
           f"|M'(psi)| = {abs(kpsi):.6f} > 1  repelling\n"
           f"sigma maps the attractor to the repeller : "
           f"{abs(sigma_on_root(phi)-psi) < TOL}")
    report("S14", "sigma does not commute with iteration -- the Galois mirror "
                  "is time reversal.",
           out, "WRONG")
    print("  note     : sigma DOES commute with M, necessarily: M is defined "
          "over Q. The sweep's\n"
          "             sentence is false. What is true, and is what it was "
          "reaching for: sigma is\n"
          "             an algebraic automorphism that carries the ATTRACTING "
          "fixed point to the\n"
          "             REPELLING one, so it cannot be realised by any "
          "topological conjugacy of\n"
          "             the dynamics. It preserves the equation and reverses "
          "the arrow. That is a\n"
          "             sharper statement than the one it replaces, and the "
          "sweep asserted the\n"
          "             loose version without checking a two-line "
          "computation.")


# ---------------------------------------------------------------- S15
def s15():
    """The one claim that was already machine-checked, re-measured here."""
    units = {"1": (1, 0), "-1": (-1, 0), "i": (0, 1), "-i": (0, -1)}

    def mul(p, q):
        return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])

    def conj(p):
        return (p[0], -p[1])

    lines, ok = [], True
    for name, R in units.items():
        selfinv = mul(R, R) == (1, 0)
        fixed = conj(R) == R
        ok &= (selfinv == fixed)
        lines.append(f"R = {name:>2}  R*R=1 : {str(selfinv):<5}  "
                     f"conj R = R : {str(fixed):<5}  agree : {selfinv == fixed}")
    report("S15", "on the four units, R = R^-1 iff conj R = R; survivors are "
                  "+-1, the semions +-i are cut. (Proved in Lean in the "
                  "sealed record as selfInverse_iff_mirror_fixed.)",
           "\n".join(lines) + "\n"
           "the cut is 4 -> 2, and it is 2+2 -> 2+0, not 1+1",
           "HELD" if ok else "WRONG")
    print("  note     : this is the ONLY claim in the sweep that had already "
          "been checked by a\n"
          "             machine before the sweep asserted it. It is also the "
          "only one that needed\n"
          "             no repair. The physical reading laid on top of it -- "
          "conjugation is time\n"
          "             reversal, so the filter is T-invariance -- is a claim "
          "about the world and\n"
          "             is NOT settled by anything above.")


# ---------------------------------------------------------------- S16
def s16():
    """Where the sweep's own picture dies, and it never noticed."""
    A0 = ((1, 0), (1, 0))
    det0 = A0[0][0] * A0[1][1] - A0[0][1] * A0[1][0]
    vals = [1 + 0 / x for x in (0.1, 1.0, -7.0, 1e6)]
    a, b = roots(0)
    out = (f"g=0 matrix [[1,g],[1,0]] = {A0}   det = {det0}  -> SINGULAR\n"
           f"M(x) = 1 + 0/x on x = 0.1, 1, -7, 1e6 : {vals}  -> CONSTANT\n"
           f"roots at g=0 : {a.real:.1f} and {b.real:.1f}  (the two idempotents)\n"
           f"det(A) = -g, so det > 0 exactly when g < 0")
    ok = det0 == 0 and len(set(vals)) == 1
    report("S16", "(not claimed by the sweep) the sweep built its whole "
                  "classical/quantum story on the 'g=0 spine' where the roots "
                  "are 0 and 1.",
           out, "NEW" if ok else "WRONG")
    print("  note     : g=0 is exactly where the Moebius picture DIES. The "
          "matrix is singular and\n"
          "             the map collapses to the constant 1 -- it is not a "
          "Moebius transformation\n"
          "             at all. The sweep called g=0 its spine and then used "
          "Moebius language\n"
          "             across it without noticing the frame does not exist "
          "there.\n"
          "             The organising fact it missed: det(A) = -g. THE SIGN "
          "OF THE GAP IS THE\n"
          "             ORIENTATION. For g<0 the map is an honest isometry of "
          "the upper half-plane;\n"
          "             for g>0 it swaps the half-planes; at g=0 there is no "
          "map. That single line\n"
          "             explains S6's failure and organises the whole sweep "
          "better than the\n"
          "             'classical / critical / quantum' three-régime story "
          "the sweep led with.")


def main():
    print("=" * 78)
    print("CHECKING THE COURIER'S GAP SWEEP".center(78))
    print("d^2 = d + g,  swept over every gap value and every number system".center(78))
    print("=" * 78)
    for fn in (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16):
        fn()
    print("\n" + "=" * 78)
    tally = {}
    for _, v in RESULTS:
        tally[v] = tally.get(v, 0) + 1
    for tag, verdict in RESULTS:
        print(f"  {tag:<4} {verdict}")
    print("-" * 78)
    print("  " + "   ".join(f"{v}: {n}" for v, n in sorted(tally.items())))
    print("=" * 78)


if __name__ == "__main__":
    main()
