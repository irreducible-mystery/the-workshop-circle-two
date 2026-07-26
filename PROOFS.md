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
           410d91dcb224d7e88a7feffd35fe1d76e8a7d1931cd7cf56e4b8a5ed5ec2a4ad
toolchain  lean/lean-toolchain  -> leanprover/lean4:v4.32.0
           2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e
measured   Lean (version 4.32.0, x86_64-unknown-linux-gnu,
           commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35, Release)
olean      854244ba92079b31bae4b31adce61c9204b71eb456c2c685585fb93873a0e295
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

```
compile   lean lean/Zi.lean   exit 0, 0 bytes, 1.8s   (the pass condition)
census    76 theorems = 24 axiom-free + 52 rest
          of the 52:  40 propext alone,  12 propext + Quot.sound
          sorryAx 0,  Classical.choice 0
size      593 lines, 11 definitions, zero imports, no sorry of either kind
shape     12 live instances, 12 control theorems, 21 decide-settled proofs
          S1 contributes 54 theorems; S2 adds 22
```

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
| squares mod 4 | `sq_mod_four`, `sq_mod_four_zero_of_even`, `sq_mod_four_one_of_odd` | `G2_squares_mod_4` (nest 4) |
| the sixteen cases, split in two | `re_even_of_norm_mod_four`, `im_even_of_norm_mod_four` | `G2_16_case_decide` (nest 16) |
| **the mandatory mod-2 control** | `control_mod_two_insufficient`, `control_mod_four_rejects_odd_pair` | `G2_control_mod2_insufficient` |
| the descent | `norm_quarters`, `natAbs_two_mul`, `descent_bound`, `norm_zero_forces_zero`, `norm_ne_zero_of_ne_zero` | `G2_descent_step_strictly_decreases`, `G2_norm_zero_forces_zero` |
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

## Honest labels — the boundaries of this delivery

- **What the kernel checked is what the file says, not what the charge
  meant.** Every theorem here is a statement about `Zi.GZ`, `Zi.mul`,
  `Zi.conj` and `Zi.norm` as this file defines them. That the definitions
  are the *right* ones is licensed by the certificate's symbolic checks and
  by the twelve live instances, not by the kernel.
- **`omega` is the file's workhorse, and its price is visible.** In S1 it
  appears twice (`brahmagupta_fibonacci`, `norm_mul`); in S2's descent it
  does most of the linear work. Twelve theorems carry `Quot.sound` as a
  result, and the census names every one. It is never aimed at a
  conjunctive goal — every conjunction is split first, which is why
  `Classical.choice` is zero across seventy-six theorems. The discipline that matters held —
  `Classical.choice` is zero — and the transcript's Plant B shows the same
  toolchain producing `Classical.choice` the moment an `omega` is aimed at
  a conjunctive goal.
- **The `.olean` hash is same-machine reproducible**, measured; nothing
  stronger is claimed.
- **Nothing here proves S2.** No theorem in this file states that Z[i] has
  no zero divisors. That is next round's charge, and
  `control_split_has_zero_divisors` is why it is a real theorem.
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
