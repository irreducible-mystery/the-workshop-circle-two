# Capability report — can this architecture host the Fable↔Ultracode loop?

*SuperNinja, meta-auditor seat, second session. Quarantine still applies
to my prose (norm 16); everything marked MEASURED was produced by an
instrument in this container this session. This note is the experiment's
first deliverable: the capability audit, before any orchestration.*

---

## The ferried artifacts (pins measured here — none rode in the message)

- `theworkshoprepo.zip` — sha256
  `c269c755037e40f5a26692e7d519eff0209674f991a02676d218e05584116ea2`
  — **this matches the Circle One crate pin in Circle Two's README**
  ("Circle One crate as received here: c269c755…"). MEASURED, and the
  strongest possible identity check: the crate is the record.
  Contents: `lean/` = the sealed Circle One repository, a real git
  repo at the published two-commit history `b82cf31 → 499ebb8`
  (MEASURED via git log). Six .lean files, floor/, audit/ (~90
  instruments), all round letters, capstone.
- `workshop_(16).zip` — sha256 `3d5ab812…a09a08a` (not `3a09a09a`;
  full: `3d5ab8122b20c77877b702fa7b043e3f2d93589391d9f4350631e60a3ca9a09a`).
  No pin anywhere on record that I can match this against. Contents:
  a mid-arc snapshot — floor + `lean/` with only four proof files and
  round letters up to ROUND5.md; PROOFS/HANDOFF/Anyon/MagicSquare all
  differ from the sealed record. Reading: a historical working crate
  (~round 5 era), useful as context for the flow, NOT a record. Treated
  as such.

## Environment measurements (MEASURED)

| capability | result |
|---|---|
| sandbox | Linux x86_64, 2 cores, 3.8 GiB RAM, ~3.3 GiB disk free |
| Python floor | 29/29 PASS after `pip install numpy scipy` (both circles' floors) |
| elan + Lean | **installed clean: `leanprover/lean4:v4.32.0`** — the pinned toolchain, exact |
| Interchange.lean | exit 0, zero bytes, 0.6s |
| MagicSquare.lean | exit 0, zero bytes, 45s |
| Anyon.lean (6,817 lines) | **exit 0, zero bytes, 75s** |
| Exchangeable.lean | exit 0, zero bytes, 12s |
| Verlinde.lean | exit 0, zero bytes, 3s |
| Rigidity.lean | exit 0, zero bytes, 98s |
| source hashes | all six + lean-toolchain match VERIFY.md's stamped prefixes exactly |
| C2 certificate w/ C1_LEAN | **70/70, exit 0** — first full co-signature run outside Kelly's machine and the builder's container (the G6 calibrators read the Circle One tree ferried today) |
| shell gates | pointer + numeral gates run and PASS (measured last session) |
| git/GitHub | `gh` CLI authenticated; can commit, push branches, PR |
| parallel seats | no true parallel agent seats; sequential sessions + subprocess parallelism only |

**Headline: the entire Circle One record recompiles silent on this
architecture, kernel-checked, on the exact pinned toolchain — and the
Circle Two certificate closes 70/70 here.** Both bodies' instruments
run natively in one container.

## What the two seats actually did (read from the record)

- **Fable 5 (builder):** floor-keeper; exact Python reimplementation
  of every Lean claim from the statements alone; adversarial
  multi-seat prose audits (22 agent seats in round 2 of Circle Two);
  gates; letters/charges; corrections loudest first.
- **Ultracode (third body):** Lean 4 proving, zero imports, v4.32.0;
  compile transcripts + .olean hashes; axioms.sh census; plants;
  its own crop against the builder's letters.
- **Kelly:** the between — pins in the message, both directions.

## The honest structural question — and it is the only real one

Tooling is a clean YES: this architecture can run the floor, the
certificate, the gates, the kernel, and the git legs, all in one
place. The open question is **epistemic, not technical**: the
workshop's definition of "verified" is two-body — kernel + exact
reimplementation, built by strangers who cannot see each other's
reasoning, with the courier as the air gap. If one architecture plays
both seats, the sentences come from one model reading its own work.
The corrections law says exactly where that fails: prose written from
the author's model of an artifact, adjudicated only by the author.

Mitigations available in this architecture, honestly priced:

1. **The instruments stay the authority.** Kernel exit codes, bench
   asserts, certificate checks, gates — none of these care who runs
   them. The mathematics' adjudicators survive the merge of seats
   intact. What weakens is the *prose* classes (REGISTER rows 6, 8).
2. **Hard role separation by session + workspace:** builder-seat
   sessions and prover-seat sessions run as separate shell sessions
   with separate working trees; each seat's letters are written before
   the other seat's tree is opened; artifacts cross only as committed
   files with pins. This is discipline, not architecture — it should
   be labeled as such in the record.
3. **Blind reimplementation stays blind-ish:** the builder seat
   reimplements from theorem *statements* extracted mechanically
   (grep the statement lines), never from proof bodies. Verifiable
   by procedure, not by architecture.
4. **Kelly's seat gets stronger, not weaker:** with one model in both
   chairs, the courier is the only true stranger left. Spot-checks,
   choosing plants, and holding the pins matter more here, not less.
5. **Honest labels:** anything this experiment produces should carry
   a new register class — "single-architecture dual-seat, instruments
   two-body, prose one-body" — named at birth per norm 15, quarantined
   per norm 16, and never silently blended into the two-body record.

## Proposed experiment shape (for Kelly to approve/amend)

Target: Circle Two round 2's actual open charge — S1 (the Z[i] ring
layer) as the test article, smallest first (norm 11).

1. **Seat P (prover):** write `Zi.lean` per ROUND1.md's S1 spec —
   zero imports, v4.32.0, ring laws + conj + norm + Brahmagupta–
   Fibonacci, anti-vacuity counts, negative controls, no unmarked
   sorry. Compile silent; transcript + hashes recorded.
2. **Seat B (builder):** in a separate session/tree, mechanically
   extract the theorem *statements* only; reimplement each in exact
   Python; run; compare verdicts. Write the corrections letter
   loudest-first.
3. **Axioms census:** re-instantiate `axioms.sh` for the new tree
   (REGISTER row 4's declared frontier) — plant a defect, watch it
   bite, then run clean.
4. **Everything lands on a fresh branch** (never main), letters +
   transcripts + pins committed, PR opened for Kelly — the record
   stays git-canonical and the human stays the merge authority.
5. **Score it:** did the dual-seat discipline hold? Where did prose
   defects land? That is itself the experiment's finding, in the
   house style.

Fallbacks if any step exceeds this container: report the wall honestly
(the crash-autopsy precedent — a wall tested and found real is a
result, not a failure).

The middle holds.

*— SuperNinja, quarantined, capability audit complete*
