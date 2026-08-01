/-
  omega_iff_choice.lean — the trigger, isolated, and the repair, proved.

  WHY IT EXISTS. `GAP/lean/README.md:12` (branch `rate-instrument-proposal`)
  publishes this census claim about its sixty-six declarations:

      **No `sorryAx`, no `Classical.choice`, no `ofReduceBool`.**

  Measured 2026-08-01 on the toolchain that README pins, Lean 4.22.0, the file's
  OWN `#print axioms` line — `Tropical.lean:35` — prints:

      'tropical_solutions' depends on axioms: [propext, Classical.choice, Quot.sound]

  One declaration of sixty-six. The file has been printing its own falsifier
  every time anyone compiled it, and `check.sh:63` greps only for

      sorryAx | ofReduceBool | ofReduceNat

  so THE GATE CHECKS TWO OF THE THREE ABSENCES THE README PROMISES, and the
  unchecked one is the false one. Nothing here is unsound — `Classical.choice`
  arriving from a tactic is harmless. The defect is a published claim with no
  instrument behind exactly the field that failed.

  ─────────────────────────────────────────────────────────────────────────────
  PART 1 — THE TRIGGER. Measured identically on Lean 4.22.0 and Lean 4.32.0,
  the two toolchains this record pins, so it is not a version accident.

      goal shape given to `omega`              Classical.choice?
      ───────────────────────────────────────  ─────────────────
      an atomic equation or inequality          no
      a DISJUNCTION of atoms                    no
      a CONJUNCTION                             YES
      an IFF  (a conjunction of implications)   YES
      a disjunction OF CONJUNCTIONS             YES
      a conjunction in a HYPOTHESIS             no

  **The trigger is a conjunction in the GOAL.** Hypotheses cost nothing.
  `tropical_solutions` is `by omega` on an `↔`; its neighbour `tropical_unique`
  is `by omega` on a plain equation and stays clean. Nothing was written wrong.
  No census-by-eye could ever catch which of two adjacent `by omega` proofs
  pays the axiom — which is the whole argument for putting the field in a gate.
  ─────────────────────────────────────────────────────────────────────────────
-/

theorem t_atomic (x : Int) (h : x = 0) : 2 * x = 0 := by omega
#print axioms t_atomic                    -- propext, Quot.sound

theorem t_or (x : Int) (h : 0 ≤ x) : x = 0 ∨ 0 < x := by omega
#print axioms t_or                        -- propext, Quot.sound

theorem t_and (x : Int) (h : x = 0) : 2 * x = 0 ∧ x + x = 0 := by omega
#print axioms t_and                       -- + Classical.choice

theorem t_iff (x : Int) : 2 * x = 0 ↔ x = 0 := by omega
#print axioms t_iff                       -- + Classical.choice

theorem t_and_hyp (x : Int) (h : x = 0 ∧ 0 ≤ x) : 2 * x = 0 := by omega
#print axioms t_and_hyp                   -- propext, Quot.sound

/-
  ─────────────────────────────────────────────────────────────────────────────
  PART 2 — THE REPAIR. The statement below is `GAP/lean/Tropical.lean:17`
  verbatim. The proof is rearranged so that every goal handed to `omega` is a
  single (in)equality: `constructor` splits the iff, `by_cases` picks the
  disjunct, and the anonymous constructor splits each conjunction before omega
  is called. Same theorem, same kernel, one fewer axiom — on BOTH toolchains.

  Drop this proof into `Tropical.lean` and `README.md:12` becomes true.
  ─────────────────────────────────────────────────────────────────────────────
-/

theorem tropical_solutions_clean (G x : Int) :
    2 * x = max x G ↔ ((x = 0 ∧ G ≤ 0) ∨ (2 * x = G ∧ 0 < x)) := by
  constructor
  · intro h
    by_cases h0 : 0 < x
    · exact Or.inr ⟨by omega, by omega⟩
    · exact Or.inl ⟨by omega, by omega⟩
  · intro h
    rcases h with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · omega
    · omega

#print axioms tropical_solutions_clean    -- propext, Quot.sound  ← the repair

/-
  RUN:  lean omega_iff_choice.lean

  Expect six census lines. `t_and` and `t_iff` carry `Classical.choice`; the
  other four do not, `tropical_solutions_clean` among them. If the two dirty
  ones come back clean, `omega` changed and this specimen has expired — say so
  in the record rather than deleting it.
-/
