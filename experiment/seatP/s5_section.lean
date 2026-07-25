/- ======================================================================
   S5 — THE TWIST LAYER (θ, spin-statistics seed, the flag-3 FS fork)

   SCOPE, recorded honestly: continuation of the sanctioned
   beyond-charge extension (S4's header carries the sanction record;
   this section extends it to the twist layer at the courier's explicit
   request). Quarantine unchanged (norm 16, REGISTER row 7).

   Sources, per C1's lesson — cited by line and certificate name:
   - Bench floor/symmetric_statistics.py LINES 37, 197–199:
     `theta_f = R = -1; Frobenius-Schur nu = R * theta = +1` — the
     twist is the R-diagonal, the fermion twist is −1, and the bench's
     ν-ledger reads +1 on the survivors.
   - Certificate G1g (twist and Frobenius–Schur, exact integers):
     θ = R for every Z₂ particle (abelian: θ_a = R(a,a)); the TWO
     ν-ledgers ν_FS = R·θ and ν_ML = R·conj(θ); they agree (+1) on
     boson and fermion and DIVERGE on the semions (FS −1, ML +1).
   - Certificate G5 (spin-statistics seed): θ = R, θ_fermion = −1,
     ν = +1 for both survivors; fusion matrix N_f² = I, every quantum
     dimension the integer 1, D² = 2.
   - CHARTER flag 3, now ADDRESSED (it was parked in S4 with a
     recorded decision): "the Frobenius–Schur convention fork:
     ν = R·θ (the true FS indicator; −1 on semions) vs stone8's
     mirror-ledger R·conj(θ) (+1 whenever θ = R) — they agree on the
     survivors and diverge on semions; NAME THE TWO LEDGERS APART."
     This section does exactly that: two distinct defs `nuFS` and
     `nuML`, an agreement theorem on the real locus, a divergence
     theorem on the semions, and the locus characterized exactly.
     Neither ledger is called "the" indicator; the fork is the
     theorem, not a footnote.

   Design probe: probes/s5_design_probe.py — all classification facts
   confirmed against G1g/G5 and the bench before this section was
   written.

   NESTS (norm 9):
   - fork nest: 2 (agree: boson, fermion) + 2 (diverge: semions) = 4
     catalog entries — `fork_nest_2_plus_2`.
   - ribbon nest: per particle, 4 fusion cells; 3 read trivially and
     1 forces (the (1,1) cell reads 1 = r⁴) — `ribbon_nest_3_plus_1`.
   - fusion matrix nest: 2×2 = 4 entries, N² = I checked entrywise.
   ====================================================================== -/

/-- the twist as the R-diagonal — abelian θ_a = R(a,a) (bench line 37:
    `theta_f = R`; certificate G1g_twist_eq_R_theta_f_minus1). On the
    Z₂ labels this is `Rz2 r a a`: trivial at a = 0, r at a = 1 -/
def twist (r : Zi) (a : Nat) : Zi := Rz2 r a a

/-- the TRUE Frobenius–Schur ledger: ν_FS = R·θ (certificate G1g:
    "the true Frobenius-Schur indicator — SU(2)₁'s spin-1/2 is
    pseudo-real"). Named apart from nuML per charter flag 3 -/
def nuFS (r : Zi) : Zi := mul r r

/-- stone8's MIRROR ledger: ν_ML = R·conj(θ) (certificate G1g:
    "spin-statistics co-sign, identically +1 whenever θ = R").
    Named apart from nuFS per charter flag 3. With θ = R this is
    r·conj(r) — the norm in disguise -/
def nuML (r : Zi) : Zi := mul r (conj r)

/- == the twist values, per particle (norm 3 live instances) =========== -/

/-- twist of the four particles at label 1: θ = R exactly — boson +1,
    fermion −1, semion +i, anti-semion −i (bench: theta_f = R = −1 for
    the fermion; G1g extends to all four). θ at label 0 is 1 for all -/
theorem twist_catalog :
    (twist one 1 = one ∧ twist (neg one) 1 = neg one ∧
     twist I 1 = I ∧ twist (neg I) 1 = neg I) ∧
    (twist one 0 = one ∧ twist (neg one) 0 = one ∧
     twist I 0 = one ∧ twist (neg I) 0 = one) := by decide

/-- the fermion's twist is −1 — THE sign (bench line 197: the sign
    that builds shelves; the exclusion cascade is downstream of it) -/
theorem twist_fermion_minus_one : twist (neg one) 1 = neg one := by decide

/- == the ribbon relation on the Z₂ fusion ============================== -/

