/- S7a DESIGN PROBE part 3 (norm 15) -- route (i): the units of Z[i]
   are FINITE {1,i,-1,-i}. Test whether a unit-restricted form of the
   gauge-fixing / "meets the slice" statement becomes a decidable finite
   computation. Ships nothing; decides the reachable theorem's shape. -/

structure Zi where
  re : Int
  im : Int
deriving DecidableEq, Repr

namespace Zi

def one  : Zi := ⟨1,0⟩
def mul (x y : Zi) : Zi := ⟨x.re*y.re - x.im*y.im, x.re*y.im + x.im*y.re⟩
def conj (x : Zi) : Zi := ⟨x.re, -x.im⟩
def normSq (x : Zi) : Int := x.re*x.re + x.im*x.im

/-- the FOUR units of Z[i]. -/
def units : List Zi := [⟨1,0⟩, ⟨0,1⟩, ⟨-1,0⟩, ⟨0,-1⟩]

/-- every listed unit has normSq 1 (finite check). -/
theorem units_have_normSq_one : ∀ u ∈ units, normSq u = 1 := by decide

/-- and no two of the four units coincide (the group has 4 DISTINCT
    elements) -- pins the nest count for route (i). -/
theorem units_distinct : units.Nodup ∧ units.length = 4 := by
  exact ⟨by decide, by decide⟩

/-- CLOSURE OF THE UNIT GROUP under mul: the product of two units is a
    unit. A finite `decide` over the 4x4 table. -/
theorem units_closed_mul :
    ∀ u ∈ units, ∀ v ∈ units, mul u v ∈ units := by decide

/-- the (1,1,1)-slot motion of a UNIT gauge is a unit (the slot invariant
    lands in the finite unit group) -- matches Zi.lean's detaNum/detaDen
    at (1,1,1) = eta11*eta10 vs eta01*eta11. -/
def slotNum (_e01 e10 e11 : Zi) : Zi := mul e11 e10
def slotDen (e01 _e10 e11 : Zi) : Zi := mul e01 e11

/-- CORE REACHABLE FACT (route i): over the FINITE unit gauges, the
    slice-preserving condition (e01 = e10, from Zi.lean's
    slice_forces_eta_symmetric) makes the (1,1,1) slot motion TRIVIAL,
    for EVERY unit gauge with e01 = e10 -- verified by full finite
    enumeration, no symbolic cancellation needed. This is the
    unit-valued, fully-decidable witness that the slot is a gauge
    invariant of the slice. -/
theorem unit_slice_slot_invariant :
    ∀ e01 ∈ units, ∀ e10 ∈ units, ∀ e11 ∈ units,
      e01 = e10 → slotNum e01 e10 e11 = slotDen e01 e10 e11 := by
  decide

/-- and the SHARP CONVERSE (the honest core of "meets"): among unit
    gauges, slice-preservation (trivial slot motion) is EQUIVALENT to
    e01 = e10 -- so no unit gauge can move a symbol OFF the two-class
    slice without also moving the (1,1,1) slot. Full finite decide. -/
theorem unit_slice_iff_symmetric :
    ∀ e01 ∈ units, ∀ e10 ∈ units, ∀ e11 ∈ units,
      (slotNum e01 e10 e11 = slotDen e01 e10 e11) ↔ (e01 = e10) := by
  decide

end Zi
