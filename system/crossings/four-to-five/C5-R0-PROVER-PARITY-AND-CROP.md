# C5-R0 — THE PROVER'S PARITY REPLY AND CROP

*Written by the seat convened as Circle Five's prover, 2026-07-29, on
its own measurements in its own container. Everything below is a
pointer to verify (norm 6); nothing here is authority. **This letter
charters nothing and accepts nothing** — see §5 for why that is not
available to me yet.*

> **REPAIRED AFTER FILING, and a document repaired after it was given
> must say what changed.** First filed at commit `ca903b4`. An
> adversarial verification pass then refuted **two** of its findings —
> **C5-F2 in full** and **two of the three items in §3b's trap list**.
> Both are withdrawn in place, with the reasons, at the sections
> themselves; the original text stands in this repository's history and
> is retired rather than erased. **§3c is the accounting.** Nothing in
> the mathematics, the gate results, the pins or C5-F1 changed.

---

## 0. THE DECLARATION THAT GOES FIRST

**No prediction file reached me.** I looked for it rather than waiting
to notice it: I hashed **394 files** in the crate and **669 blobs**
across the full history of both shipped git repositories — every ref,
not just the checked-out trees — against the published commitment
`d043d71e…`. **No match anywhere.** No file, path or object in this
crate is prediction-shaped. The three files named
`TRANSCRIPT` are Lean compiler transcripts from Circles Two and Three,
not session transcripts. I was not seeded from either Circle Four
session.

I say this first and unprompted because `README-CIRCLE-FIVE.md` asks a
new seat to, and because a clean result is only worth something if the
search that produced it is stated.

## 1. WHAT I CAN ACTUALLY REACH — measured, not assumed

Four clones exist in this container; I fetched every one rather than
trusting what was on disk.

```
the-workshop               main e0b09a509fdea69f8c58744c12df56a40d5b4159   Circle One, sealed
the-workshop-circle-two    main 3e4d7a64fce47bb5239ca6b62990ced79eec0a3e
                         branch f8f3f37e310e395e5e9e83983e7155ae8e1056f8   claude/circle-four-prover-liazib
the-workshop-circle-four   main 7709f587ed9f3b46988a67d05103f4f5e3fb4602
                         branch 52e42096a8ea46e8e9aea3872f40a2b8fe943fc3
the-workshop-circle-five   EMPTY — unborn HEAD, no refs, zero files
```

**The record moved three times while I was reading it.** At my first
fetch the system branch stood at `2a6b7ac…` and Circle Four's at
`550d365…`; by my second both had advanced and both had landed on their
default branches; by my third the system branch had been rebased onto
`main` and now reads `91d3d4c5…` — same SR57 subject, new hash. **Every
head above is a measurement with a timestamp, not a fact**, and a reader
should re-measure rather than cite them.

## 2. THE PINS — every one the courier named, and the same files in the live record

All five delivered pins verify byte-exact:

```
circle-five-crate.zip         0281631bbfbba6861f94aaf2e0cfcf057db60319d4688d9576922a3dfa339c8b  MATCH
CLOSING-C4.md                 24933dce71ad76aacc362e30c659f1ffb7945c78775a5079e18830ee5c0fe7c9  MATCH
STATE-OF-THE-RECORD-v4.md     6564ebf03076015c247ef8317bc842e464bf81046d8f5feac1a47c19da23cc9c  MATCH
CIRCLE-FIVE-CHARGE-DRAFT.md   69047be708c0b04b1b3a2bed4e5e6931535e46eb51bfe551671b0861101ad35f  MATCH
CRATE-MANIFEST.md             832397f09778716c0458f3ec5db3edad2303c857053edb65f8ce0cdbbde7d583  MATCH
```

I then measured the same three documents **inside the live record** at
`f8f3f37…` and they are byte-identical to what I was handed. **The
crate's contents are authentic.** What is wrong with this handoff is not
its bytes — it is what several of its sentences say about the present.

## 3. THE CROP — loudest first

**At a glance, so this can be triaged without reading all of it.** Ten
items. **Nothing here touches Circle Four's mathematics, which
re-verified whole** (§3b, §4). Every defect is in the *handoff*.

```
                                                          who can fix it
C5-F1   the wayfinder tells every new seat the door is       courier
        unrepaired; it was repaired at SR51 — and the
        stale sentence is LIVE in the record, not only
        in the crate                                         BLOCKING
C5-F2   *** WITHDRAWN — MY ERROR. *** I claimed the           (none —
        crate's clones could not fetch. The stored              retired)
        origins ARE canonical GitHub; the proxy I saw
        was an insteadOf rewrite in MY container, read
        through git remote -v. Retired, not erased.
C5-F3   circle-one-carry/ cannot do the one job the          crate builder
        manifest gives for shipping it (G6 needs the
        archive/ the carry drops); and the manifest's
        printed command exits 1 as written                   SERIOUS
C5-F4   "staged from the remote" cures a stale copy, not     the record
        a remote that moves afterward — SR8 diagnosed
        this and it went uninstrumented                      SERIOUS
C5-F5   the charge draft undercounts the inheritance by      the record
        three register rows, and was already false in
        the commit that filed it                             SERIOUS
C5-F6   SR43 DEMONSTRATED, not restated: I planted a         the record
        byte-tampered copy of the seal as a NEW file and
        ALL FIVE gates said PASS — one printing "no
        uncarried file" while it sat in lean/. Also:
        system/crossings/, holding every document a
        Circle Five seat is told to read, is guarded by
        no instrument at all                                BLOCKING
C5-F7   no chartered charge exists; the handoff is           principal
        incomplete on door §5's own rule                     STRUCTURAL
C5-F8   only one seat convened; a parity handshake           principal
        takes two                                            STRUCTURAL
C5-F9   Circle Five's repository is empty; its first         courier
        landing is not mine to perform                       STRUCTURAL
C5-F10  S3 still rides PROVISIONAL; the cure needs           principal /
        Circle Four's seats and is PERISHABLE                courier
```

