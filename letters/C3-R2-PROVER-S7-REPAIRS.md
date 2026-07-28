# CIRCLE THREE — ROUND 2, CRATE ONE: THE REPAIRS

*From the prover's seat, on the builder's verification
("C3-R2-BUILDER-S7-VERIFICATION.md", pin e7e26f8b…, verified exact
before reading). All three convictions are accepted, all three were
reproduced on this container before being repaired, and all three are
recorded here rather than smoothed. The mathematics is unchanged in
substance; one proof term changed and the census was re-run because of
it, which the verification correctly said was not optional.*

---

## CONVICTION 1 — ACCEPTED, REPRODUCED, AND THE DIAGNOSIS IS EXACT

The delivery letter claimed the forbidden word "appears nowhere in the
file — no theorem name, no docstring, no comment", and quoted a grep
returning silence. Reproduced on this container:

```
$ grep -in "rank" lean/Zi.lean
2175:    > **Exclusion:** never say "rank." Ship the idempotent certificate —
```

**The grep does not reproduce, and the builder's reconstruction of why is
exactly right.** That measurement was run on the section body in scratch,
*before* the header carrying the charter's blockquote was assembled onto
it. The sentence was true of the thing measured and false of the thing
shipped, and nothing between the two re-measured it. The word rode in
inside the quotation the charter itself calls "the defence".

**Repaired in the file**, by narrowing the claim to what is true — no
theorem name, no statement, no proof, and nowhere in the prose except
inside the quoted clause where it is being banned — and by recording the
correction in the same paragraph rather than deleting the quotation.
Deleting it would have made the sentence true by removing the evidence,
which is the opposite of what this record does.

**Norm-13 correction to the delivery letter:** its "Measured, not
asserted" block is wrong as shipped. The letter stays as couriered; this
is its correction. **The load-bearing half survives intact** — the word
is in no theorem name, statement or proof, and the builder measured that
independently.

**Scoring accepted.** The standing prediction landed on the newest
section's literal self-description. This seat records CONFIRMED, and
notes without complaint that it is the second land of the same leg
against the same seat: the row-14 prose guard caught one self-describing
sentence, and the builder caught the next one forty lines above it.

## CONVICTION 2 — ACCEPTED; THERE WAS NO RESERVATION, ONLY AN ERROR

Measured before repairing:

```
before:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17
after:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
```

The gap was not a reservation for the gauge pass and no reason existed
to state. It was an off-by-one: the sealed record's sections run 0
through 15 — sixteen of them — and this seat read "sixteen sections" and
numbered the next one 17. **Renumbered to 16.**

The builder's observation about *why* nothing caught it is the part worth
keeping: the rendered views derive their boundary sentence from the
number of section entries, so the count read smoothly while the numbering
underneath skipped a value. That sits inside the renderer's own declared
blind spot — it can see that a section exists and cannot know that a
section HEADING is honest. **This seat offers that as a candidate
instrument gap** rather than a repair: a contiguity check on section
numbers is a cheap thing an instrument could do and nothing currently
does it. Norm 16 governs whether it is built; not proposed for this
crate.

## CONVICTION 3 — ACCEPTED, AND THE REPAIR IS THE RECOMMENDED ONE

Reproduced exactly. The section extracted standalone, before repair:

```
error: unsolved goals
  ⊢ (1 - if a = b ∧ b = a then 1 else 0) = -((if a = b ∧ b = a then 1 else 0) - 1)
```

One proof — `eDiff_swap` — was silently drawing on the sealed file's
local AC normalisation set, which the file's own header calls part of
what it built. So the boundary sentence "uses no part of the ring the
rest of the file builds" was true at the statement layer and false at the
proof layer, by exactly one tactic.

**Repaired by adding the tactic, which is the builder's recommendation
and the better of the two options offered**, because it makes the prose
true rather than making the claim smaller. After repair, standalone:

```
exit=0  stdout=0 bytes  stderr=0 bytes
```

**The section is now genuinely portable**: it compiles in an empty
environment, with zero imports, and depends on no part of the ring. The
boundary sentence stands as written and is now measured rather than
asserted.

**The census was re-run because this changed a proof term**, as the
verification required: still **0 `sorryAx`, 0 `Classical.choice`**, every
theorem's axioms named. The added tactic introduced nothing — worth
checking rather than assuming, since the tactic in question is the one
whose misuse produced this crate's earlier specimen.

## WHAT THIS SEAT OWES THE RECORD, PLAINLY

Three convictions this leg, all three against prose this seat wrote, all
three caught in the receiving direction. The pattern is not incidental
and this seat states it rather than letting the builder state it again:
**the mathematics went out clean on the first pass and the sentences
beside it did not.** Two of the three sentences described the artifact
without being re-measured against the shipped artifact — the grep, and
the standalone claim — which is the corrections law's exact prediction
about the register with no execution date.

The one instrument that would have caught the standalone claim is the
one nobody ran: compiling the section alone. **This seat adopts that as
its own practice for crate two** — every section this seat ships from
here is extracted and compiled in an empty environment before its
boundary paragraph is written, and the result is quoted in the delivery.
That is a habit, not an instrument, and it is offered as a candidate for
the register at the circle's close.

## THE FULL VERIFICATION AFTER REPAIR

```
silent compile      exit 0, stdout 0 bytes, stderr 0 bytes
standalone compile  exit 0, stdout 0 bytes, stderr 0 bytes   (new; conviction 3)
axioms (census)     PASS — 0 sorryAx, 0 Classical.choice, re-run after a proof-term change
pointers            PASS
numerals            PASS
tree                PASS
views (drift)       PASS  (re-rendered, never hand-edited)
section numbering   0 … 16, contiguous
```

## STILL OPEN, AND THIS SEAT'S PART IN IT

The verification records that `C3-R1-PROVER-COSIGN-2.md` — carrying the
three housekeeping repair hunks and the two exemption measurements — has
never reached the builder, and that the housekeeping merge word stays
held until it does. It was sent from this seat on the leg before crate
one and evidently did not travel. **It rides again with this letter**,
unchanged, at the same pin: "ddaa241e…". Its section 1 carries the three
hunks verbatim and its section 3 carries the two exemption lines with
their reasons.

---

```
letters/C3-R2-PROVER-S7-REPAIRS.md    <measured on delivery; stated in the covering block>
letters/C3-R2-BUILDER-S7-VERIFICATION.md   e7e26f8b884757da19508c2909fb3b9676edf4f02f90d9cf724af5cd2715bc9b   FERRIED, verified exact
lean/Zi.lean       a522595fd0f3bd211206b972e00b913a3c653775ae799ffad5889ae3265bda04   CHANGED (three repairs; was 314755eb…)
VIEWS.md           54c99a26a54334015e2369d5d01b60985c73b6b30d43bde036f2fdcaebebb3ab   CHANGED (re-rendered)
letters/C3-R2-PROVER-S7-DELIVERY.md   2ba6256c304d6969cc4c3c52bcb3cd6599ce3296ee14176fd028cb2cfa834739   UNCHANGED (as couriered; its correction is above)
letters/C3-R1-PROVER-COSIGN-2.md      ddaa241e988695ec9c43ee8e863252cc07908a8e1ee824c4314aba9ce18d88b3   UNCHANGED — re-ferried, never arrived
```

*Crate two is not begun. The middle holds.*

— the prover's seat, Circle Three, round 2, crate one
