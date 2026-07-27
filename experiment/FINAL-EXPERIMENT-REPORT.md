# THE DUAL-SEAT EXPERIMENT — FINAL CONSOLIDATED REPORT (S1 → S6)

*SuperNinja (meta-auditor, REGISTER row 7) → Kelly, and through her to
the builder and the third body. Norm 16 applies to this whole
directory and to this document: QUARANTINED — everything below rides
on the branch `superninja/dual-seat-experiment-s1` (PR #1 merged the
S1 rehearsal; PR #2 open, carrying S2–S6) and nothing entered `main`
by this seat's hand. Sub-rounds S4–S6 went BEYOND the chartered S1–S3
boundary; the extension was explicitly sanctioned by the courier
(Kelly), and the divergence is recorded in the Lean source headers, in
every commit message, and again here. This is the experiment's closing
artifact: one document, the whole arc, all pins.*

*DIVERGENCE — Round Three, §10 characterization crop (sanctioned by Kelly).
The §10 closing originally distinguished fermion from boson by the fermion's
−1 "annihilating double occupation." That sentence was false: double-
occupation vanishing (ab − ba = 0) follows from commutativity alone and is
common to BOTH statistics (`pauli_double_occupation_dies`); it does not
separate them. The true separator is the symmetrized occupancy — the boson
admits the doubly-occupied state (`control_boson_no_exclusion`: ⟨2,0⟩ ≠ 0),
the fermion excludes it. The sentence was cropped and replaced on Kelly's
explicit sanction (a frozen primary source is not touched otherwise). Finding
raised by the Round-3 stranger pass; scored REGISTER row 8 CONFIRMED; carried
in `CORRECTIONS-LETTER-ROUND3.md` item 1. This is the only content change to
this document since its S6 freeze.*

---

## 1. What was asked, and what was answered

Kelly asked whether this architecture can host the flow Circle One ran
between two Claude seats (Fable 5 as builder, Ultracode as third
body): **charge → prove → extract → blind reimplement → corrections →
repair → re-verify**, with instruments as the authority throughout.
The test article was S1 of Circle Two's live charge (the Z[i] ring
layer), the smallest chartered section. It grew — by results and by
sanction — into six sub-rounds covering the round's entire
mathematical arc, ending on the workshop's own title claim as a single
kernel-checked statement:

```lean
def roomy (f r : Zi) : Prop := pentagon f ∧ hexagon f r ∧ conj r = r

theorem the_roomy_world_has_exactly_two_particles (r : Zi) :
    (∃ f, roomy f r) ↔ (r = one ∨ r = neg one)
```

The answer to the capability question is yes, six times over. The
answer to the epistemics question is more careful, and section 7
prices it honestly.

## 2. The protocol (what "dual-seat" meant, mechanically)

Every sub-round ran the same loop, no step skipped:

1. **Design probe first.** Before any Lean, a Python probe
   (`seatP/probes/`) computed the sub-round's expected structure —
   classifications, nests, forcing sites, ranks — and checked it
   against the bench (`floor/symmetric_statistics.py`) and the
   certificates (G1c–G1g, G3b, G4, G5). No theorem was attempted whose
   content had not first been measured.
2. **Seat P (prover)** appended a section to `seatP/Zi.lean`: zero
   imports, a hand-rolled ring over `structure Zi where re im : Int`,
   Circle One's house style. Pass = **silence**: exit 0 AND zero
   bytes. Then the axiom census (`axioms_zi.sh`, the row-4 pattern):
   every theorem covered, **0 sorryAx, 0 Classical.choice**, or ALARM.
3. **The courier step was a script, not a hand.**
   `courier/extract_statements.py` strips every proof body and ships
   statements + definitions only, sha256-pinned, re-extraction
   byte-identical. Seat B read only that file — never the proofs,
   never the bench.
4. **Seat B (blind verifier)** reimplemented every claim in exact
   Python — polynomial rings with Gaussian-integer coefficients
   (coefficientwise equality, complete over all integers, not
   sampled), exact `Fraction` elimination for ranks, independent
   routes wherever seat P's route was visible in the statement shapes.
5. **Plants, both directions** (norm 16): every instrument, every
   sub-round, was fed a deliberate mutation and had to FAIL (exit 1,
   the poisoned check named), then pass clean on byte-identical
   restore. An alarm that has never fired is not an alarm.
6. **The corrections pass drew blood, loudest first.** Seat B's letter
   each round (`seatB/CORRECTIONS-LETTER*.md`); seat P applied the
   crop; the courier re-extracted; everything re-pinned.
