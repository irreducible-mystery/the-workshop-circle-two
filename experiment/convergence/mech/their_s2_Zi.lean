/-
  Circle Two — S1: the Z[i] ring layer, and S2: the domain.

  The roomy world's catalog is proved over Z[i]; this file builds the ring
  it is proved over, and nothing else. Zero imports: the kernel on `Int`
  alone, no lake, no mathlib, no Std. Toolchain pinned
  leanprover/lean4:v4.32.0 (commit 8c9756b2…, measured by `lean --version`
  on the machine that compiled this file).

  PROVENANCE. Every design fact below is certificate-checked in
  audit/c2_gift_certificates.py; the check name is named at the theorem it
  licenses, per the charge ("verify, then use"). The certificate proves
  these as POLYNOMIAL IDENTITIES over Z — true in every commutative ring —
  and this file proves them again in the kernel, which is the two-body
  standard: an exact reimplementation and a kernel, never one of them.

  STYLE. Hand-rolled, in Circle One's manner: no typeclass instances beyond
  the one disclosed below, no `ring` tactic (there is none without mathlib),
  no `omega` on a conjunctive goal (the Classical.choice trap named in
  Circle One's HANDOFF.md, twice bitten there). The ring identities are
  closed by an associative-commutative `simp` normalisation whose lemmas are
  declared `local simp` ONCE, below — as attributes rather than per-call
  arguments, so that the unused-argument linter has nothing to say and the
  file's silence is earned rather than configured.

  THE AXIOM FOOTPRINT, as measured rather than as hoped (audit/c2_axioms.sh,
  and the per-theorem answers in lean/TRANSCRIPT.txt):
    24 of the 76 theorems depend on NO axioms at all;
    40 depend on `propext` alone;
    12 depend on `propext` and `Quot.sound`, which is the footprint
       `omega` leaves on this toolchain — two of them in S1
       (`brahmagupta_fibonacci`, `norm_mul`) and ten in S2's descent,
       where `omega` does most of the linear work;
     0 depend on `Classical.choice`, and 0 on `sorryAx`.
  Those three add to 76, which is the count of theorems in this file; a
  census whose parts do not sum to its whole is not a census.
  An earlier draft of this header claimed every theorem depended on
  `propext` and nothing else. That was false in both directions — it missed
  the two `Quot.sound` theorems and it missed the axiom-free ones — and it
  contradicted this delivery's own transcript. It was caught by the
  adversarial audit of this file, not by its author; the correction is
  recorded in PROOFS.md, loudest first.

  ONE DISCLOSED INSTANCE. The structure derives `DecidableEq` (core Lean, no
  import), which is what lets the live instances and the controls be settled
  by `decide` — a kernel evaluation. It is a generated typeclass instance,
  and it is flagged here rather than buried; see PROOFS.md, correction #3.

  NORMS in force: no unmarked sorry (there are none of either kind); every
  claim stated once and pointed at (norm 13); anti-vacuity live instances
  with their count (norm 3, section 7); negative controls that actually
  return false (norm 5, section 8); the pass condition is silence.
-/

namespace Zi

/-! ## 0. The carrier, the operations, and the one law -/

/-- A Gaussian integer as an ordered pair of integers: `⟨a, b⟩` is `a + bi`.
    Two coordinates, not four — Z[i] is Z5's little sibling. -/
structure GZ where
  re : Int
  im : Int
deriving DecidableEq

/-- Extensionality, hand-rolled: pairs agree iff their coordinates agree.
    Used everywhere below to split a GZ goal into two Int goals. -/
theorem ext {z w : GZ} (hre : z.re = w.re) (him : z.im = w.im) : z = w := by
  cases z; cases w; simp only [GZ.mk.injEq]; exact ⟨hre, him⟩

/-- The converse direction, so the split is an iff and no goal is lost. -/
theorem ext_iff {z w : GZ} : z = w ↔ z.re = w.re ∧ z.im = w.im := by
  constructor
  · intro h; subst h; exact ⟨rfl, rfl⟩
  · intro h; exact ext h.1 h.2

def zero : GZ := ⟨0, 0⟩
def one : GZ := ⟨1, 0⟩

/-- `i` itself: the pair `(0, 1)`. -/
def I : GZ := ⟨0, 1⟩

def add (z w : GZ) : GZ := ⟨z.re + w.re, z.im + w.im⟩
def neg (z : GZ) : GZ := ⟨-z.re, -z.im⟩
def sub (z w : GZ) : GZ := add z (neg w)

/-- Multiplication forced by `i² = -1` and distributivity, nothing else. -/
def mul (z w : GZ) : GZ := ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩

/-- Conjugation: the sigma of Circle Two. Fixes the first coordinate. -/
def conj (z : GZ) : GZ := ⟨z.re, -z.im⟩

/-- The norm `N(a + bi) = a² + b²`, an integer, not a Gaussian integer. -/
def norm (z : GZ) : Int := z.re * z.re + z.im * z.im

/- The AC normalisation set. Declared once, as local simp attributes: this
   is the whole automation budget of the file, and it is never raised.
   Subtraction becomes addition-of-negation and distributes; then
   associativity and commutativity for the two operations; then the one
   cancellation lemma.

   EVERY LEMMA HERE IS LOAD-BEARING, measured one at a time: removing any
   single one of the eleven makes this file stop compiling. That is not a
   claim about elegance, it is the reason the list is this length and no
   longer. An earlier draft carried nine more — the units and annihilators
   (`Int.add_zero`, `Int.mul_one`, …) and `Int.neg_mul`, `Int.mul_assoc` —
   together with a comment asserting, as "measured", that this toolchain's
   default `simp` does not carry the units for `Int`. That was backwards:
   `a + 0 = a` and `a * 1 = a` ARE closed by a bare `simp` here; what is
   not is `a + -a = 0`, which is why `Int.add_right_neg` stays. The false
   comment and the nine redundant lemmas were found by the adversarial
   audit and removed together; see PROOFS.md, correction #2. -/
attribute [local simp]
  Int.sub_eq_add_neg Int.neg_add Int.mul_add Int.add_mul Int.mul_neg
  Int.mul_comm Int.mul_left_comm
  Int.add_assoc Int.add_comm Int.add_left_comm Int.add_right_neg

/-! ## 1. The additive structure — an abelian group -/

theorem add_comm (z w : GZ) : add z w = add w z := by
  cases z; cases w; simp only [add, GZ.mk.injEq]; constructor <;> simp

theorem add_assoc (x y z : GZ) : add (add x y) z = add x (add y z) := by
  cases x; cases y; cases z; simp only [add, GZ.mk.injEq]; constructor <;> simp

theorem add_zero (z : GZ) : add z zero = z := by
  cases z; simp only [add, zero, GZ.mk.injEq]; constructor <;> simp

theorem zero_add (z : GZ) : add zero z = z := by
  cases z; simp only [add, zero, GZ.mk.injEq]; constructor <;> simp

theorem add_neg (z : GZ) : add z (neg z) = zero := by
  cases z; simp only [add, neg, zero, GZ.mk.injEq]; constructor <;> simp

theorem neg_add (z : GZ) : add (neg z) z = zero := by
  cases z; simp only [add, neg, zero, GZ.mk.injEq]; constructor <;> simp

theorem neg_neg (z : GZ) : neg (neg z) = z := by
  cases z; simp only [neg, GZ.mk.injEq]; constructor <;> simp

theorem sub_self (z : GZ) : sub z z = zero := by
  simp only [sub]; exact add_neg z

/-! ## 2. The multiplicative structure — a commutative monoid

    `G2_ring_laws_symbolic` certifies mul-assoc and mul-comm as polynomial
    identities in six variables; here they are in the kernel. -/

theorem mul_comm (z w : GZ) : mul z w = mul w z := by
  cases z; cases w; simp only [mul, GZ.mk.injEq]; constructor <;> simp

theorem mul_assoc (x y z : GZ) : mul (mul x y) z = mul x (mul y z) := by
  cases x; cases y; cases z; simp only [mul, GZ.mk.injEq]; constructor <;> simp

theorem mul_one (z : GZ) : mul z one = z := by
  cases z; simp only [mul, one, GZ.mk.injEq]; constructor <;> simp

theorem one_mul (z : GZ) : mul one z = z := by
  cases z; simp only [mul, one, GZ.mk.injEq]; constructor <;> simp

theorem mul_zero (z : GZ) : mul z zero = zero := by
  cases z; simp only [mul, zero, GZ.mk.injEq]; constructor <;> simp

theorem zero_mul (z : GZ) : mul zero z = zero := by
  cases z; simp only [mul, zero, GZ.mk.injEq]; constructor <;> simp

/-! ## 3. Distributivity — the ring closes

    `G2_ring_laws_symbolic`'s third conjunct certifies **left**
    distributivity only — `U·(V+W) = U·V + U·W` — and nothing else in this
    section. `right_distrib`, `mul_neg` and `neg_mul` have no certificate
    counterpart; they are proved here and licensed by nothing but the
    kernel, which is stated rather than left for a reader to discover. An
    earlier version of this comment credited the one conjunct with all four
    theorems: the same miscitation species the S1 audit convicted in the
    additive family, standing one section over from its own conviction, and
    caught by the builder's pass rather than mine.

    Both distributive laws are proved outright; the right-hand one is NOT
    inferred from commutativity by hand-wave, because a reader who trusts
    one inference will trust the next one. -/

theorem left_distrib (x y z : GZ) : mul x (add y z) = add (mul x y) (mul x z) := by
  cases x; cases y; cases z; simp only [mul, add, GZ.mk.injEq]; constructor <;> simp

theorem right_distrib (x y z : GZ) : mul (add x y) z = add (mul x z) (mul y z) := by
  cases x; cases y; cases z; simp only [mul, add, GZ.mk.injEq]; constructor <;> simp

theorem mul_neg (z w : GZ) : mul z (neg w) = neg (mul z w) := by
  cases z; cases w; simp only [mul, neg, GZ.mk.injEq]; constructor <;> simp

theorem neg_mul (z w : GZ) : mul (neg z) w = neg (mul z w) := by
  cases z; cases w; simp only [mul, neg, GZ.mk.injEq]; constructor <;> simp

/-! ## 4. The one law: `i² = -1`

    `G2_i_squared_is_minus_one`: `(0,1)² = (-1,0)`. Everything above is the
    ring; this is the only thing that makes it Z[i] rather than Z[x]. -/

theorem I_squared : mul I I = neg one := by
  simp only [mul, I, neg, one, GZ.mk.injEq]; constructor <;> simp

/-- The same law read as the defining property: `i² + 1 = 0`. -/
theorem I_squared_add_one : add (mul I I) one = zero := by
  simp only [mul, I, add, one, zero, GZ.mk.injEq]; constructor <;> simp

/-! ## 5. Conjugation is a ring homomorphism

    `G2_conj_is_a_ring_hom_symbolic` certifies exactly two things: that
    conjugation is multiplicative and that it is additive. Those are the
    two conjuncts of its tested boolean. The involution — `conj (conj z) =
    z` — appears only in that check's printed message, where it is called
    "trivial"; a printed string is not a check, so `conj_conj` below is
    licensed by the kernel alone. Same for `conj_re` and `conj_I`. An
    earlier version of this comment credited the check with the involution
    too. It fixes the first coordinate — that is what makes it the mirror
    rather than an arbitrary automorphism. -/

theorem conj_add (z w : GZ) : conj (add z w) = add (conj z) (conj w) := by
  cases z; cases w; simp only [conj, add, GZ.mk.injEq]; constructor <;> simp

theorem conj_mul (z w : GZ) : conj (mul z w) = mul (conj z) (conj w) := by
  cases z; cases w; simp only [conj, mul, GZ.mk.injEq]; constructor <;> simp

theorem conj_conj (z : GZ) : conj (conj z) = z := by
  cases z; simp only [conj, GZ.mk.injEq]; constructor <;> simp

theorem conj_one : conj one = one := by
  simp only [conj, one, GZ.mk.injEq]; constructor <;> simp

theorem conj_zero : conj zero = zero := by
  simp only [conj, zero, GZ.mk.injEq]; constructor <;> simp

/-- Conjugation fixes the first coordinate, stated as the coordinate fact. -/
theorem conj_re (z : GZ) : (conj z).re = z.re := rfl

/-- And it is the mirror on the second: `conj i = -i`. -/
theorem conj_I : conj I = neg I := by
  simp only [conj, I, neg, GZ.mk.injEq]; constructor <;> simp

/-! ## 6. The norm — and why the descent will have an engine

    `G2_z_times_conj_is_norm_symbolic`: `z · conj z = (N(z), 0)`, the norm
    as a ring element. `G2_brahmagupta_fibonacci_symbolic`: N is
    multiplicative, i.e. `(a²+b²)(c²+d²) = (ac−bd)² + (ad+bc)²` — the
    Brahmagupta–Fibonacci identity, here as a ring identity, not a
    numerical check. -/

theorem mul_conj (z : GZ) : mul z (conj z) = ⟨norm z, 0⟩ := by
  cases z; simp only [mul, conj, norm, GZ.mk.injEq]; constructor <;> simp

theorem conj_mul_self (z : GZ) : mul (conj z) z = ⟨norm z, 0⟩ := by
  cases z; simp only [mul, conj, norm, GZ.mk.injEq]; constructor <;> simp

/-- Brahmagupta–Fibonacci as the bare integer identity, in exactly the form
    the certificate states it:
    `(a²+b²)(c²+d²) = (ac−bd)² + (ad+bc)²`. Proved by AC-normalising both
    sides and then closing the resulting LINEAR relation among monomials
    with `omega` — on a single goal, never a conjunctive one. That
    restriction is not decoration: an `omega` aimed at a conjunctive goal is
    the `Classical.choice` trap Circle One's HANDOFF.md records being bitten
    by twice, and this file's census shows it was not bitten a third time. -/
theorem brahmagupta_fibonacci (a b c d : Int) :
    (a * a + b * b) * (c * c + d * d)
      = (a * c - b * d) * (a * c - b * d) + (a * d + b * c) * (a * d + b * c) := by
  simp
  omega

/-- Brahmagupta–Fibonacci as the statement about this ring: N is multiplicative. -/
theorem norm_mul (z w : GZ) : norm (mul z w) = norm z * norm w := by
  cases z; cases w; simp only [norm, mul]; simp; omega

theorem norm_conj (z : GZ) : norm (conj z) = norm z := by
  cases z; simp only [norm, conj]; simp

theorem norm_one : norm one = 1 := by
  simp only [norm, one]; simp

theorem norm_zero : norm zero = 0 := by
  simp only [norm, zero]; simp

theorem norm_I : norm I = 1 := by
  simp only [norm, I]; simp

/-- The norm of a real element is its square — the bridge S2 will descend on. -/
theorem norm_re (a : Int) : norm ⟨a, 0⟩ = a * a := by
  simp only [norm]; simp

/-! ## 7. Anti-vacuity — norm 3

    Exactly ONE theorem above is guarded by hypotheses — `ext`, which takes
    the two coordinate equations — and its guard is satisfiable (take
    z = w), so it is not vacuous either; every other theorem binds data,
    not proofs. An earlier draft opened "Nothing above is guarded by a
    hypothesis", which `ext` falsifies. The audit caught it; the conclusion
    survived the correction, which is why it is recorded quietly. The live
    risk here is the other one — that the definitions do not compute what
    the prose says. These are the live instances, and the count is stated:
    EIGHT witnesses, each an exact evaluation in the kernel, and none of
    them a restatement of a theorem proved above. That last clause was
    FALSE when first written: `live_1` used to assert `mul I I = (-1,0)`,
    which is `I_squared`'s statement definitionally — a probe file proves
    the old `live_1` with `I_squared`'s proof term verbatim, exit 0. The
    builder's pass caught it; the witness is now `(3+i)(2-5i) = 11-13i`,
    an evaluation no theorem here already proves. -/

theorem live_1 : mul ⟨3, 1⟩ ⟨2, -5⟩ = ⟨11, -13⟩ := by decide
theorem live_2 : mul ⟨1, 1⟩ ⟨1, -1⟩ = ⟨2, 0⟩ := by decide
theorem live_3 : norm ⟨3, 4⟩ = 25 := by decide
theorem live_4 : norm ⟨1, 1⟩ * norm ⟨1, -1⟩ = norm (mul ⟨1, 1⟩ ⟨1, -1⟩) := by decide
theorem live_5 : conj ⟨5, -7⟩ = ⟨5, 7⟩ := by decide
theorem live_6 : mul ⟨2, 3⟩ (conj ⟨2, 3⟩) = ⟨13, 0⟩ := by decide
theorem live_7 : add ⟨2, 3⟩ (neg ⟨2, 3⟩) = zero := by decide
theorem live_8 : mul ⟨0, 2⟩ ⟨0, 3⟩ = ⟨-6, 0⟩ := by decide

/-! ## 8. Negative controls — norm 5

    A control earns its name by ruling something out. Six of the eight
    below do that directly — they assert that a near-miss FAILS, and the
    kernel agrees. The other two are the near-miss's credentials:
    `control_fake_mirror_is_additive` is a universally quantified TRUE
    property, and its job is to prove the fake mirror is a genuine
    candidate rather than a straw man, so that its failure of
    multiplicativity means something. An earlier version of this sentence
    said each control "is FALSE of some near-miss", which misdescribed
    that one; the builder's pass caught it. The sentence is fixed, not the
    control. A check that cannot fail is not a check. EIGHT control theorems across FOUR
    families — the ring's non-triviality (one), the mirror's non-triviality
    (one), the fake mirror that is additive yet not multiplicative
    (`G4_control_fake_mirror_fails`, two), and the sign in `i² = -1` shown
    to be load-bearing (four). An earlier draft's comment said "Four
    controls, one per family", counting the families and calling them
    theorems; the audit caught the arithmetic. -/

/-- The ring is not the zero ring: the two-particle catalog has room to live. -/
theorem control_one_ne_zero : one ≠ zero := by decide

/-- Conjugation is not the identity map — the mirror is a real involution. -/
theorem control_conj_ne_id : conj I ≠ I := by decide

/-- `G4_control_fake_mirror_fails`, in the kernel. The near-miss
    `(a,b) ↦ (a, 2b)` is additive and fixes the first coordinate, so it
    looks like a mirror — and it is not multiplicative. Witness below. -/
def fakeMirror (z : GZ) : GZ := ⟨z.re, 2 * z.im⟩

theorem control_fake_mirror_is_additive (z w : GZ) :
    fakeMirror (add z w) = add (fakeMirror z) (fakeMirror w) := by
  cases z; cases w; simp only [fakeMirror, add, GZ.mk.injEq]; constructor <;> simp

theorem control_fake_mirror_fails_multiplicative :
    fakeMirror (mul I I) ≠ mul (fakeMirror I) (fakeMirror I) := by decide

/-- The sign is load-bearing. With `i² = +1` instead — the split-complex
    multiplication — the ring acquires zero divisors, so the domain result
    S2 is charged to prove is a statement about the SIGN, not about pairs
    of integers. This control is why `no_zero_divisors` is not free. -/
def splitMul (z w : GZ) : GZ := ⟨z.re * w.re + z.im * w.im, z.re * w.im + z.im * w.re⟩

theorem control_split_has_zero_divisors :
    splitMul ⟨1, 1⟩ ⟨1, -1⟩ = zero := by decide

/-- BOTH factors, separately. The claim "the ring acquires zero divisors"
    needs two non-zero factors with a zero product, and an earlier draft
    proved only the first while its name and its prose said "factors".
    Half a control is not a control; the audit caught it, and here is the
    other half. -/
theorem control_split_first_factor_is_nonzero :
    (⟨1, 1⟩ : GZ) ≠ zero := by decide

theorem control_split_second_factor_is_nonzero :
    (⟨1, -1⟩ : GZ) ≠ zero := by decide

/-- And the honest contrast, in the real ring: the same two factors that
    kill each other under `splitMul` have product `(2,0)` under `mul`. The
    two multiplications differ exactly where the sign does. -/
theorem control_mul_of_same_factors_is_nonzero :
    mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ zero := by decide

/-! ## 9. S2 — THE DOMAIN, BY ONE MOD-4 DESCENT

    Charged in `ROUND1.md` and approved in the builder's S1 verification:
    the order-free route. The whole argument is four moves — squares mod 4
    are exactly {0,1}; a norm divisible by 4 forces both coordinates even;
    halving strictly shrinks a Nat measure, so `N(z) = 0` forces `z = 0`;
    and then the chain `z·w = 0 ⟹ conj(z)·z·w = 0 ⟹ (N(z),0)·w = 0 ⟹
    w = 0`.

    THE FORK, labelled rather than silent (the charge asks for this
    explicitly). Lean's `Int` carries an order, and with it the domain is
    three lines: `a*a ≥ 0`, `b*b ≥ 0`, a sum of two non-negatives is zero
    only if both are, done. **That route is not taken here.** The descent
    is taken instead because it is the pattern Circle One's 2-adic argument
    established, and because an argument that never mentions an order
    survives transport to settings that have none — which is worth more to
    S5–S7 than the saved lines. The order route is not wrong; it is not
    this proof.

    NO NEW AXIOMS ARE INTRODUCED: `omega` appears only on goals that are
    linear in their atoms, and never on a conjunctive goal — every
    conjunction below is split first, and the census is the receipt. -/

/-- `a·a mod 4` is `0` or `1`, never `2` or `3`. Certificate:
    `G2_squares_mod_4`, nest 4 = |Z/4|. Proved by reducing the square to
    the square of the residue (`Int.mul_emod`), so nothing nonlinear is
    ever reasoned about — the four residues are then decided. -/
theorem sq_mod_four (a : Int) : a * a % 4 = 0 ∨ a * a % 4 = 1 := by
  have hm : a * a % 4 = (a % 4) * (a % 4) % 4 := Int.mul_emod a a 4
  rcases (by omega : a % 4 = 0 ∨ a % 4 = 1 ∨ a % 4 = 2 ∨ a % 4 = 3) with h|h|h|h <;>
    rw [hm, h] <;> decide

theorem sq_mod_four_zero_of_even (a : Int) (h : a % 2 = 0) : a * a % 4 = 0 := by
  have hm : a * a % 4 = (a % 4) * (a % 4) % 4 := Int.mul_emod a a 4
  rcases (by omega : a % 4 = 0 ∨ a % 4 = 2) with h4|h4 <;> rw [hm, h4] <;> decide

theorem sq_mod_four_one_of_odd (a : Int) (h : a % 2 = 1) : a * a % 4 = 1 := by
  have hm : a * a % 4 = (a % 4) * (a % 4) % 4 := Int.mul_emod a a 4
  rcases (by omega : a % 4 = 1 ∨ a % 4 = 3) with h4|h4 <;> rw [hm, h4] <;> decide

/-! ### The sixteen cases, as two split theorems

    Certificate: `G2_16_case_decide`, nest 16 = |(Z/4)²| — of the sixteen
    residue pairs exactly four have `a² + b² ≡ 0 (mod 4)`, and those four
    are precisely the ones with both coordinates even; twelve fail. The two
    conclusions are proved as SEPARATE theorems rather than one conjunction,
    because a conjunctive goal handed to `omega` is the trap this house has
    been bitten by twice. -/

theorem re_even_of_norm_mod_four (a b : Int) (h : (a * a + b * b) % 4 = 0) :
    a % 2 = 0 := by
  rcases (by omega : a % 2 = 0 ∨ a % 2 = 1) with ha | ha
  · exact ha
  · have h1 : a * a % 4 = 1 := sq_mod_four_one_of_odd a ha
    rcases (by omega : b % 2 = 0 ∨ b % 2 = 1) with hb | hb
    · have h2 : b * b % 4 = 0 := sq_mod_four_zero_of_even b hb
      omega
    · have h2 : b * b % 4 = 1 := sq_mod_four_one_of_odd b hb
      omega

theorem im_even_of_norm_mod_four (a b : Int) (h : (a * a + b * b) % 4 = 0) :
    b % 2 = 0 := by
  refine re_even_of_norm_mod_four b a ?_
  omega

/-- **The mandatory negative control** (`G2_control_mod2_insufficient`), and
    the reason the modulus is 4 rather than 2: the mod-2 analogue is FALSE.
    `(1,1)` has norm `2 ≡ 0 (mod 2)` while both coordinates are odd, so a
    mod-2 descent would halt at its first step. Two ramifies in Z[i]
    (`2 = -i(1+i)²`); the modulus 4 is load-bearing, and here is the
    witness that says so. -/
theorem control_mod_two_insufficient :
    (1 * 1 + 1 * 1) % 2 = 0 ∧ (1 : Int) % 2 ≠ 0 := by
  constructor
  · decide
  · decide

/-- And the contrast at the working modulus: the same pair fails mod 4, which
    is exactly why the descent makes progress where a mod-2 version cannot. -/
theorem control_mod_four_rejects_odd_pair : (1 * 1 + 1 * 1) % 4 ≠ 0 := by decide

/-! ### The descent

    Halving a nonzero even integer strictly shrinks `Int.natAbs`, so the
    descent terminates. The measure is a `Nat` bound carried as an explicit
    induction parameter — ordinary structural induction on `Nat`, not
    well-founded recursion, which keeps the proof term small and the tactic
    budget unraised. Certificate: `G2_descent_step_strictly_decreases`,
    `G2_norm_zero_forces_zero`. -/

/-- Halving quarters the norm: the algebraic step the descent runs on. -/
theorem norm_quarters (a b : Int) :
    2 * a * (2 * a) + 2 * b * (2 * b) = 4 * (a * a + b * b) := by
  simp [Int.add_mul, Int.mul_assoc, Int.mul_comm, Int.mul_left_comm]

theorem natAbs_two_mul (k : Int) : (2 * k).natAbs = 2 * k.natAbs := by
  rw [Int.natAbs_mul]; rfl

/-- The descent proper, stated on a `Nat` bound so the induction is
    structural. The conclusion is the MEASURE being zero rather than a
    conjunction `a = 0 ∧ b = 0`, so that no `omega` in this proof ever sees
    a conjunctive goal. -/
theorem descent_bound : ∀ n : Nat, ∀ a b : Int,
    a.natAbs + b.natAbs ≤ n → a * a + b * b = 0 → a.natAbs + b.natAbs = 0 := by
  intro n
  induction n with
  | zero => intro a b h _; omega
  | succ m ih =>
    intro a b hle hz
    have h4 : (a * a + b * b) % 4 = 0 := by omega
    have hae : a % 2 = 0 := re_even_of_norm_mod_four a b h4
    have hbe : b % 2 = 0 := im_even_of_norm_mod_four a b h4
    obtain ⟨a', ha'⟩ : ∃ k, a = 2 * k := ⟨a / 2, by omega⟩
    obtain ⟨b', hb'⟩ : ∃ k, b = 2 * k := ⟨b / 2, by omega⟩
    subst ha'; subst hb'
    have hq := norm_quarters a' b'
    have hz' : a' * a' + b' * b' = 0 := by omega
    have hna := natAbs_two_mul a'
    have hnb := natAbs_two_mul b'
    have hle' : a'.natAbs + b'.natAbs ≤ m := by omega
    have hih := ih a' b' hle' hz'
    omega

/-- `N(z) = 0` forces `z = 0`. The two coordinates are concluded
    separately and reassembled by `ext`. -/
theorem norm_zero_forces_zero (z : GZ) (h : norm z = 0) : z = zero := by
  have hb := descent_bound (z.re.natAbs + z.im.natAbs) z.re z.im (by omega) (by
    simpa only [norm] using h)
  refine ext ?_ ?_
  · simp only [zero]; omega
  · simp only [zero]; omega

/-- The contrapositive, in the form the chain consumes. -/
theorem norm_ne_zero_of_ne_zero (z : GZ) (h : z ≠ zero) : norm z ≠ 0 := by
  intro hn
  exact h (norm_zero_forces_zero z hn)

/-! ### Torsion-freeness, and the scalar action

    Certificate: `G2_torsion_free` — `n·w = 0` with `n ≠ 0` forces `w = 0`,
    coordinatewise, because Z is a domain; and the scalar action IS
    multiplication by `(n, 0)`. -/

theorem scalar_is_mul (n : Int) (w : GZ) :
    mul ⟨n, 0⟩ w = ⟨n * w.re, n * w.im⟩ := by
  cases w; simp only [mul, GZ.mk.injEq]; constructor <;> simp

theorem torsion_free (n : Int) (w : GZ) (hn : n ≠ 0) (h : mul ⟨n, 0⟩ w = zero) :
    w = zero := by
  rw [scalar_is_mul] at h
  have hre : n * w.re = 0 := congrArg GZ.re h
  have him : n * w.im = 0 := congrArg GZ.im h
  refine ext ?_ ?_
  · simp only [zero]
    rcases Int.mul_eq_zero.mp hre with h1 | h1
    · exact absurd h1 hn
    · exact h1
  · simp only [zero]
    rcases Int.mul_eq_zero.mp him with h1 | h1
    · exact absurd h1 hn
    · exact h1

/-! ### The chain — Z[i] is a domain

    Certificate: `G2_no_zero_divisors_box`, and the chain it names, each
    link proved above:
      `z·w = 0  ⟹  conj(z)·(z·w) = 0  ⟹  (N(z),0)·w = 0  ⟹  w = 0`. -/

theorem no_zero_divisors (z w : GZ) (hz : z ≠ zero) (h : mul z w = zero) :
    w = zero := by
  have step : mul ⟨norm z, 0⟩ w = zero := by
    have e : mul ⟨norm z, 0⟩ w = mul (conj z) (mul z w) := by
      rw [← conj_mul_self z, mul_assoc]
    rw [e, h, mul_zero]
  exact torsion_free (norm z) w (norm_ne_zero_of_ne_zero z hz) step

/-- The same fact in the shape the exactly-two argument will use: a product
    is zero only if a factor is. Stated as a disjunction, never proved by an
    `omega` on a conjunction. -/
theorem mul_eq_zero_iff (z w : GZ) : mul z w = zero ↔ z = zero ∨ w = zero := by
  constructor
  · intro h
    rcases (by exact Decidable.em (z = zero)) with hz | hz
    · exact Or.inl hz
    · exact Or.inr (no_zero_divisors z w hz h)
  · intro h
    rcases h with h | h
    · rw [h]; exact zero_mul w
    · rw [h]; exact mul_zero z

/-! ### S2's own live instances and controls -/

theorem live_9 : norm ⟨0, 0⟩ = 0 := by decide
theorem live_10 : (5 * 5 + 3 * 3) % 4 ≠ 0 := by decide
theorem live_11 : (6 * 6 + 2 * 2) % 4 = 0 := by decide
theorem live_12 : mul ⟨2, 3⟩ ⟨1, -1⟩ ≠ zero := by decide

/-- Negative control for the descent's engine: a norm that is `0 mod 4`
    does NOT make the element zero — the descent needs the full equation
    `N(z) = 0`, not a congruence. Without this the reader might think
    divisibility alone was doing the work. -/
theorem control_norm_mod_four_is_not_norm_zero :
    (6 * 6 + 2 * 2) % 4 = 0 ∧ (6 * 6 + 2 * 2 : Int) ≠ 0 := by
  constructor
  · decide
  · decide

/-- Negative control for the domain: in the SPLIT ring (`i² = +1`) the same
    chain fails at its first link, because there `conj(z)·z` is not the norm.
    `(1,1)` is non-zero and `splitMul (1,1) (1,-1) = 0`, so `no_zero_divisors`
    is false of `splitMul` — the theorem above is about `mul`, and the sign
    is what makes it true. -/
theorem control_split_is_not_a_domain :
    splitMul ⟨1, 1⟩ ⟨1, -1⟩ = zero := by decide

end Zi
