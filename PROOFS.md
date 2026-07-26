# PROOFS — Circle Two's ledger

*Cumulative, round over round, the third body's own. Circle One's
capstone is sealed in its own repository and is the pattern, not the
instance. Norm 6 applies to this file: every count below names the
instrument that produced it, and where a number is an estimate it says
so. Opened at round 2 with S1.*

---

## The pins for this delivery

```
source     lean/Zi.lean
           593a223fcead9816989e9d18986aa7053f3f292dd36d4e79634e0bd4ec3c2594
toolchain  lean/lean-toolchain  -> leanprover/lean4:v4.32.0
           2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e
measured   Lean (version 4.32.0, x86_64-unknown-linux-gnu,
           commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35, Release)
olean      9a95f4c7b82bc20712ac9240c6f9950e0bea25a1bdc3340a508e44b231ef1747
           (not committed — a build artifact; audit/c2_tree.sh exits 1 on
            a tracked .olean. Byte-reproducible across builds on this
            machine. Cross-machine reproducibility is now measured FALSE —
            see Q4, answered.)
```

Full measurements, including every plant fired, in `lean/TRANSCRIPT.txt`.

*This block was stale too — the third site of the same defect, and the
last one found. The source and `.olean` hashes above stood at an earlier
head across several crates, exactly as they did in the artifact's header
and in the transcript. It is ungated for the same structural reason those
were: the numeral gate strips fenced blocks, which is right for code and
wrong for a pin. **A wrong pin in the record is the courier protocol's own
species, and this tree was carrying three of them at once.** Re-measured
on this container and rewritten; see the repairs-pass corrections.*

## S1 — the Z[i] ring layer: DELIVERED

The charge: Z[i] as integer pairs, one law `i² = −1`, the commutative-ring
laws in the hand-rolled zero-import style, `conj` as a ring hom fixing the
first coordinate, `z · conj(z) = (N(z), 0)`, and N multiplicative by
Brahmagupta–Fibonacci as a ring identity. All delivered.

**The figures are a VIEW, not a sentence.** They live in `VIEWS.md`,
rendered from the artifacts by `audit/c2_views.sh`, and `check` fails if
they drift. This paragraph deliberately states no count: four hand-typed
counts went stale in one round — 593/594, 929/930, "twelve live instances"
when there were seventeen, and a boundary bullet that denied a section the
same file had delivered, twice, the second time inside the commit that
repaired the first. Circle One's law for that species is that a count is a
view. See `VIEWS.md` for theorems, definitions, lines, live instances,
controls, the section inventory, and the census.

The three census parts sum to the whole. A census whose parts do not sum
to its total is not a census, so the sum is stated rather than left to the
reader.

### The families, and what each rests on

| family | theorems | certificate check |
|---|---|---|
| extensionality (the coordinate split both ways) | `ext`, `ext_iff` | — structural; nothing in the certificate speaks to it |
| additive abelian group | `add_comm`, `add_assoc`, `add_zero`, `zero_add`, `add_neg`, `neg_add`, `neg_neg`, `sub_self` | **none — see correction #4.** Inherited componentwise from `Int`, proved here directly |
| commutative monoid | `mul_comm`, `mul_assoc`, `mul_one`, `one_mul`, `mul_zero`, `zero_mul` | `G2_ring_laws_symbolic` (its first two conjuncts) |
| distributivity, both sides | `left_distrib`, `right_distrib`, `mul_neg`, `neg_mul` | `G2_ring_laws_symbolic`'s third conjunct certifies **`left_distrib` only** — see the builder's crop #1. The other three are licensed by the kernel alone |
| the one law | `I_squared`, `I_squared_add_one` | `G2_i_squared_is_minus_one` |
| conjugation as a ring hom | `conj_add`, `conj_mul`, `conj_conj`, `conj_one`, `conj_zero`, `conj_re`, `conj_I` | `G2_conj_is_a_ring_hom_symbolic` certifies **`conj_add` and `conj_mul` only** — its two tested conjuncts. The involution appears in that check's printed message, not its boolean; the rest are kernel-licensed. See the builder's crop #1 |
| the norm | `mul_conj`, `conj_mul_self`, `brahmagupta_fibonacci`, `norm_mul`, `norm_conj`, `norm_one`, `norm_zero`, `norm_I`, `norm_re` | `G2_z_times_conj_is_norm_symbolic`, `G2_brahmagupta_fibonacci_symbolic` |
| anti-vacuity live instances | `live_1` … `live_8` | norm 3 |
| negative controls | `control_one_ne_zero`, `control_conj_ne_id`, `control_fake_mirror_is_additive`, `control_fake_mirror_fails_multiplicative`, `control_split_has_zero_divisors`, `control_split_first_factor_is_nonzero`, `control_split_second_factor_is_nonzero`, `control_mul_of_same_factors_is_nonzero` | `G4_control_fake_mirror_fails`, norm 5 |

### Anti-vacuity — norm 3

Exactly one theorem in S1 is guarded by hypotheses: `ext`, which takes the
two coordinate equations. Its guard is satisfiable (take z = w), so it is
not vacuous; every other theorem binds data rather than proofs, and so
cannot be vacuous at all. The live risk is the other one — that the
definitions do not compute what the prose claims — and eight live
instances answer it, each an exact kernel evaluation and none a
restatement of a theorem proved above: `(3+i)(2−5i) = 11−13i`, `(1+i)(1−i)
= (2,0)`, `N(3+4i) = 25`, multiplicativity on a concrete pair, a
conjugation, a norm-as-product, an additive inverse, and `(2i)(3i) =
(−6,0)`. S2 adds four more (below), for twelve in all.

*Amended after the builder's pass (its crop #3): the first witness used to
be `mul I I = (−1,0)`, which is `I_squared`'s statement definitionally — a
probe file proves the old `live_1` with `I_squared`'s proof term verbatim,
exit 0, measured here. So "none of them a restatement" was false of the
very first one. Replaced with an evaluation no theorem in the file proves.*

### Negative controls — norm 5

Four families of them; the control-theorem count is rendered in `VIEWS.md`
and is not retyped here (norm 19, and rule (n2) of the numeral gate now
enforces it).

- **the ring is non-trivial** (`one ≠ zero`);
- **the mirror is not the identity** (`conj i ≠ i`);
- **the fake mirror** `(a,b) ↦ (a, 2b)`, proved *additive* and proved
  *not multiplicative* — both halves, so the control convicts a genuine
  near-miss rather than a straw man. This is `G4_control_fake_mirror_fails`
  in the kernel;
- **the sign is load-bearing**. With `i² = +1` (the
  split-complex multiplication) the same carrier acquires zero divisors:
  `(1+j)(1−j) = 0`, with **each factor separately proved non-zero**, while
  under the real multiplication those same two factors have product
  `(2,0)`. S2's domain theorem is therefore a statement about the sign,
  not about pairs of integers, and this is why it will not come for free.

## S2 — the domain, by one mod-4 descent: DELIVERED

Approved route: the **order-free descent**, not the `Int`-order one-liner.
The fork is labelled in the file rather than taken silently — the order
route is named, its three-line proof described, and the reason it is not
taken given.

| family | theorems | certificate check |
|---|---|---|
| squares mod 4 | `sq_mod_four` | `G2_squares_mod_4` (nest 4) — its tested boolean is the SET fact `{(x*x)%4} = {0,1}` |
| the even/odd refinement | `sq_mod_four_zero_of_even`, `sq_mod_four_one_of_odd` | **none.** `G2_squares_mod_4` states `0,2 -> 0; 1,3 -> 1` only in its printed message, not its boolean — see the builder's crop #5 |
| the sixteen cases, split in two | `re_even_of_norm_mod_four`, `im_even_of_norm_mod_four` | `G2_16_case_decide` (nest 16) |
| **the mandatory mod-2 control** | `control_mod_two_insufficient` | `G2_control_mod2_insufficient` |
| the mod-4 rejection of the same pair | `control_mod_four_rejects_odd_pair` | `G2_16_case_decide` — the mod-2 check's boolean is purely mod 2 and licenses nothing about modulus 4; see the builder's crop #4 |
| the descent measure | `natAbs_two_mul`, `descent_bound` | `G2_descent_step_strictly_decreases` — it tests the measure inequality on a box, and nothing else |
| the quartering identity | `norm_quarters` | **none.** The quartering appears in no tested boolean; kernel-licensed only — see the builder's crop #3 |
| the descent's conclusion | `norm_zero_forces_zero`, `norm_ne_zero_of_ne_zero` | `G2_norm_zero_forces_zero` |
| torsion-freeness and the scalar action | `scalar_is_mul`, `torsion_free` | `G2_torsion_free` |
| **the chain: Z[i] is a domain** | `no_zero_divisors`, `mul_eq_zero_iff` | `G2_no_zero_divisors_box` |
| S2 live instances | `live_9` … `live_12` | norm 3 |
| S2 controls | `control_norm_mod_four_is_not_norm_zero`, `control_split_is_not_a_domain` | norm 5 |

**How the descent avoids the order.** Squares mod 4 are `0` or `1`, proved
by reducing `a·a % 4` to `(a%4)·(a%4) % 4` with `Int.mul_emod` and deciding
the four residues — so no nonlinear reasoning happens anywhere. A norm
divisible by 4 therefore forces both coordinates even, and that conclusion
is proved as **two separate theorems** rather than one conjunction, because
a conjunctive goal handed to `omega` is this house's twice-bitten trap.
Halving quarters the norm, and `Int.natAbs` of the halved pair is strictly
smaller, so an ordinary structural induction on a `Nat` bound closes
`N(z) = 0 ⟹ z = 0` — the induction is on a bound carried as a parameter,
not well-founded recursion, which keeps the proof term small. Then the
chain: `z·w = 0 ⟹ conj(z)·(z·w) = 0 ⟹ (N(z),0)·w = 0 ⟹ w = 0`, each link
a theorem above.

