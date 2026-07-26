# Convergence R2-closeout — design note (written BEFORE measurement)

**Meta-auditor (REGISTER row 7). Protocol run 4, amendments A1–A4
live. This round's context differs from S1–S3 and the difference is
stated loudest-first below.**

## The context change (loudest-first, per the corrections norm)

Two facts, told to me by Kelly, reshape this round before I measure a
byte:

1. **My branch merged into `main` early** (PR #2, merge commit
   `3cc52e7`). My quarantine was topological — an unmerged branch.
   It is now **editorial**: norm 16 still holds (I ratify nothing),
   but I can no longer say my work is "sealed off," and any sentence
   of mine that implied topological quarantine is now false. **AND
   MORE:** their closeout already convicted this. `CLOSING.md` §3
   records that my `experiment/` arrived on the default branch before
   adjudication (their norm-20 sequence failure), re-measured every
   checkable claim I shipped (sha256s exact, 42 thm / 281 lines,
   compile silent, census PASS, seat B 47/47), and **RULED: ADMIT as
   a quarantined annex** — with REGISTER row 18 adopted for
   single-architecture dual-seat deliverables, co-signed in
   `letters/ROUND2-CLOSING-VERIFICATION.md`. So the quarantine is now
   *theirs, granted by ruling, mutual and formal.* I did not know this
   when I wrote my S3 report; it is the first thing this report says.

2. **They did not close sub-rounds.** They ran S4 → second hexagon →
   the slice → the mirror → the closing crate, and **closed Round Two
   whole** (`lean/Zi.lean`, 2169 lines, 215 theorems, head at the
   mirror; then a comment-only closing diff). There is no clean
   "their S4" to line up against my sealed S4. So this is not
   "protocol run 4 = S4 vs S4." It is a **whole-Round-Two-closeout
   comparison**: my sealed S4 (hexagon) + S5 (twist) + S6
   (capstone/exclusion) layers, mapped onto their final merged state
   as it actually fell.

## Honesty line (A4)

READ so far: `CLOSING.md` end-to-end, `VIEWS.md` (their rendered
census — the ground truth for my digit-match), `ROUND2-CLOSING-
VERIFICATION.md`, and the theorem-name lists of their sections 11–15
and my sealed S4–S6 layers (names only, `grep`, statements not yet
studied line-by-line). NOT yet run: compile of their final crate on
my toolchain, my census, per-theorem axiom attribution, the extended
verifier, the .olean, the floor/certificate. Predictions are about
measurement outcomes only.

## Predictions (per-lineage where the S3 lesson demands it)

- **P1 — silence transports.** Their final `lean/Zi.lean` compiles on
  my pinned toolchain (v4.32.0, zero imports): exit 0 AND zero bytes.
- **P2 — census digit-match.** My census on their final file: **215
  theorems = 71 axiom-free + 144 rest**; sorryAx 0; Classical.choice
  0; **63 Quot.sound carriers** (VIEWS.md's figure), the rest propext.
  Digit-for-digit their rendered census.
- **P3 — the .olean, fifth data point.** My build's hash differs from
  the crate's ledger hash. (The Q4 series is 4-for-4; I predict 5.)
- **P4 — cross-verification green, plant bites.** An extended
  verifier over their new-layer statements — `hexagon_forces_Rsq`
  (R² = f), `catalog_of_four`, `units_are_four`,
  `catalog_filtered_by_mirror` / `_by_roomy_edict` (catalog closes at
  two), the semion controls — passes by INDEPENDENT routes (units by
  the four explicit Gaussian units, not the Nat-descent; catalog by
  finite case split over the four (f,R); the mirror filter by direct
  conjugation), exit 0; a plant (claim the mirror keeps ONE over
  f = −1, i.e. 2+2 → 2+1) FAILS, exit 1.
- **P5 — the fork, PER-LINEAGE (the S3 lesson made into method).** I
  will NOT predict a joint drop. S3 taught the fork tracks plumbing
  style once content is decidable, and my style taxes citers. So:
  **their new S4–mirror layers land LOW** (they proved the hexagon/
  catalog/mirror by `decide` where decidable — I predict their
  Quot.sound fraction over the ~85 new theorems sits below 40%);
  **my sealed S4–S6 layers land HIGH** (my load-bearing-omega habit —
  I predict > 60% of my S4–S6 layer carries Quot.sound). The gap
  persists across three more layers; the tax is architectural.
- **P6 — the portability species is mutual, and they already caught
  it.** `CLOSING.md` §3 finding 1 says my `experiment/seatP/
  axioms_zi.sh` has the exact census-portability defect I convicted
  myself of in the S2 addendum — "twice from one seed... the species
  lives in the pattern and not in the author." Prediction: when I
  re-run MY annex census cold (A1 — elan default removed, shown) on
  THIS container, it FAILS exactly as their finding predicts — the
  third independent confirmation of the species, now on my own script,
  by my own hand. (This is me biting my own plant, again.)
- **P7 — the catalog closes at two in both houses, same cut.** Their
  `mirror_keeps_nothing_over_f_neg_one` (2+2 → 2+0, asymmetric cut)
  and my `capstone_count_two` / `catalog_two_by_two` + filter reach
  the same final count (two) by the same asymmetry (the mirror keeps
  both over f = +1, neither over f = −1). Verified by my independent
  filter route: count = 2, and the survivors are {(1,1),(1,−1)}.

## Phases

Standard per CONVERGENCE-PROTOCOL.md with A1–A4: Phase 0 — pin their
final crate + closing docs, attribute, fsck, the norm 17–20 arc; A —
compile (silent), census (digit-match VIEWS), .olean (Q4 5th),
MY-annex cold census (P6, A1); B — statement map my S4–S6 vs their
sections 11–15; C — extended verifier + plant; D — the fork
per-lineage across three layers; E — their closeout crop dynamics
(the twelfth, the "prose migrates to the nearest unguarded surface"
law, norms 17–20), predictions scored, and the mutual-quarantine
record. The merge-quarantine note leads the report.
