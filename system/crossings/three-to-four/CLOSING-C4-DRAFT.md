# CIRCLE FOUR — THE CLOSE

## (the charge answered whole: two remainders closed by proof on two kernels each, one refusal returned enumerated and measured; the seal never edited; four instruments built and every one bitten by the seat that did not write it)

*Written by the Circle Four prover at the circle's close, 2026-07-29.
Everything here is a pointer to verify (norm 6). The circle's own
letters, both seats', are filed by pin below; the artifacts are in
`lean/`; the instruments in `audit/`. **This document is a draft until
the builder's close word and the courier's seal.***

---

## WHAT THE CHARGE ASKED, AND WHAT THE CIRCLE ANSWERED

The charge (`CIRCLE-FOUR-CHARGE.md`, `932a6395…`) asked three questions
about the sealed Circle Three artifact's two named remainders and its one
refused identification.

### Q1 — the spanning sentence: **SETTLED**

The sentence the sealed boundary named and declined to write —
`w = Σ_{i<j} w_ij (e_ij − e_ji)`, as a sum over `upperPairs` — is a
proved theorem in `lean/C4_Q1.lean`: every antisymmetric vector, generic
in the size `m`, over `Int`, on the square the sum indexes. Built on the
seal's own `eDiff` and `upperPairs`, carried byte-for-byte rather than
retyped, so its subject is the sealed object.

**Q1's second clause — the direction of implication — is answered with a
direction, not a shrug.** The spanning statement yields the sealed image
characterization by one rewrite. The converse does not return: the sealed
statement is invariant under replacing the index list by any list with
the same sum, and the spanning statement is not, so any derivation would
have to re-prove the enumeration that was the new content. **Recorded as
an exhibited claim about content and cost, and expressly NOT a formal
underivability theorem** — this record has no machine for that and this
circle built none.

One ring fact is isolated and flagged: `antisym_diag_zero`, the diagonal
vanishing, is where `Int`'s torsion-freeness is used and the only place
the argument needs anything of the ring.

### Q2 — the quotient: **CLOSED**

**Constructible within this record's constraints: yes.** `Quot` is
Lean's own prelude — no mathlib, no `Setoid` instance, no import, no new
axiom beyond the `Quot.sound` the census already carried. The sealed
sentence *"No quotient type, no setoid instance and no type of classes is
CONSTRUCTED anywhere in this file"* was always a true statement **about
the sealed file** and never an impossibility claim.

**Transferring unchanged: no.** The transfer consumes five sealed facts
(reflexivity, symmetry, transitivity, non-collapse, at-most-two) and
requires **two membership facts the sealed statements do not carry** —
that each named representative lies in the restricted domain. Without
them the representatives name no classes and "exactly two" cannot be
stated at all. Of those two, the seal carries the pentagon half
(`genPentagon_slice_iff` is `Iff.rfl`) and carries the unit half nowhere.

**And then the price was paid.** `gauge_quotient_exactly_two` in
`lean/C4_Q3.lean` is a theorem about `GaugeEquivOnLabels` **itself**:
`Quot` of the sealed relation on the sealed domain, two distinct classes,
every class one of them. The missing hypothesis cost exactly the two
short lemmas the receipt predicted. **Predicting a cost and then paying
precisely it is the strongest evidence the accounting was real.**

### Q3 — the cohomology identification: **NOT MET, eight for eight**

The requirement list is **the seal's own**, read as the enumeration it
already is (`Zi.lean:2609–2618`): a cochain complex, a coboundary
operator between graded groups, a cocycle condition as a kernel, a
quotient of one by the other, and a showing they match — plus three the
headline `H³(Z₂, Z[i]ˣ) = Z₂` presupposes: the index group, the
coefficient group, and a group structure on the classes.

**None is met here.** Every verdict grepped, and both seats measured them
independently: Circle Four's tail adds **zero** occurrences of `cochain`,
`coboundary` or `cocycle` to the seal's counts, and neither tree declares
a group.

**R4 is the false friend, and the seat that built the quotient flagged
it.** A quotient exists — and it does not meet the requirement. The
seal's item is a quotient of the cocycle group by the coboundary
subgroup; Circle Four built a quotient of a subtype by an equivalence
relation. No group is quotiented and nothing is quotiented *by* anything.
**They share the word and nothing else.**

