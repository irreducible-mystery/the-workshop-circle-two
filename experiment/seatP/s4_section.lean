   S4 — THE HEXAGON LAYER (BEYOND the S1–S3 charge)

   SCOPE, recorded honestly: ROUND1.md's charge to the third body is
   S1–S3; this section is the hexagon layer — R² = F, the four units,
   the flatland filter as a Galois statement, the mirror — which the
   charge assigns beyond S1–S3. The courier (Kelly) sanctioned the
   extension explicitly, noting the divergence from chartered
   boundaries; this comment is the record of that. Quarantine
   unchanged (norm 16, REGISTER row 7).

   Index conventions, sourced per C1's lesson — ALL from
   floor/symmetric_statistics.py:
   - Hexagon plumbing (e = (a+b)%2, z = (a+c)%2, admissibility
     d = (e+c)%2 = (z+b)%2, g = (b+c)%2; R applies at (1,1) only):
     hex_residual_z2, LINE 124 — transcribed verbatim below.
   - The F-symbol is S3's Fz2 (bench LINE 102), reused.

   Certificate sources: G1d (8 instances, one forcing, R² = F; the
   reduction identity; catalog4 satisfies BOTH hexagons; wrong-R
   controls), G3b (semion factorization over Z[i]; no integer semion;
   the Z[i]/5 chartered control), G1e (the filter: conj(R) = R kills
   the semions), G4 (the mirror: semions a conjugate pair; classes
   conj-fixed; norms all 1).

   Charter flags carried:
   - flag 4: the 2×2 count is a Z[i] statement — over Z the F = −1
     class is EMPTY (`no_integer_semion`).
   - flag 5: the bench imposes ONE hexagon; the R⁻¹-hexagon is
     equivalent on units (u⁻¹ = conj u, `unit_inverse_is_conj`) —
     both are imposed on the catalog here
     (`catalog_satisfies_both_hexagons`), and nothing here claims the
     bench did.
   - flag 3 (the Frobenius–Schur convention fork, ν = R·θ vs the
     mirror-ledger R·conj(θ)) is a TWIST-layer item and is NOT
     addressed here; no theorem below mentions ν — recorded so the
     absence is a decision, not a gap.

   NEST (norm 9): 16 loop assignments (a,b,c,d); exactly 8 admissible
   (d = a+b+c forced — `hex_nest_8_of_16`); of the 8: 5 read 1 = 1,
   2 read R = R, 1 forces — 5 + 2 + 1 = 8, counted at a separating
   witness. The catalog nest: 2 classes × 2 particles = 4, filtered
   to 2 (`filter_nest_2_of_4`).
   ====================================================================== -/

/-- the bench R-symbol: R applies at (1,1) only — hex_residual_z2,
    LINE 124 (`Rs(x, y, c) = R if (x, y) == (1, 1) else 1`; the bench's
    unused third argument dropped, the plumbing otherwise verbatim) -/
def Rz2 (r : Zi) (x y : Nat) : Zi :=
  if x = 1 ∧ y = 1 then r else one

/-- hexagon admissibility — bench LINE 124: d = (e+c)%2 AND d = (z+b)%2
    with e = (a+b)%2, z = (a+c)%2; the bench checks the pair, so the
    pair is what this def states (both reduce to d = (a+b+c)%2) -/
def hexAdm (a b c d : Nat) : Prop :=
  d = (((a+b) % 2) + c) % 2 ∧ d = (((a+c) % 2) + b) % 2

instance (a b c d : Nat) : Decidable (hexAdm a b c d) := by
  unfold hexAdm; exact inferInstance

/-- hexagon lhs — bench LINE 124: R(e,c) · F(c,a,b,d,z,e) -/
def hexL (f r : Zi) (a b c d : Nat) : Zi :=
  let e := (a+b) % 2
  let z := (a+c) % 2
  mul (Rz2 r e c) (Fz2 f c a b d z e)

/-- hexagon rhs — bench LINE 124:
    F(a,b,c,d,e,g) · R(b,c) · F(a,c,b,d,z,g) · R(a,c) -/
