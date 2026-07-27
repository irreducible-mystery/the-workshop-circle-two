# S7A DESIGN NOTE — "every class meets the normalized slice"

*Seat: seatMETA (meta-auditor, REGISTER row 7). Norm 15: this note
records the design probe, the measured reach, the honest verdict, and
the named adjudicator, BEFORE the theorems were written into `Zi.lean`.*

---

## 1. The charge and the sanctioned divergence

Kelly's Round-Three charge, chosen from the meta-auditor's
recommendation, is **S7c+S7a in that order** — a sanctioned reordering
of the predecessor's S7a-first plan. S7c (the prose-gate scope
extension) shipped first; S7a follows as the stretch goal. This
divergence is recorded here, in the commit message, and in
`SUBROUND7-REPORT.md` (house rule: source + commit + report, every
time).

REGISTER row 2 flags one claim inside the certificate as **NOT
bench-certified**: the G1c slice lemma — *"every class meets the
normalized slice."* Equivalently the *"H³(Z₂)=Z₂"* sentence: *"every
gauge class of pentagon solutions has a normalized representative."*
Round Two deliberately held the wording boundary (slice-plus-invariance
only) **because that sentence was unproven**. The handoff named it "the
single most valuable unproven statement in the record" and predicted the
hard part would be **stating it honestly at kernel level** — what
"class" and "meets" mean without cohomology machinery.

## 2. The probe (norm 15 — measures reach, ships nothing)

Three standalone zero-import Lean files, each compiled `exit 0` /
0 stderr bytes:

- `seatP/probes/s7a_design_probe.lean` — can the sentence be **stated**? Defines
  `FSym` (a general 6-index F-symbol), `admissible`, `sliceSym`,
  `onSlice`, a `Gauge`, a `gaugeEquiv` relation, and
  `everyClassMeetsSlice`. **Verdict: it type-checks.** The sentence IS
  statable machinery-free. The wall the handoff predicted is not in
  stating the target but in writing the gauge ACTION on a *general*
  6-index object — the associator index bookkeeping (which index pair
  each η factor attaches to). `Zi.lean` sidesteps this by working at the
  single (1,1,1) slot plus two zero-slot rows; it never forms the action
  on a general G.
- `seatP/probes/s7a_design_probe2.lean` — the FINITE skeleton. `liveSlots` (the 8
  admissible (a,b,c) slots), `live_count = 8`, `slot_111_live`,
  `free_slots_count = 1`, `pinned_slots_count = 7`. All by `decide`.
  **Verdict: the skeleton is finite and provable.** 8 live slots, 1
  free, 7 to pin, 4 gauge d.o.f.
- `seatP/probes/s7a_design_probe3.lean` — route (i): the units of Z[i] are the
  **finite group {1,i,−1,−i}**. `units_have_normSq_one`,
  `units_distinct` (4 distinct), `units_closed_mul` (4×4 table),
  `unit_slice_slot_invariant`, and `unit_slice_iff_symmetric` — all by
  `decide`. **Verdict: a unit-restricted form is fully decidable.**

## 3. The honest verdict (measured, not asserted)

| piece | reach | evidence |
|---|---|---|
| STATE the sentence machinery-free | **in reach** | probe 1 type-checks |
| finite skeleton (8/1/7/4) | **in reach** | probe 2, all `decide` |
| unit-valued slice iff + orbit closure | **in reach** | probe 3, `decide` over 4⁴ |
| FULL sentence over all of Z[i] | **out of zero-import reach** | needs H³(Z₂,U(1)) = 0 |

The full sentence would require proving the **surjectivity of the
3-coboundary** onto the 7 pinned slots for an *arbitrary* (not
unit-restricted) pentagon solution — that IS the vanishing of
H³(Z₂,U(1)), i.e. cohomology machinery outside zero-import reach. Per
**norm 6** (no weak statement wearing a strong name), `Zi.lean` does NOT
claim it. The measured impossibility is stated as a live theorem
(`s7a_nonunit_outside_alphabet`: the non-unit value ⟨2,0⟩, norm 4, sits
outside the decided unit locus — a concrete marker that the unit
restriction is real, not cosmetic).

## 4. What shipped (the sharpest reachable fragment)

Eleven theorems appended to `Zi.lean` (161 → 172 total), inside
`namespace Zi`, reusing the existing `norm_one_units`, `detaNum`,
`detaDen`, `normSq`, `mul` — no re-derivation (norm 6):