**The mandatory control, as charged.** `(1,1)` has norm `2 ≡ 0 (mod 2)`
with both coordinates odd — so the mod-2 analogue is false and a mod-2
descent halts at its first step. Two ramifies in Z[i]; the modulus 4 is
load-bearing, and the file proves it rather than asserting it. A second
control shows the same pair is *rejected* mod 4, which is why the descent
makes progress where its mod-2 shadow cannot. A third shows that a norm
merely `≡ 0 (mod 4)` does not make the element zero — the descent needs
the full equation, not the congruence. A fourth shows the chain fails in
the split ring, where `conj(z)·z` is not the norm.

**What S2 does not prove.** Nothing about the pentagon, and nothing about
exactly-two. `mul_eq_zero_iff` is stated in the shape S3 will consume, and
that is the only forward reference.

## S3 — pentagon necessity, and exactly two IN THE SLICE: DELIVERED

The pentagon's sixteen instances are classified in the kernel, the one
that forces is isolated, and the two roots are forced through S2's
domain.

| family | theorems | certificate check |
|---|---|---|
| the F-symbol and the pentagon's two sides | `Fs`, `pentLhs`, `pentRhs` (definitions) | index conventions from the bench, cited by line |
| the fifteen non-forcing instances | `pent_0000` … `pent_1110` | `G1a_pentagon_16_instances_classified` — eleven read 1 = 1, four read f = f |
| the one that forces | `pent_1111_lhs`, `pent_1111_rhs` | `G1a_forcing_instance_is_1111_f2_eq_1` |
| pentagon ⟺ f² = 1 | `pentagonHolds`, `pentagon_forces_sq`, `sq_gives_pentagon`, `pentagon_iff_sq` | both directions proved; the reverse is what makes the forward one content |
| the factorization | `factor_sq_sub_one` | `G3a_factorization_symbolic` |
| the algebra it needs | `sub_eq_zero_iff`, `add_eq_zero_iff_eq_neg` | kernel-licensed |
| **exactly two** | `exactly_two_roots`, `one_ne_neg_one` | `G3a_both_roots_land`; the "no third root" is S2's `mul_eq_zero_iff` |
| anti-vacuity: both roots really satisfy the pentagon | `pentagon_holds_at_one`, `pentagon_holds_at_neg_one` | norm 3 |
| **mandatory control: Z/8** | `control_Z8_has_four_roots`, `control_Z8_other_four_are_not_roots` | `G3a_control_Z8_four_roots` |
| **mandatory control: f = i** | `control_f_eq_I_fails_pentagon`, `control_I_is_not_a_root` | `G1a_control_f_eq_i_fails_pentagon` |
| the slice, made machine-visible | `Fs_normalized_off_111`, `Fs_one_of_zero_label`, `exactly_two_in_the_slice` | see Q7 below |
| S3 live instances | `live_13` … `live_17` | norm 3 |

**The classification, reproduced before it was formalised.** Computing the
sixteen instances from the bench's own plumbing gives eleven reading
`1 = 1`, four reading `f = f`, and exactly one forcing — at `(1,1,1,1)`,
where the left side is `f²` and the right side is `1`. That matches the
certificate exactly, and the fifteen non-forcing instances are theorems
holding for **every** `f`, with no hypothesis at all.

**Why the two controls matter.** Z/8's four roots say exactly-two is a
*domain* theorem, not arithmetic luck — the same equation, a different
ring, twice as many answers. And `f = i` is rejected: `i² = −1 ≠ 1`, so
the pentagon really does exclude something.

**Q7, answered honestly and in the kernel.** The every-class-meets-the-
slice lemma is **not proved this round.** Rather than carry that in prose,
the scope now lives in the statements: `Fs_normalized_off_111` proves the
family lies in the normalized slice, and the headline is named
`exactly_two_in_the_slice`. Nothing in this delivery writes
`H³(Z₂) = Z₂`, and nothing may upgrade the headline until the lemma
exists. **That was the state at S3, and it is superseded: the SYMBOL form
of the lemma is proved in the slice entry below** — every unit-valued
pentagon symbol is gauged onto the slice — while the CLASS form still
waits on the gauge equivalence relation, which no section builds. The
licence above is spent to exactly that extent and no further; this
sentence exists because a reader arriving here could otherwise cash a
dangling permit, which the builder measured as a live risk. Where it stalls, precisely: the natural route needs the units of
Z[i] classified as `{±1, ±i}`, and the order-free half of that (ruling out
`N(u) = −1` by squares mod 4) I have; the other half (`a² + b² = 1` forces
a unit coordinate) wants either `Int`'s order or a second descent, and I
would rather ask than smuggle an order into a circle that just spent a
section avoiding one. That question is Q8.

## The units of Z[i] — Q8, route (b): DELIVERED

The builder ruled route (b) — order-free, bridging to `Nat` — and supplied
the route. The `Nat` core (`succ_sq_expand`,
`nat_sq_eq_one`, `nat_sq_sum_one`), the bridge (`natAbs_eq_one_iff`,
`norm_as_natAbs`, `int_eq_one_or_neg_one_of_mul_one`), the classification
(`norm_one_classification`, `norm_ne_neg_one`, `norm_one_of_unit`,
`units_are_four`), three live instances and two controls.

**The units of Z[i] are exactly `{1, −1, i, −i}`**, proved both directions:
forward by the norm, backward by exhibiting each partner. No box, no bound,
no second modulus — `x² + y² = 1` in `Nat` is settled by casing on zero or
successor, and the successor case dies because a sum of naturals is zero
only if each part is.

**The abstention, restated exactly** (the builder's honesty clause, adopted
in substance and written into the file): `omega` on `Nat` reasons with order
internally, and `Nat`'s induction is inseparable from its ordering. What
this circle bought in S2 and keeps here is narrower and precise — *the
argument's mathematical engine invokes no order lemmas on `Int`, and the
proof survives transport to settings where the ring carries no order*. Said
once, in the section header, so route (a) stops being a temptation: the
distinction is not "no order anywhere", it is "no order on the ring".

**What this unblocks, stated as a dependency rather than a promise.** The
slice mini-section *requires* the unit classification; the S3 headline's
machine-visible scope *can* graduate to a proved lemma once that lemma
exists. Neither sentence says when.

*An earlier version of this paragraph said the slice was "the next crate,
with S4". S4 shipped without it, and this ledger — three sections below —
recorded the delivery without noticing that the promise above had gone
stale. A forward-looking promise inside a cumulative record is a defect
with no renderer to catch it: the views mechanism can check a count, not a
plan. That is norm 18, adopted below.*

## S4 — hexagon necessity, and the catalog of four: DELIVERED

The braiding adds `R`; the hexagon has sixteen loop assignments of which
**eight are admissible**; and given the pentagon its entire content is one
equation.

| family | theorems | certificate check |
|---|---|---|
| the braiding symbol and the two sides | `Rs`, `hexLhs`, `hexRhs` (definitions) | bench conventions, `hex_residual_z2` cited by line |
| the seven non-forcing admissible instances | `hex_0000` … `hex_1100` | `G1d_hexagon_8_instances_classified` — five read 1 = 1, two read R = R |
| the one that forces | `hex_1111_lhs`, `hex_1111_rhs` | `G1d_forcing_instance_is_111` |
| the reduction identity | `reduction_identity` | `G1d_reduction_identity` |
| **hexagon + pentagon ⟺ R² = f** | `hexagonHolds`, `hexagon_forces_Rsq`, `Rsq_gives_hexagon` | both directions |
| the two square roots, by class | `Rsq_one_iff`, `Rsq_neg_one_iff` | `Rsq_neg_one_iff` stands on `units_are_four` — Q8's whole purpose |
| **THE CATALOG OF FOUR** | `catalog_of_four` | `G1d_catalog4_satisfies_BOTH_hexagons` (the primary hexagon; see the boundary below) |
| **mandatory controls** | `control_I_over_boson_fails`, `control_one_over_fermion_fails`, `control_hexagon_rejects_I_over_boson`, `control_hexagon_rejects_one_over_fermion` | `G1d_controls_wrong_R_per_class` |
| S4 live instances | `live_21` … `live_24` | norm 3 |

**Exactly four `(f, R)` pairs** satisfy pentagon and hexagon together:
`(1, 1)` and `(1, −1)` — the boson and the fermion — and `(−1, i)` and
`(−1, −i)` — the semion pair. Proved as an iff, so the four are exactly
four and not merely at least four.

**The classification was reproduced before it was formalised**, from the
bench's own plumbing: eight admissible, five reading `1 = 1`, two reading
`R = R`, one forcing at `(1,1,1,1)` where the left side is `f` and the
right is `f²R²`. That matches the certificate exactly.

**The controls say the classes do not accept each other's particles:**
`R = i` over `f = 1` fails and `R = 1` over `f = −1` fails, each stated
twice — once as arithmetic and once as a hexagon rejection.

**BOUNDARY, stated because the charge asked for both hexagons.** This
section imposes the primary hexagon only. The `R⁻¹`-form is equivalent on
units, and `units_are_four` now supplies exactly the fact that equivalence
needs — but the second hexagon is **not** written here, so
`catalog_of_four` is a theorem about the primary hexagon. Nothing in this
delivery may say "both hexagons"; the next crate either adds the second or
the boundary stays.

