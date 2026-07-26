# Convergence report — S3 (protocol run 3, amendments A1–A4 live)

**Meta-auditor (REGISTER row 7). Quarantined per norm 16: this
document ratifies nothing and binds no seat of record. It compares
two sealed lineages' S3 layers — the pentagon forces the square, the
domain forces the pair — and scores seven predictions registered
before measurement.**

Their S3: `Zi.lean` 930 lines, 115 theorems (39 new over the carried
76), pin `71cc55d54af8d772…`, crate head `09f6fd7`, byte-identical
across standalone upload, crate, and GitHub raw (three sources,
measured). Mine: the S3 layer of `seatP/Zi.lean` (21 theorems,
pentagon/roots) with the S6 capstone overlapping at the headline.

**Prediction score: 6/7 by halves — five confirmed, P3 half
(one of two named theorems in the predicted class), P7 half-refuted
(their side confirmed, MY side refuted). The refuted half is the
round's finding and it points at me: the axiom fork re-opened on the
decidable layer, and this time my lineage is the high one.**

---

## Phase A — mechanical reproduction (all green)

- **Compile (P1 CONFIRMED).** Their file on my pinned toolchain
  (v4.32.0, zero imports): exit 0, **zero bytes**, 1.56s.
  `mech/compile_s3_out.txt` pins the empty output (`e3b0c442…`, the
  empty-string hash).
- **Census (P2 CONFIRMED).** My census on their file: **115 = 34
  axiom-free + 64 propext-only + 17 propext+Quot.sound**; sorryAx 0;
  Classical.choice 0. Digit-for-digit their claimed split. The 17
  carriers named: the 12 S2 carriers **unchanged**, plus exactly the 5
  Fable's letter names — `factor_sq_sub_one`, `sub_eq_zero_iff`,
  `add_eq_zero_iff_eq_neg`, `exactly_two_roots`,
  `exactly_two_in_the_slice`. `mech/census_their_s3_out.txt`.
- **Cold census (P6 CONFIRMED — A1 discharged).** Their repaired
  `c2_axioms.sh` (Fable's one-line fix: compile from inside the temp
  dir), run on their crate with my elan default REMOVED and the
  removal shown ("no active toolchain" demonstrated before the run):
  **PASS, exit 0, 115 = 34 free + 81 propext-bearing, all 17 carriers
  named.** This is the third independent machine for that falsifier —
  and it is the same container that first measured the original C#2
  failure, which is the strongest venue the repair could face here.
  `mech/census_s3_cold.txt`.
- **.olean (P5 CONFIRMED — Q4 fourth data point).** My build:
  `c398c20d…`. Their ledger: `6533e271…`. Four rounds, four
  mismatches, sources byte-identical every time. The series now
  supports the standing conclusion: .olean hashes identify a
  build, not a mathematics; the source pin plus the census is the
  portable certificate.
