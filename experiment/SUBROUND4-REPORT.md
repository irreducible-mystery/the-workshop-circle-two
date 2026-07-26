# DUAL-SEAT EXPERIMENT — SUB-ROUND 4 REPORT: THE HEXAGON LAYER

**Quarantined per norm 16; REGISTER row 7. BEYOND the S1–S3 charge —
extension explicitly sanctioned by the courier (Kelly), divergence from
chartered boundaries knowingly recorded, here and in the Lean source's
S4 header comment.**

## What S4 is

The hexagon layer of the round-1 mathematics: the bench's
`hex_residual_z2` (floor/symmetric_statistics.py line 124) formalized
over Z[i] — R² = F, the four units, the semion pair, the flatland
filter as a Galois statement, the mirror. Design cross-checked against
certificates G1d, G3b, G1e, G4 before a line of Lean was written
(probe: `seatP/probes/s4_design_probe.py`).

## Seat P (prover)

**Zi.lean now 115 theorems** (S1 42 → S2 57 → S3 84 → S4 115), compile
**silent** (exit 0, zero bytes), census **115/115 covered, 0 sorryAx,
0 Classical.choice, RESULT: PASS**.

Pin: `Zi.lean` sha256
`6d51cafa7bd4ce169be1727e740622c914490556ce1cc6c0ce750b254c7b8146`

The S4 headline chain:

1. **Nest** (norm 9): 16 loop assignments, 8 admissible (d = a+b+c
   forced) — `hex_nest_8_of_16`, by decide.
2. **Classification 5+2+1 = 8**: seven off-forcing instances are
   identities in symbolic f AND r (`hexagon_offdiag`, full rcases
   sweep); the forcing site is (1,1,1,1) where lhs = f and
   rhs = (f·r)² (`hexagon_forcing_lhs/rhs`).
3. **Reduction identity**, exact over Zi:
   f²r² − f = (r² − f) + r²(f² − 1) — degree-4 componentwise, closed by
   distribute-normalize-omega (`hexagon_reduction_identity`).
4. **PENTAGON + HEXAGON ⟺ R² = F** (`pentagon_hexagon_iff_R_sq_F`):
   given f² = 1, the hexagon holds exactly when r² = f. The headline.
5. **The four units**: a² + b² = 1 forces z ∈ {1, −1, i, −i}
   (`norm_one_units`) — completeness needs no search box; helpers
   `int_sq_nonneg` / `int_sq_eq_zero` / `int_sq_eq_one` route integer
   facts through Zi's certified domain.
6. **The catalog 2×2**: r² = 1 ⟺ r = ±1 (boson/fermion);
   (r−i)(r+i) = r²+1 symbolically, so r² = −1 ⟺ r = ±i (the semions)
   via the domain (`semion_factorization`, `R_over_semion_class`).
   Flag 4 held: `no_integer_semion` — over Z the F = −1 class is EMPTY;
   the 2×2 count is a Z[i] statement.
7. **The flatland filter as a Galois statement** (G1e): on units
   u⁻¹ = conj u (`unit_inverse_is_conj`), so the roomy edict R = R⁻¹ is
   literally conj(R) = R — fixed points among the four are exactly
   boson and fermion (`flatland_filter`). The semions die on the filter
   exactly as the anyon died on the roomy edict.
8. **The mirror** (G4): conj swaps the semions (a conjugate pair, the
   golden/Yang–Lee pattern one level down) and fixes both F-classes —
   σ acts WITHIN the F = −1 fiber, unlike Circle One's σ which moved
   between pentagon classes (`mirror_structure`).
9. Flag 5 held: both hexagons imposed on the catalog here
   (`catalog_satisfies_both_hexagons`); nothing claims the bench did.
   Flag 3 (FS fork) is twist-layer, explicitly NOT addressed — recorded
   as a decision, not a gap.
10. **Live** (norm 3): all four particles satisfy the full 8-instance
    hexagon (`live_hexagon_{boson,fermion,semion,antisemion}`); the
    forcing site separates at (1, ⟨2,0⟩). **Controls** (norm 5):
    wrong-R-per-class exact residues ⟨∓2,0⟩; the chartered Z[i]/5
    control (deferred from S2, landing where the charge placed it) —
    (2+i)(2−i) = 5, four roots of +1 AND four of −1 mod 5; a non-unit
    passes the reality filter, so the filter selects among the catalog
    rather than defining it.

