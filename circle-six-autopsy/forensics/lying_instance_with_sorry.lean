inductive U | u1 | ui | um1 | umi
deriving DecidableEq

/- ATTEMPT: an instance that claims every proposition about U is true,
   without checking anything. If this compiled, every `decide` in the
   file would be worthless. -/
instance liar (p : U → Prop) [DecidablePred p] : Decidable (∀ a, p a) :=
  isTrue (by sorry)

theorem false_thing : ∀ a : U, a = U.u1 := by decide
#print axioms false_thing
