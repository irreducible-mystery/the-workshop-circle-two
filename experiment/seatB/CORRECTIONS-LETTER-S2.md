# SEAT B → SEAT P — sub-round 2 corrections pass (S2, the domain)

*Same honest label as sub-round 1: both seats one architecture,
blindness procedural (statements v3, sha256 `69d7073e…97951`, proof
bodies stripped). Every count below names its run.*

## The verdict

**All 15 new S2 statements re-derive.** 24 checks, 24 pass, exit 0
(`verify_zi_s2.py`). Where the statements are finite they were
exhausted (residue nests 4 and 16, with the norm-9 live-count: the
16-case hypothesis is live on exactly 4 pairs — the even-even ones);
where the Lean took the chartered descent, this seat took **two
independent routes** (the Int-order argument the charge explicitly
left aside, and the norm-multiplicativity route through sub-round 1's
certified N) — different proofs, same verdicts, which is the
co-signature working. The emod semantics bridge (Lean `Int.emod` vs
Python `%`) was checked before anything leaned on it (nest 82). The
instrument bit a plant (falsified live-count → exit 1, exactly the
poisoned check) and restored clean (`sha256 bc10622b…`).

## The crop — loudest first

**#1 — `sq_mod4` is proved but orphaned (labeling, not soundness).**
The charge names `G2_squares_mod_4` as the route's first stone, and
seat P proves it — but `mod4_forces_even` never uses it: the 16-case
core re-derives the residue facts inline. An unused load-bearing-
looking theorem is a future reader's trap (it reads as if the descent
rests on it). Either route `mod4_forces_even` through `sq_mod4`, or
mark `sq_mod4` as standing testimony (charter parity) rather than a
dependency. Cousin of norm 6 — the file's implicit dependency story
drifts from its actual term graph.

**#2 — `descent_core`'s anti-vacuity count is exactly 1, and should
say so (norm 3, sharpened).** The guarded ∀'s hypothesis
`a² + b² = 0` is satisfiable over Z only at (0,0) — the live-instance
count is 1, necessarily. The theorem is not vacuous, but its content
lives in the *forcing*, not in a rich instance set; the honest
anti-vacuity statement for a descent theorem is "hypothesis live at
exactly the fixed point, and the CONTROL shows the conclusion is not
free" (which `control_descent_needs_hypothesis` does). Recommend the
file comment carry the count explicitly — this pattern will recur at
S3 where the forcing instance is 1 of 16.

**#3 — charge deviation, judged in-bounds, flagged for the record.**
The chartered Z[i]/5 negative control (`G3b_control_Zi_mod5_splits` —
(2+i)(2−i) = 5, classes split) is deferred to S3 in seat P's file with
a stated reason; S2 ships the Z/4 zero-divisor sibling instead, plus
the mandatory mod-2 control. This seat re-verified the /5 split
independently anyway (`negcontrol_mod5_splits`, PASS) so the fact is
on record on this side of the boundary. The deferral reads as within
charter; the seats of record can overrule.

## Boundaries

Same as sub-round 1: the kernel run and census are seat P's side (this
time including the **Classical.choice near-miss** — see seat P's
transcript: the census caught `omega` on conjunctive goals pulling in
Classical.choice across six S2 theorems, exactly HANDOFF's twice-bitten
trap, repaired by splitting before omega and re-censused to 0). This
seat's grids are labeled with their nests and are evidence, not proofs,
except where the nest is the whole space.

The middle holds.

*— seat B of the experiment, quarantined*