7. **Ship**: report, PIN-TRACKER block, commit, push, PR comment, zip.

Six sub-rounds, six full loops, zero skipped steps.

## 3. The mathematical arc (what was actually proven)

The layer cascade is itself a theorem chain: each layer's forcing
equation is the next layer's hypothesis.

**S1 — the ring** (42 theorems). Z[i] as a commutative ring with
conjugation and norm, from scratch: all ring axioms, conj as an
involutive automorphism, N(z) = z·conj(z), N multiplicative. The
foundation everything else rides on.

**S2 — the domain** (57 cumulative). No zero divisors, by one mod-4
descent: squares mod 4 land in {0, 1}, so a² + b² ≡ 0 (mod 4) forces
both even; fuel-indexed structural induction (order-free, the
chartered fork) gives N(z) = 0 ⟹ z = 0; the chain
z·w = 0 ⟹ N(z)·w = 0 ⟹ w = 0 closes the domain. Mandatory control:
the modulus is load-bearing — mod 2 the argument dies (2 ramifies).

**S3 — pentagon necessity** (84). The bench's pentagon transcribed
instance by instance: 15 of 16 instances are identities in a symbolic
f; the forcing instance at (1,1,1,1) reads f² = 1. Pentagon ⟺ f² = 1;
the factorization (f−1)(f+1) = f² − 1 plus S2's domain gives
**exactly two** solutions on the normalized slice; the gauge layer
(slot invariance, division-free) makes the two classes genuinely
distinct. Charter flag 2 held: slice-plus-invariance wording only —
no statement claims "H³(Z₂) = Z₂". Controls: Z/8 has four square
roots of 1 (the domain is load-bearing); f = i fails with residual
exactly 4.

**S4 — the hexagon layer** (115; first beyond-charter sub-round,
sanctioned). 8 admissible instances of 16; seven are identities; the
forcing site reads f = (f·r)². The reduction identity
f²r² − f = (r² − f) + r²(f² − 1) gives the headline:
**pentagon + hexagon ⟺ R² = F**. The four norm-1 units — completeness
with no search box, from a² + b² = 1 over the certified domain. The
catalog 2×2: r² = 1 ⟺ r = ±1 (boson/fermion), r² = −1 ⟺ r = ±i (the
semions). Flag 4 held: over Z the F = −1 class is EMPTY — the 2×2
count is a Z[i] statement. **The flatland filter as a Galois
statement** (G1e): on units u⁻¹ = conj u, so R = R⁻¹ is literally
conj(R) = R; the fixed points are exactly boson and fermion. The
mirror (G4): conj swaps the semions, acting within the F = −1 fiber.
Chartered Z[i]/5 control landed: (2+i)(2−i) = 5, four roots each of
+1 and −1 mod 5 — split primes break the count.

**S5 — the twist layer** (141). θ as the R-diagonal; the ribbon
identity symbolic, its nest tied 3+1 with the forcing cell exactly
1 = r⁴ — and the hypothesis **discharged by the earlier layers**
(f² = 1 from S3, r² = f from S4 give r⁴ = 1). **Charter flag 3
ADDRESSED**: the Frobenius–Schur convention fork formalized as two
defs named apart — ν_FS = R·θ and ν_ML = R·conj(θ) — agreeing on the
survivors, diverging on the semions (FS −1, ML +1), with the fork
locus characterized exactly as the real locus. The structural
asymmetry proven: ν_ML is the norm in disguise, blind on all norm-1
units; only ν_FS separates. The fork is a theorem, not a footnote.
Spin-statistics seed (G5): θ = R per particle — spin and statistics
are literally the same Gaussian integer in the abelian collapse.

**S6 — the capstone and the exclusion layer** (161). **S6a**: `roomy`
packs pentagon + hexagon + filter into one Prop;
`the_roomy_world_has_exactly_two_particles` stitches
five prior-layer theorems into the title claim — no new axioms of
content, and it says so. Count tied at 2; the ν-rider closes S5's
fork on the capstone set. Controls: the semion passes pentagon AND
hexagon and dies on the filter alone; r = 3 is real but not roomy —
each gate weighed separately. **S6b** (certificate G1f): the −1 has
teeth. Triangular numbers exact (2·T(m) = m(m−1) for all m, by
induction, no Nat-division); the Pauli kill symbolic over Zi
(commutativity is the killer); the m = 2 antisymmetrizer M = I − SWAP
as an exact integer matrix — M² = 2M, tr M = 2, image = the line
(both inclusions, no rank function), kill ⟺ ad = bc, double
occupation dies. Control: **bosons do not exclude** — the symmetrized
double occupation is 2 ≠ 0. Honest label (norm 6): the m = 3..6 ranks
were declared seat B territory up front; seat B's exact elimination
returned [1, 3, 6, 10, 15] = m(m−1)/2 and confirmed the trace
certificate is the general mechanism, not an m = 2 accident.

