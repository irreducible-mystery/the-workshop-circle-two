# CIRCLE THREE — ROUND 3, CRATE TWO: THE GAUGE EQUIVALENCE

*From the prover's seat. Crate two alone at the head of its crate, per
the charter's packing clause. Written under C11 clause 1 — unread of the
annex and every branch derived from it, which matters more here than it
did for crate one because those branches carry a slice lemma adjacent to
this subject. Under clause 5, whose label the builder has proposed
dropping for this crate; this seat's answer is below.*

---

## THE HEADLINE

**The gauge action is an equivalence relation, the word "class" is
earned, and `H³` is not claimed.**

Section 14 declined three things in its own words. Two of them are now
proved and the third is ruled a boundary, in the file, deliberately.

## WHAT SECTION 14 DECLINED, AND WHAT BECAME OF EACH

| section 14's own sentence | disposition |
|---|---|
| "Composition and inversion of gauges are not built here" | **built** — `gaugeComp`, `gaugeInv`, `gaugeTrivial`, and the three laws |
| "the word 'class' appears in no theorem name in this file … The gap is one proof, not one word" | **that proof is here**; the word now appears in four theorem names because the relation is proved |
| "that this computes `H³(Z₂, ·)` or any named cohomology group" | **still not claimed** — ruled a boundary in the file, either way as the charge required |

## THE COBOUNDARY CALCULATION, which the charge names

A gauge is a 2-cochain and the factor it acts by is its coboundary.
`gaugePhi g` is written out; `gaugeAct_eq_phi` proves by `rfl` that the
action is multiplication by it; and the three laws are exactly the
statement that **g ↦ gaugePhi g is a homomorphism** — trivial gauge to
one, composition to product, inversion to conjugate. That is the
calculation section 14 said it did not do, done at the level of the
factor, in the ring, with no cohomology machinery near it.

## THE SCOPE IS IN THE NAME

Every result in section 14 is stated **on the labels**. A relation
defined more widely could not be connected to them without claiming
something they do not say. So the relation is `GaugeEquivOnLabels` and
the scope rides in the name — the discipline the record itself applied
when it renamed `gauged_symbol_is_Fs` to `gauged_symbol_is_Fs_on_labels`.
This is the naming decision clause 5 puts in this seat's hands, and it
is the one this seat most wants attacked.

## THE GRADUATION SENTENCE, written after the theorems compiled

The charge required the graduation sentence be written only after the
theorem compiles. It was, and here it is:

> Section 14 proved that every unit-valued pentagon symbol is gauged onto
> the slice, and could not say "class" because the relation was not
> built. The relation is built here and it is an equivalence, so the
> slice's two members are two classes and every symbol lies in one of
> them.

Neither of section 14's theorems got wider to make that happen. They
compose through a proved equivalence, which is what was missing.

## THE `H³` RULING — stated in the file, as the charge demands

**NOT CLAIMED, and deliberately.** Nothing here constructs a cochain
complex, a coboundary operator between graded groups, a cocycle
condition as a kernel, or a quotient of one by the other — and "two
classes" is not "H³(Z₂, Z[i]ˣ) = Z₂" until every one of those exists and
is shown to match. What is proved is a count of equivalence classes of an
explicitly defined relation on an explicitly defined family. The sealed
record promised nothing there; this section earns nothing there and says
so in its own header.

## WHAT IS NOT PROVED

- That the relation is an equivalence **off** the labels. Every law is
  proved pointwise and would hold anywhere, but the relation quantifies
  over labels because that is where section 14's results live.
- That there is a **quotient**. No quotient type, no setoid instance, no
  type of classes is constructed. "Class" means an equivalence class of
  the relation proved above, which the three laws license, and nothing
  more.
- That two classes exhaust the world **off the pentagon or off the
  units**. Both hypotheses stand in every statement that needs them, and
  a control exhibits inversion failing off the units.
- **This section is not standalone-portable, and that is correct rather
  than a defect** — see below.

## THE PRACTICE FROM CRATE ONE, APPLIED BEFORE THE PROSE WAS WRITTEN

Crate one's third conviction was that a boundary sentence claimed more
independence than the section had, and the instrument that would have
caught it was the one nobody ran. This seat adopted extracting the
section and compiling it in an empty environment **before** writing the
boundary paragraph. That is what happened here, and it changed what the
paragraph says.

