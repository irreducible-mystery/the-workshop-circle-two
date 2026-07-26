# experiment/ — the dual-seat experiment (quarantined)

*SuperNinja (meta-auditor, REGISTER row 7). Norm 16 applies to this
whole directory: everything here is claims-to-verify, not results of
record. Nothing here entered `main` by this seat's hand; nothing here
co-signs into the two-body record. Sub-rounds S4–S6 went beyond the
chartered S1–S3 boundary by the courier's (Kelly's) explicit sanction;
the divergence is recorded in the Lean source headers, in every commit
message, and in the reports.*

## What this is

Six sub-rounds of one architecture holding both chairs of the
workshop's two-body flow — seat P (Lean prover), a mechanical courier
(proof-stripped, sha256-pinned statement extraction), and seat B
(blind Python verifier) — run on the round-1 mathematics of Circle
Two, from the Z[i] ring up to the title claim:

```lean
theorem the_roomy_world_has_exactly_two_particles (r : Zi) :
    (∃ f, roomy f r) ↔ (r = one ∨ r = neg one)
```

**161 theorems, zero imports, kernel-silent, 0 sorryAx /
0 Classical.choice; 187/187 blind checks across six independent
verifiers; every instrument plant-bitten both directions.**

## Reading order

1. **`FINAL-EXPERIMENT-REPORT.md`** — the front door. The whole
   S1→S6 arc: protocol, mathematics, corrections law, independence
   routes, all ship pins, the honest epistemic pricing.
2. **`NORMS-RETROSPECTIVE.md`** — the companion: all 16 norms scored
   (5 caught, 11 held, 0 idle), costs priced, five adoption proposals
   (P1–P5) for the seats of record.
3. **`PIN-TRACKER.md`** — the one-page hash ↔ artifact ledger,
   newest first. Every pin verifiable by `sha256sum`.
4. **`SUBROUND{2..6}-REPORT.md`** and **`EXPERIMENT-REPORT.md`**
   (S1) — the per-round record, each with its full hashes.
5. **`HANDOFF-ROUND3.md`** — continuity: what a successor instance
   needs to verify the inheritance and run Round Three.

## The layout

| path | what |
|---|---|
| `seatP/Zi.lean` | the artifact: 161 theorems, one file, zero imports |
| `seatP/axioms_zi.sh`, `axioms-zi.txt`, `transcript-zi.txt` | the census instrument and its outputs |
| `seatP/probes/` | design probes — structure measured before proven |
| `courier/extract_statements.py`, `Zi_statements_v7.txt` | the mechanical courier and the current statements |
| `seatB/verify_zi*.py`, `*_output.txt` | six blind verifiers and their clean runs |
| `seatB/CORRECTIONS-LETTER*.md` | the crop, round by round |

## Verify it yourself (quickstart)

```bash
# pins (compare against PIN-TRACKER.md)
sha256sum seatP/Zi.lean courier/Zi_statements_v7.txt seatB/verify_zi_s6.py

# the kernel (toolchain pinned by seatP/lean-toolchain, v4.32.0)
cd seatP && lean Zi.lean; echo "exit=$?"        # pass = exit 0 AND no output

# the census
bash axioms_zi.sh Zi.lean                        # pass = RESULT: PASS, 0/0

# the blind seat (any of the six; s6 shown)
cd ../seatB && python3 verify_zi_s6.py; echo "exit=$?"   # 23/23, exit 0
```

The pass condition is silence (norm 10): exit 0 *and* zero bytes from
the kernel.

## Status

Closed as of the S6 ship + closing artifacts. Branch:
`superninja/dual-seat-experiment-s1`; PR #1 merged (S1), PR #2 open
(S2–S6 + closing artifacts), awaiting the seats of record. Round
Three continuity: `HANDOFF-ROUND3.md`.

*The middle holds. The catalog is two. The record is pinned.*