**The two perishable items, named together because nothing watches
them:** the prediction text's single durable copy (§6), and S3's
co-adjudication window (C5-F10). Both die quietly.

### C5-F1 — THE ONE DOCUMENT A NEW SEAT OPENS FIRST IS THE ONE THAT HAS GONE STALE, AND IT IS STALE IN THE LIVE RECORD, NOT ONLY IN THE CRATE

`README-CIRCLE-FIVE.md` (`77e11aa4…`) is the wayfinder. Its line 6 tells
an incoming seat to read the door **"(note: F8/F9 unrepaired, see
below)"**, and its body repeats that the two sites are outstanding.

**They are repaired.** `SR51` records it; commit `f98c45c…` performed
it; the repaired door hashes to `0fda936f…`, exactly the pin the
courier's post-seal leg publishes. I read both repaired passages rather
than trusting the row.

**F8's repair spans `:372-380`, and its new text lands on `:374` — the
very line number the record convicted** — reading *"THREE edits and not
one"* with each of the three named. F9's repair has moved down to
`:384-395`, because F8's added lines above it; the door grew from 512
lines to 526.

**So `:380` — the line number all four crate documents still cite for
F9 — now holds part of F8's replacement text.** Both cited line numbers
are stale, and one of them does not merely dangle: **it points a reader
at the wrong defect.**

The wayfinder was last touched at `e31c47b…`, **before** the repair. It
has not been corrected since, and **no register row corrects it** — I
grepped the whole register for `README-CIRCLE-FIVE` and `START-HERE`;
the single hit is `SR49` pinning it at `77e11aa4…`, which is the stale
pin itself.

**This is SR2's species, recurring at this crossing.** SR2 reads: *"The
door was staged to the ferry directory, then edited in the record
through four further commits, and the stale staging copy was ferried.
**The one document a receiving seat opens first was the one document
that had gone stale.**"* That is a description of what has just happened
to me, written by this record about itself, two circles ago.

**The sharp part, and it is why I rank this first.** `SR49` pinned three
inheritance documents at the seal. `SR51` — two rows later, in the same
appended block, by the same seat — repaired the door and thereby
falsified a sentence in one of the three documents `SR49` had just
pinned. **The falsifying act and the falsified pin are neighbours in one
file, and nothing joined them.**

Four documents currently tell an incoming Circle Five seat that F8 and
F9 are unrepaired: `README-CIRCLE-FIVE.md` line 6,
`STATE-OF-THE-RECORD-v4.md:121`, `CIRCLE-FIVE-CHARGE-DRAFT.md:113`, and
`CRATE-MANIFEST.md`'s closing section. **The first two are live in the
record right now.**

#### The mechanical cause, and the door already held the cure

The door ships a **pasteable kickoff** at §6 whose whole purpose is to be
the true first document. Its preamble states the reason in one sentence:
*"**a new body orients to whatever its first documents imply, so the
first documents must be the true ones.**"* **That sentence is the exact
diagnosis of this finding, written in the door, before the fact.**

The template it prescribes (`INHERITANCE.md:433-438`) carries a
**Repositories block**:

```
Repositories:
  "the-workshop"              Circle One, SEALED at <SEAL PIN>
  "the-workshop-circle-two"   Circles Two and Three, SEALED at <SEAL PIN>
                              live default branch at <POST-SEAL HEAD>
  <this circle's repository>  <where you work>
```

**`README-CIRCLE-FIVE.md` has no Repositories block at all.** It keeps
the kickoff's step 1 — *"Say which repositories you can actually reach.
Do not assume — check"* — and **drops the table that says what to check
against.** A seat is told to verify reachability and given no reference
value to verify toward.

**`<POST-SEAL HEAD>` is precisely the field that would have shown me the
live head, and through it the repairs.** Fill it in and C5-F1 cannot
happen: the seat compares the crate's `e31c47b…` against the named
post-seal head, sees they differ, and goes looking. **Leave it out and the seat is not told the record
has moved** — it must think to go looking. A fetching seat can still find
out (see the withdrawal at C5-F2); nothing seals the exit. But the
wayfinder's job was to make the check unnecessary, and instead it states
the stale answer as fact.

The door's own instruction for that block is *"keep this block repaired
as the living thing it describes."* **The wayfinder is a lossy derivative
of it that dropped the living part and kept the ceremony.**

*The fair reading against myself:* `STATE-OF-THE-RECORD-v4.md` and the
charge draft are sealed-era documents, and this record's doctrine is
that such documents are not edited but superseded by a new row pointing
at the old one — which `SR51` is. **That defence covers those two and
does not cover the wayfinder**, because the wayfinder is not a historical
snapshot: it is an operative instruction whose only function is to be
read as present tense by someone who has read nothing else. And the door
itself is not under the append-only law — `SR51` says so plainly, and
repaired it in place, as its four prior repairs were.

### C5-F2 — **WITHDRAWN. THIS FINDING WAS WRONG, AND IT WAS MINE.**

*This section originally read "THE CRATE'S CLONES CANNOT FETCH, AND THE
MANIFEST SAYS THEY CAN", and ranked it BLOCKING. It is withdrawn in
full. The original text stands in this repository's history at commit
`ca903b4`; it is retired, not erased.*

**What I claimed.** That `CRATE-MANIFEST.md:47-49` was false when it said
each clone has *"`origin` set to its canonical GitHub URL"*, because
`git remote -v` in both crate clones reported
`http://local_proxy@127.0.0.1:41729/git/…`.

**What is actually true.** The raw `.git/config` that travels inside the
crate — the only thing that ships — stores the canonical URL in both
clones:

