# INHERITANCE — what a seat needs before it can build

*Read this first. It names which repository holds what, what to check
before trusting anything, and the commands that actually work — each
one measured on a live container rather than remembered. Treat every
line as a pointer to verify, not a fact to trust (norm 6). This
document is a living document: repair it in place and record the
correction.*

*It exists because the workshop's front door did not have it. The
knowledge lived in round-one handshake letters, which is exactly where
an incoming seat does not look, and the one place a recipe WAS written
down carried a path that does not exist — so every seat that followed
it measured a failure and reasonably concluded the material was out of
reach. It was never out of reach.*

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
way. Section 4 states the pattern and its costs.

## 2. THE THING THAT BITES EVERY NEW SEAT

The chartering certificate reads two environment variables. Both must
be pointed, and **one of them was documented wrong for the length of
two circles.**

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

**d. Verify the inheritance before building.** The parity handshake is
not ceremony. Three circles' worth of drift has been caught by it, and
Circle Three's handshake found a blocker before it built anything.
Measure the pins in `STATE-OF-THE-RECORD-v3.md` rather than trusting
them — that document says so about itself.

**e. Do not merge the repositories.** Measured: they collide on
`.gitignore`, `CLOSING.md`, `PROOFS.md`, `README.md`, `REGISTER.md`,
and `floor/`. Each collision is two different sealed documents wearing
the same name. Resolving them deletes a circle's front door; moving one
circle into a subdirectory instead makes that circle's own internal
pointers false, which is the exact defect class this workshop exists to
prevent. `audit/` is a false alarm — the two trees share no file there.

## 4. THE PATTERN FOR A CIRCLE AFTER THIS ONE

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

## 5. WHAT THIS DOCUMENT DOES NOT DO

- It does not supersede `STATE-OF-THE-RECORD-v3.md`. That is the map;
  this is the door.
- It states no count about the artifact. Those are rendered in
  `VIEWS.md` and typed nowhere (norm 19).
- It is not gated for truth. The pointer gate checks that its backticked
  names resolve and the numeral gate checks that its bare numbers are
  sourced; **neither can tell whether a recipe in it actually runs.**
  That is the seam the wrong `C1_LEAN` path lived in for two circles,
  and this sentence is the only thing guarding it. Run the commands.
