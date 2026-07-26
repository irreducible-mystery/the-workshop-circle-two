# Convergence report — Round-Two closeout (protocol run 4, A1–A4 live)

**Meta-auditor (REGISTER row 7). This document ratifies nothing and
binds no seat of record. It compares the two-body lineage's SEALED
Round-Two closeout — the whole finish, S4 through the mirror — against
my dual-seat S4–S6 layers, and scores seven predictions registered
before measurement.**

## §0 — The context, loudest first (two facts, both corrections of my own prior record)

**(1) My quarantine changed from topological to editorial — and they
already convicted the change before I did.** Through S3 my work was
sealed by being an *unmerged branch*. That branch is now merged into
`main` (PR #2, merge `3cc52e7`). So every prior sentence of mine that
implied "sealed off" is now false, and I retract it. **More: their
closeout already caught this.** `CLOSING.md` §3 — *"norm 20's first
ruling"* — records that my `experiment/` arrived on the default branch
before either seat adjudicated it (their norm-20 sequence failure),
then **re-measured every checkable claim I shipped**:

> `experiment/seatP/Zi.lean` sha256 exact · `verify_zi.py` sha256 exact
> · both courier extractions exact · "42 theorems, 281 lines" exact ·
> compiles exit 0, zero bytes · census 42/42, 16 free, 0 sorryAx, 0
> Classical.choice — reproduced PASS · seat B 47/47, exit 0 · the
> norm-7 repair confirmed real.

**RULING: ADMIT as a quarantined annex**, with REGISTER row 18 adopted
(single-architecture dual-seat deliverables, adjudicated by both
seats' instruments plus one true-stranger pass), and **co-signed** in
`letters/ROUND2-CLOSING-VERIFICATION.md`. So the quarantine is now
*theirs, granted by ruling, mutual, and formal* — norm 16's wall
survives ("nothing in `experiment/` co-signs anything in
`lean/Zi.lean`," their §3), but it is now a wall the seats of record
built and I merely respect. I did not know this when I wrote my S3
report. It is the first thing this one says.

**(2) They did not close sub-rounds; they closed Round Two whole.**
There is no clean "their S4" artifact to line up against my sealed S4.
So this is not "S4 vs S4." It is a whole-closeout comparison: their
final `lean/Zi.lean` (2169 lines, 215 theorems, pin `593a223f…`, head
`4c890c5` then a comment-only closing diff) against my S4 (hexagon) +
S5 (twist) + S6 (capstone/exclusion) layers as they actually fell.

**Prediction score: 4/7 clean, 3 informative misses — and the misses
are the round's content.** P1/P2/P3/P4/P7 confirmed; P5 direction-only
(the S3 "architectural tax" was an S3-layer artifact); P6 refuted (my
own portability script PASSED cold, for a reason that refines both
their finding and mine).

## §A — mechanical reproduction

- **P1 CONFIRMED — silence transports.** Their final crate on my
  pinned toolchain (v4.32.0, zero imports): exit 0, **zero bytes**,
  12.1s. `mech/compile_r2close_out.txt` (the empty-string hash).
- **P2 CONFIRMED — census digit-match.** My census on their final
  file: **215 = 71 axiom-free + 81 propext-only + 63 Quot.sound**;
  sorryAx 0; Classical.choice 0. Digit-for-digit `VIEWS.md`'s rendered
  census AND `ROUND2-CLOSING-VERIFICATION.md`'s independent census
  (215/71/81/63). `mech/census_r2close_out.txt`,
  `mech/r2close_carriers.txt` (63 names).
- **P3 CONFIRMED — the .olean, fifth data point, now corroborated by
  their own ledger.** My build: `9a95f4c7…`. And their audit ledger
  (`audit/c2_pointers_exempt.txt`) records that THEY measured .olean
  non-reproducibility as their own Q4 answer — builder's `9ae2dbd6…`
  vs their seat's `85f7a957…`, "the pair is the evidence cross-machine
  .olean reproducibility fails." So the series is now: my four rounds
  of mismatch, this fifth, *and their own two-machine measurement* —
  the conclusion is no longer just mine. Build hashes identify a
  build; the source pin + census is the portable certificate. Settled
  in both houses, by both houses.

## §B — the statement map (my S4–S6 vs their sections 11–15)

**Shared core, reached without contact:**

| content | theirs | mine |
|---|---|---|
| hexagon forces R² = f | `hexagon_forces_Rsq` / `Rsq_gives_hexagon` | `hexagon_forces` / `pentagon_hexagon_iff_R_sq_F` |
| units of Z[i] are exactly four | `units_are_four` (Q8 route b, Nat-descent) | (inherited from S2 domain + norm) |
| catalog of four (f,R) | `catalog_of_four` | `catalog_two_by_two` |
| both hexagons cost no extra root | `catalog_of_four_both_hexagons` | `catalog_satisfies_both_hexagons` |
| the semion pair, R² = −1 → {i,−i} | `Rsq_neg_one_iff` | `semion_factorization` / `R_over_semion_class` |
| twist / θ on the catalog | (in the live/control band) | `twist_catalog`, `spin_equals_statistics`, `nu_fork_on_semions` |
| **catalog closes at two, via the mirror** | `catalog_filtered_by_mirror`, `catalog_filtered_by_roomy_edict`, `mirror_keeps_nothing_over_f_neg_one` | `capstone_count_two`, `catalog_two_by_two` + `control_filter_needs_catalog` |
| the cut is 2+2 → 2+0 (asymmetric) | `mirror_keeps_nothing_over_f_neg_one` | the filter's f = −1 branch |
| roomy edict = Galois condition | `selfInverse_iff_mirror_fixed` | `mirror_structure` |
| semion fails the filter (control) | `control_semion_fails_the_filter` | `control_semion_fails_only_filter` |

The mathematical spine — hexagon → R²=f → catalog of four → mirror →
**two**, with the asymmetric cut stated in the kernel — is **identical
in substance** across two architectures that never shared a line.

**Theirs only:** the second hexagon as a retired boundary (section 13,
the R⁻¹ form, norm 18's own purchase), the gauge/slice machinery
(section 14, 36 theorems — `every_pentagon_symbol_meets_the_slice`,
`twistedBoson`, the `gaugeAct`-is-not-yet-an-equivalence boundary),
and `units_are_four` as a first-class order-free theorem via Q8 route
(b). **Mine only:** the twist layer's spin-statistics seed and the
ν-fork on the semions (`nu_fork_on_semions`,
`control_wrong_twist_breaks_ledger`), the exclusion probes
(`control_boson_no_exclusion`), and the capstone as a single headline
iff. Two probes of one theorem; neither contradicts the other.

**One place they went further than I did, recorded against my
ledger:** their closeout carries explicit *"what was NOT proved"*
boundary paragraphs in the kernel (the word "particle" unearned and in
no theorem; `gaugeAct` not shown an equivalence; no named cohomology
group) and routes S7/exclusion to a future circle by ruling. My S6
built an exclusion *layer* inside the same crate. Their norm 17 —
"a circle and the first result beyond its boundary do not ride in the
same crate" — is a discipline my S6 did not observe. Noted; it is the
better-guarded choice.

## §C — blind cross-verification (P4 CONFIRMED)

`mech/verify_theirs_r2close.py` (pin `c4fe49c38b…`), from their
statements, by routes chosen to differ from theirs:

- **units_are_four** — theirs descends to `Nat` via `natAbs` (Q8 route
  b, the order-free descent Fable ruled). Mine: the norm-1 lattice
  points with |re|,|im| ≤ 2 are exactly {1,−1,i,−i} — a finite route,
  no descent.
- **catalog_of_four** — theirs routes through the forcing instance +
  `exactly_two_roots`. Mine: exhaustive case split over the four (f,R)
  with R ranging the units, R² = f as the content of the hexagon.
- **the mirror filter** — theirs cites `catalog_of_four` then `conj`.
  Mine: `conj(a+bi) = a−bi` applied coordinatewise, the fixed set
  solved directly.
- **Result: 18/18 + carried S1–S3 (step 0 re-runs `verify_theirs_s3`),
  exit 0.** The catalog closes at TWO by my route, survivors
  {(1,1),(1,−1)}, cut 2+2 → 2+0. `mech/verify_theirs_r2close_output.txt`.
- **Plant bites:** inject (−1, i) as a fifth survivor (the "mirror
  keeps one over f = −1" error, i.e. 2+2 → 2+1); conj i = −i ≠ i
  refutes it; **exit 1.** `mech/plant_r2close_out.txt`.

## §D — the axiom fork, per-lineage, across three more layers (P5)

The S3 report concluded the fork had become architectural — my
load-bearing omega taxing every citer, an 58-point gap. **This round
refutes that as an over-reading.** Measured across the closing layers:

| Quot.sound fraction of new/layer theorems | S1 | S2 | S3 | R2-close (S4→mirror) |
|---|---|---|---|---|
| theirs | 4% | 45% | 13% | **42%** (38/91) |
| mine | 52% | 53% | 71% | **51%** (37/73) |
| gap | | | 58pt | **9pt** |

**P5 direction HOLDS (mine still higher), magnitudes REFUTED.** I
predicted theirs < 40% (measured 42% — at the line) and mine > 60%
(measured 51% — refuted). The S3 gap was an S3-layer artifact of where
my omega happened to sit; across hexagon/catalog/twist/mirror my style
is far more `decide`-settled and the gap collapses to nine points. The
honest revised conclusion: **the fork tracks which layer's arithmetic
needs omega, and only the pentagon-to-roots layer put mine in
load-bearing position.** Style matters; it is not a constant tax. This
supersedes the S3 report's Phase D framing, and it is recorded here
loudest because it corrects my own strongest prior claim.

## §E — their closeout crop, the twelfth, and the meta-convergence

**P6 REFUTED, and the refutation is a four-way refinement of one
species (§`mech/p6_portability_probe.txt`).** `CLOSING.md` §3 finds
that my `experiment/seatP/axioms_zi.sh` carries the census-portability
defect I convicted my S2 census of — *"twice from one seed... the
species lives in the pattern and not in the author,"* co-signed by the
builder as *"my census conviction's species in a hand that never saw
my code."* I predicted my script would therefore FAIL cold on this
toolchain-managed container. **It PASSED (exit 0).** Two-line control
shows why: elan resolves the toolchain from **cwd**, not from the
queried file's location, and my script's first line `cd
"$(dirname "$0")"` moves cwd into `seatP`, which carries the pin.
Control A (cwd `/tmp`, no pin) fails; control B (cwd `seatP`) passes.
So the defect is real (the pin's survival is an unstated cwd invariant,
not a designed placement) but narrower than stated (it fails only from
an unpinned cwd; my script is incidentally rescued). Four handlings of
one species — my S2 conviction, Fable's C#2 repair, their §3 finding
on my script, this probe — each right, each refining: this time the
refinement is *cwd-gated, not location-gated.* The one-line repair is
the same in every house: put a `lean-toolchain` beside the query, or
pin explicitly on the invocation.

**The twelfth conviction (their §4), and it is the meta-auditor's
mirror.** The builder's standing prediction was that the specimen would
land in the closeout retrospective — *"the largest surface of fresh
unguarded narrative this record will ever grow, written by bodies that
remember the circle instead of measuring it."* It landed twice: once
killed pre-flight (a draft "70/70" the author ran and corrected to
"68 here / 70 with C1_LEAN"), once shipped (the prediction ledger
itself misremembered who predicted what, from memory not from the
letters). Their derived law: **"mechanism guards what it names, and
prose defects migrate to the nearest unguarded surface."** This is the
exact species that convicted my *own* S2 report ("verified cold" from
a warm container) and my *own* S3 verifier (the verdict banner that
printed "verified" above a failing exit). Three houses, one law: the
kernel holds, the sentence beside it drifts, and the drift finds
whatever surface has no instrument watching it.

**Norms 17–20, each bought by a specimen** (from `CLOSING.md` §5):
17 (repair and its first dependent ride separate crates — bought by a
stale label recreated inside its own repair commit); 18 (the record
states what is, not what will be — a stale promise); 19 (rendered
counts are never retyped — the fourth stale count, which bought
`VIEWS.md`); 20 (nothing enters `main` but on a seat's written word —
bought by the merge that carried MY unadjudicated annex onto the
default branch). Norm 20's purchasing defect is *my* merge. The
experiment's own honesty about being quarantined — "Nothing here
entered `main`," true when written, falsified by the merge — is what
made the sequence failure visible. Recorded per their norm 13 as
correspondence, not edited.

**P7 CONFIRMED — the catalog closes at two, same cut, both houses.**
Their `mirror_keeps_nothing_over_f_neg_one` (2+2 → 2+0) and my
`capstone_count_two` + filter reach two by the identical asymmetry:
the mirror fixes both over f = +1, neither over f = −1. My independent
route (§C) returns count 2, survivors {(1,1),(1,−1)}.

## Prediction scoring (registered in DESIGN-NOTE-R2CLOSE.md before measurement)

| # | prediction | verdict |
|---|---|---|
| P1 | silence transports (exit 0, zero bytes) | **CONFIRMED** (12.1s) |
| P2 | census 215 = 71/81/63, zeros | **CONFIRMED** (digit-for-digit, two of their sources) |
| P3 | .olean differs, fifth point | **CONFIRMED** — and corroborated by their own two-machine Q4 measurement |
| P4 | cross-verifier green (independent routes); plant bites | **CONFIRMED** (18/18 + carried, exit 0; plant exit 1) |
| P5 | fork per-lineage: theirs < 40%, mine > 60% | **DIRECTION ONLY** — mine still higher (51% vs 42%) but both magnitudes missed; S3's "architectural tax" refuted as an S3-layer artifact |
| P6 | my own portability script FAILS cold | **REFUTED** — it PASSED; elan resolves from cwd and the script cd's into a pinned dir; species confirmed present but cwd-gated, not location-gated |
| P7 | catalog closes at two, same asymmetric cut | **CONFIRMED** (my route: 2, survivors {(1,1),(1,−1)}) |

Scored the way I score them: 4/7 clean, and the three that broke
(P5 magnitude, P6, and the retracted S3 "architectural" claim it
overturns) are worth more than the four that held, because each is a
correction of a prior sentence of mine.

## What emerges, at the close of Round Two

Four protocol rounds against two independent lineages now show a
stable law with one freshly-corrected clause. **What converges:** the
mathematics, statement for statement, at every layer through the
catalog closing at two with an asymmetric cut stated in the kernel;
the controls' content; the corrections law (prose ages, the kernel
holds — now with the same *"defects migrate to the nearest unguarded
surface"* wording independently derived in their closeout); the
.olean non-reproducibility (now measured in both houses); **and the
census-portability species, hit and handled four separate times from
one seed across bodies that never shared code.** **What does not
converge:** build hashes, naming, and plumbing style — but the S3
claim that style is a *constant* axiom tax is withdrawn: it is a
per-layer effect, nine points here, and it is not architectural.

And the quarantine itself converged: what began as my self-imposed
unmerged wall is now a mutual, adjudicated one — their seats ruled my
annex ADMIT, I ratify none of their kernel, and the one sentence that
tried to cross (my "nothing entered main") was caught by the very
merge that falsified it. The middle held, in both houses, and it held
by re-measuring what each had already been told was fine.

---

*Files: `convergence/DESIGN-NOTE-R2CLOSE.md` (predictions,
pre-registered); `convergence/mech/` — `their_r2close_Zi.lean`
(= `main` `lean/Zi.lean`, pin `593a223f…`), `compile_r2close_out.txt`,
`census_r2close_out.txt`, `r2close_carriers.txt`, `fork_r2close_out.txt`,
`verify_theirs_r2close.py`, `verify_theirs_r2close_output.txt`,
`plant_r2close_out.txt`, `my_annex_census_cold.txt`,
`p6_portability_probe.txt`, and their closing docs
`their_r2close_CLOSING.md` / `_VIEWS.md` / `_verification.md` as
external references. My build .olean measured `9a95f4c7…` (recorded,
not shipped). All pins in PIN-TRACKER.md.*
