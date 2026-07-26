# Phase 1 — RAW statements-only findings (recorded BEFORE any prose unsealed)

*SuperNinja instance 2, meta-auditor (REGISTER row 7). Written after reading
`courier/Zi_statements_v7.txt` end to end and NOTHING ELSE of the prose record.
At the moment of writing I have NOT opened: FINAL-EXPERIMENT-REPORT.md,
NORMS-RETROSPECTIVE.md, EXPERIMENT-REPORT.md, SUBROUND*-REPORT.md,
NOTE-TO-THIRD-BODY.md, CORRECTIONS-LETTER*.md, or any verify_zi*.py source.
I have read Zi.lean only to distinguish extractor-shape artifacts from math
defects on 3 specific lines (noted below); that is source, not prose record.*

## What I read
- `courier/Zi_statements_v7.txt`: 615 lines, 161 `theorem` lines, plus defs.
- The workshop canon is open by charter but I have NOT yet consulted it for these
  findings; these are pure "read the claims cold" reactions.

## Overall shape (cold reading)
The file tells a coherent story with no prose help:
S1 ring (Z[i] algebra) → S2 domain (no zero divisors, descent) → S3 pentagon
(`pentagon f ↔ f·f = one`, exactly {±1}) → S4 hexagon + gauge slice + unit
catalog → S5 twist/ribbon/Frobenius-Schur fork → S6 capstone
(`roomy = pentagon ∧ hexagon ∧ conj r = r`) ⇒ exactly two particles, plus a
Pauli/antisymmetrizer exclusion census at m=2. The naming is disciplined:
`live_*` = worked witnesses, `control_*` = negative controls, `*_nest_*` =
counted enumerations. Every count I can see ties to an explicit list/enum.

## FINDINGS

### F1 (INSTRUMENT DEFECT — courier) — inline `let` statements are silently truncated to vacuity
Three declarations use a `let … :=` binding *inside the statement type*.
`extract_statements.py` cuts every theorem at the first `:=`, so it discards
the actual proposition and emits only the fragment up to `let eta`/the def head:
- L266 `theorem live_gauge_witness :` → emitted as just `let eta` (claim dropped)
- L269 `theorem control_gauge_moves_slot :` → emitted as just `let eta` (claim dropped)
- L421 `def twist (r : Zi) (a : Nat) : Zi` → emitted with body dropped (it is `Rz2 r a a`)

Checked against source (Zi.lean L850–855, L862–865, L1339): the REAL statements
are substantive (live_gauge_witness asserts 3 gauge-invariance equalities AND
`eta 1 1 ≠ one`; control_gauge_moves_slot asserts 2 inequalities). So this is
**not a math defect** — the kernel checked the real theorems — but it IS a
genuine instrument finding: **seat B, reading statements-only, reviewed a
vacuous fragment for these claims.** Its blind review of `live_gauge_witness`
and `control_gauge_moves_slot` inspected essentially nothing. The "statements
re-extraction byte-identical" pass is real but hides that the extractor is
lossy on inline-`let` types. Provenance to check in the prose: did any report
CLAIM seat B independently reviewed these two? If so, that claim overstates.

### F2 (INSTRUMENT DEFECT — courier) — a block comment leaked into the statements file
L400–416 of the statements file contain report-style PROSE, not statements:
"…theorem on the semions, and the locus characterized exactly. … Design probe:
probes/s5_design_probe.py … NESTS (norm 9): …  ==== -/". This is an S5
section-header `/- … -/` block comment from Zi.lean that the extractor failed
to strip (it strips proof bodies and skips decl lines, but does not skip
multi-line block comments; the indented lines fell through). Harmless to the
math, but it means the "seat B sees definitions and claims only" guarantee is
violated: seat B also saw a chunk of seat-P-authored prose describing the
S5 design and its nests. A blindness leak, however small. Flag for norm-8
(prose) adjudication and for the S7c gate story.