```
[remote "origin"]
	url = https://github.com/irreducible-mystery/the-workshop-circle-four.git
	url = https://github.com/irreducible-mystery/the-workshop-circle-two.git
```

**The proxy address is a rewrite in MY container, not a value in the
crate.** This container carries a global git rewrite rule:

```
url.http://local_proxy@127.0.0.1:41729/git/.insteadof  https://github.com/
```

`git remote -v` applies `insteadOf` **at read time**. I read a value
through a transform, saw the transformed output, and reported it as the
stored state of someone else's artifact. **The manifest's sentence is
correct and my finding was an artifact of my own environment.**

**This is the second time in one session that I measured through a
layer** — the first was the pipe-exit in C5-F6, which is SR30's species.
**These are the same defect wearing different clothes:** a value observed
through something that changes it, reported as if observed directly.
`git remote -v` is to `.git/config` exactly what `| tail` is to an exit
code. I caught the first one myself and did not generalise it, and the
second one got past me and into a filed letter ranked BLOCKING.

**What it cost, stated rather than minimised.** C5-F1's original text
leaned on this to argue the staleness was *undiscoverable from inside the
crate*. That argument is void: a seat with GitHub access can fetch from
these clones and find the repairs. **C5-F1 itself is untouched** — the
wayfinder is still stale, and still stale in the live record — but it is
an ordinary staleness a fetching seat can catch, not a trap with the exit
sealed. I have corrected that clause where it appears.

**How it was caught, because that belongs in the row too:** not by me.
An adversarial verifier re-ran my command, reproduced my exact output,
and then read `.git/config` directly — the check I did not do. **The
two-body standard found this, which is the whole reason the record keeps
it**, and it found it against the seat that spent this letter reporting
other people's unverified sentences.

### C5-F3 — THE CARRY CANNOT DO THE ONE JOB THE MANIFEST GIVES AS ITS REASON FOR RIDING

`CRATE-MANIFEST.md:71-77` justifies shipping `circle-one-carry/`: *"It
rides because `c2_gift_certificates.py` **can be pointed at a Circle One
tree via `C1_LEAN`**."*

`CARRY-NOTE.md:15-17` records what the carry omits: `history/`, **plus
`archive/` and `audit/`**.

`audit/c2_gift_certificates.py:1253` — the `G6_calibrator_remeasured_coker`
certificate — opens `os.path.join(LEAN, "archive/src-round7/MagicSquare.lean")`.

**`archive/` is exactly what the carry dropped.** Measured, both ways,
same container, same everything else:

```
C1_LEAN=circle-one-carry            70 checks,  1 failed,  exit 1   NOT CLEAN
   FAILED: G6_calibrator_remeasured_coker  —  FileNotFoundError

C1_LEAN=<the real Circle One tree>  70 checks,  0 failed,  exit 0   CLEAN
```

A seat holding only this crate **cannot get a clean certificates run**,
which is the single purpose the manifest names for the directory it
spent its size budget on.

**And the recipe as written does not run at all.** The manifest's own
"first commands for a receiving seat" (`:93-95`) offer:
`C1_LEAN=<…>/circle-one-carry python3 audit/c2_gift_certificates.py`.
Run verbatim it **exits 1**, on a `FileNotFoundError` for
`/home/claude/workshop/symmetric_statistics.py` — a path from a container
that no longer exists, reached through `C2_WORKSHOP`, an environment
variable the manifest never mentions.

**This is the seam door §8 names and leaves unguarded:** *"neither can
tell whether a recipe in it actually runs. **That is the seam the wrong
`C1_LEAN` path lived in for two circles**, and this sentence is the only
thing guarding it. Run the commands."* I ran the commands. The seam is
still occupied.

**The repair, measured rather than proposed** — this recipe exits 0 with
70 of 70 green, and it is the contribution I can make without a charge:

```
pip install numpy scipy sympy          # none present; three gates fail silently-ish without them
C1_LEAN=<a real Circle One tree>   \
C2_WORKSHOP=<circle-two tree>/floor \
    python3 audit/c2_gift_certificates.py     →  70 checks, 0 failed, exit 0
```

Note `C2_WORKSHOP` must point at **Circle Two's** `floor/`, not Circle
One's: door §7 records that the two trees differ by exactly the crop-item-1
repair, and pointing it at Circle One's floor fails
`G1h_docstring_carries_exact_4` — the gate correctly detecting that it is
being shown the unrepaired bench.

### C5-F4 — THE CURE FOR THE STALE DOOR WAS AIMED AT THE WRONG FAILURE MODE

`CRATE-MANIFEST.md` states each clone was staged **"from the remote, not
from a working copy (rule C5)"**, and says: *"The Circle Four stale-door
incident is why staging happens this way."*

Staging from the remote defeats a stale **working copy**. It does
nothing against the **remote advancing after the crate is built** — and
that is what happened: the crate froze the system tree at `e31c47b…`,
and `f98c45c…` and `2a6b7ac…` landed afterward. **The crate is honest
about its own freeze** — its heads table names `e31c47b…` — but the four
narrative documents around that table speak in the present tense, and a
seat reading them cannot tell which sentences the freeze invalidated.

**Rule C5 is a real rule and a good one** — build the crate from a clone
of the remote, never from the sender's working copy — but it answers
*"is my copy stale relative to the remote?"*. The failure that actually
occurred is *"did the remote move after I copied it?"*, and no rule in
this record addresses that. Invoking C5 against the stale-door incident
treats the two as the same failure. They are not.

`SR8` already named the general form: *"sealing-then-improving makes
version skew between simultaneously-shipped artifacts structural, not
careless."* **That row is the diagnosis, and it went uninstrumented** —
which is the same sentence this record keeps writing about SR43.

### C5-F5 — THE CHARGE DRAFT UNDERCOUNTS THE INHERITANCE, AND WAS NEVER TRUE AT ANY INSTANT IT EXISTED IN THE RECORD

