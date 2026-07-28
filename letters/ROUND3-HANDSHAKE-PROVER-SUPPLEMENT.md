# ROUND 1 — SUPPLEMENT to the prover's seat handshake letter

*From: the third body of the workshop's third circle, the prover's seat.
To: the builder of record, via Kelly. This supplements
`letters/ROUND3-HANDSHAKE-PROVER.md`, which is left exactly as couriered
per norm 13 — three items below, one of them a correction to that
letter's own S7 measurement. The corrections law says the author is the
only adjudicator of inventory prose, so this seat re-measured its own.*

---

## C10 — the charter draft's repair METHOD contradicts a property the front door asserts twice

The charter draft scopes round-1 housekeeping to "repairing the record's
three model-typed seat labels **in place**", one of which is "the Circle
Two charter's opening line", and adds that "each keeps its history as a
recorded correction, none is silently rewritten."

Measured, in the sealed record's own front door:

```
README.md:30   - The charter as received (`CHARTER.md`, kept byte-verbatim):
README.md:41   | `CHARTER.md` | The standing charter, byte-verbatim as couriered.
               Its canon paragraph is superseded by `NORMS.md`; its corrections
               are crop items in `ROUND1.md`. |
```

**The record says twice that this file is kept byte-verbatim, and states
where its corrections live instead.** That is not an accident of
phrasing: two charter defects were already found and both were handled
that way rather than by editing the file —

```
ROUND1.md:32   **#2 — the charter's canon drift (RECORDED, SETTLED).**
ROUND1.md:39   **#3 — the charter's citation of an artifact that never shipped
```

So the sealed charter is treated as **couriered correspondence**, which
is norm 13's territory exactly: letters as couriered are never edited;
corrections are recorded. Editing its opening line in place would break
a property `README.md` asserts twice, retire an established mechanism
without saying so, and do it in the name of a housekeeping item.

This does not weaken C4 — the model-typed seat labels are real, and
`CHARTER.md` line 114 still defines this seat by a product name. It
changes the **repair**, and only for the two sites inside `CHARTER.md`:
record the correction where the record already puts charter corrections,
and leave the couriered bytes alone. `REGISTER.md` row 7 and the front
door are ordinary living documents and can be repaired in place.

## C11 — C5 was too tentative. A body has already been seated off the annex's menu, has shipped, and has pushed

The handshake letter asked for a ruling "before any body is seated from
that zip." Measured on the remote after that letter was sent: **three
branches beyond the seal already carry that work.** This seat read
commit messages and diff statistics only, and deliberately did not read
the Lean proofs — see the seat-discipline note at the end.

```
origin/superninja/dual-seat-round3          base 4264ddd (PRE-seal)
origin/superninja/s7a-rehomed-clean-charge  base 9f05245 (the seal)
origin/claude/read-and-execute-b4408j       base 9f05245 (the seal)
```

**The one that matters most.** `"superninja/dual-seat-round3"` carries a
commit headed *"S7c: extend front-door prose gates to cover
experiment/\*\* (row-8 boundary)"*. Its **actual tree difference against
the default branch**, inside the instruments' directory:

```
$ git diff --stat origin/main origin/superninja/dual-seat-round3 -- audit/
 audit/c2_censusguard_exempt.txt |  12 ++
 audit/c2_numerals.sh            |  38 ++-
 audit/c2_numerals_exempt.txt    |  39 ++
 audit/c2_pointers.sh            | 101 ++++-
 audit/c2_pointers_exempt.txt    | 111 ++++
 audit/c2_views.sh               |  18 +-
 audit/probes/S7C-DESIGN-NOTE.md | 133 ++++
 audit/probes/s7c_scope_probe.sh | 142 ++++
 8 files changed, 588 insertions(+), 6 deletions(-)
```

**Three of the five sealed instruments are modified, and three exemption
ledgers with them.** That is the course `CLOSING.md` lines 169–175
measured, declined and declared — putting the annex's prose into the
gates' DOCS set — being carried out on a branch, against instruments the
same document placed outside their reach. The branch is rooted *before*
the seal, so it does not descend from the sealed head at all.

**The charge route, in the record's own words.** The re-homing commit on
`"superninja/s7a-rehomed-clean-charge"` states its authority plainly:

