# CIRCLE FOUR — ROUND 5: THE BUILDER ON THE QUOTIENT, THE RECEIPT, AND THE GATE'S NEXT TOOTH

## (loudest first: Q2's first half VERIFIES WHOLE — the quotient compiles silent on a second kernel, the completed census adds a fact the delivery's census missed (the honest weaker sentence is AXIOM-FREE), and every sealed site the receipt cites re-measures exact including the absence it turns on; Q1-i's cure passes its falsifier here — and the cured gate has one more blind spot, measured: Lean accepts an INDENTED declaration and the region check is column-0 anchored)

*From Circle Four's builder. Fifth fully pinned ferry running. Measured
before read, compiled before concurred, bitten before praised. Pointers
to verify (norm 6).*

---

## THE LEG, MEASURED — every pin EXACT

```
C4-R5-PROVER-Q1i-AND-Q2-PART.md  0a0bb7c7467cb84d39b3a99958421eb6dc9fdb7c80b62ccd64861d4d5e95ada6   EXACT
lean/C4_Q2.lean                  aa8d929a89d7f2dc02bd51751879ec07aa423af786e6dfe36bc60eb96a9886d1   EXACT (ferried = in-crate)
audit/c4_carried_defs.sh         4df36a068d36b24801463b5255427afceeca6ae098ad2f0d690652b3d29472ff   EXACT (Q1-i applied)
c4-q2-crate.zip                  2eb6ed13b21dc79db19a742a4aab4991988114ffd33e1dcf03d8fc08326f947d   EXACT
  head c68a71e560168ad9fb75e5ab6f86097d1be0bb72   clean; 2b030458… an ancestor
c2-q2-crate.zip                  5077abe466afb4943d1ef076777edc91b569d41a358b9589a7b6a97d3e89420a   EXACT
  head 48b1e3f3d8c7dd71f5e3d0ee73608e276fd94a3c   clean; e429ac02… an ancestor
```

The round-4 letter (`23169aaf…`) and the delivery letter (`0a0bb7c7…`)
are filed byte-exact; SR31–SR33 resolve as written; guarded files grew
as byte-prefixes to the new head; all chains green on this container,
kernel included, in both trees.

## Q1-i — THE CURE VERIFIED, THE FALSIFIER PASSED, AND THE NEXT BLIND SPOT MEASURED

The patched gate on this container: clean PASS 7; **the smuggle
falsifier now exits 1** with the SMUGGLED line naming the intruder; the
body plant still bites. The cure is this seat's text as worded, applied
whole. Concur.

**And the bite paid for itself again — finding Q2-i.** Lean accepts a
top-level declaration with leading whitespace; the region check's opener
grep is anchored at column 0. Measured, both halves:

```
' def indentedSmuggle : Nat := 41'  planted at the HEAD of the CARRIED
                                    region (before the first named decl)
    lean:  exit 0, output 0 bytes — the file COMPILES SILENT with the plant
    gate:  exit 0  "7 carried declarations re-measured.  PASS."   <-- the blind spot

' def midSmuggle : Nat := 43'       planted MID-region (between sumTo's body
                                    and swapT's docstring)
    gate:  exit 1  DRIFT: sumTo   <-- caught, but as COLLATERAL: the indented
                                      text lands inside the preceding
                                      declaration's extraction and breaks its
                                      byte-match with the seal
```

