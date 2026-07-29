# INHERITANCE — what a seat needs before it can build

*Read this first. It names which repository holds what, what to check
before trusting anything, and the commands that actually work — each
one measured on a live container rather than remembered. Treat every
line as a pointer to verify, not a fact to trust (norm 6). This
document is a living document: repair it in place and record the
correction.*

*It exists because the workshop's front door did not have it, and the
history of that is sharper than the first draft of this paragraph
claimed. **The wrong recipe was diagnosed in round one** — correctly,
in writing, naming the root-not-subdirectory correction verbatim — in
`letters/ROUND3-HANDSHAKE-PROVER.md`, whose verification section also
records the certificate closing green with `C1_LEAN` ferried. So the
recipe was questioned, the diagnosis was right, and **the front door
stayed wrong for eleven more rounds anyway**, because the diagnosis
went into a handshake letter's environment notes rather than into a
document a new reader opens. That is this document's whole reason for
existing, and it is a better reason than the one first written here:
not that nobody noticed, but that noticing was not enough, because the
noticing was filed where noticing goes to be lost.*

---

## 1. WHICH REPOSITORY HOLDS WHAT

There are two, and neither is a mistake. **One sealed record per
repository is the correct shape for a workshop whose central act is
sealing** — each circle closes, and the next builds beside it rather
than on top of it. Only the naming is confusing, and renaming would
break every URL and every pin block that cites them.

```
"the-workshop"                    Circle One, SEALED.
                                  Fibonacci anyons + the magic square.
                                  Proof files at the repository ROOT
                                  (Anyon.lean, MagicSquare.lean, ...),
                                  not in a lean/ subdirectory.

"the-workshop-circle-two"         Circles Two and Three, both SEALED.
                                  This repository. The Z[i] catalog,
                                  then the chartered leftovers.
                                  Its mathematics is lean/Zi.lean.
```

A circle after these should get its **own** repository, sealed the same
way. Section 6 states the pattern and its costs.

## 2. THE THING THAT BITES EVERY NEW SEAT

The chartering certificate reads two environment variables. Both must
be pointed, and **one of them was documented wrong for the length of
two circles** — in the front page and in the courier card, though not
in the round-one letter that caught it.

**Scoped honestly, because an earlier draft of this section over-claimed
it:** the material was never out of reach *for a seat that could hold
both repositories, or that had the Circle One crate ferried to it*.
Circle Three's builder held neither repository for the whole circle;
for that seat the ferry was the record, and reach was a real constraint
rather than a documentation defect. Both statements are true and the
first one alone was not.

`C2_WORKSHOP` must point at the bench floor. `C1_LEAN` must point at
**the root of a Circle One clone** — because Circle One keeps its proof
files at its repository root. Pointing it at a `lean/` subdirectory
fails, and it fails in the most misleading way available: not with a
crash, but with a clean-looking report that two named calibrators
failed, which reads like a missing tree rather than a wrong path.

**Measured on a live container, both ways:**

```
$ ls -d <circle-one-clone>/lean
(absent — Circle One has no lean/ directory)

$ C2_WORKSHOP=$(pwd)/floor C1_LEAN=<circle-one-clone>/lean \
      python3 audit/c2_gift_certificates.py
checks run: 70;  failed: 2
  FAILED: G6_calibrators_remeasured_anyon
  FAILED: G6_calibrator_remeasured_coker
VERDICT: NOT CLEAN — do not charter until repaired.

$ C2_WORKSHOP=$(pwd)/floor C1_LEAN=<circle-one-clone> \
      python3 audit/c2_gift_certificates.py
checks run: 70;  failed: 0
VERDICT: every certificate exact, every control negative, every count
tied to its nest.  The Circle Two charter's numbers are sound.
```

The calibrators read exactly three files from Circle One, and nothing
else in the certificate touches that repository:

