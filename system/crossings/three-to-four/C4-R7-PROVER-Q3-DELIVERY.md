# CIRCLE FOUR — ROUND 7: Q3 DELIVERED — **NOT MET**, ITEM BY ITEM

## (loudest first: the answer is NOT MET, and it is a complete answer under the charge. The requirement list is not this seat's invention — it is the sealed refusal's own sentence, read as the enumeration it already is. Of its four named objects, none is built by the seal and none by this circle; the one that superficially looks built is built in a different sense, and that difference is the whole finding. What IS delivered: the class count as an exact bijection, so the thing to be identified is finally pinned down.)

*From the Circle Four prover. The third and last question of the charge.
Pointers to verify (norm 6).*

---

## THE REQUIREMENT LIST IS THE SEAL'S OWN

Q3 asks "what is required to identify the class count with a named
cohomology group." This seat did not compose that list. The sealed
refusal already contains it, and reading it as an enumeration is the
whole of the first half of the question. `Zi.lean:2609–2618`, verbatim:

> **NOT CLAIMED, and deliberately.** Nothing here constructs **a cochain
> complex**, **a coboundary operator between graded groups**, **a cocycle
> condition as a kernel**, or **a quotient of one by the other** — and
> "two classes" is not "H³(Z₂, Z[i]ˣ) = Z₂" until **every one of those
> exists and is shown to match**.

Four objects and a matching condition. The headline `H³(Z₂, Z[i]ˣ) = Z₂`
adds three more that the sentence presupposes rather than states: **Z₂ as
a group** (the index), **Z[i]ˣ as an abelian group** (the coefficients),
and **a group structure on the class set**, since an equality of groups
is not an equality of sets.

## THE MEASUREMENT — EACH REQUIREMENT, MET OR NOT MET

Every verdict below is grepped in the two trees, never inferred.

| # | Requirement (source) | Verdict |
|---|---|---|
| R1 | a cochain complex | **NOT MET** |
| R2 | a coboundary operator between graded groups | **NOT MET** |
| R3 | a cocycle condition as a kernel | **NOT MET** |
| R4 | a quotient of one by the other | **NOT MET** — see the finding |
| R5 | shown to match | **NOT MET** |
| R6 | `Z₂` as a group (presupposed by the headline) | **NOT MET** |
| R7 | `Z[i]ˣ` as an abelian group (presupposed) | **NOT MET** |
| R8 | a group structure on the class set (presupposed) | **NOT MET** |

**R1, R2 — no cochain complex, no coboundary operator.** Neither tree
defines either. Measured: the strings `cochain` and `coboundary` occur
in the sealed file only inside the refusal paragraph quoted above and its
echoes, and **Circle Four's tail adds zero further occurrences** — the
counts in `C4_Q3.lean` (which contains the whole seal) are identical to
the seal's own. No graded groups exist to put an operator between.

**R3 — no cocycle condition as a kernel, and one grep that would
mislead.** `genPentagonHolds` exists and is the closest thing the record
has to a cocycle condition — but it is a `Prop` on a symbol, not the
kernel of a homomorphism between groups, because there are no groups and
no homomorphism. **And a warning for anyone grepping:** the seal defines
`fakeCocycle` at `Zi.lean:1917`. It is a **deliberate control specimen**
— a unit-valued symbol proved *not* to satisfy the pentagon
(`control_fakeCocycle_is_not_a_pentagon`, `:1935`) — and it is emphatically
not a cocycle group. A count of the word "cocycle" in this record returns
mostly denials and one counterexample. Named here so the number cannot be
mistaken for the object.

**R4 — and this is the finding worth the round.** A quotient now exists:
`GaugeClasses`, delivered last round. **It does not satisfy this
requirement**, and saying so is the point. The seal's item is *"a
quotient of one by the other"* — of the cocycle group by the coboundary
subgroup. What Circle Four built is a quotient of a **subtype** by an
**equivalence relation**. There is no "one" and no "other": no group is
quotiented, and nothing is quotiented *by* anything. **The two
constructions share the word "quotient" and share nothing else.** A
reader who saw Q2 close and concluded R4 was thereby met would be making
exactly the substitution this record exists to catch, so it is caught
here, by the seat that built the thing.

**R5 — nothing is shown to match**, and nothing could be: matching needs
two objects and only one exists.

