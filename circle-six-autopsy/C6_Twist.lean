/-
  C6_Twist.lean — the charge, in the kernel. Circle Six, round two.

  WHAT THIS IS
    Round one (ROUND-ONE.md, probe/) answered the charge in Python. Python is
    outside the prose but it is not the kernel, and this compartment's terminal
    condition is the kernel. This file re-decides the part that fits.

    Lean 4.22.0, no Mathlib, no imports — the seal imports nothing, and that
    turns out to be load-bearing rather than aesthetic. Reproduce with:

        lean lean/C6_Twist.lean ; echo "EXIT=$?"

    Exit 0 is the only evidence. `native_decide` is NOT used anywhere: it
    trusts the compiler rather than the kernel, and a compartment whose one
    rule is "something outside the prose decides" cannot spend its verdict on
    a faster oracle. Audit in lean/AUDIT.txt: 41 theorems, 41 `#print axioms`
    lines, 40 axiom-free, 1 on `propext`, 0 `sorryAx`.

  WHAT IS PROVED HERE
    - `conj` IS inversion on the units, with the scope shown to be
      load-bearing (`conj_not_inv_off_units`).
    - `pentagon_iff_seal` — the reduced pentagon this file sweeps IS the seal's
      `genPentagonHolds`, admissibility guard and Int label arithmetic
      included. Without this the rest would be about a model, not the seal.
    - The four-row table, both actions. `-1` and `i` trade places exactly.
    - `fermion_is_sigma_coboundary` — the fermion becomes gauge-trivial under
      the twist, with the trivialising gauge written down rather than asserted.
    - `sliceI_*` — the σ-generator is `sliceCore I`, an object the seal can
      already name and which the seal's own pentagon rejects.
    - |B³| = 16 untwisted / 32 twisted, |ker d²| = 16 / 8, and B³ ⊆ Z³ in both
      readings.
    - `twist_vanishes_on_reals` — a real proof, not a `decide`: on ±1-valued
      symbols the twist vanishes identically. Circle Five's boson and fermion
      are both real, so five circles computed with the trivial action and got
      the right answer because the question had no visible consequence anywhere
      they looked.

    - The braiding sector answers the obvious objection to the line above.
      `twist_vanishes_on_reals` says σ is invisible on ±1-valued SYMBOLS. It is
      NOT invisible on the seal's braidings: `boson_braids_real` and
      `fermion_braids_imaginary` show the boson braids by ±1 and the fermion
      braids by ±i, and `sigma_swaps_fermion_braidings` shows σ exchanges the
      fermion's two braidings with no fixed point. `edict_fermion_fails` shows
      `SelfInverse` -- "the roomy edict" -- holds for the boson and fails for
      the fermion, because i² = −1. The seal already writes σ there:
      `hexInvHolds f R = hexagonHolds f (conj R)`.

      So the honest statement is NOT "the question had no consequence." It is:
      **σ is invisible in the pentagon sector and visibly a chirality swap in
      the braiding sector, and the seal's own classification
      (`IsClassifiedSymbol` = unit-valued + pentagon) is defined so that only
      the first sector is looked at.** The consequence was always visible in
      the ordinary place one looks for it. It was outside what got classified.

  WHAT IS **NOT** PROVED HERE, AND MUST NOT BE READ AS IF IT WERE
    The 65536-symbol sweep — |Z³| = 32 untwisted and 64 twisted, 8 shared, and
    the identity `pentagon ↔ isCocycle false` across the whole space. Those
    numbers are COMPILER-CHECKED ONLY (`#eval`), never kernel-decided. Two
    kernel runs at depth 16 were killed by a container restart about three
    minutes into a ten-minute job. They are not in this file and no theorem
    below depends on them.

    Engineering note for whoever finishes it, because it cost real time: the
    obvious unary recursion `countUpTo p (n+1)` ABORTS the kernel (SIGABRT) at
    16384 — it is a stack failure, not a heartbeat failure, and raising
    maxHeartbeats does not touch it. Binary splitting on a depth parameter
    (`sweep (d+1) lo = add (sweep d lo) (sweep d (lo + 2^d))`) has depth 16
    instead of 65536 and clears it: depth 12 kernel-decides in 37s, so depth 16
    is ~10 minutes. Decode each symbol once into a structure rather than
    dividing per access.

  Consistent with the compartment's rule, nothing here is a finding. It is a
  kernel-decided result inside a compartment whose exit requires it to be
  rewritten where the canon applies.
