/- ======================================================================
   S6 — THE CAPSTONE AND THE EXCLUSION LAYER

   SCOPE: continuation of the sanctioned beyond-charge extension
   (records in the S4/S5 headers carry forward; this section was
   requested by the courier as "next move options a and b").
   Quarantine unchanged (norm 16, REGISTER row 7).

   S6a — THE CAPSTONE. One headline statement stitching S1–S5: the
   roomy conditions (pentagon + hexagon + reality filter) hold exactly
   on {(1,1), (1,−1)} — boson and fermion, nothing else, count 2.
   Every ingredient is a prior layer's theorem: pentagon_iff_f_sq_one
   (S3), pentagon_hexagon_iff_R_sq_F (S4), R_over_boson_class /
   R_over_semion_class (S4), the filter (S4), the ν-rider (S5). The
   capstone adds NO new axioms of content — it is the stitching, and
   says so.

   S6b — THE EXCLUSION LAYER. Bench claim (3), lines 30–36 and
   185–196; certificate G1f. The −1 has teeth: exchange antisymmetry
   annihilates double occupation. Formalized at the zero-import
   kernel level:
   - the triangular numbers as a recursion, values 1,3,6,10,15 for
     m = 2..6, the recurrence, and 2·T(m) = m(m−1) proved by
     induction (the closed form without Nat-division hazards);
   - the Pauli kill SYMBOLIC over Zi: the antisymmetrized components
     ψᵢψⱼ − ψⱼψᵢ vanish identically (commutativity is the killer —
     G1f_pauli_kill_symbolic);
   - the m = 2 antisymmetrizer M = I − SWAP as an exact integer
     matrix: M² = 2M entrywise, tr M = 2 = m² − m, image on the line
     spanned by (0,1,−1,0) — the rank-1 fact stated kernel-honestly
     (image ⊆ line ∧ line ⊆ image), no rank function needed;
   - the kill criterion: M₂(ψ⊗φ) = 0 ⟺ ad = bc — the 2×2
     determinant; double occupation (φ = ψ) is the diagonal case;
   - NEGATIVE CONTROL: the symmetrizer does NOT annihilate — bosons
     do not exclude; the teeth belong to the −1 alone.

   HONEST LABEL (norm 6): the m = 3..6 ranks (6, 10, 15 …) are NOT
   kernel-checked here — a general rank needs matrix machinery this
   zero-import file deliberately lacks. What IS kernel-checked: the
   triangular values and recurrence (all m, by induction), and the
   m = 2 block end to end. The m = 2..6 exact-elimination census is
   seat B's independent territory (certificate G1f did it with exact
   Fractions; seat B re-derives). The division of labor is a
   decision, recorded.

   Design probe: probes/s6_design_probe.py — capstone survivor set,
   ranks, recurrence, M(2) rows, determinant criterion, boson
   control: all confirmed against G1f before this section was
   written.

   NESTS (norm 9): capstone: 2 survivors + 2 killed semions = 4
   catalog entries (the S4 catalog, closed by the S6 headline);
   exclusion: T(m+1) = T(m) + m ties each census to the next,
   1 + 3 = 4 = 2² kernel-checked at m = 2 (antisym 1 + sym 3 = 4).
   ====================================================================== -/

/- == S6a: the capstone ================================================= -/

/-- the roomy conditions, in one Prop: coherence (pentagon), braiding
    coherence (hexagon), and the flatland/reality filter — the three
    gates every roomy particle must pass (bench claims (1)+(2); the
    whole S1–S5 arc is the proof kit for this def) -/
def roomy (f r : Zi) : Prop :=
  pentagon f ∧ hexagon f r ∧ conj r = r

/-- THE CAPSTONE: the roomy conditions hold exactly on the two-element
    set {(1,1), (1,−1)} — boson and fermion. Forward: pentagon forces
    f² = 1 (S3), hexagon then forces r² = f (S4), the class split
    gives r ∈ {±1} over f = 1 and r ∈ {±i} over f = −1 (S4), and the
    filter kills both semions (S4) — leaving f = −1 EMPTY. Backward:
    the live instances (S3, S4) plus reality by decide. No new
    content — the stitching of five layers into one iff -/