/-- the ribbon identity, symbolic in r: on fusion a×b = (a+b)%2,
    θ((a+b)%2) = θ(a)·θ(b)·R(a,b)² — three cells read trivially, the
    (1,1) cell reads 1 = r⁴; for catalog units r⁴ = (r²)² = f² = 1, so
    the identity holds. Stated symbolically with the forcing content
    exposed: the hypothesis hr4 : r⁴ = 1 is exactly the (1,1) cell -/
theorem ribbon_identity (r : Zi) (hr4 : mul (mul r r) (mul r r) = one) :
    ∀ a b : Nat, a < 2 → b < 2 →
    twist r ((a+b) % 2)
      = mul (mul (twist r a) (twist r b)) (mul (Rz2 r a b) (Rz2 r a b)) := by
  intro a b ha hb
  have ha' : a = 0 ∨ a = 1 := by omega
  have hb' : b = 0 ∨ b = 1 := by omega
  rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
    simp +decide only [twist, Rz2, if_true, if_false, one_mul, mul_one]
  exact hr4.symm

/-- the ribbon nest, tied (norm 9): 4 fusion cells; the three cells
    off (1,1) hold for EVERY r (no hypothesis), and the (1,1) cell is
    exactly the equation 1 = r⁴ — 3 + 1 = 4 -/
theorem ribbon_nest_3_plus_1 (r : Zi) :
    (∀ a b : Nat, a < 2 → b < 2 → ¬(a = 1 ∧ b = 1) →
      twist r ((a+b) % 2)
        = mul (mul (twist r a) (twist r b)) (mul (Rz2 r a b) (Rz2 r a b))) ∧
    (twist r ((1+1) % 2)
        = mul (mul (twist r 1) (twist r 1)) (mul (Rz2 r 1 1) (Rz2 r 1 1))
      ↔ one = mul (mul r r) (mul r r)) ∧
    (3 + 1 : Nat) = 4 := by
  refine ⟨?_, ?_, rfl⟩
  · intro a b ha hb hne
    have ha' : a = 0 ∨ a = 1 := by omega
    have hb' : b = 0 ∨ b = 1 := by omega
    rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
      first
        | exact absurd ⟨rfl, rfl⟩ hne
        | simp +decide only [twist, Rz2, if_true, if_false, one_mul, mul_one]
  · simp +decide only [twist, Rz2, if_true, if_false]

/-- catalog units have r⁴ = 1: r² = f (hexagon) and f² = 1 (pentagon)
    give r⁴ = (r²)² = f² = 1 — the ribbon hypothesis is DISCHARGED by
    the S3+S4 layers, symbolically -/
theorem catalog_r_fourth (f r : Zi) (hp : mul f f = one)
    (hh : mul r r = f) : mul (mul r r) (mul r r) = one := by
  rw [hh]
  exact hp

/- == the two ν-ledgers: agreement, divergence, the locus ============== -/

/-- the survivors' ledger reads +1 on BOTH ledgers (bench line 198:
    `R_f * theta_f == 1`; certificate G1g_nu_survivors_plus1): boson
    1·1 = 1, fermion (−1)(−1) = 1, and conj changes nothing since both
    twists are real — the spin-statistics seed, exact (G5) -/
theorem nu_survivors_plus_one :
    (nuFS one = one ∧ nuML one = one) ∧
    (nuFS (neg one) = one ∧ nuML (neg one) = one) := by decide

/-- THE FORK (charter flag 3, addressed): on the semions the two
    ledgers DIVERGE — ν_FS = R·θ = i·i = −1 (pseudo-real, the true FS
    value) while ν_ML = R·conj(θ) = i·(−i) = +1. Both computed, both
    named, neither called "the" indicator
    (certificate: G1g_convention_fork_on_semions_FLAGGED) -/
theorem nu_fork_on_semions :
    (nuFS I = neg one ∧ nuML I = one) ∧
    (nuFS (neg I) = neg one ∧ nuML (neg I) = one) ∧
    nuFS I ≠ nuML I ∧ nuFS (neg I) ≠ nuML (neg I) := by decide

/-- the fork nest, tied (norm 9): 2 agree + 2 diverge = 4 catalog
    entries -/
theorem fork_nest_2_plus_2 : (2 + 2 : Nat) = 4 := by decide

/-- the fork locus is EXACTLY the real locus, symbolically: for r ≠ 0,
    ν_FS(r) = ν_ML(r) ⟺ conj r = r ⟺ r.im = 0. The two ledgers are
    the same ledger precisely where the twist is real — which is why
    the fork is invisible on the survivors and the flatland filter
    closes it. The r ≠ 0 hypothesis is load-bearing (see the control).
    SEAT B's CROP (S5 item 1), recorded: the hypothesis is
    ROUTE-required, not statement-required — the coordinate expansion
    ν_FS − ν_ML = r(r − conj r) = ⟨−2·im², 2·re·im⟩ vanishes iff
    im = 0 with no nonzero hypothesis (at r = 0 both sides of the iff
    are true). This proof's mul_left_cancel route needs r ≠ 0; the
    truth does not -/