## 4. The corrections law — the experiment's central dataset

The workshop's law is that first deliveries carry defects and
adjudicators younger than the defect species catch them. Six
sub-rounds produced six confirmations, each a different species:

| round | defect / catch | species | adjudicator |
|---|---|---|---|
| S1 | `sub_eq_add_neg` was the definition restated — a check that cannot fail | norm-7 vacuity | seat B's letter (cross-seat) |
| S2 | six theorems pulled Classical.choice — omega on conjunctive goals | the HANDOFF trap, 3rd author bitten | census ALARM, same run |
| S3 | gauge section could not close — η's unit hypothesis missed in transcription | prose-adjacent transcription | dead-end in-flight, pre-ship |
| S4 | `norm_one_units` pulled Classical.choice — omega on a DISJUNCTIVE goal | the same trap, new disguise | census ALARM, same run |
| S5 | (clean first census — the discipline held) | — | crop: route-vs-statement hypothesis note |
| S6 | (clean first census, second in a row) | — | crop: generic-anti-symmetry label note |

**The omega-trap saga deserves its own sentence.** The trap —
`omega` silently pulling `Classical.choice` when handed compound
goals — bit twice in Circle One's record (HANDOFF.md), then bit this
seat in S2 (conjunctive, ×6) and again in S4 (disjunctive, ×1: the
same species one disguise over). The census caught it live all four
times across three authors. By S5 the lesson had moved from repair
practice to design practice — `refine ⟨?_, ?_⟩` and `by_cases` before
omega, always — and the last two sub-rounds censused clean on first
run. That is what an instrument is for: the defect was younger than
its adjudicator every time, so it died on schedule, every time.

The crop across six letters: 1 norm-7 conviction (repaired), 1
Nat-subtraction hazard labeled (S4: the mod-5 encoding's range guard
was load-bearing and invisible), 2 stronger-than-certificate labels,
1 orphaned-theorem role label, 1 missing Gaussian witness added, 2
route-vs-statement notes, and 4 positive independence findings. Every
item applied or adjudicated; none ignored.

## 5. Seat B's independence — the routes, round by round

The blind seat never re-proved seat P's route when a different one
existed:

- **S1**: exact reimplementation, polynomial coefficients over Z,
  47/47.
- **S2**: the descent re-derived by TWO routes seat P didn't take
  (Int-order argument; norm multiplicativity), 24/24.
- **S3**: the classification re-derived in Z[i][fr, fi]
  coefficientwise; the root count by norm-census, not factorization,
  32/32.
- **S4**: four commuting indeterminates Z[i][fr, fi, rr, ri]; root
  censuses by the complete norm box, independent of the factorization
  route, 36/36.
- **S5**: the fork locus by expanding the DIFFERENCE
  ν_FS − ν_ML = −2ri² + 2·rr·ri·i coefficientwise — not seat P's
  cancellation route, 25/25.
- **S6**: the capstone by **direct exhaustion** — box completeness
  derived from the norm forcing equations, every pentagon instance
  (16) and admissible hexagon instance (8) actually run on all 16
  unit pairs, not cited. Five stitched theorems vs one brute
  exhaustion: the same two-element set. Plus the exclusion census
  completed exactly for m = 2..6 by fraction-free elimination, 23/23.

**187 blind checks total, all passing, every instrument plant-bitten
in both directions, every sub-round** — each verifier fed a deliberate
mutation (exit 1, the poisoned check named) then restored
byte-identical to a clean run, plus the S1 census plant (a planted
`sorry`, bitten and restored) that first proved the census's teeth.

## 6. The final artifact, by the numbers

- **`seatP/Zi.lean`**: 161 theorems, zero imports, one file, compiles
  silent (exit 0, zero bytes) on pinned `leanprover/lean4:v4.32.0`.
  Census: 161/161 covered, **0 sorryAx, 0 Classical.choice**, PASS.
  Growth: 42 → 57 → 84 → 115 → 141 → 161.
- **Statements**: v7, 161 statements, mechanical extraction,
  re-extraction byte-identical.
- **Blind verification**: 6 verifiers, 187/187 checks, exit 0
  throughout.
- All five charter flags held or formally addressed: flag 2
  (slice-plus-invariance wording, S3), flag 3 (the FS fork named
  apart as theorems, S5), flag 4 (no integer semion, S4), flag 5
  (both hexagons imposed here, claimed of no one else, S4), and the
  descent fork stated order-free (S2).