-/

/- The claims that do not need the 65536 sweep. -/

set_option maxRecDepth 8000

structure GZ where
  re : Int
  im : Int
deriving DecidableEq, Repr

namespace GZ
def one  : GZ := ⟨1, 0⟩
def mul (z w : GZ) : GZ := ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩
def conj (z : GZ) : GZ := ⟨z.re, -z.im⟩
end GZ

inductive U | u1 | ui | um1 | umi
deriving DecidableEq, Repr

namespace U
def toGZ : U → GZ | u1 => ⟨1,0⟩ | ui => ⟨0,1⟩ | um1 => ⟨-1,0⟩ | umi => ⟨0,-1⟩
def mul : U → U → U
  | u1, y => y | x, u1 => x
  | ui, ui => um1  | ui, um1 => umi | ui, umi => u1
  | um1, ui => umi | um1, um1 => u1 | um1, umi => ui
  | umi, ui => u1  | umi, um1 => ui | umi, umi => um1
def conj : U → U | u1 => u1 | ui => umi | um1 => um1 | umi => ui
def inv  : U → U | u1 => u1 | ui => umi | um1 => um1 | umi => ui
end U

instance decAllU (p : U → Prop) [DecidablePred p] : Decidable (∀ a, p a) :=
  if h1 : p .u1 then if h2 : p .ui then if h3 : p .um1 then
    if h4 : p .umi then isTrue (fun a => by cases a <;> assumption)
    else isFalse (fun h => h4 (h _))
  else isFalse (fun h => h3 (h _)) else isFalse (fun h => h2 (h _))
  else isFalse (fun h => h1 (h _))

instance decAllBool (p : Bool → Prop) [DecidablePred p] : Decidable (∀ b, p b) :=
  if h1 : p false then
    if h2 : p true then isTrue (fun b => by cases b <;> assumption)
    else isFalse (fun h => h2 (h _))
  else isFalse (fun h => h1 (h _))

/-! ## The bridge: `U` is the seal's units under the seal's arithmetic -/

theorem toGZ_mul : ∀ a b : U, (U.mul a b).toGZ = GZ.mul a.toGZ b.toGZ := by decide
theorem toGZ_conj : ∀ a : U, (U.conj a).toGZ = GZ.conj a.toGZ := by decide
theorem toGZ_inj : ∀ a b : U, a.toGZ = b.toGZ → a = b := by decide
theorem is_unit : ∀ a : U, GZ.mul a.toGZ (U.inv a).toGZ = GZ.one := by decide

/-! ## CHECK 1 — `conj` IS inversion on the units -/

theorem conj_eq_inv : ∀ a : U, U.conj a = U.inv a := by decide
theorem conj_is_the_inverse : ∀ a : U, GZ.mul a.toGZ (GZ.conj a.toGZ) = GZ.one := by decide

/-- The scope is load-bearing: off the units the two maps part at once. -/
theorem conj_not_inv_off_units : GZ.mul ⟨1,1⟩ (GZ.conj ⟨1,1⟩) ≠ GZ.one := by decide

/-- σ is genuinely non-trivial, so nothing below is vacuous. -/
theorem sigma_ne_id : ∃ a : U, U.conj a ≠ a := ⟨.ui, by decide⟩

/-! ## The complex -/

abbrev Sym := Bool → Bool → Bool → U
abbrev Gge := Bool → Bool → U

/-- σ applied at the leading face, indexed by the group element and the reading.
    `tw = false` is the seal's complex; `tw = true` is the counterfactual one. -/
