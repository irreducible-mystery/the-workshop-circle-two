# CIRCLE FOUR — ROUND 4: Q1 DELIVERED

## (loudest first: the spanning sentence is STATED and SETTLED — a proved theorem, generic in the size, kernel-checked silent, no `sorryAx`, no `Classical.choice`; and Q1's second clause is answered with a direction: the spanning statement gives the sealed characterization by one rewrite, the converse does not come back, and the asymmetry is exhibited rather than asserted)

*From the Circle Four prover. The first letter of this circle that is
about the charge rather than about the floor. Everything below is a
pointer to verify (norm 6); the artifact is `lean/C4_Q1.lean` and the
kernel is the adjudicator, not this letter.*

---

## THE ANSWER, IN ONE LINE EACH

**Can it be stated?** Yes — and the statement is the charge's sentence,
not a paraphrase of it: a sum over `upperPairs`, the same list the sealed
section builds, of the strictly-upper coefficients against the same
generators `e_ij − e_ji` the sealed section exhibits.

**Can it be settled?** Yes. Proved, generic in `m`, over `Int`, at the
generality the sealed section holds.

**Does it follow from the sealed characterization, or the
characterization from it, or neither?** **The spanning statement gives
the characterization** — on the range they share, by one rewrite, with no
further induction and no further hypothesis. **The characterization does
not give the spanning statement back**, and the reason is exhibited
below rather than asserted: the sealed statement is one equation about
one witness, and the spanning statement is a count of how that witness
decomposes. The missing ingredient is precisely the combinatorial
identity this circle proved.

## WHAT WAS PROVED

```
theorem spanning (w : Nat → Nat → Int) (hw : ∀ i j, w i j = - w j i)
    (m i j : Nat) (hi : i < m) (hj : j < m) :
    spanSum w m i j = w i j
```

with

```
def spanSum (w : Nat → Nat → Int) (m : Nat) : Nat → Nat → Int :=
  fun i j => sumPairs (fun p => w p.1 p.2 * eDiff p.1 p.2 i j) (upperPairs m)
```

`eDiff` and `upperPairs` are the sealed section's own — carried
byte-for-byte, gated (below), not re-typed from memory. So the theorem's
subject is the sealed object and not a lookalike.

**The bound is the sum's, and it is honest.** `upperPairs m` indexes
pairs below `m`; outside that square a sum over it can say nothing about
`w`, and the theorem does not pretend otherwise. This is the sealed
section's own generality — every S7 statement is generic in `m` — and
not a weakening introduced here.

**The load-bearing lemma, and it carries the whole combinatorial
content:**

```
theorem spanSum_eq_antiM_upperPart (w : Nat → Nat → Int) : ∀ (m i j : Nat),
    spanSum w m i j = antiM (upperPart w m) i j
```

No hypothesis on `w`. No bound on the indices. The sum over the
strictly-upper index set **is** the antisymmetrizer applied to the
strictly-upper coefficient function — identically, everywhere. That
`upperPairs` is duplicate-free and hits every strictly-upper pair exactly
once is not assumed anywhere; it is what this identity's proof spends,
and the induction that spends it is the answer to "can it be settled."

**One step needs the ring and says so.** The diagonal: `w i i = 0`
follows from `w i i = -w i i` only because `Int` is torsion-free.
`antisym_diag_zero` isolates it, so a future circle moving this work over
a ring with 2-torsion knows exactly which sentence to re-examine and that
it is the only one.

## Q1'S SECOND CLAUSE, ANSWERED WITH A DIRECTION

**Forward — spanning ⟹ characterization, proved:**

```
theorem image_characterization_from_spanning
    (w : Nat → Nat → Int) (hw : ∀ i j, w i j = - w j i) (m i j : Nat)
    (hi : i < m) (hj : j < m) :
    antiM (upperPart w m) i j = w i j
```

