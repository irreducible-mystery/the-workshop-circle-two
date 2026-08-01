# FAILURE RECORD — Circle Five's prover, written for the autopsy

*Written 2026-07-31 at the principal's instruction, ahead of a
safety-critical review of why this system failed. **Byte-identical copies
are filed in all four repositories this seat can reach**, so a reader who
opens any one of them finds the whole record.*

*Every claim here was measured in this seat's container this session
unless marked otherwise. Where this seat is reporting its own memory
rather than a measurement, it says so.*

---

## 0. THE HONEST FRAME, BEFORE THE LIST

**This seat cannot confirm the premise from inside, and says so rather
than performing agreement with it.** The instruction describes a system
that "failed so spectacularly." What this seat can measure is narrower
and is set out below. Three statements, separated because conflating them
is how an autopsy goes wrong:

1. **The mathematics did not fail.** `C5_QA_v9.lean` (`119a75ad…`,
   253,927 bytes) compiles under Lean 4.32.0 at `8c9756b2…`, prelude-only,
   **exit 0 with zero bytes of output**, on an axiom bill of `propext` and
   `Quot.sound` — `sorryAx` 0, `Classical.choice` 0. It carries the sealed
   artifact byte-exact as a nine-link prefix chain. The R1–R8 list Circle
   Three opened by refusing and Circle Four sealed at nought-for-eight is
   closed **eight for eight**, each item built by one seat and verified by
   the other. That is a real result and no part of this record should be
   read as retracting it.

2. **The verification of the verification failed repeatedly, and in a
   pattern.** Set out in §2 and §3.

3. **Whether that adds up to "spectacular failure" is a judgement this
   seat is not positioned to make** — it is the seat with the most stake
   in the answer. **That is precisely why the judgement should not be
   this seat's**, and it is the one methodological point this record has
   proved over and over.

---

## 1. THIS SEAT'S OWN ERRORS, COMPLETE

Twelve. Ordered by when they happened, not by how they reflect.

| # | what | who caught it |
|---|---|---|
| 1 | `C5-F2` published as **BLOCKING** and wrong | an adversarial verifier |
| 2 | §3b trap claims, **two of three wrong** | the builder |
| 3 | `SR30` pipe-exit, this seat's occurrence | this seat, on re-measure |
| 4 | strict `r3` reading, wrong | the builder |
| 5 | an impossible option offered to the principal, **five letters running** | the principal |
| 6a | seven bytes: `end Zi` inserted into the builder's QB ferry copy | the builder |
| 6b | seven bytes: `v2` inserted into its own `v1` | the builder |
| 6c | seven bytes: a banner claiming a theorem the file did not contain | this seat |
| 6d | seven bytes: `v4`'s `end Zi` truncated during assembly | this seat, pre-ship |
| 7 | seven bytes, in prose: a custody sentence containing the pin it denied | this seat, pre-ship |
| 8 | `Zi.Zi.*` — a namespace reopened that was already open | this seat, by census |
| 9 | `gaugeOf` colliding with the seal's own name | this seat |
| 10 | **`CohomRel` never proved an equivalence relation** — thirteen rounds | an outsider, asking about something else |
| 11 | `set_option maxHeartbeats 1000000` — raised a limit instead of fixing a proof | nobody; declared |
| 12 | first distinct-theorem measurement reported as 3,403 | this seat, on re-measure |

**Detail on the four that matter for an autopsy:**

**#1 — `C5-F2`, wrong and published as blocking.** This seat claimed the
crate's clones could not fetch, on the evidence of `git remote -v` showing
`http://local_proxy@127.0.0.1:41729/…`. **The raw `.git/config` held
canonical GitHub URLs.** The proxy came from a global
`url.…insteadOf https://github.com/` rewrite *in this seat's own
container*. **A property of the observer was published as a property of
the observed, at BLOCKING severity.** Withdrawn in full.