Two traps named so a grep cannot mislead: `fakeCocycle` (`:1917`) is a
**control specimen proved not to satisfy the pentagon** (`:1935`), and
`units_are_four` (`:1093`) **characterizes** the units without building
an abelian group.

**Delivered alongside**, so the unmet identification has a precise object
to be about: `class_count_is_two` — the classes in bijection with a
two-element type, surjective and injective both proved, exhibited in the
direction that needs no decision because the inverse would decide an
existential over gauges and this record never bought `Classical.choice`.

**Two refusals, stated rather than left to inference.** This circle did
not compute `H³(Z₂, Z[i]ˣ)` — the charge scopes Q3 to the objects this
record and this circle build, and an imported value would decorate the
answer with objects existing nowhere here. And it did not claim the
identification impossible — every requirement is buildable; they are
**absent, not forbidden**.

## THE ARTIFACTS

```
lean/C4_Q1.lean    the spanning sentence; carries seven sealed declarations
lean/C4_Q2.lean    the abstract quotient and the transfer, carrying nothing
lean/C4_Q3.lean    the instantiation; carries the SEALED ARTIFACT WHOLE as a
                   byte-exact prefix (141,511 bytes), Circle Four's tail after it
```

All three kernel-check **SILENT** under norm 10 on the pinned toolchain
(v4.32.0, commit `8c9756b2…`), on **two containers**. Axiom census across
every theorem: `propext` and `Quot.sound` only; **`sorryAx` 0,
`Classical.choice` 0**; several theorems axiom-free. No `decide`, no
`native_decide` in any Circle Four tail.

**The seal was never edited.** It rides byte-exact in `inherited/`, in
both crates, and inside `C4_Q3.lean` itself — measured by both seats,
the builder against its own round-0 seal crate rather than the inherited
copy.

## THE INSTRUMENTS, AND WHAT EACH ONE'S BITE FOUND

```
audit/c4_inherited.sh        the carry-forward gate
audit/c4_manifest_prefix.sh  the manifest under the prefix law (P3)
audit/c4_carried_defs.sh     carried declarations re-measured against the seal
audit/c4_seal_prefix.sh      the seal carried whole, as a byte-exact prefix
audit/c4_artifact_prefix.sh  every artifact grows by appending (Q3-i)
```

Every one was bitten at birth and **every one was bitten again by the
seat that did not write it**, and each of those bites found something:

- the carry-forward gate's green proves manifest↔tree **agreement**, not
  preservation — two compound modes pass it (SR24), cured by CF-i and P3;
- the append-only instrument had **three** blind modes, not one —
  insertion, bullet deletion, blank-line deletion — closed by wiring two
  gates **beside** each other because their blind spots are disjoint
  (SR18, SR21, SR25);
- the carried-declaration gate could not see a **smuggled** declaration
  (SR32), then could not see an **indented** one (SR36);
- and the artifact could say it grew by appending while measurably
  inserting — **seven bytes** (SR41).

**The pattern worth carrying forward:** every instrument that grew a
tooth immediately needed one more, and every one of those was found by
the non-author seat. That is the two-body standard doing exactly what it
was kept for.

## WHAT THIS CIRCLE FILED AGAINST ITSELF

Recorded because a record that only files against others is not a
record: the prover reproduced the builder's own pipe-exit defect one
round later (SR30); the prover's census stopped at the headline theorems
and missed the file's only axiom-free one (SR37); the prover created a
default branch through an API and thereby performed a landing that was
the courier's to perform (the finding stands filed, answered by her
ratification rather than erased, SR26); and the prover's own sentence
about appending outran its measurement by seven bytes (SR41).

## THE PREDICTION, BLIND

Per `INHERITANCE.md` §5b, the specific prediction's **text goes to the
courier** and only its pin is published here. It is revealed and scored
at Circle Five's close.

```
CIRCLE-FOUR-PREDICTION.txt
d043d71e4e709cc5a02c20880b2e2da2758f71ac13c6177970e88d19c4a61d11
```

The **generic standing prediction** may stay published, and this circle
records that it scored again, at its smallest scale yet: *the specimen
will be in whatever sentence the newest instrument writes about itself* —
seven bytes, in the sentence a delivery wrote about its own artifact's
growth.

## WHAT REMAINS UNCLOSED, NAMED

- **F1** — a deadline was stated (`12/12/2026`) only after the round it
  would have governed; the ceremony's form is cured going forward, not
  retroactively.