def act (tw a : Bool) (x : U) : U := if tw && a then U.conj x else x

/-- `d³`, both readings. `tw = false` is exactly the seal's `d3`. -/
def d3 (tw : Bool) (F : Sym) (a b c d : Bool) : U :=
  U.mul (U.mul (U.mul (U.mul (act tw a (F b c d)) (U.inv (F (xor a b) c d)))
    (F a (xor b c) d)) (U.inv (F a b (xor c d)))) (F a b c)

/-- `d²`, both readings. -/
def d2 (tw : Bool) (g : Gge) (a b c : Bool) : U :=
  U.mul (U.mul (act tw a (g b c)) (U.inv (g (xor a b) c)))
        (U.mul (g a (xor b c)) (U.inv (g a b)))

def isCocycle (tw : Bool) (F : Sym) : Prop := ∀ a b c d, d3 tw F a b c d = .u1
instance (tw) (F) : Decidable (isCocycle tw F) := by unfold isCocycle; infer_instance

/-- The seal's pentagon, reduced form, stated on its own so it can be compared
    with `isCocycle false` rather than assumed equal to it. -/
def pentagon (F : Sym) : Prop :=
  ∀ a b c d, U.mul (U.mul (F a b c) (F a (xor b c) d)) (F b c d)
           = U.mul (F (xor a b) c d) (F a b (xor c d))
instance (F) : Decidable (pentagon F) := by unfold pentagon; infer_instance

/-! ## Gauges, enumerated by code, for the coboundary question -/

def decU : Nat → U | 0 => .u1 | 1 => .ui | 2 => .um1 | _ => .umi
def gge (n : Nat) : Gge := fun a b =>
  decU ((n / (if a then (if b then 64 else 16) else (if b then 4 else 1))) % 4)

def eqSym (F G : Sym) : Bool :=
  decide (∀ a b c, F a b c = G a b c)

/-- `F` is a coboundary in reading `tw` iff some gauge among the 256 hits it. -/
def cobAux (tw : Bool) (F : Sym) : Nat → Bool
  | 0   => false
  | n+1 => eqSym (d2 tw (gge n)) F || cobAux tw F n
def isCoboundary (tw : Bool) (F : Sym) : Bool := cobAux tw F 256

/-! ## Fidelity: the reduced pentagon IS the seal's `genPentagonHolds`.
     Transcribed from lean/C6_SEED.lean with Int labels and the admissibility
     guard, so the reduction is proved rather than assumed. -/

def GZ.zero : GZ := ⟨0, 0⟩

/-- the seal's `boolOf` -/
def boolOf (i : Int) : Bool := if i = 1 then true else false
/-- the seal's `lab` -/
def lab (b : Bool) : Int := if b then 1 else 0

/-- the seal's `symbolOf`: a `U`-valued symbol read as the seal reads it -/
def Fint (F : Sym) : Int → Int → Int → GZ :=
  fun i j k => (F (boolOf i) (boolOf j) (boolOf k)).toGZ

/-- the seal's `Fgen`, verbatim -/
def Fgen (F : Int → Int → Int → GZ) (a b c d x y : Int) : GZ :=
  if x = (a + b) % 2 ∧ y = (b + c) % 2 ∧ d = (a + b + c) % 2 then F a b c else GZ.zero

/-- the seal's `genPentLhs`, verbatim -/
def genPentLhs (F : Int → Int → Int → GZ) (a b c d : Int) : GZ :=
  let x := (a + b) % 2; let y := (x + c) % 2; let t := (y + d) % 2
  let w := (c + d) % 2; let v := (b + w) % 2; let u := (b + c) % 2
  GZ.mul (GZ.mul (Fgen F a b c y x u) (Fgen F a u d t y v)) (Fgen F b c d v u w)

