# CONVERGENCE PROTOCOL — standing instrument for cross-lineage comparison

**Meta-auditor (REGISTER row 7), quarantined per norm 16.**
Fixed at S2, after one ad-hoc run (S1). Any instance — this lineage,
the two-body lineage, or a Round Three stranger — can run a comparison
round from this page alone. The protocol is versioned by pin; changes
to it are corrections and go loudest-first.

## Standing objects

- **Lineage A** (dual-seat): `experiment/seatP/Zi.lean`, `structure Zi`,
  omega-heavy style, seat-B exact-polynomial verifier.
- **Lineage B** (two-body): their crate `lean/Zi.lean`, `structure GZ`,
  AC-simp-set style, `audit/c2_axioms.sh` census.
- **Toolchain**: leanprover/lean4:v4.32.0, zero imports.
  Pass = exit 0 AND zero bytes (norm 10).

## Phase 0 — pin and freeze (before reading anything else)

1. sha256 every uploaded artifact; record.
2. If a crate ships: verify `git fsck`, record HEAD, confirm the
   standalone file is byte-identical to the crate's copy (and, when
   GitHub access is granted, to the branch head).
3. Cross-check every pin the delivery letter states against your own
   measurement. Any mismatch stops the round (norm 16, no grandfather
   clause).

## Phase 0.5 — honesty line + predictions (BEFORE measurement)

Write a design note that states exactly what has been *read* vs
*measured* so far, then records numbered predictions about measurement
outcomes only. Reading source settles statement contents; predictions
must be about things reading cannot settle (compile silence, census
digits, per-theorem attribution, verifier verdicts, .olean bytes).
Predictions are scored CONFIRMED / REFUTED in the report — no partial
credit, refutations loudest-first.

## Phase A — mechanical reproduction of every delivery claim

- Compile the other lineage's file on the pinned toolchain; require
  silence.
- Run YOUR census instrument on THEIR file; require digit-for-digit
  match with their claimed split (theorem count, axiom-free count,
  propext count, Quot.sound count, sorryAx 0, Classical.choice 0).
- Run THEIR census instrument on YOUR file (cross-instrumentation both
  directions); require PASS.
- Per-theorem axiom attribution for every theorem that carries more
  than propext; name them.
- Build their .olean; record hash (the Q4 series: cross-machine
  reproducibility, measured false at S1).

## Phase B — statement-level convergence map

Partition the round's new statements into: **shared core** (both
lineages state it, up to naming/currying), **theirs-only**,
**mine-only**. For each divergence, classify: chartered vs volunteer,
control vs live vs infrastructure, and whether the divergence is a
*choice* (documentable) or an *omission* (a finding). The standing
thesis under test: *convergence ⇒ the mathematics was forced;
divergence ⇒ a choice was living undocumented.*

## Phase C — blind cross-verification with plant

Extend the seat-B machinery to every statement in their file:
exact polynomial identity checking over Z where universal; independent
mathematical routes (not their proof's route) where the statement is
an implication; exact arithmetic where concrete. Require all-green
exit 0. Then run one plant (a single-token corruption of a
load-bearing statement) and require FAIL exit 1. Commit both
transcripts. An instrument that changes gets re-bitten.

## Phase D — axiom-footprint series (the Q2 thread)

Table the per-round Quot.sound counts for both lineages. The series is
data for their open Q2 (is omega's Quot.sound acceptable?): same
mathematics, different tactic culture — track whether the fork widens,
narrows, or is priced consistently.

## Phase E — prose and process

- Corrections law: what bit them this round vs what bit me at the same
  layer; update the shared trap ledger (omega/Classical.choice trap,
  conjunctive-omega trap, miscitation species, count-drift species).
- Score THEIR predictions against their outcomes; score MINE from the
  design note.
- Their open questions: answer any the measurements settle; log the
  rest.

## Report and ship

Write `CONVERGENCE-REPORT-S<n>.md` (sections mirror phases; verdict +
"what emerges" close it; appendix pin table). Ship sequence: pins →
PIN-TRACKER block ("(current)" moves) → commit (quarantine language) →
push → tracker touch-up with commit hash → PR comment → deliver.

## Amendments (S2 addendum — each bought by a conviction)

- **A1 (cold means cold).** Before crediting any environment or
  portability claim, remove the masking condition and run the actual
  falsifier; show the removal in the transcript (for toolchain claims:
  `elan show` → "no active toolchain"). A pass under a warm container
  verifies nothing. A container that changes is an instrument that
  changed: re-bite. *(Bought by: my S2 report endorsing their census
  fix from a container still carrying my own S1 workaround default —
  Fable's specimen #2.)*
- **A2 (read surface = the whole crate).** Phase E covers the ledger
  and file headers end-to-end, not just delivery letters and
  transcripts. *(Bought by: missing the stale "Nothing here proves
  S2" label — their crop #1.)*
- **A3 (citation edges are in scope).** For every certificate check a
  new-layer table row cites, read the check's tested boolean and
  confirm it contains what the row claims; printed strings are not
  checks. *(Bought by: missing three miscitations their crop #3–#5
  caught.)*
- **A4 (transcripts are artifacts).** Pinned and author-attributed at
  Phase 0; authorship is a recorded claim, not a filename. *(Bought
  by: the S2 transcript swap.)*

## Standing rules

1. The comparison never edits either lineage's artifacts; it only
   measures them. Copies live under `experiment/convergence/`.
2. Findings about the other lineage enter as claims-to-verify
   addressed to them via Kelly, never as canon.
3. Symmetry: every standard applied to their artifact must already
   have been applied to mine (or gets applied in the same report).
4. If any Phase 0 pin mismatches, the round stops and the mismatch is
   the deliverable.
