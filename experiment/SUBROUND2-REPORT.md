# SUB-ROUND 2 — S2, the domain by one mod-4 descent (quarantined)

*SuperNinja, dual-seat experiment, second sub-round. Same protocol as
sub-round 1, same honest label: one architecture, both chairs, seat
boundary procedural. Everything below marked measured was produced by
an instrument this session.*

## What shipped

- **Seat P:** S2 appended to `Zi.lean` — 15 new theorems (57 total,
  ~460 lines): `sq_mod4` (nest 4), `mod4_forces_even` (the 16-case
  core, live on exactly 4 of 16 residue pairs), `descent_core`
  (fuel-indexed structural induction, order-free — the chartered fork,
  stated), `normSq_eq_zero_iff`, `normSq_ne_zero`, `intScalar_mul`,
  `torsion_free`, `no_zero_divisors` (the chartered chain z·w = 0 ⟹
  conj(z)·z·w = 0 ⟹ N(z)·w = 0 ⟹ w = 0), four live witnesses, three
  negative controls including the **mandatory mod-2 control** (2
  ramifies; the modulus 4 is load-bearing). Compile: **exit 0, zero
  bytes, ~1.5s.** Final pin: `Zi.lean` sha256
  `fbe854890a5e839089d3c0154139695d8ff5bb11085127c3f388bc124c3c65f1`.
- **Courier:** statements v3 extracted mechanically (57 theorems,
  sha256 `69d7073e9e92b85afc0f1ff87d743911bc27e5da8453ae05fe5f01254c697951`).
- **Seat B:** `verify_zi_s2.py` — 24 checks, 24 pass, exit 0.
  Exhaustive where the nest is finite; **two independent routes** where
  the Lean took the descent (the Int-order argument the charge left
  aside, and the norm-multiplicativity route); the emod semantics
  bridge checked first; nests labeled per norm 9. Plant bitten
  (falsified live-count → exit 1, named), restored clean
  (sha256 `bc10622bce65e80acbc6b93be8717198abb6216b3aabf002a2dd859d0663f449`).

## The headline finding — the trap bit a third author, and the alarm held

Seat P's S2 first draft shipped **six theorems carrying
Classical.choice**: `omega` closing conjunctive goals — exactly
HANDOFF.md's twice-bitten trap, bitten a third time in a third
author's hands. **The census caught it the same run** (ALARM, exit 1);
repaired by splitting every conjunctive goal before omega; re-censused
**0 sorryAx, 0 Classical.choice**. This is the workshop's register-age
law confirmed once more: the defect was younger than its adjudicator,
so it died on schedule. The correction rides loudest-first in the
compile transcript, per norm 4.

## Seat B's crop (letter in tree)

1. `sq_mod4` proved but orphaned — the 16-case core re-derives its
   facts inline; repaired with an honest ROLE label (standing
   testimony, flat term graph on purpose).
2. `descent_core`'s anti-vacuity count is exactly 1 (the fixed point)
   — the honest norm-3 statement for a descent theorem; count now in
   the file comment, with the note that S3's forcing instance repeats
   the 1-of-N shape.
3. The chartered Z[i]/5 control deferred to S3 with stated reason —
   judged in-bounds; seat B re-verified the /5 split independently
   anyway (`negcontrol_mod5_splits`), so the fact is on record on both
   sides of the seat boundary.

## Running score, two sub-rounds in

| | sub-round 1 (S1) | sub-round 2 (S2) |
|---|---|---|
| theorems | 42 | 57 cumulative |
| kernel | silent, ~0.6s | silent, ~1.5s |
| census | 0/0, plant bitten | 0/0, **live ALARM fired** (Classical.choice ×6, repaired) |
| seat B checks | 47/47, plant bitten | 24/24, plant bitten |
| crop | 1 norm-7 conviction, repaired | 2 labels applied + 1 deferral judged |
| corrections law | confirmed (defect in first delivery, caught cross-seat) | confirmed (trap's third bite, caught by pre-existing alarm) |

S3 (pentagon necessity) is the natural next sub-round: the 16-instance
classification, f² = 1 forced at (1,1,1,1), the factorization, both
roots landing, the Z/8 four-roots control, the f = i residual-4
control — and the slice-plus-invariance wording discipline (charter
flag 2) will be the first PROSE-heavy target, which is exactly where
the dual-seat mode is weakest and the experiment most informative.

The middle holds.

*— SuperNinja, sub-round 2, quarantined*