/-- the seal's `genPentRhs`, verbatim -/
def genPentRhs (F : Int → Int → Int → GZ) (a b c d : Int) : GZ :=
  let x := (a + b) % 2; let y := (x + c) % 2; let t := (y + d) % 2
  let w := (c + d) % 2; let v := (b + w) % 2
  GZ.mul (Fgen F x c d t y w) (Fgen F a b w t x v)

/-- **The reduction, proved.** No admissibility guard ever fires: every one of
    the five `Fgen` call sites is on-locus at all 16 label points, so the seal's
    composition collapses to the three- and two-factor products the sweep uses. -/
theorem lhs_reduces (F : Sym) (a b c d : Bool) :
    genPentLhs (Fint F) (lab a) (lab b) (lab c) (lab d)
      = GZ.mul (GZ.mul (F a b c).toGZ (F a (xor b c) d).toGZ) (F b c d).toGZ := by
  cases a <;> cases b <;> cases c <;> cases d <;> rfl

theorem rhs_reduces (F : Sym) (a b c d : Bool) :
    genPentRhs (Fint F) (lab a) (lab b) (lab c) (lab d)
      = GZ.mul (F (xor a b) c d).toGZ (F a b (xor c d)).toGZ := by
  cases a <;> cases b <;> cases c <;> cases d <;> rfl

theorem lhs_reduces_U (F : Sym) (a b c d : Bool) :
    genPentLhs (Fint F) (lab a) (lab b) (lab c) (lab d)
      = (U.mul (U.mul (F a b c) (F a (xor b c) d)) (F b c d)).toGZ := by
  rw [lhs_reduces, toGZ_mul, toGZ_mul]

theorem rhs_reduces_U (F : Sym) (a b c d : Bool) :
    genPentRhs (Fint F) (lab a) (lab b) (lab c) (lab d)
      = (U.mul (F (xor a b) c d) (F a b (xor c d))).toGZ := by
  rw [rhs_reduces, toGZ_mul]

/-- **`pentagon` is the seal's pentagon**, guard and Int label arithmetic included. -/
theorem pentagon_iff_seal (F : Sym) :
    pentagon F ↔ ∀ a b c d : Bool,
      genPentLhs (Fint F) (lab a) (lab b) (lab c) (lab d)
        = genPentRhs (Fint F) (lab a) (lab b) (lab c) (lab d) := by
  constructor
  · intro h a b c d
    rw [lhs_reduces_U, rhs_reduces_U, h a b c d]
  · intro h a b c d
    have hx := h a b c d
    rw [lhs_reduces_U, rhs_reduces_U] at hx
    exact toGZ_inj _ _ hx


/-! ## The symbols the seal names -/

def topCell (u : U) : Sym := fun a b c => if a && b && c then u else .u1
def boson   : Sym := topCell .u1              -- sliceCore one
def fermion : Sym := topCell .um1             -- fermionCochain / sliceCore (neg one)
def sliceI  : Sym := topCell .ui              -- sliceCore I
def twistedBoson : Sym := fun _ b c => if c then (if b then .ui else .umi) else .u1
def fakeCocycle  : Sym := fun a b c => if !a && !b && c then .ui else .u1

/-! ## RESULT 1 — the four-row table, in the kernel.
     Untwisted the classification is carried by ±1 and ±i is not admissible.
     Twisted, ±1 is gauge-trivial and ±i carries the classification. -/

theorem row_one_untwisted   : isCocycle false boson   ∧ isCoboundary false boson   = true := by decide
theorem row_one_twisted     : isCocycle true  boson   ∧ isCoboundary true  boson   = true := by decide

theorem row_i_untwisted     : ¬ isCocycle false sliceI := by decide
theorem row_i_twisted       : isCocycle true sliceI ∧ isCoboundary true sliceI = false := by decide

theorem row_neg1_untwisted  : isCocycle false fermion ∧ isCoboundary false fermion = false := by decide
theorem row_neg1_twisted    : isCocycle true  fermion ∧ isCoboundary true  fermion = true  := by decide