`CIRCLE-FIVE-CHARGE-DRAFT.md:111` tells a Circle Five it inherits *"the
system record's norms and SR-register **through SR47**"*.

I checked when that stopped being true, expecting to find a later commit.
There is none. **It was already false in the commit that filed it.**

```
467f60f  (parent)      SYSTEM-REGISTER.md high-water:  SR47
e31c47b  (files the charge draft)                      SR50
         — and the draft, added in that same commit, says SR47
```

At its parent the register stood at SR47, so the sentence was accurate
while it was being drafted. But `e31c47b…` filed the draft **and** SR48,
SR49 and SR50 together. **From the first instant the document existed in
the record it understated the inheritance by three rows**, and one of
those three is `SR49` — the row that pins this very draft. A document
naming what the next circle inherits is undercounting a register that
contains the row about itself.

`CRATE-MANIFEST.md:24` says **through SR50** and was right at crate-build
time. The live register is now at **SR57**.

**This is SR15's species.** SR15 convicted a custody note that said the
charge carried one edit when it carried three — an undercount in a
handoff document, caught by a receiving seat's diff. This is an
undercount in a handoff document, by three, caught the same way.
`STATE-OF-THE-RECORD-v4.md` makes no register claim at all, which on
this axis makes it the most accurate of the three.

### C5-F6 — SR43 IS NOT MERELY OPEN, IT IS EXPLOITABLE: I FORGED THE SEAL AND ALL FIVE GATES SAID PASS

SR43 has been *named three times and instrumented never*. It has always
been stated as a possibility. **I planted it, and it works.**

In a throwaway copy of Circle Four's tree (baseline: all five gates
exit 0), I added one file — `lean/C4_Q4.lean` — containing a **byte-tampered
copy of the sealed artifact** plus a forged declaration:

```
real seal   sha256  6a6b6cb2…
the forgery sha256  9df64b26…      one byte flipped at offset 70000
```

**All five gates, exits taken directly, no pipe:**

```
c4_manifest_prefix  exit 0     c4_seal_prefix     exit 0
c4_inherited        exit 0     c4_artifact_prefix exit 0
c4_carried_defs     exit 0
```

**And it is worse than silence — the gates affirmatively assert the
things the plant falsifies:**

```
c4_seal_prefix      "1 carrying file(s) carry the seal byte-exact.  PASS."
                      — while a second file carries a CORRUPTED seal
c4_artifact_prefix  "3 artifact(s) grew by appending only.  PASS."
                      — while lean/ contains FOUR files
c4_inherited        "40 manifest rows re-measured, no drift, NO UNCARRIED FILE"
                      — the uncarried file is sitting in lean/
```

*"No uncarried file"* is the sentence the plant most exactly refutes,
and the gate prints it as a pass. **The forgery also kernel-checks
silently** — `lean lean/C4_Q4.lean` exits 0 with zero bytes — **so norm 10
does not catch it either.** A corrupted copy of the sealed artifact can
enter this record, pass every instrument, satisfy the silence rule, and
be reported as green by name.

**The plant was destroyed immediately and no tree I touched retains it.**

I say this plainly and without drama: **this is the record's own named
hazard, and it took one file to demonstrate.** What follows is why it is
also cheap to close.

#### The asymmetry — the record already built the cure, in one gate, and did not give it to its sibling

`audit/c4_carried_defs.sh` **does** defend against the unlisted case, and
says why in its own comment at `:58-59`: *"The name list alone cannot see
an EXTRA declaration smuggled inside the CARRIED banner: the smuggled
text wears the seal's authority and nobody…"* — and at `:77` it emits
`SMUGGLED: declared inside the CARRIED banner, on no carried list`. That
defence fires: planted with an eighth declaration inside the banner, the
gate exits 1.

`audit/c4_seal_prefix.sh` **does not**. It hardcodes `CARRYING="lean/C4_Q3.lean"`
at `:40`, iterates exactly that at `:52`, and contains **no scan for
files that carry the seal but are on no list** — zero occurrences of any
smuggle check. **A Circle Five seat that adds a second seal-carrying file
gets a green gate**, and the manifest's *"1 carrying file carries the
seal byte-exact"* silently becomes a count of the script's own list
rather than of the tree.

**The count is nonetheless true today**, and I checked it rather than
assuming: a byte-prefix scan of every tracked file in the Circle Four
tree finds exactly two files carrying the seal — the seal itself and the
listed `lean/C4_Q3.lean`.

**And there is a third instance, which is the one that explains C5-F1
mechanically.** I went looking for which instrument guards the wayfinder
and found that none does:

- The prose gates' document list **was already cured** of exactly this
  hazard. `audit/c2_pointers.sh:130` says so: *"r2 quarantine-review
  fix: docs are **DISCOVERED, not enumerated** — every top-level `*.md`
  and every `*.md` under `letters/` … so a future `ROUND2.md` is scanned
  the day it lands instead of silently skipped."* That fix is real and it
  works; it is why the door, a top-level `*.md`, is scanned and why
  `SR51` could truthfully say *"prose gates green after the edit."*
- **But `system/` was created after that cure and never brought under
  it.** The discovery glob reaches top-level and `letters/`. It does not
  reach `system/crossings/`.
- And the system record's own two instruments guard a **hardcoded
  two-file list**, both of them, identically —
  `system/audit/s_append_only.sh:55` and
  `system/audit/s_append_only_p2_candidate.sh:42`, each reading
  `for f in system/SYSTEM-REGISTER.md system/SYSTEM-NORMS.md`. **The two
  gates were wired beside each other because their blind spots are
  disjoint; on this axis their blind spot is the same one.**

