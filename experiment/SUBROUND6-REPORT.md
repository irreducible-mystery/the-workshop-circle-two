# DUAL-SEAT EXPERIMENT — SUB-ROUND 6 REPORT: THE CAPSTONE AND THE EXCLUSION LAYER

**Quarantined per norm 16; REGISTER row 7. Continuation of the
sanctioned beyond-charge extension (Kelly's explicit request: "next
move options a and b"); the divergence records in the S4/S5 headers
carry forward and this section extends them.**

## What S6 is

Two movements shipped as one sub-round.

**S6a — the capstone.** One headline statement stitching S1–S5: the
roomy conditions (pentagon + hexagon + reality filter, packed into a
single `def roomy`) hold exactly on {(1,1), (1,−1)} — boson and
fermion, nothing else, count 2. Every ingredient is a prior layer's
theorem: `pentagon_iff_f_sq_one` (S3), `pentagon_hexagon_iff_R_sq_F`
(S4), `R_over_boson_class` / `R_over_semion_class` (S4), the filter
(S4), the ν-rider (S5). The capstone adds NO new axioms of content —
it is the stitching, and says so in its header.

**S6b — the exclusion layer.** Bench claim (3), lines 30–36 and
185–196; certificate G1f. The −1 has teeth: exchange antisymmetry
annihilates double occupation. Triangular numbers, the m = 2
antisymmetrizer exact, the Pauli kill symbolic. Design probed before
any Lean (probes/s6_design_probe.py) — capstone survivors, ranks
[1,3,6,10,15], symmetrizer ranks [3,6,10,15,21], M(2) matrix, the
kill criterion ad = bc, boson control — all confirmed against the
certificates.

## Seat P (prover)

**Zi.lean now 161 theorems** (42 → 57 → 84 → 115 → 141 → **161**),
compile **silent** (exit 0, zero bytes), census **161/161 covered,
0 sorryAx, 0 Classical.choice, RESULT: PASS** — **clean on first full
census again** (two in a row; the omega-trap discipline has become
design practice, not repair practice).

Pin: `Zi.lean` sha256
`b7ef35425e13b740e253892916fffb8a6ed5adddaa08a1bbe01360b77fcdba5e`

The S6 chain:

1. **THE CAPSTONE**: `def roomy (f r : Zi) : Prop := pentagon f ∧
   hexagon f r ∧ conj r = r`, then
   `roomy_iff_boson_or_fermion : roomy f r ↔ ((f = one ∧ r = one) ∨
   (f = one ∧ r = neg one))` — proved by stitching the five prior-layer
   theorems, not by fresh computation. The r-only headline:
   **`the_roomy_world_has_exactly_two_particles (r : Zi) :
   (∃ f, roomy f r) ↔ (r = one ∨ r = neg one)`** — the workshop's title
   claim as a single kernel-checked iff. The count tied (norm 9,
   `capstone_count_two`: both survivors roomy, distinct, and any third
   roomy r collapses into the pair); the ν-rider stitched in
   (`capstone_nu_rider`: every roomy particle carries ν_FS = ν_ML = +1
   — S5's fork closes on the capstone set).
2. **Capstone controls** (norm 5): the semion passes pentagon AND
   hexagon and dies on the filter ALONE
   (`control_semion_fails_only_filter` — each gate weighed separately);
   r = 3 is real but not roomy for any unit f
   (`control_real_but_not_roomy` — the filter alone is not enough).
3. **Triangular numbers, no division hazards**: `def tri` as a
   recursion; values 1, 3, 6, 10, 15 for m = 2..6 (`tri_values`, bench
   line 34 verbatim); the recurrence T(m+1) = T(m) + m is `rfl`
   (`tri_recurrence`); and the closed form for ALL m by induction:
   `tri_double : 2 * tri m = m * (m − 1)` — the m(m−1)/2 formula
   stated multiplicatively, exactly, with no Nat-division.
4. **THE PAULI KILL, symbolic over Zi** (`pauli_kill_symbolic`): the
   antisymmetrized components ψᵢψⱼ − ψⱼψᵢ vanish identically —
   commutativity is the killer, per certificate G1f.
5. **The m = 2 antisymmetrizer, exact**: `Mmat` = I − SWAP on Z⁴
   (integer entries, index p = 2i+j); M² = 2M entrywise
   (`M2_sq_eq_two_M`, all 16 cells by decide over List.range);
   tr M = 2 = m² − m (`M2_trace`) — with the projector identity this
   is the rank-by-trace certificate at the kernel-checked size. The
   rank-1 fact stated kernel-honestly with no rank function:
   image ⊆ line (`M2_image_on_line`: M(ψ⊗φ) = (0, ad−bc, bc−ad, 0))
   ∧ line ⊆ image (`M2_image_attains_generator`: ψ = e₁, φ = e₂
   attains the generator).
6. **The kill criterion**: M₂(ψ⊗φ) = 0 ⟺ ad = bc — the 2×2
   determinant (`M2_kill_iff_det_zero`); double occupation φ = ψ is
   the diagonal case and DIES (`pauli_double_occupation_dies` — no two
   fermions in one state, symbolic). Census nest tied at m = 2
   (norm 9): antisym 1 + sym 3 = 4 = m² (`census_nest_m2`).
7. **Exclusion controls and live** (norms 5, 3): the SYMMETRIZED
   double occupation is 2 ≠ 0 — **bosons do not exclude; the teeth
   belong to the −1 alone** (`control_boson_no_exclusion`);
   M(I + SWAP) = 0 (`control_M_times_P_zero` — the complement is
   orthogonal); a non-parallel pair survives
   (`live_nonparallel_survives` — exclusion kills double occupation,
   not everything).
8. **HONEST LABEL** (norm 6, in the section header AND the
   statements): the m = 3..6 ranks (6, 10, 15, …) are NOT
   kernel-checked — a general rank needs matrix machinery this
   zero-import file deliberately lacks. What IS kernel-checked: the
   triangular values/recurrence/closed form for all m, and the full
   m = 2 mechanism (projector, trace, image-shape, kill). The general
   census is declared seat B's independent territory — a division of
   labor stated up front, not discovered after.

## Courier

Statements v7 (S1–S6), 161 statements, proof bodies stripped,
byte-identical on re-extraction — and byte-identical across the crop
application (the crop was docstring-only). Pin: `Zi_statements_v7.txt`
sha256 `97faef58cd0e0e4a7e348807bbb03fc5d208f1da9723f036c8e870cbf8ca0a27`

## Seat B (blind verifier)

`verify_zi_s6.py` — **23/23, exit 0**. Pin: sha256
`64bdc767c785cac980be2ceafa30bc608db2ade4b29618bbe6e2bc758a6bce0b`

- **The capstone re-derived by DIRECT EXHAUSTION** — not seat P's
  stitching route. Box completeness derived from the forcing equations
  (N(f) = N(r) = 1 ⟹ the four units, by a² ≤ 1 ⟹ |a| ≤ 1); then
  EVERY pentagon instance (16) and every admissible hexagon instance
  (8) run on all 16 unit pairs, intersected with the filter: exactly
  {(1,1), (1,−1)}. Five stitched theorems vs one brute exhaustion —
  same two-element set.
- **The exclusion census completed, m = 2..6** — exact fraction-free
  elimination: antisym ranks [1, 3, 6, 10, 15] = m(m−1)/2; symmetrizer
  ranks [3, 6, 10, 15, 21] = m(m+1)/2; each split sums to m². M² = 2M,
  tr M = m² − m, and M(I+S) = 0 confirmed at EVERY size — the trace
  certificate seat P kernel-checks at m = 2 is the general mechanism,
  not an m = 2 accident. The honest label's division of labor honored
  from the other side.
- The Pauli kill re-verified coefficientwise (16 component
  polynomials); Mmat/swapIdx transcription checked against an
  independent I − SWAP construction; the kill criterion checked over
  a Gaussian grid.
- **Plant bitten both directions** (norm 16): the filter leg dropped
  from `roomy` → 4 FAILs, exit 1 (the semion sneaks in and three
  downstream checks break); restored → 23/23, exit 0.

## The crop (3 items, applied)

1. **`M2_image_on_line`'s third conjunct is generic anti-symmetry**:
   x − y = −(y − x) holds in any ring and does not use the tensor
   structure; the line-shape claim rides conjuncts 1+2 plus the
   attainment witness. Docstring sentence added recording this.
   (Applied — proof-comment only; statements pin unchanged.)
2. Division-of-labor confirmation from seat B's side — the m = 3..6
   census run and consistent with the kernel-checked m = 2 mechanism.
   (Positive finding.)
3. Independence report: capstone agreement reached by two fully
   different routes (stitching vs exhaustion) — "the strongest
   agreement this seat can report, and a fitting one for the
   capstone." (Positive finding.)

## Running score, six sub-rounds in

| | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| theorems | 42 | 57 | 84 | 115 | 141 | **161** |
| kernel | silent | silent | silent | silent | silent | silent |
| census | 0/0 | ALARM ×6, repaired | clean | ALARM ×1, repaired | clean first census | **clean first census** |
| seat B | 47/47 | 24/24 | 32/32 | 36/36 | 25/25 | **23/23** |
| seat B route | exact | two routes | poly Z[i][f] | poly 4-var + norm | poly Z[i][r] + coords | **brute exhaustion + exact elimination** |
| crop | 1 conviction | 2+1 | 2+1 | 1 hazard + 2 obs | 1 route-note + 2 obs | **1 label-note + 2 positive** |

**The arc closes on its own title: S1 the ring, S2 the domain, S3
pentagon necessity, S4 the hexagon layer, S5 the twist layer, S6 the
capstone and the exclusion teeth — 161 theorems kernel-silent over
Z[i], and the workshop's headline claim now stands as ONE
kernel-checked statement:
`the_roomy_world_has_exactly_two_particles : (∃ f, roomy f r) ↔
(r = one ∨ r = neg one)` — re-derived blind by a route that shares
nothing with the proof.** And the fermion's −1 is not just a catalog
entry: it annihilates double occupation, symbolically, while the
boson's +1 demonstrably does not.

The middle holds. The catalog is two.

*— SuperNinja, sub-round 6, quarantined, beyond-charge by sanction*
