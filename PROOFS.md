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
           71cc55d54af8d772f71e07f324b579c3aa71608fc57fc13b8323135c04790cc0
toolchain  lean/lean-toolchain  -> leanprover/lean4:v4.32.0
           2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e
measured   Lean (version 4.32.0, x86_64-unknown-linux-gnu,
           commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35, Release)
olean      6533e27153c3f1b51a6ec33248afea83121c7b406f8770f9b2ced8fc6d66709f
           (not committed — a build artifact; audit/c2_tree.sh exits 1 on
            a tracked .olean. Byte-reproducible across builds on this
            machine. Cross-machine reproducibility is now measured FALSE —
            see Q4, answered.)
```

Full measurements, including every plant fired, in `lean/TRANSCRIPT.txt`.

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

Eight control theorems across four families:

- **the ring is non-trivial** (`one ≠ zero`) — one theorem;
- **the mirror is not the identity** (`conj i ≠ i`) — one theorem;
- **the fake mirror** `(a,b) ↦ (a, 2b)`, proved *additive* and proved
  *not multiplicative* — two theorems, so the control convicts a genuine
  near-miss rather than a straw man. This is `G4_control_fake_mirror_fails`
  in the kernel;
- **the sign is load-bearing** — four theorems. With `i² = +1` (the
  split-complex multiplication) the same carrier acquires zero divisors:
  `(1+j)(1−j) = 0`, with **each factor separately proved non-zero**, while
  under the real multiplication those same two factors have product
  `(2,0)`. S2's domain theorem is therefore a statement about the sign,
  not about pairs of integers, and this is why it will not come for free.

## S2 — the domain, by one mod-4 descent: DELIVERED

Approved route: the **order-free descent**, not the `Int`-order one-liner.
Twenty-two theorems, and the fork is labelled in the file rather than taken
silently — the order route is named, its three-line proof described, and
the reason it is not taken given.

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

Thirty-nine theorems. The pentagon's sixteen instances are classified in
the kernel, the one that forces is isolated, and the two roots are forced
through S2's domain.

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
exists. Where it stalls, precisely: the natural route needs the units of
Z[i] classified as `{±1, ±i}`, and the order-free half of that (ruling out
`N(u) = −1` by squares mod 4) I have; the other half (`a² + b² = 1` forces
a unit coordinate) wants either `Int`'s order or a second descent, and I
would rather ask than smuggle an order into a circle that just spent a
section avoiding one. That question is Q8.

## The units of Z[i] — Q8, route (b): DELIVERED

The builder ruled route (b) — order-free, bridging to `Nat` — and supplied
the route. Fifteen theorems: the `Nat` core (`succ_sq_expand`,
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

Twenty-three theorems. The braiding adds `R`; the hexagon has sixteen loop
assignments of which **eight are admissible**; and given the pentagon its
entire content is one equation.

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

Twelve theorems. On a unit the inverse is the conjugate — `mul u (conj u) =
(N(u), 0)` from S1, `N(u) = 1` from Q8 — so the R⁻¹-hexagon is the
R-hexagon read at `conj R`. No new plumbing, no second set of instances, no
new admissibility.

**`catalog_of_four_both_hexagons`**: imposing the R-hexagon **and** the
R⁻¹-hexagon yields exactly the same four pairs. That is the certificate's
"no extra root cost" (`G1d_catalog4_satisfies_BOTH_hexagons`) proved rather
than quoted, and it is what discharges S4's boundary. The theorem `catalog_braidings_are_units` records that each of the four
braidings is a unit whose inverse is its conjugate.

**Controls**: `control_non_unit_breaks_the_bridge` shows the equivalence is
about units and not about everything — `1 + i` has norm two, so its
conjugate is not its inverse; and the wrong-class rejection survives the
inverse form.

**Section 12's scope sentence stays**, now that the boundary is discharged
elsewhere: a boundary retired in another section is not a boundary that was
never there, and the file says which section imposes what.

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
