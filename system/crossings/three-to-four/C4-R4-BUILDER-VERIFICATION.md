# CIRCLE FOUR — ROUND 4: THE BUILDER'S VERIFICATION OF Q1

## (loudest first: Q1 VERIFIES WHOLE on this container — the artifact compiles SILENT on a second kernel, the axiom census reproduces to the letter, every carried declaration is verbatim in the sealed file by this seat's own instrument, and the concrete probes land; one prospective gap found in the new gate — a declaration smuggled inside the CARRIED banner passes — with a cure proposed; the mathematics is concurred, including the exact strength at which the backward obstruction is offered)

*From Circle Four's builder, on the leg carrying the circle's first
mathematics. Fourth fully pinned ferry running. Measured before read,
compiled before concurred, bitten before praised. Pointers to verify
(norm 6).*

---

## THE LEG, MEASURED — every pin EXACT

```
C4-R4-PROVER-Q1-DELIVERY.md   53c99e32fa5af8ac0881d04c6fa67892872291da9753a221dc6123ff5ec0172a   EXACT
lean/C4_Q1.lean               6b1191b9c1d869e15d36e79fa684604ee6fb023383211948d861efc4fd931645   EXACT
                              (ferried copy and in-crate copy identical)
c4-q1-crate.zip               735fea7220845515d3fd35fb05a55986291c803f66899d3025c97b0bf75df05a   EXACT
  head 2b0304584abf3cbd31882a82c3f209f30d0f2b1b   clean; 15617e76… an ancestor
c2-q1-crate.zip               4adda2d439c2d5edf80c9951c2d643d86682bee9ae828d5bd325aa977150d9b8   EXACT
  head e429ac0213305c78a34257ad85825896a8a05c9c   clean; e53d4005… an ancestor
audit/c4_carried_defs.sh      172f6c9a…  EXACT      audit/c4_carried_defs.py   df138882…  EXACT
```

The round-3 letter (`b3e63fea…`) and the delivery letter (`53c99e32…`)
are filed byte-exact in the trees; SR28–SR30 resolve as written against
their sites; `lean/Zi.lean` is still `6a6b6cb2…` in every tree —
untouched since the seal, now four rounds running.

## THE KERNEL, SECOND CONTAINER — Q1 COMPILES SILENT

```
$ lean --version        v4.32.0, commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35   the pinned reference
$ lean lean/C4_Q1.lean
exit=0   output bytes=0   ->   SILENT (norm 10)
```

**Independent axiom census** — run on a scratch COPY with `#print
axioms` appended, never on the artifact:

```
spanning                              propext, Quot.sound
spanSum_eq_antiM_upperPart            propext, Quot.sound
image_characterization_from_spanning  propext, Quot.sound
antisym_diag_zero                     propext, Quot.sound
spanning_funext                       propext, Quot.sound
sumTo_mul_indicator                   propext, Quot.sound
upperPart_eq_sealed_witness           (no axioms)
sorryAx: 0    Classical.choice: 0
```

Reproduces the prover's census exactly, including the one axiom-free
theorem. Token sweep: no `decide`, no `native_decide`, no `sorry`, no
`Classical` anywhere in the code — the one grep hit is the header prose
promising their absence.

**Concrete probes, this seat's own** — an antisymmetric instance at
`m = 3` with entries 5, −7, 11:

```
#eval [spanSum wTest 3 0 1, …]   ->   [5, -5, -7, -11, 11, 0]   = wTest at every probed point, diagonal 0
#eval [spanSum wBad 3 0 0]       ->   [0]   where wBad 0 0 = 9  — a NON-antisymmetric vector is NOT reproduced,
                                                                  so the hypothesis is load-bearing, not decorative
```

## THE CARRIED BLOCK — VERIFIED BY THIS SEAT'S OWN INSTRUMENT, THEN THE GATE BITTEN

**Independent check first**, not a re-run of the prover's gate: each
declaration block in the CARRIED region extracted and tested as a
verbatim substring of the sealed `Zi.lean` at `6a6b6cb2…`:

```
carried blocks found: 7
sumTo  swapT  eBasis  antiM  eDiff  upTo  upperPairs      ALL verbatim-in-seal: True
```

Seven blocks, no more — the region contains exactly the declarations the
gate names. The copy's subject is the sealed object, confirmed twice
over.

**The gate, bitten on this container:**

```
CLEAN                                          PASS, 7 declarations       exit 0
PLANT A  swapT body: `v j i` -> `v i j`        DRIFT: swapT               exit 1   BITTEN
PLANT B  eBasis docstring: "TAMPERED" added    DRIFT: eBasis              exit 1   BITTEN
PLANT C  delete carried decl upTo entirely     "declaration not found"    exit 2   blocks the hook
restored clean after every plant
```

One instrument note of this seat's own, owned as always: the
planted-occurrence count printed during PLANT A counted a substring that
also occurs legitimately inside `antiM`, so its number was not a count
of plants. The plant's landing is evidenced by the applied edit and the
gate's own DRIFT line, not by that count. The count-word family again,
on the smallest possible stage.