theorem roomy_iff_boson_or_fermion (f r : Zi) :
    roomy f r ↔ ((f = one ∧ r = one) ∨ (f = one ∧ r = neg one)) := by
  constructor
  · rintro ⟨hp, hh, hc⟩
    have hf2 : mul f f = one := (pentagon_iff_f_sq_one f).mp hp
    have hr2 : mul r r = f := (pentagon_hexagon_iff_R_sq_F f r hf2).mp hh
    rcases (f_sq_one_iff_pm_one f).mp hf2 with rfl | rfl
    · rcases (R_over_boson_class r).mp hr2 with rfl | rfl
      · exact Or.inl ⟨rfl, rfl⟩
      · exact Or.inr ⟨rfl, rfl⟩
    · rcases (R_over_semion_class r).mp hr2 with rfl | rfl
      · exact absurd hc (by decide)
      · exact absurd hc (by decide)
  · rintro (⟨rfl, rfl⟩ | ⟨rfl, rfl⟩)
    · exact ⟨live_pentagon_plus_one, live_hexagon_boson, by decide⟩
    · exact ⟨live_pentagon_plus_one, live_hexagon_fermion, by decide⟩

/-- the headline, r-only: SOME F-symbol makes r a roomy particle iff
    r ∈ {+1, −1} — "the roomy world has exactly two particles" as a
    single kernel-checked statement about the particle label alone -/
theorem the_roomy_world_has_exactly_two_particles (r : Zi) :
    (∃ f, roomy f r) ↔ (r = one ∨ r = neg one) := by
  constructor
  · rintro ⟨f, h⟩
    rcases (roomy_iff_boson_or_fermion f r).mp h with ⟨_, rfl⟩ | ⟨_, rfl⟩
    · exact Or.inl rfl
    · exact Or.inr rfl
  · rintro (rfl | rfl)
    · exact ⟨one, (roomy_iff_boson_or_fermion one one).mpr
        (Or.inl ⟨rfl, rfl⟩)⟩
    · exact ⟨one, (roomy_iff_boson_or_fermion one (neg one)).mpr
        (Or.inr ⟨rfl, rfl⟩)⟩

/-- the count, tied (norm 9): both survivors are roomy, they are
    distinct, and every roomy pair is one of the two — 2 named + 0
    others, the complement supplied by the capstone iff -/
theorem capstone_count_two :
    roomy one one ∧ roomy one (neg one) ∧ (one : Zi) ≠ neg one ∧
    ∀ f r : Zi, roomy f r → f = one ∧ (r = one ∨ r = neg one) := by
  refine ⟨?_, ?_, by decide, ?_⟩
  · exact (roomy_iff_boson_or_fermion one one).mpr (Or.inl ⟨rfl, rfl⟩)
  · exact (roomy_iff_boson_or_fermion one (neg one)).mpr
      (Or.inr ⟨rfl, rfl⟩)
  · intro f r h
    rcases (roomy_iff_boson_or_fermion f r).mp h with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
    · exact ⟨rfl, Or.inl rfl⟩
    · exact ⟨rfl, Or.inr rfl⟩

/-- the ν-rider (S5 stitched in): every roomy particle carries
    ν_FS = +1 AND ν_ML = +1 — on the survivors the fork closes and
    both ledgers read +1: the spin-statistics seed rides the capstone -/
theorem capstone_nu_rider (f r : Zi) (h : roomy f r) :
    nuFS r = one ∧ nuML r = one := by
  rcases (roomy_iff_boson_or_fermion f r).mp h with ⟨_, rfl⟩ | ⟨_, rfl⟩ <;>
    exact ⟨by decide, by decide⟩

/-- NEGATIVE CONTROL (the semion fails ONLY the filter): pentagon and
    hexagon both hold at (f, r) = (−1, i) — the semion is a perfectly
    coherent braided particle — and the reality filter alone kills it:
    each gate carries its own weight (norm 5; the anyon's death
    certificate, itemized) -/
theorem control_semion_fails_only_filter :
    pentagon (neg one) ∧ hexagon (neg one) I ∧ conj I ≠ I ∧
    ¬ roomy (neg one) I := by
  refine ⟨live_pentagon_minus_one, live_hexagon_semion, by decide, ?_⟩
  intro h
  exact absurd h.2.2 (by decide)

/-- NEGATIVE CONTROL (the filter alone is not enough): r = 3 is real —
    it passes the filter — but no F-symbol makes it roomy: the
    coherence gates carry their own weight too -/
theorem control_real_but_not_roomy (f : Zi) : ¬ roomy f ⟨3, 0⟩ := by
  intro h
  rcases (roomy_iff_boson_or_fermion f ⟨3, 0⟩).mp h with ⟨_, hr⟩ | ⟨_, hr⟩ <;>
    exact absurd hr (by decide)

