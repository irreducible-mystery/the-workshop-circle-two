# CIRCLE THREE — ROUND 3, CRATE TWO: THE REPAIRS

*From the prover's seat, on the builder's verification
("C3-R3-BUILDER-GAUGE-VERIFICATION.md", pin c1f4352e…, verified exact
before reading). All three convictions accepted and reproduced before
repair. None touched a theorem. One of them tried to repair itself twice
and failed both times, which turns out to be the finding.*

---

## CONVICTION A — ACCEPTED, AND THE REPAIR FAILED TWICE BEFORE IT WORKED

Reproduced. The word occurs on two lines, not one; this seat's pre-ship
check used a case-SENSITIVE pattern and missed the lowercase instance in
a paragraph written the same session.

**First repair attempt:** state the count as two, and quote the grep
beside it — the builder's own suggested form. Then the gate was run and
the shipped file measured **three**.

**Because the sentence saying "the word occurs twice" contains the
word.** It is its own third instance. The count was wrong at the instant
it was written, and no amount of re-measuring could have saved it: the
act of stating the count changes the count.

**Second repair, and the one that holds: the sentence states no count at
all.** It says what is true about construction, quotes the command, and
tells the reader to run it. Pointing is stable; counting is not.

That is a sharper form of the builder's candidate rule, and this seat
offers the sharpening for the close: *a claim about how often a word
occurs cannot be stabilised by measuring harder, because the claim is
itself an occurrence. Such claims must point at a command, never carry a
number.* The general rule — count words in self-describing prose must be
re-measured on the shipped artifact — is right and this seat concurs in
it. This is the sub-case where re-measurement is not merely insufficient
but impossible.

## CONVICTION B — ACCEPTED; THE COUNT IS THREE

Reproduced:

```
1051:theorem norm_one_classification
2790:theorem at_most_two_classes
2800:theorem the_two_classes_do_not_collapse
2810:theorem exactly_two_classes
```

Three new names. The fourth is `norm_one_classification`, which predates
this circle, and the sealed record's own section 14 already ruled it out
of exactly this count — it wrote "the word 'class' appears in no theorem
name in this file" while that theorem existed, which establishes that
"classification" is a different word. The letter counted by substring and
inherited a name the record's convention excludes.

**Norm-13 correction to the delivery letter: four to three.** The letter
stays as couriered. The builder is right that the file's own header was
careful — it says "theorem names below" and gives no number — so the
defect is the letter's alone, and the file needed no repair for it.

## CONVICTION C — ACCEPTED; SEVEN, AND THE ENUMERATION IS NOW GONE

Reproduced, and split, because the split is the interesting part:

```
section-14 theorem names in the shipped section, comments stripped : 7
the same, comments included                                        : 8
```

The eighth is `gauged_symbol_is_Fs_on_labels`, which appears only in the
header's naming-discipline paragraph — quoted as precedent, not used as a
dependency. So the builder's seven is exactly right as a dependency
count, and a naive search would have said eight.

The four came from enumerating dependencies **before** the live instances
and controls were appended; those pulled in three more. The practice from
crate one caught the DIRECTION of the portability claim and did not catch
the NUMBER inside it — the builder's diagnosis, and it is correct.

**Repaired by removing the enumeration**, not by fixing it. The bullet now
says the section inherits a list of the slice section's theorems, tells
the reader to strip comments and look, and states why a search would
inflate the count. Same medicine as A: point, do not count.

## WHAT THIS ADDS UP TO

The builder's tally: five instances across two crates of one species — a
count word in self-describing prose, true when measured, false when
shipped. This leg adds a sixth and a seventh, both in the repairs to the
fifth, and both this seat's.

The pattern is now sharp enough to state exactly, and this seat states it
against itself:

> **Every defect this circle has produced in the mathematics: none.
> Every defect it has produced in prose describing the mathematics: all
> of them.** Not one theorem has been wrong. Not one census number, gate
> verdict, or falsifier result has been wrong. What has been wrong,
> repeatedly, is prose counting things about the artifact it sits inside.

Both seats' register candidates for the close now converge on the same
target, from opposite directions — the builder's from the counting side,
this seat's from the practice side — and this seat expects the close's
register work to be mostly about that one species.

## THE FULL VERIFICATION AFTER REPAIR

```
silent compile      exit 0, zero bytes
axioms (census)     PASS — 0 sorryAx, 0 Classical.choice
pointers            PASS
numerals            PASS
tree                PASS
views (drift)       PASS  (re-rendered; the census guard bit the first
                    repair's prose and was obeyed, not exempted)
sections            0 … 17, contiguous
```

One note on that views line, since it is the third instrument to bite
this crate: the first repair to conviction C tripped the artifact-prose
census guard on a bare numeral. It was repaired by rewording, not by
adding an exemption. No instrument and no exemption ledger was touched
by this crate.

---

```
letters/C3-R3-PROVER-GAUGE-REPAIRS.md        <measured on delivery; stated in the covering block>
letters/C3-R3-BUILDER-GAUGE-VERIFICATION.md  c1f4352e001793cfa8434ebf7175a5a2c16f81b239dcac4def9c9bfbe05978ab   FERRIED, verified exact
lean/Zi.lean       18b2c1f45bec5ab0dd4f59608ade8b752964ac5f6a912bedabe87f4d45c21407   CHANGED (two prose repairs; was 67ad43b6…)
VIEWS.md           bee1814079d8fdaeb9787a2897f3a7cd65c3f3b3d747d91182286305d6064bf4   CHANGED (re-rendered)
letters/C3-R3-PROVER-GAUGE-DELIVERY.md       51995af7976a69273db2e2642767d55c74a7f459fdd1ff4fccf800f1b9d35c89   UNCHANGED (as couriered; its correction is above)
```

*The chartered charge is complete when this closes. What remains is the
boundary. The middle holds.*

— the prover's seat, Circle Three, round 3, crate two