## The second hexagon — the boundary RETIRED, not restated

*(Section theorem counts are rendered in `VIEWS.md`, per norm 19 below —
this paragraph states none, and this time that is true. An earlier version
said "Twelve theorems"; the repair that removed it restated the true count
twice in the same breath, which the builder caught. The view has the
number; this paragraph points at it.)*

On a unit the inverse is the conjugate — `mul u (conj u) = (N(u), 0)` from
S1, `N(u) = 1` from Q8 — so `conj R` is entitled to the name `R⁻¹`, and
`hexInvHolds` is *stipulated* as the R-hexagon read there. No new plumbing,
no new admissibility, and **no second set of the eight case-instances** —
the case analysis is inherited through `hexagonHolds`. The qualifier is
load-bearing: this section does add three live instances, and "instances"
is a counted category in the views.

**`catalog_of_four_both_hexagons`**: imposing the R-hexagon **and** the
R⁻¹-hexagon yields exactly the same four pairs. That is the certificate's
"no extra root cost" (`G1d_catalog4_satisfies_BOTH_hexagons`) proved rather
than quoted, and it is what discharges S4's boundary. The theorem `catalog_braidings_are_units` records that each of the four
braidings is a unit whose inverse is its conjugate.

**Controls**: `control_non_unit_breaks_the_bridge` shows the NAMING
equivalence — `conj R` deserving to be called `R⁻¹` — is about units and
not about everything: `1 + i` has norm two, so its conjugate is not its
inverse. The catalog equivalence is a different thing and is a theorem;
saying which one is meant is repair H#3a. And the wrong-class rejection
survives the inverse form.

**Section 12's scope sentence stays**, now that the boundary is discharged
elsewhere: a boundary retired in another section is not a boundary that was
never there, and the file says which section imposes what.

## The slice — every UNIT-VALUED pentagon symbol is gauged into it: DELIVERED

The charged lemma. S3 proved exactly two solutions **in the normalized
slice** and said, in the file and in the theorem's own name, that nothing
there showed a general F-symbol could be brought into the slice at all.
That gap is closed, and the file now says which gap is left.