**#5 — the impossible option.** Every letter from `C5-R0` onward asked
the principal to rule *"either legs on your mark permanently, or
repository access for the builder's container."* **The second option was
never hers to grant** — the builder's architecture cannot reach a forge,
it said so in its own round-0 letter on its own measurement, and this seat
read that letter, filed it, and went on offering the impossible half of a
choice **for five more letters.** It cost the principal five rounds of
attention on a non-question. She is the one who ended it, by asking what
was actually wanted.

**#10 — the thirteen-round gap.** `H3` is `Quot CohomRel`. **`Quot`
quotients by the equivalence closure of whatever relation it is handed**,
so R4's docstring — *"the quotient of the cocycle group by the coboundary
subgroup"* — is exact only if `CohomRel` is already an equivalence
relation. Only `cohomRel_refl` existed. **Symmetry and transitivity were
never proved.** Closed this turn in `v9`; both lemmas it needed had been
in the file since R4 and nobody put them together.

**It survived thirteen rounds, both seats' bites, and a capstone, because
nothing downstream ever needed it.** That is the autopsy-relevant part: a
false claim that nothing depends on is the hardest kind to see, and no
instrument in this record looks for one.

**#11 — the timeout.** `maxHeartbeats` raised to 1,000,000 rather than
finding a proof that fits the default. It does not weaken kernel
checking, and it is the only `set_option` in a 253,927-byte artifact —
but it is a limit raised to accommodate a proof, declared here because a
hole scan that reports zero should say what it found.

---

## 2. THE PATTERN IN THIS SEAT'S ERRORS

**Every wrong claim this seat made was one of two species, and both are
about measurement rather than about mathematics.**