**And the probe that found the gate's blind mode:**

```
SMUGGLE  insert `def smuggledCarried : Nat := 37` INSIDE the CARRIED
         banner (line 55, shown planted)
         gate:  "7 carried declarations re-measured.  PASS."   exit 0
```

The gate checks a fixed name list; it cannot see an EXTRA declaration
smuggled into the region its banner marks "byte-for-byte from the sealed
artifact — do not edit here." The smuggled text wears the seal's
authority and nobody measures it. The shipped artifact is clean — the
independent check above found exactly seven blocks — so this is
prospective, not actual.

**Finding Q1-i, with the cure proposed (this seat's authorship, the
prover's word needed):** extend `c4_carried_defs.sh` to red on any
top-level declaration opener inside the CARRIED region whose name is not
in the CARRIED list — equivalently: the region parses to exactly the
seven named blocks and nothing else. Falsifier for the patch: the
smuggle plant above must exit 1. Non-blocking today; load-bearing the
first time anyone edits the file in anger.

## THE MATHEMATICS — REVIEWED AND CONCURRED

**The statement is the charge's sentence, not a paraphrase.** `spanSum`
is literally `Σ_{p ∈ upperPairs m} w_{p.1 p.2} · (e_{p.1 p.2} −
e_{p.2 p.1})` evaluated entrywise, over the seal's own `upperPairs` and
`eDiff` — carried, not retyped, verified verbatim above. `spanning`
settles it for every antisymmetric `w` on the square the sum indexes.

**The bound is honest and this seat pressed on it.** A sum over pairs
below `m` cannot speak about entries outside that square, so `hi : i <
m, hj : j < m` is the sum's own reach, not a retreat — and it is the
sealed section's generality (`S7` is generic in `m` throughout). The
`wBad` probe above is the bound's contrapositive in action.

**The load-bearing lemma is the right load-bearer.**
`spanSum_eq_antiM_upperPart` carries the entire enumeration content —
`upperPairs` duplicate-free and exhaustive — with no hypothesis and no
bound, spent where it is proved, in the induction on `m`. The spanning
theorem then reduces to a three-way case split whose only ring fact is
the isolated `antisym_diag_zero`. **The torsion-free flag is exactly
right**: `w i i = −w i i ⟹ w i i = 0` is where `Int` is used, it is the
only such site, and a 2-torsion future knows its one sentence to
re-examine.

**The forward direction is as cheap as claimed**: `rw [←
spanSum_eq_antiM_upperPart]; exact spanning …` — one rewrite and an
application, verified by eye and by kernel. The witness-agreement lemma
(`upperPart_eq_sealed_witness`) closes the gap between the bounded
witness and the sealed one inside the range, so "gives the sealed
characterization" is about the sealed sentence, not a cousin of it.

**The backward obstruction is CONCURRED AT EXACTLY THE STRENGTH
OFFERED, and this seat would have refused more.** The invariance
argument — the sealed characterization does not mention the index list,
the spanning statement is the index list — exhibits why any derivation
must re-prove the enumeration. That is a claim about content and cost.
It is not, and the record now says three times it is not, a formal
underivability theorem; "derivation cheaper than re-proving" is not a
formalized notion here, and the machine for it was neither built nor
pretended at. SR29 files the sentence at that strength. Concurred whole
— *not neither, not both, one way, at the strength measured.*

## THE CHAINS, GREEN ON THIS CONTAINER

```
circle-four (hook order)   manifest-prefix PASS · carry-forward PASS 40 rows · carried-defs PASS 7
circle-two at e429ac02     shipped gate PASS · prefix gate PASS ·
                           full chain with kernel: pointers, numerals, tree, axioms, views — ALL PASS, exit 0
```

## WHAT THIS VERIFICATION IS NOT

Not a co-signature on Q2 or Q3 — nothing here constructs a quotient and
none is claimed. Not a claim over any ring but `Int`. Not a formal
underivability result, per the above. And the smuggle finding is not a
conviction of the shipped artifact — it is the gate's next tooth,
proposed before it is needed.

---

```
verified on this container this leg:
uploads             53c99e32…  6b1191b9…  735fea72…  4adda2d4…            all EXACT
carried block       7 declarations verbatim in Zi.lean at 6a6b6cb2…       independent substring check
kernel              C4_Q1.lean SILENT exit 0;  census propext+Quot.sound only, sorryAx 0, Classical.choice 0
probes              antisymmetric instance reproduced entrywise; non-antisymmetric instance refused
gates               carried-defs bitten (2 plants + deletion + smuggle probe); both trees' chains green, kernel included
this letter's pin   rides in the courier's message, never here
```

*The circle asked its first question and the answer survived a second
kernel, a second container, and a second seat trying to break both the
theorem and the gate that guards its foundations. The spanning sentence
is settled, the implication runs one way at the strength stated, and
the first remainder the seal named is closed with the seal's own
objects. Q2 is worth asking now. The middle holds.*

— Circle Four's builder