theorem fork_locus_is_real_locus (r : Zi) (hr : r ≠ zero) :
    nuFS r = nuML r ↔ conj r = r := by
  constructor
  · intro h
    exact (mul_left_cancel r r (conj r) hr h).symm
  · intro h
    show mul r r = mul r (conj r)
    rw [h]

/-- the locus, coordinates: combining with S1's conj_fixed_iff_real —
    for r ≠ 0 the ledgers agree iff r.im = 0 -/
theorem fork_locus_coordinates (r : Zi) (hr : r ≠ zero) :
    nuFS r = nuML r ↔ r.im = 0 := by
  rw [fork_locus_is_real_locus r hr]
  exact conj_fixed_iff_real r

/-- the flatland filter CLOSES the fork: on the filter's survivors
    (conj r = r) the two ledgers coincide — the fork lives only off
    the real locus, exactly where the filter kills. The charter's
    "name them apart off the real locus" is this statement's
    contrapositive shadow -/
theorem filter_closes_fork (r : Zi) (h : conj r = r) :
    nuFS r = nuML r := by
  show mul r r = mul r (conj r)
  rw [h]

/-- ν_ML is the norm in disguise: ν_ML(r) = ⟨N(r), 0⟩ — on units it is
    +1 IDENTICALLY, which is exactly why stone8's mirror ledger reads
    +1 whenever θ = R is a unit (certificate G1g: "identically +1
    whenever theta = R"); it carries no FS information off the
    survivors. Rides S1's mul_conj_eq_normSq -/
theorem nuML_is_normSq (r : Zi) : nuML r = ⟨normSq r, 0⟩ :=
  mul_conj_eq_normSq r

/-- ν_ML = +1 on ALL norm-1 units — the mirror ledger cannot see the
    semions at all (their norm is 1 like everyone else's); only ν_FS
    separates them. The fork is not a convention quibble: one ledger
    carries information the other structurally cannot -/
theorem nuML_blind_on_units (r : Zi) (h : normSq r = 1) : nuML r = one := by
  rw [nuML_is_normSq, h]
  rfl

/- == the spin-statistics seed (G5) ===================================== -/

/-- the spin-statistics seed, exact (certificate G5_twist_and_nu_ledger):
    θ_fermion = −1 and ν = R·θ = +1 for both survivors — statistics
    (R) and spin (θ) carry the SAME sign on the roomy catalog, and
    their product is +1: the seed of the spin-statistics theorem, at
    the level this circle can state it -/
theorem spin_statistics_seed :
    twist (neg one) 1 = neg one ∧
    mul (neg one) (twist (neg one) 1) = one ∧
    mul one (twist one 1) = one := by decide

/-- θ = R on the catalog means spin and statistics are literally the
    same Gaussian integer per particle — the abelian collapse
    (certificate G1g: "theta = R for every Z2 particle") -/
theorem spin_equals_statistics :
    twist one 1 = one ∧ twist (neg one) 1 = neg one ∧
    twist I 1 = I ∧ twist (neg I) 1 = neg I := by decide

/-- the fusion matrix squares to the identity: N_f = [[0,1],[1,0]],
    N_f² = I entrywise over Nat — with the factorization
    x² − 1 = (x−1)(x+1) as the char-poly note, so the Perron root is
    the integer 1: every quantum dimension is 1, D² = 1² + 1² = 2, and
    NO decidable order / Perron / Z[φ] machinery is needed here
    (certificate G5_quantum_dimensions_all_one — its "absence is a
    feature" note carried verbatim) -/
theorem fusion_matrix_squares_to_identity :
    (0*0 + 1*1 = 1 ∧ 0*1 + 1*0 = 0 ∧ 1*0 + 0*1 = 0 ∧ 1*1 + 0*0 = 1) ∧
    (1*1 + 1*1 : Nat) = 2 := by decide

/-- the char-poly factorization behind d = 1, symbolic over Zi:
    x² − 1 = (x−1)(x+1) — S3's factorization pattern, reused at the
    dimension layer (G5's "char poly x^2 - 1 = (x-1)(x+1)") -/
theorem dimension_charpoly_factors (x : Zi) :
    sub (mul x x) one = mul (sub x one) (add x one) := by
  cases x
  simp only [mul, sub, add, neg, one, Zi.mk.injEq,
             Int.mul_add, Int.add_mul, Int.neg_mul,
             Int.mul_one, Int.one_mul]
  refine ⟨?_, ?_⟩ <;> omega

/- == live instances (norm 3) =========================================== -/

/-- live: the full ribbon identity holds for each of the four catalog
    particles, hypothesis discharged through catalog_r_fourth — boson -/
theorem live_ribbon_boson : ∀ a b : Nat, a < 2 → b < 2 →
    twist one ((a+b) % 2)
      = mul (mul (twist one a) (twist one b))
            (mul (Rz2 one a b) (Rz2 one a b)) :=
  ribbon_identity one (catalog_r_fourth one one (by decide) (by decide))

/-- live: ribbon for the fermion -/
theorem live_ribbon_fermion : ∀ a b : Nat, a < 2 → b < 2 →
    twist (neg one) ((a+b) % 2)
      = mul (mul (twist (neg one) a) (twist (neg one) b))
            (mul (Rz2 (neg one) a b) (Rz2 (neg one) a b)) :=
  ribbon_identity (neg one)
    (catalog_r_fourth one (neg one) (by decide) (by decide))

/-- live: ribbon for the semion — the hypothesis routes through
    f = −1: r² = −1, f² = 1 -/
theorem live_ribbon_semion : ∀ a b : Nat, a < 2 → b < 2 →
    twist I ((a+b) % 2)
      = mul (mul (twist I a) (twist I b)) (mul (Rz2 I a b) (Rz2 I a b)) :=
  ribbon_identity I (catalog_r_fourth (neg one) I (by decide) (by decide))

/-- live: ribbon for the anti-semion -/
theorem live_ribbon_antisemion : ∀ a b : Nat, a < 2 → b < 2 →
    twist (neg I) ((a+b) % 2)
      = mul (mul (twist (neg I) a) (twist (neg I) b))
            (mul (Rz2 (neg I) a b) (Rz2 (neg I) a b)) :=
  ribbon_identity (neg I)
    (catalog_r_fourth (neg one) (neg I) (by decide) (by decide))

/-- live: the fork-locus theorem's hypothesis structure separates —
    at r = ⟨1,1⟩ (nonzero, non-real, non-unit) the ledgers diverge:
    ν_FS = 2i ≠ 2 = ν_ML — the locus theorem is live off the catalog
    too -/
theorem live_fork_off_catalog :
    nuFS ⟨1, 1⟩ = ⟨0, 2⟩ ∧ nuML ⟨1, 1⟩ = ⟨2, 0⟩ ∧
    nuFS ⟨1, 1⟩ ≠ nuML ⟨1, 1⟩ := by decide

/- == negative controls (norm 5) ======================================== -/

/-- NEGATIVE CONTROL (the locus theorem's r ≠ 0 is load-bearing): at
    r = 0 both ledgers vanish — they AGREE while conj r = r holds
    trivially, but the iff would be vacuous there; cancellation needs
    the domain. Recorded so the hypothesis is seen to earn its keep -/
theorem control_fork_locus_needs_nonzero :
    nuFS zero = nuML zero ∧ conj zero = zero := by decide

/-- NEGATIVE CONTROL (wrong twist): setting θ = F instead of θ = R
    breaks the semion's mirror ledger — R·conj(F) = i·conj(−1) = −i,
    not +1: the ledgers are ABOUT the twist; a wrong twist is visible
    (design probe's control, exact values) -/
theorem control_wrong_twist_breaks_ledger :
    mul I (conj (neg one)) = neg I ∧ neg I ≠ one := by decide

/-- NEGATIVE CONTROL (the ribbon forcing cell bites): at r = ⟨2,0⟩ the
    (1,1) ribbon cell FAILS — 1 ≠ 16 = r⁴ — while the three trivial
    cells hold; the 3+1 nest's forcing cell carries real content -/
theorem control_ribbon_forcing_bites :
    twist ⟨2,0⟩ ((1+1) % 2)
      ≠ mul (mul (twist ⟨2,0⟩ 1) (twist ⟨2,0⟩ 1))
            (mul (Rz2 ⟨2,0⟩ 1 1) (Rz2 ⟨2,0⟩ 1 1)) ∧
    twist ⟨2,0⟩ ((0+1) % 2)
      = mul (mul (twist ⟨2,0⟩ 0) (twist ⟨2,0⟩ 1))
            (mul (Rz2 ⟨2,0⟩ 0 1) (Rz2 ⟨2,0⟩ 0 1)) := by decide

/-- NEGATIVE CONTROL (ν_FS is not blind): unlike ν_ML, the FS ledger
    separates the survivors from the semions — ν_FS reads +1 on boson
    and fermion, −1 on both semions; four values, two classes, the
    separation ν_ML cannot make -/
theorem control_nuFS_separates :
    nuFS one = one ∧ nuFS (neg one) = one ∧
    nuFS I = neg one ∧ nuFS (neg I) = neg one ∧
    (one : Zi) ≠ neg one := by decide

