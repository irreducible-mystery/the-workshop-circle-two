# CONVERGENCE REPORT — two independent S1 formalizations, compared

*SuperNinja (meta-auditor, REGISTER row 7) → Kelly, and through her to
both bodies. Quarantined per norm 16 as always. Two lineages have now
formalized the same charge (ROUND1.md §S1, the Z[i] ring layer)
independently: the **two-body lineage** (Fable 5 builder + Opus/Code
third body, the seats of record) and the **dual-seat lineage** (this
experiment, sealed before their artifacts arrived — my S1 shipped
2026-07-25, PR #1; their S1 arrived 2026-07-26). Neither lineage saw
the other's Lean before shipping its own. This report compares them:
mechanical first, statements second, process last. Design note with
predictions recorded before measurement: `DESIGN-NOTE.md`.*

## 0. The artifacts

| | two-body S1 | dual-seat S1 |
|---|---|---|
| file | `lean/Zi.lean`, pin `2e227702…` | `experiment/seatP/Zi.lean` S1 section, pin at S1-ship `5930c54a…` |
| carrier | `structure GZ`, namespace `Zi` | `structure Zi`, namespace `Zi` |
| theorems | 54 | 42 |
| lines | 350 | 281 |
| defs | 11 | 10 |
| toolchain | v4.32.0, commit `8c9756b2…` | identical |

Their artifact reached me three ways, all agreeing: Kelly's uploaded
file, the crate zip (`circletwos1.zip` → `lean/Zi.lean`), and the
GitHub branch `claude/courier-circle-two-dulbsg` raw file — all three
measure `2e227702…`. Norm 12 satisfied at the source.

## 1. Phase A — their artifact on my instruments (all claims verified)

Every number their delivery letter claims, re-measured independently
on this container:

| their claim | my measurement | verdict |
|---|---|---|
| compile exit 0, 0 bytes | **exit 0, 0 bytes**, 0.77s | CONFIRMED |
| 54 theorems | 54 (my census AND a modifier-tolerant harvest both) | CONFIRMED |
| 16 axiom-free | **16** | CONFIRMED |
| 36 propext-only | **36** | CONFIRMED |
| 2 propext + Quot.sound (`brahmagupta_fibonacci`, `norm_mul`) | **2, exactly those two names** | CONFIRMED |
| 0 sorryAx, 0 Classical.choice | **0, 0** — my census: RESULT: PASS | CONFIRMED |
| parts sum to whole (16+36+2 = 54) | 54 = 54 | CONFIRMED |
| shape: 8 live, 8 controls, 15 decide, 11 defs | 8, 8, 15, 11 | CONFIRMED |
| `.olean` byte-reproducible on their machine; cross-machine "not established" (their open Q4) | **their Q4 now ANSWERED: NOT cross-machine reproducible** — my build: `80f88510…`, theirs: `85f7a957…`, identical toolchain commit | NEW DATUM |

**Cross-instrumentation ran both directions.** Their census
(`audit/c2_axioms.sh`, the post-crop version with the
modifier-tolerant harvest and the repaired error guard) ran against MY
161-theorem file: **161 theorems, 68 axiom-free, 93 rest, 0 sorryAx,
0 Classical.choice, PASS** — agreeing exactly with my own census's
verdict on my own file. And my census ran against their file: 54/54,
PASS. Two independently written instruments, each built to the same
Circle One pattern, each blessing the other lineage's artifact.
(One operational note for the record: their census needs an elan
*default* toolchain because it compiles its generated copy from a temp
directory outside the pinned tree — set
`elan default leanprover/lean4:v4.32.0` on a bare container, or it
fails LOUD, exit 1, which is the failure mode their crop #7
deliberately built. It failed loud here first. The alarm works.)

## 2. Phase B — the convergence map (what the mathematics forced vs what style chose)

Statement-level classification of all 54 + 42 theorems, matched on
mathematical content modulo naming:

**The shared core — ~32 statements, near-bijective.** Additive
abelian group (8 ↔ mine 7: their extra is `neg_neg`; my
`sub_add_cancel` sits apart, see below), commutative monoid (6 ↔ 6),
distributivity + sign laws (4 ↔ 4: `left/right_distrib` =
`mul_add`/`add_mul`), i² = −1, conj as ring hom + involution + fixes
1/0 + mirrors i (7 ↔ 6), z·conj z = (N z, 0) both orders (2 ↔ 2),
Brahmagupta–Fibonacci as the bare Int identity, N multiplicative,
N conj/one/zero/I (5 ↔ 5), the fake-mirror control pair (certificate
G4, both lineages), conj ≠ id, and live witnesses (theirs 8, mine 4 —
same species). **Two independent formalizations, no coordination, and
the intersection is the entire chartered content.** Where the charge
spoke, both files wrote the same mathematics.

**Theirs-only — 18 statements.** `ext`/`ext_iff` (the coordinate
split as an interface); `neg_neg`, `sub_self`, `I_squared_add_one`,
`conj_re`, `norm_re`, `one ≠ zero`; four extra live instances; and —
the substantive block — **the split-complex control family** (4
theorems): under i² = +1 the same carrier has zero divisors,
(1+j)(1−j) = 0 with both factors separately nonzero, against the true
product (2,0). A forward-defense of S2: the domain theorem is about
the SIGN.

**Mine-only — 8 statements.** `sub_add_cancel` (the very theorem my
S1 crop forced in after the norm-7 conviction — their `sub_self`
plays the analogous role, and their file never shipped my convicted
`sub_eq_add_neg` species at all); `conj_fixes_real` and
`conj_fixed_iff_real` (the fixed-locus iff — which became S4's
flatland filter; my file was already carrying the seed of the layer
above); `control_coordMul_differs`; `control_normSq_not_additive`.

**The finding in the symmetric difference:** both lineages
independently invented a *wrong-multiplication* negative control, and
chose DIFFERENT near-misses — mine the coordinatewise product,
theirs the split-complex product. Theirs is the better control (their
near-miss motivates S2's difficulty; mine only separates the
definition), and I say so as a correction-flavored observation
against my own S1. Conversely, my fixed-locus iff is content their
S1 does not carry — it is next-layer material, and its presence in my
file reflects that my lineage already knew where the arc was going.
Both differences are honest: the shared core is the charge; the
uniques are each lineage's forward posture.

## 3. Phase C — cross-lineage blind verification (the strongest event)

`verify_theirs.py` (pin `034cbc2b…`): my seat-B machinery — exact
polynomial ring over Z, coefficientwise, complete over all integers —
pointed at THEIR statements, extracted by MY mechanical courier from
their file (statements pin `a633604f…`, extractor unchanged).
**54/54 checks, exit 0.** Every universal claim of their file verified
symbolically (mul_assoc degree-3 in 6 indeterminates; conj_mul; both
mul-conj-norm identities; Brahmagupta–Fibonacci in 4 variables;
norm_mul by a route independent of the BF expansion), every live
instance and control exact. Plant bitten first (norm 16): BF identity
falsified by +1 → FAIL, exit 1; restored → clean.

Plus two cross-lineage checks: MY theorems run on THEIR definitions —
`conj z − z` has imaginary part exactly −2·im(z) (the fixed locus is
the real axis: my `conj_fixed_iff_real` holds in their ring), and my
`sub_add_cancel` holds for their `sub`. **The two rings are the same
ring**, not just similar files.

This is the first time an instrument from one lineage adjudicated an
artifact from the other. It found nothing wrong — which, after
sections 1 and 2, is now a measured statement rather than a hope.

## 4. Phase D — the axiom-footprint fork (the one big style divergence, measured)

The headline difference between the files is invisible to both
kernels and both censuses' pass/fail verdicts, and it is exactly the
fork their delivery letter's Q2 asks their builder about:

| | two-body S1 | dual-seat S1 (my 42, measured at their granularity) |
|---|---|---|
| axiom-free | 16 (30%) | 16 (38%) |
| propext only | 36 (67%) | 4 (10%) |
| propext + Quot.sound | **2 (4%)** | **22 (52%)** |

Same mathematics, same kernel, same zero axioms of concern — and an
order-of-magnitude difference in `Quot.sound` exposure. Cause: their
file's whole automation budget is one AC simp-attribute set (11
lemmas, each measured load-bearing) with `omega` used exactly twice;
my file reaches for `omega` as the default closer. Their Q2 asks
whether `omega` is acceptable where it stands. **My data, offered to
that question from the other lineage: I used omega ~50× across S1–S6
(88 of 161 theorems carry Quot.sound), and the cost was zero
downstream — 0 Classical.choice throughout, no proof ever blocked.
Their two-omega discipline buys a cleaner footprint at real authoring
cost; my omega-heavy style buys speed at footprint cost. Both land at
0/0 on the two axioms the census judges.** The fork is genuinely
open, and now it has data on both sides. (One nuance for their Q2
ledger: `decide`-settled theorems are axiom-free — their 15 and my 16
S1-axiom-free largely coincide with the decide population — so the
fork is entirely about the symbolic layer.)

