# STRANGER-AUDIT-ROUND3 — the true-stranger pass the record was waiting for

*SuperNinja instance 2 (meta-auditor, REGISTER row 7, fresh, set to max)
→ Kelly, and through her to the builder and the third body. Quarantined per
norm 16, like everything in `experiment/`. This is the document the Round Two
retrospective said it owed the record: a reader who did not write the 161
proofs, has no memory of the six letters, and read the statements cold before
the prose. Every claim here entered as a claim-to-verify; the measurements are
mine, this session, on the shipped artifacts.*

---

## 0. What I checked, and in what order (the order is the evidence)

The reading order was the experimental instrument. I honored it and I can
attest to it:

1. **Phase 0 — inheritance, mechanically, before any prose.** Pins, kernel,
   census, courier re-extraction, six verifiers, and a norm-16 plant/restore
   on the S6 verifier. All measured PASS (§1).
2. **Phase 1.1 — statements only.** I read `courier/Zi_statements_v7.txt` end
   to end and wrote `STRANGER-PHASE1-STATEMENTS-FINDINGS.md` — eight findings
   and four falsifiable predictions — and delivered it to Kelly **before
   unsealing one line of the prose record.** That document is timestamped
   ahead of every report I had not yet opened. This is the load-bearing fact:
   the predictions below were committed in writing while the prose was sealed.
3. **Phase 1.2 — my own verifier.** I wrote `seatMETA/verify_stranger.py` from
   scratch — Gaussian integers reimplemented as Python tuples, no import of
   Zi.lean's defs, no reading of the six seat-B verifiers first — covering the
   12 claim families I judged most load-bearing, with negative controls and a
   built-in norm-16 self-test (§2).
4. **Phase 1.3 — the prose, unsealed in the handoff's order**, then the canon
   (REGISTER, ROUND1, README), then the bench and certificate run live (§3–§5).
5. **This document** (§6 is the verdict on the owed caveat).

I did not touch GitHub. Section 8 of the handoff remains sealed.

---

## 1. Phase 0 — inheritance verification (all PASS)

| step | measured | verdict |
|---|---|---|
| pins (full 64-char) | `Zi.lean` = `b7ef35425e13…dba5e`; `Zi_statements_v7.txt` = `97faef58cd0e…ca0a27`; `verify_zi_s6.py` = `64bdc767c785…6bce0b` | **match claims** |
| kernel (norm 10) | clean re-run `exit=0 bytes=0` | PASS |
| census | 161 thm / 161 census lines / 0 sorryAx / 0 Classical.choice / RESULT PASS (68 axiom-free) | PASS |
| courier | re-extract 161 thm → `diff` BYTE-IDENTICAL; sha = `97faef58cd0e…` | PASS |
| verifiers | `verify_zi{,_s2..s6}.py` all exit 0 | PASS |
| norm 16 (S6) | plant `len(roomy_pairs)==2 → ==3`: exit 1, names `FAIL the_roomy_world_has_exactly_two_particles`, 22/23; byte-identical restore: exit 0, 23/23 | PASS both directions |

**Every claim in HANDOFF §1 measured true.** The predecessor asked me to be
disappointed in myself if I trusted it; I did not, and it held anyway.

---

## 2. Phase 1.2 — my independent verifier (and the three bugs it caught in me)

`seatMETA/verify_stranger.py` (pin `cf603918357d…`): **27/27 PASS, exit 0** on
the clean run; `--plant` (a "three particles" injection) → exit 1 naming
`PLANTED_headline`. Both directions on record. Every load-bearing claim
re-derived by a route of my own choosing (brute enumeration over the Z₂ index
cube for pentagon/hexagon/nests; from-scratch Gaussian arithmetic over
[-5,5]² boxes for ring/domain/units; an explicit 4×4 integer matrix with exact
`Fraction` rank for the antisymmetrizer).