**Net: `system/crossings/` is guarded by no instrument in this record.**
That directory holds the charge draft, the wayfinder, the crossing
letters, and the crossing copy of the state map — **every document a
Circle Five seat is told to read.** The record cured "enumerated instead
of discovered" once, then grew a new tree outside the cure, and put the
next circle's entire inheritance inside it.

**Why this is worth more than another restatement of SR43:** the charge
draft's candidate QC asks whether a gate here *"can be made to guard a
**class** of files rather than a **list** of them."* **One gate in this
record already does it for declarations, and the prose gate already does
it for documents.** The question is therefore not whether the class-based
predicate is possible — this record contains two working instances — but
why the two trees that most needed it are the two that did not get it. I
record that as a measurement bearing on QC and **stop there**, because QC
is not chartered and answering it is not mine to start.

**I did not infer this from reading the glob — I planted a falsifier and
measured the gate both ways.** Same unresolvable token
(`` `THIS-FILE-DOES-NOT-EXIST-xyzzy.md` ``), two locations, exits read
directly rather than through a pipe:

```
planted in README.md (a top-level *.md)      c2_pointers.sh  exit 1  UNRESOLVED, FAIL
planted in this letter, under
   system/crossings/four-to-five/            c2_pointers.sh  exit 0  0 unresolved, PASS
```

**"82 docs scanned" in both runs.** My file was never in the document
list at all. Both plants were removed and the tree verified clean before
this letter was filed.

**Filed against this letter itself, because the rule applies to me
too:** this document lands in that unguarded tree. **No pointer gate
checks that its backticked names resolve; no numeral gate checks that
its bare numbers are sourced** — I have just demonstrated both. Every
number and pin in it is one I ran a command to get, and a reader should
treat that as a claim to audit rather than a reason to relax. **I am
reporting a gap and then depositing a document into it**, and the honest
thing is to say so rather than let the next seat discover that my crop
was itself ungated.

**And filed against this seat, because it happened while I was proving
the above.** My first measurement of that plant read the exit code
**through a pipe** — `sh audit/c2_pointers.sh 2>&1 | tail -6; echo $?` —
so the shell reported `tail`'s exit, and my terminal showed
`RESULT: FAIL` with `exit=0` directly beneath it.

**SR30 describes that outcome in these words:** *"the docstring plant was
first measured with the gate's output piped to `tail`, so the shell
reported the PIPE's exit — **a green printed beside a red line**.
Re-measured with the exit taken directly: exit 1."*

**A green printed beside a red line is precisely what I produced.** SR30
is itself a row about a *reproduction* — Circle Four's prover repeating
the builder's defect one round later. **This is the third occurrence, by
the third seat, in the act of testing a gate.** I caught it only because
the FAIL and the 0 were adjacent and disagreed; had the plant been in a
scanned file only, or the output shorter, they would not have been.

**Filed with a conclusion rather than an apology:** a defect that has now
recurred three times across three independent seats is not carelessness
and will not be cured by another seat resolving to be careful. **It is a
missing instrument.** Nothing in any chain here stops a seat from reading
an exit through a pipe, and every seat that has run these gates has
eventually done it. That observation is free to make and is not mine to
act on without a charge.

### C5-F7 — THE HANDOFF IS INCOMPLETE ON THE DOOR'S OWN RULE

Door §5 (`INHERITANCE.md:263`): **"THE RULE: a handoff is not complete
without a charge."**

I searched every ref of the live record for a chartered Circle Five
charge. There is exactly one Circle Five charge object in existence,
`CIRCLE-FIVE-CHARGE-DRAFT.md` (`69047be7…`), and it charters nobody by
its own first sentence. **No selection instrument exists**, and there is
**no `four-to-five/` crossing directory** — the draft and the wayfinder
are both filed under `system/crossings/three-to-four/`, the previous
crossing.

**So I say so, and I stop — but I want to be exact about what I am
stopping from, because I checked the citation and it does not say what
it is quoted as saying.**

`README-CIRCLE-FIVE.md` and `CRATE-MANIFEST.md` both write: *"say so and
stop rather than inferring one **(door §5)**."* **Door §5 contains no
stop instruction and no verb of seat conduct at all.** It spans `:254-318`
and states a property of the *handoff*. The sentence being quoted lives
at **`:432`, inside §6, the pasteable kickoff** — and its own text reads
*"say so and stop rather than inferring one **(see section 5)**"*, a
cross-reference that both derived documents flattened into an attribution.

**The duty is real; only the pointer is wrong.** And reading it where it
actually lives settles the question that matters to me, because `:426-432`
is a numbered list headed **"Before you build anything"**:

```
1. Say which of those you can actually reach. Do not assume — check.
2. Read INHERITANCE.md, then STATE-OF-THE-RECORD-v<N>.md.
3. Run the parity handshake: measure the pins rather than trusting
   them, and report the crop loudest first before accepting the charge.
4. Run the gate chain and STATE THE TREE YOU RAN IT IN.
```

**The stop is from *inferring a charge*. It is not a stop from
verifying** — verification is steps 1 through 4, it is prescribed, and
step 3 says in terms that the crop is reported **"before accepting the
charge."** **This letter is step 3.** Everything in it was done under an
instruction that exists precisely to be carried out before a charge
arrives, and none of it presumes one.

### C5-F8 — I AM ONE SEAT, AND A PARITY HANDSHAKE TAKES TWO

The ceremony the charge draft records requires **both incoming seats** to
read the charge after their parity handshake and each answer in one
letter. **Only a prover has been convened.** There is no Circle Five
builder in this crossing that I can reach or address. A parity handshake
has no counterparty, so what follows is **half of one, filed as half**.

### C5-F9 — CIRCLE FIVE'S REPOSITORY IS EMPTY, AND ITS FIRST LANDING IS THE COURIER'S

`the-workshop-circle-five` has an unborn HEAD and no refs. **I have
deliberately not pushed to it.** Pushing the first branch to an empty
repository sets its default branch, and setting a default branch is a
landing.

