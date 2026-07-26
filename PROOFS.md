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
           2e227702a6666f2b75f00481f8a941040106ca642046e2951ef35616b046e1d3
toolchain  lean/lean-toolchain  -> leanprover/lean4:v4.32.0
           2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e
measured   Lean (version 4.32.0, x86_64-unknown-linux-gnu,
           commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35, Release)
olean      85f7a957962a95f85ee2c0238eb38ab8a915eb8d8786c73e7b6c5b7f1246d435
           (not committed — a build artifact; audit/c2_tree.sh exits 1 on
            a tracked .olean. Byte-reproducible across builds on this
            machine; cross-machine reproducibility not established.)
```

Full measurements, including every plant fired, in `lean/TRANSCRIPT.txt`.

## S1 — the Z[i] ring layer: DELIVERED

The charge: Z[i] as integer pairs, one law `i² = −1`, the commutative-ring
laws in the hand-rolled zero-import style, `conj` as a ring hom fixing the
first coordinate, `z · conj(z) = (N(z), 0)`, and N multiplicative by
Brahmagupta–Fibonacci as a ring identity. All delivered.

```
compile   lean lean/Zi.lean   exit 0, 0 bytes, 1.3s   (the pass condition)
census    54 theorems = 16 axiom-free + 38 rest
          of the 38:  36 propext alone,  2 propext + Quot.sound
          sorryAx 0,  Classical.choice 0
size      350 lines, 11 definitions, zero imports, no sorry of either kind
shape     8 live instances, 8 control theorems, 15 decide-settled proofs
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
| distributivity, both sides | `left_distrib`, `right_distrib`, `mul_neg`, `neg_mul` | `G2_ring_laws_symbolic` (its third conjunct) |
| the one law | `I_squared`, `I_squared_add_one` | `G2_i_squared_is_minus_one` |
| conjugation as a ring hom | `conj_add`, `conj_mul`, `conj_conj`, `conj_one`, `conj_zero`, `conj_re`, `conj_I` | `G2_conj_is_a_ring_hom_symbolic` |
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
restatement of the theorem it witnesses: `i² = (−1,0)`, `(1+i)(1−i) =
(2,0)`, `N(3+4i) = 25`, multiplicativity on a concrete pair, a
conjugation, a norm-as-product, an additive inverse, and `(2i)(3i) =
(−6,0)`.

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

**#2 — nine of the twenty simp lemmas were redundant, under a comment
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

## Honest labels — the boundaries of this delivery

- **What the kernel checked is what the file says, not what the charge
  meant.** Every theorem here is a statement about `Zi.GZ`, `Zi.mul`,
  `Zi.conj` and `Zi.norm` as this file defines them. That the definitions
  are the *right* ones is licensed by the certificate's symbolic checks and
  by the eight live instances, not by the kernel.
- **`omega` appears exactly twice**, in `brahmagupta_fibonacci` and
  `norm_mul`, each time on a single non-conjunctive goal after AC
  normalisation has reduced the identity to a linear relation among
  monomials. Its price is visible and named: those are the two theorems
  carrying `Quot.sound`. The discipline that matters held —
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
boundary has now carried a specimen in each of two rounds.

## QUESTIONS — for the builder

**Q1 — `deriving DecidableEq`: within charter, or to be removed?** It adds
no import but does generate a typeclass instance. Measured: fifteen proofs
are settled by `decide`, and thirteen of them fail to synthesise without
it. If you rule it out I will replace those with explicit evaluation and
re-ship; nothing else depends on it.

**Q2 — is `omega` acceptable where it stands?** Twice, single goals,
`Classical.choice` zero and the census proving it, `Quot.sound` the visible
price. The alternative for `brahmagupta_fibonacci` is a hand-written
cancellation chain — longer, and to my eye less legible, but it would put
the file on `propext` alone. Your call.

**Q3 — S2's honest fork, my intent stated in advance so you can veto it
before I build.** I intend the **order-free mod-4 descent**, not the `Int`-
order one-liner: the descent is the pattern Circle One's 2-adic argument
established, and a route that does not need an order is worth more to
S5–S7 than three saved lines.

**Q4 — cross-machine `.olean` reproducibility.** Mine is byte-identical
across builds on this machine only. If you want the stronger claim, your
seat or Kelly's can build the same source under the same pin and compare
to the hash above. Worth a leg?

**Q5 — the count, and what to do about estimates.** The charge's
G6-calibrated estimate for S1 was about thirty-five theorems in about three
hundred lines. Delivered: fifty-four theorems in three hundred and fifty
lines. The overshoot is in the parts the estimate did not itemise — both
extensionality directions, both distributive laws proved rather than one
inferred, eight live instances, eight controls where the certificate
offered one, and two theorems added by the audit repairs. No budget was
raised; the file compiles in about a second. If you would rather S2 track
its estimate closely, say so and I will price the sections down instead
of up.

---

*The ring is built. `i² = −1`, and the pair `(a, b)` obeys every law a
commutative ring is required to obey — checked by a kernel that was given
no library to lean on, co-signed by an exact reimplementation written
before the kernel ever saw it, and then taken apart by five seats that
found things its author had not. The domain, and the two roots, next.*

*The middle holds.*

*— the third body of Circle Two*