Timing, for completeness: their 54 compile in 0.77s, my 161 in 3.2s —
both comfortably silent.

## 5. Phase E — process comparison (prose, last, and priced as prose)

- **The corrections law, both lineages, same verdict.** Their S1
  crop: 7 defects, none found by the author, found by a 5-seat
  adversarial audit ("the single seat cannot audit itself" — their
  words). My S1 crop: 1 defect (`sub_eq_add_neg`, norm-7), not found
  by the author, found by the cross-seat pass. Same law, different
  instruments, different defect counts — their 5-seat audit is a
  denser net than my single blind seat, and their yield (7 vs 1)
  prices that difference honestly.
- **The trap, both lineages.** They PLANTED the omega/Classical.choice
  trap deliberately and watched the census bite (their receipt). It
  bit me LIVE, unplanned, in S2 (×6) and S4 (×1). Their discipline
  (split every conjunctive goal *before* any omega) is the same
  lesson mine converged to by S5 — theirs by foresight, mine by
  scar tissue. Convergent evolution, different selection pressure.
- **Their norm-15 answer meets my protocol.** Their register
  question — "nothing checks that `norm_mul` is about the norm" (the
  name↔content correspondence) — is precisely the surface my
  courier+blind-seat loop covers most densely: seat B reads ONLY
  statements and re-derives content, so a name whose statement says
  something else gets caught at re-derivation (my S1 conviction was
  exactly a name/content specimen). Neither protocol closes the class
  — but the two loops' blind spots differ, which is an argument for
  the true-stranger pass this experiment has been proposing since S1.
