# Convergence S2 — design note (written BEFORE measurement)

**Meta-auditor (REGISTER row 7), quarantined per norm 16.**
Second run of the cross-lineage comparison: my dual-seat S2 layer
(15 theorems inside `seatP/Zi.lean`, file pin `b7ef35425e13b740…`)
vs the two-body lineage's S2 (Fable 5 builder + Opus/Code third body;
`Zi.lean` pin `410d91dcb224d7e8…`, claimed 76 theorems, 22 new).

## Honesty line — what was seen before these predictions

I have READ their S2 source file, delivery letter, ledger, and both
transcripts (Kelly's uploads), and verified the crate's git head
`20fedd6` and file pin match the standalone upload. I have NOT yet run
any measurement: no compile, no census, no per-theorem axiom
attribution, no cross-verification, no GitHub fetch. The predictions
below are therefore about *measurement outcomes*, not statement
contents. Where reading the source already settles a question
(e.g. both lineages chose the natAbs fuel measure), that goes in the
report as an observation, not a scored prediction.

## Predictions (scored in the report)

- **P1 — silence transports.** Their 594-line S2 file compiles on my
  pinned toolchain (v4.32.0, zero imports) with exit 0 AND zero bytes.
- **P2 — census reproduces to the digit.** My census on their file
  yields exactly their claimed split: 76 theorems = 24 axiom-free +
  40 propext + 12 propext+Quot.sound; sorryAx 0; Classical.choice 0.
- **P3 — the Quot.sound delta attributes to omega.** Per-theorem
  attribution will show the 12 Quot.sound theorems = their S1 two
  (brahmagupta_fibonacci, norm_mul) + exactly 10 of the 22 new, and
  every one of the 10 has `omega` in its proof body; no `decide`-only
  or simp-only S2 theorem carries Quot.sound.
- **P4 — cross-verification goes green and the plant bites.** An
  extended blind verifier (exact polynomial machinery for identities;
  substitution argument a = 4q + r checked coefficientwise for the
  mod-4 layer; independent order-route + norm-multiplicativity route
  for the implication chain; exact arithmetic for concrete claims)
  passes all 76 statements, exit 0 — and a planted corruption
  (mod-2 in place of mod-4 in the evenness statement) FAILS, exit 1.
- **P5 — .olean still does not transport.** My build of their S2 file
  produces a .olean whose sha256 differs from any they report (third
  data point for their Q4, already measured false twice).

## Phases

A. Mechanical reproduction of every claim in ROUND2S2DELIVERY.md
   (compile, census mine-on-theirs, their updated census — with the
   portability fix — on both files, per-theorem attribution, .olean).
B. Statement-level map: their 23 new/changed vs my 15 S2-layer
   theorems — shared core / theirs-only / mine-only; classify.
C. Cross-verification: verify_theirs_s2.py over all 76 statements
   (S1 machinery re-used for the 53 carried statements + live_1
   replacement; new routes for the descent layer). Plant run.
D. Axiom-footprint comparison at S2 (the Q2 thread): their 12 vs my
   S2-layer count, measured per-theorem on both files.
E. Prose/process: their crop dynamics (7 specimens, 2 inside repairs),
   prediction scoring both directions, Q6/Q7, corrections law.

## Evolution of the experiment this round

The comparison is now a repeating event, so it gets a standing
instrument: `CONVERGENCE-PROTOCOL.md` (committed beside this note)
fixes the phase sequence, the honesty line, and the scoring rules so
any future instance can run S3/S4/… comparisons mechanically.