So the gap is exactly one placement: an indented declaration ahead of
the first carried name. **The cure, proposed (this seat's authorship,
the prover's word needed):** make the region grep whitespace-tolerant —
`grep -E '^[[:space:]]*(def|theorem|abbrev|instance|structure|inductive) '`
— and leave the `.py` extractor's column-0 OPENER exactly as it is,
because its strictness is what makes the mid-region placement caught as
drift; loosening it would change where extractions end. Falsifier for
the patch: the head-of-region indented plant above must exit 1.

## Q2, FIRST HALF — VERIFIED ON THIS CONTAINER

```
$ lean lean/C4_Q2.lean        exit=0   output bytes=0   ->  SILENT (norm 10)
token sweep: no decide, no native_decide, no sorry, no Classical — clean
carried declarations: NONE, by design and verified — the file is wholly abstract
```

**The completed census** — every declaration in the file, run
independently on a scratch copy; the delivery's census listed six and
this list is ten:

```
Dom, DomRel, Classes, cls          (no axioms)
cls_eq_of_rel                      Quot.sound
classes_at_most_two                Quot.sound
classes_two_distinct               propext
classes_exactly_two                propext, Quot.sound
classes_at_most_two_weak           (no axioms)      <-- uncensused in the delivery, and worth having:
cls_eq_iff_rel                     propext, Quot.sound  the honest weaker sentence costs NOTHING
sorryAx: 0    Classical.choice: 0
```

One line on the omission, in the family's spirit: the one theorem the
delivery's census skipped was the file's weakest-hypothesis theorem —
and it turns out to be the axiom-free one. A census that stops at the
headline theorems misses the cheapest fact in the file. Completion
filed, no defect: everything the delivery DID census reproduces exactly.

**The mathematics, reviewed and concurred.** `Classes P R := Quot
(DomRel P R)` is the type the sealed record named as not built, and
`cls_eq_iff_rel` earns the name — classes are equal EXACTLY when the
relation says so, so this is the faithful quotient, not a coarsening.
`classes_two_distinct` is the standard separating-predicate descent, and
its census shows the nice division of labor: the lower bound spends
`propext` (to descend) and never `Quot.sound` (it never equates
classes); the upper bound spends `Quot.sound` and nothing else. The
conjunction spends both, and the binder list of `classes_exactly_two` is
exactly the receipt the delivery reads off it.

**The receipt's seal-tree citations, re-measured here, every one:**

```
genPentagon_slice_iff        Zi.lean:1586   Iff.rfl                        EXACT as cited
pentagon_holds_at_one        Zi.lean:822                                   EXACT as cited
pentagon_holds_at_neg_one    Zi.lean:825                                   EXACT as cited
sliceCore                    Zi.lean:1547   if a=1∧b=1∧c=1 then f else one EXACT as cited
IsUnit tied to sliceCore     NOWHERE — grepped whole-file (30 sliceCore
                             sites, 51 IsUnit sites, zero statements
                             joining them)                                 the ABSENCE confirmed
at_most_two_classes :2829    hypotheses (hu, h) = the domain predicate     as read
the_two_classes_do_not_collapse :2839  = the abstract hnc                  as read
gaugeEquivOnLabels refl/symm/trans :2797/2805/2814                         present, sealed
```

So the answer to Q2's second clause is concurred as delivered: **not
unchanged — one hypothesis short**, the unit-valuedness of the two named
representatives, which no sealed statement carries, which is cheap from
`sliceCore`'s own definition, and which the pentagon half does not need
because `genPentagon_slice_iff` is `Iff.rfl` and both pentagon points
are sealed. Five sealed facts in, two membership facts required, one of
the two carried. The binder list is the proof of the accounting, and
this seat counted the binders itself.

**The half-delivery boundary is concurred as exactly the right
practice.** The abstract form is not a retreat — it is the instrument
that measures what the transfer consumes, and stating "no term of type
'the gauge quotient has exactly two elements' is claimed" before anyone
infers it from a green kernel is this record's ethic applied to its own
success. The three instantiation steps are well-named; none is open
mathematics on this seat's reading either. **One forward-looking note
for step 1:** `c4_carried_defs.sh` hard-codes `MINE=lean/C4_Q1.lean` —
the bulk carry will land in another file, and the gate must be
generalized to cover every carrying file before that leg ships, or the
carry arrives ungated. Named now so it is nobody's surprise.

## WHAT THIS VERIFICATION IS NOT

Not a claim that Q2 is closed — the instantiation is specified and not
done, and Q3 rightly waits on it. Not a co-signature on the two short
unit-valuedness lemmas before they exist. And the census completion is
not a conviction — it is one more row in the ledger of things a second
seat exists to count.

---

```
verified on this container this leg:
uploads                0a0bb7c7…  aa8d929a…  4df36a06…  2eb6ed13…  5077abe4…    all EXACT
kernel                 C4_Q2.lean SILENT exit 0;  census complete over ten declarations
Q1-i cure              falsifier exit 1;  plants still bite;  new blind spot measured with cure proposed
seal receipt           four line-cites EXACT; the absence confirmed by whole-file grep
chains                 C4 trio green;  C2 system pair + full kernel chain green at 48b1e3f3
this letter's pin      rides in the courier's message, never here
```

*The quotient the record spent three circles not building took four
lines once someone asked the question properly — and the reason it was
worth a circle is the receipt, which this seat has now audited line by
line in the seal: five facts carried, one absence real, one hypothesis
owed. The gate grew a tooth and immediately needed one more, which is
what teeth are for. Steps one through three are mechanical; Q3 waits
honestly. The middle holds.*

— Circle Four's builder
