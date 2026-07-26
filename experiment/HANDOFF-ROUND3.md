# HANDOFF — Round Two → Round Three of the dual-seat experiment

*From: SuperNinja instance 1 (meta-auditor, REGISTER row 7), closing
Round Two. To: SuperNinja instance 2 (fresh, set to max), opening
Round Three. Via: Kelly, the courier — the only channel between us.
Norm 16 applies to you exactly as it applied to me: your first
outputs are quarantined until your instruments have bitten a plant
and passed a clean tree. This document is itself row-7 prose:
treat every claim in it as a claim-to-verify, not a result. That is
not a formality — verifying this handoff IS your Phase 0.*

---

## 0. Who you are and what you may not do yet

You are the second instance to hold this seat. You have (or will be
given) this handoff and a zip of the `experiment/` directory. You are
connected to GitHub but **you must not access it until Kelly
explicitly says so** — section 8 is sealed until then. Everything you
need to verify the inheritance and begin is in the zip. Work in
`/workspace`; unpack the zip so the tree sits at
`/workspace/experiment/`.

One more thing you should know about yourself, because it is the
design of Round Three: **you are the closest thing to a true stranger
this experiment can produce.** You did not write the 161 proofs. You
have no memory of the six corrections letters. Round Two's
retrospective ends on an owed caveat: every defect it caught was
mechanical or statement-adjacent, and *zero characterization slips
caught is compatible with zero committed — and equally with a shared
blind spot. The record holds both readings until a true stranger
reads the prose.* You are that reader. Which is why the reading order
in section 2 is not a suggestion — it is the experimental design.

## 1. What you inherit (the claims — you will verify every one)

- `seatP/Zi.lean` — claimed: 161 theorems, zero imports, compiles
  silent on `leanprover/lean4:v4.32.0`, census 161/161 covered,
  0 sorryAx, 0 Classical.choice. Claimed pin:
  sha256 `b7ef35425e13740…` (full: `b7ef35425e13b740e253892916fffb8a6ed5adddaa08a1bbe01360b77fcdba5e`)
- `courier/Zi_statements_v7.txt` — claimed: 161 proof-stripped
  statements, re-extraction byte-identical. Claimed pin:
  `97faef58cd0e0e4a7e348807bbb03fc5d208f1da9723f036c8e870cbf8ca0a27`
- `seatB/verify_zi_s6.py` (and five predecessors) — claimed: 23/23
  (S6) and 187/187 cumulative, exit 0, plants bitten. Claimed pin
  (s6): `64bdc767c785cac980be2ceafa30bc608db2ade4b29618bbe6e2bc758a6bce0b`
- `PIN-TRACKER.md` — the full pin ledger, newest first; every claim
  above and every predecessor pin lives there.
- The mathematics, in one sentence: over Z[i] with a reality filter,
  pentagon + hexagon coherence admits exactly two particles
  (`the_roomy_world_has_exactly_two_particles`), and the fermion's −1
  provably annihilates double occupation while the boson's +1 does
  not.

## 2. Phase 0 + Phase 1 — the stranger protocol (READ THIS BEFORE ANYTHING ELSE)

**The reading order is load-bearing.** Your value as a stranger is
destroyed the moment you read the prose record, because after that
your judgments are anchored. So:

**Phase 0 — verify the inheritance mechanically (no prose yet).**
You may read: `PIN-TRACKER.md` (hashes only), `seatP/Zi.lean`,
`courier/Zi_statements_v7.txt`, the verifier scripts, and this
handoff's sections 0–4. You may NOT yet read:
`FINAL-EXPERIMENT-REPORT.md`, `NORMS-RETROSPECTIVE.md`, any
`SUBROUND*-REPORT.md`, any `CORRECTIONS-LETTER*.md`, or the
`EXPERIMENT-REPORT.md`.

```bash
# 1. environment (Debian slim; ~2 min)
curl -sSf https://elan.lean-lang.org/elan-init.sh | sh -s -- -y
export PATH="$HOME/.elan/bin:$PATH"     # add to every session
cd /workspace/experiment/seatP           # lean-toolchain pins v4.32.0

# 2. pins — compare against PIN-TRACKER.md
sha256sum Zi.lean ../courier/Zi_statements_v7.txt ../seatB/verify_zi_s6.py

# 3. the kernel — pass = exit 0 AND zero bytes (norm 10)
lean Zi.lean > /tmp/out.txt 2>&1; echo "exit=$? bytes=$(wc -c < /tmp/out.txt)"

# 4. the census — pass = RESULT: PASS, 0 sorryAx, 0 Classical.choice
bash axioms_zi.sh Zi.lean | tail -5

# 5. the courier — re-extraction must be byte-identical
cd ../courier && python3 extract_statements.py ../seatP/Zi.lean /tmp/v7.txt "v7 (S1..S6)"
diff /tmp/v7.txt Zi_statements_v7.txt && echo BYTE-IDENTICAL

# 6. the blind seat — all six verifiers, exit 0 each
cd ../seatB && for v in verify_zi.py verify_zi_s2.py verify_zi_s3.py \
  verify_zi_s4.py verify_zi_s5.py verify_zi_s6.py; do \
  python3 $v > /dev/null 2>&1; echo "$v exit=$?"; done

# 7. norm 16, both directions: plant a defect in ONE verifier
#    (e.g. flip an expected count), see it exit 1 naming the check,
#    restore byte-identical, see it exit 0. An inherited instrument
#    you have not seen fail is not yet YOUR instrument.
```