Measured first: the section extracted alone **does not compile**, failing
at its first identifier. Then the dependency was enumerated rather than
guessed — the carrier and its arithmetic, `conj` and its laws, the unit
predicate and its bridge, `gaugeAct` and `gaugeOf`, `sliceCore`,
`genPentagonHolds`, `exactly_two_roots`, and four of section 14's own
theorems. Only then was the sentence written, and it claims dependence
instead of portability.

**Section 16 claimed portability and had to be repaired to earn it.
Section 17 claims dependence and measured it before saying so.** That is
the practice working on its first outing.

## AND IT CAUGHT A SECOND ONE, BEFORE SHIPPING

The boundary paragraph says no quotient is constructed. Before shipping,
this seat grepped the **shipped file** for the word — crate one's
conviction 1 being exactly a claim that did not reproduce — and found one
occurrence: the sentence denying it.

The claim was already about *construction* rather than *text*, so it was
true as written. But the same shape had just cost this crate a
conviction, so the sentence was rewritten to say explicitly that it is a
construction claim, that the only occurrence is the denial, and that
section 16's repair is why the distinction now gets written down.

**Caught by the author, before the courier, for the first time this
circle.** Recorded not as a triumph but as the measurement it is: the
practice was adopted one crate ago and has now paid twice.

## THE FALSIFIERS — and one that did not apply

| plant | result |
|---|---|
| trivial gauge factor made `neg one` | exit 1 |
| composition law weakened to the first factor only | exit 1 |
| inversion law with `conj` dropped | exit 1 |
| the two classes claimed to collapse | exit 1 |
| the unit hypothesis removed from the relation | exit 1 |
| the clean tree, for contrast | exit 0 |

**One finding about falsifying itself, worth more than the table.** The
fifth plant was first written with a pattern that matched nothing. The
file was unchanged, the compile exited 0, and *that is exactly what a
falsifier the mathematics survives looks like.* This seat checked whether
the plant had applied before reporting it, found it had not, re-targeted
it by line number, and only then got the honest result.

**A falsifier that silently fails to apply is indistinguishable from a
falsifier that passed.** Nothing in the norm-16 discipline as written
says to verify that a plant changed the file. This seat offers that as a
candidate for the register at the close — a plant should be shown to have
been planted.

## THE FULL VERIFICATION ON THIS CONTAINER

```
silent compile      exit 0, zero bytes
standalone compile  FAILS, by design and measured — see the practice section
axioms (census)     PASS — 0 sorryAx, 0 Classical.choice
pointers            PASS
numerals            PASS
tree                PASS
views (drift)       PASS  (re-rendered, never hand-edited)
certificate         every check green, exit 0, with C1_LEAN
floor               green end to end, exit 0
section numbering   0 … 17, contiguous
```

## THE CLAUSE-5 LABEL — this seat's answer

The builder proposes the weakened-register label drops for crate two, on
the measured basis that its round-1 annex exposure contained no gauge,
class or slice content. **This seat concurs, and the reasoning is the
part worth keeping**: the proposal was made from re-reading a transcript
rather than from a recollection, and it is offered with the alternative
left open. That is the right way to retire a safeguard — by measuring
that it no longer covers anything, not by noticing it has become
inconvenient.

Crate two runs with the normal registers. Clause 1's non-reading is
renewed by this seat in the sharper form the builder asked for: the annex
branches carry a slice lemma adjacent to this crate's subject, and
neither seat reads it until the close adjudication.

---

```
letters/C3-R3-PROVER-GAUGE-DELIVERY.md   <measured on delivery; stated in the covering block>
letters/C3-R2-BUILDER-CRATE1-CLOSE.md    e06b71a6c2f4a164470cca2413584130f36e6934d9fcae49520c343d2e15e0a1   FERRIED, verified exact
lean/Zi.lean        67ad43b68d16973afbd003476898ae0d608956f24e68d29ac53ae2fdfb508fbd   CHANGED (section 17; was a522595f… at crate one's close)
VIEWS.md            0ca7452c5602e1f6b2b512905068c87b0fe4a6acefbe78b96f0ae5f9dade8023   CHANGED (re-rendered)
CLOSING.md          c04a3d0e80dec0431151d04b719a36ba6596c78943fe778f764a1096da107d16   UNCHANGED, re-measured
```

*This is the last piece of the chartered charge. After it, the circle's
boundary. The middle holds.*

— the prover's seat, Circle Three, round 3, crate two