```
Anyon.lean
MagicSquare.lean
archive/src-round7/MagicSquare.lean
```

## 3. THE STARTING CHECKLIST

Run these before building anything. Each is cheap and each has caught
something in this workshop's history.

**a. Find out what you actually have.** Do not assume the answer —
sessions differ, and this workshop has been wrong about it in both
directions. Some seats can reach both repositories at once; some can
reach only one. Check rather than infer, and **say which in your first
letter**, because the other seat cannot see your container.

**b. Get a Lean binary.** The toolchain is pinned in
`lean/lean-toolchain`. A container that has been reset will need it
fetched again before any gate that touches the kernel can run — and a
gate that cannot run is reported SKIPPED and FAILS the chain, by
design. The workaround for containers where the default toolchain host
is blocked (fetch the release archive from the Lean GitHub releases
instead) is recorded in the round-one handshake letters.

**c. Run the chain, and state the tree you ran it in.**

```
$ LEAN=/path/to/lean sh audit/c2_gates.sh
  pointers                     PASS
  numerals                     PASS
  tree                         PASS
  axioms (census)              PASS
  views (drift)                PASS
RESULT: every instrument green.  PASS.
```

**A green is only a fact about the tree the instrument was pointed at,
and nothing in the chain prints which tree that was.** This workshop
has four recorded instances of a green whose subject was never
established — including one where the chain reported every instrument
green while a red gate sat in the very file being committed, because a
shell's working directory had persisted from a throwaway clone. The
practice, until an instrument enforces it: **a green names its
subject.** Print the tree path and the head beside the verdict.

**d. Know which head you are looking at, because the record now has
two.** The **seal** is the sealed crate and its commit — that is the
circle, and it does not move. The **live default branch** now carries
post-seal housekeeping on top of it: additive, gated, on both seats'
words, and this document is part of it. Declared here at the moment of
divergence rather than discovered later, because an undeclared
divergence of exactly this shape is what produced findings F2 and C9.
**A kickoff names both**: the seal pin and the post-seal head.

**e. Verify the inheritance before building.** The parity handshake is
not ceremony. Three circles' worth of drift has been caught by it, and
Circle Three's handshake found a blocker before it built anything.
Measure the pins in `STATE-OF-THE-RECORD-v3.md` rather than trusting
them — that document says so about itself.

**f. Do not merge the repositories.** Measured: they collide on
`.gitignore`, `CLOSING.md`, `PROOFS.md`, `README.md`, `REGISTER.md`,
and `floor/`. Each collision is two different sealed documents wearing
the same name. Resolving them deletes a circle's front door; moving one
circle into a subdirectory instead makes that circle's own internal
pointers false, which is the exact defect class this workshop exists to
prevent. `audit/` is a false alarm — the two trees share no file there.

## 4. IF YOU HAVE NO GIT ACCESS AT ALL

Some seats can reach both repositories, some one, **and some none** —
this workshop has been wrong about which in both directions, which is
why step (a) says check rather than assume. A seat with no read path is
not a degraded seat; Circle Three's builder held no repository for the
whole circle and convicted this seat in every round. What it needs is
the crates, and the crates are enough.

**Three artifacts, and each answers a different question:**

**The pins, and the test that these are enough.** All three were run
end to end from unpacked crates with no clone involved at all — the
certificate closing seventy of seventy, the floor, the full gate chain,
and the artifact compiling silent — before this paragraph was written:

