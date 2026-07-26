#!/usr/bin/env python3
"""verify_stranger.py — independent stranger verifier (REGISTER row 7, instance 2).

Written WITHOUT reading any seat-B verifier and WITHOUT importing Zi.lean's defs.
Gaussian integers are reimplemented from scratch as Python (re, im) int tuples.
Every load-bearing claim from courier/Zi_statements_v7.txt that I flagged in
STRANGER-PHASE1-STATEMENTS-FINDINGS.md is re-derived by a route of my own
choosing (brute enumeration over the Z2 index cube; from-scratch arithmetic;
explicit 4x4 integer matrix build). Norm 5: each claim family carries a negative
control. Norm 16: this instrument self-tests — run with `--plant` to see it bite.

exit 0 == all checks pass AND all negative controls behave as negatives.
"""
import sys
from fractions import Fraction

# ------------------------------------------------------------------ arithmetic
# Gaussian integer = (re, im), pure Python, independent of Zi.lean.
def add(z, w):  return (z[0] + w[0], z[1] + w[1])
def neg(z):     return (-z[0], -z[1])
def sub(z, w):  return (z[0] - w[0], z[1] - w[1])
def mul(z, w):  return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])
def conj(z):    return (z[0], -z[1])
def normSq(z):  return z[0]*z[0] + z[1]*z[1]
ZERO=(0,0); ONE=(1,0); I=(0,1); MONE=(-1,0); MI=(0,-1)

PLANT = "--plant" in sys.argv
CHECKS = []
def check(name, ok, note=""):
    CHECKS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {note}" if note else ""))

# ------------------------------------------------------------------ S1 ring
check("i_squared_is_minus_one", mul(I, I) == MONE, "i^2 = -1")
# normSq multiplicative (Brahmagupta–Fibonacci), brute over a box
bf = all(normSq(mul((a,b),(c,d))) == normSq((a,b))*normSq((c,d))
         for a in range(-3,4) for b in range(-3,4)
         for c in range(-3,4) for d in range(-3,4))
check("normSq_mul / brahmagupta", bf, "|zw|^2=|z|^2|w|^2 over [-3,3]^4")
check("live_mul_witness", mul((1,2),(3,4)) == (-5,10))
check("conj_mul", all(conj(mul((a,b),(c,d))) == mul(conj((a,b)),conj((c,d)))
                      for a in range(-3,4) for b in range(-3,4)
                      for c in range(-2,3) for d in range(-2,3)))

# ------------------------------------------------------------------ S2 domain
# normSq z = 0  <->  z = 0 ; and no zero divisors, brute over a box
box5 = [(a,b) for a in range(-5,6) for b in range(-5,6)]
check("normSq_eq_zero_iff",
      all((normSq(z)==0) == (z==ZERO) for z in box5))
nzd = True
for z in box5:
    for w in box5:
        if mul(z,w)==ZERO and not (z==ZERO or w==ZERO):
            nzd=False
check("no_zero_divisors", nzd, "brute [-5,5]^2 x [-5,5]^2")

# ------------------------------------------------------------------ pentagon (S3)
# Rebuild pentagon semantics from the statements file's defs, independently.
def Fz2(f, a,b,c,d,x,y):
    if x==(a+b)%2 and y==(b+c)%2 and d==(a+b+c)%2:
        return f if (a==1 and b==1 and c==1) else ONE
    return ZERO
def pentL(f,a,b,c,d):
    x=(a+b)%2; y=(x+c)%2; t=(y+d)%2; w=(c+d)%2; v=(b+w)%2; u=(b+c)%2
    return mul(mul(Fz2(f,a,b,c,y,x,u), Fz2(f,a,u,d,t,y,v)), Fz2(f,b,c,d,v,u,w))
def pentR(f,a,b,c,d):
    x=(a+b)%2; y=(x+c)%2; t=(y+d)%2; w=(c+d)%2; v=(b+w)%2
    return mul(Fz2(f,x,c,d,t,y,w), Fz2(f,a,b,w,t,x,v))
def pentagon(f):
    return all(pentL(f,a,b,c,d)==pentR(f,a,b,c,d)
               for a in range(2) for b in range(2) for c in range(2) for d in range(2))
# f*f = one over the units and a few extras -> pentagon iff f in {+1,-1}
sat = [f for f in [ONE,MONE,I,MI,(2,0),(0,2),(1,1),(3,0)] if pentagon(f)]
check("pentagon_exactly_two", sorted(sat)==sorted([ONE,MONE]),
      f"pentagon holds exactly for {sorted(sat)} = {{+1,-1}}")