## 7. The epistemic finding — priced honestly, unchanged from S1

The finding from the first report survives six-fold repetition and is
worth restating rather than inflating:

- **Instruments' authority: undiminished.** Exit codes, axiom
  censuses, and coefficient equality do not care who runs them. The
  two-body *mechanical* structure — kernel + exact blind
  reimplementation — survived intact through 161 theorems and 187
  checks, and caught real defects of exactly the species the norms
  predict.
- **Prose adjudication: weakened, labeled.** The blindness was
  procedural (proof bodies stripped by script; seats in separate
  working modes), not architectural — one substrate wrote both sides.
  A characterization slip shared by both seats would pass both. The
  S3 gauge dead-end is the honest specimen: prose-adjacent structure
  (what a certificate *means* by "units") is where this mode works
  hardest and guarantees least.
- **What six rounds added to the S1 finding**: the corrections law is
  not an S1 fluke — it fired in a different species every round it
  had material, and the two clean censuses at the end are themselves
  data (the trap's lesson transferred from adjudication into design).
  And the S6 independence result — stitching vs exhaustion agreeing
  on the two-element set — is the strongest cross-seat agreement the
  protocol produced.
- **The standing proposal from the S1 report remains open** for the
  seats of record: a register row for *single-architecture dual-seat
  deliverables*, adjudicated by both seats' instruments PLUS one
  true-stranger pass before anything is called verified. This
  experiment feeds that pass; it does not replace it.

## 8. What this branch does NOT do

Unchanged from round one, restated at close: it does not touch `main`
or the third body's branch; it does not claim any section of the round
for the record (the third body's charge stands — this is a rehearsal
on the same target, available as an independent cross-check if the
seats of record want it); it does not co-sign anything into the
two-body record. S4–S6 exist because Kelly sanctioned the extension;
the divergence from chartered boundaries is recorded in the source, in
the commits, and in this paragraph.

## 9. The consolidated pin table (ship-state pins only)

Full 64-char hashes live in each SUBROUNDn-REPORT.md; PIN-TRACKER.md
is the grep-able one-pager. Ship-state, newest first:

| round | Zi.lean | statements | verifier | zip | commit |
|---|---|---|---|---|---|
| S6 | `b7ef35425e13` (161 thm) | v7 `97faef58cd0e` | s6 `64bdc767c785` (23/23) | `2c94275e84fc` | `26c7b2e` |
| S5 | `e505e5192b51` (141) | v6 `1071e8541e39` | s5 `24f50d913640` (25/25) | `d5b68c7d1ff4` | `90a2f0a` |
| S4 | `6d51cafa7bd4` (115) | v5 `d195b3de0ead` | s4 `acfa68424e8b` (36/36) | `3d8cc366250f` | `b98fcdb` |
| S3 | `49e850e1f043` (84) | v4 `1314192cf5ee` | s3 `feac6e838ed1` (32/32) | `e353a5af9bdf` | `e20f31a` |
| S2 | `fbe854890a5e` (57) | v3 `69d7073e9e92` | s2 `bc10622bce65` (24/24) | — | `c045e6e` |
| S1 | `5930c54ab93a` (42) | v2 `12ea1133…` | s1 `8eb939be4241` (47/47) | — | PR #1 |

## 10. Closing

Six sub-rounds ago the question was whether one architecture could
hold two chairs apart well enough for the instruments to keep their
authority. The instruments answered: a vacuous theorem died in S1, a
choice-tainted proof died in S2 and again in S4, a transcription gap
died in S3 before it could ship, and by S5 the discipline they taught
had moved upstream into the writing itself. The mathematics answered
too: the ring, the domain, the pentagon, the hexagon, the twist, and
then the two of them together — the roomy world has exactly two
particles, said once, kernel-checked, and re-derived blind by a route
that shares nothing with the proof. And what separates the fermion from
the boson is not that either one "annihilates double occupation" — that
vanishing (ab − ba = 0) is commutativity, common to both — but the
symmetrized occupancy: the boson admits the doubly-occupied state
(⟨2,0⟩ ≠ 0) and the fermion excludes it. [§10 sentence cropped and
corrected on Kelly's sanction, Round 3; see header divergence note and
CORRECTIONS-LETTER-ROUND3.md item 1.]

The middle holds. The catalog is two. The record is pinned.

*— SuperNinja, dual-seat experiment closing report, quarantined per
norm 16, beyond-charge sub-rounds by sanction, all divergence
recorded*
