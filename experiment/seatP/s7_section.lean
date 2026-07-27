
/- ======================================================================
   S7 — THE SLICE LEMMA, OVER THE UNITS OF Z[i]  (charge S7a)

   SCOPE, recorded honestly: this section answers CHARGE-S7a-SLICE-LEMMA.md
   (SuperNinja instance 2, meta-auditor, Round Three), carried by Kelly.
   It closes the step S3's gauge block declares NOT claimed, and which
   REGISTER row 2 has carried as this record's oldest declared exclusion:
   that the reduction to the normalized slice is without loss of
   generality. Quarantine unchanged (norm 16, REGISTER row 7).

   THE OBJECT, and why the first framing was wrong. A gauge class is an
   orbit of a COCYCLE, not of an arbitrary function. The charge ships two
   SUPERSEDED probes that enumerated arbitrary cochains and reported the
   lemma FALSE; their "counterexample" (i at the (1,1,0) slot) is not a
   cocycle and was therefore never a class. It ships here as
   `controlCochainA`, the section's first negative control — the trap,
   kept as an instrument.

   WHAT IS PROVEN: `slice_lemma_over_zi_units`. Every unit-valued
   3-cochain satisfying the pentagon (cocycle) relation is cohomologous
   to a normalized `Fnorm f` representative, with f = +1 or −1. The
   witnesses are EXPLICIT and READ OFF the cochain — eta from F's own
   values (`sliceGauge`), f = F(1,1,1)·F(1,0,0)·F(0,0,1) — so nothing is
   searched for and no choice principle enters.

   WHAT IS NOT PROVEN, and cannot be here (norm 6, the charge's
   load-bearing constraint): the continuous sentence H³(Z₂, U(1)) = Z₂.
   U(1) is not representable in a zero-import kernel over Int. Every
   theorem name and docstring in this section says "over the units of
   Z[i]", never "over U(1)". Whether the Z[i]-unit fragment discharges
   REGISTER row 2 or leaves U(1) as a narrowed residue is the
   adjudicator's ruling (charge §5), not this file's to assert.

   NESTS (norm 9), each matching the authoritative design probe
   `probes/s7a_cocycle_reach.py` (32 / 16 / 2):
   - 32 cocycles of 64 parameter triples — `s7_nest_cocycles_32`, tied to
     the objects by the classification (`cocycle_is_cochainOf` forward,
     `cochainOf_is_cocycle` backward, `cochainOf_injective` no overcount,
     `cocycle_triple_in_nest` membership).
   - 16 coboundaries of 4⁴ = 256 gauges — `s7_nest_coboundaries_16`, in
     two halves: reduction to normal form and distinctness of the 16.
   - 2 classes, 16 + 16 = 32 — `s7_nest_classes_2`.

   ANTI-VACUITY (norm 3): both classes are inhabited by named cocycles
   (`live_both_classes_inhabited`), and the lemma is exercised where it
   has work to do — `cochainOf I one I` sits off the real axis AND off
   the slice, and the gauge the lemma builds for it is not the identity
   (`live_gaussian_cocycle_off_slice`, `live_slice_gauge_normalizes`).

   NEGATIVE CONTROLS (norm 5), two, in the two directions the charge
   names: the cocycle hypothesis is load-bearing
   (`control_A_not_a_cocycle_and_never_normalized` — 256 gauges x 4 units
   all fail on a non-cocycle), and the gauge must be the constructed one
   (`control_B_identity_gauge_fails` on the same cochain that
   `live_slice_gauge_normalizes` succeeds on).

   GUARDRAILS: no budget raises — this file still contains no
   `set_option`. The 256-gauge sweeps run as coordinate-wise nests so
   evaluation depth stays additive rather than multiplicative.

   Design probe: probes/s7a_cocycle_reach.py (authoritative, 32/16/2) and
   the third body's structural probe, run BEFORE any Lean was written
   (norm 15).
   ====================================================================== -/

/- == unit vocabulary =================================================== -/

/-- a UNIT of `Zi`: an element of norm 1. The four units are
    `one, I, neg one, neg I` (`norm_one_units`, S4) -/
def isUnit (z : Zi) : Prop := normSq z = 1

/-- a unit is nonzero — the hypothesis S2's domain wants -/
theorem unit_ne_zero (z : Zi) (h : isUnit z) : z ≠ zero := by
  intro hz
  have h' : normSq zero = 1 := by rw [← hz]; exact h
  exact absurd h' (by decide)

/-- on a unit the INVERSE IS THE CONJUGATE: z · conj z = 1. The symbolic
    form of S4's `unit_inverse_is_conj`, which checked the four by name -/
theorem unit_mul_conj (z : Zi) (h : isUnit z) : mul z (conj z) = one := by
  rw [mul_conj_eq_normSq, h]
  rfl

