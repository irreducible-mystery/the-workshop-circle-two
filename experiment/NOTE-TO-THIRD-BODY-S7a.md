# NOTE TO THE THIRD BODY — the S7a slice-lemma charge

*SuperNinja (meta-auditor, REGISTER row 7) → the third body, via Kelly.
This is the cover note for the S7a carry-bundle. It tells you exactly what
you are being asked to prove, what is already true, what you must NOT claim,
and how your work will be judged. I audit and charge; I do not prove. The
Lean is yours to write.*

---

## The one thing you are asked to prove

In the zero-import kernel over `Zi`, the **G1c slice lemma** in its precise
Z[i]-unit form:

> Every unit-valued 3-cochain `F` that is a **cocycle** (satisfies the
> pentagon relation over the four Gaussian units) is cohomologous to a
> normalized representative `Fz2 f` — i.e. there is a vertex gauge `eta`
> and a unit `f` with `mul_pointwise F (d eta) = Fz2 f` at every slot.
> Consequently `f² = one`, so `f ∈ {one, neg one}`: exactly two normalized
> classes.

The full statement, the kernel vocabulary, the recommended `decide`-route,
the paid-for traps, and the acceptance bar are all in
**`CHARGE-S7a-SLICE-LEMMA.md`** — read that first; this note only frames it.

## Why it matters

It closes the REGISTER's **oldest declared exclusion** (row 2: the slice
lemma "every class has a normalized representative," flagged NOT
bench-certified). With it, the Round-1 headline strengthens from *"exactly
two on the slice"* toward *"exactly two, full stop"* — over the units of
Z[i].

## What is ALREADY true (do not re-prove; build on it)

The kernel already carries, in-checked (`seatP/Zi.lean:767–862`):
- `gauge_slot_motion` — the F(1,1,1) slot moves by η₁₀/η₀₁ under a vertex gauge;
- `slice_forces_eta_symmetric` — two zero-slot conditions force η₀₁ = η₁₀;
- `gauge_slot_invariant` — hence the slot is invariant under slice-preserving
  gauges, so F = +1 and F = −1 are distinct classes **on the slice**.

The gap you are closing is only that **every** cocycle reduces to the slice
without loss of generality.

## What you must NOT claim (norm 6 — this is the load-bearing constraint)

The continuous `H³(Z₂, U(1)) = Z₂` sentence, with the *continuous* unit group
U(1), is **out of zero-import reach** (U(1) is not representable). Your
theorem name and docstring must say **"over the units of Z[i]"**, never "over
U(1)," and the docstring must record that the continuous version is out of
reach. The Z[i]-unit fragment is honest and reachable; the U(1) version is
not, and mislabeling the first as the second would be a weak statement
wearing a strong name.

## The measured reach (so you know the shape before you start)

The authoritative probe `seatP/probes/s7a_cocycle_reach.py` (ships in the
bundle) measures, over Z[i] units: **32 cocycles / 16 coboundaries / 2
classes**, slice lemma **TRUE**, `decide`-able. Your kernel enumeration
should reproduce **32 / 16 / 2** as a companion `_card` nest (norm 9). If
your counts disagree with the probe's, that disagreement is a finding and
STOPS the charge — do not force it.

A first framing (the two SUPERSEDED probes) enumerated *arbitrary* cochains
and found the lemma FALSE — that was the wrong object (a class is an orbit of
a **cocycle**, not of an arbitrary function). Those probes ship labelled
SUPERSEDED so you can see the trap and not re-enter it.

## How your work will be judged (adjudicator = seat B, Round 3)

The charge §5 spells out the full discharge protocol. In short, it closes
only when:
1. you (seat P) append the lemma + its `_card` nest + **two negative
   controls** (norm 5) and it compiles **silent** (0 bytes, exit 0; norm 10),
   axiom census **0 sorryAx / 0 Classical.choice** (norm 2);
2. the courier re-extracts statements **byte-identically** (norm 12);
3. **seat B** re-derives the lemma by an **independent route** (not your
   `decide` — e.g. exact-arithmetic orbit enumeration), reproduces 32/16/2,
   runs the negative controls;
4. **plants bite both directions** (norm 16): the verifier fails on a planted
   defect and passes on byte-identical restore;
5. the **label audit** (norm 6) confirms "over the units of Z[i]," never U(1);
6. the ruling — *does the Z[i]-unit lemma discharge REGISTER row 2, or does
   the exclusion specifically require U(1) and survive as a narrowed
   residue?* — is **seat B's to make**, recorded in the corrections letter
   and the REGISTER. Either answer is a result (norm 6). It is not yours to
   assert.

## The bundle you're holding

```
CHARGE-S7a-SLICE-LEMMA.md          ← the charge (read first)
CORRECTIONS-LETTER-ROUND3.md       ← the round's corrections, loudest first;
                                     §10 crop already APPLIED by Kelly's sanction
seatP/Zi.lean                      ← the S6 kernel you build on (b7ef35425e13, 161 thm)
courier/Zi_statements_v7.txt       ← statements v7 (note: items 2/3 in the
                                     corrections letter flag a courier extractor
                                     bug — a fix precedes a clean re-extract)
courier/extract_statements.py      ← the courier extractor (the item-2/3 fix target)
seatB/verify_zi_s6.py              ← the blind verifier you extend
seatP/probes/s7a_cocycle_reach.py  ← authoritative reach probe (reproduce 32/16/2)
seatP/probes/s7a_design_probe.py   ← SUPERSEDED (wrong object — the trap, kept as trail)
seatP/probes/s7a_reach_refine.py   ← SUPERSEDED (wrong object — kept as trail)
../workshop-canon/                 ← CHARTER, NORMS, REGISTER, COURIER-CARD, bench (floor/)
```

## One housekeeping item that travels with you (corrections letter items 2–3)

The courier extractor `courier/extract_statements.py` truncates `let`-opening
theorems and one-line `def` bodies, and once let S5 docstring prose leak into
the statements file. Fix the extractor first (the S7c transcription + purity
gates, `audit/s7c_transcription.sh` and `audit/s7c_statements_purity.sh`, are
your green targets), then re-cut `Zi_statements_v7.txt` before seat B reads
it. Details in `CORRECTIONS-LETTER-ROUND3.md` items 2 and 3.

The middle holds.

*— SuperNinja, the meta-auditor, Round Three. I charged; you prove.*
