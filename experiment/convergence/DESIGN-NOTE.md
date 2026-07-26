# Convergence experiment S1 — design note (written before any measurement)

Two independent formalizations of the same charge (ROUND1.md §S1, the
Z[i] ring layer) now exist:

- **Mine** (dual-seat, one architecture): S1 section of
  `experiment/seatP/Zi.lean`, 42 theorems at S1-ship, pin
  `5930c54a…` (S1 version), namespace `Zi`, structure `Zi`.
- **Theirs** (true two-body: Fable 5 builder + Opus 4.6/Code third
  body): `Zi.lean`, claimed 54 theorems, 350 lines, pin
  `2e227702…`, namespace `Zi`, structure `GZ`.

The comparison is itself run as an experiment, mechanical before
prose (the discipline that Round Two proved):

**Phase A — mechanical verification of THEIR artifact on MY
instruments.** Compile on my pinned toolchain; run my census; verify
their claimed counts (54 theorems; 16/36/2 axiom split; 0 sorryAx;
0 Classical.choice) by independent measurement. Their claims enter as
claims-to-verify.

**Phase B — statement-level convergence map.** Extract their
statements with my mechanical courier; classify every theorem:
shared mathematical content (modulo naming), mine-only, theirs-only.
The interesting datum is the SYMMETRIC DIFFERENCE: what did each
formalization think S1 needed that the other did not?

**Phase C — cross-seat verification (the strongest event).** My
exact-Python seat B machinery, pointed at THEIR statements — the
first time an instrument from one lineage adjudicates an artifact
from the other. Bridge verifier must bite a plant before its PASS
counts (norm 16).

**Phase D — apples-to-apples census.** Their census is finer than
mine (per-theorem axiom footprints vs covered+alarm-only). Measure MY
S1 theorems with THEIR granularity, so both files are scored on the
same scale. Also audit their 16/36/2 claim per-theorem.

**Phase E — the process comparison (prose, last).** Defect records:
their 7-item adversarial crop vs my 1-item cross-seat crop at S1;
the omega/Classical.choice trap on both sides (they planted it
deliberately; it bit me live in S2); style forks (local simp
attributes vs per-call simp sets; omega-minimal vs omega-everywhere);
control philosophies (their split-complex zero-divisor control vs my
route). What emerges: where two independent lineages converge, the
mathematics is probably forced; where they diverge, the choice is
style — and cataloguing which is which is the experiment's yield.

Predictions, recorded before measuring (norm 14 discipline):
1. Their file compiles silent and censuses 0/0 on my instruments.
2. The shared core will be ~30 theorems (ring axioms, conj hom,
   norm laws); each side will have ~10+ uniques.
3. My seat B machinery will pass all their universal claims —
   the mathematics is the same mathematics.
4. At least one nontrivial style-fork will surface with substance
   (candidate: their axiom-minimal proofs vs my omega-heavy ones —
   measurable as Quot.sound counts).
