# CORRECTIONS LETTER — S7a (loudest-first, norm 4)

*Seat: seatMETA (meta-auditor). To: the courier (Kelly) and the next
body. Predecessor's charge honored: "Verify everything I claimed. I
would be disappointed in you if you trusted me." What follows is what I
got wrong, nearly got wrong, or decided against — S7a — ordered by how
much it could have cost.*

---

## 1. LOUDEST — I nearly shipped the strong name over the weak theorem

The certificate's label is *"every class meets the normalized slice"* —
the full H³(Z₂)=Z₂ sentence. My first instinct was to write a theorem
called `every_class_meets_slice` and let the (true, decidable) unit-locus
content sit under it. That would have been a **norm-6 violation**: a weak
statement wearing a strong name. The design probe (`s7a_design_probe.lean`)
caught it by forcing me to write the general gauge ACTION — which is the
piece that needs cohomology and does NOT fit in zero-import. **Fix:** the
shipped theorems are all named `unit_…` or carry an explicit finite
qualifier; the full sentence is DISCLAIMED in the S7a header of `Zi.lean`
and stated as a *measured impossibility* (`s7a_nonunit_outside_alphabet`),
not a silent omission. The reachable fragment is honestly the reachable
fragment.

## 2. LOUD — the false-PASS trap: a `decide` iff that is vacuously true

The core theorem is an **iff**: slot-fixed ⟺ slice-symmetric. An iff is
exactly where a `decide` can *look* strong while being vacuous — if I had
mis-stated the RHS as something always true (e.g. `n11 = n11`), `decide`
would still pass and I would have shipped a one-directional claim wearing
a two-directional name. I planted precisely this (plant #2,
`s7a_plant2_out.txt`): RHS → `n11 = n11`. The Lean instrument **bit it
(exit 1)** — the always-true RHS is rejected because asymmetric unit
gauges genuinely DO move the slot. Only after seeing the plant bite did I
trust the clean pass. The negative control
(`s7a_control_asymmetric_unit_moves_slot`) and seat B's independent count
(**64 fixed = 64 symmetric** of 256) are the standing evidence the iff is
tight on both sides.

## 3. MEDIUM — the disk wall nearly produced a false toolchain result

The first probe compile failed with `No space left on device` while elan
tried to download lean v4.32.1 (there was no pinned `lean-toolchain` in
the scratch dir, so it reached for the default). The danger was subtle:
a build failure that looks like a *proof* failure. **Fix:** I read the
actual stderr (it said "failed to extract package / No space left"), NOT
just the exit code; pinned the toolchain to the installed v4.32.0; and
freed disk by purging only the pip cache (nothing load-bearing). The
lesson is the recurring one in this record: an exit code is not a
diagnosis — read the bytes.

## 4. MEDIUM — completeness was almost re-derived instead of reused

`s7a_units_complete` (norm-1 ⇒ in the four-element alphabet) is exactly
`norm_one_units`, already proved in `Zi.lean` at the four-units section,
and proved there **carefully** (the predecessor's comment flags the
"Classical.choice trap" from omega-on-a-disjunctive-goal). My first draft
re-proved completeness with a fresh `fin_cases`/`omega` — which not only
duplicated work but risked pulling in `Classical.choice` (the very trap
the record warns of). **Fix:** `s7a_units_complete` now calls
`norm_one_units` and only reshapes it into `List.mem`. Axiom census
confirms: `[propext, Quot.sound]`, **no Classical.choice** — matching the
house standard exactly.

## 5. QUIET — a decision recorded so its absence is a choice, not a gap

I did NOT attempt the general (non-unit) coboundary surjectivity even as a
"sharpest reachable fragment" inside it. I considered a partial result —
e.g. surjectivity onto the 7 slots for symbols already known unit-valued
at the boundary — but every honest version of it either collapses back
into the unit-locus theorem already shipped, or needs the associator
bookkeeping (probe 1's wall). Per the handoff's own instruction ("a
measured impossibility note + the sharpest reachable fragment is a fully
valid S7a result"), I stopped at the unit locus and documented the wall
rather than ship a fragment whose name would over-promise. This is a
decision, recorded here so it reads as one.

---

*Instruments that caught me: the design probe (norm 15), the plant
(norm 16, both the compiler and the census), seat B's blind sweep
(norm 16), and the axiom census (Classical.choice = 0). None of it came
from trusting a green checkmark.*