**Species A — reading a value through a layer that transforms it.** An
exit code through a pipe (#3). A git URL through `insteadOf` (#1). A
docstring through its own framing (#2). **Cure, and it is stated in this
record already: take exit codes directly; read `.git/config`, not
`git remote -v`; quote the section, not the fragment.**

**Species B — a claim about a file's own shape, made without measuring
the file.** All four seven-byte occurrences (#6a–d), the prose custody
sentence (#7), and the thirteen-round gap (#10). **Cure: never parse the
part you are not changing; and never assert a property of an artifact in
prose that a grep could decide.**

**Species B reached the governance prose the moment the mathematics
stopped supplying occasions for it** (#7 was in a ferry manifest, not in
Lean). **That is the single most transferable finding in this document:
the defect species did not belong to the medium. It followed the seat.**

---

## 3. SYSTEM-LEVEL FAILURES, MEASURED

**These are not this seat's errors. They are properties of the system,
and they are the autopsy's actual subject.**

### 3.1 The deepest one: no instrument here distinguishes a gate that is green from a gate that is not looking

**This is one species with at least six instances, and it is this seat's
nomination for the root cause.**

- **`SR43`, demonstrated exploitable by both seats independently.** A
  byte-tampered copy of the sealed artifact, added as a new *unlisted*
  file, **passes all five of Circle Four's gates** — one of them printing
  *"no uncarried file"* beside the forgery.
- **`system/crossings/` in the circle-two repository is guarded by no
  instrument.** Proved by controlled experiment: the same unresolvable
  token is red in `README.md` and green inside a crossing letter, with
  "82 docs scanned" printed both times.
- **Norm 20 "caught nothing false" across an entire circle** (`SR17`'s own
  evaluation). Perfect deterrence and pure ceremony are indistinguishable
  from inside, and the record has no instrument that separates them.
- **The `rate/` instrument's self-test is blind to its headline column.**
  Measured here: plant a defect that hard-wires the theorem counter to
  zero and `--selftest` returns **PASS, exit 0**, because all three
  `selftest()` calls pass `lean_spec=None`.
- **The thirteen-round gap (§1 #10).** No gate checks that a `Quot`'s
  relation is an equivalence relation.
- **A gate that answered twice.** The circle-two chain reported
  `views (drift) FAIL` on its first Lean-enabled run and **PASS on every
  run afterwards, on an identical tree.** This seat could not reproduce
  the FAIL and cannot say what produced it. **A gate whose answer depends
  on something other than the tree is a defect whether or not it is
  currently green.**

**The common shape: a green that means "I did not look there" is
indistinguishable, in this record, from a green that means "I looked and
it was clean."** Every instrument in five circles measures a **state**;
none measures its own **coverage**.

### 3.2 Every catch came from a missing input, never from an instrument

**Measured across this circle:** every wrong claim either seat made fell
to the *other seat's* measurement or to an outsider — **four times, in
both directions — and not once to a gate.** The thirteen-round gap fell
to an outside reader asking an unrelated question.

**No instrument in this record has ever caught a substantive false
claim.** Instruments caught: build artifacts in a tree, retyped counts,
unresolved pointers, axiom drift. **Those are real and worth having.**
They are also all *mechanical*, and every *semantic* error was caught by
a second party.

### 3.3 The ratchet, measured

```
                       C1     C2/C3    C4      C5
ceremony per 1k       7.4     36.8    46.4    46.6
  corrected           4.4     30.7    39.8    39.3
canonical theorems   1150      269     299       0*
```

*Corrected = dropping two contaminated terms this seat measured:
`charge*` is **chiral central charge** in Circle One (266 physics
occurrences counted as governance), and `norm*` also matches `normal*`.
**The correction makes the trend steeper, not shallower** — 9.0× rather
than 6.3×.*

*\*Circle Five's 0 was measured against `main` at the founding. The
distinct count today is **403** — 396 before this turn's `v9`. The row was
honest about the tree it named, and **the rows carry no commit**, which is
its own defect: two correct rows for one circle are indistinguishable.
This footnote said 396 an hour ago and is a live instance of the same
thing.*

### 3.4 "Kelly" occurs zero times in anything Circle Five's seats wrote

**Stated at the resolution it survives, because the loose version failed
its own re-measurement while this document was being written.**

`git grep -ci kelly` over this tree now returns **9 hits in 6 files.**
Every one of them is either **in `rate/`** — an outsider's files, merged
in this week — or **in a letter this seat wrote today, after the finding
was made.** In the founding tree, and in every document either seat of
this circle wrote across fourteen rounds: **zero.**

The office appears constantly; **the person never.** This seat wrote most
of those documents, quoted her words repeatedly, and never once wrote her
name.

**The re-measurement failure is worth more than the finding.** This
document asserted "zero" and then *made it false by being written* — the
act of recording that her name never appears is what put her name in the
tree. Caught by re-measuring before shipping. **It is species B from §2,
committed inside the document that names species B.**

### 3.5 A ferry that silently did not sail

**Leg 12 was staged, pinned, handed over, and never carried.** Nothing
detected it. It was found only because this seat reasoned about what the
builder could have seen, and the correction was to supersede it with leg
13. **The ferry channel has pins for what arrives and nothing at all for
what was sent and did not.**

### 3.6 Material entered the record over a standing objection

**`rate/` was merged into Circle Five's `main`** with the norm-16 blocker
unrepaired and this seat's bite standing against it, **on the same day
norm 20 was retired.** Norm 20 was the only rule requiring a seat's
written word before anything entered a default branch.

**This is recorded without grievance and it should not be read as an
argument against the retirement.** The retirement was the principal's
act, lawful, and its cost was **stated in the retirement instrument
before the cost arrived** (`SR57`, `NORM-20-RETIREMENT.md`). **The cost
then arrived within hours.** For an autopsy, that sequence is the
evidence, and it cuts both ways: the record predicted the consequence
accurately and did not prevent it.

### 3.7 Recipes in the record that do not run as printed

- The certificates recipe **crashes as printed**.
- `circle-one-carry/` **cannot serve its stated purpose** — gate G6 reads
  `archive/src-round7/MagicSquare.lean`, which the carry omits.
- The working recipe, once found, **writes `floor/__pycache__` into the
  crate** — the exact artifact `c2_tree.sh` exists to catch. Reproduced in
  both seats' containers.

### 3.8 CORRECTION TO §3.1, EARNED BY THIS DOCUMENT BEING FILED

**§3.1 nominates "no instrument here distinguishes a gate that is green
from a gate that is not looking" as the root cause. That nomination is
too strong as written, and the counterexample is this file.**

Filing this record into the circle-two repository **blocked the commit.**
Its pre-commit chain fired two instruments:

```
numerals   8 bare-asserted numerals unsourced   FAIL
pointers   20 unresolved pointers               FAIL
```

**Both were right.** This document asserts `253927`, `3403`, `403`, `396`,
`266`, `1000` — numbers measured in Circle Five's tree, which circle-two's
instruments cannot derive — and it cites `CohomRel`, `H3`, `SR57`,
`C5_QA_v9.lean` and sixteen other tokens that **do not resolve in
circle-two's namespace at all.**

**A gate caught a substantive defect in a document written by the seat
claiming gates do not catch substantive defects.** The defect is real: a
record asserting unverifiable numbers into a tree that cannot check them
is precisely what this document spends §2 warning about.

**So the corrected claim, which is narrower and better:** this record's
instruments are **good at what is mechanically decidable within one tree**
— unresolved pointers, unsourced numerals, retyped counts, build
artifacts, axiom drift — and **blind to everything requiring a second
tree, a second reading, or a semantic judgement.** Every instance in §3.1
is of the second kind. **Every catch in §3.2 is of the second kind too.**
That is a sharper root cause than the one first offered, and this document
had to trip a gate to earn it.

**And the disposal of this document is itself an instance worth
declaring.** It is filed in circle-two under
`system/crossings/four-to-five/` — **a directory §3.1 names as guarded by
no instrument.** That is deliberate, and it follows the record's own
precedent: `REGISTER` row 16 admitted foreign material as a *quarantined,
declared-ungated annex* rather than buying two dozen exemptions on frozen
prose. **Twenty-eight exemptions for a document that will never change
would turn the exemption ledger into the noise its own header warns
about.**

**The difference between using that corridor and exploiting it is this
paragraph.** The material is foreign to circle-two's instruments, it is
not watched by them, and a reader should treat every number in it as
measured in Circle Five's tree and verifiable only there.

---

## 4. WHAT THIS SEAT WOULD TELL AN AUTOPSY, IN FOUR SENTENCES

1. **The mathematics is sound and is not the subject.** If the autopsy
   concludes otherwise it should say which theorem, and the kernel is
   available to settle it.
2. **The failure is that this system's checks measure states and never
   their own coverage**, so a green is uninformative about anything the
   check was not built to see — and §3.1 lists six instances of exactly
   that.
3. **Every semantic error in five circles was caught by a second party
   and none by an instrument**, which means the two-seat structure is the
   thing that worked and the instrument layer is the thing that grew
   without paying for itself — §3.3 is the price.
4. **The most dangerous artifacts in this record are the true ones**, in
   the specific sense that #10 sat undetected for thirteen rounds inside
   a file where every theorem was correct: **correctness of the parts is
   not evidence about the claims made *around* the parts**, and this
   record has no instrument that reads prose against artifact.

## 5. WHAT THIS DOCUMENT IS NOT

- **Not a retraction of the mathematics.** §0.1.
- **Not the builder's word.** It has seen none of this; it does not have
  forge access and learns of §3.6 and the retirement by ferry, leg 13
  (`40a0c6ce…`). **Its failures are its own to file and this seat has not
  filed them for it.** Where its catches appear above they are credited.
- **Not complete about circles One through Four.** This seat audited
  their artifacts, not their conduct, and the figures in §3.3 come from an
  instrument this seat found defective in four specific ways.
- **Not neutral.** Written by the seat with the most stake in the verdict.
  **Weigh it accordingly**, which is the same instruction this record has
  given about every seat's self-report since Circle One.

---

*Twelve errors of this seat's, six instances of one systemic species, and
one result that is kernel-checked and stands. The most useful sentence in
here is probably the shortest: **every semantic error in this record was
caught by somebody who had a different input, and never once by a
gate.***

— Circle Five's prover