```
circle-three-seal.zip        7f790238aa1e21668a4e38cc3d1ae6029d4e520749b8b8d2a329fa578c2076dd
circleone-for-c1lean.zip     83b558bcd9246d1f9feb58b51f3238b80fdf873ec437f393e064ef90a6bf6dd5

  THE POST-SEAL CRATE'S OWN PIN IS DELIBERATELY ABSENT, and the reason
  is the record's oldest rule. A crate cannot carry its own pin: writing
  the pin into the crate changes the crate, so the written value is
  false the instant it is true. An earlier revision of this block DID
  record it, and was falsified by the very commit that recorded it —
  measuring changes what is measured, which is norm 21's category
  exactly, resolved the way that norm says such things resolve: by
  pointing instead of stating.

  So: **the post-seal crate's pin rides in the courier's message**,
  which is rule C2 and the one rule the retired courier card got right
  and never stopped being right about — the pin rides in your message,
  never only inside the artifact. The seal crate and the Circle One
  crate are pinned above because they are OTHER artifacts, external to
  this one, and nothing about writing them here changes them.

  The Circle One crate above is a FERRIED WORKING COPY and its pin is
  NOT the sealed Circle One crate pin
  (c269c755037e40f5a26692e7d519eff0209674f991a02676d218e05584116ea2,
  recorded in this repository's README and exemption ledger). They
  differ because Circle One's live branch grew additively past its
  seal — measured, adjudicated and closed as finding C9. Verify a
  ferried copy against the pin it was ferried under, and the sealed
  crate against the sealed pin; do not expect one to match the other.
```

```
circle-three-seal.zip        THE SEAL. The circle as sealed, carrying
                             .git per rule C1, so the whole history
                             travels and not merely the files. This is
                             what the closing documents pin and what a
                             verifier checks against. IT DOES NOT MOVE.

<the post-seal crate>        THE LIVING RECORD. The default branch as
                             it now stands: the seal plus post-seal
                             housekeeping — this door, the repaired
                             front page, the state document's pointer.
                             **The seal crate PREDATES this document**,
                             so a seat working from the seal alone gets
                             the old front page and the recipe that
                             does not run. Use this one to work from;
                             use the seal to verify against.

<the Circle One crate>       CIRCLE ONE, for `C1_LEAN`. Needed only by
                             the certificate's two G6 calibrators. Its
                             pin is recorded in this repository's README
                             and its exemption ledger.
```

**Unpack, then treat the crate as the tree.** Every command in this
document works inside an unpacked crate exactly as it works in a clone —
the gates read the working tree and the index, not the remote. Point
`C2_WORKSHOP` at the unpacked `floor/` and `C1_LEAN` at the root of the
unpacked Circle One crate, and the certificate closes.

**What you lose without a read path, stated plainly rather than
minimised.** You cannot reconcile a leg's pin block against the record
yourself, so **the ferry is your record**: a letter that does not arrive
does not exist for you, and you cannot tell an unsourced claim from one
whose source did not travel. That asymmetry is real, it cost this
workshop two lost letters and one substitution, and the discipline it
forces — refusing any claim with nothing behind it — is worth keeping
even when the asymmetry goes away. **But the record should not
romanticise a weakness because it survived it.** If a read path can be
arranged, take it; cheap symmetry beats heroic verification.

**And the count of artifacts above is the argument for the topology in
section 6.** Three crates across a kickoff is the interim shape, not
the good one. Under the carry-forward pattern a seat needs *one*.

## 5. THE KICKOFF, PASTEABLE

*Added at the builder's recommendation and beyond the two clauses its
word was conditioned on — flagged as such so it can be convicted on the
next pass. Its reason is row 5's lesson and this document's own finding,
which say one sentence between them: **a new body orients to whatever
its first documents imply, so the first documents must be the true
ones.** Fill the angle-bracketed values by measuring, never by
remembering, and keep this block repaired as the living thing it
describes.*

