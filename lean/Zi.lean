/-
  Circle Two — S1: the Z[i] ring layer.

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

  STYLE. Hand-rolled, in Circle One's manner: no typeclass instances, no
  `ring` tactic (there is none without mathlib), no `omega` on a conjunctive
  goal (the Classical.choice trap named in Circle One's HANDOFF.md, twice
  bitten there). The ring identities are closed by an associative-
  commutative `simp` normalisation whose lemmas are declared `local simp`
  ONCE, below — as attributes rather than per-call arguments, so that the
  unused-argument linter has nothing to say and the file's silence is
  earned rather than configured. Measured consequence: every theorem here
  depends on `propext` and nothing else — no `Classical.choice`, no
  `Quot.sound`, no `sorryAx`. The census is audit/c2_axioms.sh.

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
   is the whole automation budget of the file, and it is never raised. The
   first line turns subtraction into addition-of-negation and distributes;
   the second and third are associativity/commutativity for the two
   operations; the fourth supplies the units and annihilators, which this
   toolchain's default simp set does NOT carry for `Int` (measured: `a + 0
   = a` is not closed by a bare `simp` here). -/
attribute [local simp]
  Int.sub_eq_add_neg Int.neg_add Int.mul_add Int.add_mul Int.mul_neg Int.neg_mul
  Int.mul_assoc Int.mul_comm Int.mul_left_comm
  Int.add_assoc Int.add_comm Int.add_left_comm
  Int.add_zero Int.zero_add Int.mul_one Int.one_mul Int.mul_zero Int.zero_mul
  Int.neg_zero Int.add_right_neg Int.neg_neg

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

    `G2_ring_laws_symbolic`, third conjunct. Both sides are proved; the
    right-distributive law is NOT inferred from commutativity by hand-wave,
    it is proved, because a reader who trusts one inference will trust the
    next one. -/

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

    `G2_conj_is_a_ring_hom_symbolic`: additive and multiplicative, and an
    involution. It fixes the first coordinate — that is what makes it the
    mirror rather than an arbitrary automorphism. -/

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

    Nothing above is guarded by a hypothesis, so nothing above can be
    vacuously true; the risk here is the other one — that the definitions
    do not compute what the prose says. These are the live instances, and
    the count is stated: EIGHT witnesses, each an exact evaluation in the
    kernel, none of them a rewriting of the theorems they witness. -/

theorem live_1 : mul I I = ⟨-1, 0⟩ := by decide
theorem live_2 : mul ⟨1, 1⟩ ⟨1, -1⟩ = ⟨2, 0⟩ := by decide
theorem live_3 : norm ⟨3, 4⟩ = 25 := by decide
theorem live_4 : norm ⟨1, 1⟩ * norm ⟨1, -1⟩ = norm (mul ⟨1, 1⟩ ⟨1, -1⟩) := by decide
theorem live_5 : conj ⟨5, -7⟩ = ⟨5, 7⟩ := by decide
theorem live_6 : mul ⟨2, 3⟩ (conj ⟨2, 3⟩) = ⟨13, 0⟩ := by decide
theorem live_7 : add ⟨2, 3⟩ (neg ⟨2, 3⟩) = zero := by decide
theorem live_8 : mul ⟨0, 2⟩ ⟨0, 3⟩ = ⟨-6, 0⟩ := by decide

/-! ## 8. Negative controls — norm 5

    Each of these is FALSE of some near-miss and the kernel says so; a check
    that cannot fail is not a check. Four controls, one per family: the
    ring's non-triviality, the mirror's non-triviality, a fake mirror that
    breaks multiplicativity (`G4_control_fake_mirror_fails`), and the sign
    in `i² = -1` shown to be load-bearing. -/

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

theorem control_split_factors_are_nonzero :
    (⟨1, 1⟩ : GZ) ≠ zero := by decide

/-- And the honest contrast, in the real ring: the same two factors that
    kill each other under `splitMul` have product `(2,0)` under `mul`. The
    two multiplications differ exactly where the sign does. -/
theorem control_mul_of_same_factors_is_nonzero :
    mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ zero := by decide

end Zi