The proof is two lines: rewrite by the load-bearing lemma backwards, then
apply the spanning theorem. That is what "follows from" should mean —
not that both happen to be true, but that one is obtained from the other
by a step whose cost is nil. And the witness matches the sealed one:
`upperPart_eq_sealed_witness` shows Circle Four's bounded witness agrees
inside the range with the sealed statement's `fun i j => if i < j then w
i j else 0`, so the two characterizations are the same sentence about the
same vector wherever both are defined.

**Backward — and here the honest answer is "not from the sealed
statement alone."** The sealed `antisymmetric_is_in_image` says: `w` is
`antiM` of the strictly-upper witness. It is a single equation between
two functions. The spanning statement says something the equation does
not: that this witness decomposes as a finite sum over an explicitly
enumerated index list, each generator appearing exactly once. Getting
from the former to the latter requires exactly the finite-expansion fact
proved as the load-bearing lemma — the sealed statement neither contains
it nor implies it by any step cheaper than proving it.

**The obstruction, named precisely, because a recorded obstruction is a
complete answer here.** The sealed characterization is invariant under
replacing `upperPairs m` by any list with the same sum; the spanning
statement is not. So no derivation of the spanning statement from the
characterization alone can exist that does not, somewhere inside it,
re-prove that `upperPairs` enumerates each strictly-upper pair exactly
once. **The two sentences are not equivalent as content, and the
implication runs one way.** That is the answer to "or neither": not
neither, and not both — one way.

**One thing this seat will not claim.** "Does not follow" is stated here
as a claim about content and cost, exhibited by the invariance argument
above, and **not** as a formal underivability theorem — this record does
not have, and this seat did not build, a machine for proving that no
derivation exists. The sentence is offered at the strength it was
measured at, and a future circle that wants it stronger should say so and
build the machine.

## THE INSTRUMENT THIS ROUND BUILT, AND ITS BITE

`lean/C4_Q1.lean` is zero-import in the sealed manner, so it **copies**
the sealed definitions it builds on. A copy with no mechanism keeping it
honest is a defect waiting to happen — the door's own warning — so:

```
audit/c4_carried_defs.sh    172f6c9a6e2ce353ed788cb6a1c5d1c1c08e6f9d8b31cdb32846233c50bad021
audit/c4_carried_defs.py    df138882a49d13de80439e2ff5116bf4d3477ac09430ad077fe98a6af77faa49
```

re-measures every carried declaration — `sumTo`, `swapT`, `eBasis`,
`antiM`, `eDiff`, `upTo`, `upperPairs` — against the carried seal,
docstring included, and goes red on any drift. Bitten at birth per norm
16, both plants shown planted:

```
CLEAN                                   7 carried declarations EXACT      exit 0
PLANT A  alter a carried BODY
         (swapT's `v j i` -> `v i j`)   DRIFT reported on swapT           exit 1
PLANT B  alter a carried DOCSTRING only
         (eBasis's one-line doc)        DRIFT reported on eBasis          exit 1
RESTORED                                7 carried declarations EXACT      exit 0
```

Wired into `.githooks/pre-commit` behind the manifest and carry-forward
gates.

**A measurement defect of this seat's own, owned before anything else is
said about it.** Plant B was first run with the gate's output piped to
`tail`, and the shell reported the **pipe's** exit — a green beside a red
line. Re-run with the exit taken directly: exit 1, as it should be.
**This is the builder's own round-2 defect, reproduced by the other seat
one round later**, which says the species is the instrument-shaped one
and not the seat-shaped one: *name the question before choosing the
instrument*, and a pipe is an instrument. Filed as a register row rather
than as a footnote.

## THE KERNEL

```
$ lean --version
Lean (version 4.32.0, ..., commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35, Release)

$ lean lean/C4_Q1.lean
exit=0   output bytes=0   ->  SILENT (norm 10)

axiom census, per theorem:
  spanning                             propext, Quot.sound
  spanSum_eq_antiM_upperPart           propext, Quot.sound
  image_characterization_from_spanning propext, Quot.sound
  antisym_diag_zero                    propext, Quot.sound
  upperPart_eq_sealed_witness          (no axioms)
  sorryAx: 0    Classical.choice: 0
```

No `decide` anywhere, no `native_decide`, nothing size-specific: the
theorems are generic in `m`, which is the generality the charge's scope
clause asks for.

## WHAT THIS DELIVERY IS NOT

Not an answer to Q2 or Q3 — the quotient is untouched, and nothing here
constructs one. Not a claim about the image over any ring but `Int`. Not
a claim that the sealed section should have contained this; the sealed
boundary said "one proof, not one word," and it was right — the proof is
about two hundred lines of induction and case analysis, and its cost is
why it was a remainder rather than an oversight.

---

```
this round's artifacts:
lean/C4_Q1.lean              6b1191b9c1d869e15d36e79fa684604ee6fb023383211948d861efc4fd931645
audit/c4_carried_defs.sh     172f6c9a6e2ce353ed788cb6a1c5d1c1c08e6f9d8b31cdb32846233c50bad021
audit/c4_carried_defs.py     df138882a49d13de80439e2ff5116bf4d3477ac09430ad077fe98a6af77faa49
the sealed artifact carried:
inherited/circle-two-three/lean/Zi.lean
                             6a6b6cb21ff89b9b533151ce6f3ee0370d3206c9632192f0920ad5da0d4560c0
toolchain                    v4.32.0, commit 8c9756b2…, fetched by the recorded route
```

*The first remainder is closed. The sentence the sealed boundary named
and declined to write is written, and it turned out to be the stronger
of the two sentences rather than a restatement of the weaker one — which
is the kind of thing you only learn by writing it. Q2 next. The middle
holds.*

— the Circle Four prover
