/-
  Zi.lean — CIRCLE TWO, S1: the Z[i] ring layer.

  EXPERIMENT ARTICLE — single-architecture dual-seat trial (SuperNinja),
  quarantined per norm 16 and REGISTER row 7. NOT a two-body deliverable:
  the kernel check below is real; the independent reimplementation is by
  the builder-seat of the same architecture (seat separation by session
  and tree, labeled honestly). This file enters the record as a claim.

  Charge: ROUND1.md §S1 (~35 thm). Z[i] as integer pairs, one law
  i² = −1 (certificate G2_i_squared_is_minus_one); commutative-ring laws
  hand-rolled, zero imports, Circle One's style (Z5's little sibling —
  Anyon.lean:677-713 is the pattern); conj a ring hom fixing the first
  coordinate (G2_conj_is_a_ring_hom_symbolic); z·conj(z) = (N(z), 0)
  (G2_z_times_conj_is_norm_symbolic); N multiplicative via
  Brahmagupta–Fibonacci as a ring identity
  (G2_brahmagupta_fibonacci_symbolic).

  Index conventions, sourced per C1's lesson: Zi ⟨re, im⟩ represents
  re + im·i; mul ⟨a,b⟩ ⟨c,d⟩ = ⟨a·c − b·d, a·d + b·c⟩ — matching the
  bench's complex arithmetic in floor/symmetric_statistics.py (native
  complex; the certificate's Z[i] layer in audit/c2_gift_certificates.py
  G2 block is the exact source).

  Norms: zero imports (norm 2); no unmarked sorry (norm 1); anti-vacuity
  live instances (norm 3); negative controls (norm 5); honest labels
  (norm 6); pass condition silence — exit 0 AND zero bytes (norm 10).

  Guardrails honored (HANDOFF.md): conjunctive goals split with
  refine ⟨?_, ?_⟩ BEFORE omega (the Classical.choice trap); no budget
  raises; the simp-only-distribute-then-omega pattern throughout.

  Toolchain: leanprover/lean4:v4.32.0 (pinned, matching lean-toolchain).
-/

structure Zi where
  re : Int
  im : Int
deriving DecidableEq

namespace Zi

/-- 0 = ⟨0, 0⟩ -/
def zero : Zi := ⟨0, 0⟩
/-- 1 = ⟨1, 0⟩ -/
def one : Zi := ⟨1, 0⟩
/-- i = ⟨0, 1⟩ — the imaginary unit, the one new law's carrier -/
def I : Zi := ⟨0, 1⟩
/-- componentwise addition -/
def add (z w : Zi) : Zi := ⟨z.re + w.re, z.im + w.im⟩
/-- multiplication with i² = −1 folded in: ⟨a,b⟩·⟨c,d⟩ = ⟨ac−bd, ad+bc⟩ -/
def mul (z w : Zi) : Zi := ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩
/-- additive inverse -/
def neg (z : Zi) : Zi := ⟨-z.re, -z.im⟩
/-- subtraction, as add-neg -/
def sub (z w : Zi) : Zi := add z (neg w)
/-- conjugation: i ↦ −i, fixing the first coordinate — this circle's σ -/
def conj (z : Zi) : Zi := ⟨z.re, -z.im⟩
/-- the norm N(a+bi) = a² + b², landing in Int -/
def normSq (z : Zi) : Int := z.re * z.re + z.im * z.im

/-- NEGATIVE-CONTROL apparatus: the fake mirror (a,b) ↦ (a,2b) — the
    certificate's ready-made control (G4_control_fake_mirror_fails) -/
def fakeMirror (z : Zi) : Zi := ⟨z.re, 2 * z.im⟩
/-- NEGATIVE-CONTROL apparatus: coordinatewise product — what mul would
    be WITHOUT the i² = −1 law -/
def coordMul (z w : Zi) : Zi := ⟨z.re * w.re, z.im * w.im⟩

/- == the additive laws ================================================= -/