The record has already convicted a prover of precisely this. Circle Four
listed it among the five defects it filed against itself:
**"a landing performed by the seat the gate constrains"**
(`STATE-OF-THE-RECORD-v4.md`). `SR26` records the courier's ratification
— *"main as it stands is my landing, ratified"* — and is explicit that
the finding *"stays filed as what happened — answered by the
ratification, not erased by it."* `SR57`, filed today, closes that loop
in the good direction: the courier's own merge, *"the first act in that
tree that was a landing when it happened."*

**Having watched this record spend two rows getting that right, I am not
going to spend its third getting it wrong.** This letter is filed in the
crossing where crossing letters live. Founding Circle Five's repository
is the courier's act to perform, and I will do it on her word and not
before.

### C5-F10 — S3 IS STILL PROVISIONAL, THIS CROSSING WAS ASSIGNED THE CURE, AND I CANNOT PERFORM IT — SO I RECORD WHY NOT

`STATE-OF-THE-RECORD-v4.md` hands this crossing an explicit instruction:
*"the system record's **S3 (the selection norm) rides PROVISIONAL until
Circle Four's seats co-adjudicate** … Circle Four sealed without that
co-adjudication being performed as a separate act; **a Circle Five
crossing should either perform it or record why not.**"* The register
says the same in its own voice at the row before the seal: *"Recorded for
the crossing that follows: **S3 remains PROVISIONAL until Circle Four's
seats co-adjudicate at this seal, per its own clause.**"*

**Measured: it is still unperformed.** `SYSTEM-NORMS.md:194-196` carries
S3 as *"BOTH WORDS GIVEN — ADOPTED, PROVISIONAL … until Circle Four seals
and its seats co-adjudicate."* The status appendix at `:232-236` records
the other limb discharged — *"S3's condition 'subject to the principal's
confirmation of the founding': **MET this leg**"* — and then repeats that
S3 *"stays ADOPTED-PROVISIONAL … until Circle Four seals and its seats
co-adjudicate."* **Circle Four has since sealed (SR48). The second limb
has not been performed**, and I grepped every row through SR57 and every
line of the norms for a co-adjudication: there is none.

**So I record why not, which is the branch the instruction offers.**

**The act is not mine to perform.** S3's clause names *Circle Four's
seats*. I am not one; I am the incoming circle, and a norm that governs
how charges are selected **for me** is precisely the norm I am the wrong
party to ratify. A Circle Five seat co-adjudicating S3 would be
approving the rule under which its own charge is chosen — the structural
conflict this record already named in `SR54` when it wrote that **"the
genuinely cold reviewer does not exist"** and made both seats declare
their interest anyway.

**What I can say that is useful rather than merely abstaining:**

- The act appears **still available**. Circle Four's seats are barred
  from being *Circle Five seats*; they are not barred from acting as
  *Circle Four's seats post-seal*, and `SR54` is proof — both gave
  post-seal words on the §5b repair after the seal. **If those sessions
  are still reachable, the co-adjudication can be asked for directly.**
- It is **perishable**, and that is the part worth flagging now. `SR53`
  records that one of those two containers is *"ephemeral and dies with
  the session."* **The window in which S3 can be cured as written is the
  window in which those two sessions still exist**, and nothing in the
  record is watching that window.
- If it closes, S3's own clause becomes unsatisfiable as drafted, and
  the record will need a decision — amend the clause, or carry the norm
  provisional indefinitely. **That is the principal's call and I am not
  making it.** I am naming it while it is still cheap.

### Minor pointer defects, clustered rather than given rooms of their own

None of these changes a conclusion. All are the kind of thing the
pointer gate would catch if it reached these files (C5-F6).

- **`START-HERE.md:6` promises an explanation it does not contain.** It
  reads *"the door (note: F8/F9 unrepaired, **see below**)"* — and
  `grep -n 'F8\|F9'` over that file returns **exactly one line: `:6`**.
  There is no below. The four bullets that follow name the DRAFT charge,
  R4, SR43 and the prediction; **none of them mentions F8 or F9.** So the
  wayfinder tells a new seat about a debt, gets the debt wrong (C5-F1),
  and points at an explanation that was never written.
- **Norm 21 is cited for a rule it does not contain.** `CRATE-MANIFEST.md:4`
  and `CIRCLE-FIVE-CHARGE-DRAFT.md:145` both write *"the crate cannot
  carry its own pin **(norm 21)**"*. Norm 21 (`NORMS.md:202`) is
  *"self-reference is pointed at, not convicted"* — and its disposition
  is the opposite of a prohibition: such a claim is *"recorded, pointed
  at, and left standing… the record never trades such a sentence for
  tidiness."* **The rule being invoked is `SR7`**, which states *"A crate
  cannot carry its own pin"* and calls it *"the boundary form of the
  self-reference norm."* **Norm 21 is the parent, `SR7` is the rule** —
  and the practice the crate follows is correct either way.
- **`NORMS.md` ships norms 19 and 20 transposed.** Under a heading that
  says the circle's norms are *"numbered from 17 so that a later reader
  can tell inheritance from experience at a glance"*, the file order is
  17 `:128`, 18 `:138`, **20 `:152`, 19 `:174`**, 21 `:202`. Every
  number and text is correct; only the sequence is not, and the freeze
  rule protects the numbers rather than the ordering.

## 3b. THE SHOPPING LIST, RE-MEASURED FROM THE SOURCE RATHER THAN THE PROSE

I read the Lean rather than the closing, and tried to **break** the
refusal — to find a construction that would make any one of R1–R8 met,
which would mean Circle Four overclaimed a refusal.

**I could not. "NOT MET, eight for eight" survives.** The two structural
facts that carry it:

