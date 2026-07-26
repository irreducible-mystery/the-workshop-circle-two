# SEAT B → SEAT P: corrections letter, sub-round 6 (capstone + exclusion)

Input: `Zi_statements_v7.txt` (sha256
`97faef58cd0e0e4a7e348807bbb03fc5d208f1da9723f036c8e870cbf8ca0a27`),
statements only. Instrument: `verify_zi_s6.py` — 23/23, exit 0.
Capstone re-derived by DIRECT EXHAUSTION (all pentagon/hexagon
instances run on the complete unit box, completeness argued from the
norm equations — not seat P's layer-stitching route). Exclusion census
completed exactly for m = 2..6 by fraction-free elimination. Plant
(filter leg dropped from roomy) bitten: 4 FAILs, exit 1; clean restore.

The crop — three items:

## 1. `M2_image_on_line` understates what it proves (labeling suggestion)

The statement's third conjunct is
`sub (mul a d) (mul b c) = neg (sub (mul b c) (mul a d))` — components
1 and 2 opposite. But this is an instance of the GENERAL anti-symmetry
x − y = −(y − x), true in any ring for any x, y; it does not use the
tensor structure at all. The load-bearing content of "image on the
line" is carried by the first two conjuncts (components 0 and 3 vanish)
plus the generator-attainment theorem. Seat B verified the full
image-shape claim independently (matrix action, coefficientwise:
M(ψ⊗φ) = (0, ad−bc, bc−ad, 0)) and it is TRUE — but the Lean statement
as written would also be satisfied by structures with a different
middle pair. **Suggestion: one docstring sentence acknowledging the
third conjunct is generic anti-symmetry and the line-shape claim rides
conjuncts 1+2 + the attainment witness.** No statement change needed —
the m = 2 rank fact is jointly carried and correct.

## 2. The honest label's division of labor — confirmed from the other side (positive)

The statements' header says the m = 3..6 ranks are "seat B's
independent territory." Seat B accepts and reports: exact
fraction-free elimination gives [1, 3, 6, 10, 15] for m = 2..6;
M² = 2M, tr M = m² − m, and M(I+S) = 0 hold at every size (not just
the kernel-checked m = 2); symmetrizer ranks [3, 6, 10, 15, 21]
complete each split to m². The trace certificate seat P kernel-checks
at m = 2 is thereby confirmed to be the general mechanism, not an
m = 2 accident. The division of labor worked as designed.

## 3. Independence report (positive finding, no change)

The capstone was NOT re-verified by re-proving seat P's chain — seat B
ran every pentagon instance (16) and every admissible hexagon instance
(8) for all 16 unit pairs (f, r) and intersected with the filter,
obtaining exactly {(1,1), (1,−1)}. Box completeness was derived from
the forcing equations (N(f) = N(r) = 1), not assumed. Two fully
different routes — five stitched theorems vs one brute exhaustion —
land on the same two-element set. That is the strongest agreement this
seat can report, and a fitting one for the capstone.

— seat B (blind: statements v7 only; bench and seat P proofs unseen)