/-- units are closed under multiplication (N multiplicative, S1) -/
theorem unit_mul (z w : Zi) (hz : isUnit z) (hw : isUnit w) :
    isUnit (mul z w) := by
  show normSq (mul z w) = 1
  rw [normSq_mul, hz, hw]
  rfl

/-- units are closed under conjugation -/
theorem unit_conj (z : Zi) (h : isUnit z) : isUnit (conj z) := by
  show normSq (conj z) = 1
  rw [normSq_conj]; exact h

/-- cancellation by a unit — S2's domain, with the nonzero-ness supplied
    by the norm rather than assumed -/
theorem unit_cancel (a x y : Zi) (ha : isUnit a) (h : mul a x = mul a y) :
    x = y :=
  mul_left_cancel a x y (unit_ne_zero a ha) h

/-- the third associativity/commutativity law, so that `simp` can
    AC-normalize products of `mul` -/
theorem mul_left_comm (z w v : Zi) : mul z (mul w v) = mul w (mul z v) := by
  rw [← mul_assoc, mul_comm z w, mul_assoc]

/- == the general 3-cochain, its pentagon, and the normalized shape ===== -/

/-- a 3-COCHAIN is a map on slots (a,b,c) ∈ {0,1}³; UNIT-VALUED means
    every one of the 8 slot values is a unit of `Zi` -/
def unitCochain (F : Nat → Nat → Nat → Zi) : Prop :=
  ∀ a b c : Nat, a < 2 → b < 2 → c < 2 → isUnit (F a b c)

/-- the pentagon (3-cocycle) relation on a GENERAL cochain — the 5-term
    associativity relation, multiplicative and division-free:
    F(b,c,d)·F(a,b+c,d)·F(a,b,c) = F(a+b,c,d)·F(a,b,c+d), with the Z₂
    group law as (·+·)%2. Guarded ∀, live on the 16 quadruples of
    `pentQuads`. NOTE the object: the kernel's S3 `pentagon` is this
    relation specialized to the hardcoded `Fz2` shape; THIS predicate is
    the honest general one, which is what a gauge CLASS is an orbit of -/
def cocycle3 (F : Nat → Nat → Nat → Zi) : Prop :=
  ∀ a b c d : Nat, a < 2 → b < 2 → c < 2 → d < 2 →
    mul (mul (F b c d) (F a ((b+c) % 2) d)) (F a b c)
      = mul (F ((a+b) % 2) c d) (F a b ((c+d) % 2))

/-- the NORMALIZED (slice) shape as a plain 3-cochain: `one` on every
    slot carrying a 0, free only at (1,1,1) ↦ f -/
def Fnorm (f : Zi) (a b c : Nat) : Zi :=
  if a = 1 ∧ b = 1 ∧ c = 1 then f else one

/-- `Fnorm` IS the kernel's `Fz2` read on its admissible slots — the tie
    that keeps this section's "normalized representative" the same object
    S3's headline is about, not a look-alike (norm 6) -/
theorem Fnorm_eq_Fz2 (f : Zi) (a b c : Nat) :
    Fnorm f a b c = Fz2 f a b c ((a+b+c) % 2) ((a+b) % 2) ((b+c) % 2) := by
  unfold Fnorm Fz2
  rw [if_pos (show (a+b) % 2 = (a+b) % 2 ∧ (b+c) % 2 = (b+c) % 2 ∧
                   (a+b+c) % 2 = (a+b+c) % 2 from ⟨rfl, rfl, rfl⟩)]

/- == the five forced slots of a unit-valued cocycle ==================== -/

/-- F(0,0,0) = 1 — from the (0,0,0,0) instance alone -/
theorem cocycle_at_000 (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) : F 0 0 0 = one := by
  have h : mul (mul (F 0 0 0) (F 0 0 0)) (F 0 0 0) = mul (F 0 0 0) (F 0 0 0) :=
    hc 0 0 0 0 (by decide) (by decide) (by decide) (by decide)
  have hU : isUnit (mul (F 0 0 0) (F 0 0 0)) :=
    unit_mul _ _ (hu 0 0 0 (by decide) (by decide) (by decide))
      (hu 0 0 0 (by decide) (by decide) (by decide))
  refine unit_cancel _ _ _ hU ?_
  rw [h, mul_one]

/-- F(0,1,0) = 1 — from the (0,1,0,0) instance -/
theorem cocycle_at_010 (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) : F 0 1 0 = one := by
  have h : mul (mul (F 1 0 0) (F 0 1 0)) (F 0 1 0) = mul (F 1 0 0) (F 0 1 0) :=
    hc 0 1 0 0 (by decide) (by decide) (by decide) (by decide)
  have hU : isUnit (mul (F 1 0 0) (F 0 1 0)) :=
    unit_mul _ _ (hu 1 0 0 (by decide) (by decide) (by decide))
      (hu 0 1 0 (by decide) (by decide) (by decide))
  refine unit_cancel _ _ _ hU ?_
  rw [h, mul_one]

