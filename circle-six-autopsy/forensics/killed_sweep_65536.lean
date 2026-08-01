set_option maxRecDepth 8000
set_option maxHeartbeats 1000000
/- The claims that do not need the 65536 sweep. -/

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

/-! ## The symbols the seal names -/

def topCell (u : U) : Sym := fun a b c => if a && b && c then u else .u1
def boson   : Sym := topCell .u1              -- sliceCore one
def fermion : Sym := topCell .um1             -- fermionCochain / sliceCore (neg one)
def sliceI  : Sym := topCell .ui              -- sliceCore I
def twistedBoson : Sym := fun _ b c => if c then (if b then .ui else .umi) else .u1
def fakeCocycle  : Sym := fun a b c => if !a && !b && c then .ui else .u1


/-! ## The sweep. Binary splitting (depth 16, not 65536-deep unary recursion,
     which aborts the kernel) and one decode per symbol rather than per access. -/

structure S8 where
  v000 : U
  v001 : U
  v010 : U
  v011 : U
  v100 : U
  v101 : U
  v110 : U
  v111 : U
deriving DecidableEq

def decode (n : Nat) : S8 :=
  ⟨decU (n % 4), decU (n / 4 % 4), decU (n / 16 % 4), decU (n / 64 % 4),
   decU (n / 256 % 4), decU (n / 1024 % 4), decU (n / 4096 % 4), decU (n / 16384 % 4)⟩

def S8.get (s : S8) : Sym
  | false, false, false => s.v000 | false, false, true  => s.v001
  | false, true,  false => s.v010 | false, true,  true  => s.v011
  | true,  false, false => s.v100 | true,  false, true  => s.v101
  | true,  true,  false => s.v110 | true,  true,  true  => s.v111

/-- The symbol with code `n`. -/
def symOf (n : Nat) : Sym := (decode n).get

structure Counts where
  nPent : Nat
  nSig : Nat
  nBoth : Nat
deriving DecidableEq, Repr

def Counts.add (x y : Counts) : Counts :=
  ⟨x.nPent + y.nPent, x.nSig + y.nSig, x.nBoth + y.nBoth⟩

/-- The two predicates at a single code, evaluated against the SAME `pentagon`
    and `isCocycle` definitions the named theorems above use. -/
def at1 (n : Nat) : Counts :=
  let F := symOf n
  let p := decide (pentagon F)
  let s := decide (isCocycle true F)
  ⟨if p then 1 else 0, if s then 1 else 0, if p && s then 1 else 0⟩

def pow2 : Nat → Nat | 0 => 1 | n+1 => 2 * pow2 n

/-- `sweep d lo` visits exactly `2^d` codes starting at `lo`. -/
def sweep : Nat → Nat → Counts
  | 0,    lo => at1 lo
  | d+1,  lo => Counts.add (sweep d lo) (sweep d (lo + pow2 d))

set_option maxHeartbeats 0
theorem sweep_counts : sweep 16 0 = ⟨32, 64, 8⟩ := by decide
