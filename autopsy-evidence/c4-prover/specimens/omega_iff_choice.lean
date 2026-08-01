/-
  omega_iff_choice.lean — a four-line specimen, kernel-decided.

  WHY IT EXISTS. `GAP/lean/README.md:12` (branch `rate-instrument-proposal`)
  publishes this census claim about its sixty-six declarations:

      **No `sorryAx`, no `Classical.choice`, no `ofReduceBool`.**

  Measured 2026-08-01 with the toolchain that README pins (Lean 4.22.0), the
  file's OWN `#print axioms` line — `Tropical.lean:35` — prints:

      'tropical_solutions' depends on axioms: [propext, Classical.choice, Quot.sound]

  One declaration of sixty-six. The claim is false, the file has been printing
  its falsifier every time anyone compiled it, and `check.sh:63` greps only for

      sorryAx | ofReduceBool | ofReduceNat

  so THE GATE CHECKS TWO OF THE THREE ABSENCES THE README PROMISES, and the
  unchecked one is the false one. That is the finding: not an unsound proof —
  `Classical.choice` here is harmless — but a published census claim with no
  instrument behind exactly the field that failed.

  THE ROOT CAUSE, isolated below and transferable to anyone writing Lean under
  an axiom-census norm:

      `omega` on an IFF goal pulls in `Classical.choice`.
      `omega` on a plain equation or inequality does NOT.

  Verified identical in Lean 4.22.0 and Lean 4.32.0 — the two toolchains this
  record pins — so it is not a version accident. `tropical_solutions` is
  `by omega` on an `↔`; its neighbour `tropical_unique` is `by omega` on a plain
  equation and stays clean. Nothing was written wrong. The tactic's iff path
  simply costs an axiom, and no census-by-eye would ever catch which of two
  adjacent `by omega` proofs pays it.

  RUN:  lean omega_iff_choice.lean
        Expect exactly two lines, the first carrying Classical.choice and the
        second not. If both come back clean, the tactic changed and this
        specimen has expired — say so rather than deleting it.
-/

theorem iff_by_omega (x : Int) : 2 * x = 0 ↔ x = 0 := by omega
#print axioms iff_by_omega

theorem eq_by_omega (x : Int) : x + 0 = x := by omega
#print axioms eq_by_omega