### F3 (WATCH — potentially-vacuous by construction) — `pauli_kill_symbolic` and friends
- `pauli_kill_symbolic (x y : Zi) : sub (mul x y) (mul y x) = zero`
- `pauli_double_occupation_dies (a b : Zi) : sub (mul a b) (mul b a) = zero ∧ …`
- `M2_image_on_line`: first two conjuncts are `sub (mul a c) (mul a c) = zero`
These are TRUE for ALL x,y precisely because Zi multiplication is COMMUTATIVE
(mul_comm is S1). i.e. `x·y − y·x = 0` is not a Pauli/antisymmetry fact — it is
`mul_comm` wearing an exclusion-flavored name. This is the "theorem that could
not fail" species Round Two warned about (a commutative-ring triviality dressed
as a many-body exclusion). **Strong-name / weak-content candidate.** The real
exclusion content, if any, must live in the `Mmat`/`M2_*`/`census_nest_m2`
matrix statements (which are genuinely about I − SWAP), not in these
commutator-of-scalars lines. Must check the prose: does it CHARACTERIZE these
as the exclusion mechanism? If yes, that is a characterization slip.

### F4 (WATCH — name vs content) — `dimension_charpoly_factors`
`dimension_charpoly_factors (x : Zi) : sub (mul x x) one = mul (sub x one) (add x one)`
is literally `x² − 1 = (x−1)(x+1)` for a commutative ring — a factorization
identity with NO dimension/char-poly content of its own. The "dimension /
charpoly" reading is supplied entirely by an external model. Edge-supplied-by-
the-model candidate (matches the REGISTER row-8 prediction verbatim). Not
false; just named far above its content.

### F5 (WATCH — vacuous conjunct) — several `*_nest_*` carry a trivial arithmetic tail
`census_nest_m2 : tri 2 + tri 3 = 4 ∧ (2*2 : Nat) = 4`,
`fork_nest_2_plus_2 : (2+2 : Nat) = 4`, `filter_nest_2_of_4 : (2+2:Nat)=4`,
`M2_trace : … ∧ (2*2−2:Nat)=2 ∧ tri 2 = 1`, `M2_sq_eq_two_M` etc.
The `(2+2:Nat)=4` conjuncts are trivially true and carry no nest content by
themselves; the CONTENT is in the neighboring `tri`/enumeration facts. These
are fine AS LONG AS the accompanying enumerated fact is what's load-bearing and
the report ties the count to a real nest. Norm 9 says every count ties to its
nest — I will verify each count actually equals a genuinely enumerated
cardinality, not just an arithmetic tautology. `pent_nest_card`,
`pent_classification_counted` (11+4+1=16), `hex_nest_8_of_16` DO tie to real
`List` enumerations — good. The `(2+2)=4`-style ones need their partner enum.

### F6 (WATCH — strength of the capstone) — read the exactly-two claim precisely
`the_roomy_world_has_exactly_two_particles (r : Zi) :
   (∃ f, roomy f r) ↔ (r = one ∨ r = neg one)`
This is EXACTLY-TWO **in r**, existentially quantified over f. Combined with
`roomy_iff_boson_or_fermion` and `capstone_count_two` (which pins f = one for
any roomy pair), the "two particles" = {(f,r)} = {(1,1),(1,−1)}. This is
honest and matches "exactly two on the slice." NOTE the definition
`roomy f r := pentagon f ∧ hexagon f r ∧ conj r = r` — the third conjunct
`conj r = r` is the REALITY FILTER / slice. So the headline is "exactly two
**given the reality filter**." Anything in the prose claiming "exactly two,
full stop" (without the filter caveat) would OVERSTATE. This is the boundary
the handoff says Round Two deliberately held (charter flag 2). Watch the prose
for whether it keeps the "on the slice / gauge-invariantly" qualifier.

