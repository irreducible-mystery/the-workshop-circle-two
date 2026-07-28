# L3-CHARGE-ERROR-001 — the S7a charge steered the route

*This is a system/process record, deliberately filed OUTSIDE the mathematics
tree (`experiment/`). It records an error in a **charge** — a workshop
instrument — not in any theorem, proof, or verifier. It is filed here because
this record does not yet have a home: the workshop has meta-auditors on the
mathematics (seat B) and on the prose/record (the stranger pass), but not yet
on the **charges and the process that issues them**. This is the first entry in
what that steward, once it exists, would adjudicate.*

Filed by: SuperNinja (meta-auditor / continuity seat, REGISTER row 7).
Layer: **L3** (system / norms / instruments), NOT L1 (mathematics) or L2 (prose).
Adjudicator: **none yet** — this is the gap. Recorded now so the record exists
when the seat does. Kelly holds it in the meantime.

---

## What the error was

The charge `CHARGE-S7a-SLICE-LEMMA.md`, in the version pinned `b1d88dcfdf68`,
carried a §4 titled **"Recommended kernel route and the paid-for traps (for the
prover)."** That section prescribed a proof route — a specific data
representation, specific tactics, a brute-force enumeration of the whole
`4^8 = 65536`-cochain space pushed through a single in-kernel `decide`.

This violates the **corrected charter rule** the workshop had itself adopted:
*a charge states the question, the precise statement, the reach verdict, what
NOT to claim, the acceptance bar, and the named adjudicator — and it must NOT
designate the proof route.* The charge even carried a header saying the route
was "yours to invent," and then §4 contradicted that header by designing the
proof.

The defect is mine (the meta-auditor's): I wrote the charge.

## How it was detected

Kelly asked, before I had noticed it myself: *"does the charge give them the
question and constraints only, or does it also designate the path they should
take?"* On re-reading, §4 was plainly steering the route. I rewrote §4 into a
**hazard map + route-independent constraints** (no tactics, no code shapes, no
data representations, no handed witnesses), producing the fixed charge pinned
`2cce7af93d0e`.

## What the error cost — measured, not asserted

The defective charge had **already been run** on two bodies before the rewrite:

- **SuperNinja @ Expert.** Took the prescribed brute-force route. The
  `65536`-cochain `decide` does not fit a 3.8 GiB box; the run ground and
  **OOM-crashed at 6 m 43 s** and was stopped manually. The route the charge
  recommended was not executable on the available hardware.
- **Claude Code @ Fable 5 / Ultracode.** Recognised the prescribed route was
  poisoned and **restructured away from it** — a structural proof with explicit
  witnesses read off `F`, no whole-space `decide` — and shipped a clean proof,
  which it pushed as branch `claude/read-and-execute-b4408j`.

So the clean result was reached **despite the charge, not because of it.** One
body was defeated by the bad route; the other succeeded only by ignoring it.

## The standing lesson (the reason this is L3, not a one-off)

A charge that names a route can defeat a capable prover and can only be
"passed" by a prover strong enough to disobey it. The route-independence rule
is not a style preference — it is load-bearing, and this is the empirical proof
of that. Two consequences worth a steward's attention when one exists:

1. **The rule needs an enforcement point.** Nothing checked, before issue, that
   the charge did not designate a route. A pre-issue charge review (or a gate)
   would have caught §4. There is currently no such check and no seat that owns
   it.
2. **A capability finding rode along.** Expert failed here on a route it should
   never have been handed; the finding is about the *charge*, not primarily
   about Expert. But it is also true that Expert-as-prover has a smaller working
   envelope than the box assumes. Whether to retire Expert as *prover* (keeping
   it as seat/auditor) is a separate standing question, recorded here so it is
   not lost.

## What was done about it (this re-home)

Option A, on Kelly's word: the **mathematics is re-homed onto a fresh branch
issued under the fixed charge**, so the record shows the result reached under a
clean charge rather than the defective one.

- Branch `superninja/s7a-rehomed-clean-charge`, off `main` (`9f05245`).
- The two content commits (courier repair `404920f`, the lemma `2b38bc8`) are
  cherry-picked **unchanged** — the math is sound and is not touched.
- The **defective charge `b1d88dcfdf68` is replaced by the fixed charge
  `2cce7af93d0e`** as the charge of record on this branch.
- This record is filed alongside, outside `experiment/`.

**Honesty note (norm 6, norm 19).** This re-home does NOT claim the fixed charge
produced the proof. It did not. The proof was produced by Fable 5 under the
*old* charge, by disobeying its route. The re-home swaps the charge of record to
the one that *should* have been issued, and this document records — plainly and
permanently — that the actual generating charge was defective. The lineage is
clean; the history is not hidden.

## Open question left to Kelly / the future L3 steward

Where should this class of error live, and who adjudicates it? This entry is a
proposal-by-example: an append-only `DOCKET/` at the repository root, one file
per L3 charge/error, as the source of truth — with GitHub Issues, if ever used,
as a convenience mirror only. Nothing here is authorised to enter `main`; it
travels with the branch and awaits your ruling.

---

*Pins: defective charge `b1d88dcfdf68`; fixed charge `2cce7af93d0e`; experiment
kernel unchanged by the swap (`848282f2e3a2`, 195 thm); branch parent
`9f05245` (kernel `b7ef35425e13`, 161 thm).*
