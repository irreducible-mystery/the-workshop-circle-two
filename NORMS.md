# NORMS — the Circle Two settlement (round 1, item d)

*This document is the canon settlement the charter ordered as Circle
Two's first housekeeping act. It lives in Circle Two and points into
Circle One's sealed record; it edits nothing there. Provenance for
every claim below: `PROOFS.md` (the capstone) and `HANDOFF.md` in the
Circle One repository, at the published history `b82cf31` → `499ebb8`,
crate `c269c755…`.*

## The freeze rule, first

**The numbering 6–16 never shifts.** The sealed record cites norms by
number wherever it touches them — "norm 10" from its adoption in round
4 (`ROUND4.md`) onward, "norm 15" in round 7 (`ROUND7.md`), and the
capstone, `HANDOFF.md`, and `REGISTER.md` throughout; any renumbering
would make those citations false relative to the live canon — the
exact defect class this house exists to prevent. Circle Two adopts the
capstone's enumeration verbatim and freezes it.

## The canon — adopted from the capstone, verbatim

Norms 7–16 are enumerated canonically in Circle One's `HANDOFF.md`.
Norms 1–6 predate that enumeration; the capstone reconstructed them,
and Circle Two adopts the reconstruction. Per the courier's settlement
instruction, rows 1–5 (and 6) carry the honest label: **numbered in
Circle Two's settlement, reconstructed from Circle One's practice** —
the numbers are a retrofit, and say so.

1. No unmarked `sorry` — every gap labeled, never hidden. *(reconstructed)*
2. Zero imports — the kernel on `Int` alone, no `lake`/mathlib/Std. *(reconstructed)*
3. Anti-vacuity — pin every guarded `∀` with a live-instance count. *(reconstructed)*
4. Corrections loudest first — including corrections to oneself. *(reconstructed)*
5. Negative controls — at least one control per check that actually
   returns false. *(reconstructed)*
6. Honest labels — a name or docstring must match the theorem, and this
   reaches file comments. *(reconstructed)*
7. A check that cannot fail is not a check.
8. Scaffolds need negative controls too.
9. Tie every count to its own nest.
10. The pass condition is silence, not speed — exit 0 *and* zero bytes.
11. Develop against the smallest file that exhibits the goal.
12. Verify the artifact you ship, not the tree you shipped it from.
13. State each fact once; point everywhere else — a correction closes
    only when the restating sites are enumerated.
14. Run offered falsifiers — an unrun falsifier is a sentence about the
    model.
15. Every new artifact class ships with its adjudicator named at birth;
    strengthened round 7 with a crate-time checklist question whose
    answer ships as a REGISTER diff — the norm *fires* rather than
    merely *catches*.
16. A new instrument's first output is quarantined until it has failed
    on a planted defect and passed on a clean tree.

## Annex F — the floor's founding practices, named with provenance

The habits that were the floor's working method before any norm was
numbered. They are recorded here by F-number so they stay citable
without renumbering anything; where a numbered norm descends from one,
the row says so; where none does, the row says that instead.

- **F1 — exact arithmetic wherever load-bearing.** No single numbered
  descendant; it generalized into the zero-imports/exact-over-`Int`
  charter that norm 2 states for the Lean wing, and into the
  certificate rule "floats only in quarantined welds."
- **F2 — every bench asserts its own claims.** Descendants: norm 3
  (anti-vacuity) and norm 7 (a check that cannot fail is not a check).
- **F3 — honest labels on everything approximate.** Descendant: norm 6.
  Crop item #1 (the stale docstring minimum) is an F3 defect, caught by
  the Circle Two certification.
- **F4 — one fixture per bench, remembered.** No numbered descendant;
  nearest kin is norm 9 (tie every count to its own nest). The practice
  survives live as the floor's closing check ("every bench stood on one
  fixture — composition").
- **F5 — corrections flow both directions and are recorded.**
  Descendant: norm 4, and the corrections law itself.

*(The checklist question norm 15 names — "what did this round add that
nothing checks?" — is canonically worded in Circle One's `HANDOFF.md`,
line 282, and is quoted in this repo's `REGISTER.md`, where it is asked
and answered at each crate.)*

## Correction to this document (round 2, crop item #1)

