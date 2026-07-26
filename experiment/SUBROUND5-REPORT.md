# DUAL-SEAT EXPERIMENT — SUB-ROUND 5 REPORT: THE TWIST LAYER

**Quarantined per norm 16; REGISTER row 7. Continuation of the
sanctioned beyond-charge extension (Kelly's explicit request:
"proceed with the twist layer"); the divergence record from S4's
header carries forward and this section extends it.**

## What S5 is

θ, the spin-statistics seed, and — the centerpiece — **charter flag 3
ADDRESSED**: the Frobenius–Schur convention fork, parked in S4 with a
recorded decision, now formalized. Sources: bench lines 37/197–199
(`theta_f = R = -1; nu = R * theta = +1`), certificates G1g (the two
ν-ledgers, the fork on semions) and G5 (spin-statistics seed, N_f² = I,
D² = 2), CHARTER.md flag 3 ("name the two ledgers apart"). Design
probed before any Lean (probes/s5_design_probe.py) — fork nest 2+2,
fork locus = real locus, ribbon nest 3+1 with forcing cell r⁴ = 1, all
confirmed against the certificates.

## Seat P (prover)

**Zi.lean now 141 theorems** (42 → 57 → 84 → 115 → **141**), compile
**silent** (exit 0, zero bytes), census **141/141 covered, 0 sorryAx,
0 Classical.choice, RESULT: PASS** — clean on first full census this
time (the S2/S4 omega-trap lesson held; no disjunctive/conjunctive
omega goals were written).

Pin: `Zi.lean` sha256
`e505e5192b51c909ca4e1f284a45cbf1220102593200e8ba73c4e03643da2c80`

The S5 chain:

1. **The twist is the R-diagonal** (`twist r a = Rz2 r a a`, abelian
   θ_a = R(a,a) per G1g); catalog values +1/−1/+i/−i; the fermion's
   −1 stated by itself (`twist_fermion_minus_one`) — the bench's "sign
   that builds shelves."
2. **The ribbon identity, symbolic**: θ((a+b)%2) = θ(a)·θ(b)·R(a,b)²
   holds for all r given r⁴ = 1 (`ribbon_identity`); the nest tied
   3 + 1 = 4 (`ribbon_nest_3_plus_1`) — three cells hold for EVERY r,
   the (1,1) cell is exactly 1 = r⁴; and the hypothesis is DISCHARGED
   by the earlier layers (`catalog_r_fourth`: r² = f ∧ f² = 1 ⟹
   r⁴ = 1) — S3's pentagon and S4's hexagon feed the ribbon.
3. **THE FORK (flag 3 addressed)**: two defs, named apart — `nuFS`
   (R·θ, the true Frobenius–Schur indicator) and `nuML` (R·conj(θ),
   stone8's mirror ledger). Agreement on the survivors
   (`nu_survivors_plus_one`), divergence on the semions — FS −1, ML +1
   (`nu_fork_on_semions`), nest 2 + 2 = 4. Neither ledger is called
   "the" indicator; the fork is a theorem, not a footnote.
4. **The fork locus characterized exactly**: for r ≠ 0,
   ν_FS = ν_ML ⟺ conj r = r ⟺ r.im = 0
   (`fork_locus_is_real_locus`, `fork_locus_coordinates`) — the two
   ledgers coincide precisely on the real locus, so the flatland
   filter CLOSES the fork (`filter_closes_fork`): the fork lives only
   where the filter kills. And the structural asymmetry:
   **ν_ML is the norm in disguise** (`nuML_is_normSq`, riding S1's
   mul_conj_eq_normSq) — it reads +1 on ALL norm-1 units
   (`nuML_blind_on_units`), so it structurally cannot see the semions;
   only ν_FS separates (`control_nuFS_separates`). The fork is not a
   convention quibble: one ledger carries information the other cannot.
5. **The spin-statistics seed** (G5): θ_f = −1, R·θ = +1 on both
   survivors (`spin_statistics_seed`); θ = R per particle — spin and
   statistics are literally the same Gaussian integer
   (`spin_equals_statistics`, the abelian collapse). Fusion matrix
   N_f² = I entrywise, D² = 2, with the char-poly factorization
   x² − 1 = (x−1)(x+1) symbolic over Zi
   (`dimension_charpoly_factors`) — and G5's honest note carried: no
   decidable order, no Perron, no Z[φ] needed; the absence is a
   feature.
6. **Live** (norm 3): the full ribbon for each of the four particles
   (hypothesis routed through catalog_r_fourth); the fork live OFF the
   catalog at r = 1+i (ν_FS = 2i ≠ 2 = ν_ML). **Controls** (norm 5):
   r = 0 collapses the locus iff's cancellation route (hypothesis
   earns its keep); a wrong twist (θ = F) breaks the ledger visibly;
   the ribbon forcing cell bites at r = 2 (1 ≠ 16); ν_FS's separation
   stated as its own control.

