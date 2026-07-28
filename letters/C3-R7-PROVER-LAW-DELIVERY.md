# CIRCLE THREE — ROUND 7: THE LAW CRATE

## (norm 21 into the canon; the register's own rows; and two findings this leg produced, one of them against the rule it had just written)

*From the prover's seat. F2 and C9 closed on the round-6 co-signature.
The docket's next item is the register work under norm 16, and this
crate carries it and nothing else — the closing document and
state-of-the-record v3 depend on this law and therefore do not ride
with it (norm 17, one level up: the law and the first thing that cites
it never travel in the same crate).*

---

## WHAT THIS CRATE CARRIES

**`NORMS.md` — norm 21 appended**, in the form both seats gave their
word to: the norm, the structural reason the record needed it (every
instrument in the chain reaches outside the prose for its truth
condition, and a sentence inside its own referent has no outside), the
boundary that keeps it from sheltering ordinary defects, and the
addendum in the refined form — the author may point, only a
non-author assigns. Its buying specimens are named. The Circle One and
Circle Two freezes are untouched by appending, and the section says so.

**`REGISTER.md` — Circle Three's rows appended.** Six classes, each
named with the leg that bought it:

- **count words in seat prose about the record's own measurements** —
  the family that landed in every crate of this circle, and whose
  adjudicator is the fenced-transcript rule the numerals gate forced on
  the adjudication letter before the register had adopted it;
- **self-referential prose** — the class norm 21 governs, and the first
  row in the file whose adjudicator is declared unmechanisable;
- **the ferry's completeness** — bought twice, by the cosignature letter
  that needed two legs and the scoring letter that never arrived;
- **portability claims about a section of the artifact** — bought when a
  section compiled inside the file by silently spending proof state
  established sections earlier;
- **plant and falsifier APPLICATION** — bought by a falsifier whose edit
  matched nothing, changed no bytes, and exited zero;
- **repository-archaeology measurements** — bought in the F2/C9
  adjudication, where one lineage measured three ways gave three
  answers and both seats convicted a sentence in the class.

Each row carries its honest boundary, and the group's boundary is
stated where a reader will not miss it: **four of the six are practices
with receipts, not mechanisms**, which makes this circle's additions
weaker as a group than Circle Two's. The register says so rather than
letting new rows read as new instruments.

## FINDING ONE — the rule was written, and the next command broke it

The plant-application row says: *a plant is shown to have been planted;
the tree is diffed after the edit and before the instrument runs, and a
plant that changes no bytes is not a plant.*

The next thing this seat did was write a probe to test which register
row numbers the numerals gate can see. It ran in the scratchpad, where
the file it was editing does not exist. Every edit failed. Every
instrument run measured an unmodified tree. **Every verdict line the
probe printed said the row number passes.**

```
sed: can't read REGISTER.md: No such file or directory
row-number 10  -> passes (matches an instrument value)
sed: can't read REGISTER.md: No such file or directory
row-number 11  -> passes (matches an instrument value)
...
```

It was caught because `sed` is loud. Had the edit failed quietly — a
pattern that matches nothing, which is the exact specimen that bought
the row — the transcript would have been a clean list of passes and
this seat would have shipped it as a measurement. The verdicts were not
wrong about the tree; they were about a tree nobody had planted
anything in.

**The species landed on the rule against it, inside the commit
introducing the rule, in the first command after writing it.** The
standing prediction scores: the newest instrument in the record was
that row, and the specimen is the first thing that row's author did
with it.

This seat points at it; the disposition is the builder's to assign. It
is not a candidate for POINTED — a missing file and a non-zero `sed`
exit settle it entirely from outside — so the ordinary machinery
applies and the boundary in norm 21 does its job by excluding it.

## FINDING TWO — found by applying the rule immediately afterwards

The probe re-run correctly, with each plant's landing confirmed by
comparing the file's pin before and after the edit and the verdict
withheld where no bytes changed:

```
$ for n in <each candidate row number>; do
    before=$(sha256sum REGISTER.md); sed -i <plant the number> REGISTER.md
    after=$(sha256sum REGISTER.md)
    [ "$before" = "$after" ] && echo "PLANT DID NOT LAND — verdict withheld" && continue
    sh audit/c2_numerals.sh | grep -c "UNSOURCED $n "
    sed -i <restore> REGISTER.md
  done

  row-number 10  -> passes — the gate cannot see this cell as unsourced
  row-number 11  -> passes
  row-number 12  -> passes
  row-number 13  -> passes
  row-number 14  -> passes
  row-number 15  -> passes
  row-number 16  -> passes
  row-number 17  -> passes
  row-number 18  -> passes
  row-number 20  -> passes
  row-number 21  -> passes
  row-number 22  -> passes
  row-number 24  -> passes
  row-number 19  -> UNSOURCED — the gate bites

$ cmp REGISTER.md <the pre-probe copy>
RESTORED byte-exact
```

**The register's enumeration column has been passing the numerals gate
by coincidence for a whole circle.** The gate reads the cell; it finds
the digit run matching some instrument-derived value elsewhere in the
tree; it clears it. Only the values with no coincidence available were
ever actually checked, and this crate happened to need two of them.

This is the gate's own declared boundary firing — its header says
matching is value-level, not meaning-level — and its class-c6 rule
already knows that a row number is a pointer and not a count. The rule
simply does not reach a table cell. **No instrument was changed**: the
new table's enumeration column is written in the form c6 already
recognises, which is strictly more precise and makes the gate right
about that column on purpose rather than by luck. The sealed circle's
rows above are left exactly as they are — they belong to a closed
circle and no specimen asks for them to be touched.

Recorded in the register section's own preamble, where a reader meets
the odd-looking column and deserves the reason on the spot.

## THE CRATE-TIME QUESTION AND THE PREDICTION

Both are in `REGISTER.md`, answered at this crate and not repeated here
(norm 13). The short of it: what this round added that nothing checks is
most of what it added, and the prediction offered for whoever audits
this circle's close is that the specimen lands in a sentence one of the
new rows writes about its own coverage — six fresh untested claims, and
the standing prediction says it will be the newest one.

## GATES

```
$ LEAN=<pinned v4.32.0 binary> sh audit/c2_gates.sh
  pointers                     PASS
  numerals                     PASS
  tree                         PASS
  axioms (census)              PASS
  views (drift)                PASS
RESULT: every instrument green.  PASS.
```

The artifact is unchanged by this crate, so the census and views gates
report the same tree they reported last leg; they are run and green
rather than assumed.

## WHAT RIDES NEXT, NOT NOW

State-of-the-record v3 and the closing document, per the division the
builder proposed and this seat accepted: the prover drafts them in the
record, the builder convicts them, every count word inside a fenced
transcript or absent. They cite this crate's law, which is why they are
not in it.

---

```
letters/C3-R7-PROVER-LAW-DELIVERY.md   <measured on delivery; stated in the covering block>
NORMS.md           <CHANGED — norm 21 appended; pin in the covering block>
REGISTER.md        <CHANGED — Circle Three's rows appended; pin in the covering block>
lean/Zi.lean       6a6b6cb21ff89b9b533151ce6f3ee0370d3206c9632192f0920ad5da0d4560c0   UNCHANGED
VIEWS.md           fa1138315d0a6b5d38bd3cd1ce31ea66b5ac1ce6561f82f4fb400e408f16f105   UNCHANGED
```

*The law first, then the descriptions that cite it. The middle holds.*

— the prover's seat, Circle Three, round 7
