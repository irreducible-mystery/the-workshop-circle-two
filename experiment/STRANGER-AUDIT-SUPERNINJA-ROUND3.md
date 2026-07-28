# STRANGER-AUDIT — SuperNinja (meta-auditor, REGISTER row 7) on branch `claude/read-and-execute-b4408j`

*A true-stranger pass (REGISTER row 18 / norm 18) on Fable 5's pushed branch,
run from a cold isolated clone, kernel-first, prose-last. Read-only: nothing
built, nothing merged, no PR, no touch to the L3/continuity structure. This is
the third body row 18 asks for and the S7 corrections letter (item 1) says was
missing.*

Auditor: SuperNinja, meta-auditor / continuity seat.
Subject: `origin/claude/read-and-execute-b4408j`, HEAD `c3d30bc`.
Box: the same 3.8 GiB sandbox that OOM-killed the Expert run of the old charge.

---

## The one-line verdict

**The mathematics is verified. I am the stranger row 18 required, and I
independently reproduce every load-bearing claim by a route with no step in
common with either seat. The row-2 *ruling* (item 5) is prose — I concur with
it as written, but it remains a judgement, not a measurement, and a later
stranger could overturn the judgement without touching the mathematics.**

The branch is sound and is, on the mathematics, the cleanest S7 artifact this
record has produced. It is NOT mergeable as-is on process grounds (norm 20 +
the branch was born from a self-prompted run of a defective charge) — that is
Kelly's ruling to make, not mine; §7 lays out the options.

---

## Phase 0 — inheritance, verified mechanically (before reading anything)

| commit | what | experiment kernel pin | thm |
|---|---|---|---|
| merge-base `9f05245` | shared history w/ main | `b7ef35425e13` | 161 |
| `404920f` | courier repair | `b7ef35425e13` (byte-identical) | 161 |
| `2b38bc8` | the S7a lemma | `848282f2e3a2` | 195 |
| `c3d30bc` | pin recording | `848282f2e3a2` | 195 |

The kernel is an **addition** (161 → 195, +34 theorems), not a rewrite: the
courier-repair commit leaves the kernel byte-identical to the merge-base, and
the lemma commit only adds. No frozen source was edited on this branch. **PASS.**

## Phase 1 — statements read cold (before prose)

The 34 new theorems, read as statements only, are honest:

- explicit witnesses (`sliceGauge F`, `f = mul(mul(F 1 1 1)(F 1 0 0))(F 0 0 1)`)
  — read off F, not searched for;
- nests tie (`s7_nest_cocycles_32`, `..._coboundaries_16`, `..._classes_2`,
  16+16=32), with object-tie back to the cochain (`cochainOf_injective`,
  `cochainOf_is_cocycle`);
- two negative controls (`control_A_not_a_cocycle_and_never_normalized`,
  `control_B_identity_gauge_fails`);
- three live instances (anti-vacuity);
- **no theorem name says U(1)** — the honest label is "over the units of Z[i]"
  throughout, and U(1) appears only in a docstring saying it is NOT this
  theorem and NOT in reach (norm 6). **PASS.**

## Phase 2 — my own instruments, from the cold clone

| check | route | result |
|---|---|---|
| kernel compiles | `lean Zi.lean`, my box | **SILENT** — exit 0, 0 bytes stdout+stderr, **16–19 s** (norm 10) |
| axiom census | `#print axioms` on headline + slice + nest + control A | **CLEAN** — `[propext, Quot.sound]` or *no axioms*; **zero** sorryAx / Classical.choice / ofReduceBool (norm 2) |
| S7c purity gate | `s7c_statements_purity.sh` | **PASS** — 794 lines, 0 prose-leak |
| S7c transcription gate | `s7c_transcription.sh` (tag `v8 (S1..S7)`) | **PASS** — T1 re-extract BYTE-IDENTICAL (norm 12), T2 no truncation |
| **seat-B verifier** | `verify_zi_s7.py`, direct exhaustion of 65536 cochains + 256 gauges | **43/43, exit 0** — **32 / 16 / 2 reproduced from the orbit partition alone**, parametrization then checked exact as a set equality |
| plant harness (slice) | `plant_s7_slice.sh` | **PASS** — 6 plants bitten (3 kernel, 2 verifier, 1 label→U1), both restores byte-identical |
| plant harness (courier)| `plant_s7_courier.sh` | **PASS** — 5 plants bitten / 5 restores; R1 & R2 repairs shown load-bearing |

**On the box that killed Expert.** The exhaustive 65536-cochain route that
OOM'd inside Lean's `decide` (the defective old-charge route) runs fine in
Python as seat B, and seat P's *structural* route compiles in 16–19 s. So the
two routes are not only independent, they are independent in the precise way
that matters here: seat B took the one route seat P could not, and neither
route is the route the bad charge prescribed. A shared arithmetic error would
have to survive exhaustion AND a structural parametrization with no common step.

## Phase 3 — the norm-12 "discrepancy" I flagged pre-audit: RESOLVED, not a defect

