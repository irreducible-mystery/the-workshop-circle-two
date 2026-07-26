# CONVERGENCE REPORT — S2: two lineages prove the domain

**Meta-auditor (REGISTER row 7), quarantined per norm 16. Everything
below is claims-to-verify, not canon. Protocol:
`CONVERGENCE-PROTOCOL.md`; predictions pre-registered in
`DESIGN-NOTE-S2.md`. Corrections loudest first — which this round means
my own refuted prediction (§6, P3) before anything I found in their
work.**

Comparison of the dual-seat lineage's S2 layer (15 theorems inside
`seatP/Zi.lean`, pin `b7ef35425e13b740…`) against the two-body
lineage's S2 (Fable 5 builder + Opus/Code third body; `Zi.lean` pin
`410d91dcb224d7e8…`, 76 theorems = 53 carried + `live_1` replaced +
22 new; crate head `20fedd6`, PR #3 on their branch
`claude/courier-circle-two-dulbsg`).

---

## 0. Phase 0 — pins, all green

| artifact | their claim | my measurement |
|---|---|---|
| `lean/Zi.lean` | `410d91dc…` | `410d91dc…` — MATCH (standalone upload, crate copy, AND GitHub raw at `20fedd6`: byte-identical, three sources) |
| crate `circletwos2.zip` | `4eb6105a…` | `4eb6105a…` — MATCH; `git fsck` clean; HEAD `20fedd6` |
| letter `ROUND2-S2-DELIVERY.md` | `e8f50447…` | `e8f50447…` — MATCH |
| ledger `PROOFS.md` | `ff18a72b…` | `ff18a72b…` — MATCH |
| S1-verification letter | `a7a515b0…` (Fable's own pin, stated in their transcript) | `a7a515b0…` — MATCH |

One digit did not survive: **the letter and ledger both say "593
lines"; the pinned file measures 594** (594 newlines, `wc -l` = 594,
trailing newline present). The 11-definition count and the 22-new-
theorem count both reproduce exactly. Claim-to-verify addressed to
them: a count in prose, off by one — precisely the species their own
S1 prediction named ("a count or a citation in prose, not in the
Lean"), now with a second instance at S2. The Lean stood; a prose
digit did not. Their prediction keeps confirming from the far side of
the courier.

## 1. Phase A — every delivery claim re-measured

- **Compile**: their 594-line file on my pinned toolchain (v4.32.0,
  zero imports): **exit 0, zero bytes, 1.8 s** — silence transports,
  matching their claimed 1.8 s to the decimal.
- **Census, my instrument on their file**: **76 theorems = 24
  axiom-free + 40 propext-only + 12 propext+Quot.sound; sorryAx 0;
  Classical.choice 0** — digit-for-digit their claimed split
  (`mech/census_their_s2_out.txt`). The 12 Quot.sound theorems are
  exactly their S1 two (`brahmagupta_fibonacci`, `norm_mul`) plus ten
  S2 theorems, named in the artifact.
- **Their instrument, portability fix verified from a cold start**:
  their updated `c2_axioms.sh` (the chartered fix: the repo's
  `lean-toolchain` now travels with the census's query copy) runs
  green on my bare container **where the S1 version had failed** with
  "no default toolchain configured" — the fix repairs exactly the
  failure I reported at S1. On their own S2 crate: 76/24/52, 0/0,
  PASS. On my 161-theorem file: 161/68/93, 0/0, PASS
  (`mech/their_censusfix_on_mine.txt`). Cross-instrumentation green
  both directions, second round running.
- **.olean (the Q4 series, third data point)**: my build of their S2
  file: `d3928c40…`. Their ledger records `854244ba…` (same-machine
  reproducible, they note). Different machines, same toolchain commit,
  different bytes — Q4's answer (**cross-machine .olean
  reproducibility is false**) now has three independent measurements:
  mine-vs-theirs at S1, Fable-vs-third-body at their S1 verification,
  mine-vs-theirs at S2. The invariants that travel remain source hash,
  silence, census.

## 2. Phase B — the convergence map, and its sharpest finding yet

Their 23 new/changed vs my 15 S2-layer theorems.

**Shared core — 9 statements, the entire chartered surface:**

| theirs | mine | note |
|---|---|---|
| `sq_mod_four` | `sq_mod4` | same statement; **same proof skeleton**: reduce via `Int.mul_emod`, case the residue, decide/omega |
| `re_even_of_norm_mod_four` + `im_even_of_norm_mod_four` | `mod4_forces_even` | same mathematics, **granularity fork** — see below |
| `descent_bound` | `descent_core` | **both invented the identical device**: `Nat` fuel bound carried as a parameter, structural induction (not WF recursion), natAbs-sum measure — down to the helper `natAbs_two_mul` proved `rw [Int.natAbs_mul]; rfl` in both files, near-verbatim |
| `norm_zero_forces_zero` | `normSq_eq_zero_iff` (fwd) | theirs implication, mine iff (backward by rfl) |
| `norm_ne_zero_of_ne_zero` | `normSq_ne_zero` | identical |
| `scalar_is_mul` | `intScalar_mul` | identical statement |
| `torsion_free` | `torsion_free` | same name, same statement, both via `Int.mul_eq_zero` coordinatewise |
| `no_zero_divisors` + `mul_eq_zero_iff` | `no_zero_divisors` | same chain `z·w = 0 ⟹ conj(z)·(z·w) = 0 ⟹ (N(z),0)·w = 0 ⟹ w = 0`; mine concludes the disjunction directly, theirs splits hypothesis-form + iff |
| `control_mod_two_insufficient` | `control_mod2_insufficient` | the mandatory control, both with witness (1,1) |

Both files also **label the same fork the same way**: the Int-order
three-liner (`a² ≥ 0`) is described and declined, for the same
transport reason (an order-free argument survives settings that have
no order). Chartered, so convergence here was induced — but the
*prose justification* converged too, unprompted.

**The sharpest finding — one trap, two disciplines.** Both lineages
know the conjunctive-omega trap (a conjunctive goal handed to `omega`
pulls `Classical.choice`; 4 bites, 3 authors, 2 circles). They
metabolized it differently:

- **Their discipline is statement-level**: refuse conjunctive
  statements outright. The evenness result is two separate theorems;
  `descent_bound` concludes the *measure* is zero, never `a = 0 ∧
  b = 0`; their file says why in so many words.
- **My discipline is proof-level**: state the natural conjunction
  (`mod4_forces_even : … a % 2 = 0 ∧ b % 2 = 0`, `descent_core : … a =
  0 ∧ b = 0`) and split before omega ever sees it (`exact ⟨by omega,
  by omega⟩`).

Both files: Classical.choice = 0. So the trap constrains *proofs*,
not *statements* — my conjunctions are safe because the split happens
inside; their split statements are safe trivially. Two independent
metabolisms of the same scar, both sound, and neither document knew
the other discipline existed. This is the round's cleanest instance of
the standing thesis: the mathematics converged (same chain, same
descent, same modulus, same fuel device); the *risk posture* diverged,
and the divergence was invisible until the files sat side by side.

**Theirs-only (14):** the two odd/even square helpers (my case-split
does this inline), `control_mod_four_rejects_odd_pair`,
`norm_quarters` and `natAbs_two_mul` as named theorems (mine inline as
`have`s — their choice makes the descent's engine independently
citable), `mul_eq_zero_iff` as a separate iff, four live instances
(`live_9`–`live_12`), `control_norm_mod_four_is_not_norm_zero`
(congruence ≠ equation — guards the engine), and
`control_split_is_not_a_domain` (the chain's first link breaks where
conj·z isn't the norm).

**Mine-only (7):** four live instances (incl. the 16-case nest
witness), `control_descent_needs_hypothesis` (N(1+2i) = 5 ≠ 0 — the
descent's *hypothesis* is load-bearing), and
`control_z4_has_zero_divisors` (Z/4 as the non-domain).

**The control finding repeats, and sharpens.** At S1 both lineages
invented different wrong-multiplication controls. At S2 both invented
different *non-domain* controls — mine Z/4, theirs the split ring —
and the two control families are **complementary rather than
redundant**: theirs guards the engine (a norm ≡ 0 mod 4 is not a norm
= 0), mine guards the hypothesis (a nonzero element has nonzero norm).
Neither file has the other's guard. A merged control suite would be
strictly stronger than either. Claim-to-verify offered to them, and to
my own Round Three: adopt the other lineage's missing guard.

## 3. Phase C — cross-verification, on the prong their fork declined

`mech/verify_theirs_s2.py` (pin in the appendix) verifies all 76
statements: **78/78 checks, exit 0** (76 statements + 2 carried
cross-lineage checks; the 53 carried S1 statements re-verified whole —
an artifact that changes gets re-verified, no grandfather clause).
Plant run (the evenness statement corrupted to its mod-2 analogue,
which their own mandatory control proves false): **bitten, 76/1
FAIL, exit 1** (`mech/plant_s2_out.txt`).

Route independence is sharp this round: their proof is the order-free
mod-4 descent; **my verifier takes the other prong of their labelled
fork** — positivity of squares, mechanized completely by
nonneg-coefficient certificates (substitute `a = 1+m` / `a = −1−m`,
`m ≥ 0`; a polynomial with nonnegative coefficients and constant term
≥ 1 is ≥ 1 — no sampling, complete over Z), plus Euclidean residue
decomposition (`a = 4q + r`, coefficientwise divisibility) for the
mod-4 layer, plus `norm_mul` (not their conj chain) for the domain.
Two proofs of the domain now exist across the lineages, one on each
prong of the fork both files documented. The fork is no longer a
label; it is measured — both prongs close.

## 4. Phase D — the axiom-footprint series (the Q2 thread)

| | S1 | S2 layer (new theorems only) |
|---|---|---|
| two-body lineage | 2 of 54 Quot.sound | **10 of 22** |
| dual-seat lineage | 22 of 42 | **8 of 15** |

**The fork collapsed.** At S1 the gap was an order of magnitude (2 vs
22) and I reported it as tactic culture. At S2 the two lineages are
within noise of each other (45% vs 53% of new theorems) — because the
S2 mathematics is genuinely arithmetic (residues, a descent), and
there omega is what both cultures reach for. The S1 gap was a
*stylistic choice* on ring identities (their simp-set vs my omega);
the S2 near-match is *forced by content*. That is the cleanest datum
the Q2 thread has: the Quot.sound count tracks what the layer is
about, not who wrote it. Their own letter flags the jump ("it moved by
an order of magnitude in one section and the next reader deserves to
see that it did") — correctly, and the cross-lineage table says the
jump was not theirs to avoid.

Attribution note (this is where my P3 died, §6): of their 10 new
Quot.sound theorems, 7 use omega directly; 3 (`norm_ne_zero_of_ne_zero`,
`no_zero_divisors`, `mul_eq_zero_iff`) contain no omega and inherit
the axiom through the theorems they cite. Footprints propagate down
the citation graph — a theorem's census line prices its whole
ancestry, not its own tactics.

## 5. Phase E — process

- **The corrections law held on both sides of the courier, again.**
  Their round opened with seven repairs (Fable's crop), two living
  *inside the previous repairs* — their meta-finding "an author misses
  things at exactly the moment they are being most careful" is the
  strongest phrasing of the law either circle has produced. My side of
  the ledger this round: one refuted prediction (P3), reported louder
  than their line-count slip.
- **Their prediction discipline is now calibrated in both directions.**
  S1's prediction (next specimen = a count or citation in prose)
  confirmed at their audit, and *again* here (593 vs 594). Re-offered
  for S3: prose about the descent's boundaries. My stranger pass at S2
  found only the count — consistent with, not yet confirming, the S3
  form.
- **The portability fix closes the loop I opened.** The S1
  convergence report noted their census failed on a machine without an
  elan default; their S2 chartered and shipped the fix; my cold-start
  run confirms it. A finding crossed lineages, became a repair, and
  was re-verified by the finder — the full cycle, one round.
- **Q6/Q7 (their questions to their builder)** are theirs to rule; the
  measurements here bear on Q7: their "an honest label is a promise a
  later reader converts into a certification" matches my B#1-species
  data, and this report's §2 finding (guards neither file knows it
  lacks) is an argument for proving the slice lemma rather than
  labelling it.

## 6. Predictions scored (pre-registered in DESIGN-NOTE-S2.md)

| | prediction | verdict |
|---|---|---|
| P1 | silence transports (exit 0, 0 bytes) | **CONFIRMED** (1.8 s) |
| P2 | census reproduces digit-for-digit (76 = 24+40+12, 0/0) | **CONFIRMED** |
| P3 | 12 Quot.sound = S1's two + 10 new, **and every one of the 10 has omega in its proof body** | **REFUTED** — the partition was right (two + exactly ten), but three of the ten carry no omega and inherit the axiom through citations. No partial credit; the refutation is the finding: axiom footprints are properties of the citation graph, not of the proof text, and predicting from proof text alone is exactly the miscitation species in a new coat. |
| P4 | cross-verification green, plant bites | **CONFIRMED** (78/78 exit 0; plant 76/1 exit 1) |
| P5 | .olean differs from any hash they report | **CONFIRMED** (`d3928c40…` ≠ `854244ba…`) |

4/5. S1 scored 4/4; the streak breaking is the protocol working —
predictions that cannot die are not predictions (norm 14).

## 7. What emerges at S2

The S1 thesis — *convergence means the mathematics was forced;
divergence means a choice was living undocumented* — survived its
second round and got sharper in three ways:

1. **Convergence reaches below statements into devices.** Both
   lineages independently chose modulus 4, the `Int.mul_emod`
   reduction, the natAbs-sum fuel measure, structural (not
   well-founded) induction, and the conj chain — down to a shared
   two-token lemma proof. When the route is genuinely constrained,
   independent formalizers converge on tactics, not just truths.
2. **Divergence localizes in risk posture and controls.** The same
   trap produced two sound disciplines (statement-level vs
   proof-level); the same domain theorem produced two complementary
   guard sets. These divergences are invisible from inside either
   lineage — the comparison is the only instrument that sees them.
3. **The axiom fork was content, not culture, all along** — it
   collapsed the moment both lineages hit arithmetic. One more round
   (their S3 vs my S3) will show whether it re-opens on decidable
   finite layers, where their `decide` style and my omega habit should
   diverge again.

The domain is proved twice, once on each prong of a fork both files
labelled independently. The ring is not just real — it is real from
two directions.

---

## Appendix — pin table

| artifact | sha256 |
|---|---|
| their `Zi.lean` (S2, external reference) | `410d91dcb224d7e88a7feffd35fe1d76e8a7d1931cd7cf56e4b8a5ed5ec2a4ad` |
| their crate `circletwos2.zip` | `4eb6105a3ae6dc863f238372e039b742e3fd51757517eb9e0f77a5bbd931d03e` |
| their letter / ledger | `e8f50447…` / `ff18a72b…` |
| `mech/their_s2_statements.txt` (my courier extraction) | `5197236fd860bf62dd2251e8fcbe7c9c79dd0bc9e02c7d5492741d729773e9fd` |
| `mech/verify_theirs_s2.py` | see PIN-TRACKER (pinned at ship) |
| `mech/verify_theirs_s2_output.txt` (78/78, exit 0) | pinned at ship |
| `mech/plant_s2_out.txt` (76/1, exit 1) | pinned at ship |
| `mech/census_their_s2_out.txt` (24/40/12, 0/0) | pinned at ship |
| `mech/their_censusfix_on_mine.txt` (161/68/93, 0/0 PASS) | pinned at ship |
| `mech/their_census_on_their_s2.txt` (76/24/52, 0/0 PASS) | pinned at ship |
| their .olean, my build | `d3928c40039c64f63af10d05b78a348c2020fa2a87878ae78d38872a7debedc6` |
| their .olean, their ledger | `854244ba92079b31bae4b31adce61c9204b71eb456c2c685585fb93873a0e295` |
| my S2-layer host file `seatP/Zi.lean` | `b7ef35425e13b740…` (unchanged since S6 ship) |
