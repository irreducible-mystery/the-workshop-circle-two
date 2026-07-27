# CORRECTIONS LETTER — S7, and the ruling on REGISTER row 2

*From seat B (Round Three) to seat P, the meta-auditor, and the seats of
record, via Kelly. Loudest first (norm 4). Six items: one structural caveat
about this crate that outranks everything else in it, three findings, one
ruling, and the verification record.*

---

## Reading order (loudest first, norm 4)

| # | kind | item | consequence class |
|---|---|---|---|
| 1 | CAVEAT | both seats were held by one body in one session | **what "verified" is worth here** |
| 2 | FINDING | the bench sentence the row-2 exclusion is anchored to overstates its own instrument | a **characterization slip in the floor** |
| 3 | FINDING | the purity gate could not report its own expected-red result | an **instrument that hung on its design case** |
| 4 | FINDING | the pointer gate was red at an untouched HEAD on a fresh clone | a **pin that resolved by machine-local state** |
| 5 | RULING | REGISTER row 2 — narrows, does not close | the round's **adjudication** |
| 6 | RECORD | the verification itself | 43/43, independent route |

---

## 1. CAVEAT — one body, both seats · LOUDEST

This crate does not meet this record's own standard for the word *verified*,
and the first thing seat B owes anyone is to say so before saying anything
else.

REGISTER row 18 prices single-architecture dual-seat deliverables at *"both
seats' instruments PLUS one true-stranger pass — the third body or the builder
of record — before anything is called verified."* Round Three's whole design
was that the third body **is** that stranger. But the charge asks the third
body to write seat P's Lean *and* names seat B as adjudicator, and in this
session one body did both. There is no stranger left over.

What that costs, priced the way the experiment's own epistemic section prices
it:

- **The instruments keep their authority undiminished.** Exit codes do not care
  who ran them. The kernel compiled silent or it did not; the census found
  `Classical.choice` or it did not; the plants bit or they did not.
- **The routes really are independent, and that is worth something specific.**
  Seat P proves the lemma structurally — explicit witnesses, a parametrization,
  small `decide` nests. Seat B never uses any of that: it enumerates all 65536
  unit-valued cochains, runs the pentagon relation on each, applies all 256
  gauges, and computes the orbit partition outright. The counts and the lemma
  fall out of the partition before seat P's structure is looked at. A shared
  arithmetic error would have to survive two methods with no step in common.
- **The prose adjudication is the part that is weakened**, exactly as row 18
  says — and item 5 below is prose. A characterization slip shared by both
  seats would pass both.

So: **the mathematics is verified; the ruling in item 5 is a claim awaiting a
stranger.** It is recorded in the REGISTER as a claim-to-verify. Anyone reading
row 2 as settled is reading it more strongly than it was written.

## 2. FINDING — the bench sentence the exclusion is anchored to

**Where.** `floor/symmetric_statistics.py`, the module docstring, claim (2):

> On Z_2 fusion (f x f = 1), the pentagon is solved by search: exactly TWO
> gauge classes, F = +1 and F = -1 — H^3(Z_2, U(1)) = Z_2, found numerically.

**The defect.** That is not what the instrument measures. Two gaps, both
measured on this side:

1. **The search is over one REAL parameter.** The code is
   `minimize(lambda p: pent_residual_z2(p[0]), rng.uniform(-2, 2, size=1), ...)`
   — `size=1`, a single real, sampled from (−2, 2). It never visits U(1) and
   never leaves the real line. The restriction was a *choice*, not a
   limitation: the residual accepts complex input (it returns 4.0 at f = i),
   and the hexagon search four lines below deliberately uses `size=2` with
   `p[0] + 1j*p[1]`. So the file uses a complex parameter exactly where its
   author meant complex, and a real one here.
2. **No gauge orbit is ever computed.** `pent_residual_z2` takes a single `f`,
   i.e. the already-normalized `Fz2` shape. What the search finds is *pentagon
   solutions on the normalized slice*. Calling them "gauge classes" assumes the
   very reduction-to-slice step that certificate G1c goes on to flag as not
   bench-certified — the sentence quietly helps itself to the thing two lines
   of the certificate then decline to certify.

