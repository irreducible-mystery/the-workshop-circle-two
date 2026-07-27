/- S7a DESIGN PROBE part 2 (norm 15) -- measures the FINITE structure
   of the live slots, to decide whether "meets the slice" is a finite
   gauge-fixing computation (decidable, in reach) or needs cohomology
   (out of zero-import reach). Ships nothing. -/

/-- enumerate the admissible (live) 6-index slots over {0,1}^4 with the
    forced x,y,d. For each (a,b,c) in {0,1}^3, x=(a+b)%2, y=(b+c)%2,
    d=(a+b+c)%2 are FORCED -- so the live slots are indexed by (a,b,c):
    exactly 8 of them. This is the whole "shape" of a normalized symbol. -/
def liveSlots : List (Nat × Nat × Nat × Nat × Nat × Nat) :=
  (List.range 2).flatMap (fun a =>
    (List.range 2).flatMap (fun b =>
      (List.range 2).map (fun c =>
        (a, b, c, (a+b+c)%2, (a+b)%2, (b+c)%2))))

/-- COUNT: exactly 8 live slots (nest, norm 9). -/
theorem live_count : liveSlots.length = 8 := by decide

/-- the (1,1,1) slot -- the single FREE one -- is among them. -/
theorem slot_111_live : (1,1,1,1,0,0) ∈ liveSlots := by decide

/-- Which live slots have (a,b,c)=(1,1,1)?  EXACTLY ONE.  So a
    normalized symbol has 1 free value and 7 that normalization pins
    to 1.  A gauge eta : Z2xZ2 -> units has 4 values eta(0,0),
    eta(0,1), eta(1,0), eta(1,1). The question "can 4 gauge d.o.f.
    normalize 7 slots to 1" is a finite linear(-over-units) system. -/
theorem free_slots_count :
    (liveSlots.filter (fun s => s.1 = 1 ∧ s.2.1 = 1 ∧ s.2.2.1 = 1)).length = 1 := by
  decide

/-- The seven slots normalization must send to 1, by (a,b,c): all of
    {0,1}^3 except (1,1,1). Count = 7. -/
theorem pinned_slots_count :
    (liveSlots.filter (fun s => ¬(s.1 = 1 ∧ s.2.1 = 1 ∧ s.2.2.1 = 1))).length = 7 := by
  decide

/- MEASURED FINDING (recorded in the design note):
   - "meets the slice" is a statement about a FINITE object: 8 live
     slots, 1 free, 7 to be pinned, 4 gauge d.o.f.
   - BUT: normalizing the 7 slots is NOT free counting -- it is a
     coboundary condition (the gauge acts multiplicatively via the
     associator index bookkeeping). The map "gauge -> its effect on the
     7 slots" is the 3-coboundary d^2 : C^2 -> C^3 whose IMAGE being all
     of the normalization-target is exactly H^3(Z2,U(1)) = 0 for the
     NORMALIZABLE part. Proving surjectivity of d^2 onto the 7-slot
     target = computing that the relevant cohomology vanishes -- the
     "H^3(Z2)=Z2" sentence the record deliberately withheld.
   - So the HONEST reachable fragment is: state everyClassMeetsSlice
     (done, probe 1, type-checks); prove the FINITE combinatorial
     skeleton (8/1/7/4, done here); and prove the SLOT-LEVEL gauge
     mechanics that Zi.lean already has (detaNum/detaDen at (1,1,1),
     slice_forces_eta_symmetric). The missing middle -- surjectivity of
     the coboundary onto the 7 pinned slots for an ARBITRARY pentagon
     solution -- needs either (i) a full finite case-explosion over the
     unit group of Z[i] (which is {1,i,-1,-i}, FINITE! so this MAY be
     decidable) or (ii) cohomology machinery (out of reach).
   - NEXT PROBE (part 3): test route (i) -- the unit group is finite
     (4 elements), so the whole gauge-fixing MIGHT be `decide`-able if
     we restrict gauges and symbols to unit-valued. That would make a
     GENUINE zero-import proof of a precise (unit-valued) form. -/
