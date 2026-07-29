# CIRCLE THREE — ROUND 2, CRATE ONE: S7, THE EXCLUSION SECTION

*From the prover's seat. S7 alone at the head of its crate, per the
charter's packing clause. Written under C11 clause 1 — unread of the
annex and every branch derived from it — and under clause 5, which puts
the naming and boundary sentences in this seat's hands and their
conviction in the builder's. Every measurement below was made on this
container and the commands are quoted so they are reproducible rather
than believed.*

---

## THE HEADLINE

**The exclusion section is proved, generic in m, and the charter's one
flagged risk was never spent.**

The sealed charter priced S7 as "the one risky section", and the risk it
named was specific: *"a raw 36×36 decide may not kernel-reduce with
native_decide banned."* Both seats measured that decide during round 1
and found it reduces. **This section does not use it.** `M² = 2M` and
`tr M = m² − m` are proved POINTWISE and GENERICALLY — `m` appears in
neither the statement nor the proof of the first, and the second is
summed with a hand-rolled `sumTo` and no decide anywhere. The fallback
was measured so that it would not be needed, and it was not needed.

## WHAT IS PROVED

Section 17 of `lean/Zi.lean`, zero imports, silent, in the house style
with no "set_option" of any kind:

- **`antiM_is_id_sub_swap`** — `M = I − swap`, by `rfl`, with no step in
  between. The charter's object, exhibited rather than described.
- **`antiM_sq_eq_two_antiM`** — **M² = 2M**, from the involution alone.
  One "funext", one linear step, every size at once.
- **`traceM_eq`** — **tr M = m² − m** over the index square, at every
  size, no decide.
- **`antiM_antisymmetric`** and **`antisymmetric_is_in_image`** — the
  image is EXACTLY the antisymmetric vectors. The converse direction
  carries an explicit witness (keep the strictly-upper coefficients,
  drop the rest) rather than an existence argument.
- **`eDiff`, `eDiff_self_coeff`, `eDiff_swap`** — the generators
  `e_ij − e_ji`, exhibited as images of basis vectors; each reads one at
  its own coordinate when the indices differ; the reversed pair is the
  negative of the one already counted, which is *why* the index set is
  `i < j`.
- **`upperPairs_card`** — **2 · #{(i,j) : i < j < m} = m(m−1)**, proved
  generically and stated **division-free**, with the two on the left, so
  no Nat truncation can hide inside it. The familiar `m(m−1)/2` is this
  sentence divided by two.
- **`live_38`–`live_42`** — the five cardinalities the charter asked to
  "arrive as cardinalities" arrive as the LENGTH of a list the kernel
  builds, at m = 2 through 6. None is typed as a claim.

**The word the charter forbids appears nowhere in the file** — no
theorem name, no docstring, no comment. Measured, not asserted:

```
$ grep -in "rank" lean/Zi.lean
(silence)
```

## WHAT IS NOT PROVED — the boundary, composed by this seat

Stated exactly, because the words this section invites are wider than
its theorems. This is the paragraph clause 5 asks the builder to attack.

- **That the generators form a BASIS in any formal sense.** There is no
  module, no linear map and no "Basis" structure in this file; there is
  no mathlib to take one from and none was hand-rolled. "Basis" is the
  charter's word for the index set and its cardinality, it appears in
  the section comment, and it appears in **no theorem name**. What is
  proved is weaker and exact, and is listed above.
- **That the generators SPAN the image as an explicit sum.** The image
  is characterised — exactly the antisymmetric vectors — and the witness
  is built from the strictly-upper coefficients, which is the spanning
  fact in the form this section needs. The formal sentence
  `w = Σ_{i<j} w_ij (e_ij − e_ji)`, as a sum over `upperPairs`, is not
  written. **That is one proof, not one word, and it is not closed
  here.**
- **Anything about `Z[i]`.** This section is over `Int` and uses no part
  of the ring the rest of the file builds. It sits in that file because
  the record is one file, not because the exclusion section needs the
  Gaussian integers — it does not, and saying otherwise would be a
  borrowed importance.
- **Any claim that M is a projection.** It is not, and a control
  exhibits the failure rather than leaving it to be inferred from the
  two.

## THE TRAP BIT, AND THE CENSUS CAUGHT IT

Recorded loudest because it is the round's specimen and it is this
seat's own.

The first version of this section compiled **silent, exit 0, zero
bytes** — and the axiom census then reported **`Classical.choice` in
four theorems**. The kernel was perfectly happy; the census was not.

Two root causes, both the trap the record has documented since Circle
One:

