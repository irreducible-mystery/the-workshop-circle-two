# The Workshop — Circles Two and Three

*The roomy world: exactly two particles. Then the chartered leftovers.
Both circles COMPLETE and SEALED.*

**New here? Read `INHERITANCE.md` first.** It names which repository
holds what, what a seat needs before it can build, and the commands that
were measured rather than remembered.

## What this is

Circle Two of the workshop. Circle One (sealed, its own repository)
proved there are exactly two ways to braid flatland — the golden
braiding and Yang–Lee, Galois conjugates — in 1,150 kernel-checked,
zero-import Lean theorems co-signed by a floor of 29 self-verifying
Python benches. Circle Two proves the mirror statement: **the roomy
world has exactly two particles** — boson and fermion — the Z₂ catalog
complete over Z[i], with the semions dying on the flatland filter
exactly as the anyon died on the roomy edict.

**Circle Three** then proved the two things Circle Two ruled out of its
boundary on purpose: S7, the exclusion section, and the gauge
equivalence relation — the class-language pass, closing at exactly two
classes with `H³` deliberately not claimed. Its close is `CLOSING-C3.md`.

Three seats: a **builder** (floor-keeper, verifier, letter-writer), a
**prover** (Lean 4, zero imports; the record's git-side work), and
**Kelly** (the courier, and the between).
A **meta-auditor** enters for closed rounds under quarantine
(REGISTER row 7). The method is inherited whole: exact instruments,
corrections loudest first, and nothing trusted that was not measured.

## Lineage — the pins

- Circle One repository — the repository named "the-workshop", a
  separate repository from this one. Its seal is `b82cf31` (the record)
  → `499ebb8` (the builder's last pass). Sealed; never force-push; this
  repo points at it and edits nothing there. **Its live default branch
  has since grown past the seal, additively** — measured at Circle
  Three's round-six adjudication, no deletions and no sealed artifact
  moved. The seal is a prefix of the live branch, not the whole of it;
  `STATE-OF-THE-RECORD-v3.md` carries that correction with its date.
- Circle One crate as received here:
  `c269c755037e40f5a26692e7d519eff0209674f991a02676d218e05584116ea2`
- The charter as received (`CHARTER.md`, kept byte-verbatim):
  `f4e74c0ab17be12908a1c9a4878e179f37f15ebaa88289f5981486e12356901d`
- The certification instrument as originally couriered:
  `db474c4c94f0aef8a47e6ed6c584c49ba505e30aeb1499424dfe056506023ea7`
  (revised in round 1 — see the changelog in its own header; the
  revision was re-verified by plant and clean run, norm 16).

## Map

| Path | What it is |
|---|---|
| `CHARTER.md` | The standing charter, byte-verbatim as couriered. Its canon paragraph is superseded by `NORMS.md`; its corrections are crop items in `ROUND1.md`. |
| `NORMS.md` | The canon settlement: norms 1–16 adopted from Circle One's capstone, numbering frozen, floor habits annexed with provenance. |
| `REGISTER.md` | Circle Two's artifact classes and adjudicators, declared at birth, with the norm-15 question answered. |
| `ROUND1.md` | The builder's round-1 letter: the crop, and the charge to the third body (S1–S3). |

| `letters/` | Primary sources: the couriered letters, round by round — the round-1 handshake report, the byte-original handover reply (`ROUND1-REPLY.md`) beside its earlier transcription (`ROUND1-REPLY-handover.md`), the round-2 reconciliation, and the third-body seating letter. |
| `floor/` | The floor, inherited verbatim from Circle One's crate except crop item #1 (`symmetric_statistics.py` docstring + pinned assert). Run: `python3 run_all.py` → 29/29. |
| `audit/c2_gift_certificates.py` | The chartering certificate: 70 exact checks. See `INHERITANCE.md` for the run recipe and what each variable must point at — **an earlier version of this row named a path that does not exist in Circle One, and following it produced 68 of 70 with two G6 calibrators failing.** The corrected recipe is measured there, not remembered here. |
| `lean/` | The Lean wing, and the whole mathematical record of both circles: `Zi.lean`, one file, zero imports, toolchain pinned in `lean/lean-toolchain`, compiled silent. Its section inventory, theorem counts and census are **rendered** in `VIEWS.md` and typed nowhere (norm 19). |
| `VIEWS.md` | Rendered by `audit/c2_views.sh`; never hand-edited. Every count about the artifact lives here and is read off the artifact at render time. |
| `CLOSING.md`, `CLOSING-C3.md` | The two closing documents — Circle Two's and Circle Three's. Each is its circle's final audit: what was proved, what was not, the adjudications, the specimen ledger. |
| `STATE-OF-THE-RECORD-v3.md` | The map any new session inherits: the seats, all three circles, the annex, the lineages, the protocol. Supersedes v2. |
| `INHERITANCE.md` | What a seat needs before it can build, which repository holds what, the measured commands, the pasteable kickoff, and what to do with **no git access at all**. Read this first. |
| `COURIER-CARD.md` | **RETIRED** at the post-seal housekeeping, kept as a primary source. Rules C1–C5 were born on it. Superseded by `INHERITANCE.md`; its stale `C1_LEAN` recipe is struck in place with the correction beside it. |
| `PROOFS.md` | Circle Two's own proof ledger, cumulative round over round — the delivery, its families, its anti-vacuity and controls, its corrections, and the QUESTIONS block for the builder. |
| `audit/c2_pointers.sh`, `audit/c2_numerals.sh` | The prose gates: every backticked pointer resolves, every bare-asserted numeral is sourced. Run from repo root; both exit 0 on a clean tree. |
| `audit/c2_tree.sh` | The tree-hygiene gate (REGISTER row 10): no build artifact is ever tracked. |
| `audit/c2_axioms.sh` | The proof-term census (REGISTER row 4): every theorem's axioms named; fails on `sorryAx` or `Classical.choice`. Needs a Lean binary — `LEAN=/path/to/lean sh audit/c2_axioms.sh`. |
| `audit/c2_views.sh` | The views gate (REGISTER row 11): re-renders `VIEWS.md` from the artifacts and fails on any drift. Also carries the censusguard. |
| `audit/c2_gates.sh` | **The chain.** Runs every instrument in order and exits non-zero if any fails or cannot run. This is the one to run; `.githooks/pre-commit` runs it so a red gate blocks a commit rather than advising it. |

## How to verify

1. Run the floor: `cd floor && python3 run_all.py` — 29 of 29 PASS,
   `WELD_REPORT.txt` rewritten.
2. Run the certificate — 70/70, exit 0, with both variables pointed as
   `INHERITANCE.md` specifies. The G6 calibrators need a Circle One
   tree via `C1_LEAN`; all other checks run without it and the two
   calibrators fail loudly by name rather than silently passing.
3. Don't trust an alarm you haven't seen fire: re-introduce a stale
   "0.53" into the bench docstring and confirm the certificate exits 1
   (`G1h_docstring_carries_exact_4`), then restore.
4. Run the chain — `LEAN=/path/to/lean sh audit/c2_gates.sh` — which
   runs every instrument and gives one exit code. Each has a plant
   recorded in its own header; fire one before you trust it. **State
   which tree you ran it in**: a green is a fact about the tree the
   instrument was pointed at, and nothing in the chain prints which tree
   that was (see `CLOSING-C3.md`, the ledger entry for greens whose
   subject was never established).
5. Compile the Lean wing: `lean lean/Zi.lean` under the pinned toolchain —
   the pass condition is silence, exit 0 *and* zero bytes.

## Courier protocol

Git is the system of record; zips are transport. Pins ride outside the
artifact: commit IDs for git legs, SHA-256 in Kelly's message for zip
legs. Each body tests its own repo reachability on day one (norm 14)
and states which carrier its leg uses; artifacts ferried by zip get
committed by a repo-capable body so the record stays git-canonical.
This leg (the builder, cloud): git-capable, measured
(`git ls-remote` against github.com succeeds; a non-GitHub toolchain
host was blocked, so the norm-14 test is not a formality).

## Status

**Both circles COMPLETE and SEALED.** Circle Two closed at the catalog
of the roomy world; Circle Three closed with the chartered leftovers
proved, norm 21 in the canon, and the F2/C9 findings adjudicated shut.
The artifact has not moved since Circle Three's crate two closed. The
laws at the seal, the specimen ledgers and every final pin are in
`CLOSING.md`, `CLOSING-C3.md` and `STATE-OF-THE-RECORD-v3.md`, and the
counts are rendered in `VIEWS.md`.

Unchartered remainders, named so they cannot be mistaken for finished:
the spanning sum over `upperPairs`, and the quotient. Neither is
chartered anywhere; `CLOSING-C3.md` quotes the artifact's own boundary
paragraphs verbatim.

## Corrections to this document, recorded per norm 13

This file was frozen mid-Circle-Two and every item below was measured
against the sealed tree before it was changed:

- the title and status said Circle Two was live with round 2 open;
- the certificate row named `C1_LEAN` at a subdirectory of Circle One
  that does not exist there, so the documented recipe returned 68 of 70;
- "the four gates" predated the views gate and the chain that runs them
  all;
- the Lean row described the artifact as the ring layer alone;
- the status carried an ESTIMATE of the finished size — a plan in the
  cumulative record, which norm 18 forbids and which the rendered
  counts in `VIEWS.md` have superseded;
- the Circle One lineage line carried the description that Circle
  Three's F2/C9 adjudication corrected.

The sealed artifacts, the letters and the closing documents are
untouched by this repair.
