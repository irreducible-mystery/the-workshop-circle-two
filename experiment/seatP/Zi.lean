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


end Zi