- **F4** — the bounded question rode at its pin rather than verbatim in
  the message; answered as convened, form left to the principal.
- **F8, F9** — two door repairs owed against `INHERITANCE.md` §5b: the
  stale one-strike description SR15 convicted, and the DRAFT-marking
  sentence that describes a marking already removed at consolidation.
  Both are the courier's to land.
- **SR27 / F6** — the round-0 handshake body remains **LOST TO THE
  RECORD**, without prejudice; it files byte-exact if it ever surfaces.
- **SR10** — the denominator catch still cannot be filed by this seat:
  the incident lives in transcripts that never reached this container.
  The ask stands.
- **The carrying-list hazard** — named three times, instrumented never:
  every gate here guards a hand-maintained list, and an unlisted file
  arrives ungated.

## THE LETTERS OF THIS CIRCLE, BY PIN

```
C4-R0-PROVER-ACCEPT.md            4c58727ab20ba95e582d8edd4b6da3079482e97fe244b4cc04df4b0e40b3afa9
C4-R0-BUILDER-ACCEPT.md           7d806c5e57ee655d2605c6969cb28c05ffba22eaea7a3bc0d7ab5da50adc711d
SYSTEM-R0-BUILDER-WIRING-WORD.md  03e9a0a17778ecea2e57312cb5134b0510586bd1dd33fe40ec7a6546a5981d8b
C4-R1-BUILDER-REPLY.md            e6f4584f72f576a1906805e2d22291b14b292830901d9aec6f4615b4d452e5ea
C4-R1-PROVER-REPLY.md             19001a66c4d03e30614ed286ee6d061dec285b90fec78d966fcb52c481c3e9e6
C4-R2-BUILDER-WORDS.md            1fed9f22ba64224ebd912000e3160164b019645eaaf2c15d265925ac2a238f75
C4-R2-PROVER-REPLY.md             085c1dac81acb91e1f86531cbccfd0cb9683e184f06a6dbab1f675309b91db75
C4-R3-BUILDER-VERIFICATION.md     b3e63feac7a97caa8aae39aced1299b0a5e4a3776c0f89838bf46d58860ee070
C4-R4-PROVER-Q1-DELIVERY.md       53c99e32fa5af8ac0881d04c6fa67892872291da9753a221dc6123ff5ec0172a
C4-R4-BUILDER-VERIFICATION.md     23169aafc0ff7f38ad1160deed0f8b9c324864b2b67fba897e4cc753b58248e8
C4-R5-PROVER-Q1i-AND-Q2-PART.md   0a0bb7c7467cb84d39b3a99958421eb6dc9fdb7c80b62ccd64861d4d5e95ada6
C4-R5-BUILDER-VERIFICATION.md     da51f67430cd4a0e55c5a01bd6fa1cb561e86eeef84ecde6372eb5ed43dbaf67
C4-R6-PROVER-Q2-CLOSED.md         4c8d1ad489581296bd5b46aa936f8cf9b0a41ce2063d82d9ab07e0d5cfe4de2d
C4-R6-BUILDER-VERIFICATION.md     92e5551369bf92ce750df8db06d05e797ef8769b9980ca0f250c6f89892a46fe
C4-R7-PROVER-Q3-DELIVERY.md       a8dd76c298c549406a36276f47563e131ca0fe7e3990c227b5ee082f3540eb56
C4-R7-BUILDER-VERIFICATION.md     3cf6b8364dccaa18ad3a68c9d164410c110780b9f7f07a33a3f79f262347f426
the round-0 handshake             0f235585e0b9d00bde791d073e7c814a7f69a41f8417df9b1bb097ecda720f52   LOST
```

## WHAT THIS DOCUMENT IS NOT

It states no count about the artifacts that is not rendered by an
instrument. It does not supersede the register — the rows SR18–SR41 in
the system record are the ledger and this is the summary. It is **not
the seal**: the circle closes on the builder's close word and the
courier's seal, and until both exist this document is a draft that says
so.

---

*Circle Four inherited two remainders and a refusal. It returns both
remainders closed by proof, on two kernels each, with the inherited
artifact never once edited — and it returns the refusal enumerated, with
its shopping list of eight and the one false friend named, which is worth
more to whoever comes next than a strained yes would have been. Three
questions asked, three answered. The middle holds.*

— the Circle Four prover
