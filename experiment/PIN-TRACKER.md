# PIN TRACKER — hashes ↔ artifacts, one page

**For Kelly.** One row per pinned artifact, newest sub-round first.
Convention going forward: every sub-round adds one small block here at
ship time — artifact path, what it is, sha256 (first 12 chars are enough
to grep; full hash lives in the sub-round report). To verify any pin:
`sha256sum <path>` and compare. All paths relative to `experiment/`.

**Branch:** `superninja/dual-seat-experiment-s1` · **PR:** #2 (open; PR #1 merged S1)

---

## S4 — hexagon layer (current)

| artifact | what | sha256 (short) |
|---|---|---|
| `seatP/Zi.lean` | 115 thm, S1–S4, kernel-silent, census PASS | `6d51cafa7bd4` |
| `courier/Zi_statements_v5.txt` | statements v5, 115 stmts, proof-stripped | `d195b3de0ead` |
| `seatB/verify_zi_s4.py` | blind verifier, 36/36, 4-indeterminate poly ring | `acfa68424e8b` |

commit: *(added at ship — see PR #2 comment)*

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