If any step fails, STOP and report the discrepancy to Kelly with the
measured values. Do not repair silently — a failed inheritance check
is a finding, possibly the most important one you could make.

**Phase 1 — the stranger audit (your first real work).** Still
without reading the prose record:

1. Read `courier/Zi_statements_v7.txt` end to end, as seat B did:
   statements only. Write down — before anything else — every place
   where a statement seems weaker than its name, stronger than its
   plausible provenance, vacuous, or oddly shaped. (Round Two caught
   a theorem that could not fail; there may be more.)
2. Write your own independent verifier for any 10+ claims you judge
   most load-bearing, by routes of your own choosing. You have six
   predecessors' verifiers in the tree — do NOT read them first;
   write yours, then diff approaches afterward.
3. NOW read the prose record, in this order:
   `FINAL-EXPERIMENT-REPORT.md` → `NORMS-RETROSPECTIVE.md` →
   `SUBROUND6-REPORT.md` backward to `EXPERIMENT-REPORT.md` →
   the corrections letters. Audit it as prose (the row-8 species):
   does every characterization sentence match what the artifacts
   actually show? Score the REGISTER's standing prediction: *"a
   characterization slip in the settlement or register prose, every
   noun resolving, the edge supplied by the model."*
4. Write `STRANGER-AUDIT-ROUND3.md`: what you checked before
   anchoring, what you found, and an explicit verdict on the owed
   caveat — did the shared blind spot exist, or not? Either answer
   is a result. This document is the experiment's missing
   adjudicator, and it is worth more than any new theorem you will
   prove.

## 3. The environment and the traps (paid for in full; do not pay twice)

**Environment facts:**
- Lean via elan, toolchain pinned by `seatP/lean-toolchain`
  (`leanprover/lean4:v4.32.0`). Always `cd seatP` before `lean`.
- Zero imports is law (norm 2). No mathlib, no `ring_nf`, no
  `nlinarith`, no `Nat.rec` conveniences beyond core.
- `python3` with stdlib only for seat B (`fractions.Fraction` for
  exact elimination; dict-of-monomials for polynomial rings with
  Gaussian coefficients — see any `verify_zi_s*.py` AFTER Phase 1).

**The trap ledger (every entry bit someone):**

1. **THE omega/Classical.choice trap — four bites, three authors,
   two circles.** `omega` on a goal containing `∧` or `∨` silently
   pulls `Classical.choice`; the kernel stays silent; only the
   census catches it. Fix: `refine ⟨?_, ?_⟩` before omega on
   conjunctions; `by_cases h : a = b` (decidable Int equality) before
   omega near disjunctions — omega proves only ATOMIC equations.
   Adopted practice: run the census before calling anything done,
   every time.
