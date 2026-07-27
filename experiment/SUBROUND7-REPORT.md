# SUB-ROUND 7 — the slice lemma, over the units of Z[i]

*From the third body (seat P, Round Three) to Kelly, for carriage to the
meta-auditor and the seats of record. This discharges
`CHARGE-S7a-SLICE-LEMMA.md` and corrections-letter items 2 and 3. Seat B's
verification, the ruling on REGISTER row 2, and this round's findings are in
`seatB/CORRECTIONS-LETTER-S7.md`, which should be read second.*

---

## 0. What shipped, in two crates

Norm 17 says a repair and the first thing that depends on it never ride in the
same crate. The S7a kernel work reads statements the courier cuts, so the
courier repair had to land and be verified **alone** first.

| crate | what | kernel |
|---|---|---|
| 1 | the courier repair (items 2, 3) + the round's inheritance | UNCHANGED at `b7ef35425e13` |
| 2 | the S7a slice lemma, statements v8, seat B's verifier, plants, the ruling | `848282f2e3a2` |

Crate 1 was checked out from the index into a clean tree and its gates run
there, against the untouched S6 kernel, before crate 2 was begun.

## 1. The charge, discharged

**`slice_lemma_over_zi_units`** — every unit-valued 3-cochain satisfying the
pentagon (cocycle) relation is cohomologous to a normalized `Fnorm f`
representative, with `f = one ∨ f = neg one`. Stated in the kernel's own
division-free cleared form against `detaNum`/`detaDen`, the G1c coboundary
pair that was already in the file.

**The witnesses are explicit and read off the cochain**, never searched for:

```
eta(1,0) = F(1,0,0)      eta(0,1) = conj F(0,0,1)      eta(0,0) = eta(1,1) = 1
f        = F(1,1,1) · F(1,0,0) · F(0,0,1)
```

That is the whole content of the lemma. Nothing is quantified over that is not
constructed, which is why the axiom census shows **0 `Classical.choice`** with
no special pleading: there is no existential to discharge by choice.

**Route.** The charge §4 recommended stating the finite ∀∃ as one `decide` over
an explicit index list. That route is not reachable: the cochain space is
4⁸ = 65536, and `decide` cannot evaluate it inside the kernel's budget without a
`set_option` raise, which the HANDOFF guardrail forbids and which this file has
never used. So the proof is **structural** instead. Five of the eight slots are
*forced* by single pentagon instances —

| slot | forced to | from instance |
|---|---|---|
| (0,0,0) | `one` | (0,0,0,0) |
| (0,1,0) | `one` | (0,1,0,0) |
| (1,1,0) | `conj F(1,0,0)` | (1,1,0,0) |
| (0,1,1) | `conj F(0,0,1)` | (0,0,1,1) |
| (1,0,1) | `F(0,0,1)·F(1,0,0)` | (1,0,0,1) |

— leaving exactly three free unit parameters, and the (1,1,1,1) instance then
forces `(F(1,1,1)·F(1,0,0)·F(0,0,1))² = one`. S3's own `f_sq_one_iff_pm_one`
turns that into `f ∈ {+1, −1}`. The eight slot equations are then checked one
by one against the constructed gauge.

**The tie back to S3.** `Fnorm_eq_Fz2` proves the normalized shape used here IS
the kernel's `Fz2` read on its admissible slots, and
`exactly_two_over_zi_units` returns the reached representative as a solution of
S3's own `pentagon` predicate. The lemma strengthens the existing headline
rather than standing beside a look-alike.

## 2. The counts, tied to the objects (norm 9)

The design probe measures 32 / 16 / 2. The kernel reproduces all three, and —
this is the part that matters — the counts are tied to the *cocycles*, not to
an index set that resembles them:

- **32 cocycles** of 64 parameter triples — `s7_nest_cocycles_32`, made a count
  of objects by `cocycle_is_cochainOf` (forward: every cocycle is the
  parametrized shape of its own three values), `cochainOf_is_cocycle`
  (backward: every admitted triple really is a cocycle, so 32 is not an upper
  bound), `cochainOf_injective` (no overcount), and `cocycle_triple_in_nest`
  (membership).
- **16 coboundaries** of 4⁴ = 256 gauges — in two halves: every gauge has the
  coboundary of its normalized form, and the 16 normalized forms are pairwise
  distinct.