theorem row_negi_untwisted  : ¬ isCocycle false (topCell .umi) := by decide
theorem row_negi_twisted    : isCocycle true (topCell .umi) ∧ isCoboundary true (topCell .umi) = false := by decide

/-! ## RESULT 2 — the fermion becomes gauge-trivial, with the witness written down -/

/-- The gauge that trivialises the fermion under σ: `g(1,1) = i`, `1` elsewhere. -/
def gFermion : Gge := fun a b => if a && b then .ui else .u1

theorem fermion_is_sigma_coboundary : ∀ a b c, d2 true gFermion a b c = fermion a b c := by decide
theorem fermion_not_untwisted_coboundary : isCoboundary false fermion = false := by decide

/-! ## RESULT 3 — twistedBoson: a pentagon solution that is not a σ-cocycle -/

theorem twistedBoson_pentagon : pentagon twistedBoson := by decide
theorem twistedBoson_not_sigma_cocycle : ¬ isCocycle true twistedBoson := by decide
theorem twistedBoson_untwisted_cocycle : isCocycle false twistedBoson := by decide
theorem twistedBoson_gauge_trivial : isCoboundary false twistedBoson = true := by decide

/-! ## RESULT 4 — sliceCore I: the σ-generator the seal can already name,
     and which the seal's own pentagon rejects -/

theorem sliceI_fails_pentagon : ¬ pentagon sliceI := by decide
theorem sliceI_is_sigma_cocycle : isCocycle true sliceI := by decide
theorem sliceI_not_sigma_coboundary : isCoboundary true sliceI = false := by decide

/-! ## RESULT 5 — the seal's negative control still behaves -/

theorem fakeCocycle_fails_both : ¬ pentagon fakeCocycle ∧ ¬ isCocycle true fakeCocycle := by decide

/-! ## RESULT 6 — why five circles never saw it.
     On real-valued symbols the twist vanishes identically, because `conj`
     fixes ±1. Circle Five's boson and fermion are both real. -/

def isReal (u : U) : Bool := u == .u1 || u == .um1

theorem conj_fixes_reals : ∀ u : U, isReal u = true → U.conj u = u := by decide

/-- Proved with an explicit `congrArg` rather than `simp`: `simp` pulls in
    `propext`, and with this written out the whole file depends on NO axioms
    at all -- not `propext`, not `Classical.choice`, not `Quot.sound`. -/
theorem twist_vanishes_on_reals (F : Sym) (h : ∀ a b c, isReal (F a b c) = true) :
    ∀ a b c d, d3 true F a b c d = d3 false F a b c d := by
  intro a b c d
  cases a
  · rfl
  · exact congrArg (fun z => U.mul (U.mul (U.mul (U.mul z (U.inv (F (xor true b) c d)))
      (F true (xor b c) d)) (U.inv (F true b (xor c d)))) (F true b c))
      (conj_fixes_reals _ (h b c d))

theorem boson_real   : ∀ a b c, isReal (boson a b c) = true := by decide
theorem fermion_real : ∀ a b c, isReal (fermion a b c) = true := by decide

/-! ## |B³| by enumeration: count gauges whose coboundary is not already
     produced by an earlier gauge. 256 gauges, so this is cheap. -/

def gaugeEq (g h : Gge) : Bool := decide (∀ a b, g a b = h a b)
def symEq (F G : Sym) : Bool := decide (∀ a b c, F a b c = G a b c)

/-- has some code `< m` the same coboundary as code `n`? -/
def seenBefore (tw : Bool) (n : Nat) : Nat → Bool
  | 0   => false
  | m+1 => symEq (d2 tw (gge m)) (d2 tw (gge n)) || seenBefore tw n m

/-- number of DISTINCT coboundaries among the 256 gauges = |B³| -/
def countB : Bool → Nat → Nat
  | _,  0    => 0
  | tw, n+1  => (if seenBefore tw n n then 0 else 1) + countB tw n

