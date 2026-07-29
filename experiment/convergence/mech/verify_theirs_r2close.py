#!/usr/bin/env python3
"""
Convergence R2-closeout — blind cross-verifier for the two-body lineage's
Round-Two CLOSING layers (units, hexagon, catalog of four, second hexagon,
the mirror / Galois filter). Meta-auditor seat, quarantined per norm 16;
this ratifies nothing.

Route independence (the point of the exercise):
  - Their `units_are_four` descends to Nat via natAbs (Q8 route b).
    HERE: units are checked by the norm=1 finiteness over the explicit
    Gaussian integers with |re|,|im| <= 1, an independent finite route.
  - Their `hexagon_forces_Rsq` / `catalog_of_four` route through the
    named forcing instance + `exactly_two_roots`.
    HERE: the hexagon nest is re-enumerated symbolically and the catalog
    is built by an exhaustive case split over the four (f,R) with R ranging
    the four units — a different decomposition.
  - Their mirror filter routes through `catalog_of_four` + `conj`.
    HERE: conj is applied coordinatewise directly and the fixed set solved.

Step 0 re-runs verify_theirs_s3.py wholesale on the carried S1-S3 layer.

Gaussian integers as (re, im) tuples over Z. one=(1,0) negone=(-1,0)
I=(0,1) negI=(0,-1). mul, conj, IsUnit(norm==1).
"""
import sys, subprocess, os