- **2 classes, 16 + 16 = 32** — `s7_nest_classes_2`.

**One honest note on the sweeps.** The 256-gauge checks run as coordinate-wise
nests (4 × 4 × 4 × 4) rather than one flat traversal, and `gaugeQuads` is not
built as a 256-element list at all. That is not stylistic: a flat traversal
exceeds the evaluation depth, and the fix available in the tactic language is
`set_option maxRecDepth`, which is a budget raise. Restructuring was chosen
over raising, so the file still contains **no `set_option` anywhere in 2566
lines**.

## 3. Negative controls (norm 5), in the two directions the charge named

- **The cocycle hypothesis is load-bearing.**
  `control_A_not_a_cocycle_and_never_normalized`: the superseded probes'
  witness (`i` at (1,1,0)) is unit-valued, is **not** a cocycle, and **no**
  gauge normalizes it — all 256 gauges × 4 units fail, checked in-kernel. The
  trap the charge paid for is now an instrument.
- **The constructed gauge is load-bearing.**
  `control_B_identity_gauge_fails` on `cochainOf I one I`, a genuine cocycle:
  the identity gauge fails at the (1,0,0) slot. `live_slice_gauge_normalizes`
  shows the **same** cochain normalized at all 8 slots by the gauge the lemma
  builds. The pair isolates the construction as the content.

Anti-vacuity (norm 3): both classes are inhabited by named cocycles, and the
lemma is exercised off the real axis *and* off the slice.

## 4. Measurements

```
kernel        lean Zi.lean            exit 0, 0 bytes (norm 10)
              195 theorems, 43 defs, 2566 lines
census        sh axioms_zi.sh         195/195 covered, 0 sorryAx,
                                      0 Classical.choice — RESULT: PASS
courier       extract v8              195 theorems; re-extraction byte-identical
gates         s7c_transcription.sh    T1 PASS, T2 PASS
              s7c_statements_purity.sh 0 prose-leak lines, PASS
plants        plant_s7_courier.sh     5 bitten, 5 restores — PASS
              plant_s7_slice.sh       6 bitten, restores byte-identical — PASS
seat B        verify_zi_s7.py         43/43, exit 0
C2 gates      audit/c2_gates.sh       every instrument green
```

## 5. Pins (first 12 chars; `sha256sum <path>` to verify)

```
848282f2e3a2  seatP/Zi.lean                     ← 195 thm (was b7ef35425e13, 161)
03d6b71770c1  seatP/s7_section.lean             ← the S7 section alone
36101a90232d  courier/Zi_statements_v8.txt      ← statements v8 (S1..S7)
568d8a6d9a59  courier/Zi_statements_v7.txt      ← RE-CUT (was 97faef58cd0e)
d3093b7e76f9  courier/extract_statements.py     ← repaired (was aac64a45c6f4)
9737784cc5a4  seatB/verify_zi_s7.py
6808236b13bf  seatB/verify_zi_s7_output.txt
d14fe0fc5419  audit/s7c_transcription.sh        ← bumped to v8, TAG parameterized
1baa46a44831  audit/s7c_statements_purity.sh    ← recursion repaired, bumped to v8
72d1acb28c0c  audit/plant_s7_courier.sh
3b2ce48bfe79  audit/plant_s7_slice.sh
4a7f78f943a4  seatP/probes/s7a_cocycle_reach.py ← unchanged, as received
```

## 6. What I did NOT do

- **I did not claim U(1).** No theorem name or docstring in S7 says it; the
  section records that the continuous version is out of zero-import reach; the
  verifier audits this mechanically and the plant harness renames a lemma to
  `slice_lemma_over_U1` and watches that audit go red.
- **I did not make the row-2 ruling as seat P.** It is seat B's, and it is in
  the corrections letter. Read that letter before treating row 2 as settled —
  it also carries a finding about the bench sentence the exclusion is anchored
  to, and a plain statement of what this crate's dual-seat structure is worth.
- **I did not touch the frozen sources.** The one edit to
  `FINAL-EXPERIMENT-REPORT.md` was the §10 crop already applied under Kelly's
  sanction; I carried it in and checked its replacement sentence against the
  two theorems it names.

*— the third body, seat P, Round Three. The middle holds.*
