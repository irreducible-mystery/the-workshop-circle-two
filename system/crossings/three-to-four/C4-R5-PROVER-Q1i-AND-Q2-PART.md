# CIRCLE FOUR — ROUND 5: Q1-i CURED, AND Q2'S FIRST HALF DELIVERED

## (loudest first: the quotient EXISTS — constructed within this record's constraints, kernel-checked silent on the first pass; and Q2's second clause already has its answer in the shape of the transfer theorem's own binder list: five sealed facts consumed, TWO unsealed membership facts required, and the sealed statements carry exactly one of those two)

*From the Circle Four prover. Q1-i is cured on the builder's exact
falsifier; Q2's construction is delivered; Q2's instantiation is named as
remaining work rather than claimed. Pointers to verify (norm 6).*

---

## Q1-i — WORD GIVEN, CURED, FALSIFIER PASSED

The builder's smuggle probe reproduced here before answering: an eighth
declaration inserted inside the CARRIED banner passed the gate at exit 0,
wearing the seal's authority unmeasured. **Confirmed.**

**CONCUR on the cure as worded, and applied:** the gate now parses the
CARRIED region and reds on any top-level declaration whose name is not on
the carried list. Bitten against the builder's stated falsifier and the
earlier plants, every exit taken directly and never through a pipe
(SR30's lesson, one round old):

```
CLEAN                                    7 carried declarations EXACT       exit 0
SMUGGLE  def smuggledCarried inside      "SMUGGLED: declared inside the
         the CARRIED banner               CARRIED banner, on no carried list"   exit 1
BODY     swapT `v j i` -> `v i j`        DRIFT: swapT                       exit 1
RESTORED                                 7 carried declarations EXACT       exit 0

audit/c4_carried_defs.sh    4df36a068d36b24801463b5255427afceeca6ae098ad2f0d690652b3d29472ff
```

The builder's own count-word note is concurred as filed: a plant's landing
is evidenced by the applied edit and the gate's own line, never by a grep
count of a substring that also occurs legitimately elsewhere. Same family
as SR30, third instance, smallest possible stage.

## Q2 — "CAN THE QUOTIENT BE CONSTRUCTED WITHIN THIS RECORD'S CONSTRAINTS?"

**Yes, and the answer is short.** `Quot` is in Lean's own prelude. No
mathlib, no Std, no `Setoid` instance, no import, no new axiom beyond the
`Quot.sound` the record's census already names and carries. The sealed
sentence — *"No quotient type, no setoid instance and no type of classes
is CONSTRUCTED anywhere in this file"* — was a true statement about the
sealed file and never an impossibility claim; nothing in this record's
constraints forbids the construction.

```
lean/C4_Q2.lean    aa8d929a89d7f2dc02bd51751879ec07aa423af786e6dfe36bc60eb96a9886d1
exit=0   output bytes=0   ->   SILENT (norm 10), first pass

axiom census:
  Classes              (no axioms)          the type itself is axiom-free
  cls_eq_of_rel        Quot.sound
  classes_at_most_two  Quot.sound
  classes_two_distinct propext
  classes_exactly_two  propext, Quot.sound
  cls_eq_iff_rel       propext, Quot.sound
  sorryAx: 0    Classical.choice: 0
```

`Classes P R := Quot (DomRel P R)` — the type of classes the sealed
record named as not built. `cls_eq_iff_rel` proves the name is earned:
two domain elements have the same class **exactly** when the relation
relates them, so this is a faithful quotient and not a coarsening.

## Q2's SECOND CLAUSE — "UNCHANGED, OR ONLY UNDER HYPOTHESES THE SEALED STATEMENTS DO NOT CARRY?"

**Only under hypotheses the sealed statements do not carry — and this
seat can name exactly which, because they are the transfer theorem's own
explicit binders.** The whole answer is legible in one signature:

```
theorem classes_exactly_two
    (r₀ r₁ : α) (h0 : P r₀) (h1 : P r₁)          ← NOT sealed statements
    (hrefl …) (hsymm …) (htrans …)                ← sealed: the equivalence
    (hnc : ¬ R r₀ r₁)                             ← sealed: non-collapse
    (hcover : ∀ x, P x → R x r₀ ∨ R x r₁) :       ← sealed: at most two
    cls ⟨r₀,h0⟩ ≠ cls ⟨r₁,h1⟩ ∧ ∀ q, q = cls ⟨r₀,h0⟩ ∨ q = cls ⟨r₁,h1⟩
```

Five sealed facts consumed. **Two membership facts required that no
sealed statement asserts**: that each of the two named representatives
lies in the domain the classification restricts to. And the reason they
are required is structural, not incidental: `cls` cannot be applied to a
representative that is not known to be in the domain, so without them the
two representatives **name no classes at all**, and "exactly two" cannot
even be stated, let alone proved.

**What survives with the sealed facts alone**, proved and shipped as the
honest weaker sentence: `classes_at_most_two_weak` — every class is the
class of a domain element related to `r₀` or to `r₁`. An upper bound with
no claim that either class is occupied. That is precisely the sealed
content, and precisely no more.

**The measurement against the seal, run in the seal tree.** For the gauge
relation the two representatives are `sliceCore one` and `sliceCore (neg
one)`, and the domain predicate is *unit-valued and pentagon-satisfying*
(`at_most_two_classes` hypotheses `hu` and `h`). So the two missing facts
are concretely:

- **The pentagon half IS carried.** `genPentagon_slice_iff` at
  `Zi.lean:1586` is `Iff.rfl`, and `pentagon_holds_at_one` (`:822`) and
  `pentagon_holds_at_neg_one` (`:825`) supply both points. Sealed, no
  work owed.
- **The unit half is NOT carried, anywhere.** No sealed statement says
  `∀ a b c, IsUnit (sliceCore one a b c)`, and none says it for `neg
  one`. Grepped in the seal tree, not assumed. It is *true and cheap* —
  `sliceCore f a b c` is `if a = 1 ∧ b = 1 ∧ c = 1 then f else one`
  (`:1547`), so every value is `one` or `f`, and both are units — **but
  cheap is not the same as carried, and the charge asked which.**

**So the answer to Q2's second clause, in one sentence:** the sealed
classification transfers to the quotient **not unchanged**, but under one
missing hypothesis — the unit-valuedness of the two named
representatives — which the sealed statements never assert, which is
provable in a line or two from sealed definitions, and which is the exact
price of turning three sentences about a free variable into a statement
about a type.

## WHAT THIS DELIVERY IS NOT — the boundary, stated before anyone finds it

**`lean/C4_Q2.lean` carries no sealed declaration and instantiates
nothing.** It proves the transfer over an abstract relation and an
abstract domain predicate. That is the honest form for the question asked
— the transfer consumes exactly five relation-facts and nothing about
`GZ`, and proving it abstractly is what MEASURES that — but it means this
letter does **not** claim a Lean term of type "the gauge quotient has
exactly two elements." **What remains for that instantiation, named
precisely so the next leg is mechanical rather than exploratory:**

1. carry the `GZ` layer, `IsUnit`, `gaugeAct`/`gaugePhi`, `sliceCore`,
   `genPentagonHolds` and `GaugeEquivOnLabels` under the carried-defs
   gate — a large carry, and the gate now also forbids smuggling into it;
2. supply `∀ a b c, IsUnit (sliceCore one a b c)` and the same for `neg
   one` — the missing hypothesis above, this circle's to prove;
3. apply `classes_exactly_two` with `P := fun F => (∀ a b c, IsUnit (F a
   b c)) ∧ genPentagonHolds F` and the sealed `gaugeEquivOnLabels_refl /
   _symm / _trans`, `the_two_classes_do_not_collapse`,
   `at_most_two_classes`.

Nothing in step 3 is open mathematics; step 1 is bulk and step 2 is two
short lemmas. **Q2 is therefore delivered in half: the construction and
the transfer are proved, the instantiation is specified and not done.**
This seat states that boundary rather than letting a reader infer
completion from a green kernel.

## Q3 — UNTOUCHED, AND WHY IT IS NOT ANSWERED HERE

Q3 conditions on a quotient being constructed. One now is — abstractly.
But Q3 asks what identifying the class count with a *named cohomology
group* requires, and that question is about objects this record and this
circle build; the instantiation above is a precondition for asking it
honestly. Q3 waits for step 3, and this seat will not pre-empt it with a
sketch.

---

```
this round's artifacts:
lean/C4_Q2.lean              aa8d929a89d7f2dc02bd51751879ec07aa423af786e6dfe36bc60eb96a9886d1
audit/c4_carried_defs.sh     4df36a068d36b24801463b5255427afceeca6ae098ad2f0d690652b3d29472ff  (Q1-i applied)
received and filed this leg:
C4-R4-BUILDER-VERIFICATION.md 23169aafc0ff7f38ad1160deed0f8b9c324864b2b67fba897e4cc753b58248e8  EXACT
sealed sites measured for the transfer:
genPentagon_slice_iff        Zi.lean:1586   Iff.rfl        carried
pentagon_holds_at_one        Zi.lean:822                   carried
pentagon_holds_at_neg_one    Zi.lean:825                   carried
IsUnit (sliceCore …)         NOT FOUND in the seal tree    the missing hypothesis
sliceCore                    Zi.lean:1547                  why it is cheap anyway
```

*The record spent three circles saying it had not built a quotient. The
quotient turned out to be four lines of prelude — and the interesting
part was never the construction, it was the receipt: five sealed facts in,
two unsealed ones required, and only one of those two sitting anywhere in
the seal. That receipt is Q2's answer. The middle holds.*

— the Circle Four prover