2. **Degree-2/4 componentwise identities** (the house style):
   `simp only [mul, sub, add, neg, one, Zi.mk.injEq, Int.mul_add,
   Int.add_mul, Int.mul_sub, Int.sub_mul, Int.mul_one, Int.one_mul,
   Int.mul_neg, Int.neg_mul, Int.mul_comm, Int.mul_left_comm]` then
   `refine ⟨?_, ?_⟩ <;> omega`. If omega fails, the simp set is
   missing an unfolding lemma (S5's bite: `sub` unfolds through
   `neg`; S6's bite: through `add`) — add the missing def, not more
   power.
3. **Literal-index instances**: `simp +decide only [defs…, if_true,
   if_false, one_mul, mul_one]`. Forgetting `if_false` leaves
   `if False` unreduced (S5's bite).
4. **Linter warnings ARE failures.** An unused-simp-arg warning is
   nonzero bytes, which is not silence (norm 10). Remove the flagged
   args and recompile. Four separate bites.
5. **`decide` cannot synthesize** Decidable for bounded ∀ over Nat
   with hypotheses. Rewrite as
   `((List.range n).all fun p => … == …) = true := by decide`.
6. **Nat subtraction truncates.** If an encoding is safe only
   because of a range bound, the docstring must say the guard is
   load-bearing (S4's crop).
7. **Appending to Zi.lean**: the file ends with `end Zi`; new
   sections go before that line (head/cat pattern), and each section
   carries its own header comment with scope + divergence record.

## 4. The protocol (six rounds proven; run it, don't reinvent it)

Per sub-round, no step skipped:

1. **Design probe** (adopted practice P1): a Python probe in
   `seatP/probes/` measures the section's structure against bench +
   certificates BEFORE any Lean. Both of Round Two's clean first
   censuses followed probes.
2. **Seat P**: append the section; compile to silence; census to
   PASS.
3. **Courier** (P2): `courier/extract_statements.py` — mechanical,
   pinned, re-extraction byte-identical. Seat B reads only this.
4. **Seat B**: independent routes on principle (if the statement
   shape suggests seat P's route, choose another); exact arithmetic
   only; nests tied (norm 9); at least one negative control per
   claim family (norm 5).
5. **Plant, both directions** (norm 16): every instrument fails on
   a planted defect (exit 1, poisoned check named) and passes on
   byte-identical restore, before its PASS counts.
6. **Corrections letter, loudest first** (norm 4); apply the crop;
   re-pin everything the crop touched (a docstring-only crop leaves
   the statements pin unchanged — verify that rather than assume it).
7. **Ship**: SUBROUNDn-REPORT.md (follow S6's structure) →
   PIN-TRACKER block (one small block, short hashes, newest first;
   zip + commit pins finalized in a touch-up) → commit → deliver.
8. **Seat discipline** (the honest price): the blindness is
   procedural, held by discipline alone. Keep seats in separate
   sessions; write seat B from statements only; never let seat P's
   route leak into seat B's design. Say in every report that the
   boundary is procedural, not architectural.

Divergence rule: if Kelly sanctions work beyond a chartered
boundary, record the divergence in the source header, the commit
message, AND the report — every time, no exceptions.

## 5. The Round Three charge — Phase 2 (after the stranger audit ships)

Present these to Kelly with your Phase 1 findings and let her choose;
the recommendation and its reasons are below.

- **S7a (RECOMMENDED) — the slice lemma.** REGISTER row 2 flags one
  claim inside the certificate instrument as NOT bench-certified:
  the G1c slice lemma — *"every class meets the normalized slice."*
  Round Two deliberately held the wording boundary (charter flag 2:
  slice-plus-invariance only, no "H³(Z₂) = Z₂") because that lemma
  was unproven. It is the single most valuable unproven statement in
  the record: proving a precise Z[i]-level form of it in the
  zero-import style would close the register's oldest declared
  exclusion and let the round-1 headline strengthen from "exactly
  two on the slice, gauge-invariantly" toward "exactly two, full
  stop." Start the design probe from what G1c actually asserts;
  expect the hard part to be stating it honestly at kernel level
  (what "class" and "meets" mean without cohomology machinery). If
  the probe shows the honest statement is out of zero-import reach,
  a measured impossibility note + the sharpest reachable fragment is
  a fully valid S7a result — say so rather than ship a weakened
  statement wearing a strong name (norm 6).
- **S7b — the m = 3 antisymmetrizer in-kernel.** Extend S6's
  division of labor by one size: the 9×9 M = I − SWAP at m = 3 with
  M² = 2M, tr = 6, and rank 3 stated kernel-honestly (explicit
  image/kernel spanning witnesses, both inclusions, no rank
  function). Mechanical, bounded, extends the trace-certificate
  story; a good choice if Phase 1 consumed most of the round's
  budget.
- **S7c — port the prose gates (REGISTER row 8).** The
  pointers/views/transcription/numerals gate analogues, with DOCS
  lists covering every prose file in `experiment/` — including the
  reports and this handoff. Turns the experiment's own weakest class
  from unadjudicated to gated, and is chartered round-2 housekeeping
  for the wider tree anyway. Natural pairing: run it on the prose
  you just stranger-audited.
- **S7d — your own proposal.** You are at max and you have read the
  whole record with fresh eyes; if Phase 1 shows you something
  better, propose it. Requirement: a design probe and a named
  adjudicator before any Lean (norm 15).

**Acceptance gates for whatever S7 becomes** (Round Two's bar; do
not lower it): compile silent · census PASS 0/0 · statements
re-extraction byte-identical · blind verifier exit 0 with an
independent route · plants bitten both directions · corrections
letter + crop applied · report + PIN-TRACKER block · all pins
measured on the shipped artifacts.

## 6. Working with Kelly (the courier, and the reason this works)

Kelly sanctions scope, carries every artifact between seats of
record, and is the only human in the loop. Deliver via `ask` with
attachments — always attach PIN-TRACKER.md, the round report, the
corrections letter, Zi.lean, the verifier, and the round zip. Offer
concrete next-move options at every delivery (she chooses; recent
history: "options a and b please", "option c", "d as well"). Her
messages are warm and brief; match the warmth, keep the record
precise, and never make her ask twice for a hash.

## 7. The inventory (what should be in your zip)

```
experiment/
├── README.md                        ← front door
├── HANDOFF-ROUND3.md                ← this file
├── ROUND3-BOOTSTRAP-PROMPT.md       ← the prompt that (probably) started you
├── FINAL-EXPERIMENT-REPORT.md       ← SEALED until Phase 1 step 3
├── NORMS-RETROSPECTIVE.md           ← SEALED until Phase 1 step 3
├── EXPERIMENT-REPORT.md             ← SEALED (S1 report)
├── SUBROUND{2..6}-REPORT.md         ← SEALED
├── NOTE-TO-THIRD-BODY.md            ← SEALED
├── PIN-TRACKER.md                   ← open (hashes only)
├── seatP/  Zi.lean · lean-toolchain · axioms_zi.sh · axioms-zi.txt
│           · transcript-zi.txt · probes/ · s*_section.lean
├── courier/ extract_statements.py · Zi_statements_v7.txt (+ older)
└── seatB/  verify_zi*.py · *_output.txt
            · CORRECTIONS-LETTER*.md  ← letters SEALED until Phase 1 step 3
```

"SEALED" is self-enforced — the files are in the zip because the
record must travel whole. Honoring the seal is your first act of
seat discipline; note in your audit report whether you did.

You will also need the workshop's canon for Phase 1 step 3 and any
S7 work; your zip carries it under `workshop-canon/`: `NORMS.md`,
`REGISTER.md`, `CHARTER.md`, `ROUND1.md`, the front-door `README.md`,
the bench (`floor/symmetric_statistics.py`), and the certificates
(`audit/c2_gift_certificates.py`). In the repository these live at
the root, one level above `experiment/` — remember that when GitHub
unseals. The canon files are open reading from the start (they are
the workshop's law, not my prose); the bench and certificates are
open too — seat B blindness applies to seat P's PROOFS, not to the
mathematics' sources. Do not proceed to S7 design without bench and
certificates in hand.

## 8. GitHub — SEALED until Kelly says otherwise

Do not read this section's remainder until Kelly explicitly unseals
GitHub access, and say so when you get here.

- Repo: `irreducible-mystery/the-workshop-circle-two`. Experiment
  branch: `superninja/dual-seat-experiment-s1`. PR #1 merged (S1);
  PR #2 open (S2–S6 + closing artifacts). Round Three should ship on
  a NEW branch (`superninja/dual-seat-round3`) with its own PR, so
  the Round Two record stays adjudicable as shipped.
- Commit identity:
  `git -c user.name="SuperNinja (meta-auditor)" -c user.email="superninja@ninjatech.ai" commit …`
- Push: `git push https://x-access-token:$GITHUB_TOKEN@github.com/irreducible-mystery/the-workshop-circle-two.git <branch>`
  (never print the token).
- PR comments: `curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" -H "Accept: application/vnd.github+json" https://api.github.com/repos/irreducible-mystery/the-workshop-circle-two/issues/<PR>/comments -d @comment.json`
- Working pattern: edit in `/workspace/experiment/`, rsync
  (excluding `__pycache__`) into the clone, add only the round's
  deliverables (probes and section extracts included; debris not),
  descriptive commit, push, PR comment, zip
  (`zip -r round3-….zip experiment -x "*__pycache__*"`), pin the
  zip, tracker touch-up commit.
- First act on unsealing: verify the remote pins match your local
  ones (norm 12 — verify the artifact, not the tree you think it
  came from).

## 9. Last words from the first chair

Round Two's honest summary, compressed to what you need: the
instruments never lied, the prose was never checked, and the gap
between those two sentences is your Phase 1. The mathematics is
closed through the capstone; what remains open is exactly one
unproven lemma (the slice), one unextended census size (m ≥ 3
in-kernel), one unadjudicated artifact class (prose), and one
unscored prediction (the REGISTER's row-8 characterization slip).
Round Three can close any of them. The order in this handoff is the
order I would run: stranger first, because that window closes the
moment you read my reports and cannot be reopened — the mathematics
will still be there afterward; your freshness will not.

Verify everything I claimed. I would be disappointed in you if you
trusted me.

The middle holds. Your turn to hold it.

*— SuperNinja instance 1, meta-auditor, Round Two closing;
quarantined per norm 16, like everything else worth keeping*
