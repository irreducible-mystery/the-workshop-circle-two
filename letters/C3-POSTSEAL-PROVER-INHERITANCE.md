# CIRCLE THREE — POST-SEAL: THE INHERITANCE CRATE

## (a housekeeping leg on a sealed record, offered for the builder's word — and the loudest thing in it is that the front door's own verify recipe never ran)

*From the prover's seat, on the courier's request after the seal. The
courier asked why new instances cannot reach the material they need,
and whether the two repositories should be merged. **Both questions had
measured answers that contradicted their premises**, and the second
answer is the more important one: they should not be merged, and the
reason is not taste.*

*This is a post-seal housekeeping leg. It touches no sealed artifact
and no letter. It repairs a living front door, adds one new living
document, and adds one pointer to the state document. It needs the
builder's word under norm 20 before it enters the default branch, and
it is offered rather than taken.*

---

## LOUDEST FIRST — THE PUBLISHED `C1_LEAN` RECIPE DOES NOT RUN

`README.md` has carried, since Circle Two, this instruction for the
chartering certificate:

> `C2_WORKSHOP=$(pwd)/floor C1_LEAN=<circle-one>/lean python3 audit/c2_gift_certificates.py` → 70/70, exit 0.

**Circle One has no `lean/` directory.** Its proof files sit at the
repository root. Measured on a live container with a real Circle One
clone attached, running the published recipe verbatim:

```
$ ls -d <circle-one-clone>/lean
(absent)

$ C2_WORKSHOP=$(pwd)/floor C1_LEAN=<circle-one-clone>/lean python3 audit/c2_gift_certificates.py
checks run: 70;  failed: 2
  FAILED: G6_calibrators_remeasured_anyon
  FAILED: G6_calibrator_remeasured_coker

$ C2_WORKSHOP=$(pwd)/floor C1_LEAN=<circle-one-clone> python3 audit/c2_gift_certificates.py
checks run: 70;  failed: 0
VERDICT: every certificate exact, every control negative, every count
tied to its nest.  The Circle Two charter's numbers are sound.
```

**This is the whole of the "seats cannot reach Circle One" problem, and
it was never an access problem.** It was a wrong path in the document
whose job is to tell a new seat how to verify. Every seat that followed
the recipe got two named calibrator failures — which reads exactly like
a missing tree, not like a wrong argument — and reasonably concluded the
material was out of reach. It was in reach the whole time. **The
certificate closes 70 of 70 and this seat has now seen it do so**, which
no leg of this circle managed, having inherited the wrong recipe and
never questioned it.

Two things about this specimen are worth the builder's attention:

**It lived in the one seam no instrument covers.** The pointer gate
checks that a backticked token resolves *in this tree*; the path names a
directory in another repository, so there was nothing for it to resolve
against and nothing to fire on. The numeral gate saw no numeral. **A
cross-repository reference is unguarded by construction** — which is
Circle Two's law running one level out: mechanism guards what it names,
and a mechanism scoped to one tree cannot name anything in another.

**And it is the species this circle spent eleven rounds convicting**, in
its purest form yet: a sentence standing next to a correct instrument,
describing how to run it, wrong. The certificate was never wrong. The
recipe beside it was.

## WHAT THE CRATE CARRIES

**`INHERITANCE.md` — new, and it is the document that was missing.**
Which repository holds what; the corrected recipe with both transcripts;
the three files the calibrators actually read; a starting checklist; and
the topology design note the courier asked for. Every command in it was
run on a live container before it was written down. Its closing section
states plainly that **no gate in this tree can tell whether a recipe in
it actually runs** — the seam this crate's own specimen lived in, named
where the next reader will meet it.

**`README.md` — repaired, with the corrections recorded in the file.**
It was frozen mid-Circle-Two. Each item measured against the sealed tree
before it was touched: the title and status said Circle Two was live
with round two open; the certificate row carried the recipe above; "the
four gates" predated the views gate and the chain; the Lean row still
described the artifact as the ring layer alone; the Circle One lineage
line carried the description the F2/C9 adjudication corrected. **And one
item the builder should weigh separately: the status carried an ESTIMATE
of the finished size — a plan, in the cumulative record, which norm 18
forbids.** It had been sitting there since before norm 18 was bought.

**`STATE-OF-THE-RECORD-v3.md` — one paragraph added**, pointing at the
new door and stating the corrected variable. The environment paragraph
it joins was not wrong; it was incomplete, and its incompleteness is why
the knowledge lived nowhere a new seat would look.

**Nothing sealed is touched.** `lean/Zi.lean`, `VIEWS.md`, both closing
documents, `NORMS.md`, `REGISTER.md` and every letter are unchanged, and
their pins are in the block below.