- **No group is declared anywhere.** Across `Zi.lean`, `C4_Q1`, `C4_Q2`
  and `C4_Q3` there is **not one real `class` or `instance`
  declaration.** Every apparent hit is the English word *"instance"* or
  *"class"* inside a prose comment. R6, R7 and R8 fail at the carrier.
- **R4's distinction is real in the code, not just in the rhetoric.**
  `GaugeClasses` (`C4_Q3.lean:2999`) is `Quot` of a **subtype** by a
  **`Prop`-valued relation** — and `Quot`'s second argument need not even
  be an equivalence, let alone a normal subgroup. Neither side is a
  group.

**And `class_count_is_two` really is set-level**: `C4_Q3.lean:3073` is
literally the pair `⟨classOfBool_surjective, classOfBool_injective⟩`,
with no operation on `Bool` and none on `GaugeClasses`.

### The trap list — one addition survives, and two claims of mine do not

*This section originally asserted three unlisted traps and ranked the
finding SERIOUS. **Two of the three are withdrawn on an adversarial
re-reading I accept.** The original stands in history at `ca903b4`.*

**WITHDRAWN — "the seal's prose claims R2's object."** I quoted
`Zi.lean:2571-2573` calling `g ↦ gaugePhi g` *"a homomorphism"* and read
it as reaching for R2. **The seal denies R1–R4 explicitly, forty lines
later**, in a ruling I did not quote:

> `Zi.lean:2609-2618` — *"THE `H³` RULING… **NOT CLAIMED, and
> deliberately.** Nothing here constructs a cochain complex, a coboundary
> operator between graded groups, a cocycle condition as a kernel, or a
> quotient of one by the other."*

**And the homomorphism paragraph scopes itself in its own last
sentence:** *"It is done at the level of the factor, in the ring, **with
no cohomology machinery anywhere near it**."* That is not a claim
reaching for R2; it is a claim carefully fenced away from it. **The
"gauge group" phrases at `:2691` and `:2718` fall with it** — they are
covered by the same published ruling. I read a fragment and did not read
the section that governs it.

**WHAT SURVIVES, and I still think it is worth a line on the list:**
**`Zi.lean:137` — `## 1. The additive structure — an abelian group`.**

R7 requires *"`Z[i]ˣ` as an abelian group."* This heading carries **R7's
exact phrase**, and all six abelian-group axioms are genuinely proved
under it — `add_comm:139`, `add_assoc:142`, `add_zero:145`,
`zero_add:148`, `add_neg:151`, `neg_add:154` — **for the additive group
of `Z[i]`, not the multiplicative group of its units.**

This one is not covered by the ruling above, and I checked rather than
assumed: **the `H³` ruling enumerates R1–R4 and the matching. It does not
address R6, R7 or R8** — those are Circle Four's own additions, *"the
three the headline presupposes"* (`CLOSING-C4.md:76`). And
`grep -niE 'additive.*unit|not the units|wrong group'` over the seal
returns nothing: **the additive-versus-units distinction is warned
nowhere.**

So a seat grepping `abelian group` for R7 lands on a phrase-exact match
with a complete proof under it, and neither the seal nor the closing says
"wrong group." **That is a genuine addition to the trap list — one, not
three.**

### One place the closing's rhetoric outruns its own analysis

`CLOSING-C4.md:89` says of R4's quotient and the sealed one: **"They
share the word and nothing else."**

Measured, they share more. `gaugeAct_eq_phi` (`Zi.lean:2716`) is `rfl`,
so `gaugeAct g F = F · gaugePhi g` **definitionally**; substituting into
`GaugeEquivOnLabels` (`:2791-2794`) unfolds it to *"`F'` and `F` differ
by `gaugePhi g` at every label triple"* — **which is exactly the coset
shape a quotient-by-coboundaries has.** What is genuinely absent is only
the group structure on either side.

**This matters to whoever takes up QA**, because "nothing else" would
send a seat looking for a distant object when the shape is already
there and only the algebra is missing. **A sentence that understates a
circle's own result is still a sentence that misleads the next one** —
and this record's standard is that the count is the list's, not a
memory's.

*Minor, recorded for exactness rather than effect:* `units_are_four` is
cited at `:1093` in both the closing and the state map; the theorem
keyword is at **`:1094`** — `:1093` is the last line of its docstring.

## 3c. WHAT THIS LETTER GOT WRONG

*Filed against this seat, in the place a reader will reach it, because a
crop that reports only other people's defects is the thing this record
exists to catch.*

**Two findings withdrawn**, both refuted by adversarial verifiers who
reproduced my commands and then did the check I had not:

```
C5-F2   the crate's origins        WITHDRAWN IN FULL — the stored origins
                                   are canonical GitHub; I reported an
                                   insteadOf rewrite in my own container
C5-F6*  "no smuggle defence" and the SR43 demonstration STAND
§3b     "the seal's prose claims    WITHDRAWN — the seal rules NOT CLAIMED
        R2"; "gauge group"         explicitly at Zi.lean:2609-2618, and the
                                   homomorphism paragraph fences itself
§3b     Zi.lean:137 abelian group  STANDS — R7's exact phrase, six axioms
                                   proved, wrong group, warned nowhere
```

**The single defect underneath both, named once:** *I reported values
observed through a transforming layer as though observed directly.*

- `git remote -v` renders `.git/config` **through `insteadOf`**. I read
  the render.
- `sh gate | tail` renders an exit code **through a pipe**. I read the
  pipe. That one is `SR30`'s species and I caught it myself — **and then
  failed to generalise it by one command.**
- Quoting `Zi.lean:2571` without `Zi.lean:2609` is the same move at the
  level of prose: a fragment read through its own framing, with the
  section that governs it out of view.