**The honest part.** My *first* run failed 3 checks — and all three were **my
verifier's bugs, not the record's:** (a) a duplicated candidate in my
`roomy_pairs` list (I listed `(-1,0)` twice, so a correct 2-element set printed
as 3 with a dup); (b) float error in my rank routine (fixed with `Fraction`);
and (c) — the instructive one — **I had asserted the m=2 antisymmetrizer has
rank 2. It has rank 1.** M = I − SWAP at m=2 is
`[[0,0,0,0],[0,1,-1,0],[0,-1,1,0],[0,0,0,0]]`; M²=2M, tr=2 ⇒ one eigenvalue 2 ⇒
**rank 1** (one antisymmetric mode, one Slater determinant). The record never
claimed rank 2 — the S6 report says "image = the line … no rank function," and
seat B's census reports `[1,3,6,10,15]` = m(m−1)/2, i.e. **1** at m=2. My guess
was wrong; the record was right. This is exactly why a stranger writes their
own instrument: the bug you catch is your own before it can masquerade as a
finding about someone else's work.

After correcting *my* tool: **26/26 substantive claims re-derived, controls
behave as negatives, F3 and F6 measured directly.**

---

## 3. Findings, reconciled against the prose

My eight statements-only findings (F1–F8), each now adjudicated against what
the reports and letters actually say:

**F1 — the courier silently truncates inline-`let` statements to vacuity.
STANDS, and it is new.** `extract_statements.py` cuts every theorem at the
first `:=`. Three declarations put a `let … :=` binding *inside the statement
type* — `live_gauge_witness` (Zi.lean L850), `control_gauge_moves_slot`
(L862), and `def twist` (L1339). The courier emitted only the fragment up to
`let eta` / the def head; **the actual proposition was dropped.** The kernel
checked the real, substantive theorems (I read those three source lines to
confirm), so the *mathematics* is sound. But seat B, reading statements-only,
was handed a vacuous fragment for two of them — its blind review of
`live_gauge_witness` and `control_gauge_moves_slot` inspected essentially
nothing. **No report, letter, or retrospective mentions this.** It passes
every instrument: the kernel is silent, the census counts the real theorems,
and "re-extraction byte-identical" is true *of the lossy output*. This is a
genuine instrument defect in the courier, invisible to all six sub-rounds.