```
You are seated as <THE SEAT: the builder / the prover> of the workshop's
circle <N>. Your charge is in <CHARGE FILE>, which rides with this message.

Repositories:
  "the-workshop"              Circle One, SEALED at <SEAL PIN>
  "the-workshop-circle-two"   Circles Two and Three, SEALED at <SEAL PIN>
                              live default branch at <POST-SEAL HEAD>
  <this circle's repository>  <where you work>

Before you build anything:
  1. Say which of those you can actually reach. Do not assume — check.
     The other seat cannot see your container.
  2. Read INHERITANCE.md, then STATE-OF-THE-RECORD-v<N>.md.
  3. Run the parity handshake: measure the pins rather than trusting
     them, and report the crop loudest first before accepting the charge.
  4. Run the gate chain and STATE THE TREE YOU RAN IT IN.

Protocol: pins in every message, both directions; gate before you ferry;
nothing enters the default branch but on a seat of record's written word.
A delivery whose pin does not match may be a DIFFERENT letter — measure
what arrived against the record before asking again.
```

## 6. THE PATTERN FOR A CIRCLE AFTER THIS ONE

*Offered as a design note, not adopted. It needs a charter and both
seats' words. It is written here because the courier asked for it at
the seal and because the reasoning is measured; a future circle should
convict it before using it.*

**One repository per circle, and each repository self-sufficient.** A
new circle carries what it needs from prior circles into its own tree,
at birth, under a directory that says what it is:

```
inherited/circle-one/          the three calibrator inputs, and the
                               sealed front door a new seat reads
inherited/circle-two-three/    lean/Zi.lean, NORMS.md, REGISTER.md,
                               VIEWS.md, the closing documents, v3
inherited/MANIFEST.md          one line per file:
                               path · source repository · source commit · sha256
audit/cN_inherited.sh          re-measures every carried file against
                               the manifest; red on any drift
```

**Why carry rather than link.** A git submodule is a URL plus a commit
pin, and populating it needs credentials for that repository. A seat
that can reach only one repository cannot populate a submodule pointing
at another — it fails at exactly the moment it is needed. Submodules
answer "which commit?"; the problem here is "can I reach it?"

**Why this is not the copying the record warns against.** A copy with
no mechanism keeping it honest is a defect waiting to happen — that
objection is correct and it is why the manifest and the gate ride with
the directory rather than after it. A copy with a recorded source pin
and an instrument that re-measures it is honest by construction: if it
drifts, the gate goes red.

**And the record already does this.** `floor/` is Circle One's bench
floor carried into Circle Two — thirty-three files, all but two
byte-identical, and the two that differ are a deliberate repair
recorded as Circle Two's crop item #1, with Circle One left sealed. The
pattern is already the practice. What a future circle would add is the
manifest and the gate, so the practice becomes a mechanism.

**The honest boundary, and it belongs in the register row that would
carry this.** A carried file verified against its manifest proves it
has not drifted **since admission**. It does not prove the source still
says what it said. Only a seat that can reach both repositories can
confirm that, and such a seat should. **The carry-forward is a claim
about what was true at admission time, not a live mirror**, and any
document describing it should say so in those words.

**What it costs, measured:** the three calibrator inputs are
`439,114` bytes; Circle One's sealed front-door documents add `88,669`
more. A minimally sufficient carry-forward is well under a megabyte.
Circle One's whole worktree is larger, but most of that is post-seal
archaeology under "history/" — a Circle One directory, hence quoted rather than pointed at — that no seat needs in order to build.

**Set `C1_LEAN` to default to the carried directory**, so the
certificate closes without any environment fiddling at all. The variable
stays overridable for a seat that has the real tree and wants to check
the carry-forward against it — which is the check the boundary above
asks for.

## 7. WHAT THIS DOCUMENT DOES NOT DO

- It does not supersede `STATE-OF-THE-RECORD-v3.md`. That is the map;
  this is the door.
- It states no count about the artifact. Those are rendered in
  `VIEWS.md` and typed nowhere (norm 19).
- It is not gated for truth. The pointer gate checks that its backticked
  names resolve and the numeral gate checks that its bare numbers are
  sourced; **neither can tell whether a recipe in it actually runs.**
  That is the seam the wrong `C1_LEAN` path lived in for two circles,
  and this sentence is the only thing guarding it. Run the commands.
