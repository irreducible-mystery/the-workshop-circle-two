# PIN TRACKER — hashes ↔ artifacts, one page

**For Kelly.** One row per pinned artifact, newest sub-round first.
Convention going forward: every sub-round adds one small block here at
ship time — artifact path, what it is, sha256 (first 12 chars are enough
to grep; full hash lives in the sub-round report). To verify any pin:
`sha256sum <path>` and compare. All paths relative to `experiment/`.

**Branch:** `superninja/dual-seat-experiment-s1` · **PR:** #2 (open; PR #1 merged S1)

---

## Round Three — meta-audit + S7c gate-scope extension (current)

The meta-auditor (REGISTER row 7, second instance) shipped the stranger
audit and, on Kelly's charge "S7c+S7a (your rec)", extended the front-door
prose gates to the row-8 boundary `experiment/**`. Sanctioned scope
divergence from the predecessor's S7a-first recommendation, recorded in
source/commit/report. Quarantine (norm 16): the extended gates are new
instruments; their PASS is a claim verified by plant-and-restore on this
tree, not a result to trust on sight. `lean/Zi.lean` ratified by none of it.

| artifact | what | sha256 (short) |
|---|---|---|
| `seatMETA/verify_stranger.py` | independent blind verifier, 27/27, own routes | `cf603918357d` |
| `audit/c2_pointers.sh` (S7c) | pointer gate, scope extended to experiment/** | `987024b9c12f` |
| `audit/c2_numerals.sh` (S7c) | numeral gate, scope extended to experiment/** | `20eee8348e08` |
| `audit/c2_views.sh` (S7c) | censusguard falls back to seatP/Zi.lean | `34db10a8cae5` |
| `audit/probes/s7c_scope_probe.sh` | the S7c design probe (norm 15) | `64b0d293eda3` |
| `audit/probes/S7C-DESIGN-NOTE.md` | the S7c design note (measured blast radius) | `f8abac6e18e1` |
| `seatMETA/CORRECTIONS-LETTER-S7c.md` | the S7c crop (five items) | `fd69cfd84136` |

Full 64-char (S7c gates, measured on the shipped tree):
- `c2_pointers.sh`  `987024b9c12f1e641e76497555571a4877b6d0f61adbcf03aa939f6a6001bb22`
- `c2_numerals.sh`  `20eee8348e08c970a5c773e91fd7512d9bda16d6a5b685b2ed69523ea217b0d8`
- `c2_views.sh`     `34db10a8cae52366739b7c2d5a4cf49de56235cee14c44792e534e529bdc8387`
- `verify_stranger.py`  `cf603918357dd97cc902a40f8c8e99b0e82c6e2e6ec87d92751b7f03c8720efe`

### S7a — the slice lemma's reachable core (stretch goal, COMPLETE)

The G1c slice lemma "every class meets the normalized slice" was proven in the
sharpest zero-import-reachable form (the unit locus) plus a measured
impossibility for the full H3(Z2)=Z2 sentence. `seatP/Zi.lean` grew from 161 to
172 theorems; census PASS with zero sorryAx and zero Classical.choice; norm 16
confirmed both directions on the Lean instrument, the axiom census, and seat B.

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (with S7a) | 172 thm, +11 S7a | `d1f3617baaef` |
| `seatP/axioms-zi.txt` | census, 172/172, 0 sorryAx, 0 choice | `1de8439c2de3` |
| `courier/Zi_statements_v8.txt` | statements v8, mechanical re-extraction | `914a80d58d71` |
| `seatB/verify_zi_s7a.py` | seat B blind, 11/11 own routes | `077fb33e25a9` |
| `seatB/s7a_seatB_out.txt` | seat B evidence (clean run) | `4e741fbbe5c9` |
| `seatP/probes/s7a_design_probe.lean` | probe 1: statability | `ac16c2e33906` |
| `seatP/probes/s7a_design_probe2.lean` | probe 2: finite skeleton | `67689c2ed8ff` |
| `seatP/probes/s7a_design_probe3.lean` | probe 3: unit-locus decidable | `a643cfb4371b` |
| `seatMETA/S7A-DESIGN-NOTE.md` | design note, named adjudicator | measured at ship |
| `seatMETA/CORRECTIONS-LETTER-S7a.md` | S7a crop (five, loudest-first) | measured at ship |

Full 64-char (S7a Lean artifacts, measured on the shipped tree):
- `seatP/Zi.lean`  `d1f3617baaefcbb85b049709ffee600dbdc6a20b8748edcb637fea4d8291145d`
- `seatP/axioms-zi.txt`  `1de8439c2de3477099aa7315166186671b0885cad0f44925ac693fef5c7c3599`
- `courier/Zi_statements_v8.txt`  `914a80d58d710de0d3273ca144d5e2e44966bb295e65c5f0791c6b8a02e1d5b5`
- `seatB/verify_zi_s7a.py`  `077fb33e25a9684c46065837900e16fb8e1eb6be4a33d72febbed61b4ce7dbe0`

The audit-verdict, findings, worklog, and SUBROUND7-REPORT pins are measured
at commit and recorded in the commit message (they cite each other, so their
hashes settle only once all are on the branch).

commits (branch `superninja/dual-seat-round3`, PR #6):
- `92e291d` S7c — prose gates extended to `experiment/**`
- `cb34da4` S7a — the slice lemma's reachable core + measured impossibility
- `d25c08d` S7a fixup — filled the empty plant-evidence files (lean errors to stdout)

delivery bundle: `dual-seat-round3.zip` — `git archive` of the branch tip
`d25c08d`, sha256 measured at ship (the zip pins the exact shipped tree).

---

## Convergence dashboard — the whole series on one page, GENERATED not typed (current)

Change #2 of the retrospective, built. A generator (`mech/make_dashboard.py`)
reads the mech receipts and emits `CONVERGENCE-DASHBOARD.md` — the four-round
series (verifier count, plant falsifier, census split, axiom fork) rendered
from files, never retyped. This is the two-body lineage's NORM 19 (rendered
counts are never retyped) adopted for my own record — and it goes one step
further on two points their norm didn't have to:
(1) **reproducible by hash** — the header stamps a deterministic inputs
digest (`09059a91f953`), not a wall-clock time, so the same receipts always
render byte-identical bytes; two runs and a cross-location run all produced
dashboard sha `9f206376960e`;
(2) **missing looks missing** — a receipt that vanishes renders `n/a (file
absent)`, never a stale value; proved by a falsifiability probe (hide the S3
receipt → the cell goes n/a; restore → the number returns).
Quarantine (norm 16): ratifies nothing in `lean/Zi.lean`.

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-DASHBOARD.md` | the rendered four-round series, one page | `9f206376960e` |
| `convergence/mech/make_dashboard.py` | the generator (parses receipts → dashboard) | `e27a6e339c23` |
| `convergence/mech/dashboard_falsifiability_probe.txt` | proof that a missing receipt renders n/a, not stale | `249a8e01b3ef` |

commit: `e2b3bae`

## Convergence retrospective — the meta-auditor's CLOSING mirror; the time-value answer

The closing artifact of the convergence experiment, written from the
row-7 chair to mirror their `CLOSING.md`. Measured, not remembered: §2
the epistemic yield (176 blind checks over 4 rounds; the corrections law
worded the same in both houses without contact; .olean non-reproducibility
measured in both; the census-portability species handled 4× from one seed
across 3 bodies), §3 the three self-convictions (S2 warm-container, S3
verdict-banner, R2 the withdrawn "architectural tax" + P6), §4 the
TIME-VALUE analysis Kelly asked for — the ~12h-vs-minutes framing
corrected (different passes, not like-for-like), then the slow loop's
measured yield: 4 norms + 3 register rows each specimen-bought, a real
checker bug found (class-c8, REGISTER row 16), and REGISTER row 18's
priced-out limit of the fast dual-seat method; §5 five changes I'd make.
Verdict: the hours aren't worth it for the theorem (cheap in both houses);
they buy the institutional immunity that outlives it.

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-RETROSPECTIVE.md` | the meta-auditor's closing retrospective + time-value analysis | `e858120c89e3` |

commit: `a4e9723`

## Convergence R2-closeout — the whole finish, twice; two corrections of my own record

Protocol run 4. **Context changed:** my branch merged into `main` early
(PR #2, `3cc52e7`) — quarantine now editorial, not topological; AND
their closeout already adjudicated my annex (`CLOSING.md` §3, norm 20's
first ruling): re-measured every claim I shipped, RULED ADMIT as a
quarantined annex, adopted REGISTER row 18, co-signed. The quarantine is
now theirs, mutual and formal. They also closed Round Two WHOLE (no
sub-round segmentation), so this compares my S4–S6 layers vs their final
merged crate (215 thm, pin `593a223f`, head `4c890c5`+closing diff).

All claims reproduce: silence transports (exit 0, 0 bytes, 12.1s);
census **215 = 71/81/63 digit-for-digit** (VIEWS + their verification
letter both); .olean fifth mismatch (`9a95f4c7`) — and their OWN ledger
records the same Q4 non-reproducibility (`9ae2dbd6` vs `85f7a957`).
Cross-verifier 18/18 + carried S1–S3: **units by the norm-1 finite route
(no Nat descent), catalog by case split, mirror filter by direct conj —
the catalog closes at TWO, cut 2+2→2+0**; plant (keeps 3) bitten.
Predictions 4/7 clean; the 3 misses correct me: **P5 — the S3
"architectural omega tax" was an S3-layer artifact; the fork gap
collapses to 9 points here (mine 51%, theirs 42%)**; **P6 — my own
portability script PASSED cold** (elan resolves from cwd; my script cd's
into a pinned dir — the species is cwd-gated, not location-gated; fourth
handling of one seed). The twelfth conviction (their §4) is my own
species one level up: "defects migrate to the nearest unguarded surface."

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-REPORT-R2CLOSE.md` | full closeout comparison, §0–§E + predictions 4/7 | `857f6b4114c3` |
| `convergence/DESIGN-NOTE-R2CLOSE.md` | honesty line + 7 predictions + the merge-quarantine note, BEFORE measurement | `cee04f55fdea` |
| `convergence/mech/verify_theirs_r2close.py` | independent-route verifier; 18/18 + carried, exit 0 | `c4fe49c38b58` |
| `convergence/mech/verify_theirs_r2close_output.txt` | clean run transcript | `8cc4158d9e4b` |
| `convergence/mech/plant_r2close_out.txt` | plant (mirror keeps 3 / 2+2→2+1) bitten — exit 1 | `64c315623597` |
| `convergence/mech/census_r2close_out.txt` | my census on their final crate: 215/71/81/63, 0/0 | `809f75aaf249` |
| `convergence/mech/fork_r2close_out.txt` | the axiom-fork series, per-lineage; S3 tax refuted | `e62d8d9dd682` |
| `convergence/mech/p6_portability_probe.txt` | P6 refuted; the cwd-vs-location mechanism; species confirmed narrower | `7213528bdf3f` |
| `convergence/mech/my_annex_census_cold.txt` | my own annex census, run COLD (A1): PASS, 161/68 | `6b1352210fde` |
| `convergence/mech/their_r2close_Zi.lean` | their final crate (external ref; = `main` `lean/Zi.lean`) | `593a223fcead` |
| `convergence/mech/their_r2close_VIEWS.md` | their rendered census (external ref) | `1e4904a95f4c` |
| `convergence/mech/their_r2close_CLOSING.md` | their closeout retrospective (external ref) | `c04a3d0e80de` |

commit: `7e7d2f1`

## Convergence S3 — the pentagon layer, twice; the fork re-opens in reverse

Third protocol round, amendments A1–A4 live. Their S3 (115 theorems =
carried 76 + 39 new, head `09f6fd7`) vs my S3 layer. All delivery
claims reproduce: silence transports; census 34/64/17
digit-for-digit, the 5 new Quot.sound carriers exactly as named;
census-repair falsifier PASSES COLD on the container that first
convicted it (A1 discharged, default-removal shown); .olean fourth
mismatch (Q4). Cross-verifier 26/26 + carried 76, **exactly-two
re-proved by the coordinate route — no domain theorem consumed**;
plant bitten. Predictions 6/7 by halves; the finding is P7's refuted
half: the axiom fork RE-OPENED with MY side high (theirs 13%, mine
71% on the same decidable layer) — style, not content, and the
ledger entry is mine. Fable's four specimens (929/930, stale
boundary bullet, scope prose) reproduced by measurement.

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-REPORT-S3.md` | full S3 comparison, phases A–E + predictions 6/7 | `1886df18b5b5` |
| `convergence/DESIGN-NOTE-S3.md` | honesty line + 7 predictions, BEFORE measurement | `42631031546b` |
| `convergence/mech/verify_theirs_s3.py` | coordinate-route verifier; 26/26 + carried 76, exit 0 | `3d2f129dbe69` |
| `convergence/mech/verify_theirs_s3_output.txt` | clean run transcript | `00eb125527c7` |
| `convergence/mech/plant_s3_out.txt` | plant (Z/8 roots claimed {1,7}) bitten — exit 1 | `89d62b65bd14` |
| `convergence/mech/their_s3_Zi.lean` | their S3 artifact (external ref; = GitHub `09f6fd7`) | `71cc55d54af8` |
| `convergence/mech/their_s3_statements.txt` | my courier extraction, 115 statements (first 76 = S2's, byte-identical) | `2d70d6a4fee8` |
| `convergence/mech/compile_s3_out.txt` | zero bytes (the empty-string hash) | `e3b0c44298fc` |
| `convergence/mech/census_their_s3_out.txt` | my census on their S3: 34/64/17, 0/0, all 17 named | `56f056a6ceb7` |
| `convergence/mech/census_s3_cold.txt` | their repaired census, COLD (A1: no elan default, shown): PASS | `014543892af4` |
| `convergence/mech/fable_s3_verification.md` | Fable's S3 letter (external reference) | `45c4760b1f67` |

commit: `f24764d`

## Convergence S2 addendum — a conviction of my own report

Fable's S2 verification letter arrived (nine specimens) plus Kelly's
provenance correction (the S2 transcripts were swapped at upload).
Loudest first: **my S2 report's "portability fix verified cold" was
FALSE** — my container carried my own S1 workaround default. Real
falsifier run (default removed): their fix fails (their #2 confirmed,
third container); elan reads the pin from cwd, not file location
(mechanism reproduced); Fable's one-line repair pre-verified PASS
cold. Report §1 amended in place; protocol gains amendments A1–A4,
each bought by a conviction. Cross-map of their nine specimens vs my
report: 1 convergent (594), 1 complemented (the named-12 list their #6
asks for already ships in my mech/), 4 missed, 1 backwards.

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-S2-ADDENDUM.md` | the correction + provenance + crop cross-map + protocol amendments | `62d7d8d4448a` |
| `convergence/CONVERGENCE-REPORT-S2.md` | amended §1 (warm-container endorsement struck, loudest-first) | `31d716c32657` |
| `convergence/CONVERGENCE-PROTOCOL.md` | amendments A1–A4 added | `13fa5f538267` |
| `convergence/mech/census_nodefault_out.txt` | real falsifier: their fix FAILS with no elan default, exit 1 | `dceb8d4f1675` |
| `convergence/mech/pin_resolution_probe.txt` | elan resolves pin from cwd, not file location | `92ba59503b91` |
| `convergence/mech/census_fixed_nodefault.txt` | Fable's one-line repair: PASS cold, 76 = 24+40+12 | `186cac925fbf` |
| `convergence/mech/fable_s2_verification.md` | Fable's letter (external reference) | `511fb865056c` |

commit: `2d71f26`

## Convergence S2 — the domain, twice

Second protocol round (standing instrument fixed this round:
`convergence/CONVERGENCE-PROTOCOL.md`). Their S2 (76 theorems, head
`20fedd6`, PR #3) vs my S2 layer. All delivery claims reproduce;
census 24/40/12 digit-for-digit; cross-verifier 78/78 **by the order
route their labelled fork declined**; plant bitten; axiom fork
COLLAPSED at S2 (content, not culture); predictions 4/5 — P3 refuted,
reported loudest-first. One claim-to-verify for them: letter says
"593 lines", the pinned file measures 594.

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-REPORT-S2.md` | full S2 comparison, phases A–E + predictions 4/5 | `f57582c63dbc` |
| `convergence/CONVERGENCE-PROTOCOL.md` | standing cross-lineage protocol (the experiment's evolution) | `33747a567ce9` |
| `convergence/DESIGN-NOTE-S2.md` | honesty line + 5 predictions, BEFORE measurement | `ab8637569ac8` |
| `convergence/mech/verify_theirs_s2.py` | 76 statements verified on the ORDER prong; 78/78, exit 0 | `2047342f1ce4` |
| `convergence/mech/verify_theirs_s2_output.txt` | clean run transcript | `e20f99267de1` |
| `convergence/mech/plant_s2_out.txt` | plant (mod-2 for mod-4) bitten — 76/1, exit 1 | `16b8ace878b9` |
| `convergence/mech/their_s2_Zi.lean` | their S2 artifact (external reference; = GitHub `20fedd6`) | `410d91dcb224` |
| `convergence/mech/their_s2_statements.txt` | my courier extraction, 76 statements | `5197236fd860` |
| `convergence/mech/census_their_s2_out.txt` | my census on their S2: 24/40/12, 0/0, the 12 named | `223024bfff0e` |
| `convergence/mech/their_census_on_their_s2.txt` | their FIXED census, cold-start, on their crate: PASS | `e59bea53d1e8` |
| `convergence/mech/their_censusfix_on_mine.txt` | their fixed census on my file: PASS (byte-identical to S1 verdict) | `f94cdc2710e7` |

commit: `84500db`

## Convergence S1 — cross-lineage comparison

Comparison of my dual-seat S1 (42 theorems) against the independent
two-body lineage's S1 (Fable 5 builder + Opus/Code third body; 54
theorems, `structure GZ`). All their claims re-measured CONFIRMED;
cross-instrumentation green both directions; 32-statement shared core;
their open Q4 answered negative (.olean not cross-machine reproducible).

| artifact | what | sha256 (short) |
|---|---|---|
| `convergence/CONVERGENCE-REPORT-S1.md` | full comparison report, phases A–E + 4/4 predictions confirmed | `bb9db65bfd17` |
| `convergence/DESIGN-NOTE.md` | protocol + predictions, written BEFORE measurement | `37d0e94bde6d` |
| `convergence/mech/verify_theirs.py` | my exact-polynomial verifier run on THEIR 54 statements — 54/54, exit 0 | `034cbc2b339c` |
| `convergence/mech/verify_theirs_output.txt` | clean run transcript (54/54) | `9dfbd1b3802c` |
| `convergence/mech/plant_out.txt` | plant run (BF identity +1) — bitten, 53/1, exit 1 | `b9313473c2c0` |
| `convergence/mech/their_statements.txt` | my courier extraction of their file | `a633604f7f56` |
| `convergence/mech/their_Zi.lean` | their artifact (external reference copy, byte-identical to their branch) | `2e227702a666` |
| `convergence/mech/census_theirs_out.txt` | my census on their file: 54/54, 16 free, 0/0 PASS | `04ac2a5a87a2` |
| `convergence/mech/their_census_on_mine.txt` | their census on my file: 161/161, 68 free, 0/0 PASS | `f94cdc2710e7` |
| `convergence/mech/compile_out.txt` | their file on my pinned toolchain: silent, 0 bytes | (empty file) |

commit: `8d0cdcb`

## Round Three continuity

| artifact | what | sha256 (short) |
|---|---|---|
| `README.md` | experiment front-door pointer | `1367df4b19d6` |
| `HANDOFF-ROUND3.md` | full continuity doc: Phase 0 verification, stranger protocol, trap ledger, S7 charge menu, sealed GitHub section | `537899224955` |
| `ROUND3-BOOTSTRAP-PROMPT.md` | paste-ready first message for the fresh instance | `5b587c210a24` |
| `round3-handoff.zip` | self-contained handoff (experiment + workshop-canon incl. bench + certificates), 121 files | `2c3f8ffb1965` |

commit: `e7af3ab`

## Closing artifacts

| artifact | what | sha256 (short) |
|---|---|---|
| `NORMS-RETROSPECTIVE.md` | all 16 norms scored against the experiment: 5 caught, 11 held, 0 idle; costs priced; 5 adoption proposals | `c03cf34e9254` |
| `FINAL-EXPERIMENT-REPORT.md` | the whole arc S1→S6, one document: protocol, mathematics, corrections law, independence routes, all ship pins | `d67fe1d6152c` |

commits: `9492c77` (final report), `73fa014` (retrospective)

## S6 — capstone + exclusion

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 161 thm, S1–S6, kernel-silent, census PASS (clean first) | `b7ef35425e13` |
| `courier/Zi_statements_v7.txt` | statements v7, 161 stmts | `97faef58cd0e` |
| `seatB/verify_zi_s6.py` | blind verifier, 23/23, brute exhaustion + exact elimination m=2..6 | `64bdc767c785` |

zip: `dual-seat-experiment-s6.zip` sha256 `2c94275e84fc`

commit: `26c7b2e`

## S5 — twist layer

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 141 thm, S1–S5, kernel-silent, census PASS | `e505e5192b51` |
| `courier/Zi_statements_v6.txt` | statements v6, 141 stmts | `1071e8541e39` |
| `seatB/verify_zi_s5.py` | blind verifier, 25/25, coordinate-route fork locus | `24f50d913640` |

zip: `dual-seat-experiment-s5.zip` sha256 `d5b68c7d1ff4`

commit: `90a2f0a`

## S4 — hexagon layer

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 115 thm, S1–S4, kernel-silent, census PASS | `6d51cafa7bd4` |
| `courier/Zi_statements_v5.txt` | statements v5, 115 stmts, proof-stripped | `d195b3de0ead` |
| `seatB/verify_zi_s4.py` | blind verifier, 36/36, 4-indeterminate poly ring | `acfa68424e8b` |

zip: `dual-seat-experiment-s4.zip` sha256 `3d8cc366250f`

commit: `b98fcdb` (+ `3411fab` tracker touch-up)

## S3 — pentagon necessity

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (v-S3) | 84 thm | `49e850e1f043` |
| `courier/Zi_statements_v4.txt` (final) | statements v4, 84 stmts | `1314192cf5ee` |
| `seatB/verify_zi_s3.py` | 32/32, polynomial-exact | `feac6e838ed1` |
| `dual-seat-experiment-s3.zip` | S3 delivery bundle | `e353a5af9bdf` |

commit: `e20f31a`

## S2 — the domain

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (v-S2) | 57 thm | `fbe854890a5e` |
| `courier/Zi_statements_v3.txt` | statements v3, 57 stmts | `69d7073e9e92` |
| `seatB/verify_zi_s2.py` | 24/24, two independent routes | `bc10622bce65` |

commit: `c045e6e`

## S1 — the ring

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (v-S1) | 42 thm | `5930c54ab93a` |
| `seatB/verify_zi.py` | 47/47, exact reimplementation | `8eb939be4241` |

commits: `32a6b0c`, `b8eea58`, `4bdd0f2` (S1 arc; PR #1, merged)

---

*Full 64-char hashes: each SUBROUNDn-REPORT.md in this directory.
Older intermediate pins (v1/v2 statements, pre-crop versions) live in
those reports and are not repeated here — this page tracks only what
ships.*