### F7 (GOOD — negative controls present, per claim family)
Every family has a `control_*`: ring (fake_mirror, coordMul, conj_not_id,
normSq_not_additive), domain (mod2_insufficient, descent_needs_hypothesis,
z4_has_zero_divisors), pentagon (f=i fails, f=2 fails, z8_four_roots),
hexagon/gauge (gauge_moves_slot, wrong_R_per_class, Zi_mod5_splits,
filter_needs_catalog), twist (fork_locus_needs_nonzero, wrong_twist,
ribbon_forcing_bites, nuFS_separates), capstone (semion_fails_only_filter,
real_but_not_roomy, boson_no_exclusion, M_times_P_zero). Norm 5 looks honored
at the statement level. I will spot-check that the controls actually FAIL the
property they claim to fail (i.e. are true negative controls, not true-by-
triviality). `control_gauge_moves_slot` is F1-truncated so its control content
is invisible from statements-only — noted.

### F8 (WATCH — descent_core fuel parameter)
`descent_core : ∀ fuel : Nat, ∀ a b : Int, a.natAbs + b.natAbs ≤ fuel →
   a*a+b*b=0 → a=0 ∧ b=0`. The `fuel` universally quantified with a `≤ fuel`
guard is a standard structural-recursion dressing; the mathematical content
(`a²+b²=0 → a=b=0`) is downstream in `normSq_eq_zero_iff`. Fine, but the
"≤ fuel" hypothesis makes the statement WEAKER than "for all a,b" until you
observe fuel can be chosen = natAbs sum. Not a defect (normSq_eq_zero_iff is
the unconditional form and it's present), just noting the shape.

## Load-bearing claims I will independently verify in Phase 1.2 (≥10)
Chosen for centrality to the headline and for the F3/F4/F6 suspicions:
1.  `i_squared_is_minus_one`               (ring anchor)
2.  `normSq_mul` / `brahmagupta_fibonacci_int` (multiplicativity)
3.  `no_zero_divisors` / `normSq_eq_zero_iff`  (domain)
4.  `pentagon_exactly_two` / `pentagon_iff_f_sq_one` (S3 headline)
5.  `pent_classification_counted` (11+4+1=16 nest — verify the enumeration)
6.  `hex_nest_8_of_16` (hexAdm admissible count — verify enumeration)
7.  `norm_one_units` (four units)
8.  `roomy_iff_boson_or_fermion`            (S6 core)
9.  `the_roomy_world_has_exactly_two_particles` + `capstone_count_two` (headline)
10. `M2_sq_eq_two_M`, `M2_trace`, `M2_kill_iff_det_zero`, `census_nest_m2`
    (the m=2 antisymmetrizer — the REAL exclusion content vs F3's trivialities)
11. `pauli_kill_symbolic` / `pauli_double_occupation_dies` (confirm F3: true by
    commutativity, i.e. content-free as an exclusion statement)
12. `nu_fork_on_semions` / `fork_locus_is_real_locus` (S5 fork)

By-my-own-routes rule: I will NOT read the six seat-B verifiers until after I
have written mine. My routes: brute enumeration over the Z2 index cube for the
pentagon/hexagon/nest claims; a from-scratch Gaussian-integer arithmetic
reimplementation (independent of Zi.lean's defs) for the ring/domain/unit
claims; explicit 4x4 integer matrix build for the M2 antisymmetrizer.

## Predictions I am committing to BEFORE reading the prose
- P-A: The prose will keep the "reality filter / on the slice" qualifier on the
  two-particle headline (F6). If it drops it, that is the row-8 slip.
- P-B: If the prose characterizes `pauli_*`/`M2_image_on_line`'s commutator
  conjuncts as the exclusion mechanism (rather than the I−SWAP matrix), that is
  a characterization slip (F3): edge supplied by the model.
- P-C: The prose likely will NOT mention that the courier truncates inline-`let`
  statements (F1) or that a block comment leaked (F2), because those are
  invisible unless a stranger re-reads the extraction. These are my candidate
  "shared blind spot" items — mechanical enough to pass every instrument, prose-
  adjacent enough that both seats could miss them.
- P-D: `dimension_charpoly_factors` (F4) name will be justified in prose by a
  model/bench reference, "every noun resolving, the edge supplied by the model"
  — matching the REGISTER prediction rather than contradicting it.