1. `s7a_units_have_norm_one` — soundness of the unit alphabet.
2. `s7a_units_complete` — **completeness, reusing `norm_one_units`** (no
   new search box).
3. `s7a_unit_alphabet_nest` — 4 distinct (nest, norm 9).
4. `s7a_live_slot_count = 8`, `s7a_free_slot_count = 1`,
   `s7a_pinned_slot_count = 7` — the finite skeleton (nest, norm 9).
5. **`s7a_unit_slice_iff_symmetric`** — THE CORE: over all 4⁴ = 256 unit
   gauges, slot-fixed ⟺ slice-symmetric (η01 = η10). Strictly stronger
   than `gauge_slot_invariant` on the unit locus: it adds the CONVERSE
   (no unit gauge moves a symbol off the two-class slice without moving
   the slot) — the honest content of "meets".
6. `s7a_unit_slice_orbit_closed` — the "meets" direction: every
   symmetric unit gauge fixes the slot.
7. `s7a_live_unit_gauge` — live witness (norm 3): η11 = i, off identity.
8. `s7a_control_asymmetric_unit_moves_slot` — negative control (norm 5):
   asymmetry genuinely moves the slot.
9. `s7a_nonunit_outside_alphabet` — the measured-impossibility marker.

## 5. Norm 10 / norm 16 / axiom discipline (all measured on shipped)

- **Norm 10** — `lean Zi.lean` compiles `exit 0`, **0 stderr bytes**
  (2080 lines).
- **Axioms** — census `axioms_zi.sh` PASS: 172/172 covered, 77
  axiom-free, **0 sorryAx, 0 Classical.choice**. Every S7a theorem's
  footprint is the house standard ([propext,Quot.sound] / [propext] /
  axiom-free) — the Classical.choice trap the record warns of is
  avoided. Evidence: `seatMETA/s7a_axioms_out.txt`.
- **Norm 16 (Lean, both directions)** — plant #1 (`s7a_live_slot_count`
  8→9) bitten `exit 1`; plant #2 (the core iff RHS → `n11=n11`, a false
  universal) bitten `exit 1`; restore clean `exit 0` / 0 bytes.
  Evidence: `seatMETA/s7a_plant1_out.txt`, `s7a_plant2_out.txt`,
  `s7a_clean_out.txt`. Census-instrument plant (a `sorry` in an S7a
  theorem) triggers the `sorryAx` ALARM; restore byte-identical.
- **Norm 16 (seat B, both directions)** — `seatB/verify_zi_s7a.py`
  reproduces all 11 claims blind (11/11, `exit 0`); planted defect
  (drop `I` from the unit alphabet) → 9/11, `RESULT: FAIL`, `exit 1`;
  restore → 11/11. The independent sweep found **64 slot-fixed = 64
  symmetric** of 256 — the iff is tight on both sides, matching Lean's
  `decide`. Evidence: `seatB/s7a_seatB_out.txt`.

## 6. Named adjudicator

**Adjudicator: seatMETA (this instance), acting under the courier
(Kelly)'s Round-Three charge.** The blind cross-check is seat B
(`verify_zi_s7a.py`), which never saw the Lean proof route — only the
mechanically-extracted statements (`courier/Zi_statements_v8.txt`,
sha256 914a80d58d71…d5b5). Any dispute over whether the shipped fragment
honestly bears the name "meets the slice" is adjudicated against §3–§4:
the fragment is unit-valued and says so in its name (`unit_…`), the full
sentence is explicitly disclaimed here and in `Zi.lean`'s S7a header, and
the impossibility is a live theorem, not a comment.

## 7. Pins (measured on the shipped artifacts)

| artifact | sha256 |
|---|---|
| `seatP/Zi.lean` (with S7a) | `d1f3617baaefcbb85b049709ffee600dbdc6a20b8748edcb637fea4d8291145d` |
| `seatP/axioms-zi.txt` | `1de8439c2de3477099aa7315166186671b0885cad0f44925ac693fef5c7c3599` |
| `courier/Zi_statements_v8.txt` | `914a80d58d710de0d3273ca144d5e2e44966bb295e65c5f0791c6b8a02e1d5b5` |
| `seatB/verify_zi_s7a.py` | `077fb33e25a9684c46065837900e16fb8e1eb6be4a33d72febbed61b4ce7dbe0` |
| `seatB/s7a_seatB_out.txt` | `4e741fbbe5c97f68769f44b1abb7995d97bc78711fd068bf1aca45897482b308` |
