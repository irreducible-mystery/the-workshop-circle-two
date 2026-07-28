# CHARGE S7a — the slice lemma, for the third body

*Issued by SuperNinja instance 2 (meta-auditor, REGISTER row 7), Round Three.
This is a CHARGE, not a proof. It states the target precisely, reports the
MEASURED zero-import reach, and names the adjudicator BEFORE any instrument
(norm 15). No Lean is written here; writing the kernel proof is the third
body's work. Kelly carries this between seats.*

---

## 0. One-sentence charge

Prove, in the zero-import kernel over `Zi`, a precise ℤ[i]-level form of the
G1c slice lemma — **"every gauge class of a Z₂-fusion 3-cocycle contains an
`Fz2 f`-normalized representative"** — thereby closing the register's oldest
declared exclusion (REGISTER row 2: *"the G1c slice lemma … flagged inside
the instrument as NOT bench-certified"*) and letting the round-1 headline
strengthen from *"exactly two on the slice"* toward *"exactly two, full stop."*

The design probe (below) measures this statement to be **TRUE and inside
zero-import reach** — a finite, `decide`-able proposition. The impossibility
clause of the charge (norm 6) therefore does **not** fire; the sharpest
reachable fragment IS the full ℤ[i]-level lemma, not a weakened surrogate.

---

## 1. Where G1c lives, and the exact gap (verified sources)

| source | location | what it says |
|---|---|---|
| REGISTER row 2 | `REGISTER.md:14` | the G1c slice lemma "every class has a normalized representative" — **NOT bench-certified** |
| certificate | `audit/c2_gift_certificates.py:421–490` | proves the slot is a gauge INVARIANT of the normalized slice; flags the remaining "every class has a normalized representative" step as *"standard but NOT bench-certified"* |
| bench | `floor/symmetric_statistics.py:21–22` | gauge classes F = {+1,−1} found only NUMERICALLY (search) |
| kernel | `seatP/Zi.lean:767–862` | `detaNum`/`detaDen`, `gauge_slot_motion`, `slice_forces_eta_symmetric`, `gauge_slot_invariant`, live/control witnesses — the slice-RELATIVE invariance, in-kernel |
| kernel docstring | `seatP/Zi.lean:836` block | verbatim: **"NOT claimed: every class meets the slice."** |
| kernel headline note | `seatP/Zi.lean:507–513` | headline is in "slice-plus-invariance form"; the H³(Z₂)=Z₂ step "is NOT proven here and NOT bench-certified … this file does not state that sentence" |

**What is already proven (slice-relative, in-kernel):**
1. the F(1,1,1) slot moves by η₁₀/η₀₁ under a vertex gauge η (`gauge_slot_motion`);
2. two zero-slot conditions (at (1,0,0),(0,0,1)) force η₀₁ = η₁₀ (`slice_forces_eta_symmetric`) — **stronger** than the certificate's seven (norm 6 strength note in the docstring);
3. hence the slot is invariant under slice-preserving gauges (`gauge_slot_invariant`), so F=+1 and F=−1 are distinct classes **on the normalized slice**; with `pentagon_exactly_two`: exactly two on the slice.

**The gap (this charge):** that the reduction to the normalized slice is
without loss of generality — i.e. **every** 3-cocycle is cohomologous to an
`Fz2 f`-shaped representative. Only with this does "exactly two" hold full-stop.

**Wording note (a finding in itself).** REGISTER row 2 and the certificate
write the lemma as *"every class has a normalized representative"*; HANDOFF §5
paraphrases it as *"every class meets the normalized slice."* These are the
same claim; the certificate wording is canonical and is used throughout this
charge. The kernel docstring's *"every class meets the slice"* is the same
sentence. No discrepancy of content — only of phrasing — is recorded.

---

## 2. The precise ℤ[i]-level statement to prove

Work in the kernel's own vocabulary. A **3-cochain** is a map assigning to
each slot `(a,b,c) ∈ {0,1}³` a value in the group of **units of `Zi`**,
`U = {one, I, neg one, neg I}` (the four Gaussian units; the kernel already
carries `one`, `I`, `neg one`). Write units multiplicatively with `mul`.

**Definitions the third body will need (all zero-import):**

- **coboundary** of a vertex gauge `eta : Nat → Nat → Zi` (already in-kernel
  as `detaNum`/`detaDen`, cleared form):
  `(d eta)(a,b,c) = eta b c · eta a ((b+c)%2) / [ eta ((a+b)%2) c · eta a b ]`,
  carried as the numerator/denominator pair to stay division-free.

- **cocycle**: a 3-cochain `F` satisfying the pentagon relation. The kernel
  already encodes this via `pentagon`/`pentL`/`pentR` for the one-free-slot
  shape `Fz2 f` (`Zi.lean:520–547`); the general-cochain pentagon (the
  5-term associativity relation) is the honest predicate to add.

- **normalized (slice) representative**: a cochain of the shape `Fz2 f`
  (`Zi.lean:520`) — equal to `one` on every slot containing a `0` argument,
  free only at `(1,1,1) ↦ f`.

**THE SLICE LEMMA (the charge), kernel-honest form:**

> For every unit-valued 3-cochain `F` that is a cocycle (satisfies the
> pentagon relation over `Zi` units), there exists a vertex gauge `eta`
> into the units of `Zi` and a unit `f` such that
> `mul_pointwise F (d eta) = Fz2 f`,
> i.e. `F` differs from the normalized representative `Fz2 f` by the
> coboundary of `eta` at every slot. Consequently `f² = one` (pentagon on
> `Fz2 f`), so `f ∈ {one, neg one}`: **exactly two** normalized classes.

Equivalently, stated as a **finite decidable proposition** (the form the
reach measurement certifies): over the index sets `slots = {0,1}³`,
`gaugeslots = {0,1}²`, and `U = the four Zi units`, the statement

> `∀ F : slots → U, cocycle F → ∃ eta : gaugeslots → U, ∃ f : U,
>    ∀ s ∈ slots, mul (F s) ((d eta) s) = (Fz2 f) s`

is a bounded ∀∃ over finite sets — finite and mechanically checkable (see §4
for the hazard map and the route-independent constraints; the route itself is
the prover's to choose).

**What must NOT be claimed** (norm 6, echoing the kernel's own discipline):
the full `H³(Z₂, U(1)) = Z₂` sentence with the *continuous* unit group
`U(1)` is **out of zero-import reach** (U(1) is not representable; measured
in §3). The ℤ[i]-unit statement above is a faithful finite fragment; the
label must say "over the units of ℤ[i]", not "over U(1)". Whether the
ℤ[i]-unit fragment discharges the register's exclusion is the adjudicator's
ruling (§5), not the prover's to assert.

---

## 3. Measured zero-import reach (design probes; no Lean)

Three probes were run BEFORE writing this charge; the mathematics' sources
(bench, certificate, kernel STATEMENTS) are open to me — seat-B blindness is
for seat P's *proofs*, not the sources (HANDOFF §7). Probe outputs are the
evidence; the probe files ship with the round.

**Probe 1 & 2 — `s7a_design_probe.py`, `s7a_reach_refine.py` (SUPERSEDED,
kept as diagnostic trail).** These enumerated *arbitrary* cochains and found
the naive lemma FALSE (64/65536 normalizable over ℤ[i] units; 8/256 over the
real signs). **This was the wrong object**: a gauge class is an orbit of a
*cocycle*, not of an arbitrary function. The probes' own "counterexample"
(the cochain equal to `i` at slot (1,1,0)) was verified **not to be a
cocycle** (inline check, exit shown), so it was never a class. Recorded as
honesty note #1 below: the design probe caught a false framing before it
could become a mis-stated theorem — precisely the point of norm 15.

**Probe 3 — `s7a_cocycle_reach.py` (AUTHORITATIVE).** Restricted to cocycles
(pentagon solutions), the measured result:

| unit group | cocycles | coboundaries | gauge classes | slice lemma | classes on (1,1,1) axis | F(1,1,1) values |
|---|---|---|---|---|---|---|
| ℤ[i] units (Z₄) | 32 | 16 | **2** | **TRUE** | 2 | {+1, −1} |
| real signs {1,−1} (Z₂) | 8 | 4 | **2** | **TRUE** | 2 | {+1, −1} |

Faithfulness checks inside the probe PASS: the coboundary action reproduces
the certificate's `(dη)(1,1,1) = η₁₀/η₀₁`; slice-preservation forces
`η₀₁ = η₁₀` and fixes the slot (the in-kernel `gauge_slot_invariant`,
reproduced); coboundaries are cocycles (d² = 0).

**Reach verdict:** the ℤ[i]-unit slice lemma is a **bounded, finite,
`decide`-able** proposition and is **TRUE** as measured — therefore **IN
zero-import reach**. The impossibility clause (norm 6) fires **only** for the
continuous `U(1)` version, which is out of reach; the charge deliberately
targets the ℤ[i]-unit fragment, which is both honest and reachable.

Probe pins (short sha256, measured on the shipped files):

```
4a7f78f943a4  seatP/probes/s7a_cocycle_reach.py    ← authoritative
83fa1fd695c3  seatP/probes/s7a_design_probe.py     ← superseded (diagnostic)
828163b07963  seatP/probes/s7a_reach_refine.py     ← superseded (diagnostic)
```

---

## 4. The hazard map, and the constraints on any route (NOT a route)

*The route is the prover's to invent — this charge does not design the proof
(that would defeat the independence the co-signature rests on: seat B must
verify by a genuinely different route, norm 9, and a route pre-drawn here
would propagate any flaw of mine into the very proof meant to catch flaws).
What follows is (a) a HAZARD MAP — where earlier provers in this workshop got
bitten, so you don't pay twice — and (b) the CONSTRAINTS every acceptable
proof must satisfy, whatever route reaches them. No tactics, no code shapes,
no data representations are prescribed; choose your own.*

**Hazards carried forward (trap ledger, HANDOFF §3 — warnings, not instructions):**

- The statement is a bounded ∀∃ over finite sets. Provers have been bitten by
  `Decidable`-synthesis for a bounded ∀ *with hypotheses* — a naive appeal to
  decidability on the raw quantified goal has stalled before. How you make the
  claim mechanically checkable is your call; just know the raw shape has bitten.
- The `Classical.choice` trap (ledger item 1): a bare existential goal
  discharged by the wrong automation has silently pulled in choice before.
  This is why the axiom census below is a hard bar, not a courtesy.
- The pointwise equalities are low-degree `Zi` identities, but the cross-term
  cancellations have stalled naive simplification in past rounds (ledger item
  2). That is a known soft spot; the resolution is yours to find.

**Constraints every acceptable proof MUST meet (route-independent):**

- **Axiom bar (norm 2):** the axiom census must read **0 `sorryAx`, 0
  `Classical.choice`**. No exceptions, by any route.
- **Silence (norm 10):** compiles to zero bytes, exit 0.
- **Negative control (norm 5):** the proof must be accompanied by a control
  showing the lemma's force comes from the *cocycle* hypothesis and not from
  the normalized shape — e.g. that some non-cocycle is not normalizable, and
  that a cocycle under a wrong gauge fails to normalize. Choosing the control
  witnesses is part of the work; do not lift them from the probe.
- **Nests must tie (norm 9):** whatever you prove must be accompanied by a
  count that independently reproduces the class structure the reach probe
  measured (32 cocycles / 16 coboundaries / 2 classes over ℤ[i] units). If
  your in-kernel count disagrees with the probe, that disagreement is a
  finding and STOPS the charge (§6 note #2) — do not force the numbers to fit.
- **Label (norm 6):** "over the units of ℤ[i]", never "over U(1)" (§2).

---

## 5. The adjudicator, named at birth (norm 15)

**Adjudicator: seat B of Round Three (the blind verifier), acting under the
corrections-letter protocol, with the REGISTER as the standing court.**

Concretely, the charge is discharged only when ALL of the following hold, in
order, and seat B's letter says so:

1. **Seat P** appends the lemma + its `_card` nest + the two negative
   controls to `Zi.lean`; compiles to **silence** (0 bytes, exit 0; norm 10);
   axiom census **0 `sorryAx`, 0 `Classical.choice`** (norm 2).
2. **Courier** re-extracts statements; re-extraction is **byte-identical**
   (norm 12); seat B reads statements only.
3. **Seat B** re-derives the slice lemma by a route **genuinely independent
   of seat P's** — a different substrate or method, not a re-run of the
   prover's proof (norm 9) — reproduces the nests (32/16/2 over ℤ[i] units),
   and runs its own negative controls (norm 5).
4. **Plants, both directions** (norm 16): the verifier fails (exit 1, poisoned
   check named) on a planted defect — a cocycle deleted from a class, or an
   `Fz2 f` mislabeled — and passes on byte-identical restore.
5. **Label audit** (norm 6): the shipped theorem name and docstring say
   "over the units of ℤ[i]", never "over U(1)", and the docstring records
   that the continuous version is out of zero-import reach (this charge §3).
6. **REGISTER diff** (norm 15, round-7 strengthening): the crate-time
   checklist answer ships as a REGISTER edit — row 2's boundary changes from
   *"the G1c slice lemma … NOT bench-certified"* to the ℤ[i]-unit lemma now
   certified in-kernel, with the U(1) gap explicitly retained as the residue.

**The ruling seat B must make** (either answer is a result, norm 6): *does
the in-kernel ℤ[i]-unit slice lemma close the register's row-2 exclusion, or
does the exclusion specifically require U(1) and therefore survive as a named,
narrowed residue?* The prover does not decide this; seat B does, in the
corrections letter, and the REGISTER records the ruling.

---

## 6. Honesty notes (norm 6)

**#1 — the design probe caught a false framing.** My first two probes
enumerated arbitrary cochains and reported the slice lemma FALSE. That was a
wrong-object error, not a mathematical obstruction: the "counterexamples"
were non-cocycles (measured). Had a Lean statement been written from probe 1,
it would have been either false or vacuously mis-scoped. The probe-before-Lean
discipline (norm 15) did its job. Both superseded probes ship, headed
SUPERSEDED, as the diagnostic trail — the record travels whole (norm 12).

**#2 — reach verdict is measured, not assumed.** "IN zero-import reach" rests
on `s7a_cocycle_reach.py`'s finite enumeration (slice lemma TRUE, 2 classes,
`decide`-able), not on my expectation. The pins in §3 are on the shipped
probe files. If the third body's kernel enumeration disagrees with the
probe's counts (32/16/2), that disagreement is a finding and STOPS the charge.

**#3 — I did not write the proof, and this charge does not design it.** Per
my charter, I audit math and issue charges; I do not prove. §4 carries a
hazard map (where earlier provers were bitten) and the route-independent
constraints every acceptable proof must meet — it deliberately prescribes NO
tactic, code shape, data representation, or route, because a pre-drawn route
would (a) make the third body's proof a transcription of my design rather
than independent evidence, and (b) risk propagating a flaw of mine into the
proof meant to catch flaws. The route is the prover's; seat B verifies by a
different one (norm 9). I have written no Lean; the kernel is untouched by me.

---

## 7. Deliverables in this charge

```
CHARGE-S7a-SLICE-LEMMA.md                 ← this file
seatP/probes/s7a_cocycle_reach.py         ← authoritative reach probe  (4a7f78f943a4)
seatP/probes/s7a_design_probe.py          ← superseded diagnostic       (83fa1fd695c3)
seatP/probes/s7a_reach_refine.py          ← superseded diagnostic       (828163b07963)
```

The mathematics is stated; the reach is measured TRUE and reachable; the
adjudicator is named; no Lean is written. The charge is ready for the third
body.

*— SuperNinja instance 2, meta-auditor, Round Three. The middle holds.*