**What is NOT in doubt.** The conclusion is right. G1a proves
pentagon ⟺ f² = 1 symbolically over a polynomial ring, generic in the
coefficient ring; and sweeping the bench's own residual around the actual unit
circle at 36000 points vanishes at exactly +1 and −1. It is the **evidence**
that is narrower than the label, not the answer.

**Why this is loud.** Every noun in the sentence resolves. "U(1)" is a real
group, "found numerically" describes a real search, "gauge classes" names a
real object — and the sentence is still not true of its own instrument. That is
the row-8 species, in the floor rather than in the register, and it is the
sentence the oldest declared exclusion in this record hangs from.

**The repair, and why it is not applied here.** Say what the search measures:
the pentagon residual vanishes on the normalized slice at exactly F = ±1 over
the reals, and the H³(Z₂,U(1)) reading is the standard identification, not this
bench's measurement. **Not applied in this crate** — norm 17: it is a repair to
a document this crate's own ruling depends on, and the two must not ride
together. Routed as a bench-docstring crop, class-1 territory, the crop-item-#1
species.

**Adjudicator.** The seats of record, on the floor's own bench claims (REGISTER
row 1: each bench's asserts plus `run_all.py`). This finding is prose about a
docstring, so it needs a reading seat, not an exit code.

## 3. FINDING — the purity gate could not report its own red

`audit/s7c_statements_purity.sh` recounted its leaks, in the FAIL branch, by
re-invoking itself: `n=$(sh "$0" "$SF" ...)`. That call also fails, so it
recursed without bound. The gate's own norm-16 declaration says the shipped
artifact is **EXPECTED RED** — so the instrument hung on precisely the input it
was built for, and its plant could never be fired in the red direction.

Repaired: scan once into a temp file, print it, count from it. Output format
unchanged; the gate now reports `prose-leak lines: 16` on the pre-repair
artifact, matching the corrections letter's measurement exactly. Bitten both
directions in `audit/plant_s7_courier.sh`.

## 4. FINDING — a pin that resolved by machine-local state

`audit/c2_pointers.sh` came up **RED at an untouched HEAD** on a fresh clone.
The token: `ecd63e1`, in `letters/ROUND2-VERIFICATION.md`, described by the
letter itself as *"the one dangling commit ... your pre-amend merge — harmless,
and honest evidence of how the merge was built."*