**Corrections law bit once more, in-flight**: the first census run
ALARMed — `norm_one_units` pulled Classical.choice via omega on a
*disjunctive* `have` goal (the same trap species as S2's, one
disguise over: not a conjunctive goal this time but a disjunction
`(a²=0 ∧ b²=1) ∨ (a²=1 ∧ b²=0)` discharged by omega). Repaired by
`by_cases` on decidable Int equality so omega proves only atomic
equations. Census after repair: 0 Classical.choice, PASS. Fourth bite
of the same underlying trap; the alarm held every time.

## Courier

Statements v5 (S1+S2+S3+S4), 115 statements, proof bodies stripped,
byte-identical on re-extraction. Pin: `Zi_statements_v5.txt` sha256
`d195b3de0ead00799b4e913eeba4f6a71c900c6209859b947e1132c37387e3bb`

## Seat B (blind verifier)

`verify_zi_s4.py` — **36/36, exit 0**. Pin: sha256
`acfa68424e8b1e0358b20ee9398ddf9da2fd736551e05764b9dad06b11026a25`

- Symbolic route upgraded for two Gaussian variables: the polynomial
  ring **Z[i][fr, fi, rr, ri]** (four commuting indeterminates);
  agreement is coefficientwise, not sample points. The classification,
  the forcing sides, (f·r)² = f²r², and the reduction identity all
  verified as polynomial identities (grid 5⁴ = 625 as secondary
  evidence, labeled as such).
- **Independent route held**: root censuses via N(r²) = N(r)² = 1 ⟹
  N(r) = 1 and the complete [−1,1]² box (complete because a² ≤ 1
  forces |a| ≤ 1) — NOT seat P's factorization route. Both routes name
  the same sets. The factorization verified coefficientwise as its own
  claim. Z[i]/5 counted by direct modular squaring, independent of the
  statement's arithmetic encoding — and the encoding checked against
  it separately.
- **Plant bitten** (norm 16): an R-at-(1,0) mutant of the hexagon
  plumbing fails the off-diagonal sweep — a wrong transcription of
  bench line 124 could not pass this instrument.

## The crop (3 items, applied)

1. **Nat-subtraction hazard** in `control_Zi_mod5_splits`: the
   `(a*a + 5*5 - b*b) % 5` encoding is safe only because range-5 bounds
   b² ≤ 16 < 25 — Nat subtraction truncates. TRUE as stated, but the
   guard is load-bearing and was invisible. Docstring sentence added to
   the Lean source. (Applied.)
2. `filter_nest_2_of_4` is the count theorem; the verdicts live in
   `flatland_filter` — matches prior nest-tying convention, recorded so
   no reader mistakes one for the other. (Observation, no change.)
3. Independence report: two independent derivations of the root
   censuses agree — the strongest PASS seat B issues. (Positive
   finding.)

## Running score, four sub-rounds in

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| theorems | 42 | 57 | 84 | **115** |
| kernel | silent ~0.6s | silent ~1.5s | silent ~2.1s | silent |
| census | 0/0 | ALARM ×6, repaired | clean first compile | **ALARM ×1 (norm_one_units), repaired** |
| seat B | 47/47 | 24/24, two routes | 32/32, poly-exact | **36/36, 4-indeterminate poly + norm route** |
| crop | 1 conviction | 2 + 1 deferral | 2 + 1 witness | **1 hazard label + 2 observations** |

The Classical.choice trap has now bitten in two disguises (conjunctive
S2, disjunctive S4) and the census caught it both times live. That is
what the instrument is for.

**S1–S4 complete: the ring, the domain, pentagon necessity, and the
hexagon layer — 115 theorems kernel-silent over Z[i], every claim
re-derived blind cross-seat, every instrument plant-bitten both
directions, the extension beyond charter sanctioned and recorded.**

The middle holds.

*— SuperNinja, sub-round 4, quarantined, beyond-charge by sanction*