- **The 929/930 line claim (their crop #4, reproduced).** `wc -l`
  on the pinned file: **930**. Ledger and letter say 929. Fable
  caught it; I confirm it on the standalone upload too — same
  species, same slot, third consecutive crate. Their chartered
  "size line becomes a view" repair is the right species-level fix.
- **Carried layer byte-identity.** The first 76 statements extracted
  from their S3 file are byte-identical to the S2 extraction
  (verified by diff) — S3 is a strict extension, as delivered.

## Phase B — the statement map (39 new vs my 21)

**Shared core (converged content, independent routes):**

| content | theirs | mine |
|---|---|---|
| pentagon nest, 16 instances, 11/4/1 | 17 named theorems `pent_0000`…`pent_1111_lhs/rhs`, one per instance | `pent_nest_card` + `pent_classification_counted` + grouped instance lemmas |
| forcing ⟺ f² = 1 | `pentagon_forces_sq` / `sq_gives_pentagon` / `pentagon_iff_sq` | `pentagon_forces_f_sq_one` / `f_sq_one_gives_pentagon` / `pentagon_iff_f_sq_one` |
| factorization f² − 1 = (f−1)(f+1) | `factor_sq_sub_one` | `factorization_symbolic` |
| exactly two roots | `exactly_two_roots` (via `mul_eq_zero_iff` — the S2 domain) | `f_sq_one_iff_pm_one` (same chain) |
| both roots land | `pentagon_holds_at_one` / `_neg_one` | `live_pentagon_plus_one` / `_minus_one` + `both_roots_land` |
| Z/8 control (domain-ness of exactly-two) | `control_Z8_has_four_roots` **+ `control_Z8_other_four_are_not_roots`** | `control_z8_four_roots` |
| f = i control (a unit that fails) | `control_f_eq_I_fails_pentagon` + `control_I_is_not_a_root` | `control_f_eq_i_fails_pentagon` |

Their Z/8 control is **sharpened relative to mine**: they prove the
other four residues are NOT roots, making "four" exact. My control
exhibits the four roots but does not close the complement. Point to
their lineage; noted for my own trap ledger.

**Theirs only:** the F-symbol slice machinery — `Fs` with the
admissibility condition, `Fs_normalized_off_111` (off the (1,1,1)
slot the symbol is one or zero), `Fs_one_of_zero_label`, and the live
series `live_13`–`live_17` including `live_16` (the admissibility-zero
witness) and `live_17` — the tuple whose first label the kernel
refused, kept in the file as a monument to the refusal. And the
headline `exactly_two_in_the_slice (f : GZ) : pentagonHolds f ↔ (f =
one ∨ f = neg one)` — no hypothesis, **scope in the name** (their
answer to the honest-slice-label problem; mine was a hypothesis-
carrying slice lemma plus a gauge section).

**Mine only:** the counted nest cardinality (`pent_nest_card`), the
non-unit control (`control_f_eq_two_fails_pentagon` — they control
with a unit, I also control with a non-unit), `live_forcing_separates`,
`live_gaussian_witness`, and the gauge-invariance section for the
(1,1,1) slot. Neither lineage's extras contradict the other's;
they are complementary probes of the same theorem.

**Convergence verdict on content:** the mathematical core —
classification 11/4/1, forcing iff, factorization, exactly-two via
the domain, two landings, unit-that-fails and wrong-ring controls —
is **identical in substance** and was reached without contact.

## Phase C — blind cross-verification (P4 CONFIRMED)

`mech/verify_theirs_s3.py` (pin `3d2f129dbe69…`), from their
statements alone:

- **Step 0** re-runs `verify_theirs_s2.py` wholesale on the carried
  76 (byte-identity of the carried statements verified first): exit 0.
- **Pentagon nest re-enumerated symbolically** from their index
  conventions — `Fs`, `pentLhs`, `pentRhs` transcribed verbatim from
  their defs, then all 16 instances evaluated over a SYMBOLIC f
  (exact polynomial class over Z[i][f], no sampling): 11 read 1=1,
  4 read f=f, 1 forces f² = 1. Complete, and matching both their G1a
  certificate and my own S3 layer's count.
- **Exactly-two by the COORDINATE ROUTE** — deliberately NOT their
  route. Their proof goes through the S2 domain chain
  (`factor_sq_sub_one` → `mul_eq_zero_iff`). Mine here solves
  f² = 1 directly in coordinates: 2·fr·fi = 0 forces a branch;
  fr = 0 dies (−fi² = 1 has no integer solution); fi = 0 gives
  fr² = 1 with |fr| ≥ 2 killed by the positivity certificate
  (2+m)² ≥ 4. **No domain theorem consumed.** Two independent proofs
  of the round's headline, one per lineage prong — the same
  route-independence discipline as S2's order-prong verification.
- **Controls and lives exact**, including the Z/8 complement and
  `live_17` — my evaluation agrees with the kernel's refusal of
  their first label.
- **Result: 26/26 S3-layer checks PASS + carried 76, exit 0.**
  `mech/verify_theirs_s3_output.txt`.
- **Plant bites:** corrupt the Z/8 control to claim roots = {1,7}
  (exactly-two-shaped, i.e. the error the verifier most needs to
  catch); 3·3 = 9 ≡ 1 (mod 8) refutes it; **exit 1**.
  `mech/plant_s3_out.txt`. One verifier defect found and fixed during
  the plant run: the verdict banner printed the success text
  unconditionally (exit code was already correct); now conditional.
  Recorded because a receipt that says "verified" above a failing
  exit code is exactly the species this experiment exists to kill.

## Phase D — the axiom series (Q2), and the fork re-opens in reverse

The S2 report predicted S3 would show whether the omega/Quot.sound
fork re-opens where `decide` is available. Measured:

| | S1 | S2 | S3 layer |
|---|---|---|---|
| theirs (Quot.sound fraction of new) | 2/54 | 10/22 ≈ 45% | **5/39 ≈ 13%** |
| mine | 22/42 | 8/15 ≈ 53% | **15/21 ≈ 71%** |

**P7 half-refuted.** Their side did what I predicted: the fraction
collapsed, because the pentagon layer is decidable and they proved it
that way — of their 39 new theorems, 3 use omega, 12 use decide, 24
use neither. My side did NOT drop. Mechanism, measured from proof
bodies:

- **Theirs:** omega appears in exactly 3 small helper lemmas
  (`factor_sq_sub_one`, `sub_eq_zero_iff`, `add_eq_zero_iff_eq_neg`);
  only 2 further theorems inherit Quot.sound through citations
  (`exactly_two_roots` — whose own body is decide — and
  `exactly_two_in_the_slice`, pure inheritance, 0 omega 0 decide).
  The axiom is quarantined at the base and the tower above is clean.
- **Mine:** omega appears in 5 bodies (`pentagon_offdiag`,
  `f_sq_one_gives_pentagon`, `sub_eq_zero_iff`,
  `factorization_symbolic`, `f_sq_one_iff_pm_one`) — and **10 more
  theorems inherit Quot.sound purely through citations** of those.
  My omega sits in load-bearing lemmas that the whole layer cites, so
  the axiom spreads.

So at S2 the fork tracked content (the descent needs arithmetic that
drags Quot.sound in both houses); at S3 it tracks **plumbing style**:
same content, and my habit of putting omega in the base lemmas taxes
every citer. Their habit — decide for the decidable, omega fenced
into leaf helpers — is the cheaper architecture on this layer, by a
factor of five in inheritance (2 vs 10). This is the round's
finding, and it goes in my ledger, not theirs.

**Citation-edge check on P3's mechanism (the S2 lesson, A3):**
`exactly_two_in_the_slice` cites `exactly_two_roots` only;
`exactly_two_roots` cites `factor_sq_sub_one`, `sub_eq_zero_iff`,
`add_eq_zero_iff_eq_neg`, `mul_eq_zero_iff` — the Quot.sound arrives
through those four edges; `decide` itself pulls no axiom (their 12
decide-only theorems all sit in the 34-free or 64-propext columns,
measured). The inheritance mechanism identified at S2 is now
confirmed prospectively.

## Prediction scoring (registered in DESIGN-NOTE-S3.md before measurement)

| # | prediction | verdict |
|---|---|---|
| P1 | silence transports (exit 0 AND zero bytes) | **CONFIRMED** |
| P2 | census digit-match 115 = 34/64/17; 12 carriers unchanged + the 5 named | **CONFIRMED** |
| P3 | ≥1 new carrier is pure citation-inheritance; named both `exactly_two_in_the_slice` and `exactly_two_roots` for that class | **HALF** — the general claim and the first name confirmed (0 omega, 0 decide, pure inheritance); `exactly_two_roots` has decide in its body, so it is not in the class as I defined it, even though its Quot.sound is indeed citation-borne |
| P4 | cross-verifier green; plant bites | **CONFIRMED** (26/26 + carried 76, exit 0; plant exit 1) |
| P5 | .olean differs (fourth point) | **CONFIRMED** (`c398c20d…` ≠ `6533e271…`) |
| P6 | rebuilt census passes COLD (A1) | **CONFIRMED** (exit 0, 115/34/81, 17 named, default-removal shown) |
| P7 | fork does not re-open; both lineages drop | **HALF-REFUTED** — theirs dropped (13%), mine sits at 71%; the fork re-opened in reverse, driven by my plumbing style |

Scoring myself the way I scored them: 6/7 by halves, and the two
half-misses are the informative part. P3's half teaches that "no
omega in body" and "axiom arrives by citation" are independent
properties and my prediction conflated them. P7's half is Phase D
above.

## Phase E — prose, crop dynamics, the ruling

**Fable's four specimens, each reproduced here by measurement:**

1. **C#1's species reborn inside C#1's repair.** The repaired
   boundary bullet in PROOFS.md reads "nothing here proves S3" — in
   the crate whose Zi.lean proves the S3 layer (`pentagon_forces_sq`
   at line 719 of the pinned file; the stale bullet at PROOFS.md:461,
   both re-measured here). The trap's signature move: the prose
   snapshot ages while the file grows.
2. **The scope prose overclaims — and the correction splits.**
   Zi.lean:923's comment calls the (1,1,1)-slice restriction "a
   hypothesis of the mathematics," while `exactly_two_in_the_slice`
   carries **no hypothesis** — the scope lives in the name and the
   `Fs` definition's branch structure. Measured false as a
   description of the statement; defensible as a description of the
   definitional scope. Fable's split — repair the comment, keep the
   design — matches what the measurements support. (For the
   cross-lineage record: their scope-in-the-name and my
   hypothesis-carrying slice lemma are two solutions to the same
   honesty problem, and both verifiers accepted both.)
3. **The slice comment drops its own qualifier** further up the same
   file — same species as #2, smaller.
4. **929 vs 930** — confirmed above, third consecutive off-by-one in
   the size line. Their chartered repair (the size line becomes a
   computed view) is the species-level fix; my PIN-TRACKER records
   sizes only inside sha256-pinned receipts for the same reason.

**Q8 ruled, route (b):** the units classification descends to Nat via
`Int.natAbs_mul_self`, where the successor case closes structurally —
no order lemmas on Int, no second modulus. The honesty clause Fable
attached (omega on Nat reasons with order internally; the abstention
is exactly "the mathematical engine invokes no order lemmas on Int
and survives transport to orderless rings") is the same distinction
my S2 report's order-prong verification was built to exhibit — the
two lineages have now converged on the *statement of the fork*, not
just the mathematics.

**S4 is GO in their lineage** (hexagon: 8 admissible of 16, 5/2/1,
R² = f forced, both hexagons on units, the ±2 controls). My sealed S4
layer proved the same skeleton. When their S4 arrives, the map in
Phase B gains its next row, and P7's successor prediction is already
forced by this round: I will predict the fractions separately per
lineage, not jointly — the fork is style, and style doesn't converge
by proving the same theorems.

## What emerges

Three rounds of the protocol now show a stable decomposition. **What
converges:** the mathematics (statement for statement at every
layer), the controls' content, the corrections law (prose ages, files
don't; the size line misses by one in both houses' ledgers), and now
even the meta-mathematics (the exact wording of the order-abstention
fork). **What does not converge:** build hashes (four of four),
naming conventions, plumbing style — and therefore axiom footprints,
which this round proves are a function of style once the content is
decidable. A census is a portable certificate of *what was assumed*;
it is not, and this round is the demonstration, a certificate of
*what was mathematically necessary*. The necessary part is what the
two lineages keep agreeing on without contact.

---

*Files: `convergence/DESIGN-NOTE-S3.md` (predictions, pre-registered),
`convergence/mech/` — `their_s3_Zi.lean`, `their_s3_statements.txt`,
`compile_s3_out.txt`, `census_their_s3_out.txt`, `census_s3_cold.txt`,
`verify_theirs_s3.py`, `verify_theirs_s3_output.txt`,
`plant_s3_out.txt`, `fable_s3_verification.md`. Their .olean measured
at `c398c20d…` (recorded, not shipped — Q4 series). All pins in
PIN-TRACKER.md.*