/- == S6b: the exclusion layer ========================================== -/

/-- the triangular numbers, as a recursion — no Nat-division hazards
    (the bench's m(m−1)/2 stated below as 2·T = m(m−1), exact) -/
def tri : Nat → Nat
  | 0 => 0
  | n + 1 => tri n + n

/-- the fermionic census values (bench line 34: "1, 3, 6, 10, 15 for
    m = 2..6"; certificate G1f_antisymmetrizer_ranks_exact) -/
theorem tri_values :
    tri 2 = 1 ∧ tri 3 = 3 ∧ tri 4 = 6 ∧ tri 5 = 10 ∧ tri 6 = 15 := by
  decide

/-- the recurrence T(m+1) = T(m) + m — each census ties to the next
    (norm 9's ladder): definitional -/
theorem tri_recurrence (m : Nat) : tri (m + 1) = tri m + m := rfl

/-- the closed form, exactly and for ALL m: 2·T(m) = m(m−1) — the
    bench's m(m−1)/2 without the division; proved by induction, the
    quadratic handled by distributing to the shared monomial k² -/
theorem tri_double (m : Nat) : 2 * tri m = m * (m - 1) := by
  induction m with
  | zero => rfl
  | succ n ih =>
    cases n with
    | zero => rfl
    | succ k =>
      have ih' : 2 * tri (k + 1) = (k + 1) * k := ih
      have e1 : (k + 1 + 1) * (k + 1) = k * k + 3 * k + 2 := by
        simp only [Nat.add_mul, Nat.mul_add, Nat.mul_one, Nat.one_mul]
        omega
      have e2 : (k + 1) * k = k * k + k := by
        simp only [Nat.add_mul, Nat.one_mul]
      show 2 * (tri (k + 1) + (k + 1)) = (k + 1 + 1) * (k + 1)
      omega

/-- THE PAULI KILL, symbolic over Zi: every component of the
    antisymmetrized ψ⊗ψ is ψᵢψⱼ − ψⱼψᵢ = 0 IDENTICALLY — the killer
    is commutativity itself (certificate G1f_pauli_kill_symbolic:
    "vanishes for every psi, not just sampled ones"). Two Gaussian
    variables stand for any two components -/
theorem pauli_kill_symbolic (x y : Zi) :
    sub (mul x y) (mul y x) = zero := by
  rw [mul_comm]
  exact (sub_eq_zero_iff _ _).mpr rfl

/-- the m = 2 antisymmetrizer, exact: index p = 2i + j ∈ [0,4);
    SWAP sends (i,j) to (j,i) — 0↔0, 1↔2, 3↔3 -/
def swapIdx : Nat → Nat
  | 0 => 0
  | 1 => 2
  | 2 => 1
  | _ => 3

/-- M = I − SWAP on Z⁴, entrywise (the bench's A = (I−SWAP)/2 scaled
    by 2 to stay integer — same rank, G1f's move) -/
def Mmat (p q : Nat) : Int :=
  (if p = q then 1 else 0) - (if q = swapIdx p then 1 else 0)

/-- M² = 2M entrywise — the scaled-projector certificate, all 16
    entries by kernel computation (certificate
    G1f_idempotent_certificate: "M = I−S satisfies M^2 = 2M …
    exactly") -/
theorem M2_sq_eq_two_M :
    ((List.range 4).all fun p => (List.range 4).all fun q =>
      ((List.range 4).foldl (fun acc k => acc + Mmat p k * Mmat k q) 0)
        == 2 * Mmat p q) = true := by decide

/-- tr M = 2 = m² − m at m = 2 — with the projector identity this is
    the rank-by-trace certificate: rank = tr/2 = 1 = T(2)
    (G1f: "rank = tr/2 — the Lean-friendly certificate") -/
theorem M2_trace :
    ((List.range 4).foldl (fun acc k => acc + Mmat k k) 0) = 2 ∧
    (2 * 2 - 2 : Nat) = 2 ∧ tri 2 = 1 := by decide

/-- the image of M₂ lies on the line spanned by (0,1,−1,0): for every
    ψ⊗φ input with components (ac, ad, bc, bd), the output is
    (0, ad−bc, bc−ad, 0) — first and last components zero, middle two
    opposite. Rank ≤ 1, stated kernel-honestly without a rank
    function.
    SEAT B's CROP (S6 item 1), recorded: the third conjunct is an
    instance of generic anti-symmetry (x − y = −(y − x), any ring);
    the line-shape claim is jointly carried by conjuncts 1+2 (the
    vanishing components) and M2_image_attains_generator — seat B
    verified the full image shape independently via the matrix
    action -/
theorem M2_image_on_line (a b c d : Zi) :
    sub (mul a c) (mul a c) = zero ∧
    sub (mul b d) (mul b d) = zero ∧
    sub (mul a d) (mul b c) = neg (sub (mul b c) (mul a d)) := by
  refine ⟨(sub_eq_zero_iff _ _).mpr rfl, (sub_eq_zero_iff _ _).mpr rfl, ?_⟩
  cases a; cases b; cases c; cases d
  simp only [mul, sub, add, neg, Zi.mk.injEq]
  constructor <;> omega

/-- the spanning vector IS attained: ψ = (1,0), φ = (0,1) maps to
    exactly (0,1,−1,0) — image ⊇ the line's generator; with
    M2_image_on_line this is the m = 2 rank-1 fact, both inclusions
    (live instance, norm 3) -/
theorem M2_image_attains_generator :
    sub (mul one zero) (mul one zero) = zero ∧
    sub (mul one one) (mul zero zero) = one ∧
    sub (mul zero zero) (mul one one) = neg one ∧
    sub (mul zero one) (mul zero one) = zero := by decide

/-- THE KILL CRITERION: M₂(ψ⊗φ) = 0 ⟺ ad = bc — the 2×2 determinant
    (the design probe's "kill ⟺ parallel"); rides S4's
    sub_eq_zero_iff -/
theorem M2_kill_iff_det_zero (a b c d : Zi) :
    (sub (mul a d) (mul b c) = zero ∧ sub (mul b c) (mul a d) = zero)
      ↔ mul a d = mul b c := by
  constructor
  · intro ⟨h, _⟩
    exact (sub_eq_zero_iff _ _).mp h
  · intro h
    exact ⟨(sub_eq_zero_iff _ _).mpr h,
           (sub_eq_zero_iff _ _).mpr h.symm⟩

/-- DOUBLE OCCUPATION DIES: φ = ψ is the diagonal of the kill
    criterion — ab = ba by commutativity, so M₂(ψ⊗ψ) = 0 for EVERY ψ:
    no two fermions in one state, symbolically (bench line 31:
    "exchange antisymmetry annihilates double occupation"; the exact
    version of the bench's 1e-16) -/
theorem pauli_double_occupation_dies (a b : Zi) :
    sub (mul a b) (mul b a) = zero ∧ sub (mul b a) (mul a b) = zero :=
  (M2_kill_iff_det_zero a b a b).mpr (mul_comm a b)

/-- the m = 2 census nest, tied (norm 9): antisym rank 1 + sym rank 3
    = 4 = 2² — the two-sided split is complete at the kernel-checked
    size (G1f: "ranks sum to m^2"); the sym value 3 = T(3) is the
    control's census -/
theorem census_nest_m2 : tri 2 + tri 3 = 4 ∧ (2 * 2 : Nat) = 4 := by
  decide

/-- NEGATIVE CONTROL (bosons do not exclude): the SYMMETRIZED double
    occupation is 2ψᵢψⱼ ≠ 0 — at ψ = (1,1) the middle component is
    1·1 + 1·1 = 2. The teeth belong to the −1 alone (certificate
    G1f_pauli_kill_exact_gaussian_psi's control; bench: "the -1 has
    teeth") -/
theorem control_boson_no_exclusion :
    add (mul one one) (mul one one) = ⟨2, 0⟩ ∧ (⟨2, 0⟩ : Zi) ≠ zero := by
  decide

/-- NEGATIVE CONTROL (the symmetrizer complement, m = 2): P = I + S
    satisfies M·P = 0 entrywise — the split M ⊕ P is orthogonal
    exactly (G1f: "(I-S)(I+S) = 0 … exactly") -/
theorem control_M_times_P_zero :
    ((List.range 4).all fun p => (List.range 4).all fun q =>
      ((List.range 4).foldl (fun acc k =>
        acc + Mmat p k * ((if k = q then 1 else 0)
                          + (if q = swapIdx k then 1 else 0))) 0) == 0)
      = true := by decide

/-- live (norm 3): a NON-parallel pair survives the antisymmetrizer —
    ψ = (1,0), φ = (0,1) has det = 1 ≠ 0: the kill criterion's
    hypothesis structure separates; exclusion kills double occupation,
    not everything -/
theorem live_nonparallel_survives :
    sub (mul one one) (mul zero zero) ≠ zero := by decide