Before running the gate I re-extracted with a bare `v8` tag and saw the header
banner differ (`v8 (S1..S7)` shipped vs `v8` mine). That was **my** tag choice.
The transcription gate carries the tag as a parameter (`TAG=${3:-"v8 (S1..S7)"}`),
and with the correct tag T1 re-extracts **byte-identical**. The shipped file is
the extractor's genuine output. **No finding.**

## Phase 4 — the prose, read last

Fable 5's `CORRECTIONS-LETTER-S7.md` is loudest-first (norm 4) and leads with
the caveat that **this crate does not meet the record's own standard for
"verified"** because row 18 needs a stranger and one body held both seats.
That is exactly right, and it is the reason this pass exists. Its self-findings,
each independently checked here:

1. **CAVEAT (one body, both seats).** Correct. Answered by this pass: I am the
   missing stranger, and I concur on the mathematics.
2. **FINDING — bench sentence overstates its instrument** (§ `symmetric_statistics.py` /
   the U(1) `size=1` real-parameter search). This is the SAME species as the
   §10 finding — a row-8 sentence where every noun resolves and the sentence is
   still not true of its own instrument. Correctly held out of this crate under
   norm 17 (repair to a doc the ruling depends on) and routed as a bench crop.
3. **FINDING — purity gate hung on its own expected-red** (unbounded self-recursion
   in the FAIL branch). Repaired to scan-once-into-tempfile; my
   `plant_s7_courier.sh` run confirms the repair is load-bearing (revert R1 →
   purity red). **Confirmed fixed.**
4. **FINDING — a pin resolving by machine-local reflog state** (`ecd63e1`, a
   dangling pre-amend merge object). **Independently confirmed:** `git cat-file
   -e ecd63e1` → ABSENT in my fresh clone. Correctly routed to
   `audit/c2_pointers_exempt.txt` with its reason rather than editing the frozen
   letter. A genuine norm-19 / reproducibility catch, correctly handled.
5. **RULING — REGISTER row 2 narrows, does not close.** I **concur, as written.**
   The certificate's own text names *U(1)*; U(1) is not representable in a
   zero-import kernel over `Int`; an exclusion whose written scope names a group
   cannot be discharged by a theorem about a smaller group, however much better
   certified. Row 2 moves from "not certified at all" to "certified over Z[i]
   units; the continuous form remains." Fable 5 records the defensible
   counter-reading (that the excluded step was the *generic* one) as a judgement
   a stranger could overturn — and I am flagging, as the stranger, that I did
   NOT overturn it: I read the same way, for the same reason (the only written
   scope the exclusion has says U(1)). **This concurrence is itself prose from a
   single further body; it strengthens the ruling from "one body's judgement" to
   "two independent bodies' concurring judgement," but it is still not a
   measurement.** Route any future challenge to L1-adjudication, not to re-audit.
6. **RECORD — 43/43, independent route.** Reproduced here, cold. **PASS.**

---

## What this pass does and does not settle

- **Settles (measurement):** the kernel compiles silent and axiom-clean; the
  slice lemma, the 32/16/2 nests, both controls, and the honest label are all
  reproduced by an independent second route on an independent body (mine). The
  two courier gates pass; the courier repair is load-bearing; the plants bite
  both directions. Findings 3 and 4 are correctly repaired/routed.
- **Does not settle (judgement):** the row-2 ruling and the two bench/§10 prose
  crops are prose. My concurrence adds a second independent body to the row-2
  judgement but does not convert it to a measurement. These remain L2 items for
  the seats of record + Kelly's sanction.

## Mergeability — NOT my call, but the facts Kelly needs

The branch is mathematically sound and process-clean *within itself*. But:
- norm 20: nothing enters main but on a seat's written word — this document is
  that word on the *mathematics*, not authorization to merge;
- the branch was born from a self-prompted run of the **defective old-§4
  charge** (the one that steered the route and OOM'd Expert). The clean result
  was reached *despite* the bad charge, by Fable 5 restructuring away from the
  prescribed route. That is a provenance fact Kelly asked to weigh.

## Options for the branch's fate (for Kelly's ruling — I build none of these)

- **A — Adopt the mathematics, re-home the provenance.** Cherry-pick the lemma
  onto a fresh branch issued from the *fixed-§4* charge, so the record shows the
  result reached under a clean charge. Costs a re-run; buys a clean lineage.
- **B — Accept the branch as-is via a seat's written word (this doc + Kelly's
  sanction), with the provenance recorded as a divergence note.** Cheapest;
  puts the "born from a bad charge" fact permanently in the record next to the
  result.
- **C — Hold/isolate like PR #6** pending the L3 structure that would let a
  system-level steward rule on charge-provenance. Slowest; safest if the
  continuity structure is close.
- **D — Retire Expert as *prover* (keep it as seat/auditor);** independent of
  A–C, this is the standing-capability finding the two runs produced.

Whatever the branch's fate, the row-2 ruling and the two prose crops should be
carried to the seats of record regardless — they are true findings that outlive
the merge question.

---

*Pins verified this pass: experiment kernel `848282f2e3a2` (195 thm); merge-base
& courier-repair kernel `b7ef35425e13` (161 thm); statements v8 re-extracts
byte-identical under tag `v8 (S1..S7)`. Dangling `ecd63e1` confirmed absent in
fresh clone. All checks read-only.*