def hexR (f r : Zi) (a b c d : Nat) : Zi :=
  let e := (a+b) % 2
  let z := (a+c) % 2
  let g := (b+c) % 2
  mul (mul (Fz2 f a b c d e g) (Rz2 r b c))
      (mul (Fz2 f a c b d z g) (Rz2 r a c))

/-- "(f, r) satisfies the R-hexagon": all admissible instances — the
    guarded ∀ is live on exactly 8 of 16 quadruples (`hex_nest_8_of_16`) -/
def hexagon (f r : Zi) : Prop :=
  ∀ a b c d : Nat, a < 2 → b < 2 → c < 2 → d < 2 → hexAdm a b c d →
    hexL f r a b c d = hexR f r a b c d

/- == integer-square helpers, through the domain ======================== -/

/-- squares over Int are nonnegative — sign split, no order imports -/
theorem int_sq_nonneg (a : Int) : 0 ≤ a * a := by
  rcases Int.le_total 0 a with h | h
  · exact Int.mul_nonneg h h
  · have h' : 0 ≤ -a := by omega
    have hn := Int.mul_nonneg h' h'
    have he : -a * -a = a * a := by
      simp only [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    rw [he] at hn
    exact hn

/-- a² = 0 forces a = 0 — routed through the Zi domain (order-free) -/
theorem int_sq_eq_zero (a : Int) (h : a * a = 0) : a = 0 := by
  have hz : mul ⟨a, 0⟩ ⟨a, 0⟩ = zero := by
    simp only [mul, zero, Zi.mk.injEq]
    exact ⟨by omega, by omega⟩
  rcases no_zero_divisors _ _ hz with h1 | h1 <;>
  · simp only [zero, Zi.mk.injEq] at h1
    exact h1.1

/-- a² = 1 forces a = ±1 — the Int-level factorization through the
    Zi domain -/
theorem int_sq_eq_one (a : Int) (h : a * a = 1) : a = 1 ∨ a = -1 := by
  have hfac : (a - 1) * (a + 1) = a * a - 1 := by
    simp only [Int.sub_mul, Int.mul_add, Int.one_mul, Int.mul_one]
    omega
  have hz : mul ⟨a - 1, 0⟩ ⟨a + 1, 0⟩ = zero := by
    simp only [mul, zero, Zi.mk.injEq]
    exact ⟨by omega, by omega⟩
  rcases no_zero_divisors _ _ hz with h1 | h1
  · left; simp only [zero, Zi.mk.injEq] at h1; omega
  · right; simp only [zero, Zi.mk.injEq] at h1; omega

/- == the nest, tied (norm 9) =========================================== -/

/-- of the 16 loop assignments exactly 8 are admissible — the
    certificate's "16 loop assignments, 8 admissible (d = a+b+c
    forced)" (G1d, nest line) -/
theorem hex_nest_8_of_16 :
    ((List.range 2).flatMap (fun a => (List.range 2).flatMap (fun b =>
      (List.range 2).flatMap (fun c => (List.range 2).filterMap (fun d =>
        if hexAdm a b c d then some (a, b, c, d) else none))))).length = 8 ∧
    (2 * 2 * 2 * 2 : Nat) = 16 := by decide

/- == the classification: 5 + 2 + 1 = 8 ================================= -/

/-- the 7 off-forcing admissible instances hold for EVERY f and r —
    5 read 1 = 1 ((0,0,0,0),(0,0,1,1),(0,1,0,1),(1,0,0,1),(1,1,0,0))
    and 2 read R = R ((0,1,1,0),(1,0,1,0)) — identities in symbolic
    f, r (certificate: G1d_hexagon_8_instances_classified = (5,2,1,0)) -/
theorem hexagon_offdiag (f r : Zi) : ∀ a b c d : Nat,
    a < 2 → b < 2 → c < 2 → d < 2 → hexAdm a b c d →
    ¬(a = 1 ∧ b = 1 ∧ c = 1 ∧ d = 1) →
    hexL f r a b c d = hexR f r a b c d := by
  intro a b c d ha hb hc hd hadm hne
  have ha' : a = 0 ∨ a = 1 := by omega
  have hb' : b = 0 ∨ b = 1 := by omega
  have hc' : c = 0 ∨ c = 1 := by omega
  have hd' : d = 0 ∨ d = 1 := by omega
  rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
    rcases hc' with rfl | rfl <;> rcases hd' with rfl | rfl <;>
    first
      | exact absurd ⟨rfl, rfl, rfl, rfl⟩ hne
      | exact absurd hadm (by decide)
      | simp +decide only [hexL, hexR, Fz2, Rz2, if_true, if_false,
                           one_mul, mul_one]