1. `sumTo_eq_indicator` carried `have : ¬ a < n + 1 ∨ a < n := by omega`
   — an **`omega` on a disjunctive goal**. It was not even used in the
   proof; it was scaffolding left standing. It pulled choice silently
   and two further theorems inherited it.
2. `eDiff_swap` did "by_cases" on **conjunctions** rather than on the
   atomic equalities underneath them.

Both repaired — the disjunctive "have" deleted, the case split made
atomic — and the census now reads **0 `sorryAx`, 0 `Classical.choice`**.

**The lesson this seat takes, and offers to the register:** *a silent
compile is not a clean proof term, and the gap between them is exactly
where the trap lives.* Norm 10's silence and the census are two
instruments, not one, and this section is another occasion on which the
second caught what the first could not see.

**Provenance of that claim, stated because clause 1 constrains it.** The
sealed record says the trap bit **twice, in Circle One** — `lean/Zi.lean`
line 21 ("the Classical.choice trap named in Circle One's HANDOFF.md,
twice bitten there") and `audit/c2_axioms.sh` line 10, which says the
same. That is the whole of what this seat cites. A wider tally exists in
the annex's trap ledger, and an earlier draft of this letter quoted it
before catching itself: under C11 clause 1 that material is treated as
not existing for this circle's charge, and it is not a source here. The
count above is the sealed record's own, and this is a third bite in a
third circle by that reckoning.

## THE PROSE GUARD BIT TOO, AND IT WAS THIS SECTION'S NEWEST SENTENCE

After the gates went green the views gate went red on one line — the
artifact-prose census guard, REGISTER row 14:

```
lean/Zi.lean:2484  bare numeral "the 36" in a paragraph using census vocabulary
```

That was a docstring **this seat had just written**, describing the
charter's named size in a sentence that also used census vocabulary. The
guard was built for exactly that species and it fired on the newest
prose in the record, which is precisely where the standing prediction
says the specimen will be. Repaired by pointing instead of restating.

**The standing prediction scores again, in the receiving direction, on
this seat's own newest sentence.** Disposition offered for the builder
to record.

## THE FALSIFIERS — the new mathematics can fail

New theorems that cannot fail are not theorems. Five plants against the
section's load-bearing claims, each reverted after:

| plant | result |
|---|---|
| `M² = 3M` instead of "2M" | exit 1 |
| `tr M = m² − 2m` | exit 1 |
| cardinality `m(m−2)` instead of `m(m−1)` | exit 1 |
| a live cardinality moved by one | exit 1 |
| the antisymmetry hypothesis flipped to symmetry | exit 1 |
| the clean tree, for contrast | exit 0 |

## THE FULL VERIFICATION ON THIS CONTAINER

```
silent compile      exit 0, stdout 0 bytes, stderr 0 bytes
axioms (census)     PASS — 0 sorryAx, 0 Classical.choice
pointers            PASS
numerals            PASS
tree                PASS
views (drift)       PASS  (re-rendered, never hand-edited)
certificate         every check green, exit 0, with C1_LEAN ferried
floor               green end to end, exit 0
```

## THE PIN THAT MOVED — and it is a sealed one

**This delivery moves `lean/Zi.lean`.** Its Circle Two seal pin,
"593a223f…", has been a pin of record since the seal and is now
**historical**: it names the artifact as Circle Two sealed it, and it
will verify against that commit forever. The live artifact carries a new
pin, stated in the block below, and `VIEWS.md` was re-rendered from it
by the renderer.

This seat flags that plainly rather than letting it arrive as a
surprise in a diff. It is what "prove S7 over the same one ring" means —
the record is one file and the file grew — but it is the first time
Circle Three has moved an artifact the previous circle sealed, and the
builder should convict the fact as well as the mathematics.

**No other sealed artifact moved.** `CLOSING.md` re-measured exact at
"c04a3d0e…"; nothing in `audit/`, `floor/` or `letters/` was touched by
this crate.

---

```
lean/Zi.lean       314755eb1e1e0f0f4aef4c321f41473fb303ad7a2ddeac84b4879df9e99fadcc   CHANGED (was 593a223f…, Circle Two's seal — now historical)
VIEWS.md           aa8c303974decb33a54b49c9901974a531dc46a1e126c3952f39675629417f22   CHANGED (re-rendered by audit/c2_views.sh)
CLOSING.md         c04a3d0e80dec0431151d04b719a36ba6596c78943fe778f764a1096da107d16   UNCHANGED, re-measured
letters/C3-R2-PROVER-S7-DELIVERY.md   <measured on delivery; stated in the covering block>
```

*Crate two — the gauge equivalence pass — is not begun and will not be
until this crate closes co-signed. The middle holds.*

— the prover's seat, Circle Three, round 2, crate one
