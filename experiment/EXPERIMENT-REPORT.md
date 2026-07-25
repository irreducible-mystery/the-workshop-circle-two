# THE DUAL-SEAT EXPERIMENT — one architecture, both chairs, S1 as the test article

*SuperNinja (meta-auditor, REGISTER row 7) → Kelly, and through her to
the builder and the third body. Norm 16 applies to this whole
directory: it is QUARANTINED — a new instrument's first output is
claims to verify, not results to report. This report says so in its
first paragraph on purpose. Nothing here entered `main`; everything
rides on a fresh branch for the seats of record to adjudicate.*

## What was asked

Kelly asked whether this architecture can host the flow that Circle
One ran between two Claude seats (Fable 5 as builder, Ultracode as
third body): charge → prove → extract → blind reimplement → corrections
→ repair → re-verify, with instruments as the authority throughout.
The test article: **S1 of Circle Two's live charge** (ROUND1.md — the
Z[i] ring layer), the smallest chartered section (norm 11).

## What happened, in ferry order

1. **Environment parity first.** The pinned toolchain
   (`leanprover/lean4:v4.32.0`) installed clean in this container; all
   six Circle One files recompiled **exit 0, zero bytes** (Interchange
   0.6s, MagicSquare 45s, Anyon 75s, Exchangeable 12s, Verlinde 3s,
   Rigidity 98s), source hashes matching VERIFY.md's stamped prefixes
   exactly. Both floors run 29/29. The Circle Two certificate closed
   **70/70, exit 0** with `C1_LEAN` pointed at the ferried Circle One
   crate (sha256 `c269c755…` — matching the README's pin exactly).
2. **Seat P (prover)** wrote `seatP/Zi.lean` per ROUND1.md §S1: zero
   imports, hand-rolled ring in Circle One's house style (the
   simp-only-distribute-then-omega pattern from Anyon.lean:677–713,
   conjunctive goals split before omega per the HANDOFF trap). Compile:
   **exit 0, zero bytes, ~0.6s. 42 theorems, 281 lines.** Census
   (`axioms_zi.sh`, re-instantiated from Circle One's `axioms.sh`
   pattern — REGISTER row 4's declared frontier, now instantiated for
   this tree): 42/42 covered, 16 axiom-free, **0 sorryAx, 0
   Classical.choice**. The census **bit a planted `sorry`** (exit 1,
   named) and passed clean on byte-identical restore — norm 16, both
   directions.
3. **The courier step was a script, not a hand.** `courier/` holds a
   mechanical extractor that strips every proof body and ships
   statements + definitions only (42 theorems, pinned by sha256).
   Seat B read only that file.
4. **Seat B (builder)** reimplemented every claim in exact Python
   (`seatB/verify_zi.py`): a from-scratch polynomial-arithmetic layer
   over Z — so each universal claim is checked by **coefficient
   equality, complete over all integers**, not sampled — plus concrete
   grids as co-signature (nests 25/625, tied per norm 9). Result:
   **47/47, exit 0.** The instrument **bit a plant** (a falsified
   witness transcription → exit 1, exactly the poisoned check) and
   passed clean on restore — norm 16, both directions.
5. **The corrections pass drew blood, loudest first.** Seat B's letter
   (`seatB/CORRECTIONS-LETTER.md`) convicted seat P's first delivery
   of a **norm-7 specimen**: `sub_eq_add_neg` was the definition of
   `sub` restated — `rfl`, a check that cannot fail. Two further
   findings labeled (an iff asymmetry in the checker itself; prose-only
   anti-vacuity), one charge deviation flagged for the seats of record.
6. **The repair closed the loop.** Seat P replaced the vacuous theorem
   with `sub_add_cancel` ((z − w) + w = z — independent content, not
   definitional), recompiled silent, re-ran the census clean; the
   courier re-extracted (v2, one-line diff, re-pinned); seat B updated
   the one check and re-verified **47/47**. Final artifacts:
   `Zi.lean` sha256 `5930c54a…`, `verify_zi.py` sha256 `8eb939be…`.

## The finding — capability

**The architecture can run the whole loop.** Kernel, floor,
certificate, gates, census, plants, blind extraction, exact
reimplementation, corrections, repair, re-verification: all of it ran
in one container, every instrument green, every alarm seen firing
before being trusted. Wall-clock for the full S1 cycle: under one
hour, most of it thinking rather than computing.

## The finding — epistemics (the honest one)

The corrections law held even here: the first delivery shipped a
defect, the adversarial pass caught it, and it was exactly the species
the norms predict (a check that cannot fail — norm 7). That the catch
happened **across a seat boundary inside one architecture** is the
experiment's real datum. What it does NOT establish: that the boundary
is as strong as two strangers. The blindness was procedural (proof
bodies stripped by script; seats in separate sessions and trees), not
architectural — one substrate wrote both sides, and prose classes
(REGISTER rows 6/8) lose the most protection. Priced accordingly:

- **Instruments' authority: undiminished.** Exit codes and coefficient
  equality do not care who runs them. The two-body *mechanical*
  structure (kernel + exact reimplementation) survives intact.
- **Prose adjudication: weakened, labeled.** A characterization slip
  shared by both seats would pass both. Kelly's seat and the original
  two bodies remain the true strangers; this mode should feed them,
  not replace them.
- **Proposed register row (for the seats of record to adopt or
  refuse):** *"single-architecture dual-seat deliverables"* —
  adjudicator: both seats' instruments PLUS one true-stranger pass
  (the third body or the builder of record) before anything is called
  verified; boundary: prose about the deliverables stays this seat's
  register (row 7), quarantined.

## What this branch does NOT do

It does not touch `main` or the third body's branch; it does not claim
S1 for the round (the third body's charge stands — this is a rehearsal
on the same target, and can serve the third body as an independent
cross-check if the seats of record want it); it does not co-sign
anything into the two-body record.

## The inventory (all pins measured this session)

| artifact | what | pin (sha256) |
|---|---|---|
| `experiment/seatP/Zi.lean` | 42 theorems, zero imports, compiles silent on v4.32.0 | `5930c54ab93a22de1cf9a28e6b31193116817c8c3e6a58552c69e05553bdc46a` |
| `experiment/seatP/axioms_zi.sh` | census instrument (row-4 pattern), plant-bitten | in tree |
| `experiment/seatP/axioms-zi.txt` | census output: 42 covered, 16 axiom-free, 0/0 | in tree |
| `experiment/seatP/transcript-zi.txt` | compile transcript, machine + toolchain + timing | in tree |
| `courier/Zi_statements.txt` / `_v2.txt` | mechanical extractions (v1/v2) | `b37dd421…` / `12ea1133…` |
| `experiment/seatB/verify_zi.py` | exact reimplementation, 47 checks, plant-bitten | `8eb939be4241cfc2518c81afc93631e146df0e134a5aad3769f454b57e7fa58b` |
| `experiment/seatB/verify_zi_output.txt` | 47/47 clean run | in tree |
| `experiment/seatB/CORRECTIONS-LETTER.md` | the crop: one norm-7 conviction + two labels | in tree |

The middle holds — and this time it was asked to hold inside one mind,
and the instruments still would not let a vacuous theorem through.

*— SuperNinja, dual-seat experiment, quarantined per norm 16*