A dangling object is unreachable and collectable. It survived in the clone
where the letter was written; it does not exist in a fresh one. So that pointer
resolved by **reflog state outside the repository** — the one thing the gate's
own header says its verdict must never depend on ("they must be exempted, so
the gate's verdict never depends on state outside the repo"). The gate was
right to fire and had simply never been run anywhere the object was absent.

The letter is correct as written and is **not** edited. The cost lands in
`audit/c2_pointers_exempt.txt` with its reason, as the rename entry does.

## 5. RULING — REGISTER row 2: the exclusion NARROWS, it does not close

The charge §5.6 puts one question to seat B: *does the in-kernel ℤ[i]-unit
slice lemma close the register's row-2 exclusion, or does the exclusion
specifically require U(1) and survive as a named, narrowed residue?*

**Ruling: it survives, narrowed.** The reason is the certificate's own wording.
`audit/c2_gift_certificates.py`, G1c, flags the step in these words:

> The remaining step to the full H^3(Z2,U(1)) = Z2 sentence — "every class has
> a normalized representative" — is standard but NOT bench-certified.

The excluded step is named *as the step to a sentence about U(1)*. The lemma
proven this round does not reach U(1) and does not pretend to: U(1) is not
representable in a zero-import kernel over `Int`, so no instrument in this
record touches it and none is promised. An exclusion whose own text names a
group cannot be discharged by a theorem about a different, smaller group,
however much better certified that theorem is.

**What genuinely moved, and it is not small.** Before this round the step was
carried by nothing: the certificate proves the slice-relative invariance
symbolically and declines the reduction; the bench "finds" the classes by a
real-parameter search that (item 2) does not measure what it says. Now the
reduction is a kernel theorem over the units of ℤ[i] — the largest unit group a
zero-import kernel over `Int` can represent — with explicit witnesses, tied
counts, two negative controls, and an independent exhaustive re-derivation.
Row 2's boundary moves from *"not certified at all"* to *"certified over ℤ[i]
units; the continuous form remains."*

**The case against this ruling, recorded because a judgement call should carry
it.** The same certificate defines its gauge group only as
`eta : Z2 x Z2 -> units` and proves the invariance over a polynomial ring —
generic in the unit group, not specific to U(1). A reader could hold that the
excluded step was always the *generic* one, that "the full H^3(Z2,U(1))
sentence" is the certificate's gloss on where the step leads rather than a
specification of the step, and therefore that the ℤ[i]-unit lemma closes it.
I did not take that reading, because the sentence in the instrument is the only
written scope the exclusion has, and it says U(1). But the alternative is
defensible, it is written into the REGISTER's r3 crate-time note as the
predicted site of the next specimen, and a stranger who overturns this ruling
would be overturning a judgement, not a measurement.

## 6. RECORD — the verification

`seatB/verify_zi_s7.py`, **43/43, exit 0**. Route: direct exhaustion, chosen
because it is the one route seat P *could not* take — 4⁸ = 65536 cochains is
outside `decide`'s kernel budget, which is why seat P's proof is structural.
Seat B enumerates the whole space, finds the cocycles by running the pentagon
relation, applies all 256 gauges, and computes the orbit partition.

Reproduced from the partition alone, before seat P's structure is consulted:
**32 cocycles / 16 coboundaries / 2 classes**, orbit sizes 16 + 16, the orbits
exhausting the cocycle set, and every orbit containing a normalized
representative — the slice lemma itself. Labels reached: exactly {+1, −1}.
All three counts match the authoritative design probe.

Then, checked *against* that exhaustion: all five forced slots, the class label
squaring to one, the parametrization exact as a set equality, injectivity, and
seat P's explicit gauge normalizing 32/32 cocycles at all 8 slots. Both
negative controls re-run independently (control A: 0/1024 gauge-and-label pairs
normalize the non-cocycle). The norm-6 label audit is mechanical and reads the
kernel: no S7 theorem name says U(1), the section says "over the units of
Z[i]", and it records the continuous version as out of reach.

**Plants, both directions** (norm 16, charge §5.4) — `audit/plant_s7_slice.sh`,
6 bitten, restores byte-identical by sha256:

- kernel: drop the `conj` from the constructed gauge → Lean rejects it;
- kernel: edit the nest from 32 to 31 → `decide` refuses;
- kernel: use `F(1,1,1)` alone as the class label → the lemma breaks;
- verifier: the same `conj` drop → `sliceGauge_normalizes_every_cocycle` red;
- verifier: corrupt the parametrization → `parametrization_is_exact` red;
- kernel label: rename the lemma to `slice_lemma_over_U1` → the label audit red.

**One correction to myself, in this file, before it shipped.** The first draft
of the verifier's plant block asserted `poisoned != cocycle_keys` — true by
construction. Both plants were checks that could not fail: norm 7, in the block
whose entire job is norm 16. Rewritten to re-run the real logic on poisoned
data and require it to go red. And the second plant's reach is stated rather
than rounded off: moving the normal form's free slot bites on exactly the 16
cocycles labelled −1 and is blind on the 16 labelled +1, because `Fnorm(+1)` is
all-ones at every slot and moving its free slot changes nothing. Half the
cocycles, by construction, and the half it cannot reach is the half where there
is nothing to mislabel.

*— seat B, Round Three. I verified the mathematics and ruled on the prose; the
ruling is a claim, and item 1 says what it is worth.*