/-- the forcing instance, lhs: at (1,1,1,1) — the admissible triple
    (a,b,c) = (1,1,1), d = 1 forced — the R·F side is f
    (certificate: G1d_forcing_instance_is_111, lhs of "f = f²R²") -/
theorem hexagon_forcing_lhs (f r : Zi) : hexL f r 1 1 1 1 = f := by
  simp +decide only [hexL, Fz2, Rz2, if_true, if_false, one_mul]

/-- the forcing instance, rhs: at (1,1,1,1) the F·R·F·R side is
    (f·r)·(f·r) — f²r² in this file's mul-tree shape -/
theorem hexagon_forcing_rhs (f r : Zi) :
    hexR f r 1 1 1 1 = mul (mul f r) (mul f r) := by
  simp +decide only [hexR, Fz2, Rz2, if_true]

/-- (f·r)² = f²·r² — the commutative regrouping, explicit-argument
    rewrites so nothing fires off-target -/
theorem square_of_product (f r : Zi) :
    mul (mul f r) (mul f r) = mul (mul f f) (mul r r) := by
  rw [mul_assoc f r (mul f r), mul_comm r (mul f r), mul_assoc f r r,
      ← mul_assoc f f (mul r r)]

/-- hexagon ⟹ f = f²r² — the forcing instance applied, in the
    certificate's orientation (G1d: "f = f² R²") -/
theorem hexagon_forces (f r : Zi) (h : hexagon f r) :
    f = mul (mul f f) (mul r r) := by
  have h1 := h 1 1 1 1 (by decide) (by decide) (by decide) (by decide)
    (by decide)
  rw [hexagon_forcing_lhs, hexagon_forcing_rhs, square_of_product] at h1
  exact h1

/-- the reduction identity, exact over Zi: f²r² − f =
    (r² − f) + r²(f² − 1) (certificate: G1d_reduction_identity) — so
    pentagon (f² = 1) + hexagon (f = f²r²) ⟺ r² = f in any commutative
    ring; the component identities are degree-4, closed by the
    Brahmagupta recipe (distribute, normalize, omega) -/
theorem hexagon_reduction_identity (f r : Zi) :
    sub (mul (mul f f) (mul r r)) f
      = add (sub (mul r r) f) (mul (mul r r) (sub (mul f f) one)) := by
  cases f; cases r
  simp only [mul, sub, add, neg, one, Zi.mk.injEq,
             Int.mul_sub, Int.mul_add, Int.sub_mul, Int.add_mul,
             Int.mul_one, Int.mul_neg,
             Int.mul_comm, Int.mul_left_comm]
  refine ⟨?_, ?_⟩ <;> omega

/-- PENTAGON + HEXAGON ⟺ R² = F: given f² = 1, the hexagon holds
    exactly when r² = f — the headline reduction. Over F = +1 this is
    r² = 1; over F = −1 it is r² = −1 (certificate: G1d forcing +
    reduction identity) -/
theorem pentagon_hexagon_iff_R_sq_F (f r : Zi) (hp : mul f f = one) :
    hexagon f r ↔ mul r r = f := by
  constructor
  · intro h
    have h1 := hexagon_forces f r h
    rw [hp, one_mul] at h1
    exact h1.symm
  · intro h
    intro a b c d ha hb hc hd hadm
    by_cases hq : a = 1 ∧ b = 1 ∧ c = 1 ∧ d = 1
    · obtain ⟨rfl, rfl, rfl, rfl⟩ := hq
      rw [hexagon_forcing_lhs, hexagon_forcing_rhs, square_of_product,
          hp, one_mul, h]
    · exact hexagon_offdiag f r a b c d ha hb hc hd hadm hq