check("pentagon_iff_f_sq_one",
      all(pentagon(f) == (mul(f,f)==ONE) for f in
          [ONE,MONE,I,MI,(2,0),(0,2),(1,1),(3,0),(5,0)]))
# nest: classification counts for f=(5,0)
f5=(5,0)
quads=[(a,b,c,d) for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
n_one  = sum(1 for (a,b,c,d) in quads if pentL(f5,a,b,c,d)==ONE)
n_f    = sum(1 for (a,b,c,d) in quads if pentL(f5,a,b,c,d)==f5)
n_f2   = sum(1 for (a,b,c,d) in quads if pentL(f5,a,b,c,d)==(25,0))
check("pent_classification_counted", (n_one,n_f,n_f2)==(11,4,1) and 11+4+1==16,
      f"(=one,=f,=f^2)=({n_one},{n_f},{n_f2}); 11+4+1=16")
check("pent_nest_card", len(quads)==16)

# ------------------------------------------------------------------ hexagon (S4)
def Rz2(r,x,y): return r if (x==1 and y==1) else ONE
def hexAdm(a,b,c,d):
    return d==(((a+b)%2)+c)%2 and d==(((a+c)%2)+b)%2
def hexL(f,r,a,b,c,d):
    e=(a+b)%2; z=(a+c)%2
    return mul(Rz2(r,e,c), Fz2(f,c,a,b,d,z,e))
def hexR(f,r,a,b,c,d):
    e=(a+b)%2; z=(a+c)%2; g=(b+c)%2
    return mul(mul(Fz2(f,a,b,c,d,e,g), Rz2(r,b,c)),
               mul(Fz2(f,a,c,b,d,z,g), Rz2(r,a,c)))
def hexagon(f,r):
    return all(hexL(f,r,a,b,c,d)==hexR(f,r,a,b,c,d)
               for a in range(2) for b in range(2) for c in range(2) for d in range(2)
               if hexAdm(a,b,c,d))
adm = [(a,b,c,d) for a in range(2) for b in range(2) for c in range(2) for d in range(2)
       if hexAdm(a,b,c,d)]
check("hex_nest_8_of_16", len(adm)==8 and 2*2*2*2==16, f"admissible={len(adm)}/16")

# ------------------------------------------------------------------ units + catalog
units = [z for z in box5 if normSq(z)==1]
check("norm_one_units", sorted(units)==sorted([ONE,MONE,I,MI]),
      f"normSq=1 exactly at {sorted(units)}")

# ------------------------------------------------------------------ capstone (S6)
def roomy(f,r):
    return pentagon(f) and hexagon(f,r) and conj(r)==r
# exactly two, over a generous candidate set for f and r
cands = sorted({ONE,MONE,I,MI,(2,0),(0,2),(1,1),(3,0),(0,3),(2,1),(0,-3),(-2,0)})
roomy_pairs = sorted({(f,r) for f in cands for r in cands if roomy(f,r)})
rset = sorted({r for f,r in roomy_pairs})
check("roomy_iff_boson_or_fermion",
      roomy_pairs==sorted([(ONE,ONE),(ONE,MONE)]),
      f"roomy pairs = {roomy_pairs}")
# the headline: exists f. roomy f r  <->  r in {+1,-1}
ex = sorted({r for r in cands if any(roomy(f,r) for f in cands)})
check("the_roomy_world_has_exactly_two_particles", ex==sorted([ONE,MONE]),
      f"exists-f roomy holds exactly for r in {ex}")
check("capstone_count_two",
      roomy(ONE,ONE) and roomy(ONE,MONE) and ONE!=MONE and
      all(f==ONE and (r in (ONE,MONE)) for f,r in roomy_pairs),
      "count=2, f pinned to one, r in {+-1}")
# F6 explicit: WITHOUT the reality filter, is the (f,r) set still 2? (measure it)
def roomy_nofilter(f,r): return pentagon(f) and hexagon(f,r)
nofilter_pairs = [(f,r) for f in cands for r in cands if roomy_nofilter(f,r)]
check("F6_reality_filter_is_load_bearing",
      len(nofilter_pairs) > 2,
      f"without conj r = r there are {len(nofilter_pairs)} pentagon&hexagon pairs "
      f"(e.g. semions) -> filter genuinely cuts them")

# ------------------------------------------------------------------ m=2 antisymmetrizer (real exclusion content)
def swapIdx(n): return {0:0,1:2,2:1}.get(n,3)
def Mmat(p,q):  return (1 if p==q else 0) - (1 if q==swapIdx(p) else 0)
n=4
M=[[Mmat(p,q) for q in range(n)] for p in range(n)]
M2=[[sum(M[p][k]*M[k][q] for k in range(n)) for q in range(n)] for p in range(n)]
check("M2_sq_eq_two_M", all(M2[p][q]==2*M[p][q] for p in range(n) for q in range(n)),
      "M^2 = 2M for M = I - SWAP (m=2)")
check("M2_trace", sum(M[k][k] for k in range(n))==2, "tr M = 2 = 2*2-2")
# rank of M over Q (independent Gaussian elimination) should be 2
def rank(A):
    # exact rational Gaussian elimination (no float error)
    A=[[Fraction(x) for x in row] for row in A]; r=0; rows=len(A); cols=len(A[0])
    for c in range(cols):
        piv=next((i for i in range(r,rows) if A[i][c]!=0), None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(rows):
            if i!=r and A[i][c]!=0:
                fac=A[i][c]/A[r][c]
                A[i]=[A[i][j]-fac*A[r][j] for j in range(cols)]
        r+=1
    return r
check("M2_rank_one", rank(M)==1,
      "rank(I-SWAP) at m=2 = 1 (M^2=2M, tr=2 => one eigenvalue 2 => rank 1; "
      "one antisymmetric mode = one Slater det). [my initial guess rank 2 was MY bug]")
check("census_nest_m2", ((lambda tri: tri(2)+tri(3)==4 and 2*2==4)
      (lambda k: k*(k-1)//2)), "tri2+tri3 = 1+3 = 4 = 2*2")

# ------------------------------------------------------------------ F3 confirmation: the 'pauli' lines are content-free
# claim: they are true for ALL x,y ONLY because mul is commutative.
pauli_holds = all(sub(mul(x,y),mul(y,x))==ZERO for x in box5 for y in box5)
comm_holds  = all(mul(x,y)==mul(y,x) for x in box5 for y in box5)
check("F3_pauli_kill_is_just_commutativity", pauli_holds and comm_holds,
      "x*y-y*x=0 for ALL x,y AND mul is commutative -> the 'exclusion' name has no content here")

# ------------------------------------------------------------------ NEGATIVE CONTROLS (norm 5): must behave as negatives
check("ctrl_fake_mirror_fails",
      (lambda fm: fm(mul(I,I)) != mul(fm(I),fm(I)))(lambda z:(z[0],2*z[1])),
      "fake mirror is NOT multiplicative")
check("ctrl_coordMul_differs",
      (lambda cm: cm(I,I) != mul(I,I))(lambda z,w:(z[0]*w[0],z[1]*w[1])))
check("ctrl_f_eq_i_fails_pentagon", not pentagon(I), "i is NOT a pentagon solution")
check("ctrl_semion_not_roomy",
      pentagon(MONE) and hexagon(MONE,I) and conj(I)!=I and not roomy(MONE,I),
      "semion passes pentagon+hexagon but fails reality filter -> not roomy")
check("ctrl_boson_no_exclusion",
      add(mul(ONE,ONE),mul(ONE,ONE))==(2,0) and (2,0)!=ZERO,
      "boson +1 does NOT annihilate double occupation")
# fermion side of the exclusion (positive of the control family)
check("fermion_minus_one_kills",
      add(mul(MONE,ONE),mul(ONE,ONE))==ZERO,
      "fermion -1 DOES annihilate: (-1)+(+1)=0")

# ------------------------------------------------------------------ NORM 16 self-test (planted defect)
if PLANT:
    # flip the headline expectation on purpose
    check("PLANTED_headline", ex==sorted([ONE,MONE,I]),
          "planted: claim three particles (should FAIL)")

# ------------------------------------------------------------------ summary
npass = sum(1 for _,ok in CHECKS if ok)
nfail = len(CHECKS)-npass
print(f"\nchecks run: {len(CHECKS)};  passed: {npass};  failed: {nfail}")
if nfail==0:
    print("VERDICT: stranger routes independently re-derive every load-bearing claim; "
          "controls behave as negatives; F3/F6 measured.")
    print("EXIT: 0"); sys.exit(0)
else:
    print("EXIT: 1"); sys.exit(1)