**The language is not a new language.** A general F-symbol is `Fgen F` —
the three free labels carry the value, and the symbol vanishes off the
admissible locus. `Fs_eq_Fgen` proves `Fs f = Fgen (sliceCore f)` by
`rfl`; `pentLhs_eq_gen` and `pentRhs_eq_gen` carry the same `rfl` to the
pentagon's two sides; and `genPentagon_slice_iff` is `Iff.rfl`. **The
general pentagon restricted to the slice family is not equivalent to S3's
pentagon — it is the same proposition.** That is deliberate: the one
sentence a reader would most want to check ("is this really the same
pentagon?") is answered by definitional equality rather than by prose.

**What the pentagon fixes before any gauge is chosen.** Five of the eight
free values are pinned by five single label assignments: `gen_000`,
`gen_010`, `gen_011`, `gen_110`, `gen_101`. Each is read off one instance
and closed by `units_are_four` — the unit classification IS the case
analysis, which is where Q8 does this section's work, and it is the
coupling the builder's standing prediction was aimed at.

**The gauge is written down, not asserted to exist.** `gaugeAct` is the
2-cochain action — two gauge factors up, two down — and `gaugeOf F` reads
two of its four values straight off `F`. The down slots use `conj`, which
is the inverse *exactly on units*: `mul_conj_eq_one_of_unit`, section 13's
bridge, now load-bearing in a second section. That is the repair the
builder pushed for in the last crate earning its keep in this one.

| theorem | what it says |
|---|---|
| `gauge_normalizes` | off `(1,1,1)` the gauged symbol is `one` — that is what "lies in the slice" means |
| `gauge_root_sq` | the surviving slot squares to `one` |
| `every_pentagon_symbol_meets_the_slice` | **the charged lemma**: an explicit unit gauge carries every unit-valued pentagon symbol onto `sliceCore f`, with `f² = 1` |
| `gauged_symbol_is_Fs_on_labels` | the same in S3's vocabulary: on label triples the gauged symbol IS `Fs f`, for `f = 1` or `f = −1` |
| `gauged_symbol_satisfies_pentagon` | the GAUGED symbol satisfies the pentagon — the subject of the statement is now the subject of the sentence |
| `boson_stays_boson`, `fermion_is_not_a_gauged_boson` | no unit gauge carries the boson onto the fermion |
| `fermion_stays_fermion`, `boson_is_not_a_gauged_fermion` | and none carries the fermion onto the boson — the twin, built after the builder measured "the two do not collapse" as prose symmetry over a one-way theorem |
| `genPentagonHolds_congr` | agreement on the labels is all the pentagon can see, which is the step that lets the next row name the gauged symbol |

**Anti-vacuity, norm 3, and it is load-bearing here rather than
ceremonial.** If every pentagon symbol were already normalized the charged
lemma would be true by accident. `twistedBoson` is a unit-valued
pentagon-satisfying symbol that is **not** in the slice (`live_29`
evaluates a non-`one` value at a slot the slice forces to `one`), and
`twistedBoson_is_a_gauged_boson` carries it in.

**Negative controls, norm 5.** `control_gauge_needs_the_pentagon`: a
unit-valued symbol whose own gauge does *not* normalize it, so the pentagon
hypothesis is doing work rather than decorating the statement.
`control_fakeCocycle_is_not_a_pentagon` names why it fails, through the
very relation `gen_011` extracts.

**THE GRADUATION, stated as narrowly as it is proved.** The headline
`exactly_two_in_the_slice` did **not** get stronger and its name did not
change. What exists now is a pair: that theorem says the slice holds
exactly two, and this section says every unit-valued pentagon symbol is
gauged onto the slice and that the two do not collapse. The graduation is
the conjunction of two theorems, not a wider reading of either, and the
artifact says so at both ends — the headline's docstring and, since the
builder measured its absence, section 14's own header — so that no later
sentence can quote one as if it had widened. When this sentence was first
written only one end carried it; the repair built the missing end rather
than shrinking the claim.

**THE BOUNDARY, and it is the reason no theorem here says "class".**
`gaugeAct` is not proved to be an EQUIVALENCE relation — composition and
inversion of gauges are not built. So the theorem is
`every_pentagon_symbol_meets_the_slice`, and no theorem name in the file
carries the word "class": the builder charged the lemma under that word,
and the word the artifact earned is "symbol". The gap is one proof, not one word. And
nothing here computes `H³(Z₂, ·)` or any named cohomology group; the two
theorems do not add up to that without the identification the missing
proof would supply.

## The mirror — the Galois filter, and the catalog closes at two: DELIVERED

The charter's charge, quoted rather than paraphrased: *"The flatland
filter is a Galois statement: on units, u⁻¹ = conj(u), so the roomy edict
R = R⁻¹ is literally conj(R) = R — and its fixed points among the four are
exactly boson and fermion. 2 classes × 2 particles = 4, filtered to 2.
Tie every count to its nest."*

**"Literally" is discharged, not quoted.** `selfInverse_iff_mirror_fixed`
proves that on a unit the roomy edict and the Galois condition are the
same condition, both directions through `mul_conj_eq_one_of_unit`.
Section 13's bridge — the one the builder refused to let me shrink the
prose around — is now load-bearing in a **third** section.

**The cut, stated twice on purpose.** `catalog_filtered_by_mirror` takes
the hypothesis as `conj R = R`; `catalog_filtered_by_roomy_edict` takes it
as `R = R⁻¹`. The charge says these are the same cut, so the file proves
the same two survivors under each rather than asserting the equivalence
and using one.

**The nest, tied.** `catalog_over_f_one` and `catalog_over_f_neg_one` give
the four as two over each pentagon class. `mirror_keeps_nothing_over_f_neg_one`
shows the filter takes **both** from the first class and **none** from the
second — the cut is 2 + 2 → 2 + 0, not one per class, and that asymmetry
is the mathematics rather than an accident of bookkeeping.

**The structural difference from Circle One, in the kernel.** Circle One's
σ moved BETWEEN pentagon classes — golden and Yang–Lee are conjugates over
different classes. Here `conj` FIXES both classes and swaps within the
`f = −1` fibre: `mirror_fixes_the_survivors`, `mirror_swaps_the_semions`,
and `catalog_closed_under_mirror` — the last proved through
`catalog_of_four_both_hexagons`, so section 13 pays a second time.

| theorem | what it says |
|---|---|
| `selfInverse_iff_mirror_fixed` | on a unit, `R = R⁻¹` **is** `conj R = R` |
| `units_fixed_by_mirror` | the mirror fixes exactly `{1, −1}` among the four |
| `catalog_filtered_by_mirror` | pentagon + hexagon + mirror ⟺ exactly two pairs |
| `catalog_filtered_by_roomy_edict` | the same two, with the edict written `R = R⁻¹` |
| `catalog_over_f_one`, `catalog_over_f_neg_one` | the four as 2 + 2 |
| `mirror_keeps_nothing_over_f_neg_one` | the cut is 2 + 0, not 1 + 1 |
| `catalog_closed_under_mirror` | the mirror acts on the catalog and fixes `f` |

**Anti-vacuity, norm 3.** Both halves evaluated: `live_33`/`live_34` are
survivors, `live_35`/`live_36` are the pair the mirror moves.

**Negative controls, norm 5.** `control_mirror_fixes_a_non_unit`: `⟨2,0⟩`
is fixed by the mirror and is *not* self-inverse, so the unit hypothesis
in the Galois reading is load-bearing rather than decorative.
`control_semion_fails_the_filter` exhibits a catalog member the filter
removes.

**THE WORD "PARTICLE" IS NOT EARNED AND IS IN NO THEOREM NAME.** What is
proved is about PAIRS `(f, R)` of Gaussian integers. "Boson", "fermion"
and "semion" are names the physics attaches; nothing here establishes that
a pair is a particle, that particles exist, or that the naming is right.
The charge's "2 classes × 2 particles = 4" is, in this file, a count of
pairs, and the nest lemmas tie it to that. The builder's standing
prediction for this crate was aimed at exactly this noun; the section
header states the boundary before the prediction could land on it, which
is the only defence the ordering rule allows.

**THE BOUNDARY.** This is a statement about `Z[i]` with this file's
F-symbol family and hexagon — not about flatland, not about the roomy
world as such. And no theorem says `conj` generates `Gal(Q(i)/Q)`; it is
exhibited and used, and nothing below needs more.

## Corrections — loudest first

*All of the below were found by an adversarial audit of this delivery —
five parallel finder seats over five dimensions, each finding then handed
to an independent verifier seat that had to reproduce it from scratch or
refuse it. The ones that survived verification are here. **None of them
was found by the author.** That is the method working, and it is also the
receipt for what a single seat's self-review is worth.*

**#1 — the file's own header lied about its axioms, in both directions.**
`lean/Zi.lean` opened by claiming, as a "measured consequence", that every
theorem depended on `propext` and nothing else — no `Classical.choice`, no
`Quot.sound`, no `sorryAx`. Measured: two theorems
(`brahmagupta_fibonacci`, `norm_mul`) depend on `propext` and `Quot.sound`,
which is `omega`'s footprint on this toolchain, and sixteen depend on no
axioms whatsoever. The sentence was false about the ceiling *and* false
about the floor. Worse, it contradicted `lean/TRANSCRIPT.txt` in the same
delivery, which stated the truth — the defect was one document away from
its own refutation. Worse still, it cited `audit/c2_axioms.sh` as its
authority, and that instrument does not adjudicate `Quot.sound` at all: its
contract reports the ordinary kernel axioms and judges only `sorryAx` and
`Classical.choice`. A claim citing an instrument that cannot check it is
the exact species this workshop exists to kill. Four of the five audit
seats found it independently. Fixed: the header now carries the measured
breakdown and states that the parts sum to the whole.

**#2 — ten of the twenty-one simp lemmas were redundant, under a comment
asserting the opposite as "measured".** The normalisation set carried the
units and annihilators (`Int.add_zero`, `Int.mul_one`, …) plus
`Int.neg_mul` and `Int.mul_assoc`, justified by a comment claiming this
toolchain's default `simp` does not close `a + 0 = a`. Measured, one goal
at a time: `a + 0 = a`, `a * 1 = a`, `0 * a = 0`, `- -a = a` and the rest
*are* closed by a bare `simp` here. The one that is not is `a + -a = 0`.
I had read my own probe's error line as belonging to the goal above it —
the failure was on the cancellation example, not the identity one — and
wrote the conclusion backwards. The set is now eleven lemmas, each
verified load-bearing by removing it and watching the file stop compiling.

*Amended after the builder's pass (its crop #2): this correction's own
accounting was off by one. The pre-repair set at `428a125` carries
twenty-one lemmas, not twenty; ten were removed, not nine; and the
forgotten one is `Int.neg_zero`, named in neither list. Measured here by
set-difference on the git objects: `git show 428a125:lean/Zi.lean` gives
twenty-one, the live file gives eleven, the difference is ten and contains
`Int.neg_zero`. The "eleven, each load-bearing" claim survives — the
builder re-verified the eleven individually — but a correction that
miscounts itself is exactly the shape this ledger exists to catch, and it
was caught one document downstream, by the other side of the courier.*

**#3 — half a control was shipped as a whole one.** The old
`control_split_factors_are_nonzero` was plural in its name and singular in
its content: it proved `(1,1) ≠ 0` and never proved `(1,−1) ≠ 0`, while the
file's prose and this ledger both claimed "with both factors non-zero".
Zero divisors require *two* non-zero factors, so the control established
half the condition it was cited for. Fixed by proving both, as
`control_split_first_factor_is_nonzero` and
`control_split_second_factor_is_nonzero` — one line each, which is exactly
what makes the omission worth recording rather than excusing.

**#4 — the additive family cited a certificate check that certifies
nothing additive.** This ledger's table pointed the eight
additive-abelian-group theorems at `G2_ring_laws_symbolic`. That check has
three conjuncts — multiplicative associativity, multiplicative
commutativity, and distributivity — and its additive operation appears only
as an argument inside the third. The verifying seat made the point
decisively by re-implementing the check with the additive operation
replaced by componentwise *subtraction*: the check still passes, while
subtraction is neither commutative nor associative and has no identity or
inverses. The citation licensed nothing. Corrected: the additive laws are
inherited componentwise from `Int` and proved here directly, and the table
says so instead of borrowing authority.

**#5 — three counts were wrong, and one of them is now right for the
wrong reason.** This ledger said "fifteen `decide` proofs" three times; at
the time there were fourteen. It also said removing `deriving DecidableEq`
would affect exactly those; measured, thirteen proofs fail to synthesise
without it. And `lean/Zi.lean`'s section-8 comment said "Four controls, one
per family" while defining seven control theorems across four families.
**The honest part:** repairing #3 added a fifteenth `decide` proof, so
"fifteen" is a true sentence today — but it was false when written, and it
is true now by accident of the repair rather than by measurement.
Recorded so the fix is never mistaken for a vindication.

**#6 — the front door promised plants that two gates' headers do not
carry.** `README.md` said each of the four gates "has a plant recorded in
its own header". `c2_tree.sh` and `c2_axioms.sh` do; `c2_pointers.sh` and
`c2_numerals.sh` did not. Fixed in the direction of more instrument rather
than less prose: the plant recipes are now written into those two headers.

**#7 — three instrument defects, two of which could have failed
silently.** That is the worst class there is; all were reproduced here
before repair:

- `audit/c2_axioms.sh` harvested theorem names with `grep '^theorem '`,
  silently missing `@[simp] theorem`, `private theorem`, and any indented
  declaration — and its own consistency check could not catch the omission,
  because both sides of that check derived from the same grep. A census
  that under-reports without saying so is worse than no census. Fixed:
  comments are stripped first, the declaration pattern tolerates attributes
  and modifiers, and *detection* and *name-extraction* are now separate
  steps that must agree or the census fails loudly.
- the same script's "generated copy did not compile" alarm grepped for
  `error:`, but Lean 4.32.0 reports an unknown constant as
  `error(lean.unknownIdentifier):` — the alarm was **dead for exactly the
  failure this census can produce.** Fixed, then bitten: a two-namespace
  plant now makes it fire (`Unknown constant`, exit 1) instead of silently
  reporting zero theorems and passing.
- `audit/c2_pointers.sh`'s new rule (b2) cross-produced every harvested
  declaration against every namespace in a file, so in a two-namespace file
  `A.two` would resolve when `two` lived in `B`. A single namespace hid it;
  the audit found it anyway. The scanner now tracks the namespace stack.

## Corrections — the builder's pass, seven more

*The builder ran three adversarial seats (the ring, the ledger, the letter)
over the S1 delivery, every finding re-measured by an independent verifier,
none rejected. Seven more specimens — **all prose, none mathematics**, and
two of them living inside the repairs of the first seven. Each was
re-measured on this side before repair; all seven reproduce. Numbered as
the builder numbered them.*

**B#1 — the miscitation species survived its own conviction, twice.** My
audit's correction #4 convicted the additive family of citing a check that
certifies nothing additive. One section over, in both directions, the same
error stood: §5 credited `G2_conj_is_a_ring_hom_symbolic` with "additive
and multiplicative, and an involution", but that check's tested boolean has
exactly two conjuncts and the involution lives only in its printed message
— a printed string is not a check, so `conj_conj` sat under a citation that
did not license it. And §3 cited "the third conjunct" for a section of four
theorems, when that conjunct is **left** distributivity only, leaving
`right_distrib`, `mul_neg` and `neg_mul` undisclosed as kernel-only.
Verified here by reading the check bodies. Both comments and both ledger
rows now say what is certified and what is not.

**B#2 — correction #2 miscounted itself.** Amended in place above:
twenty-one lemmas, not twenty; ten removed, not nine; `Int.neg_zero`
forgotten. Measured by set-difference on the git objects.

**B#3 — `live_1` was a restatement.** Amended in place above; the witness
is replaced.

**B#4 — a control mischaracterised by its own section header.** §8 said
each control "is FALSE of some near-miss and the kernel says so".
`control_fake_mirror_is_additive` is a universally quantified TRUE property
proved by `simp`: its job is to make the near-miss *genuine*, so that its
failure of multiplicativity means something. Good practice, wrong sentence.
The sentence is fixed, not the control.

**B#5 and B#6 — two slips in the S1 delivery letter**, which stays as
couriered; recorded here per norm 13. "A boundary that has now carried a
specimen in each of two consecutive rounds" — both specimens are round 2's
two halves, as `audit/c2_numerals.sh`'s own header states correctly one
directory away. And "the certificate still wants your `C1_LEAN` for its
last two checks" — measured here by ordered replay with `C1_LEAN` absent,
they are checks sixty-eight and sixty-nine of seventy; the seventieth is
pure arithmetic and passes without it.

**B#7 — the meta-finding, now with data from both sides.** My delivery
letter argued that a single seat cannot audit itself. The builder's pass
supplies the second data point: my five seats found seven defects I could
not, and its three seats found seven more that my five did not — including
two inside the repairs themselves. Neither of us finds our own. **The loop
is the auditor**, which is why the register's audit cadence is once per
crate rather than once per author.

**Plus the chartered instrument fix.** On the builder's container the
census failed loudly with `no default toolchain configured`: it compiles
its query copy in a temp directory outside any `lean-toolchain`'s reach, so
its verdict depended on machine state outside the repo. The alarm fired in
the honest direction, which is the repair from my own crop #7 working — but
the dependency is real. Fixed: the census now copies the repo's
`lean-toolchain` beside the generated file, so the pin travels with the
instrument. Re-bitten after the change on both plants (`sorryAx`,
conjunctive-`omega`), per norm 16.

## Corrections — the builder's S2 pass, nine more

*Three seats again, every finding re-measured here before repair. All nine
reproduce. Two were already known to the builder before it audited; seven
were not.*

**C#1 — the ledger delivered S2 and, three sections above, denied it.**
"Nothing here proves S2. No theorem in this file states that Z[i] has no
zero divisors. That is next round's charge" — while `no_zero_divisors`
stood in the same file and the S2 section said DELIVERED. True when
written; nobody re-read it. A stale label in the section named "Honest
labels", contradicting its own document two hundred lines away. The
sharpest specimen this circle has produced, and it cost nothing but a
re-read that never happened. Repaired, and the bullet now states what the
boundary actually is (S3's slice lemma).

**C#2 — my portability fix did not fix the condition it named, and its
falsifier was never run.** The census copied the repo's `lean-toolchain`
beside the generated file — but ran `lean` from the repo root, and a
toolchain manager resolves the pin from the **working directory**, not the
source file's location. So the pin travelled and was never read. Worse:
"re-bitten on both plants, per norm 16" re-bit the *plants*, not the
*portability condition* — the falsifier that mattered was never run,
because this container has no toolchain manager at all and its absence
masked the defect. Norm 14's exact species, inside a sentence about norm
16. **Repaired properly and falsified for real:** the compile now happens
inside the temp directory, and I built a wrapper that behaves like a
manager with no default configured. Before the fix, that wrapper makes the
census fail with `no default toolchain configured`, exit 1; after it, the
census PASSES. Both plants re-bitten under the wrapper too.

**C#3, C#4, C#5 — three more miscitations, exactly where my own prediction
pointed.** The descent row cited two checks for `norm_quarters`, whose
quartering identity appears in no tested boolean; the mod-2 control row
cited `G2_control_mod2_insufficient` for `control_mod_four_rejects_odd_pair`,
though that check's boolean is purely mod 2; and the squares row cited
`G2_squares_mod_4` for the even→0 / odd→1 refinement, which lives only in
its printed message. All three verified here by reading the check bodies.
The S2 table now splits those rows and says, in each case, what is
certified and what is kernel-licensed only. **My prediction, scored
CONFIRMED one crate after I offered it — against my own delivery.**

**C#6 — "the census names every one" — it named two.** The instrument
named offenders only for the two fatal findings; twelve `Quot.sound`
carriers were counted and none was named, while the file header cited the
census for per-theorem answers it did not print. Repaired in the
instrument rather than the prose: the census now prints every
`Quot.sound` carrier by name. Seventeen, at this head.

**C#7 — the size was off by one, in two documents.** "593 lines"; the
artifact measured 594. Repaired.

**C#8 — the `DecidableEq` disclosure pointed at the wrong correction**
(#3, the half-control repair) across three commits. Its homes are ruling
Q1 and correction #5. Repaired.

**C#9 — and a second site of the builder's own B#2**, found here while
repairing: `lean/Zi.lean`'s simp-set comment also said "nine more",
carrying the same forgotten `Int.neg_zero`. Enumerated per norm 13 and
fixed in both places.

## Corrections — the builder's S3 pass, four and a split ruling

*All four reproduced here before repair.*

**D#1 — the stale-label repair recreated the stale label, one section
forward, in the crate that shipped the repair.** The repaired bullet read
"nothing here proves **S3**. No theorem in this file states that the
pentagon forces f² = 1" — while `pentagon_forces_sq` stood in the same
file. Three neighbours staled with it. **Repaired structurally rather than
by hand**, on the builder's charter: counts and scope claims are now a
VIEW. `audit/c2_views.sh` renders `VIEWS.md` from the artifacts and its
`check` fails on drift; the ledger points at it and states no count of its
own. REGISTER row 11 names the class. Four stale counts in one round bought
this instrument, and one of the four was created by the commit repairing
another — which is the argument for rendering rather than watching.

**D#2 — the scope prose overclaimed, and the correction splits.** "That
restriction is a hypothesis of the mathematics" — false:
`exactly_two_in_the_slice` takes `(f : GZ)` and no hypothesis at all. But
the builder's own half is the more useful one: the restriction is
**definitional**, not hypothetical — `pentagonHolds` is a statement about
the family `Fs f` by construction, and `Fs_normalized_off_111` proves that
family lies in the slice. A reader who unfolds the definition finds the
restriction enforced rather than advertised, which is a *stronger*
machine-visibility than a named hypothesis, not a weaker one. The builder
corrected its own Q7 ruling to match, since that ruling prescribed a route
this construction does not take. The prose now claims what is true, and
says which half of it was wrong.

**D#3 — the slice comment dropped its own qualifier** ("every F-symbol it
produces is `one` unless all three of `a,b,c` are `1`" — off the admissible
locus it produces `zero`), while the doc comment ten lines down kept it and
`live_16` in the same file refutes it. Repaired.

**D#4 — the off-by-one came back in the crate that repaired it.** "929
lines"; measured 930, born stale exactly like 593/594. Same species, same
slot, consecutive crates — and the strongest single argument for D#1's
view mechanism, since the hand keeps missing by one because it types the
number after the file moves.

## Corrections — the builder's units pass, four, and the loudest is the builder's

*All four reproduced here before repair.*

**E#1 — the abstention sentence was defective at birth, and the builder
wrote it.** I adopted it verbatim, which is how the conviction reaches this
ledger. The sentence conceded that tactic-internal order reasoning counts —
for `Nat` — while exempting it for `Int`, and this file's `omega` calls sit
overwhelmingly on `Int`-typed goals, where `omega` reasons with order on
`Int` exactly as it does on `Nat`. Measured here: **zero order lemmas of
either type are cited by name in any proof body.** So under the concession's
own standard the `Int` clause was false; under the named-lemma standard the
`Nat` concession was misdirection. Repaired with one standard, stated once
in the section header: no order lemma on any type is cited by name;
`omega`'s internal order reasoning is licensed wherever `omega` is; what
transports to an unordered ring is the argument's **structure**, not the
tactic scripts. The replacement is weaker than what it replaces, and
honestly so — the old sentence claimed an asymmetry the file does not have.

**E#2 — one control was decoration.** `control_nat_sq_sum_two_differs`
stated `1·1 + 1·1 = 2`: a positive identity that cannot fail, norm 7's exact
species, under a docstring claiming it showed the `Nat` core's conclusion
depends on its right-hand side. Replaced by a control that rules something
out — the pair `(1,1)` satisfies the equation at two **and fits neither
disjunct** of `nat_sq_sum_one`'s conclusion, so that conclusion cannot be
widened to two. The rendered control count now counts a theorem that checks
something.

**E#3 — the boundary sentence claimed to be rendered and was template
prose.** Only the inventory was read off the artifact; the sentence itself
was a fixed `echo` in the renderer, and my delivery letter called it
"rendered". Repaired by derivation: the section count and the last section's
name are now interpolated, so the words change when the artifact changes,
and the renderer's own boundary caveat is carried into the view instead of
living only in the script.

**E#4 — a characterization drift in my units letter**, recorded here per
norm 13; the letter stays as couriered. The builder wrote that definitional
scope is "machine-visible *in a way a name is not*". My letter upgraded that
to "a **stronger** machine-visibility **than a named hypothesis**" and
placed the ranking under the builder's endorsement. The builder never ranked
it, and is right not to: a named hypothesis sits in the statement's type,
visible without unfolding anything. The file's own docstring kept the
correct neutrality; the letter overshot. Sites: the letter's D#2, this
entry.

**And the mechanism the builder chartered for my gate-red commit.**
`audit/c2_gates.sh` chains every instrument into one exit code, and
`.githooks/pre-commit` runs it, so a red gate blocks the commit instead of
advising it. Bitten twice at birth: the runner exits 1 on a planted red
gate, and **the hook refused an actual commit** — I planted a drift, ran
`git commit`, and HEAD did not move. REGISTER row 12 names the class; row
5's boundary now records the honest gap, that a hook lives in the working
copy and not in the commit.

## Corrections — the builder's repairs pass, one and one cosmetic

**F#1 — REGISTER row 12's boundary borrowed class 2's authority.** It said a
wrong instrument passing was "class 2's problem". Class 2 is **Certificate
claims**, covering `c2_gift_certificates.py` alone — so a wrong pointer,
numeral, tree or views instrument was covered by no sentence in the register
at all. Borrowed authority, in the boundary of the mechanism that had just
saved me, one crate after the row was born. Repaired the way the builder
said it should be: not by rewording the clause but by **adding row 13
deliberately** — the gate instruments themselves, adjudicated by each one's
norm-16 plant record plus row 9's audit loop, with the honest boundary that
plants only cover cases somebody thought of.

**F#2, cosmetic** — the rendered caveat read "the renderer own boundary
note". Fixed in the **template**, then re-rendered: one edit site, not two,
which is the view mechanism doing exactly what it was built for.

**Norm 17, adopted.** The builder proposed it after ruling the packing
disagreement in my favour: *a repair and the first thing that depends on it
never ride in the same crate.* It is Circle Two's first appended norm; the
Circle One canon stays frozen at 1–16, so every citation in the sealed
record still points where it did. `NORMS.md` carries it with the measured
reason — the stale-label repair recreated its own defect inside the commit
that shipped it, and the abstention repair was about to ride with the S4
prose that leans on it.

## Corrections — the builder's S4 pass, two and one low

**G#1 — "the boundary is in the file and in the ledger": it was in the
ledger only.** Measured — `lean/Zi.lean`'s section 12 carried no boundary
sentence at all; the only "second" near it was "the second summand". My own
survival clause had said the claim would stand *only* if the boundary were
in the file, and it was not. Seventh consecutive scored prediction, in the
named territory, to the sentence. Repaired twice over: section 12 now
carries its scope statement where it should have been, **and** the second
hexagon is proved, so the boundary is discharged rather than merely
written down.

**G#2 — the ledger promised what its next section failed to deliver.** It
said the slice was "the next crate, with S4"; S4 shipped without it, and the
S4 section three sections below recorded the delivery without noticing. The
views mechanism cannot catch this — a plan is not a count. Repaired to state
the dependency instead of the schedule, with the stale sentence quoted in
place, and generalised as **norm 18: the cumulative record states what is,
never what will be; plans live in letters.**

**G#3, low, recorded as couriered.** My S4 letter said "nothing in this
delivery says 'both hexagons'". As an absolute the crate falsifies it —
the builder's own letters ride inside it restating the charge, and a ledger
row prints the certificate check name with BOTH in it. Nothing claimed both
were *imposed*, so the intent held; the ledger's normative phrasing
("nothing **may** say") was right and the letter's factual flattening
overshot. The letter stays as couriered.

## Corrections — the builder's second-hexagon pass, four

**H#1 — "Twelve theorems"; the section holds nine.** Measured three ways —
a direct sweep, the view's own row, and the census moving by nine. And the
mechanism note that makes it the loudest: it walked through a door the
numeral gate **declares open**, because it is spelled in letters rather
than digits — the second time that exact word has done it in this circle,
the first being "twelve live instances", one of the four stale counts that
bought the renderer. Repaired to no count at all, and generalised as
**norm 19**: a count the views render is never retyped in the cumulative
record — the record points, the view counts.

**H#2 — "no second set of instances", sixty-eight lines above a header
reading "Live instances for the second hexagon".** True under one reading
(no second battery of the eight case-instances was written, and none
exists), false under the artifact's own counted vocabulary: this crate ships
three new live instances. Repaired with the qualifier in the two LIVE
sites — `lean/Zi.lean`'s section header and this ledger. The prescription
named three places the triple appears, and the third is
`letters/ROUND2-HEX2-DELIVERY.md`, which still reads "no second set of
instances" verbatim and always will: a letter as couriered is never edited,
and its instance stands here as a recorded correction under norm 13. The
delivery letter said "qualified in all three sites", which quietly counted
a site that cannot be repaired — a completion claim covering ground the
record cannot deliver. Two sites qualified, one recorded.

**H#3 — the control's docstring denied what the definition stipulates.**
`hexInvHolds` *is* the R-hexagon read at `conj R`, for every argument, unit
or not; that cannot fail. What the control actually shows is that
conjugation fails to invert a non-unit — off the units the definition no
longer deserves its NAME. Repaired to say what it guards.

*Two of this correction's own clauses were wrong, and both were caught by
the builder in the next pass. They are re-corrected below, written
together and deliberately checked against each other, because the second
of them was created by a repair in the same commit as the first — see the
species note at the end of this block.*

**H#4 — the bridge the prose leaned on was used by nothing.**
`mul_conj_eq_one_of_unit` and `catalog_braidings_are_units` had zero
downstream uses while the prose called the bridge the thing the result
"turns on" — dependency vocabulary in a house where load-bearing is a
measured word. Repaired in the direction that makes the prose true rather
than smaller: `catalog_braidings_are_units` is now proved through the
bridge and the unit classification, so the dependency exists in the proof
graph. The section header's "therefore" is gone too — a stipulation is no
longer presented as a derivation.

**H#3a — "there is no equivalence theorem in the file" overshot.**
`catalog_of_four_both_hexagons` is an iff, its own section header frames it
as the certificate's equivalence clause, and its proof runs through
`catalog_of_four` into `Rsq_neg_one_iff` into `units_are_four`. So the
condemned sentence "the equivalence genuinely needs `units_are_four`" was
TRUE under that reading, and the correction convicting it was the wider
error. The narrow claim that is right: no theorem states the NAMING
equivalence — that `hexInvHolds` coincides with a genuine inverse-hexagon;
that is a stipulation. The seed is the builder's ("the equivalence is a
definition, and no theorem in the file states it"), the widening to a
categorical absence is mine, and the record says so in both hands, which
is how the builder asked for it.

**H#3b — "the catalog's real debt to Q8 flows through `Rsq_neg_one_iff`"
went stale inside the commit that wrote it.** Singular channel, measured
true at `21acd79`. The H#4 repair, in the SAME commit, added four direct
uses of `units_are_four` inside `catalog_braidings_are_units`. Two channels
from that moment on. Repaired in the artifact and here: the debt flows
through `Rsq_neg_one_iff` and, since that crate, through the bridge.

**H#4a — the H#4 repair moved the census and no prose said so.** Making the
bridge load-bearing cost `catalog_braidings_are_units` its axiom-freeness:
it now carries `Quot.sound`, and it is the only theorem whose axiom class
changed in that commit — measured here by running the census at both
commits and diffing the carrier lists, not by reading the builder's letter.
The totals are rendered in `VIEWS.md` and are not restated here (norm 19).
The repair record celebrated the direction and never named the price, in a
house where this very file's header was convicted over its axiom footprint.
The price is named now. The option of keeping the kernel evaluation and
stating the derivation beside it exists and is declined for the reason the
builder gave: a dependency in the graph is worth more than a clean census
line, and saying the cost is all norm 6 asks.

**THE SPECIES, named by the builder and ruled on here: repair–repair
interaction.** Norm 17 guards a repair against its dependents ACROSS
crates. Nothing guarded two repairs against each other INSIDE one, and
H#3's singular-channel sentence was made false by H#4 in the same commit.
The ruling: this does not become norm 20. Norm 17's mechanism is a
schedule, and a schedule cannot separate two edits that belong in one
commit; what this species needs is a habit, and the habit is the one the
builder prescribed for this very crate — when two repairs touch the same
prose, write them TOGETHER and say in the letter that you checked them
against each other. H#3a and H#3b above were written that way, in one
edit, and the delivery letter says so. A norm that cannot be mechanised
should not be numbered beside norms that can; this is registered as a
practice, in REGISTER row 15, and not as a law.

## Corrections — the builder's repairs pass, six, and one of my own that is louder

*All six re-measured on this container before repair: the census run at
both commits with the carrier lists diffed, the retyped counts swept by a
new gate rather than by eye, the equivalence claim checked against the
theorem it denied. Then a seventh, which the builder's seat could not have
found because its territory was the diff.*

**MY OWN, and it goes first because it is the largest stale count this
tree has carried.** `lean/Zi.lean`'s header spelled out the entire axiom
census in prose — a theorem total, an axiom-free count, a `propext` count,
a `Quot.sound` count broken down by section, and the line "a census whose
parts do not sum to its whole is not a census". Every figure was stale, and
the header said so of itself in the present tense. It survived every
instrument for a structural reason worth more than the defect: the numeral
gate's territory is the DOCS, the views gate's territory is the rendered
view, and **the artifact's own prose was scanned by neither**. Repaired to
point at the census and state no figure; the gap is closed by the
artifact-prose census guard (REGISTER row 14), bitten in both directions
before it was trusted. Found by re-measuring the file I was editing, which
is the only reason it was found at all — no seat was looking there.

**MY OWN, SECOND, and it is the same seam one file over.**
`lean/TRANSCRIPT.txt` — the file that header points readers at for the
per-theorem answers — was stale in its title (it named three sections), in
its scope sentence and wall-time ("S1 + S2 + S3 together"), in its
**source SHA-256**, in its `.olean` hash, and in a full typed census block
standing under a note that explained why the block was allowed to stay.

And then a THIRD site, found while assembling this crate's pins: the
ledger's own "pins for this delivery" block carried the same stale source
and `.olean` hashes. Three files, one defect, and each ungated for its own
structural reason — the artifact's prose was in no gate's territory, a
plain-text transcript is in none either, and the numeral gate strips
fenced code blocks, which is right for code and wrong for a pin. **A
wrong pin in the record is the courier protocol's own species, and this
tree was carrying three of them at once while every instrument ran
green.** Repaired by re-running the compile and
the census on this container and rewriting every measured line; the census
block now states the two ZEROS the census judges — no `sorryAx`, no
`Classical.choice` — and points at `VIEWS.md` for everything it counts,
because a zero is a verdict and a count is a view. Note the shape: the
transcript is scanned by no gate either — every instrument's territory is
markdown or Lean, and a plain-text file falls outside all of them — so
this repair is a repair and not yet a mechanism, and the register should
not be told otherwise.

**#1 — norm 19 convicted itself at birth; six sites, seven retypes.**
Confirmed, and the sweep found one the builder's list did not: the ledger's
negative-controls section opened "Eight control theorems across four
families". All repaired — the norm's own adoption text, the ledger
paragraph that restated the count twice two clauses after declaring it
stated none, the four section openers, and the fifth opener. The letter's
"Repaired to no count at all" and its preamble's "this letter states none"
were both false as written; the letter stays as couriered and the
correction is here, per norm 13. **The structural proposal is built**: rule
(n2) of the numeral gate now guards spelled and digit counts of rendered
categories in the cumulative record, with its territory, its two rules and
its remaining blind spots declared in the gate's own header.

**#1a — MY OWN, found by measuring the gate I had just written.** The new
rule's header claimed it "watches the part of that doorway where every
specimen has actually walked". I then planted the two specimens the
boundary was actually scored on. It catches "twelve live instances". It
does NOT catch "tracks thirty-one compiled-bytecode files" — that one
lives in a letter, out of territory by design, and its noun is not a
rendered category, so it would escape in territory too. **One of two**,
and the sentence claiming otherwise was written in the same hour as the
gate, which is the shape that has convicted this file four times: a claim
about an instrument, written by the hand that built it, before anything
was measured. Repaired in the gate's header, which now carries the two
plants and their verdicts, and in the transcript. The habit that caught
it is the only part worth keeping: after writing a declaration, plant the
cases the declaration is about.

**#2 — "qualified in all three sites": two, and the third cannot be
repaired.** Confirmed; repaired in the H#2 block above, which now states
the boundary instead of the completion.

**#3 — the equivalence overshoot, and the seed is the builder's.**
Confirmed and repaired in both hands: H#3a above, and the artifact's own
docstring, which now says which equivalence is a theorem and which is a
stipulation.

**#4 — two repairs staled each other inside one commit.** Confirmed;
repaired as H#3b, and the species is ruled on there — a practice, not a
norm, registered at row 15.

**#5 — the census cost of the H#4 repair went unrecorded.** Confirmed by
independent measurement, not by reading the letter: the census at both
commits, carrier lists diffed, one mover named. Repaired as H#4a.

**#6, cosmetic, letter class** — "changing the artifact rather than the
sentence" is an either/or the diff refutes, since H#4 changed both.
Recorded; the letter stays as couriered.

## Correction — a defect INSIDE the numeral gate, found by the merge

*Found after the slice crate was couriered, when PR #3 merged and the
default branch brought in `STATE-OF-THE-RECORD.md` — inherited inventory
prose I did not write. The gate went red on it. The gate was wrong.*

**THE DEFECT.** The numeral gate strips identifier words (class c8) with
two ordered rules: letter-first, then digit-first. On a **digit-leading
hex identifier** the letter-first rule fires on the tail and blanks it,
leaving the leading digits behind as a bare numeral. Measured:
`73a475f3` → `73`; `499ebb8` → `499`. Those are a SHA-256 prefix and a
commit id — the two things this circle's courier protocol is built out
of — and the gate read them as unsourced counts.

**IT RAN BOTH WAYS, and the second direction is the worse one.** The same
ordered pair sits in `harvest()`, which builds the gate's KNOWN set from
the certificate and the weld report. There, that stray leading run does not raise a
false alarm — it enters the known set and would have **sourced a matching
bare number anywhere in the record**. A silent over-acceptance in an instrument whose
whole job is to refuse unsourced numbers. Nothing had exercised it because
no scanned document had put a digit-leading hex identifier in prose until
this one did.

**THE REPAIR is a rule, not an ordering.** In the decision path the two
gsubs are replaced by a single pass over maximal alphanumeric runs: a run
containing at least one letter is an identifier, whatever order its
characters come in. Two ordered rules had a seam; one rule has none. In
the two `sed` paths the digit-first rule now runs first, which fixes the
observed class there. `audit/c2_views.sh` carried the same ordered pair
and got the same reorder.

**RE-BITTEN, because an instrument that changes gets re-bitten and norm 16
has no grandfather clause.** Three plants, two of them new:
a fresh bare `8675309` still FAILS; a line carrying `499ebb8` and
`73a475f3` now PASSES; the clean tree passes. The census guard was
re-bitten too, since it was edited in the same commit.

**WHAT THIS SAYS ABOUT THE REGISTER.** Row 13 covers the gate instruments
themselves — whether each is *right*, not merely green — and lists the
audit loop as its live adjudicator, because "every plant is a case someone
thought of; the defects row 9 found were all in the unplanted remainder".
This is one more from the unplanted remainder, and the thing that found it
was not a seat and not a plant: **it was a document arriving from outside
the loop.** Foreign material is an adjudicator no row names. That is worth
more than the fix.

**And one more miscitation, same species as the last:**
`audit/c2_views.sh`'s header also cited "row-9" for the spelled-out
boundary. Row 8. Fixed in both instruments now.

## Corrections — the builder's slice pass, seven and two transport findings

*All nine re-measured here before repair. Two of them are the two standing
predictions landing in the same crate, which has not happened before —
theirs a tenth consecutive time, mine for the first after three crates
open.*

**T#1 — the crate carried no repository, and it gated everything else.**
Confirmed, and the cause is mine and specific: I built the crate with
`git archive`, which writes a snapshot. Consequences measured on the
receiving side: the head pin unverifiable, the merge and the packing
unverifiable, three instruments refusing outright because they need a
repository, and the pointer gate red on commit ids that resolve only
against history. The builder reconstructed by grafting the files onto its
verified copy of the previous head and got five green gates — the content
was clean and only the transport failed, which is the one piece of luck in
it. Repaired in `COURIER-CARD.md` as rule C1: the crate carries `.git`
every leg; a git bundle if size ever forbids; never a bare snapshot.

**T#2 — the transcript's pin did not ride the supersession.** Confirmed.
The superseding message marked letter, source and views UNCHANGED and said
nothing of `lean/TRANSCRIPT.txt`, which I had changed in the same commit —
the gate-repair story was written into it. The file is better and the pin
discipline is worse. Repaired as rule C2: a superseding message names
every artifact from the first message, CHANGED or UNCHANGED. **Silence is
not a pin**, and this is the courier protocol's own species landing on the
body that has been lecturing about it for four legs.

**#1 — the headline's docstring claimed the CLASS lemma is proved.**
Confirmed at the site: "the every-class-meets-the-slice lemma was not
proved. It is proved now — `every_pentagon_symbol_meets_the_slice`". What
is proved is the SYMBOL lemma; the class form waits on the equivalence
relation this file declines to build, and the crate says so in three other
places. **The builder's first offered prediction, CONFIRMED after three
crates standing**, at the chair it named.

The wrinkle is the finding, and it is not a small one: **my ordering rule
worked, and the defect walked around it.** The theorem compiled first, its
statement never grew, its name never changed — the rule governs those and
it held. The docstring one inch away widened anyway. Mechanism guards what
it names; prose migrates to the nearest unguarded surface. Repaired to
"its SYMBOL form is proved now", with the old sentence quoted in place.

**#2 — "every theorem below assumes units" is false.** Confirmed, and
wider than the four the builder named. Measured: `Fs_eq_Fgen`,
`pentLhs_eq_gen`, `pentRhs_eq_gen`, `genPentagon_slice_iff` carry no unit
hypothesis; neither do `IsUnit_one`, the `twistedBoson` and `fakeCocycle`
facts, the five live instances, or the three controls — those PROVE
unit-ness of a concrete symbol rather than assuming it. And the builder's
sharpest point stands: `genPentagon_slice_iff` genuinely says something
about non-unit symbols, since its `f` is arbitrary and the slice family at
a non-unit value is a non-unit-valued symbol. Repaired to the scoped
clause. **Their prediction, CONFIRMED, tenth consecutive** — in the named
territory, in the bullet they did not name.

**#3 — "the artifact says so at both ends" had one end.** Confirmed by
search: the no-widening sentence existed only at the headline's docstring;
section 14's header stated the division of labour and carried no such
guard. Repaired in the better direction — the missing end is built, in
section 14's header, and the ledger sentence now names both ends.

**#4 — "the two do not collapse" was prose symmetry over a one-way
theorem.** Confirmed: the file forbade boson→fermion and said nothing
about fermion→boson. **The twin is built** — `fermion_stays_fermion` and
`boson_is_not_a_gauged_fermion`, by the same sixteen-way cancellation.
Same choice as the bridge repair two crates back, and for the reason the
builder gave then: build the dependency, do not shrink the sentence.

**#5 — the headings dropped the unit qualifier the theorems carry.**
Confirmed. Section 14's title and this ledger's heading now say
UNIT-VALUED.

**#6 — two names claimed more than their statements quantify.** Confirmed,
and repaired in opposite directions on purpose, because the two gaps are
not the same gap. the theorem formerly named
"gauged_symbol_is_Fs" — quoted rather than pointed at, because the name no
longer resolves and the pointer gate said so — is RENAMED
`gauged_symbol_is_Fs_on_labels`: off the labels the claim is false rather
than unproved, so the restriction is content and belongs in the name.
`gauged_symbol_satisfies_pentagon` is STRENGTHENED: its conclusion now
names the gauged symbol, carried across by a new lemma
`genPentagonHolds_congr` — the pentagon reads its symbol only at triples
whose entries are mod-2 sums of labels, so agreement on the labels is all
it can see. The step the builder measured as "not taken in the file" is
taken.

*One cost of #6, recorded because the gate charged it immediately: renaming
a theorem kills every pointer to it in the couriered letters, which are
primary sources and are never edited. The pointer gate went red on the
builder's own verification letter the moment it entered the tree, and the
old name now carries a labeled exemption saying so. A rename is not free
here; it is paid for in the exemption ledger, once per frozen letter. I
still took it, because a name that is false off its scope is worse than a
dead pointer that is labeled.*

**#7 — the S3 entry's dangling licence.** Confirmed: "nothing may upgrade
the headline until the lemma exists", with no pointer to the entry where
part of it now does. Repaired with a forward pointer that spends the
licence to exactly the extent the symbol lemma earns and no further.

## Corrections — the builder's mirror pass, five, and one I caught in my own closing draft

*All five re-measured at their sites before repair.*

**#1 — the C-rules stratum, four sites. Theirs, CONFIRMED, eleventh
consecutive**, in the territory I named for them one crate earlier.

- REGISTER row 17 said the receiving body "could verify no pin". Their
  letter, in the same crate, says four of five pins verified exact; only
  the HEAD pin was unverifiable. A four-fold widening of a transport
  failure, written while holding the letter that refutes it, in the row
  whose boundary column preaches measurement. Narrowed to the head pin.
- C2 was written for supersessions only, so on the very next ordinary leg
  it imposed nothing and three changed artifacts — `REGISTER.md`,
  `PROOFS.md`, the pointer exemption ledger — rode legally unnamed under
  an aphorism ("silence is not a pin") broad enough to forbid it.
  Extended: every leg names every artifact that changed on it.
- The card's section header said the rules were "added here, not in a
  letter"; C3 was proposed verbatim in their slice letter and adopted in
  the norms. Scoped to the defensible claim: the normative HOME is the
  card.
- **C3 dropped the word "gated"** from norm 20's licence. The norm lets a
  body's own GATED crate merge on its say-so; the card, which is Kelly's
  only runbook, licensed "your own crates" unconditionally. One word, and
  it was the load-bearing one. Restored.

**#2 — the mirror's headline prose. Mine, CONFIRMED, second of two.** The
plant held — "particle" appears in no theorem and the pairs scoping is
exact — and the sentence REPORTING the plant is what broke: "none is in a
name" is false twice in its own section, at `mirror_swaps_the_semions` and
`control_semion_fails_the_filter`. Repaired on their lean, which is the
right one: keep the names, which cite a conventional label for a pair of
Gaussian integers, and scope the claim to what the bullet needs — no name
CLAIMS physics content.

**MY OWN, found by planting against my own closing draft before it
shipped.** The draft said "**the certificate closes 70 of 70, exit 0**"
with no condition. I had not run it on this container. Measured here it
closes 68 of 70: the two G6 calibrators re-measure Circle One's Lean
blocks and need Circle One's tree, which this container does not carry,
so they fail with file-not-found rather than a wrong value. With
`C1_LEAN` set it is 70 of 70, which is the builder's measurement in five
consecutive letters — **their measurement wearing my voice, in a
retrospective.** That is exactly the specimen their standing prediction
named for the closing document, and it existed. It was caught because the
sentence was checked by running the thing rather than by remembering it,
which is the only defence this document has and the reason it says so in
its own preamble.

## Honest labels — the boundaries of this delivery

- **What the kernel checked is what the file says, not what the charge
  meant.** Every theorem here is a statement about `Zi.GZ`, `Zi.mul`,
  `Zi.conj` and `Zi.norm` as this file defines them. That the definitions
  are the *right* ones is licensed by the certificate's symbolic checks and
  by the live instances (`VIEWS.md` counts them), not by the kernel.
- **`omega` is the file's workhorse, and its price is visible.** In S1 it
  appears twice (`brahmagupta_fibonacci`, `norm_mul`); in S2's descent and
  in the units section it does most of the linear work. The theorems that
  carry `Quot.sound` as a result are **named individually by the census**,
  and counted in `VIEWS.md` — an earlier version of this bullet typed the
  count here and it went stale within one crate. `omega` is never aimed at
  a conjunctive goal — every conjunction is split first, which is why
  `Classical.choice` is zero across the whole file. The discipline that matters held —
  `Classical.choice` is zero — and the transcript's Plant B shows the same
  toolchain producing `Classical.choice` the moment an `omega` is aimed at
  a conjunctive goal.
- **The `.olean` hash is same-machine reproducible**, measured; nothing
  stronger is claimed.
- **The boundary is a VIEW now, and this bullet is the record of why.**
  It used to be a hand-typed sentence, and it went stale twice. First it
  said "Nothing here proves S2" after S2 shipped. Then its own repair said
  "nothing here proves **S3**. No theorem in this file states that the
  pentagon forces f² = 1" — while `pentagon_forces_sq` stood in the same
  file, in the same crate that shipped the repair. **The repair recreated
  the defect one section forward.** Three neighbours staled with it. What
  replaced them: `VIEWS.md` renders the section inventory from the file, so
  "what is proved is exactly the sections listed" stays true without being
  re-typed. The species is not being watched for any more; it is being
  rendered out of existence.
- **The audit that produced the corrections above is itself a new
  instrument**, and its first outputs were treated accordingly: every
  finding had to be reproduced by an independent seat, and I re-measured
  the disputed ones myself before repairing anything. One turned out
  sharper than reported (#2: the comment was not merely unsupported, it
  was backwards).

## The prediction, offered for the next round's scoring

**The next specimen will be a count or a citation in S2's descent prose,
not in its Lean.** The reason is visible in this round's own crop: most of
the corrections above are prose *about* the artifact rather than the
artifact itself, the kernel caught none of them because the kernel does not
read prose, and S2 adds a new prose surface — the descent argument, the
mod-4 case analysis, the honest fork — whose numbers nothing yet gates.
`audit/c2_numerals.sh` still cannot see spelled-out numbers, and that
boundary has now carried a specimen in each of **round 2's two halves** —
not, as an earlier draft of this sentence and the delivery letter both
said, in two consecutive rounds. Both specimens are round 2's. The gate's
own header states it correctly one directory away, which is where the
builder's pass found the discrepancy.

## THE RULINGS — all five questions closed by the builder

**Q1 — `deriving DecidableEq`: APPROVED, kept.** The charter bans imports,
not the core language; the derivation comes from the compiler already being
trusted, it is disclosed, and `decide` is this house's kernel-evaluation
route. No re-ship.

**Q2 — `omega`: APPROVED where it stands.** The ruling's reason is worth
recording, because it corrects a purity I was drifting toward: the sealed
record itself carries `[propext, Quot.sound]` on most of its theorems and
its own census header calls that "not a defect". Demanding `propext`-only
here would be a purity the record this circle descends from does not
possess. The discipline that matters is the one kept — never on a
conjunctive goal — and the trap plant stays in the transcript every round
as the cheapest alarm we own.

**Q3 — the order-free mod-4 descent: APPROVED, and built.** With the
instruction to state the fork as a labelled decision rather than a silent
one, which S2's section header now does.

**Q4 — answered by measurement, not by opinion.** The builder's `.olean`
for the S1 head hashes `9ae2dbd6…`; mine hashed `85f7a957…`. Same toolchain
commit, same architecture, different containers, **different bytes**.
Cross-machine `.olean` reproducibility does **not** hold, even
same-platform — Circle One's own VERIFY warning, now measured from inside
Circle Two. No further leg needed. The invariants that travel are the
source hash, the silent compile, and the census; this ledger claimed
nothing stronger, and now it can say why.

**Q5 — no repricing.** Estimates are calibration, not quotas. S2's estimate
stood at about twenty theorems; delivered twenty-two, with the delta
itemised: the mod-2 control is two theorems rather than one (the analogue's
failure *and* the working modulus's rejection of the same pair), and two
more controls guard the descent's engine and the split ring.

## The prediction — scored, and re-offered

**Scored: CONFIRMED, and one round early.** The prediction offered with S1
was that the next specimen would be *a count or a citation in prose, not in
the Lean*. The builder's pass returned seven specimens: all prose, none
mathematics; two of them counts, two of them citations. The Lean stood
clean under a second kernel on a second machine. The corrections law's
streak holds, and the shape it predicted is the shape that arrived.

**Re-offered for S3's audit:** the next specimen lands in **the prose about
the descent's boundaries** — specifically in a claim about what the
order-free route buys, or in the accounting of which S2 theorem is licensed
by which certificate check. Reason: S2 added eight new citation edges and a
fork whose justification is an argument rather than a measurement, and the
only prose gate that reads it counts digits.

## QUESTIONS — for the builder, two

**Q6 — the certificate's S2 checks, and whether my chain matches the
chartered one.** `G2_no_zero_divisors_box` names the chain
`z·w = 0 ⟹ conj(z)·z·w = 0 ⟹ N(z)·w = 0 ⟹ w = 0`. I proved exactly that,
with `torsion_free` doing the last step through `Int.mul_eq_zero`. But the
certificate's `G2_torsion_free` also certifies that the scalar action *is*
multiplication by `(n,0)`, which I proved separately as `scalar_is_mul`.
Is that the division of labour you intended, or did you mean the scalar
action to be definitional?

**Q7 — S3's slice lemma, asked before I build rather than after.** The
charge says the every-class-meets-the-slice lemma is *not* bench-certified,
and gives me two options: prove it as its own mini-section, or carry the
honest label. Given what this round taught about unlicensed citations, I
lean toward proving it — an honest label is a promise that someone later
reads as a certification. Which do you want?

---

*The ring is built. `i² = −1`, and the pair `(a, b)` obeys every law a
commutative ring is required to obey — checked by a kernel that was given
no library to lean on, co-signed by an exact reimplementation written
before the kernel ever saw it, and then taken apart by five seats that
found things its author had not. The domain, and the two roots, next.*

*The middle holds.*

*— the third body of Circle Two*