/- == the four units of Z[i] ============================================ -/

/-- Z[i] has exactly four elements of norm 1: a² + b² = 1 over Z forces
    (a², b²) ∈ {(1,0),(0,1)} — the complete candidate list for R once
    N(r) = 1 (the charge: "Z[i] has exactly four units"; certificate
    G3b's census). Completeness needs no search box -/
theorem norm_one_units (z : Zi) (h : normSq z = 1) :
    z = one ∨ z = neg one ∨ z = I ∨ z = neg I := by
  rcases z with ⟨a, b⟩
  simp only [normSq] at h
  have ha0 : 0 ≤ a * a := int_sq_nonneg a
  have hb0 : 0 ≤ b * b := int_sq_nonneg b
  -- disjunction split WITHOUT omega-on-a-disjunctive-goal (the
  -- Classical.choice trap): by_cases on decidable Int equality, then
  -- omega proves only atomic equations
  by_cases haz : a * a = 0
  · have hb : b * b = 1 := by omega
    have ha' := int_sq_eq_zero a haz
    subst ha'
    rcases int_sq_eq_one b hb with hb' | hb' <;> subst hb'
    · right; right; left; decide
    · right; right; right; decide
  · have ha : a * a = 1 := by omega
    have hbz : b * b = 0 := by omega
    have hb' := int_sq_eq_zero b hbz
    subst hb'
    rcases int_sq_eq_one a ha with ha' | ha' <;> subst ha'
    · left; decide
    · right; left; decide

/-- the nest for the unit census (norm 9): the four units are pairwise
    distinct and all of norm 1 — 4 named + 0 others = 4, the complement
    supplied by `norm_one_units` -/
theorem units_four_distinct :
    normSq one = 1 ∧ normSq (neg one) = 1 ∧ normSq I = 1 ∧
    normSq (neg I) = 1 ∧ one ≠ neg one ∧ one ≠ I ∧ one ≠ neg I ∧
    neg one ≠ I ∧ neg one ≠ neg I ∧ I ≠ neg I := by decide

/- == the roots of r² = ±1: the four particles ========================== -/

/-- over F = +1: r² = 1 ⟺ r ∈ {+1, −1} — boson and fermion (S3's
    domain theorem, reused on r) -/
theorem R_over_boson_class (r : Zi) :
    mul r r = one ↔ (r = one ∨ r = neg one) :=
  f_sq_one_iff_pm_one r

/-- the semion factorization over Z[i]: (r − i)(r + i) = r² + 1
    symbolically (certificate: G3b_semion_factorization_over_Zi) —
    the F = −1 class's quadratic factors over Z[i], NOT over Z -/
theorem semion_factorization (r : Zi) :
    mul (sub r I) (add r I) = add (mul r r) one := by
  cases r
  simp only [mul, sub, add, neg, one, I, Zi.mk.injEq,
             Int.mul_add, Int.add_mul, Int.mul_one, Int.one_mul,
             Int.neg_mul]
  refine ⟨?_, ?_⟩ <;> omega

/-- over F = −1: r² = −1 ⟺ r ∈ {+i, −i} — the semions, by the
    factorization and S2's domain (certificate: G3b_R2_eq_f_roots_exact) -/
theorem R_over_semion_class (r : Zi) :
    mul r r = neg one ↔ (r = I ∨ r = neg I) := by
  constructor
  · intro h
    have hz : mul (sub r I) (add r I) = zero := by
      rw [semion_factorization, h]
      decide
    rcases no_zero_divisors _ _ hz with h1 | h1
    · exact Or.inl ((sub_eq_zero_iff r I).mp h1)
    · right
      rcases r with ⟨a, b⟩
      simp only [add, I, zero, Zi.mk.injEq] at h1
      simp only [neg, I, Zi.mk.injEq]
      exact ⟨by omega, by omega⟩
  · intro h
    rcases h with rfl | rfl <;> decide

/-- flag 4, the Z-emptiness: r² = −1 has NO real solution (im = 0) —
    over Z the F = −1 class is EMPTY and the roomy catalog would be
    2 classes × (2, 0) particles; the 2×2 count is a Z[i] statement
    (certificate: G3b_no_integer_semion, as the exact statement:
    a² ≥ 0 > −1, no box needed) -/
theorem no_integer_semion (r : Zi) (hreal : r.im = 0) :
    mul r r ≠ neg one := by
  rcases r with ⟨a, b⟩
  have hb : b = 0 := hreal
  subst hb
  intro h
  simp only [mul, neg, one, Zi.mk.injEq] at h
  have ha0 : 0 ≤ a * a := int_sq_nonneg a
  omega

/- == the catalog: 2 × 2 = 4, and both hexagons ========================= -/

/-- the four particles satisfy their class equations, and the catalog
    count ties to its nest: 2 pentagon classes × 2 particles = 4
    (norm 9; certificate: G3b_R2_eq_f_roots_exact) -/
theorem catalog_two_by_two :
    (mul one one = one ∧ mul (neg one) (neg one) = one) ∧
    (mul I I = neg one ∧ mul (neg I) (neg I) = neg one) ∧
    (2 * 2 : Nat) = 4 := by decide

/-- on the four units, r · conj(r) = 1: the inverse IS the conjugate —
    the identity that makes the roomy edict R = R⁻¹ a Galois statement
    (the charge: "on units, u⁻¹ = conj(u)") -/
theorem unit_inverse_is_conj :
    mul one (conj one) = one ∧ mul (neg one) (conj (neg one)) = one ∧
    mul I (conj I) = one ∧ mul (neg I) (conj (neg I)) = one := by decide

/-- flag 5: each catalog entry satisfies BOTH hexagon equations — the
    R-hexagon (r² = f) and the R⁻¹-hexagon (conj(r)² = f, since on
    units r⁻¹ = conj r) — at no extra root cost. The BENCH imposes only
    one; nothing here claims otherwise
    (certificate: G1d_catalog4_satisfies_BOTH_hexagons) -/
theorem catalog_satisfies_both_hexagons :
    (mul one one = one ∧ mul (conj one) (conj one) = one) ∧
    (mul (neg one) (neg one) = one ∧
     mul (conj (neg one)) (conj (neg one)) = one) ∧
    (mul I I = neg one ∧ mul (conj I) (conj I) = neg one) ∧
    (mul (neg I) (neg I) = neg one ∧
     mul (conj (neg I)) (conj (neg I)) = neg one) := by decide

/- == the flatland filter as a Galois statement ========================= -/

/-- THE FILTER (certificate G1e): the roomy edict R = R⁻¹ is literally
    conj(R) = R on units — and its fixed points among the four are
    exactly boson and fermion. The semions die on the flatland filter
    exactly as the anyon died on the roomy edict. Nest 2 of 4 -/
theorem flatland_filter :
    (conj one = one) ∧ (conj (neg one) = neg one) ∧
    (conj I ≠ I) ∧ (conj (neg I) ≠ neg I) := by decide

/-- the filter count ties to its nest (norm 9): 2 survivors + 2 killed
    = 4 catalog entries -/
theorem filter_nest_2_of_4 : (2 + 2 : Nat) = 4 := by decide

/-- the mirror (certificate G4): conj — this circle's σ — swaps the
    semions (a Galois-conjugate pair: the golden/Yang–Lee pattern one
    level down) and FIXES both F-classes, so σ acts WITHIN the F = −1
    fiber. Structural difference from Circle One, stated honestly:
    there σ moved BETWEEN the pentagon classes; here the pentagon data
    is rational and the swap lives inside one hexagon fiber -/
theorem mirror_structure :
    (conj I = neg I ∧ conj (neg I) = I) ∧
    (conj one = one ∧ conj (neg one) = neg one) ∧
    conj (conj I) = I := by decide

/- == live instances (norm 3) =========================================== -/

/-- live: the boson (F, R) = (+1, +1) satisfies the full hexagon -/
theorem live_hexagon_boson : hexagon one one :=
  (pentagon_hexagon_iff_R_sq_F one one (by decide)).mpr (by decide)

/-- live: the fermion (F, R) = (+1, −1) satisfies the full hexagon -/
theorem live_hexagon_fermion : hexagon one (neg one) :=
  (pentagon_hexagon_iff_R_sq_F one (neg one) (by decide)).mpr (by decide)

/-- live: the semion (F, R) = (−1, +i) satisfies the full hexagon —
    the genuinely Gaussian particle, off the real axis -/
theorem live_hexagon_semion : hexagon (neg one) I :=
  (pentagon_hexagon_iff_R_sq_F (neg one) I (by decide)).mpr (by decide)

/-- live: the anti-semion (F, R) = (−1, −i) satisfies the full hexagon -/
theorem live_hexagon_antisemion : hexagon (neg one) (neg I) :=
  (pentagon_hexagon_iff_R_sq_F (neg one) (neg I) (by decide)).mpr (by decide)

/-- live, the forcing site separates: at (f, r) = (1, ⟨2,0⟩) the
    forcing instance fails (lhs 1 ≠ rhs 4) while an R = R instance
    ((0,1,1,0)) holds — the classification's hypothesis structure is
    live, not vacuous -/
theorem live_hex_forcing_separates :
    hexL one ⟨2,0⟩ 1 1 1 1 ≠ hexR one ⟨2,0⟩ 1 1 1 1 ∧
    hexL one ⟨2,0⟩ 0 1 1 0 = hexR one ⟨2,0⟩ 0 1 1 0 := by decide

/- == negative controls (norm 5) ======================================== -/

/-- NEGATIVE CONTROL (wrong R per class): R = i over F = +1 leaves
    f²r² − f = ⟨−2,0⟩ ≠ 0; R = 1 over F = −1 leaves ⟨2,0⟩ ≠ 0 — the
    classes do not accept each other's particles
    (certificate: G1d_controls_wrong_R_per_class, both values exact) -/
theorem control_wrong_R_per_class :
    sub (mul (mul one one) (mul I I)) one = ⟨-2, 0⟩ ∧
    sub (mul (mul (neg one) (neg one)) (mul one one)) (neg one)
      = ⟨2, 0⟩ := by decide

/-- NEGATIVE CONTROL (the chartered one — deferred from S2 with stated
    reason, landing here where the charge placed it): in Z[i]/5 the
    domain fails — (2+i)(2−i) = 5 — and exactly-two fails with it:
    r² = 1 has FOUR roots mod 5 and r² = −1 has FOUR; nest 25 = 5²
    (certificate: G3b_control_Zi_mod5_splits). Represented on residue
    pairs (a,b) ∈ [0,5)², product mod 5 componentwise via the mul law.
    SEAT B's CROP (S4 item 1), recorded: the real part is encoded as
    (a*a + 5*5 - b*b) % 5 over Nat, where subtraction truncates at
    zero; the +5*5 offset is LOAD-BEARING — it keeps the difference
    nonnegative exactly because b ∈ range 5 bounds b*b ≤ 16 < 25.
    Safe on this nest; unsafe as a general recipe -/
theorem control_Zi_mod5_splits :
    (mul ⟨2, 1⟩ ⟨2, -1⟩ = ⟨5, 0⟩) ∧
    ((List.range 5).flatMap (fun a => (List.range 5).filterMap (fun b =>
      if (a*a + 5*5 - b*b) % 5 = 1 ∧ (2*a*b) % 5 = 0
      then some (a, b) else none))).length = 4 ∧
    ((List.range 5).flatMap (fun a => (List.range 5).filterMap (fun b =>
      if (a*a + 5*5 - b*b) % 5 = 4 ∧ (2*a*b) % 5 = 0
      then some (a, b) else none))).length = 4 ∧
    (5 * 5 : Nat) = 25 := by decide

/-- NEGATIVE CONTROL (the filter is not vacuous): a NON-particle passes
    the reality test — conj ⟨3,0⟩ = ⟨3,0⟩ — but solves neither class
    equation: the filter selects among the CATALOG; it does not define
    it -/
theorem control_filter_needs_catalog :
    conj ⟨3, 0⟩ = ⟨3, 0⟩ ∧ mul ⟨3, 0⟩ ⟨3, 0⟩ ≠ one ∧
    mul ⟨3, 0⟩ ⟨3, 0⟩ ≠ neg one := by decide

