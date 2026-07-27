/- S7a DESIGN PROBE (norm 15) -- measures reach, ships nothing.
   Question: is "every class meets the normalized slice" statable and
   provable in zero-import Lean over Z[i]?

   This file is a SCRATCH probe. It duplicates only the minimum ring
   scaffolding it needs (kept deliberately tiny) so it can be compiled
   in isolation to test which fragments type-check and which need
   machinery out of zero-import reach. Nothing here is shipped as a
   theorem in Zi.lean; the shipped result is decided AFTER this probe. -/

/- ---- minimal Z[i] scaffold (mirrors Zi.lean, self-contained) ---- -/
structure Zi where
  re : Int
  im : Int
deriving DecidableEq, Repr

namespace Zi

def zero : Zi := ⟨0,0⟩
def one  : Zi := ⟨1,0⟩
def I    : Zi := ⟨0,1⟩
def add (x y : Zi) : Zi := ⟨x.re+y.re, x.im+y.im⟩
def neg (x : Zi) : Zi := ⟨-x.re, -x.im⟩
def mul (x y : Zi) : Zi := ⟨x.re*y.re - x.im*y.im, x.re*y.im + x.im*y.re⟩

/- ==================================================================
   PROBE 1: can we even STATE "general F-symbol", "normalized slice",
   "gauge", "class", "meets"?  State them as plain Prop/data. This is
   the honest-statement test the handoff flagged as the hard part.
   ================================================================== -/

/-- a GENERAL Z2-fusion F-symbol: an arbitrary assignment of a Z[i]
    value to each 6-index slot. No normalization assumed. -/
def FSym := Nat → Nat → Nat → Nat → Nat → Nat → Zi

/-- admissibility mask (bench LINE 102 shape): the slot is live iff
    x=(a+b)%2, y=(b+c)%2, d=(a+b+c)%2. Off-mask entries are forced 0. -/
def admissible (a b c d x y : Nat) : Prop :=
  x = (a+b)%2 ∧ y = (b+c)%2 ∧ d = (a+b+c)%2

instance (a b c d x y) : Decidable (admissible a b c d x y) := by
  unfold admissible; exact inferInstance

/-- NORMALIZED slice: an F-symbol is on the slice iff it is off-mask-zero
    AND its only free live value sits at (1,1,1) -- i.e. it equals the
    one-parameter family Fz2 f for some f. STATE it as: there is an f
    s.t. G agrees with the canonical slice symbol everywhere. -/
def sliceSym (f : Zi) (a b c d x y : Nat) : Zi :=
  if admissible a b c d x y then
    (if a = 1 ∧ b = 1 ∧ c = 1 then f else one)
  else zero

/-- "G is ON the normalized slice" -- honest, machinery-free: G is
    literally one of the slice symbols. -/
def onSlice (G : FSym) : Prop :=
  ∃ f : Zi, ∀ a b c d x y, G a b c d x y = sliceSym f a b c d x y

/-- a VERTEX GAUGE: eta : Z2 x Z2 -> Z[i] (into units, carried as a
    hypothesis where needed). This matches Zi.lean's detaNum/detaDen. -/
def Gauge := Nat → Nat → Zi

/- The gauge ACTION on a full F-symbol is the cochain product
   G'(a,b,c,d,x,y) = G(a,b,c,d,x,y) * eta(a,b)*eta(?)... -- and HERE is
   the wall: writing the action on the 6-index object honestly needs the
   full associator index bookkeeping (which pair of the six indices each
   eta factor attaches to), the SAME bookkeeping the bench encodes only
   implicitly. Zi.lean sidesteps this by working with detaNum/detaDen at
   the SINGLE slot (1,1,1) plus two zero-slot rows -- it never forms the
   action on a general G. So: STATING the action on general G is where
   zero-import honesty gets expensive. -/

/-- "two F-symbols are gauge-equivalent" -- the honest general statement
    we would NEED: exists a gauge eta relating them slotwise via the
    coboundary. We STATE the shape but the coboundary on a general slot
    is exactly the unresolved bookkeeping. Placeholder relation: -/
def gaugeEquiv (G H : FSym) : Prop :=
  ∃ eta : Gauge, ∀ a b c d x y,
    -- the honest coboundary would go here; the general-slot form is the
    -- open piece. We write the (1,1,1)-slot projection that Zi.lean DOES
    -- pin down, and leave the rest as the measured gap:
    (a = 1 ∧ b = 1 ∧ c = 1) →
      mul (H a b c d x y) (mul (eta 0 1) (eta 1 1))
        = mul (G a b c d x y) (mul (eta 1 1) (eta 1 0))

/-- "every class meets the slice" -- the target sentence, stated: every
    pentagon-satisfying general F-symbol is gauge-equivalent to a slice
    symbol. (pentagon on general FSym omitted from the probe -- see note) -/
def everyClassMeetsSlice : Prop :=
  ∀ G : FSym, ∃ H : FSym, onSlice H ∧ gaugeEquiv G H

end Zi