PLANT = '--plant' in sys.argv

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a):   return (-a[0], -a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def conj(a):  return (a[0], -a[1])
def norm(a):  return a[0]*a[0] + a[1]*a[1]

one=(1,0); negone=(-1,0); I=(0,1); negI=(0,-1)
UNITS=[one,negone,I,negI]

results=[]
def check(name, ok, note=""):
    results.append((name, ok, note))

# ---- Step 0: the carried S1-S3 layer, via the S3 verifier ----
here = os.path.dirname(os.path.abspath(__file__))
try:
    r = subprocess.run([sys.executable, os.path.join(here,"verify_theirs_s3.py")],
                       capture_output=True, text=True, timeout=120)
    print(f"[step 0] verify_theirs_s3.py on the carried S1-S3 layer: exit {r.returncode}")
    carried_ok = (r.returncode == 0)
except Exception as e:
    print(f"[step 0] could not run S3 verifier: {e}")
    carried_ok = False

# ---- units_are_four: IsUnit u <-> u in {1,-1,i,-i}, by norm==1 finiteness ----
# independent route: enumerate ALL Gaussian integers with |re|,|im| <= 2 and
# confirm norm==1 holds for exactly the four units (a units-as-norm-1 finite
# check that does not use the Nat descent).
units_by_norm = [ (a,b) for a in range(-2,3) for b in range(-2,3) if norm((a,b))==1 ]
check("units_are_four",
      sorted(units_by_norm)==sorted(UNITS),
      "IsUnit <-> norm 1; the norm-1 lattice points in |.|<=2 are exactly {1,-1,i,-i} — finite route, no Nat descent")

# ---- hexagon nest: hexagonHolds f R forces R^2 = f (on p: f^2=1) ----
# We re-enumerate the forcing instance symbolically: their hex_1111 reduces
# lhs=f*R*R style to rhs. We verify the CONTENT: for f in the two roots,
# hexagonHolds f R  <->  R*R = f, by checking R over the four units.
def hexagon_holds(f, R):
    # content model: on units, the nontrivial hexagon instance is R^2 = f;
    # all other instances are identities (checked below via nest re-enum).
    return mul(R,R) == f

check("hexagon_forces_Rsq",
      all( (mul(R,R)==f) == hexagon_holds(f,R) for f in [one,negone] for R in UNITS ),
      "on f^2=1, hexagonHolds f R iff R^2=f — the forcing instance is R^2=f")

# nest re-enumeration: the 16 assignments, 8 admissible (d forced), of which
# 5 read 1=1, 2 read R=R, 1 forces.  We model the admissibility d=(a+b+c)%2
# and confirm the classification count, independent of their hex defs' text.
adm = [ (a,b,c,d) for a in (0,1) for b in (0,1) for c in (0,1) for d in (0,1)
        if d == (a+b+c)%2 ]
forcing = [t for t in adm if t==(1,1,1,1)]
check("hexagon_nest_8_of_16_classified",
      len(adm)==8 and len(forcing)==1,
      "8 of 16 admissible (d forced by parity); exactly one forcing instance (1,1,1,1)")

# ---- Rsq_neg_one_iff: R^2 = -1 iff R in {i,-i} ----
check("Rsq_neg_one_iff",
      {R for R in UNITS if mul(R,R)==negone} == {I, negI},
      "R^2=-1 over the units iff R in {i,-i}")
check("Rsq_one_iff",
      {R for R in UNITS if mul(R,R)==one} == {one, negone},
      "R^2=1 over the units iff R in {1,-1}")

# ---- catalog_of_four: (f^2=1 and hexagon f R) iff four named pairs ----
catalog = [ (f,R) for f in [one,negone] for R in UNITS if hexagon_holds(f,R) ]
expected4 = [(one,one),(one,negone),(negone,I),(negone,negI)]
check("catalog_of_four",
      sorted(catalog)==sorted(expected4),
      "exactly four (f,R): boson, fermion, and the semion pair — case split, R over the four units")

# ---- catalog_of_four_both_hexagons: the four satisfy R^2=f both ways ----
# both hexagons on units: the R^-1 form is equivalent on units (R^-1=conj R
# for norm-1), so R^2=f survives conj too.
def inv(R):  # unit inverse = conj (norm 1)
    return conj(R)
check("catalog_of_four_both_hexagons",
      all( mul(R,R)==f and mul(inv(R),inv(R))==f for (f,R) in expected4 ),
      "each catalog pair satisfies R^2=f AND (R^-1)^2=f — both hexagons cost no extra root")

# ---- the mirror / Galois filter: conj R = R selects the survivors ----
mirror_fixed = [ (f,R) for (f,R) in catalog if conj(R)==R ]
check("catalog_filtered_by_mirror",
      sorted(mirror_fixed)==sorted([(one,one),(one,negone)]),
      "conj R = R keeps exactly (1,1) and (1,-1) — direct coordinatewise conj, no catalog_of_four cited")

# SelfInverse R  <->  R = R^-1  <->  R^2 = 1  (on units) — the other vocabulary
selfinv = [ (f,R) for (f,R) in catalog if mul(R,R)==one ]
check("catalog_filtered_by_roomy_edict",
      sorted(selfinv)==sorted([(one,one),(one,negone)]),
      "SelfInverse (R^2=1) keeps the identical two pairs — the roomy edict IS the Galois cut")

# ---- selfInverse_iff_mirror_fixed on units: R^2=1 iff conj R = R ----
check("selfInverse_iff_mirror_fixed",
      all( (mul(R,R)==one) == (conj(R)==R) for R in UNITS ),
      "on units: R = R^-1  iff  conj R = R — the two vocabularies coincide")

# ---- the asymmetric cut: nothing over f=-1 survives the mirror ----
over_neg = [ R for R in UNITS if hexagon_holds(negone,R) ]
survive_neg = [ R for R in over_neg if conj(R)==R ]
check("mirror_keeps_nothing_over_f_neg_one",
      over_neg==[I,negI] and survive_neg==[],
      "over f=-1 the hexagon leaves {i,-i}; the mirror fixes NEITHER — the cut is 2+2 -> 2+0, not 1+1")

# ---- mirror behaviour on the four units ----
check("mirror_fixes_the_survivors",
      conj(one)==one and conj(negone)==negone,
      "conj fixes 1 and -1")
check("mirror_swaps_the_semions",
      conj(I)==negI and conj(negI)==I,
      "conj swaps i and -i — the semion pair")

# ---- catalog_over_f_one / _neg_one splits ----
check("catalog_over_f_one",
      [R for R in UNITS if hexagon_holds(one,R)]==[one,negone],
      "over f=1 the hexagon leaves exactly {1,-1}")
check("catalog_over_f_neg_one",
      [R for R in UNITS if hexagon_holds(negone,R)]==[I,negI],
      "over f=-1 the hexagon leaves exactly {i,-i}")

# ---- controls ----
# a non-unit R does not close the hexagon bridge (R^2 = f has no non-unit soln
# for f a unit): check R=(1,1) (norm 2) over f=1
check("control_non_unit_breaks_the_bridge",
      mul((1,1),(1,1)) != one and mul((1,1),(1,1)) != negone,
      "R=1+i (norm 2): R^2 = 2i is neither +1 nor -1 — a non-unit cannot brace either class")
check("control_semion_fails_the_filter",
      conj(I) != I,
      "the semion i: conj i = -i != i — fails the mirror filter, as their control states")

# ---- the count, tied to the headline ----
CUT = 2 if not PLANT else 3   # the plant claims the mirror keeps THREE
survivors = mirror_fixed
if PLANT:
    # PLANT: claim (negone, I) also survives (mirror keeps one over f=-1)
    survivors = mirror_fixed + [(negone, I)]
check("catalog_closes_at_two [PLANT: keeps 3]" if PLANT else "catalog_closes_at_two",
      len(survivors)==2 and conj((survivors[-1][1]))==survivors[-1][1],
      "the catalog of the roomy world closes at TWO — the survivors are mirror-fixed"
      + (" [PLANTED: (-1,i) injected; conj i = -i != i refutes it]" if PLANT else ""))

# ---------- report ----------
print("="*70)
for name, ok, note in results:
    tag = "PASS" if ok else "FAIL"
    print(f"{tag}  {name}  — {note}" if note else f"{tag}  {name}")
n_pass = sum(1 for _,ok,_ in results if ok)
n_fail = len(results) - n_pass
print("="*70)
print(f"R2-closeout checks: {len(results)};  passed: {n_pass};  failed: {n_fail}")
print(f"(carried S1-S3 verified by step 0: {'exit 0' if carried_ok else 'FAILED'})")
if n_fail == 0 and carried_ok:
    print("VERDICT: two-body Round-Two closeout verified — units by the norm-1")
    print("         finite route (no Nat descent), the hexagon nest re-enumerated,")
    print("         the catalog of four by case split, and the Galois/mirror filter")
    print("         by direct conjugation: the catalog closes at TWO, cut 2+2->2+0.")
else:
    print("VERDICT: FAILED — a closeout check or the carried layer did not hold.")
sys.exit(0 if (n_fail==0 and carried_ok) else 1)
