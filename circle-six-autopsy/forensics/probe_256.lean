/- Step 1: the seal's arithmetic, the four units, and the bridge between them. -/

structure GZ where
  re : Int
  im : Int
deriving DecidableEq, Repr

namespace GZ
def zero : GZ := ⟨0, 0⟩
def one  : GZ := ⟨1, 0⟩
def I    : GZ := ⟨0, 1⟩
def mul (z w : GZ) : GZ := ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩
def conj (z : GZ) : GZ := ⟨z.re, -z.im⟩
def neg (z : GZ) : GZ := ⟨-z.re, -z.im⟩
end GZ

/-- The four units of `Z[i]`, as a four-element type so the kernel can sweep them. -/
inductive U | u1 | ui | um1 | umi
deriving DecidableEq, Repr

namespace U
def all : List U := [u1, ui, um1, umi]

def toGZ : U → GZ
  | u1 => ⟨1, 0⟩ | ui => ⟨0, 1⟩ | um1 => ⟨-1, 0⟩ | umi => ⟨0, -1⟩

def mul : U → U → U
  | u1,  y   => y
  | x,   u1  => x
  | ui,  ui  => um1
  | ui,  um1 => umi
  | ui,  umi => u1
  | um1, ui  => umi
  | um1, um1 => u1
  | um1, umi => ui
  | umi, ui  => u1
  | umi, um1 => ui
  | umi, umi => um1

def conj : U → U
  | u1 => u1 | ui => umi | um1 => um1 | umi => ui

def inv : U → U
  | u1 => u1 | ui => umi | um1 => um1 | umi => ui


/-- No Mathlib here, so `decide` has no way to quantify over `U` or `Bool`.
    These two instances are the enumeration, and nothing else in this file
    depends on anything outside Lean's core. -/
instance decAllU (p : U → Prop) [DecidablePred p] : Decidable (∀ a, p a) :=
  if h1 : p .u1 then
    if h2 : p .ui then
      if h3 : p .um1 then
        if h4 : p .umi then isTrue (fun a => by cases a <;> assumption)
        else isFalse (fun h => h4 (h _))
      else isFalse (fun h => h3 (h _))
    else isFalse (fun h => h2 (h _))
  else isFalse (fun h => h1 (h _))

instance decAllBool (p : Bool → Prop) [DecidablePred p] : Decidable (∀ b, p b) :=
  if h1 : p false then
    if h2 : p true then isTrue (fun b => by cases b <;> assumption)
    else isFalse (fun h => h2 (h _))
  else isFalse (fun h => h1 (h _))

/-- THE BRIDGE. The four-element type is not a new object: it is the seal's
    `mul` and `conj`, on the seal's units, in a form the kernel can enumerate. -/
theorem toGZ_mul : ∀ a b : U, (mul a b).toGZ = GZ.mul a.toGZ b.toGZ := by decide

theorem toGZ_conj : ∀ a : U, (conj a).toGZ = GZ.conj a.toGZ := by decide

theorem toGZ_inj : ∀ a b : U, a.toGZ = b.toGZ → a = b := by decide

/-- Each `U` really is a unit of `Z[i]` in the seal's sense: it has a partner. -/
theorem is_unit : ∀ a : U, GZ.mul a.toGZ (inv a).toGZ = GZ.one := by decide

/-- **CHECK 1, in the kernel.** `conj` IS the inversion map on the units. -/
theorem conj_eq_inv : ∀ a : U, conj a = inv a := by decide

/-- And it is not a coincidence of the table: the seal DEFINES inversion as
    `conj` (`unitGroup.inv := Un.inv'`, `inv' u := ⟨conj u.val, _⟩`). This is
    that fact, checked on the representatives. -/
theorem conj_is_the_inverse : ∀ a : U, GZ.mul a.toGZ (GZ.conj a.toGZ) = GZ.one := by decide

/-- The scope is load-bearing: OFF the units the two maps part company at once.
    `mul z (conj z) = ⟨N z, 0⟩`, so `1+i` is the immediate counterexample. -/
theorem conj_not_inv_off_units :
    GZ.mul ⟨1, 1⟩ (GZ.conj ⟨1, 1⟩) ≠ GZ.one := by decide

/-- σ, the non-trivial Galois action, is genuinely non-trivial. -/
theorem conj_ne_id : ∃ a : U, conj a ≠ a := ⟨ui, by decide⟩

end U

/- ---------------------------------------------------------------------------
   Symbols. A symbol is 8 unit values indexed by (a,b,c) : Bool³, carried as a
   Nat code < 65536 so the kernel can sweep the whole space.
   --------------------------------------------------------------------------- -/

def decU : Nat → U
  | 0 => .u1 | 1 => .ui | 2 => .um1 | _ => .umi

def idx (a b c : Bool) : Nat :=
  (if a then 4 else 0) + (if b then 2 else 0) + (if c then 1 else 0)

def pow4 : Nat → Nat
  | 0 => 1 | n+1 => 4 * pow4 n

/-- The symbol with code `n`, read at the label triple `(a,b,c)`. -/
def sym (n : Nat) (a b c : Bool) : U := decU ((n / pow4 (idx a b c)) % 4)

/-- σ acting on a coefficient, indexed by the first group element. -/
def act (a : Bool) (x : U) : U := if a then U.conj x else x

/-- The seal's pentagon, in reduced form:
      F(a,b,c)·F(a,b+c,d)·F(b,c,d) = F(a+b,c,d)·F(a,b,c+d)          -/
def pentAt (F : Bool → Bool → Bool → U) (a b c d : Bool) : Bool :=
  U.mul (U.mul (F a b c) (F a (xor b c) d)) (F b c d)
    == U.mul (F (xor a b) c d) (F a b (xor c d))

/-- The σ-twisted cocycle condition: the SAME composition with the action
    inserted at the leading face, which is where the inhomogeneous complex
    puts it. This is the only difference between the two columns. -/
def sigAt (F : Bool → Bool → Bool → U) (a b c d : Bool) : Bool :=
  U.mul (U.mul (F a b c) (F a (xor b c) d)) (act a (F b c d))
    == U.mul (F (xor a b) c d) (F a b (xor c d))

def allBool4 : List (Bool × Bool × Bool × Bool) :=
  [(false,false,false,false),
   (false,false,false,true),
   (false,false,true,false),
   (false,false,true,true),
   (false,true,false,false),
   (false,true,false,true),
   (false,true,true,false),
   (false,true,true,true),
   (true,false,false,false),
   (true,false,false,true),
   (true,false,true,false),
   (true,false,true,true),
   (true,true,false,false),
   (true,true,false,true),
   (true,true,true,false),
   (true,true,true,true)]

def isPent (n : Nat) : Bool := allBool4.all fun p => pentAt (sym n) p.1 p.2.1 p.2.2.1 p.2.2.2
def isSig  (n : Nat) : Bool := allBool4.all fun p => sigAt  (sym n) p.1 p.2.1 p.2.2.1 p.2.2.2

def countUpTo (p : Nat → Bool) : Nat → Nat → Nat
  | 0,   acc => acc
  | k+1, acc => countUpTo p k (if p k then acc + 1 else acc)

set_option maxHeartbeats 0
set_option maxRecDepth 1000000
theorem p256 : countUpTo isPent 256 0 = 1 := by decide