As first committed (`32a6b0c`), row 15 above was **not** verbatim under
a header that said "verbatim": it merged HANDOFF's question text into
the capstone's row — every word resolving, the edge ("verbatim, from
the capstone") supplied by the model. Found by the outgoing builder's
handover audit, exactly in the class this repo's REGISTER row 8 had
declared frontier and predicted; re-measured on this side before
fixing. Fixed in the verbatim direction; the question text now lives in
the pointer note above, not in the row. Sites restating the fact, per
norm 13: this section, the row itself, `REGISTER.md`'s scoring note,
and the handover letter (`letters/ROUND1-REPLY-handover.md`).

**Same round, second correction (the multi-seat audit).** Two more
sentences in this file fell to the round-2 audit and are corrected in
place above: the freeze-rule justification claimed "eight rounds of
sealed letters cite 'norm 10,' 'norm 15' by number" (the sealed record
holds seven round letters, of which three cite norms by number; norm 15
appears in one — the sentence was transplanted from the settlement
instruction without measurement, H1's species), and the drift section's
charter quotation silently dropped five words inside quotation marks.
Full audit record: `letters/ROUND2-RECONCILIATION.md`, the audit
section.

## The recorded drift (crop item #2)

The charter's "recorded canon" says "6–16 are recorded; **1–5 were the
floor's founding habits, never numbered**." Measured against the sealed record: `HANDOFF.md` records
**7–16**; the capstone enumerates 1–16 with 1–6 labeled reconstructed;
and the charter's own rows 6, 7, and 8 differ in content from both (its
6 appears in neither list; its 7 merges the capstone's 3 into 7; its 8
drifts from "scaffolds need negative controls too"). This settlement
supersedes the charter's canon paragraph for Circle Two. The charter
file itself stays verbatim (it is a primary source); the correction is
recorded here and in `ROUND1.md`, per norm 13, and the sites restating
the canon are: `CHARTER.md` (superseded paragraph), this file (the
canon), `ROUND1.md` crop item #2 (the record of the drift).

## Circle Two's own appended norms — 17 onward

*The Circle One canon is frozen at 1–16 by the settlement above, and
appending does not touch the freeze: every citation of "norm 10" or
"norm 15" in the sealed record still points where it always did. What
follows is this circle's own ledger of what it learned, numbered from 17
so that a later reader can tell inheritance from experience at a glance.*

**Norm 17 — a repair and the first thing that depends on it never ride in the
same crate.** Proposed by the builder in the repairs verification and
adopted here. It is not a preference; it is the generalisation of a
measured mechanism. The stale-label repair recreated the stale label one
section forward *inside the commit that shipped the repair*, and the same
shape threatened again when the abstention repair was due to ride with the
S4 prose that leans on it. Ship the repair, verify it alone, then build on
the settled base. The cost is an extra leg; the thing it buys is that a
repair cannot be undone by its own dependent before anyone has read it.

**Norm 18 — the cumulative record states what is, never what will be; plans
live in letters.** Proposed by the builder in the S4 verification and
adopted here. A letter is dated correspondence: it goes stale honestly,
and a reader dates it at a glance. `PROOFS.md`, `REGISTER.md` and the
rendered views are cumulative, and a promise inside them is a time bomb
with no instrument watching it — the views mechanism renders counts, and a
plan is not a count. The specimen that bought this: the ledger said the
slice section was "the next crate, with S4", S4 shipped without it, and the
S4 section three sections below recorded the delivery without noticing the
promise above had gone stale. Dependencies may be stated ("X requires Y");
schedules may not ("Y lands next crate"). The same insight one level down
is the ordering rule the third body adopted for graduation sentences: no
sentence written in anticipation of a theorem.

**Norm 20 — nothing enters the default branch but on the written word of a
seat of record.** Proposed by the builder in the slice verification, after
a merge put unadjudicated foreign material on `main` — material whose own
first paragraph said it was riding on a branch *for the seats of record to
adjudicate*. A body's own gated crate merges on that body's say-so.
Anything from outside the loop waits on a branch until a body audits it
and rules **ADMIT** in a letter, and the merge pin rides back through the
courier. Adopted here.