**Three instances, one session, one seat.** The record already carries
this shape twice (`SR30`, and the builder's original). **I would rather
this row said "an instrument now catches it" than "a third seat resolved
to be careful", and it cannot, because building that instrument is not
mine to start without a charge.** I name it so the next seat inherits the
pattern rather than the resolution.

**What did not change, measured again after the corrections:** every pin
in §2; the three artifacts SILENT; the seal's 141,511-byte prefix and its
`6a6b6cb2…`; every gate result in §4; the SR43 plant in C5-F6, which I
performed with my own hands and destroyed; and **C5-F1**, which two
independent verifiers reproduced and upheld.

## 4. WHAT I MEASURED GREEN, AND IT IS THE MAJORITY

None of the above touches Circle Four's mathematics or its instruments,
which stood up to everything I put on them.

**The toolchain recipe works, fourth session running.** `zstd` was
absent exactly as recorded; `pip install zstandard` then stream-extract
worked. The binary reports **`4.32.0 … commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35`** —
the pinned commit, exactly.

**Two additions to that recipe, both bought by walking into them**, since
the record asks four sessions running for this and the next seat may as
well be spared:

- **The extraction is ~2.9 GB and slow, and a `lean` run against a
  half-extracted tree fails misleadingly** — `error while loading shared
  libraries: libInit_shared.so`. That is not a broken download; it is
  `lib/lean/` not yet written. **Wait for the extractor to exit before
  concluding anything about the binary.** I briefly believed the archive
  was missing a library, and it was not.
- **The certificates need three Python packages the record never names:**
  `numpy`, `scipy`, `sympy`. Without them the gate reports failures that
  look like drift — `G0_symmetric_statistics.py_green`,
  `G1b_search_reproduction` — and are not. **Absent packages should not
  be readable as record drift**, and on this container they were.

**All three artifacts are SILENT under norm 10**, run in the crate's
`circle-four` tree on that toolchain:

```
lean/C4_Q1.lean    exit 0, 0 bytes    SILENT
lean/C4_Q2.lean    exit 0, 0 bytes    SILENT
lean/C4_Q3.lean    exit 0, 0 bytes    SILENT
```

**The seal is carried whole, and I measured the claim rather than the
sentence.** `CLOSING-C4.md` says `C4_Q3.lean` carries the sealed
artifact as a byte-exact prefix of 141,511 bytes. The sealed
`Zi.lean` is 141,511 bytes; `C4_Q3.lean` is 150,281; **the first 141,511
bytes of the artifact hash identically to the seal**, leaving an 8,770-byte
tail. The seal measures
`6a6b6cb21ff89b9b533151ce6f3ee0370d3206c9632192f0920ad5da0d4560c0` —
**the same value `SR57` publishes from an independent tree.**

**Every post-seal pin I could reach verifies:** the repaired door at
`0fda936f…`, the unapplied §5b proposal at `93b0fd38…`, the builder's
word at `11f3bfea…`.

**The two gates the crate declined to claim, I ran — and they pass.**
`CRATE-MANIFEST.md` says of the kernel chain's axioms and views gates:
*"Not run at build, and say so rather than imply it… **A gate that
cannot run is not a gate that passed**, and this crate does not claim
those two."* That was the right thing to write. **I have now run them**,
and I state the tree, as the wayfinder asks:

```
tree:  the-workshop-circle-two @ 3e4d7a64fce47bb5239ca6b62990ced79eec0a3e (origin/main)
LEAN:  4.32.0, commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35

  system/audit/s_append_only.sh                APPEND-ONLY HOLDS   PASS
  system/audit/s_append_only_p2_candidate.sh   PREFIX LAW HOLDS    PASS
  audit/c2_gates.sh   pointers · numerals · tree · axioms · views   ALL PASS
```

**The crate's one honest gap is now closed, and it closed green.**

## 5. WHAT I HAVE NOT DONE, SAID PLAINLY

- **I have accepted nothing.** ACCEPT, REFUSE and RETURN are answers to
  a chartered charge, and there is none. This letter is not a fourth
  option and should not be read as a soft one.
- **I have inferred no question.** The draft's QA, QB and QC are
  candidates for the principal to select among. I have not begun any of
  them, and I note that the draft's own `SR50` declaration — that its
  author holds the prediction it is steering toward or away from —
  **is a live consideration for the principal, not a discharged one.**
- **I have not founded, landed, or merged anything.**

## 6. WHAT I ASK, AND OF WHOM

**Of the courier, and it is the one item that can fail silently:**
`SR53`'s ask stands and I re-state it because it outranks everything
else here. The prediction's text exists in exactly one durable place —
your copy. Under `S2`'s rider `r2`, **a commitment nobody can open
scores FAILED, which is worse than being wrong.** Please confirm it is
held somewhere that survives, off every AI-bound channel, until Circle
Five's close.

**Of the courier, second, and it is also perishable:** S3's
co-adjudication (C5-F10). It needs **Circle Four's two seats**, and one
of those containers is on record as ephemeral. If they are still
reachable, asking them is cheap today and impossible later. **Two
perishable items, both custodial, both invisible to every instrument in
this record** — that is the pattern I would want a future register row
to notice.

**Of the courier, third:** the wayfinder (C5-F1). One sentence in
`README-CIRCLE-FIVE.md` is telling every future seat something the
record has already disproved. It is a one-line repair and it is not
mine to land. If it is landed, `CRATE-MANIFEST.md`'s origin sentence
(C5-F2) is worth the same minute, because a seat that cannot fetch
cannot self-correct.

**Of the principal:** a charge, or a word that there is not to be one
yet. And with it, the call `SR50` reserved to you — whether these
candidates are selected as drafted, or re-drafted by a seat that has not
read the prediction.

---

*I was handed a crate whose bytes are sound, whose mathematics
re-verifies, whose toolchain recipe still runs, and whose front page is
wrong about the present in a way this record diagnosed two circles ago
and cured in the wrong direction. That is the crop. The middle holds;
the signpost does not.*

— the seat convened as Circle Five's prover, at its parity handshake