theorem add_comm (z w : Zi) : add z w = add w z := by
  cases z; cases w
  simp only [add, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem add_assoc (z w v : Zi) : add (add z w) v = add z (add w v) := by
  cases z; cases w; cases v
  simp only [add, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem zero_add (z : Zi) : add zero z = z := by
  cases z
  simp only [add, zero, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem add_zero (z : Zi) : add z zero = z := by
  cases z
  simp only [add, zero, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem add_neg (z : Zi) : add z (neg z) = zero := by
  cases z
  simp only [add, neg, zero, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem neg_add (z : Zi) : add (neg z) z = zero := by
  cases z
  simp only [add, neg, zero, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

/-- sub really is subtraction: (z − w) + w = z — an independent
    characterization, NOT the definition restated. Replaces the vacuous
    `sub_eq_add_neg` (seat B crop #1, norm 7: the original was `rfl` on
    the definition and could never fail). -/
theorem sub_add_cancel (z w : Zi) : add (sub z w) w = z := by
  cases z; cases w
  simp only [sub, add, neg, Zi.mk.injEq]
  exact ⟨by omega, by omega⟩

/- == the multiplicative laws =========================================== -/

theorem mul_comm (z w : Zi) : mul z w = mul w z := by
  cases z; cases w
  simp only [mul, Zi.mk.injEq, Int.mul_comm]
  exact ⟨trivial, Int.add_comm _ _⟩

theorem mul_assoc (z w v : Zi) : mul (mul z w) v = mul z (mul w v) := by
  cases z; cases w; cases v
  simp only [mul, Zi.mk.injEq, Int.sub_mul, Int.mul_sub, Int.add_mul,
             Int.mul_add, Int.mul_assoc]
  refine ⟨?_, ?_⟩ <;> omega

theorem one_mul (z : Zi) : mul one z = z := by
  cases z
  simp only [mul, one, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem mul_one (z : Zi) : mul z one = z := by
  cases z
  simp only [mul, one, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem zero_mul (z : Zi) : mul zero z = zero := by
  cases z
  simp only [mul, zero, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem mul_zero (z : Zi) : mul z zero = zero := by
  cases z
  simp only [mul, zero, Zi.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

theorem mul_add (z w v : Zi) : mul z (add w v) = add (mul z w) (mul z v) := by
  cases z; cases w; cases v
  simp only [mul, add, Zi.mk.injEq, Int.mul_add]
  refine ⟨?_, ?_⟩ <;> omega

theorem add_mul (z w v : Zi) : mul (add z w) v = add (mul z v) (mul w v) := by
  cases z; cases w; cases v
  simp only [mul, add, Zi.mk.injEq, Int.add_mul]
  refine ⟨?_, ?_⟩ <;> omega

theorem neg_mul (z w : Zi) : mul (neg z) w = neg (mul z w) := by
  cases z; cases w
  simp only [mul, neg, Zi.mk.injEq, Int.neg_mul]
  refine ⟨?_, ?_⟩ <;> omega

theorem mul_neg (z w : Zi) : mul z (neg w) = neg (mul z w) := by
  cases z; cases w
  simp only [mul, neg, Zi.mk.injEq, Int.mul_neg]
  refine ⟨?_, ?_⟩ <;> omega

/- == the one new law =================================================== -/

/-- i² = −1 — the single law that makes Zi the Gaussian integers
    (certificate: G2_i_squared_is_minus_one) -/
theorem i_squared_is_minus_one : mul I I = neg one := by decide

/- == conj is a ring hom fixing the first coordinate ==================== -/

theorem conj_add (z w : Zi) : conj (add z w) = add (conj z) (conj w) := by
  cases z; cases w
  simp only [conj, add, Zi.mk.injEq]
  exact ⟨trivial, by omega⟩

theorem conj_mul (z w : Zi) : conj (mul z w) = mul (conj z) (conj w) := by
  cases z; cases w
  simp only [conj, mul, Int.neg_mul, Int.mul_neg, Int.neg_neg, Int.neg_add]

theorem conj_zero : conj zero = zero := rfl

theorem conj_one : conj one = one := rfl

theorem conj_conj (z : Zi) : conj (conj z) = z := by
  cases z
  simp only [conj, Int.neg_neg]

/-- conj is i ↦ −i -/
theorem conj_I : conj I = neg I := rfl

/-- conj fixes the real line pointwise — "fixing the first coordinate" -/
theorem conj_fixes_real (a : Int) : conj ⟨a, 0⟩ = ⟨a, 0⟩ := rfl

/-- an element fixed by conj is real: the fixed field of σ is Z -/
theorem conj_fixed_iff_real (z : Zi) : conj z = z ↔ z.im = 0 := by
  cases z
  simp only [conj, Zi.mk.injEq]
  constructor
  · intro h
    omega
  · intro h
    exact ⟨trivial, by omega⟩

/- == the norm ========================================================== -/

/-- z · conj(z) = (N(z), 0) — the norm as a ring computation
    (certificate: G2_z_times_conj_is_norm_symbolic) -/
theorem mul_conj_eq_normSq (z : Zi) : mul z (conj z) = ⟨normSq z, 0⟩ := by
  cases z
  simp only [mul, conj, normSq, Zi.mk.injEq, Int.mul_neg, Int.mul_comm]
  refine ⟨?_, ?_⟩ <;> omega

/-- conj(z) · z = (N(z), 0) — the mirror-side reading, via mul_comm -/
theorem conj_mul_eq_normSq (z : Zi) : mul (conj z) z = ⟨normSq z, 0⟩ := by
  rw [mul_comm]
  exact mul_conj_eq_normSq z

/-- the raw Brahmagupta–Fibonacci identity over Int:
    (ac−bd)² + (ad+bc)² = (a²+b²)(c²+d²) -/
theorem brahmagupta_fibonacci_int (a b c d : Int) :
    (a*c - b*d)*(a*c - b*d) + (a*d + b*c)*(a*d + b*c)
      = (a*a + b*b)*(c*c + d*d) := by
  simp only [Int.mul_sub, Int.mul_add,
             Int.mul_comm, Int.mul_left_comm]
  omega

/-- N is multiplicative: N(z·w) = N(z)·N(w) — Brahmagupta–Fibonacci as a
    ring identity (certificate: G2_brahmagupta_fibonacci_symbolic) -/
theorem normSq_mul (z w : Zi) : normSq (mul z w) = normSq z * normSq w := by
  cases z; cases w
  simp only [normSq, mul]
  exact brahmagupta_fibonacci_int _ _ _ _

theorem normSq_zero : normSq zero = 0 := rfl

theorem normSq_one : normSq one = 1 := rfl

theorem normSq_I : normSq I = 1 := rfl

theorem normSq_conj (z : Zi) : normSq (conj z) = normSq z := by
  cases z
  simp only [normSq, conj, Int.mul_neg, Int.neg_mul, Int.neg_neg]

/- == anti-vacuity: live instances (norm 3) ============================= -/
/- The ∀-theorems above are unguarded (no hypothesis filters), so none
   can be vacuously true; these pin the operations to computed values
   anyway — the nest is: every operation exercised on a non-degenerate
   witness at least once, off the axes (re ≠ 0 ≠ im). -/

/-- live: ⟨1,2⟩·⟨3,4⟩ = ⟨−5,10⟩ — both coordinates move, sign crosses -/
theorem live_mul_witness : mul ⟨1, 2⟩ ⟨3, 4⟩ = ⟨-5, 10⟩ := by decide

/-- live: N(3+4i) = 25 — the Pythagorean witness -/
theorem live_normSq_witness : normSq ⟨3, 4⟩ = 25 := by decide

/-- live: (1+2i) + (3+4i) = 4+6i -/
theorem live_add_witness : add ⟨1, 2⟩ ⟨3, 4⟩ = ⟨4, 6⟩ := by decide

/-- live: conj moves a genuinely complex point -/
theorem live_conj_witness : conj ⟨3, 4⟩ = ⟨3, -4⟩ := by decide

/- == negative controls (norm 5) ======================================== -/

/-- CONTROL: the fake mirror (a,b) ↦ (a,2b) is NOT a ring hom — it fails
    multiplicativity at z = w = i (certificate: G4_control_fake_mirror_fails).
    fakeMirror(i·i) = ⟨−1,0⟩ but fakeMirror(i)·fakeMirror(i) = ⟨−4,0⟩ -/
theorem control_fake_mirror_fails :
    fakeMirror (mul I I) ≠ mul (fakeMirror I) (fakeMirror I) := by decide

/-- CONTROL: the coordinatewise product differs from mul — the i² = −1
    law is load-bearing, not decoration: coordMul i i = ⟨0,1⟩ ≠ ⟨−1,0⟩ -/
theorem control_coordMul_differs : coordMul I I ≠ mul I I := by decide

/-- CONTROL: conj is not the identity — the mirror actually moves -/
theorem control_conj_not_id : conj I ≠ I := by decide

/-- CONTROL: N is multiplicative, NOT additive — N(1+1) = 4 ≠ 2 = N(1)+N(1) -/
theorem control_normSq_not_additive :
    normSq (add one one) ≠ normSq one + normSq one := by decide

/- ======================================================================
   S2 — THE DOMAIN, BY ONE MOD-4 DESCENT (sub-round 2)

   The chartered route (ROUND1.md §S2, certificate G2_squares_mod_4
   through G2_no_zero_divisors_box): squares mod 4 are exactly {0,1};
   the 16-case decide over (Z/4)² shows N(a+bi) ≡ 0 mod 4 forces both
   coordinates even; halving induction kills N(z) = 0; then the chain
   z·w = 0 ⟹ conj(z)·z·w = 0 ⟹ N(z)·w = 0 ⟹ w = 0.

   THE FORK, stated per the charge: the descent route is taken (the
   pattern-preserving, order-free route matching Circle One), NOT the
   Int-order shortcut (a² ≥ 0). The fuel measure is natAbs-sum with
   structural Nat induction — no well-founded recursion, no `partial`;
   omega handles only the linear bookkeeping, never a ring goal
   (HANDOFF guardrails).
   ====================================================================== -/

/-- squares mod 4 are exactly {0, 1} — nest 4: the four residues 0,1,2,3
    land on 0,1,0,1 (certificate: G2_squares_mod_4).
    ROLE, per seat B crop #1 (S2): standing testimony for charter parity —
    `mod4_forces_even` re-derives the residue facts inline and does NOT
    depend on this theorem; the term graph is flat here on purpose
    (routing through the disjunction would cost cases, not clarity) -/
theorem sq_mod4 (r : Int) : (r*r) % 4 = 0 ∨ (r*r) % 4 = 1 := by
  have h : (r*r) % 4 = ((r%4)*(r%4)) % 4 := by rw [Int.mul_emod]
  have hr0 : 0 ≤ r % 4 := Int.emod_nonneg r (by decide)
  have hr4 : r % 4 < 4 := Int.emod_lt_of_pos r (by decide)
  have hc : r % 4 = 0 ∨ r % 4 = 1 ∨ r % 4 = 2 ∨ r % 4 = 3 := by omega
  rcases hc with h1 | h1 | h1 | h1 <;> rw [h, h1] <;> omega

/-- the 16-case core: over (Z/4)², a²+b² ≡ 0 mod 4 forces both residues
    even — nest 16 = 4×4 residue pairs, exactly 4 of which satisfy the
    hypothesis: (0,0),(0,2),(2,0),(2,2) (certificate: the mod-4 block) -/
theorem mod4_forces_even (a b : Int) (h : (a*a + b*b) % 4 = 0) :
    a % 2 = 0 ∧ b % 2 = 0 := by
  have ha : (a % 4) * (a % 4) % 4 = (a*a) % 4 := (Int.mul_emod a a 4).symm
  have hb : (b % 4) * (b % 4) % 4 = (b*b) % 4 := (Int.mul_emod b b 4).symm
  have hra0 : 0 ≤ a % 4 := Int.emod_nonneg a (by decide)
  have hra4 : a % 4 < 4 := Int.emod_lt_of_pos a (by decide)
  have hrb0 : 0 ≤ b % 4 := Int.emod_nonneg b (by decide)
  have hrb4 : b % 4 < 4 := Int.emod_lt_of_pos b (by decide)
  have hsum : ((a % 4) * (a % 4) + (b % 4) * (b % 4)) % 4 = 0 := by
    rw [Int.add_emod, ha, hb, ← Int.add_emod, h]
  have hr : a % 4 = 0 ∨ a % 4 = 1 ∨ a % 4 = 2 ∨ a % 4 = 3 := by omega
  have hs : b % 4 = 0 ∨ b % 4 = 1 ∨ b % 4 = 2 ∨ b % 4 = 3 := by omega
  rcases hr with h1 | h1 | h1 | h1 <;> rcases hs with h2 | h2 | h2 | h2 <;>
    rw [h1, h2] at hsum <;> exact ⟨by omega, by omega⟩

/-- the halving descent: fuel-indexed strong induction. a²+b² = 0 over Z
    kills both coordinates — order-free, by infinite descent on the
    natAbs-sum (certificate: the halving-induction block).
    ANTI-VACUITY (norm 3, seat B crop #2): the hypothesis is live at
    exactly ONE point of Z², the fixed point (0,0) — necessarily, since
    that is what the theorem forces; the content lives in the forcing,
    and `control_descent_needs_hypothesis` shows the conclusion is not
    free. The same 1-of-N shape returns at S3's forcing instance -/
theorem descent_core : ∀ fuel : Nat, ∀ a b : Int,
    a.natAbs + b.natAbs ≤ fuel → a*a + b*b = 0 → a = 0 ∧ b = 0 := by
  intro fuel
  induction fuel with
  | zero =>
    intro a b hle _
    exact ⟨by omega, by omega⟩
  | succ n ih =>
    intro a b hle hN
    have h4 : (a*a + b*b) % 4 = 0 := by rw [hN]; rfl
    have key := mod4_forces_even a b h4
    obtain ⟨ha2, hb2⟩ := key
    obtain ⟨a', rfl⟩ : ∃ a', a = 2*a' := ⟨a/2, by omega⟩
    obtain ⟨b', rfl⟩ : ∃ b', b = 2*b' := ⟨b/2, by omega⟩
    have hN' : a'*a' + b'*b' = 0 := by
      have h44 : 4*(a'*a' + b'*b') = 0 := by
        rw [← hN]
        simp [Int.add_mul, Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
      omega
    by_cases hz : a' = 0 ∧ b' = 0
    · exact ⟨by omega, by omega⟩
    · have hfa : (2*a').natAbs = 2 * a'.natAbs := by
        rw [Int.natAbs_mul]; rfl
      have hfb : (2*b').natAbs = 2 * b'.natAbs := by
        rw [Int.natAbs_mul]; rfl
      have hnz : a'.natAbs + b'.natAbs ≥ 1 := by
        rcases Decidable.not_and_iff_or_not.mp hz with h | h <;> omega
      have hle' : a'.natAbs + b'.natAbs ≤ n := by omega
      have := ih a' b' hle' hN'
      exact ⟨by omega, by omega⟩

/-- N(z) = 0 ↔ z = 0 — the norm detects zero (certificate:
    G2_norm_zero_iff_zero shape; forward by descent, backward by rfl) -/
theorem normSq_eq_zero_iff (z : Zi) : normSq z = 0 ↔ z = zero := by
  cases z with
  | mk a b =>
    constructor
    · intro h
      have := descent_core (a.natAbs + b.natAbs) a b (Nat.le_refl _) h
      simp only [zero, Zi.mk.injEq]
      exact ⟨this.1, this.2⟩
    · intro h
      rw [h]; rfl

/-- the contrapositive, in the form the chain uses -/
theorem normSq_ne_zero (z : Zi) (h : z ≠ zero) : normSq z ≠ 0 := by
  intro hN
  exact h ((normSq_eq_zero_iff z).mp hN)

/-- scalar action of an integer: n·z as ⟨n,0⟩ · z, componentwise -/
theorem intScalar_mul (n : Int) (z : Zi) :
    mul ⟨n, 0⟩ z = ⟨n * z.re, n * z.im⟩ := by
  cases z
  simp only [mul, Zi.mk.injEq]
  exact ⟨by omega, by omega⟩

/-- torsion-freeness: n·z = 0 with n ≠ 0 kills z — via the norm:
    N(n·z) = n²·N(z) (certificate: the torsion-freeness block) -/
theorem torsion_free (n : Int) (z : Zi) (hn : n ≠ 0)
    (h : mul ⟨n, 0⟩ z = zero) : z = zero := by
  have hN : normSq (mul ⟨n, 0⟩ z) = 0 := by rw [h]; rfl
  rw [normSq_mul] at hN
  have hnn : normSq ⟨n, 0⟩ = n * n := by
    simp only [normSq]
    omega
  rw [hnn] at hN
  have hz : normSq z = 0 := by
    rcases Int.mul_eq_zero.mp hN with h1 | h1
    · rcases Int.mul_eq_zero.mp h1 with h2 | h2 <;> exact absurd h2 hn
    · exact h1
  exact (normSq_eq_zero_iff z).mp hz

/-- the chain: Z[i] has no zero divisors —
    z·w = 0 ⟹ conj(z)·(z·w) = 0 ⟹ (N(z),0)·w = 0 ⟹ N(z) kills both
    coordinates ⟹ w = 0 (certificate: G2_no_zero_divisors_box) -/
theorem no_zero_divisors (z w : Zi) (h : mul z w = zero) :
    z = zero ∨ w = zero := by
  by_cases hz : z = zero
  · exact Or.inl hz
  · right
    have h1 : mul (conj z) (mul z w) = zero := by
      rw [h, mul_zero]
    have h2 : mul (mul (conj z) z) w = zero := by
      rw [mul_assoc]; exact h1
    rw [conj_mul_eq_normSq] at h2
    have hNz : normSq z ≠ 0 := normSq_ne_zero z hz
    cases w with
    | mk c d =>
      rw [intScalar_mul] at h2
      simp only [zero, Zi.mk.injEq] at h2
      obtain ⟨hc, hd⟩ := h2
      simp only [zero, Zi.mk.injEq]
      constructor
      · rcases Int.mul_eq_zero.mp hc with h' | h'
        · exact absurd h' hNz
        · exact h'
      · rcases Int.mul_eq_zero.mp hd with h' | h'
        · exact absurd h' hNz
        · exact h'

/- == S2 anti-vacuity: live instances (norm 3) ========================== -/

/-- live: the descent actually runs — N(0+0i) = 0 and the theorem's
    conclusion is inhabited by the only witness -/
theorem live_descent_witness : normSq zero = 0 := rfl

/-- live: a nonzero element with nonzero norm — the contrapositive has
    a live instance off the axes -/
theorem live_normSq_nonzero : normSq ⟨1, 2⟩ = 5 := by decide

/-- live: no_zero_divisors' hypothesis is satisfiable — zero·w = 0 -/
theorem live_zero_mul_witness : mul zero ⟨3, 4⟩ = zero := by decide

/-- live: sq_mod4's nest, all four residues — 0²,1²,2²,3² mod 4 = 0,1,0,1 -/
theorem live_sq_mod4_nest :
    (0*0) % 4 = 0 ∧ (1*1) % 4 = 1 ∧ (2*2) % 4 = 0 ∧ (3*3 : Int) % 4 = 1 := by
  decide

/- == S2 negative controls (norm 5) ===================================== -/

/-- CONTROL (mandatory, chartered): the mod-2 analogue FAILS — (1,1) has
    N = 2 ≡ 0 mod 2 with both coordinates ODD. 2 ramifies in Z[i]; the
    modulus 4 is load-bearing (certificate: G2_control_mod2_insufficient) -/
theorem control_mod2_insufficient :
    (1*1 + 1*1 : Int) % 2 = 0 ∧ (1 : Int) % 2 ≠ 0 := by decide

/-- CONTROL: the descent's conclusion is FALSE without the hypothesis —
    N(1+2i) = 5 ≠ 0 and (1,2) ≠ (0,0): the theorem is not vacuously
    closing everything it sees -/
theorem control_descent_needs_hypothesis :
    normSq ⟨1, 2⟩ ≠ 0 ∧ (⟨1, 2⟩ : Zi) ≠ zero := by decide

/-- CONTROL: no-zero-divisors is a DOMAIN theorem, not arithmetic luck —
    the residue world has zero divisors: 2·2 = 4 ≡ 0 mod 4 with 2 ≢ 0.
    (The chartered Z[i]/5 split — (2+i)(2−i) = 5 — is certificate
    territory (G3b) and rides with S3's exactly-two; this is the small
    sibling in Z/4.) -/
theorem control_z4_has_zero_divisors :
    (2 * 2 : Int) % 4 = 0 ∧ (2 : Int) % 4 ≠ 0 := by decide


/- ======================================================================
   S3 — PENTAGON NECESSITY (ROUND1.md §S3, ~18 thm chartered)

   Over ANY commutative ring — here over Zi, which is enough for the
   chartered claim and lets S2's domain finish the count: the 16 pentagon
   instances for the Z₂ F-symbol classify as 11 reading 1 = 1, 4 reading
   f = f, and exactly ONE forcing — (a,b,c,d) = (1,1,1,1), where
   lhs = f² and rhs = 1 (certificate: G1a_pentagon_16_instances_classified,
   G1a_forcing_instance_is_1111_f2_eq_1).

   Index conventions, sourced per C1's lesson — ALL from
   floor/symmetric_statistics.py in this repo:
   - F-symbol Fsym_z2(f, a,b,c,d,x,y): LINE 102 — admissible iff
     x = (a+b)%2, y = (b+c)%2, d = (a+b+c)%2; value f iff
     (a,b,c) = (1,1,1), else 1.
   - Pentagon plumbing (x,y,t,w,v,u as functions of a,b,c,d):
     pent_residual_z2, LINE 108 — transcribed verbatim below.

   NEST (norm 9): 16 = 2⁴ label assignments; 11 + 4 + 1 = 16, tied by
   the counted classification at a separating witness (f = ⟨5,0⟩:
   1 ≠ 5 ≠ 25 keeps the three kinds apart). No admissibility zeros on
   the path (the plumbing hits only admissible slots — the bench's
   residual counts every quadruple).

   ANTI-VACUITY (norm 3): the pentagon ∀ is guarded by a < 2 ∧ … ∧ d < 2
   — live on exactly 16 quadruples (`pent_nest_card`). The forcing
   hypothesis is live at exactly 1 of 16 — the 1-of-N shape seat B's S2
   crop #2 predicted would return here; it has.

   WORDING (charter flag 2, certificate G1c): the headline below is in
   SLICE-PLUS-INVARIANCE form. The (1,1,1) slot is a gauge invariant of
   the normalized slice (proved symbolically, `gauge_slot_invariant`),
   so F = +1 and F = −1 are genuinely distinct classes; with the
   16-instance derivation: exactly two. The remaining step to the full
   "H³(Z₂) = Z₂" sentence — EVERY class has a normalized representative
   — is NOT proven here and NOT bench-certified (certificate G1c's own
   label); this file does not state that sentence.
   ====================================================================== -/

/-- the bench F-symbol on Z₂ fusion, transcribed from
    floor/symmetric_statistics.py LINE 102: admissibility gates to zero;
    the single free slot is (a,b,c) = (1,1,1) ↦ f -/
def Fz2 (f : Zi) (a b c d x y : Nat) : Zi :=
  if x = (a+b) % 2 ∧ y = (b+c) % 2 ∧ d = (a+b+c) % 2 then
    (if a = 1 ∧ b = 1 ∧ c = 1 then f else one)
  else zero

/-- pentagon lhs — the bench's three-factor side, plumbing transcribed
    verbatim from pent_residual_z2, LINE 108 -/
def pentL (f : Zi) (a b c d : Nat) : Zi :=
  let x := (a+b) % 2
  let y := (x+c) % 2
  let t := (y+d) % 2
  let w := (c+d) % 2
  let v := (b+w) % 2
  let u := (b+c) % 2
  mul (mul (Fz2 f a b c y x u) (Fz2 f a u d t y v)) (Fz2 f b c d v u w)

/-- pentagon rhs — the bench's two-factor side, same source line -/
def pentR (f : Zi) (a b c d : Nat) : Zi :=
  let x := (a+b) % 2
  let y := (x+c) % 2
  let t := (y+d) % 2
  let w := (c+d) % 2
  let v := (b+w) % 2
  mul (Fz2 f x c d t y w) (Fz2 f a b w t x v)

/-- "f satisfies the pentagon": all 16 instances — guarded ∀, live on
    exactly the 16 quadruples of {0,1}⁴ (nest: `pent_nest_card`) -/
def pentagon (f : Zi) : Prop :=
  ∀ a b c d : Nat, a < 2 → b < 2 → c < 2 → d < 2 →
    pentL f a b c d = pentR f a b c d

/- == the classification: 11 + 4 + 1 = 16 ============================== -/

/-- the 15 off-forcing instances hold for EVERY f — 11 read 1 = 1 and
    4 read f = f, so both sides agree identically; the sweep is the
    full 16-case rcases with the forcing quadruple excluded by
    hypothesis (certificate: G1a — "the other 15 are ring identities") -/
theorem pentagon_offdiag (f : Zi) : ∀ a b c d : Nat,
    a < 2 → b < 2 → c < 2 → d < 2 → ¬(a = 1 ∧ b = 1 ∧ c = 1 ∧ d = 1) →
    pentL f a b c d = pentR f a b c d := by
  intro a b c d ha hb hc hd hne
  have ha' : a = 0 ∨ a = 1 := by omega
  have hb' : b = 0 ∨ b = 1 := by omega
  have hc' : c = 0 ∨ c = 1 := by omega
  have hd' : d = 0 ∨ d = 1 := by omega
  rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
    rcases hc' with rfl | rfl <;> rcases hd' with rfl | rfl <;>
    first
      | exact absurd ⟨rfl, rfl, rfl, rfl⟩ hne
      | simp +decide only [pentL, pentR, Fz2, if_true, if_false, one_mul, mul_one]

/-- the forcing instance, lhs: at (1,1,1,1) the three-factor side is f²
    (certificate: G1a_forcing_instance_is_1111_f2_eq_1, lhs) -/
theorem pentagon_forcing_lhs (f : Zi) : pentL f 1 1 1 1 = mul f f := by
  simp +decide only [pentL, Fz2, if_true, if_false, mul_one]

/-- the forcing instance, rhs: at (1,1,1,1) the two-factor side is 1
    (certificate: G1a_forcing_instance_is_1111_f2_eq_1, rhs) -/
theorem pentagon_forcing_rhs (f : Zi) : pentR f 1 1 1 1 = one := by
  simp +decide only [pentR, Fz2, if_true, if_false, mul_one]

/-- pentagon ⟹ f² = 1: the single forcing instance, applied -/
theorem pentagon_forces_f_sq_one (f : Zi) (h : pentagon f) :
    mul f f = one := by
  have h1 := h 1 1 1 1 (by decide) (by decide) (by decide) (by decide)
  rw [pentagon_forcing_lhs, pentagon_forcing_rhs] at h1
  exact h1

/-- f² = 1 ⟹ pentagon: the forcing instance closes by hypothesis, the
    other 15 by the sweep — so pentagon ⟺ f² = 1, over any f in Zi
    (and the proof shape is the any-commutative-ring one: nothing
    Zi-specific is used until the domain enters at the root count) -/
theorem f_sq_one_gives_pentagon (f : Zi) (h : mul f f = one) :
    pentagon f := by
  intro a b c d ha hb hc hd
  have ha' : a = 0 ∨ a = 1 := by omega
  have hb' : b = 0 ∨ b = 1 := by omega
  have hc' : c = 0 ∨ c = 1 := by omega
  have hd' : d = 0 ∨ d = 1 := by omega
  rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
    rcases hc' with rfl | rfl <;> rcases hd' with rfl | rfl <;>
    first
      | (rw [pentagon_forcing_lhs, pentagon_forcing_rhs]; exact h)
      | simp +decide only [pentL, pentR, Fz2, if_true, if_false, one_mul, mul_one]

/-- the headline equivalence at the instance level -/
theorem pentagon_iff_f_sq_one (f : Zi) : pentagon f ↔ mul f f = one :=
  ⟨pentagon_forces_f_sq_one f, f_sq_one_gives_pentagon f⟩

/- == the counted classification — nest 16, tied (norm 9) =============== -/

/-- the 16 quadruples, explicitly — the nest itself -/
def pentQuads : List (Nat × Nat × Nat × Nat) :=
  [(0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),
   (0,1,0,0),(0,1,0,1),(0,1,1,0),(0,1,1,1),
   (1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),
   (1,1,0,0),(1,1,0,1),(1,1,1,0),(1,1,1,1)]

/-- nest cardinality: 16 = 2⁴ -/
theorem pent_nest_card : pentQuads.length = 16 := by decide

/-- the counted classification at the separating witness f = ⟨5,0⟩
    (1, 5, 25 pairwise distinct, so the three kinds cannot be
    conflated): 11 instances read 1 = 1, 4 read f = f, 1 forces —
    and 11 + 4 + 1 = 16 ties the count to its nest (norm 9;
    certificate: G1a_pentagon_16_instances_classified = (11,4,1,0)).
    SCOPE, per seat B crop #1 (S3): the filters classify by LHS value
    alone; the lhs-rhs pairing that makes this a classification of
    INSTANCES is supplied by `pentagon_offdiag` (lhs = rhs off the
    forcing site) + `pentagon_forcing_lhs`/`_rhs` (f², 1 there) —
    without those three, this count would not classify -/
theorem pent_classification_counted :
    (pentQuads.filter (fun q =>
      decide (pentL ⟨5,0⟩ q.1 q.2.1 q.2.2.1 q.2.2.2 = one))).length = 11 ∧
    (pentQuads.filter (fun q =>
      decide (pentL ⟨5,0⟩ q.1 q.2.1 q.2.2.1 q.2.2.2 = ⟨5,0⟩))).length = 4 ∧
    (pentQuads.filter (fun q =>
      decide (pentL ⟨5,0⟩ q.1 q.2.1 q.2.2.1 q.2.2.2 = ⟨25,0⟩))).length = 1 ∧
    11 + 4 + 1 = 16 := by decide

/-- the four f = f instances, named: both sides equal f symbolically at
    (0,1,1,1), (1,0,1,1), (1,1,0,1), (1,1,1,0) — the bench's f_eq_f
    kind, here as identities in a symbolic f -/
theorem pent_f_eq_f_instances (f : Zi) :
    (pentL f 0 1 1 1 = f ∧ pentR f 0 1 1 1 = f) ∧
    (pentL f 1 0 1 1 = f ∧ pentR f 1 0 1 1 = f) ∧
    (pentL f 1 1 0 1 = f ∧ pentR f 1 1 0 1 = f) ∧
    (pentL f 1 1 1 0 = f ∧ pentR f 1 1 1 0 = f) := by
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩ <;>
    simp +decide only [pentL, pentR, Fz2, if_true, if_false, one_mul, mul_one]

/- == from f² = 1 to exactly two, via S2's domain ======================= -/

/-- sub z w = 0 ⟺ z = w — the cancellation bridge -/
theorem sub_eq_zero_iff (z w : Zi) : sub z w = zero ↔ z = w := by
  cases z; cases w
  simp only [sub, add, neg, zero, Zi.mk.injEq]
  constructor
  · intro ⟨h1, h2⟩; exact ⟨by omega, by omega⟩
  · intro ⟨h1, h2⟩; exact ⟨by omega, by omega⟩

/-- the factorization f² − 1 = (f−1)(f+1), symbolic over Zi
    (certificate: G3a_factorization_symbolic) -/
theorem factorization_symbolic (f : Zi) :
    mul (sub f one) (add f one) = sub (mul f f) one := by
  cases f
  simp only [mul, sub, add, neg, one, Zi.mk.injEq,
             Int.mul_add, Int.add_mul, Int.mul_one, Int.one_mul, Int.neg_mul]
  refine ⟨?_, ?_⟩ <;> omega

/-- f² = 1 ⟺ f = +1 or f = −1 — the DOMAIN theorem: the factorization
    plus S2's no_zero_divisors; over a non-domain this fails
    (`control_z8_four_roots` below). char 0 keeps the roots distinct -/
theorem f_sq_one_iff_pm_one (f : Zi) :
    mul f f = one ↔ (f = one ∨ f = neg one) := by
  constructor
  · intro h
    have hz : mul (sub f one) (add f one) = zero := by
      rw [factorization_symbolic, h]
      decide
    rcases no_zero_divisors _ _ hz with h1 | h1
    · exact Or.inl ((sub_eq_zero_iff f one).mp h1)
    · right
      cases f
      simp only [add, one, zero, Zi.mk.injEq] at h1
      simp only [neg, one, Zi.mk.injEq]
      exact ⟨by omega, by omega⟩
  · intro h
    rcases h with rfl | rfl <;> decide

/-- both roots land, and they are distinct: at least two — and by the
    domain, at most two: EXACTLY TWO (certificate: G3a_both_roots_land) -/
theorem both_roots_land :
    mul one one = one ∧ mul (neg one) (neg one) = one ∧ one ≠ neg one := by
  decide

/-- THE HEADLINE, slice-plus-invariance form (charter flag 2): a
    normalized F-symbol on Z₂ fusion satisfies the pentagon iff its one
    free slot F(1,1,1) is +1 or −1 — exactly two solutions on the
    normalized slice, distinct by char 0, and the slot is a gauge
    invariant of the slice (`gauge_slot_invariant` below), so the two
    are genuinely distinct classes. NOT claimed: that every class meets
    the slice (not proven here; not bench-certified — G1c's own label) -/
theorem pentagon_exactly_two (f : Zi) :
    pentagon f ↔ (f = one ∨ f = neg one) := by
  rw [pentagon_iff_f_sq_one]
  exact f_sq_one_iff_pm_one f

/- == live instances (norm 3) =========================================== -/

/-- live: f = +1 (the boson-side class representative) satisfies all 16 -/
theorem live_pentagon_plus_one : pentagon one :=
  f_sq_one_gives_pentagon one (by decide)

/-- live: f = −1 (the fermion-side class representative) satisfies all 16 -/
theorem live_pentagon_minus_one : pentagon (neg one) :=
  f_sq_one_gives_pentagon (neg one) (by decide)

/-- live, the forcing site: at f = ⟨5,0⟩ the forcing instance separates
    (25 ≠ 1) while an f = f instance holds — the hypothesis structure of
    the classification is live, not vacuous -/
theorem live_forcing_separates :
    pentL ⟨5,0⟩ 1 1 1 1 ≠ pentR ⟨5,0⟩ 1 1 1 1 ∧
    pentL ⟨5,0⟩ 0 1 1 1 = pentR ⟨5,0⟩ 0 1 1 1 := by decide

/-- live, off the real axis (seat B crop #3, S3): at the genuinely
    Gaussian point f = 1+i the forcing lhs is f² = 2i = ⟨0,2⟩ ≠ 1 while
    an f = f instance still holds — the symbolic claims are tied to a
    witness that exercises the imaginary coordinate -/
theorem live_gaussian_witness :
    pentL ⟨1,1⟩ 1 1 1 1 = ⟨0,2⟩ ∧ pentR ⟨1,1⟩ 1 1 1 1 = one ∧
    pentL ⟨1,1⟩ 0 1 1 1 = ⟨1,1⟩ ∧ pentR ⟨1,1⟩ 0 1 1 1 = ⟨1,1⟩ := by decide

/- == negative controls (norm 5) ======================================== -/

/-- NEGATIVE CONTROL (non-domain): in Z/8, f² = 1 has FOUR solutions
    {1,3,5,7} — exactly-two is a DOMAIN theorem, not arithmetic luck
    (certificate: G3a_control_Z8_four_roots); nest 8, tied by the iff -/
theorem control_z8_four_roots : ∀ x : Fin 8,
    (x.val * x.val) % 8 = 1 ↔
    (x.val = 1 ∨ x.val = 3 ∨ x.val = 5 ∨ x.val = 7) := by decide

/-- NEGATIVE CONTROL (Gaussian): f = i — a UNIT of Z[i] — still fails
    the pentagon: i² − 1 = −2 ≠ 0, residual N(i²−1) = 4 exactly
    (certificate: G1a_control_f_eq_i_fails_pentagon; the charge's
    "residual exactly 4") -/
theorem control_f_eq_i_fails_pentagon :
    ¬ pentagon I ∧ sub (mul I I) one = ⟨-2, 0⟩ ∧ normSq ⟨-2, 0⟩ = 4 := by
  refine ⟨fun h => ?_, by decide, by decide⟩
  have := pentagon_forces_f_sq_one I h
  exact absurd this (by decide)

/-- NEGATIVE CONTROL (non-root, non-unit): f = 2 fails the pentagon —
    4 ≠ 1 at the forcing instance (the certificate's f = 2 → residual 9
    point, here at the instance level) -/
theorem control_f_eq_two_fails_pentagon : ¬ pentagon ⟨2, 0⟩ := by
  intro h
  have := pentagon_forces_f_sq_one ⟨2, 0⟩ h
  exact absurd this (by decide)

/- == gauge: the slot is an invariant of the normalized slice =========== -/
/- Vertex gauge η : Z₂ × Z₂ → units, coboundary
   (dη)(a,b,c) = η(b,c) · η(a,(b+c)%2) / [η((a+b)%2,c) · η(a,b)]
   — certificate G1c, symbolic. Division-free here: numerator and
   denominator carried separately, equalities in cleared form. -/

/-- coboundary numerator at (a,b,c) -/
def detaNum (eta : Nat → Nat → Zi) (a b c : Nat) : Zi :=
  mul (eta b c) (eta a ((b+c) % 2))

/-- coboundary denominator at (a,b,c) -/
def detaDen (eta : Nat → Nat → Zi) (a b c : Nat) : Zi :=
  mul (eta ((a+b) % 2) c) (eta a b)

/-- the raw motion of the (1,1,1) slot: (dη)(1,1,1) = [η11·η10]/[η01·η11]
    — i.e. η10/η01 after the common factor (certificate:
    G1c_slot_moves_by_n10_over_n01), stated in cleared form -/
theorem gauge_slot_motion (eta : Nat → Nat → Zi) :
    detaNum eta 1 1 1 = mul (eta 1 1) (eta 1 0) ∧
    detaDen eta 1 1 1 = mul (eta 0 1) (eta 1 1) := ⟨rfl, rfl⟩

/-- cancellation in the domain: from a·x = a·y with a ≠ 0, x = y —
    S2's no_zero_divisors doing gauge work -/
theorem mul_left_cancel (a x y : Zi) (ha : a ≠ zero)
    (h : mul a x = mul a y) : x = y := by
  have hz : mul a (sub x y) = zero := by
    have hd : mul a (sub x y) = sub (mul a x) (mul a y) := by
      show mul a (add x (neg y)) = add (mul a x) (neg (mul a y))
      rw [mul_add, mul_neg]
    rw [hd, h]
    exact (sub_eq_zero_iff _ _).mpr rfl
  rcases no_zero_divisors _ _ hz with h1 | h1
  · exact absurd h1 ha
  · exact (sub_eq_zero_iff x y).mp h1

/-- slice-preservation forces η01 = η10: the zero-slot conditions at
    (1,0,0) and (0,0,1) — in cleared form, with the shared factors
    cancelled through the domain. η maps into UNITS per the certificate
    (G1c: "eta : Z2 x Z2 -> units"), so nonzero-ness is hypothesis, not
    accident; only the three values that get cancelled are needed
    (certificate: G1c_slice_preserving_gauges_characterized, the
    n00 = n01 = n10 reduction, the two rows that reach the slot) -/
theorem slice_forces_eta_symmetric (eta : Nat → Nat → Zi)
    (h10 : eta 1 0 ≠ zero) (h01 : eta 0 1 ≠ zero)
    (c100 : detaNum eta 1 0 0 = detaDen eta 1 0 0)
    (c001 : detaNum eta 0 0 1 = detaDen eta 0 0 1) :
    eta 0 1 = eta 1 0 := by
  -- (1,0,0): num = η00·η10, den = η10·η10 ⟹ η00 = η10 (cancel η10)
  have e1 : eta 0 0 = eta 1 0 := by
    have h1 : mul (eta 1 0) (eta 0 0) = mul (eta 1 0) (eta 1 0) := by
      have hc := c100
      simp only [detaNum, detaDen] at hc
      calc mul (eta 1 0) (eta 0 0) = mul (eta 0 0) (eta 1 0) := mul_comm _ _
        _ = mul (eta 1 0) (eta 1 0) := hc
    exact mul_left_cancel _ _ _ h10 h1
  -- (0,0,1): num = η01·η01, den = η01·η00 ⟹ η01 = η00 (cancel η01)
  have e2 : eta 0 1 = eta 0 0 := by
    have h2 : mul (eta 0 1) (eta 0 1) = mul (eta 0 1) (eta 0 0) := by
      have hc := c001
      simp only [detaNum, detaDen] at hc
      exact hc
    exact mul_left_cancel _ _ _ h01 h2
  rw [e2, e1]

/-- THE SLOT IS A GAUGE INVARIANT of the normalized slice: for any
    slice-preserving gauge (η into units, zero-slot conditions at
    (1,0,0) and (0,0,1) — the two rows of G1c's seven that reach the
    slot), the motion of F(1,1,1) is trivial: (dη)(1,1,1) reads
    num = den in cleared form (certificate:
    G1c_slot_invariant_under_slice_gauges). So F = +1 and F = −1 are
    genuinely distinct classes — with `pentagon_exactly_two`: exactly
    two on the slice. NOT claimed: every class meets the slice.
    STRENGTH, per seat B crop #2 (S3): this is STRONGER than the
    certificate's row — two of G1c's seven zero-slot conditions
    suffice; the other five are not hypothesized and not silently
    used (norm 6: the label matches the term graph) -/
theorem gauge_slot_invariant (eta : Nat → Nat → Zi)
    (h10 : eta 1 0 ≠ zero) (h01 : eta 0 1 ≠ zero)
    (c100 : detaNum eta 1 0 0 = detaDen eta 1 0 0)
    (c001 : detaNum eta 0 0 1 = detaDen eta 0 0 1) :
    detaNum eta 1 1 1 = detaDen eta 1 1 1 := by
  have he := slice_forces_eta_symmetric eta h10 h01 c100 c001
  show mul (eta 1 1) (eta 1 0) = mul (eta 0 1) (eta 1 1)
  rw [he, mul_comm]

/-- live gauge witness (norm 3): a slice-preserving gauge with η11 = i —
    the one FREE vertex value (G1c: "n11 FREE") — satisfies both
    zero-slot conditions and moves the slot trivially; and it is not the
    identity gauge, so the invariance theorem is exercised off the
    trivial point -/
theorem live_gauge_witness :
    let eta := fun a b : Nat => if a = 1 ∧ b = 1 then I else one
    detaNum eta 1 0 0 = detaDen eta 1 0 0 ∧
    detaNum eta 0 0 1 = detaDen eta 0 0 1 ∧
    detaNum eta 1 1 1 = detaDen eta 1 1 1 ∧
    eta 1 1 ≠ one := by
  refine ⟨by decide, by decide, by decide, by decide⟩

/-- NEGATIVE CONTROL (gauge): a NON-slice-preserving η — η01 = ⟨2,0⟩,
    all else 1 — violates a zero-slot condition AND moves the slot:
    the invariance is a consequence of slice-preservation, not of the
    coboundary shape (norm 5 for the gauge family) -/
theorem control_gauge_moves_slot :
    let eta := fun a b : Nat => if a = 0 ∧ b = 1 then ⟨2,0⟩ else one
    detaNum eta 0 0 1 ≠ detaDen eta 0 0 1 ∧
    detaNum eta 1 1 1 ≠ detaDen eta 1 1 1 := by
  refine ⟨by decide, by decide⟩

end Zi