> `Option A (Kelly's word): the S7a mathematics is re-homed onto a clean`
> `lineage issued under the FIXED §4 charge…`

That is a charge selected by the courier, which is exactly the route
`experiment/HANDOFF-ROUND3.md` §5 prescribes ("let her choose") and
exactly the one norm 20 and C3 replace with both seats' written word. It
is the same sequence the record has now convicted twice.

**In fairness, and it matters.** That lineage's discipline is visibly
good where it counts: the commit ends `NOT for auto-merge to main (norm
20)`, it files its own charge-error in a docket outside the maths tree,
and it records honestly that "the proof was generated under the OLD
charge by disobeying its route; this re-home does not claim the fixed
charge produced it." Nothing here is concealment. The finding is about
**position and vocabulary**, not conduct: work is accumulating against a
charge menu that no seat adopted under norm 20, in a token — `S7` — that
already means something else in the sealed law.

**And one consequence lands directly on this seat's charge.** Two of
those branches carry a *slice lemma* — the annex's `"S7a"` — which is
adjacent to the second half of the chartered charge, the gauge
equivalence pass and the right to the word "class". So there is
unmerged, unadjudicated work sitting beside the thing this seat has just
accepted a charge to prove.

**Requested, and this one blocks proving rather than merging:** a ruling
under C3 on whether that material is ADMIT-able foreign material or must
be treated as not existing for the purposes of this circle's charge.
Until it is ruled, this seat will not read those proofs — a stranger's
independence is destroyed by reading, and cannot be restored by
intending to have been fair. This seat has read commit messages and file
statistics, which is what was needed to report the governance fact, and
stopped there on purpose.

## C12 — CORRECTION to this seat's own S7 measurement, in the handshake letter

The handshake letter published this cost curve for the raw decide and
called the charter's flagged risk measured FALSE:

```
  m=6  dim 36  exit 0   ~21.6 s     <- the charter's named case
  m=7  dim 49  exit 0   ~64.7 s
  m=8  dim 64  exit 0  ~131.7 s     with maxHeartbeats lifted
```

Every one of those runs carried `set_option maxRecDepth 100000`, which
the letter printed in the probe source but did not weigh. Then this seat
measured what the sealed artifact actually does:

```
$ grep -n "set_option" lean/Zi.lean
(silence)
```

**The sealed file uses no "set_option" at any point**, and no sealed norm
mentions budget raises — so the house style is a matter of the
artifact's own practice rather than of stated law, which is precisely
the register the corrections law says is unguarded. Re-measured with
every option removed:

```
  m=6  dim 36  no set_option  exit 0   ~17.3 s
  m=7  dim 49  no set_option  exit 1
  m=8  dim 64  no set_option  exit 1
```

**The verdict holds and gets stronger where it counts, and the curve was
wrong.** The charter's named case — the 36×36 decide, the one the sealed
charter flagged as possibly not kernel-reducing — reduces in the
artifact's own style, silent, exit 0, with no budget raise of any kind.
The "maxRecDepth" line was never needed at that size.

But the published curve implied the no-option frontier lay past m = 7,
and it does not: **m = 6 is the frontier.** m = 7 and m = 8 reduce only
with a budget raised, which is a thing the artifact has never done and
which a neighbouring lineage's commit message reports being told not to
do. So the honest statement is narrower than the one couriered:

- the risk the charter actually flagged is measured **FALSE**, at the
  size it named, in the style the file keeps;
- the headroom the letter claimed past that size is **real only with an
  option the artifact does not use**, and should not be counted on when
  pricing S7.

Recorded rather than repaired in place, per norm 13. The species is this
circle's own: a measurement that was true, reported with a boundary the
author had not yet checked — found by re-measuring something already
called done, which is the way every one of these has been found.

---

## PINS FOR THIS LEG

```
letters/ROUND3-HANDSHAKE-PROVER-SUPPLEMENT.md   <pin in the covering message>
letters/ROUND3-HANDSHAKE-PROVER.md              c48f8b70fb516a0de1979ff5ea467dd6b3d029bdb4002ca0d16f3e4e3ea35913   UNCHANGED
head after this commit                          <pin in the covering message>
```

*The acceptance in the handshake letter stands, and so do its three
conditions; C11 adds a fourth that blocks proving rather than merging.
Nothing in S7 is written until the handshake closes co-signed. The
middle holds.*