**F2 — a seat-P block comment leaked into the statements file. STANDS.**
Lines ~400–416 of `Zi_statements_v7.txt` carry S5 report prose ("Design probe:
… NESTS (norm 9): …") — a `/- … -/` section header the extractor failed to
strip. The guarantee "seat B sees definitions and claims only" is violated:
seat B also saw a chunk of seat-P-authored design prose. Small, but it is a
blindness leak, and like F1 it is unmentioned anywhere in the record.

**F3 — commutator "Pauli" lines are true for all inputs by commutativity.
PARTIALLY PRE-CAUGHT; one residual crack.** I flagged `pauli_kill_symbolic`,
`pauli_double_occupation_dies`, and two conjuncts of `M2_image_on_line`. The
record does better than I expected on the last: **S6 corrections letter item
#1 independently caught the exact same species** — "the third conjunct … is an
instance of the GENERAL anti-symmetry x−y=−(y−x), true in any ring … does not
use the tensor structure," and a docstring label was added. And the S6 report
says plainly "**commutativity is the killer.**" So this is *not* a shared blind
spot for `M2_image_on_line`. **The residual crack:** the two theorems whose
*names* carry the physics — `pauli_kill_symbolic`, `pauli_double_occupation_dies`
— never received a label saying "as an *exclusion* statement this is content-
free; the exclusion content lives in `Mmat`/`M2_*`." The prose is honest that
commutativity is the mechanism; the *naming* still imports Pauli exclusion onto
a commutative-ring triviality. It is the mildest possible version of the row-8
species, and it survived six rounds unlabeled.

**F4 — `dimension_charpoly_factors` is x²−1=(x−1)(x+1), model-supplied edge.
CONFIRMED and LABELED.** The S5 report ties it to G5 (fusion matrix N²=I, D²=2)
and the S5 letter item #2 records that `fusion_matrix_squares_to_identity` "is
Nat arithmetic in disguise — the matrix is never an object." So the "dimension
/ char-poly" reading is openly acknowledged to live in the model/citation, not
the kernel statement. This is "every noun resolving, the edge supplied by the
model" — labeled, not slipped. (My prediction P-D.)

**F5 — trivial arithmetic tails on `*_nest_*`. RESOLVED, honest convention.**
The `(2+2)=4`-style conjuncts are the workshop's declared count-theorem
convention (S4 letter #2, S5 letter #2 both record it): the count theorem ties
the arithmetic, a partner theorem supplies the content. I independently re-ran
the real enumerations — `pent_classification_counted` (11+4+1=16),
`hex_nest_8_of_16`, `census_nest_m2` — and every count equals a genuinely
enumerated cardinality. Norm 9 holds.

**F6 — the headline is exactly-two *given the reality filter*. This is the
crux; see §4.**

**F7 — negative controls present per family. CONFIRMED both sides.** Every
family carries a `control_*`; I verified they behave as true negatives (semion
passes pentagon+hexagon and dies on the filter alone; boson does not exclude;
f=i fails pentagon; fake mirror non-multiplicative). The chartering
certificate's own negatives (G1a, G1e, G2, G3b, G4) also all PASS as genuine
negatives. Norm 5 holds.

**F8 — `descent_core` fuel dressing. RESOLVED.** Structural-recursion shape;
the unconditional content is `normSq_eq_zero_iff`, which is present. Seat B
(S2 letter #2) already recorded the anti-vacuity count is exactly 1. Fine.

---

## 4. The headline, and whether it slips (F6 / P-A)

The kernel statement is honest and I re-derived it independently:
`the_roomy_world_has_exactly_two_particles (r) : (∃ f, roomy f r) ↔ (r=one ∨
r=neg one)`, with `roomy f r := pentagon f ∧ hexagon f r ∧ conj r = r`. The
third conjunct **is** the reality filter / normalized slice. I measured that
the filter is load-bearing: without `conj r = r`, my enumeration finds **four**
pentagon-and-hexagon pairs (the semions survive); with it, exactly two. So the
theorem earns "exactly two" only *on the slice*.

**Where the prose keeps the qualifier (accurate):**
- S3 report: "exactly two … **on the normalized slice**"; "No statement …
  says 'H³(Z₂)=Z₂' or 'every class meets the slice' — that lemma is not proven
  and not bench-certified."
- ROUND1.md charge: "State the headline in **slice-plus-invariance form** …
  Do not write 'H³(Z₂)=Z₂' above a proof that does not contain the missing
  lemma."
- REGISTER row 2: the G1c slice lemma is explicitly "flagged inside the
  instrument as NOT bench-certified."
These are careful and correct.

**Where the front door does not (the row-8 specimen):**
- `workshop-canon/README.md`: "**the roomy world has exactly two particles —
  boson and fermion — the Z₂ catalog complete over Z[i], with the semions
  dying on the flatland filter.**"

This front-door sentence states "exactly two particles" **without** the on-the-
slice qualifier attached to the claim itself. It is not *false* — it
immediately supplies the mechanism ("semions dying on the flatland filter"), so
every noun resolves and a careful reader reconstructs the slice caveat from the
clause. But the unqualified headline is doing work the kernel theorem does not
do unaided: "the catalog complete over Z[i]" reads as *full-stop* completeness,
while the theorem is completeness *modulo the reality filter*. **This is the
REGISTER's row-8 prediction landing almost verbatim: "a characterization slip
in the settlement/register prose, every noun resolving, the edge supplied by
the model."** The edge — that "complete" is slice-relative — is supplied by the
model of the mathematics, not by the front-door sentence.

I want to be precise about weight: this is a **front-door / settlement-prose**
slip (class 8, the *declared unadjudicated* frontier), not a defect in any
kernel statement, any report's technical section, or any verifier. It is
exactly the class the row-8 gates were promised to catch and have not yet been
ported to catch. Its severity is low and its location is the one the REGISTER
predicted. That is the finding, and it is a *scored* prediction, not a
disaster.

**Empirical anchor / my negative control for this audit.** The one concrete
falsifiable number in the settlement prose — ROUND1.md crop #1's claim that the
hexagon minimum residual is "the integer 4" — I tested against the live bench:
measured `worst = 3.9999…6 = 4` exactly, at (+1,+1). The prose's labeled
"provenance conjecture" (that 0.527864… is the fractional part of the (−1,−1)
candidate's 5.527864…) also checks out: I measured that candidate at 5.527864.
So where the settlement prose makes a *checkable* characterization claim, it is
accurate. The slip in the previous paragraph is about an *unqualified* claim,
not an inaccurate one — which is precisely why it is row-8 (prose framing) and
not row-1/2/3 (a wrong instrument value).

---

## 5. The bench and certificate, run live

- Floor: `run_all.py` → **29/29** (after installing numpy/scipy; the floor is
  pure Circle-One-inherited except crop #1). "It held."
- Certificate: **68/70 PASS.** The 2 failures are exactly
  `G6_calibrators_remeasured_anyon` and `G6_calibrator_remeasured_coker`, both
  `FileNotFoundError` — they require a Circle One Lean tree via `C1_LEAN`, which
  is absent here (GitHub sealed, crate not in the zip). REGISTER row 2 and
  ROUND1.md both document that "the G6 calibrators need a Circle One tree; all
  other checks run without it." **These 2 are the documented, expected
  consequence of a missing optional dependency, not defects.** All negative
  controls in the certificate pass as genuine negatives.

---

## 6. The verdict on the owed caveat — did the shared blind spot exist?

The retrospective's §5 owed the record this: every Round-Two catch was
mechanical or statement-adjacent; **zero characterization slips were caught;**
and "zero caught is compatible with zero committed — and equally with a shared
blind spot. The record holds both readings until a true stranger reads the
prose." I am that stranger. My verdict, in three parts:

**(1) On characterization slips in the prose: a shared blind spot DID exist,
and it is small, and it is exactly where the REGISTER predicted.** The
front-door README states the two-particle headline without its slice qualifier
(§4). Both seats — one substrate — wrote and reviewed the technical prose
carefully enough to keep the qualifier *in the reports and the charge*, and
both let the *front door* drop it. That is the shared-blind-spot reading made
concrete: a slip that is invisible to the kernel, the census, the courier
(it is not even in `experiment/`), and to seat B (who never reads the front
door). It required a reader positioned outside the whole apparatus. **So the
answer to "zero committed vs shared blind spot" is: not zero committed. A
shared blind spot existed, and it produced precisely the row-8 species.**

**(2) On the instruments: a second, unpredicted shared blind spot exists in the
courier itself.** F1 (inline-`let` statements truncated to vacuity) and F2 (a
block comment leaked) are defects in the *blindness mechanism*, not the
mathematics. They are more interesting than the prose slip because they are
mechanical yet unseen: they passed the census, passed "re-extraction
byte-identical," and were never noted in six sub-rounds. They partially
*undercut* the retrospective's cleanest claim — that seat B independently
reviewed every statement — because for `live_gauge_witness` and
`control_gauge_moves_slot` seat B reviewed a vacuum. This is the sharpest thing
a stranger found, and it is a shared blind spot of a kind the retrospective did
not anticipate: not a characterization slip, but a *silent lossy instrument*
that both seats trusted.

**(3) On the mathematics: I found no defect.** Every load-bearing theorem
re-derived by my independent routes. The capstone is honest (exactly-two on the
slice, filter provably load-bearing). The exclusion story is honest
(commutativity is named as the mechanism; the m=2 antisymmetrizer is rank 1,
one Slater mode, and the record says so; m≥3 was declared seat-B territory in
advance). The one residual naming crack (F3: `pauli_*` named for exclusion
while being commutative-ring trivialities) is the mildest row-8 instance and
sits *inside* the honest-labeled S6 layer.

**Score for the REGISTER's row-8 standing prediction —
"a characterization slip in the settlement or register prose, every noun
resolving, the edge supplied by the model":** **CONFIRMED.** The README
front-door headline is the slip; every noun resolves; the edge (that
"complete" is slice-relative) is supplied by the model. The prediction was
correct. Round Two did not catch it because the prose gates for row 8 were
never ported (they are the S7c charge) and no true stranger had read the
front door — the two conditions the record itself named.

The middle holds. It holds *on the slice*, and now the front door should say
so too.

*— SuperNinja instance 2, meta-auditor, Round Three stranger audit;
quarantined per norm 16; every measurement this session, on the shipped
artifacts; GitHub sealed*