## THE TOPOLOGY QUESTION, ANSWERED WITH MEASUREMENTS

The courier asked whether to merge the two repositories. **This seat
recommends against it, and would have said the opposite before
measuring.**

```
$ comm -12 <(circle-one top level) <(this repo top level)
.gitignore   CLOSING.md   PROOFS.md   README.md   REGISTER.md   audit   floor
```

`audit/` is a false alarm — ninety-six files against twelve, sharing no
name. `floor/` shares all thirty-three, of which thirty-one are
byte-identical and two differ by Circle Two's crop item #1, deliberately
and on the record. But `CLOSING.md`, `PROOFS.md`, `README.md` and
`REGISTER.md` are each **two different sealed documents wearing one
name**, and a merge forces one of two moves: resolve them, which deletes
a circle's front door, or move a circle into a subdirectory, which makes
that circle's own internal pointers false. The second is the defect class
this workshop exists to prevent, performed on a sealed record.

**Submodules were considered and are worse for this workshop's actual
constraint.** A submodule is a URL plus a commit pin, and populating it
needs credentials for that repository. A seat that can reach only one
repository cannot populate a submodule pointing at another; it fails
precisely where it would be needed. Submodules answer *which commit*.
The problem here is *can I reach it*.

**What is offered instead**, as a design note in `INHERITANCE.md` §4 and
explicitly NOT adopted: one repository per circle, each self-sufficient,
carrying what it needs from prior circles under an "inherited/"
directory with a manifest of source pins and a gate that re-measures
them. This seat argued against plain copying earlier in the same
conversation and stands by that argument — **which is exactly why the
manifest and the gate ride with the directory rather than after it.** A
copy with a recorded pin and an instrument watching it is honest by
construction.

And the strongest thing in its favour is not the reasoning: **the record
already does this.** `floor/` is Circle One's bench floor carried
forward, with its one divergence recorded. The pattern is the practice
already. A future circle would only be adding the manifest and the gate,
so a practice becomes a mechanism — which is the shape of every good
thing in this record's history.

The honest boundary rides with it: a carried file verified against its
manifest proves it has not drifted **since admission**, not that the
source still says what it said. That is a claim about a moment, and any
row carrying it should say so in those words.

## WHAT THIS SEAT DID NOT DO

- **Did not touch `CLOSING.md`.** Its sentence about the certificate
  closing sixty-eight is dated, correctly conditioned, and TRUE of the
  container it was written on. It is history, not staleness, and
  repairing it would be falsifying a record rather than correcting one.
- Did not merge, prune, rename, or restructure anything.
- Did not adopt the topology. It is a design note awaiting a charter.
- Did not push to the default branch. This wants the builder's word.

---

```
$ tree=/home/user/the-workshop-circle-two  head=<the crate's commit>
$ LEAN=<pinned v4.32.0 binary> sh audit/c2_gates.sh
  pointers                     PASS
  numerals                     PASS
  tree                         PASS
  axioms (census)              PASS
  views (drift)                PASS
RESULT: every instrument green.  PASS.
```

*(The pointer gate bit this crate twice while it was being written:
once on a Circle One directory typed as a local path, once on the name
of a directory this letter PROPOSES and which therefore does not exist
yet. Both quoted rather than pointed at. That makes four bites in four
consecutive letters, all one species — **a mark that says "this
resolves" placed on something that does not** — and the four subjects
are worth listing because they map the seam exactly: a name being
denied, an elided pin, a path in another repository, and a thing not yet
built. The gate is right every time and can only ever see the last kind
by accident.)*

```
INHERITANCE.md              <NEW; pin in the covering block>
README.md                   <REPAIRED; pin in the covering block>
STATE-OF-THE-RECORD-v3.md   <one paragraph added; pin in the covering block>
letters/C3-POSTSEAL-PROVER-INHERITANCE.md   <measured on delivery>
lean/Zi.lean       6a6b6cb21ff89b9b533151ce6f3ee0370d3206c9632192f0920ad5da0d4560c0   UNCHANGED
VIEWS.md           fa1138315d0a6b5d38bd3cd1ce31ea66b5ac1ce6561f82f4fb400e408f16f105   UNCHANGED
CLOSING-C3.md      5f1278d3d1ad9bbbf0536ea38af2ab86f68d4d80fe3bfe6df8d5fff0b833ecb9   UNCHANGED
NORMS.md           27250658e21caa1828c99bafcb56af6b665aa8f7b3805787fe75cf3ce0f91c9c   UNCHANGED
REGISTER.md        ae758563b97fa230255d21da4b34d6ddf0ec815d7e4780cc9a3598b5ba4ac2da   UNCHANGED
```

*A sealed record's door can be repaired without opening the record. The
middle holds.*

— the prover's seat, Circle Three, post-seal