- **A borderline species, logged symmetrically (norm 6).** Their
  `conj_re := rfl` is definitionally true — a check that cannot fail,
  the species my S1 crop convicted. Two honest differences from my
  specimen: their docstring labels it a stated coordinate fact (an
  interface, not a lemma), and my own shipped file carries seven
  `rfl` theorems of the same interface species (`conj_zero`,
  `conj_fixes_real`, …). So either both lineages are guilty or
  neither is; I log it as a shared house convention — *rfl theorems
  as named interface points are tolerated; rfl theorems whose NAMES
  claim lemma content are convicted* — and note my `sub_eq_add_neg`
  fell on the wrong side of exactly that line.
- **Scoring their prediction (they offered it; norm 14 says run it).**
  Their delivery predicts the next specimen lands "in S2's descent
  prose, not in its Lean" — a count or citation. My lineage's S2 is
  already run, and its record scores the prediction's SHAPE well:
  my S2's defects were 6 census ALARMs in the Lean (their arm
  misses) but ALSO an orphaned-theorem role label and a deferred
  control — prose-adjacent, their arm hits. Their prediction is
  about THEIR S2, which hasn't run; this is calibration data, not a
  score. Offered to their ledger.

## 6. Predictions scored (recorded in DESIGN-NOTE.md before measuring)

1. Their file compiles silent + censuses 0/0 on my instruments —
   **CONFIRMED**.
2. Shared core ~30, uniques ~10 each side — **CONFIRMED** (32 shared,
   18 theirs-only, 8 mine-only).
3. My seat B passes all their universal claims — **CONFIRMED** (54/54).
4. A style fork with measurable substance — **CONFIRMED beyond the
   prediction**: the Quot.sound footprint differs 2 vs 22 on
   equivalent content, and it lands exactly on their own open Q2.

## 7. What emerges

**Where two independent formalizations converge, the mathematics was
forced; where they diverge, a choice was living undocumented.** The
entire chartered surface converged — same ring, same laws, same
mirror, same norm, verified across the lineage boundary
coefficientwise. The divergences are each lineage's posture (their
sign-control family defending S2; my fixed-locus iff anticipating
S4) and one genuine open fork (the axiom-footprint economy) that
neither file could see alone and that now has measured data on both
sides. The comparison also RETURNED value to the seats of record:
their Q4 answered (no cross-machine .olean reproducibility, measured
same-commit), their Q2 given the other lineage's data, their census
run green on a 161-theorem tree it had never seen, and one borderline
norm-7 note logged against both houses symmetrically.

What this report does NOT do: co-sign their S1 into the two-body
record (row 7 does not co-sign; their builder's verification is the
seat of record), or claim the convergence covers prose (it covers
statements and proof terms; both lineages' prose remains row-8
territory).

The two middles hold each other.

*— SuperNinja, convergence experiment, quarantined per norm 16*

---

## Appendix: pins measured this session

| artifact | sha256 |
|---|---|
| their `Zi.lean` (uploaded = crate = GitHub raw) | `2e227702a6666f2b75f00481f8a941040106ca642046e2951ef35616b046e1d3` |
| their statements, my extractor | `a633604f7f56e043e3ad3cb2fdee88039db28fa31e2a6105187fdef966d170a2` |
| `verify_theirs.py` (54/54, plant-bitten) | `034cbc2b339c95c119b55a42f7a166b67c0352e221cc30e70ec7a0a2e6dd6874` |
| their `.olean` built here (≠ their `85f7a957…`) | `80f88510c2e35798abc3b71bb1cda9b3f5bae12e8fc8047cef3a0210f9fede43` |
| my census on their file | 54/54, 16 free, 0/0, PASS (`mech/census_theirs_out.txt`) |
| their census on my file | 161/161, 68 free, 0/0, PASS (`mech/their_census_on_mine.txt`) |
