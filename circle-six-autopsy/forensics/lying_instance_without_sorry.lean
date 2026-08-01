inductive U | u1 | ui | um1 | umi
deriving DecidableEq
instance liar2 (p : U → Prop) [DecidablePred p] : Decidable (∀ a, p a) :=
  isTrue (fun a => by trivial)