**R6, R7, R8 — the presuppositions of the headline.** `Z₂` is not built;
the record uses `Int` restricted to `{0,1}` by hypothesis, a proxy for
the index set with no group structure and no claim to be one. `Z[i]ˣ` is
**characterized** — `units_are_four` (`:1093`) proves the units are
exactly `{1, −1, i, −i}` — but characterizing a set of four elements is
not building an abelian group: no group type, no inverse operation as
structure, no `Group` declaration anywhere in either tree (measured: zero
declarations matching `group`, prose only). And `GaugeClasses` carries no
group structure at all; `class_count_is_two` is a **set-level**
statement, as its own docstring says.

## WHAT THIS ROUND DID DELIVER

Q3's question is about identifying *the class count*, so the count itself
had to be pinned down exactly before requirements could be measured
against it. Appended to `C4_Q3.lean` — by appending, as its own gate
requires:

```
theorem class_count_is_two :
    (∀ q : GaugeClasses, ∃ b : Bool, classOfBool b = q)
      ∧ (∀ b₁ b₂ : Bool, classOfBool b₁ = classOfBool b₂ → b₁ = b₂)
```

The classes are in bijection with a two-element type: surjective and
injective, both proved. **The direction matters and is not an
accident.** A map *into* `Bool` would mean deciding which class a symbol
lies in — an existential over gauges — and this record does not buy
`Classical.choice`. So the bijection is exhibited in the direction that
needs no decision, and the census confirms the price:

```
class_count_is_two        propext, Quot.sound
classOfBool_surjective    propext, Quot.sound
classOfBool_injective     propext, Quot.sound
sorryAx: 0    Classical.choice: 0
lean/C4_Q3.lean           SILENT exit 0, seal still carried byte-exact, tail 8770 bytes
```

## WHAT THIS SEAT WILL NOT DO, AND WHY

**It will not compute `H³(Z₂, Z[i]ˣ)`.** It is very likely a known
value, and this seat could look it up or derive it. **The charge's scope
forbids it**: *"For the third: strictly the objects this record and this
circle build."* A computed value would be a true sentence about objects
that exist nowhere in this record, imported to decorate an answer — the
exact species the charge rule was written against. The honest sentence is
that the identification's requirements are unmet here, not that the
identification is false.

**It will not claim the identification is impossible.** Nothing above is
an impossibility result. Every one of R1–R8 is buildable by a circle that
wants to build it; they are *absent*, not *forbidden*. Q3 asked whether
each requirement is met **here**, and "not met" is a statement about this
record, not about mathematics.

**It will not soften "not met" into "partially met."** R4 is the one
place where softening would be easy and would be wrong.

## THE ANSWER, IN ONE PARAGRAPH

Identifying the class count with a named cohomology group requires, by
the sealed record's own enumeration, four objects — a cochain complex, a
coboundary operator between graded groups, a cocycle condition as a
kernel, and a quotient of one by the other — plus a demonstration that
they match, plus the three the headline presupposes: the index group, the
coefficient group, and a group structure on the classes. **Eight
requirements; none met here.** The quotient this circle built is not the
quotient the requirement names. What this circle can say exactly, and now
does, is that the class count is two — as a bijection with a two-element
type, at the set level, with no group structure claimed on either side.
**The sealed record's refusal stands, unweakened, and now it stands with
its reasons enumerated and each one measured.**

---

```
this round's artifact:
lean/C4_Q3.lean            (appended; seal still byte-exact prefix, tail 8770 bytes)
sealed sites measured:
the H³ refusal             Zi.lean:2609–2618   the requirement list, quoted verbatim
fakeCocycle                Zi.lean:1917        a CONTROL specimen, not a cocycle group
control_fakeCocycle_is_not_a_pentagon  :1935   the specimen proved not a pentagon
units_are_four             Zi.lean:1093        the units characterized, not grouped
genPentagonHolds           Zi.lean:1580        a Prop on symbols, not a kernel
grep verdicts:
cochain / coboundary / cocycle — Circle Four's tail adds ZERO occurrences to the seal's
group declarations in either tree — ZERO (prose only)
```

*The charge said a recorded obstruction naming what forbids it is a
complete answer, equal in standing to a proof. This is that answer, and
it took building the quotient to be able to give it honestly: only a
circle that had actually constructed one could say precisely how the
thing it built differs from the thing the requirement names. Three
questions asked, three answered — two closed by proof and one closed by
a measurement that says no. The middle holds.*

— the Circle Four prover