## Courier

Statements v6 (S1–S5), 141 statements, proof bodies stripped,
byte-identical on re-extraction — and byte-identical across the crop
application (the crop was docstring-only). Pin: `Zi_statements_v6.txt`
sha256 `1071e8541e396180f6d197a56fde6f4deadb0a5c41aea5f46043af53435e8735`

## Seat B (blind verifier)

`verify_zi_s5.py` — **25/25, exit 0**. Pin: sha256
`24f50d913640891f48f4b396dbc48988e8410b547ecd01394c726f60b2b0fab4`

- Ribbon and char-poly coefficientwise in **Z[i][rr, ri]**; the ribbon
  classification re-derived symbolically (3 trivial cells + the (1,1)
  cell reading exactly 1 = r⁴, matching the probe).
- **Independent route held**: the fork locus re-derived by expanding
  the DIFFERENCE ν_FS − ν_ML = r(r − conj r) = −2·ri² + 2·rr·ri·i
  coefficientwise — not seat P's cancellation route. Both routes land
  on the real locus.
- **Plant bitten both directions** (norm 16): ν_FS mutated to
  r·conj(r) → 5 FAILs, exit 1; restored → 25/25, exit 0.

## The crop (3 items, applied)

1. **The r ≠ 0 hypothesis is route-required, not statement-required**:
   seat B's coordinate expansion shows the iff
   `nuFS r = nuML r ↔ r.im = 0` holds unconditionally (at r = 0 both
   sides are true); seat P's mul_left_cancel route needs the
   hypothesis. Docstring sentence added recording the distinction.
   (Applied — proof-comment only; statements pin unchanged.)
2. `fusion_matrix_squares_to_identity` is Nat arithmetic in disguise —
   the matrix is never an object (no Matrix type in a zero-import
   file); the structural claim lives in the G5 citation. Matches the
   established count-theorem convention; recorded. (Observation.)
3. Independence report: fork values match G1g exactly on all four
   particles by independent computation; flag 3's "name them apart"
   satisfied in the statements themselves. (Positive finding.)

## Running score, five sub-rounds in

| | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|
| theorems | 42 | 57 | 84 | 115 | **141** |
| kernel | silent | silent | silent | silent | silent |
| census | 0/0 | ALARM ×6, repaired | clean | ALARM ×1, repaired | **clean first census** |
| seat B | 47/47 | 24/24 | 32/32 | 36/36 | **25/25** |
| seat B route | exact | two routes | poly Z[i][f] | poly 4-var + norm | **poly Z[i][r] + coordinate expansion** |
| crop | 1 conviction | 2+1 | 2+1 | 1 hazard + 2 obs | **1 route-note + 2 obs** |

**The full arc now stands: S1 the ring, S2 the domain, S3 pentagon
necessity, S4 the hexagon layer, S5 the twist layer — 141 theorems
kernel-silent over Z[i], every claim re-derived blind cross-seat,
every instrument plant-bitten both directions, all five charter flags
now either held or (flag 3) formally addressed.** The layer cascade is
itself a theorem chain: pentagon forces f² = 1, hexagon forces r² = f,
and together they discharge the ribbon's r⁴ = 1 — each layer's forcing
equation is the next layer's hypothesis.

The middle holds.

*— SuperNinja, sub-round 5, quarantined, beyond-charge by sanction*
