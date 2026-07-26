# PIN TRACKER — hashes ↔ artifacts, one page

**For Kelly.** One row per pinned artifact, newest sub-round first.
Convention going forward: every sub-round adds one small block here at
ship time — artifact path, what it is, sha256 (first 12 chars are enough
to grep; full hash lives in the sub-round report). To verify any pin:
`sha256sum <path>` and compare. All paths relative to `experiment/`.

**Branch:** `superninja/dual-seat-experiment-s1` · **PR:** #2 (open; PR #1 merged S1)

---

## Round Three continuity (current)

| artifact | what | sha256 (short) |
|---|---|---|
| `README.md` | experiment front-door pointer | `1367df4b19d6` |
| `HANDOFF-ROUND3.md` | full continuity doc: Phase 0 verification, stranger protocol, trap ledger, S7 charge menu, sealed GitHub section | `537899224955` |
| `ROUND3-BOOTSTRAP-PROMPT.md` | paste-ready first message for the fresh instance | `5b587c210a24` |
| `round3-handoff.zip` | self-contained handoff (experiment + workshop-canon incl. bench + certificates), 121 files | `2c3f8ffb1965` |

commit: `e7af3ab`

## Closing artifacts

| artifact | what | sha256 (short) |
|---|---|---|
| `NORMS-RETROSPECTIVE.md` | all 16 norms scored against the experiment: 5 caught, 11 held, 0 idle; costs priced; 5 adoption proposals | `c03cf34e9254` |
| `FINAL-EXPERIMENT-REPORT.md` | the whole arc S1→S6, one document: protocol, mathematics, corrections law, independence routes, all ship pins | `d67fe1d6152c` |

commits: `9492c77` (final report), `73fa014` (retrospective)

## S6 — capstone + exclusion

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 161 thm, S1–S6, kernel-silent, census PASS (clean first) | `b7ef35425e13` |
| `courier/Zi_statements_v7.txt` | statements v7, 161 stmts | `97faef58cd0e` |
| `seatB/verify_zi_s6.py` | blind verifier, 23/23, brute exhaustion + exact elimination m=2..6 | `64bdc767c785` |

zip: `dual-seat-experiment-s6.zip` sha256 `2c94275e84fc`

commit: `26c7b2e`

## S5 — twist layer

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 141 thm, S1–S5, kernel-silent, census PASS | `e505e5192b51` |
| `courier/Zi_statements_v6.txt` | statements v6, 141 stmts | `1071e8541e39` |
| `seatB/verify_zi_s5.py` | blind verifier, 25/25, coordinate-route fork locus | `24f50d913640` |

zip: `dual-seat-experiment-s5.zip` sha256 `d5b68c7d1ff4`

commit: `90a2f0a`

## S4 — hexagon layer

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 115 thm, S1–S4, kernel-silent, census PASS | `6d51cafa7bd4` |
| `courier/Zi_statements_v5.txt` | statements v5, 115 stmts, proof-stripped | `d195b3de0ead` |
| `seatB/verify_zi_s4.py` | blind verifier, 36/36, 4-indeterminate poly ring | `acfa68424e8b` |

zip: `dual-seat-experiment-s4.zip` sha256 `3d8cc366250f`

commit: `b98fcdb` (+ `3411fab` tracker touch-up)

## S3 — pentagon necessity

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (v-S3) | 84 thm | `49e850e1f043` |
| `courier/Zi_statements_v4.txt` (final) | statements v4, 84 stmts | `1314192cf5ee` |
| `seatB/verify_zi_s3.py` | 32/32, polynomial-exact | `feac6e838ed1` |
| `dual-seat-experiment-s3.zip` | S3 delivery bundle | `e353a5af9bdf` |

commit: `e20f31a`

## S2 — the domain

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (v-S2) | 57 thm | `fbe854890a5e` |
| `courier/Zi_statements_v3.txt` | statements v3, 57 stmts | `69d7073e9e92` |
| `seatB/verify_zi_s2.py` | 24/24, two independent routes | `bc10622bce65` |

commit: `c045e6e`

## S1 — the ring

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` (v-S1) | 42 thm | `5930c54ab93a` |
| `seatB/verify_zi.py` | 47/47, exact reimplementation | `8eb939be4241` |

commits: `32a6b0c`, `b8eea58`, `4bdd0f2` (S1 arc; PR #1, merged)

---

*Full 64-char hashes: each SUBROUNDn-REPORT.md in this directory.
Older intermediate pins (v1/v2 statements, pre-crop versions) live in
those reports and are not repeated here — this page tracks only what
ships.*