/-- F(1,0,0)·F(1,1,0) = 1 — the (1,1,0,0) instance: the (1,1,0) slot is
    the inverse of the (1,0,0) slot -/
theorem cocycle_at_110 (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    mul (F 1 0 0) (F 1 1 0) = one := by
  have h : mul (mul (F 1 0 0) (F 1 1 0)) (F 1 1 0) = mul (F 0 0 0) (F 1 1 0) :=
    hc 1 1 0 0 (by decide) (by decide) (by decide) (by decide)
  have h000 := cocycle_at_000 F hu hc
  have hW : isUnit (F 1 1 0) := hu 1 1 0 (by decide) (by decide) (by decide)
  refine unit_cancel _ _ _ hW ?_
  rw [mul_one, mul_comm (F 1 1 0) (mul (F 1 0 0) (F 1 1 0)), h, h000, one_mul]

/-- F(0,1,1)·F(0,0,1) = 1 — the (0,0,1,1) instance: the (0,1,1) slot is
    the inverse of the (0,0,1) slot -/
theorem cocycle_at_011 (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    mul (F 0 1 1) (F 0 0 1) = one := by
  have h : mul (mul (F 0 1 1) (F 0 1 1)) (F 0 0 1) = mul (F 0 1 1) (F 0 0 0) :=
    hc 0 0 1 1 (by decide) (by decide) (by decide) (by decide)
  have h000 := cocycle_at_000 F hu hc
  have hV : isUnit (F 0 1 1) := hu 0 1 1 (by decide) (by decide) (by decide)
  refine unit_cancel _ _ _ hV ?_
  rw [mul_one, ← mul_assoc, h, h000, mul_one]

/-- F(1,0,1) = F(0,0,1)·F(1,0,0) — the (1,0,0,1) instance: the mixed slot
    is the product of the two free ones -/
theorem cocycle_at_101 (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    F 1 0 1 = mul (F 0 0 1) (F 1 0 0) := by
  have h : mul (mul (F 0 0 1) (F 1 0 1)) (F 1 0 0) = mul (F 1 0 1) (F 1 0 1) :=
    hc 1 0 0 1 (by decide) (by decide) (by decide) (by decide)
  have hY : isUnit (F 1 0 1) := hu 1 0 1 (by decide) (by decide) (by decide)
  refine (unit_cancel _ _ _ hY ?_).symm
  rw [← mul_assoc, mul_comm (F 1 0 1) (F 0 0 1), h]

/-- THE CLASS LABEL SQUARES TO ONE: for a unit-valued cocycle,
    f := F(1,1,1)·F(1,0,0)·F(0,0,1) satisfies f² = 1 — the (1,1,1,1)
    instance, cleared through the forced slots. With S3's
    `f_sq_one_iff_pm_one` this is what pins the class count at two -/
theorem cocycle_f_sq_one (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    mul (mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1))
        (mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1)) = one := by
  have h5 : mul (mul (F 1 1 1) (F 1 0 1)) (F 1 1 1) = mul (F 0 1 1) (F 1 1 0) :=
    hc 1 1 1 1 (by decide) (by decide) (by decide) (by decide)
  rw [cocycle_at_101 F hu hc] at h5
  have lhs_eq : mul (mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1))
                    (mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1))
              = mul (mul (mul (F 1 1 1) (mul (F 0 0 1) (F 1 0 0))) (F 1 1 1))
                    (mul (F 1 0 0) (F 0 0 1)) := by
    simp only [mul_comm, mul_left_comm]
  have rhs_eq : mul (mul (F 0 1 1) (F 1 1 0)) (mul (F 1 0 0) (F 0 0 1))
              = mul (mul (F 0 1 1) (F 0 0 1)) (mul (F 1 0 0) (F 1 1 0)) := by
    simp only [mul_comm, mul_left_comm]
  rw [lhs_eq, h5, rhs_eq, cocycle_at_011 F hu hc, cocycle_at_110 F hu hc,
      mul_one]

/-- F(0,1,1) is the CONJUGATE of F(0,0,1) — the inverse relation of
    `cocycle_at_011` read through `unit_mul_conj` -/