/-- size of ker d² -/
def countKer : Bool → Nat → Nat
  | _,  0   => 0
  | tw, n+1 => (if symEq (d2 tw (gge n)) (fun _ _ _ => U.u1) then 1 else 0) + countKer tw n

/-- every coboundary is a cocycle: B³ ⊆ Z³, in both readings -/
def cobAreCocycles (tw : Bool) : Nat → Bool
  | 0   => true
  | n+1 => decide (isCocycle tw (d2 tw (gge n))) && cobAreCocycles tw n

set_option maxHeartbeats 0

theorem B3_untwisted : countB false 256 = 16 := by decide
theorem B3_twisted   : countB true  256 = 32 := by decide
theorem ker_untwisted : countKer false 256 = 16 := by decide
theorem ker_twisted   : countKer true  256 = 8  := by decide
theorem cob_subset_cocycles_untwisted : cobAreCocycles false 256 = true := by decide
theorem cob_subset_cocycles_twisted   : cobAreCocycles true  256 = true := by decide

/-! ## Is the twist really invisible? The braiding says no.

    `twist_vanishes_on_reals` says σ has no consequence on ±1-valued SYMBOLS.
    Circle Five's boson and fermion are both real, so the pentagon sector sees
    nothing. But the seal also carries `Rs`, `hexLhs`, `hexRhs`, `hexagonHolds`,
    `hexInvHolds` and `SelfInverse` — and `hexInvHolds f R = hexagonHolds f (conj R)`.
    The seal already applies σ there. So: are the braidings real too? -/

def Fs (f : GZ) (a b c d x y : Int) : GZ :=
  if x = (a + b) % 2 ∧ y = (b + c) % 2 ∧ d = (a + b + c) % 2 then
    (if a = 1 ∧ b = 1 ∧ c = 1 then f else GZ.one)
  else GZ.zero

def Rs (R : GZ) (x y : Int) : GZ := if x = 1 ∧ y = 1 then R else GZ.one

def hexLhs (f R : GZ) (a b c d : Int) : GZ :=
  let e := (a + b) % 2; let z := (a + c) % 2
  GZ.mul (Rs R e c) (Fs f c a b d z e)

def hexRhs (f R : GZ) (a b c d : Int) : GZ :=
  let e := (a + b) % 2; let z := (a + c) % 2; let g := (b + c) % 2
  GZ.mul (GZ.mul (GZ.mul (Fs f a b c d e g) (Rs R b c)) (Fs f a c b d z g)) (Rs R a c)

/-- The seal's `hexagonHolds`, verbatim: Int labels, both label hypotheses. -/
def hexagonHolds (f R : GZ) : Prop :=
  ∀ a b c d : Int, (a = 0 ∨ a = 1) → (b = 0 ∨ b = 1) → (c = 0 ∨ c = 1) →
    (d = 0 ∨ d = 1) → d = ((a + b) % 2 + c) % 2 → d = ((a + c) % 2 + b) % 2 →
    hexLhs f R a b c d = hexRhs f R a b c d

/-- The seal's `hexInvHolds`: the same plumbing read at the CONJUGATE braiding.
    σ is already here, in the seal, applied to `R`. -/
def hexInvHolds (f R : GZ) : Prop := hexagonHolds f (GZ.conj R)

/-- The seal's `SelfInverse`: "the roomy edict — a braiding is its own inverse." -/
def SelfInverse (R : GZ) : Prop := GZ.mul R R = GZ.one
instance (R : GZ) : Decidable (SelfInverse R) := by unfold SelfInverse; infer_instance

/-- Int labels restricted to {0,1} are exactly Bool labels through `lab`. -/
theorem intBool (P : Int → Prop) :
    (∀ i : Int, (i = 0 ∨ i = 1) → P i) ↔ (∀ b : Bool, P (lab b)) := by
  constructor
  · intro h b; cases b
    · exact h 0 (Or.inl rfl)
    · exact h 1 (Or.inr rfl)
  · intro h i hi
    rcases hi with rfl | rfl
    · exact h false
    · exact h true