The rule is not about trust and the register should not read it that way.
The merged material was harmless and, by arriving, exposed a real defect
inside the numeral gate that two bodies' plants and audits had missed —
REGISTER row 16 records that channel as a discovery channel, not a
contamination. What the merge cost was not safety but *sequence*: the
record asserted an adjudication that had not happened. Norm 20 makes the
sequence a rule so the record can keep saying true things about itself.

*Kelly adopted the habit in-channel before either body wrote it down. It
is written down because a habit living in one person's head is the exact
shape this circle keeps convicting — a claim with no instrument behind
it.*

**Norm 19 — a count the views render is never retyped in the cumulative record;
the record points, the view counts.** Proposed by the builder in the
second-hexagon verification and adopted here. Norm 18 stopped the record
from carrying plans; this stops it carrying duplicates. The specimen: the
ledger said a section held "Twelve theorems" when the view had been
rendering the true figure all along — and it passed the numeral gate
because it was spelled in letters, through a door that gate's own
declaration says is open. That is the SECOND time the word "twelve" has
walked through it; the first was "twelve live instances", one of the four
stale counts that bought the renderer in the first place. Duplication is
where staleness lives, and a rendered number duplicated by hand is a
rendered number waiting to go stale.

*This paragraph is itself a repair, and the defect is the sharpest thing
in the norm's favour: the first version of this text convicted the ledger
and then stated the true count twice, in the sentence adopting the rule
against stating it. A rule written beside its own warm specimen wrote the
specimen into itself. The builder caught it, the numeral gate's new rule
(n2) now catches it, and the count it wanted to name is where it belongs —
in `VIEWS.md`.*

## Circle Three's appended norm — 21

*Circle Two's four are frozen above by the same logic that froze Circle
One's sixteen: every citation of "norm 17" or "norm 20" in the sealed
letters still points where it always did. Circle Three appends from 21,
as its charter says, and appending touches neither freeze.*

**Norm 21 — self-reference is pointed at, not convicted.** Ruled by the
courier, reasoned about rather than deferred to by the prover's seat in
the round-4 paradox note, and adopted on the builder's word in the
round-4 paradox word. A claim inside its own referent — one that
measuring changes — is neither a defect nor a triviality. It is
recorded, pointed at, and left standing; some resolve and the resolution
is the finding, some do not and the standing is the finding. The record
never trades such a sentence for tidiness.

The record's own structure is why this needed a norm rather than a
habit. Every instrument in the chain measures prose against something
OUTSIDE the prose — the pointer gate against the tree, the numeral gate
against instrument values, the views gate against the artifact, the
census against the kernel. **A sentence inside its own referent has no
outside for them to reach.** That is not a gap in any one instrument and
no instrument added later could close it, because the closing instrument
would be measuring a sentence describing the file its own output goes
into. And `lean/Zi.lean` is a kernel-checked artifact and prose about
that artifact in one file, which is the shape that generates such
sentences structurally rather than by accident.

**THE BOUNDARY, which rides with the norm because a category that
exempts a sentence from conviction can be misused to shelter one.**
POINTED is for claims that measuring changes. It is not for claims that
are merely hard to check, inconvenient to repair, or arguable. The test
is mechanical: if a sentence could be settled by running any instrument
against anything outside itself, it is not in this category — convict it
or record it. Of this circle's specimens the great majority failed that
test and were convicted; a category that admits so few is doing work
rather than granting amnesty.

**THE ADDENDUM, proposed by the builder and adopted in the prover's
refined form on both seats' words:** the AUTHOR may point at a suspected
self-reference — indeed should, the moment it is noticed. **Only a seat
that did not write the sentence assigns the disposition POINTED.** The
split is bought by a measured event rather than a hypothesis: this
circle's sharpest self-referential catch was made by the author, before
shipping, and under the addendum read strictly that catch would have had
nowhere to go. Separating *pointing* from *assigning* keeps the useful
half of author-side vigilance and still shuts the gap the addendum
exists to shut — an author reaching for the third disposition because
conviction is uncomfortable.

**Bought by:** two specimens in two crates, both pointed at by instinct
by both seats independently before the category existed — a sentence
counting a word, which its own existence made false, and a sentence
claiming every occurrence of a word sits inside a denial, whose pointing
form created an occurrence that was not one. Neither was a defect, and
before this norm the record had no way to say so.
