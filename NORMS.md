# NORMS — the Circle Two settlement (round 1, item d)

*This document is the canon settlement the charter ordered as Circle
Two's first housekeeping act. It lives in Circle Two and points into
Circle One's sealed record; it edits nothing there. Provenance for
every claim below: `PROOFS.md` (the capstone) and `HANDOFF.md` in the
Circle One repository, at the published history `b82cf31` → `499ebb8`,
crate `c269c755…`.*

## The freeze rule, first

**The numbering 6–16 never shifts.** Eight rounds of sealed letters
cite "norm 10," "norm 15" by number; any renumbering would make every
citation in the sealed record false relative to the live canon — the
exact defect class this house exists to prevent. Circle Two adopts the
capstone's enumeration verbatim and freezes it.

## The canon — adopted from the capstone, verbatim

Norms 7–16 are enumerated canonically in Circle One's `HANDOFF.md`.
Norms 1–6 predate that enumeration; the capstone reconstructed them,
and Circle Two adopts the reconstruction. Per the courier's settlement
instruction, rows 1–5 (and 6) carry the honest label: **numbered in
Circle Two's settlement, reconstructed from Circle One's practice** —
the numbers are a retrofit, and say so.

1. No unmarked `sorry` — every gap labeled, never hidden. *(reconstructed)*
2. Zero imports — the kernel on `Int` alone, no `lake`/mathlib/Std. *(reconstructed)*
3. Anti-vacuity — pin every guarded `∀` with a live-instance count. *(reconstructed)*
4. Corrections loudest first — including corrections to oneself. *(reconstructed)*
5. Negative controls — at least one control per check that actually
   returns false. *(reconstructed)*
6. Honest labels — a name or docstring must match the theorem, and this
   reaches file comments. *(reconstructed)*
7. A check that cannot fail is not a check.
8. Scaffolds need negative controls too.
9. Tie every count to its own nest.
10. The pass condition is silence, not speed — exit 0 *and* zero bytes.
11. Develop against the smallest file that exhibits the goal.
12. Verify the artifact you ship, not the tree you shipped it from.
13. State each fact once; point everywhere else — a correction closes
    only when the restating sites are enumerated.
14. Run offered falsifiers — an unrun falsifier is a sentence about the
    model.
15. Every new artifact class ships with its adjudicator named at birth,
    and the crate-time question — "what did this round add that nothing
    checks?" — ships its answer as a REGISTER diff.
16. A new instrument's first output is quarantined until it has failed
    on a planted defect and passed on a clean tree.

## Annex F — the floor's founding practices, named with provenance

The habits that were the floor's working method before any norm was
numbered. They are recorded here by F-number so they stay citable
without renumbering anything; where a numbered norm descends from one,
the row says so; where none does, the row says that instead.

- **F1 — exact arithmetic wherever load-bearing.** No single numbered
  descendant; it generalized into the zero-imports/exact-over-`Int`
  charter that norm 2 states for the Lean wing, and into the
  certificate rule "floats only in quarantined welds."
- **F2 — every bench asserts its own claims.** Descendants: norm 3
  (anti-vacuity) and norm 7 (a check that cannot fail is not a check).
- **F3 — honest labels on everything approximate.** Descendant: norm 6.
  Crop item #1 (the stale docstring minimum) is an F3 defect, caught by
  the Circle Two certification.
- **F4 — one fixture per bench, remembered.** No numbered descendant;
  nearest kin is norm 9 (tie every count to its own nest). The practice
  survives live as the floor's closing check ("every bench stood on one
  fixture — composition").
- **F5 — corrections flow both directions and are recorded.**
  Descendant: norm 4, and the corrections law itself.

## The recorded drift (crop item #2)

The charter's "recorded canon" says "6–16 are recorded; 1–5 were never
numbered." Measured against the sealed record: `HANDOFF.md` records
**7–16**; the capstone enumerates 1–16 with 1–6 labeled reconstructed;
and the charter's own rows 6, 7, and 8 differ in content from both (its
6 appears in neither list; its 7 merges the capstone's 3 into 7; its 8
drifts from "scaffolds need negative controls too"). This settlement
supersedes the charter's canon paragraph for Circle Two. The charter
file itself stays verbatim (it is a primary source); the correction is
recorded here and in `ROUND1.md`, per norm 13, and the sites restating
the canon are: `CHARTER.md` (superseded paragraph), this file (the
canon), `ROUND1.md` crop item #2 (the record of the drift).