/-- Bool-quantified form of the seal's hexagon, so the kernel can enumerate it. -/
def hexB (f R : GZ) : Bool :=
  decide (∀ a b c d : Bool,
    lab d = ((lab a + lab b) % 2 + lab c) % 2 →
    lab d = ((lab a + lab c) % 2 + lab b) % 2 →
    hexLhs f R (lab a) (lab b) (lab c) (lab d)
      = hexRhs f R (lab a) (lab b) (lab c) (lab d))

theorem hexagonHolds_iff (f R : GZ) : hexagonHolds f R ↔ hexB f R = true := by
  constructor
  · intro h
    apply decide_eq_true
    intro a b c d h1 h2
    exact h _ _ _ _
      (by cases a <;> first | exact Or.inl rfl | exact Or.inr rfl)
      (by cases b <;> first | exact Or.inl rfl | exact Or.inr rfl)
      (by cases c <;> first | exact Or.inl rfl | exact Or.inr rfl)
      (by cases d <;> first | exact Or.inl rfl | exact Or.inr rfl) h1 h2
  · intro hb a b c d ha hbb hc hd h1 h2
    have h := of_decide_eq_true hb
    rcases ha with rfl|rfl <;> rcases hbb with rfl|rfl <;> rcases hc with rfl|rfl <;>
      rcases hd with rfl|rfl <;>
      first
        | exact h false false false false h1 h2 | exact h false false false true h1 h2
        | exact h false false true false h1 h2  | exact h false false true true h1 h2
        | exact h false true false false h1 h2  | exact h false true false true h1 h2
        | exact h false true true false h1 h2   | exact h false true true true h1 h2
        | exact h true false false false h1 h2  | exact h true false false true h1 h2
        | exact h true false true false h1 h2   | exact h true false true true h1 h2
        | exact h true true false false h1 h2   | exact h true true false true h1 h2
        | exact h true true true false h1 h2    | exact h true true true true h1 h2

/-! ### The answer: the boson braids REAL, the fermion braids IMAGINARY. -/

theorem boson_braids_real :
    hexB GZ.one ⟨1,0⟩ = true ∧ hexB GZ.one ⟨-1,0⟩ = true
  ∧ hexB GZ.one ⟨0,1⟩ = false ∧ hexB GZ.one ⟨0,-1⟩ = false := by decide

theorem fermion_braids_imaginary :
    hexB ⟨-1,0⟩ ⟨0,1⟩ = true ∧ hexB ⟨-1,0⟩ ⟨0,-1⟩ = true
  ∧ hexB ⟨-1,0⟩ ⟨1,0⟩ = false ∧ hexB ⟨-1,0⟩ ⟨-1,0⟩ = false := by decide

/-- σ FIXES each of the boson's braidings. -/
theorem sigma_fixes_boson_braidings :
    GZ.conj ⟨1,0⟩ = (⟨1,0⟩ : GZ) ∧ GZ.conj ⟨-1,0⟩ = (⟨-1,0⟩ : GZ) := by decide

/-- σ EXCHANGES the fermion's two braidings, with no fixed point. -/
theorem sigma_swaps_fermion_braidings :
    GZ.conj ⟨0,1⟩ = (⟨0,-1⟩ : GZ) ∧ GZ.conj ⟨0,-1⟩ = (⟨0,1⟩ : GZ)
  ∧ GZ.conj ⟨0,1⟩ ≠ (⟨0,1⟩ : GZ) ∧ GZ.conj ⟨0,-1⟩ ≠ (⟨0,-1⟩ : GZ) := by decide

/-- The roomy edict holds for the boson and FAILS for the fermion: i² = −1. -/
theorem edict_boson : SelfInverse ⟨1,0⟩ ∧ SelfInverse ⟨-1,0⟩ := by decide
theorem edict_fermion_fails : ¬ SelfInverse ⟨0,1⟩ ∧ ¬ SelfInverse ⟨0,-1⟩ := by decide