theorem cocycle_011_eq_conj (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    F 0 1 1 = conj (F 0 0 1) := by
  have hQ : isUnit (F 0 0 1) := hu 0 0 1 (by decide) (by decide) (by decide)
  refine unit_cancel (F 0 0 1) _ _ hQ ?_
  rw [unit_mul_conj _ hQ, mul_comm]
  exact cocycle_at_011 F hu hc

/-- F(1,1,0) is the CONJUGATE of F(1,0,0) -/
theorem cocycle_110_eq_conj (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    F 1 1 0 = conj (F 1 0 0) := by
  have hP : isUnit (F 1 0 0) := hu 1 0 0 (by decide) (by decide) (by decide)
  refine unit_cancel (F 1 0 0) _ _ hP ?_
  rw [unit_mul_conj _ hP]
  exact cocycle_at_110 F hu hc

/-- AC helper: swap the two right-hand factors of a triple product -/
theorem mul_swap_right (z w v : Zi) : mul (mul z w) v = mul (mul z v) w := by
  simp only [mul_comm, mul_left_comm]

/- == the normalizing gauge, built from F's own values ================== -/

/-- THE NORMALIZING GAUGE. Not searched for — READ OFF the cochain:
    η(1,0) = F(1,0,0), η(0,1) = conj F(0,0,1), η(0,0) = η(1,1) = 1.
    (η(1,1) is G1c's "n11 FREE" vertex; the lemma takes it trivial.) -/
def sliceGauge (F : Nat → Nat → Nat → Zi) (a b : Nat) : Zi :=
  if a = 1 ∧ b = 0 then F 1 0 0
  else if a = 0 ∧ b = 1 then conj (F 0 0 1) else one

/-- THE SLICE LEMMA, OVER THE UNITS OF ℤ[i] — the charge S7a.

    Every unit-valued 3-cochain `F` satisfying the pentagon (cocycle)
    relation is COHOMOLOGOUS to a normalized representative: there is a
    unit-valued vertex gauge `eta` and a unit `f` with
    `F · (d eta) = Fnorm f` at every one of the 8 slots (carried in the
    kernel's division-free cleared form, `detaNum`/`detaDen`), and
    `f ∈ {one, neg one}` — exactly two normalized classes.

    This closes the reduction-to-the-slice step that S3's
    `gauge_slot_invariant` docstring records as NOT claimed: with it,
    S3's "exactly two ON THE SLICE" becomes exactly two, full stop —
    OVER THE UNITS OF ℤ[i].

    OUT OF REACH, stated so the label cannot overreach (norm 6): the
    continuous sentence H³(Z₂, U(1)) = Z₂, with the CONTINUOUS unit
    group U(1), is NOT this theorem and is NOT in zero-import reach —
    U(1) is not representable here. This theorem is the finite ℤ[i]-unit
    fragment, and its name says so. Whether the fragment discharges
    REGISTER row 2's exclusion or leaves U(1) as a narrowed residue is
    the adjudicator's ruling, not this file's.

    The witnesses are EXPLICIT (`sliceGauge`, and f = F(1,1,1)·F(1,0,0)·
    F(0,0,1)) — read off F, never searched for, so no choice principle
    enters (axiom census: 0 Classical.choice). -/
theorem slice_lemma_over_zi_units (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    ∃ eta : Nat → Nat → Zi, ∃ f : Zi,
      (∀ a b : Nat, a < 2 → b < 2 → isUnit (eta a b)) ∧
      (f = one ∨ f = neg one) ∧
      (∀ a b c : Nat, a < 2 → b < 2 → c < 2 →
        mul (F a b c) (detaNum eta a b c)
          = mul (Fnorm f a b c) (detaDen eta a b c)) := by
  have hP : isUnit (F 1 0 0) := hu 1 0 0 (by decide) (by decide) (by decide)
  have hQ : isUnit (F 0 0 1) := hu 0 0 1 (by decide) (by decide) (by decide)
  have hQc : mul (F 0 0 1) (conj (F 0 0 1)) = one := unit_mul_conj _ hQ
  refine ⟨sliceGauge F, mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1), ?_, ?_, ?_⟩
  · -- the gauge is unit-valued
    intro a b ha hb
    have ha' : a = 0 ∨ a = 1 := by omega
    have hb' : b = 0 ∨ b = 1 := by omega
    rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl
    · exact (by decide : normSq one = 1)
    · exact unit_conj _ hQ
    · exact hP
    · exact (by decide : normSq one = 1)
  · -- the class label is +1 or −1 (S3's domain theorem, on f)
    exact (f_sq_one_iff_pm_one _).mp (cocycle_f_sq_one F hu hc)
  · -- the eight slot equations
    intro a b c ha hb hc'
    have ha' : a = 0 ∨ a = 1 := by omega
    have hb' : b = 0 ∨ b = 1 := by omega
    have hc'' : c = 0 ∨ c = 1 := by omega
    rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
      rcases hc'' with rfl | rfl
    · show mul (F 0 0 0) (mul one one) = mul one (mul one one)
      simp only [mul_one]
      exact cocycle_at_000 F hu hc
    · show mul (F 0 0 1) (mul (conj (F 0 0 1)) (conj (F 0 0 1)))
            = mul one (mul (conj (F 0 0 1)) one)
      simp only [mul_one]
      rw [← mul_assoc, hQc]
    · show mul (F 0 1 0) (mul (F 1 0 0) (conj (F 0 0 1)))
            = mul one (mul (F 1 0 0) (conj (F 0 0 1)))
      simp only [one_mul]
      rw [cocycle_at_010 F hu hc, one_mul]
    · show mul (F 0 1 1) (mul one one) = mul one (mul one (conj (F 0 0 1)))
      simp only [one_mul, mul_one]
      exact cocycle_011_eq_conj F hu hc
    · show mul (F 1 0 0) (mul one (F 1 0 0)) = mul one (mul (F 1 0 0) (F 1 0 0))
      simp only [one_mul]
    · show mul (F 1 0 1) (mul (conj (F 0 0 1)) one)
            = mul one (mul one (F 1 0 0))
      simp only [one_mul, mul_one]
      rw [cocycle_at_101 F hu hc, mul_swap_right, hQc, one_mul]
    · show mul (F 1 1 0) (mul (F 1 0 0) one) = mul one (mul one one)
      simp only [mul_one]
      rw [mul_comm]
      exact cocycle_at_110 F hu hc
    · show mul (F 1 1 1) (mul one (F 1 0 0))
            = mul (mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1))
                  (mul (conj (F 0 0 1)) one)
      simp only [one_mul, mul_one]
      rw [mul_assoc, hQc, mul_one]

/- == the classification: cocycles ARE the parametrized shapes ========== -/

/-- the cochain determined by three unit parameters — p at (1,0,0),
    q at (0,0,1), s at (1,1,1), the other five slots forced -/
def cochainOf (p q s : Zi) (a b c : Nat) : Zi :=
  if a = 1 ∧ b = 1 ∧ c = 1 then s
  else if a = 1 ∧ b = 0 ∧ c = 1 then mul q p
  else if a = 1 ∧ b = 1 ∧ c = 0 then conj p
  else if a = 0 ∧ b = 1 ∧ c = 1 then conj q
  else if a = 1 ∧ b = 0 ∧ c = 0 then p
  else if a = 0 ∧ b = 0 ∧ c = 1 then q
  else one

/-- FORWARD: every unit-valued cocycle IS `cochainOf` of its own three
    values — the five other slots carry no freedom -/
theorem cocycle_is_cochainOf (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    ∀ a b c : Nat, a < 2 → b < 2 → c < 2 →
      F a b c = cochainOf (F 1 0 0) (F 0 0 1) (F 1 1 1) a b c := by
  intro a b c ha hb hc'
  have ha' : a = 0 ∨ a = 1 := by omega
  have hb' : b = 0 ∨ b = 1 := by omega
  have hc'' : c = 0 ∨ c = 1 := by omega
  rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
    rcases hc'' with rfl | rfl
  · exact cocycle_at_000 F hu hc
  · rfl
  · exact cocycle_at_010 F hu hc
  · exact cocycle_011_eq_conj F hu hc
  · rfl
  · exact cocycle_at_101 F hu hc
  · exact cocycle_110_eq_conj F hu hc
  · rfl

/-- the parametrization is INJECTIVE — so counting triples counts
    cochains (norm 9: the nest below would overcount otherwise) -/
theorem cochainOf_injective (p q s p' q' s' : Zi)
    (h : ∀ a b c : Nat, a < 2 → b < 2 → c < 2 →
           cochainOf p q s a b c = cochainOf p' q' s' a b c) :
    p = p' ∧ q = q' ∧ s = s' :=
  ⟨h 1 0 0 (by decide) (by decide) (by decide),
   h 0 0 1 (by decide) (by decide) (by decide),
   h 1 1 1 (by decide) (by decide) (by decide)⟩

/-- `cochainOf` of units is unit-valued -/
theorem cochainOf_unitCochain (p q s : Zi)
    (hp : isUnit p) (hq : isUnit q) (hs : isUnit s) :
    unitCochain (cochainOf p q s) := by
  intro a b c ha hb hcc
  have ha' : a = 0 ∨ a = 1 := by omega
  have hb' : b = 0 ∨ b = 1 := by omega
  have hc'' : c = 0 ∨ c = 1 := by omega
  rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
    rcases hc'' with rfl | rfl
  · exact (by decide : normSq one = 1)
  · exact hq
  · exact (by decide : normSq one = 1)
  · exact unit_conj _ hq
  · exact hp
  · exact unit_mul _ _ hq hp
  · exact unit_conj _ hp
  · exact hs

/-- BACKWARD: every parameter triple whose class label squares to one
    DOES give a cocycle — so the 32 below is a count of cocycles, not an
    upper bound (the two directions together are the classification) -/
theorem cochainOf_is_cocycle (p q s : Zi)
    (hp : isUnit p) (hq : isUnit q) (hs : isUnit s)
    (hf : mul (mul (mul s p) q) (mul (mul s p) q) = one) :
    cocycle3 (cochainOf p q s) := by
  rcases norm_one_units p hp with rfl | rfl | rfl | rfl <;>
  rcases norm_one_units q hq with rfl | rfl | rfl | rfl <;>
  rcases norm_one_units s hs with rfl | rfl | rfl | rfl <;>
  first
    | exact absurd hf (by decide)
    | (intro a b c d ha hb hcc hd
       have ha' : a = 0 ∨ a = 1 := by omega
       have hb' : b = 0 ∨ b = 1 := by omega
       have hc' : c = 0 ∨ c = 1 := by omega
       have hd' : d = 0 ∨ d = 1 := by omega
       rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
         rcases hc' with rfl | rfl <;> rcases hd' with rfl | rfl <;> decide)

/- == the nests, tied: 32 cocycles / 16 coboundaries / 2 classes ======== -/

/-- the four units, explicitly (kept concrete, not as a Subtype) -/
def unitsZi : List Zi := [one, I, neg one, neg I]

/-- the 8 cochain slots -/
def slotList : List (Nat × Nat × Nat) :=
  [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]

/-- the parameter triples (p,q,s) whose class label s·p·q squares to one
    — by the classification above, exactly the unit-valued cocycles -/
def cocycleTriples : List (Zi × Zi × Zi) :=
  unitsZi.flatMap fun p => unitsZi.flatMap fun q => unitsZi.filterMap fun s =>
    if mul (mul (mul s p) q) (mul (mul s p) q) = one then some (p, q, s) else none

/-- NEST — 32 COCYCLES of 64 triples (norm 9). 4 units cubed = 64
    parameter triples; exactly 32 satisfy the class-label condition. By
    `cochainOf_is_cocycle` each is a cocycle, by `cocycle_is_cochainOf`
    every cocycle is one of them, and by `cochainOf_injective` no two
    coincide — so 32 counts COCYCLES. Matches the design probe
    `s7a_cocycle_reach.py` (32), as the charge requires -/
theorem s7_nest_cocycles_32 :
    unitsZi.length = 4 ∧ (4 * 4 * 4 : Nat) = 64 ∧
    slotList.length = 8 ∧ cocycleTriples.length = 32 := by decide

/-- every unit-valued cocycle's parameter triple is one of the 32 — the
    tie that makes the count above a count of the objects, not of a
    look-alike index set -/
theorem cocycle_triple_in_nest (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    (cocycleTriples.any fun t =>
      decide (t = (F 1 0 0, F 0 0 1, F 1 1 1))) = true := by
  have hf := cocycle_f_sq_one F hu hc
  rcases norm_one_units (F 1 0 0) (hu 1 0 0 (by decide) (by decide) (by decide))
    with h1 | h1 | h1 | h1 <;>
  rcases norm_one_units (F 0 0 1) (hu 0 0 1 (by decide) (by decide) (by decide))
    with h2 | h2 | h2 | h2 <;>
  rcases norm_one_units (F 1 1 1) (hu 1 1 1 (by decide) (by decide) (by decide))
    with h3 | h3 | h3 | h3 <;>
  rw [h1, h2, h3] at hf ⊢ <;>
  first
    | exact absurd hf (by decide)
    | decide

/-- a gauge quadruple read as the kernel's η : Nat → Nat → Zi -/
def gaugeFn (g : Zi × Zi × Zi × Zi) (a b : Nat) : Zi :=
  if a = 0 ∧ b = 0 then g.1 else if a = 0 ∧ b = 1 then g.2.1
  else if a = 1 ∧ b = 0 then g.2.2.1 else g.2.2.2

/-- the coboundary's 8-slot value vector. Division-free: the quotient
    num/den is `mul num (conj den)`, which is EXACT here because a gauge
    quadruple is unit-valued, so den is a unit and conj den = den⁻¹
    (`unit_mul_conj`) -/
def cobVec (g : Zi × Zi × Zi × Zi) : List Zi :=
  slotList.map fun t =>
    mul (detaNum (gaugeFn g) t.1 t.2.1 t.2.2)
        (conj (detaDen (gaugeFn g) t.1 t.2.1 t.2.2))

/-- the 16 coboundary representatives: η00 = η11 = 1, η01 and η10 free -/
def cobReps : List (List Zi) :=
  unitsZi.flatMap fun x => unitsZi.map fun y => cobVec (one, x, y, one)

/-- NEST — 16 COBOUNDARIES of 256 gauges (norm 9), in two halves.

    The 256 gauges are the 4 unit choices at each of the 4 vertices
    (4⁴ = 256); they are swept coordinate-wise below, never built as one
    256-element list.
    (i) REDUCTION: every gauge has the same coboundary as its normalized
        form (η00 = η11 = 1) — η00 rescales η01 and η10, and η11 cancels.
    (ii) DISTINCTNESS: the 16 normalized gauges have pairwise DISTINCT
        coboundary vectors.
    Together: the coboundary subgroup has exactly 16 elements, matching
    the design probe `s7a_cocycle_reach.py` (16).

    Both halves are swept as NESTS of 4 (4 x 4, and 4 x 4 x 4 x 4) rather
    than one flat traversal of 256, which keeps evaluation depth additive
    — no budget is raised anywhere in this file (HANDOFF guardrail). -/
theorem s7_nest_coboundaries_16 :
    unitsZi.length = 4 ∧ (4 * 4 * 4 * 4 : Nat) = 256 ∧
    cobReps.length = 16 ∧ (4 * 4 : Nat) = 16 := by
  decide

/-- (i) REDUCTION — all 256 gauges, as a 4 x 4 nest over (η00, η01), each
    slice sweeping its 16 remaining gauges -/
theorem s7_coboundary_reduces_to_normal_form :
    (unitsZi.all fun w => unitsZi.all fun x => unitsZi.all fun y =>
      unitsZi.all fun z =>
        decide (cobVec (w, x, y, z)
                  = cobVec (one, mul x (conj w), mul y (conj w), one))) = true := by
  decide

/-- (ii) DISTINCTNESS — the 16 normalized gauges give 16 different
    coboundaries: equal vectors force equal parameters -/
theorem s7_cobReps_distinct :
    (unitsZi.all fun x => unitsZi.all fun y => unitsZi.all fun x' =>
      unitsZi.all fun y' =>
        (decide (cobVec (one, x, y, one) = cobVec (one, x', y', one))
          == decide (x = x' ∧ y = y'))) = true := by
  decide

/-- NEST — 2 CLASSES, 16 + 16 = 32 (norm 9). The class label s·p·q takes
    exactly two of the four unit values over the 32 cocycles — `one` on
    16 of them and `neg one` on the other 16. Matches the design probe
    (2 classes, F(1,1,1) values {+1, −1}) -/
theorem s7_nest_classes_2 :
    (unitsZi.filter fun u =>
      cocycleTriples.any fun t => decide (mul (mul t.2.2 t.1) t.2.1 = u)).length = 2 ∧
    (cocycleTriples.filter fun t =>
      decide (mul (mul t.2.2 t.1) t.2.1 = one)).length = 16 ∧
    (cocycleTriples.filter fun t =>
      decide (mul (mul t.2.2 t.1) t.2.1 = neg one)).length = 16 ∧
    16 + 16 = 32 := by decide

/- == the strengthened headline ========================================= -/

/-- `isUnit` is the norm-1 equation — the bridge that lets a concrete
    unit check be a `decide` on `normSq` -/
theorem isUnit_of_normSq_one (z : Zi) (h : normSq z = 1) : isUnit z := h

/-- THE STRENGTHENING, over the units of ℤ[i]. S3 proved "exactly two ON
    THE NORMALIZED SLICE" (`pentagon_exactly_two`, with the slot a gauge
    invariant of the slice, `gauge_slot_invariant`) and its docstring
    recorded the missing step verbatim: "NOT claimed: every class meets
    the slice." This supplies that step: every unit-valued cocycle is
    gauge-equivalent to a normalized representative whose free slot is
    +1 or −1, and that representative satisfies S3's own `pentagon`.

    STILL NOT CLAIMED (norm 6): the continuous H³(Z₂, U(1)) = Z₂. That
    sentence is about the CONTINUOUS unit group and is out of zero-import
    reach; nothing here reaches it, and the name says ℤ[i]. -/
theorem exactly_two_over_zi_units (F : Nat → Nat → Nat → Zi)
    (hu : unitCochain F) (hc : cocycle3 F) :
    ∃ eta : Nat → Nat → Zi, ∃ f : Zi,
      (f = one ∨ f = neg one) ∧ pentagon f ∧
      (∀ a b c : Nat, a < 2 → b < 2 → c < 2 →
        mul (F a b c) (detaNum eta a b c)
          = mul (Fnorm f a b c) (detaDen eta a b c)) := by
  rcases slice_lemma_over_zi_units F hu hc with ⟨eta, f, _, hpm, hslot⟩
  exact ⟨eta, f, hpm, (pentagon_exactly_two f).mpr hpm, hslot⟩

/- == S7 anti-vacuity: live instances (norm 3) ========================== -/

/-- live: BOTH classes are inhabited by genuine unit cocycles — the
    guarded ∀ of `slice_lemma_over_zi_units` is not vacuous -/
theorem live_both_classes_inhabited :
    cocycle3 (cochainOf one one one) ∧ cocycle3 (cochainOf one one (neg one)) ∧
    cochainOf one one one 1 1 1 = one ∧
    cochainOf one one (neg one) 1 1 1 = neg one :=
  ⟨cochainOf_is_cocycle one one one (isUnit_of_normSq_one _ (by decide))
     (isUnit_of_normSq_one _ (by decide)) (isUnit_of_normSq_one _ (by decide))
     (by decide),
   cochainOf_is_cocycle one one (neg one) (isUnit_of_normSq_one _ (by decide))
     (isUnit_of_normSq_one _ (by decide)) (isUnit_of_normSq_one _ (by decide))
     (by decide),
   rfl, rfl⟩

/-- live, off the real axis and off the normalized slice: `cochainOf I
    one I` is a genuine unit cocycle whose (1,0,0) slot is i — so it is
    NOT already normalized, and the gauge the lemma builds is NOT the
    identity. The lemma is exercised where it has work to do -/
theorem live_gaussian_cocycle_off_slice :
    cocycle3 (cochainOf I one I) ∧
    cochainOf I one I 1 0 0 = I ∧
    sliceGauge (cochainOf I one I) 1 0 = I ∧
    sliceGauge (cochainOf I one I) 1 0 ≠ one :=
  ⟨cochainOf_is_cocycle I one I (isUnit_of_normSq_one _ (by decide))
     (isUnit_of_normSq_one _ (by decide)) (isUnit_of_normSq_one _ (by decide))
     (by decide),
   rfl, rfl, by decide⟩

/-- live: the gauge the lemma reads off `cochainOf I one I` really does
    normalize it, at all 8 slots, onto the f = −1 representative -/
theorem live_slice_gauge_normalizes :
    (slotList.all fun t =>
      decide (mul (cochainOf I one I t.1 t.2.1 t.2.2)
                  (detaNum (sliceGauge (cochainOf I one I)) t.1 t.2.1 t.2.2)
                = mul (Fnorm (neg one) t.1 t.2.1 t.2.2)
                      (detaDen (sliceGauge (cochainOf I one I))
                               t.1 t.2.1 t.2.2))) = true := by
  decide

/- == S7 negative controls (norm 5) ===================================== -/

/-- the design probe's witness: `one` on every slot except `I` at
    (1,1,0). The two superseded probes mistook it for a counterexample
    to the slice lemma; it is not a cocycle, so it was never a class -/
def controlCochainA (a b c : Nat) : Zi :=
  if a = 1 ∧ b = 1 ∧ c = 0 then I else one

/-- NEGATIVE CONTROL A (the COCYCLE hypothesis carries the lemma): the
    witness is unit-valued but is NOT a cocycle, and NO gauge and no unit
    f normalize it — all 256 gauges x 4 units fail. Drop the cocycle
    hypothesis from the slice lemma and it is false; the force comes from
    the hypothesis, not from the shape (charge §4) -/
theorem control_A_not_a_cocycle_and_never_normalized :
    unitCochain controlCochainA ∧ ¬ cocycle3 controlCochainA ∧
    (unitsZi.all fun w => unitsZi.all fun x => unitsZi.all fun y =>
      unitsZi.all fun z => unitsZi.all fun f =>
        (slotList.all fun t =>
          decide (mul (controlCochainA t.1 t.2.1 t.2.2)
                      (detaNum (gaugeFn (w, x, y, z)) t.1 t.2.1 t.2.2)
                    = mul (Fnorm f t.1 t.2.1 t.2.2)
                          (detaDen (gaugeFn (w, x, y, z))
                                   t.1 t.2.1 t.2.2))) == false) = true := by
  refine ⟨?_, ?_, by decide⟩
  · intro a b c ha hb hcc
    have ha' : a = 0 ∨ a = 1 := by omega
    have hb' : b = 0 ∨ b = 1 := by omega
    have hc' : c = 0 ∨ c = 1 := by omega
    rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
      rcases hc' with rfl | rfl <;> exact isUnit_of_normSq_one _ (by decide)
  · intro h
    have := h 1 1 0 0 (by decide) (by decide) (by decide) (by decide)
    exact absurd this (by decide)

/-- NEGATIVE CONTROL B (the RIGHT gauge carries it): a genuine cocycle —
    `cochainOf I one I`, class label −1 — is NOT normalized by the
    IDENTITY gauge; it fails already at the (1,0,0) slot. Compare
    `live_slice_gauge_normalizes`, where the gauge the lemma actually
    builds normalizes the SAME cochain at all 8 slots. So the lemma's
    content is the construction of the gauge, not a property of the
    shape (charge §4) -/
theorem control_B_identity_gauge_fails :
    mul (cochainOf I one I 1 0 0) (detaNum (fun _ _ : Nat => one) 1 0 0)
      ≠ mul (Fnorm (neg one) 1 0 0) (detaDen (fun _ _ : Nat => one) 1 0 0) := by
  decide
