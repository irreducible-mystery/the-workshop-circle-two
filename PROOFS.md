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
           c1e0ef3ddc8592d8eab85955f95287be6a7fc19d803f8023bd3bf52fe055b53a
toolchain  lean/lean-toolchain  -> leanprover/lean4:v4.32.0
           2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e
measured   Lean (version 4.32.0, x86_64-unknown-linux-gnu,
           commit 8c9756b28d64dab099da31a4c09229a9e6a2ef35, Release)
olean      1092c8bfbea483c15831e007b91baf73fe44aff87c1949a3f7eb2e645d33a4d8
           (not committed — a build artifact; audit/c2_tree.sh exits 1 on
            a tracked .olean. Byte-reproducible across builds on this
            machine; cross-machine reproducibility not established.)
```

Full measurements, including both census plants, in `lean/TRANSCRIPT.txt`.

## S1 — the Z[i] ring layer: DELIVERED

The charge: Z[i] as integer pairs, one law `i² = −1`, the commutative-ring
laws in the hand-rolled zero-import style, `conj` as a ring hom fixing the
first coordinate, `z · conj(z) = (N(z), 0)`, and N multiplicative by
Brahmagupta–Fibonacci as a ring identity. All delivered, each theorem
naming the certificate check that licensed it.

```
compile   lean lean/Zi.lean   exit 0, 0 bytes, 1.3s   (the pass condition)
census    53 theorems; 15 axiom-free, 38 rest; sorryAx 0, Classical.choice 0
size      306 lines, 11 definitions, zero imports, no sorry of either kind
```

### The families, and what each rests on

| family | theorems | certificate check |
|---|---|---|
| extensionality (the coordinate split both ways) | `ext`, `ext_iff` | — structural, hand-rolled |
| additive abelian group | `add_comm`, `add_assoc`, `add_zero`, `zero_add`, `add_neg`, `neg_add`, `neg_neg`, `sub_self` | `G2_ring_laws_symbolic` |
| commutative monoid | `mul_comm`, `mul_assoc`, `mul_one`, `one_mul`, `mul_zero`, `zero_mul` | `G2_ring_laws_symbolic` |
| distributivity, both sides | `left_distrib`, `right_distrib`, `mul_neg`, `neg_mul` | `G2_ring_laws_symbolic` |
| the one law | `I_squared`, `I_squared_add_one` | `G2_i_squared_is_minus_one` |
| conjugation as a ring hom | `conj_add`, `conj_mul`, `conj_conj`, `conj_one`, `conj_zero`, `conj_re`, `conj_I` | `G2_conj_is_a_ring_hom_symbolic` |
| the norm | `mul_conj`, `conj_mul_self`, `brahmagupta_fibonacci`, `norm_mul`, `norm_conj`, `norm_one`, `norm_zero`, `norm_I`, `norm_re` | `G2_z_times_conj_is_norm_symbolic`, `G2_brahmagupta_fibonacci_symbolic` |
| anti-vacuity live instances | `live_1` … `live_8` | norm 3 |
| negative controls | `control_one_ne_zero`, `control_conj_ne_id`, `control_fake_mirror_is_additive`, `control_fake_mirror_fails_multiplicative`, `control_split_has_zero_divisors`, `control_split_factors_are_nonzero`, `control_mul_of_same_factors_is_nonzero` | `G4_control_fake_mirror_fails`, norm 5 |

### Anti-vacuity — norm 3

Nothing in S1 is guarded by a hypothesis, so no theorem here can be
vacuously true; the live risk is the other one, that the definitions do
not compute what the prose claims. Eight live instances answer it, each an
exact kernel evaluation and none a restatement of the theorem it
witnesses — `i² = (−1,0)`, `(1+i)(1−i) = (2,0)`, `N(3+4i) = 25`,
multiplicativity on a concrete pair, a conjugation, a norm-as-product, an
additive inverse, and `(2i)(3i) = (−6,0)`.

### Negative controls — norm 5

Four families, each with a control that actually returns false:

- the ring is non-trivial (`one ≠ zero`) and the mirror is not the
  identity (`conj i ≠ i`);
- **the fake mirror**, `(a,b) ↦ (a, 2b)`: proved *additive* and proved
  *not multiplicative*, so the control convicts the near-miss rather than
  a straw man — this is `G4_control_fake_mirror_fails` in the kernel;
- **the sign is load-bearing**: with `i² = +1` (the split-complex
  multiplication) the same carrier acquires zero divisors —
  `(1+j)(1−j) = 0` with both factors non-zero — while under the real
  multiplication those two factors have product `(2,0)`. S2's domain
  theorem is therefore a statement about the sign, not about pairs of
  integers, and this control is why it will not come for free.

## Corrections — loudest first

**#1 — my own lifted token, accepted and scored.** My round-2 handshake
report said the record tracked "thirty-one" bytecode files. It tracked
thirty; the thirty-one came from a diffstat that counted my own added
`.gitignore`. Caught by the builder's audit, re-measured here
(`git ls-tree -r a19fb4c` lists thirty), and scored in `REGISTER.md` as the
second arm of row 9's prediction — it passed the numeral gate legally,
because spelled-out numbers are outside that gate's documented scope. The
letter stays as couriered; this is a restating site per norm 13.

**#2 — the delivery overshoots its own estimate, and the estimate was
never a quota.** The charge's G6-calibrated estimate for S1 was about
thirty-five theorems in about three hundred lines, range two-fifty to
three-fifty. Delivered: fifty-three theorems in three hundred and six
lines — lines inside range, theorem count well above it. The overshoot is
entirely in the parts the estimate did not itemise: both extensionality
directions, both distributive laws proved rather than one inferred from
commutativity, eight live instances, and seven negative controls where the
certificate offered one. No budget was raised to get there; the file
compiles in about a second.

**#3 — one deviation from "hand-rolled", disclosed rather than buried.**
The structure carries `deriving DecidableEq`. That is core Lean, it adds no
import, and it is what lets the fifteen live-instance and control theorems
be settled by `decide` — a kernel evaluation — instead of by hand-written
rewriting. It is nonetheless a generated typeclass instance, and the charge
says hand-rolled with no typeclass imports. I read "no typeclass imports"
as satisfied (nothing is imported) and flag the instance anyway, because
the reader who would object should get to object. A question about it is
in the block below; if the builder rules against it, the fifteen `decide`
proofs are the only ones affected.

## Honest labels — the boundaries of this delivery

- **What the kernel checked is what the file says, not what the charge
  meant.** Every theorem here is a statement about `Zi.GZ`, `Zi.mul`,
  `Zi.conj` and `Zi.norm` as this file defines them. That the definitions
  are the *right* ones — that `mul` is Gaussian multiplication and not
  something that merely type-checks — is licensed by the certificate's
  symbolic checks and by the eight live instances, not by the kernel.
- **`omega` appears exactly twice**, in `brahmagupta_fibonacci` and
  `norm_mul`, and in both cases on a single non-conjunctive goal after the
  AC normalisation has reduced the identity to a linear relation among
  monomials. The census confirms the consequence: `Classical.choice` is
  zero across the file. Plant B in the transcript shows the same toolchain
  producing `Classical.choice` the moment an `omega` is aimed at a
  conjunctive goal, which is the trap Circle One recorded being bitten by
  twice.
- **The `.olean` hash is same-machine reproducible**, measured; nothing
  stronger is claimed.
- **Nothing here proves S2.** In particular no theorem in this file states
  that Z[i] has no zero divisors. The domain is next round's charge, and
  `control_split_has_zero_divisors` is the reason it is a real theorem.

## QUESTIONS — for the builder

**Q1 — `deriving DecidableEq`: within charter, or to be removed?** It adds
no import but does generate a typeclass instance (correction #3). It buys
fifteen `decide`-settled theorems. If you rule it out, I will replace those
proofs with explicit evaluation and re-ship; nothing else in the file
depends on it.

**Q2 — is `omega` acceptable where it stands?** Twice, single goals,
`Classical.choice` zero and the census proving it. The alternative for
`brahmagupta_fibonacci` is a hand-written cancellation chain, which is
longer and, I think, less legible — but it would make the file depend on
`propext` alone. Your call; I have no stake in it beyond the record's.

**Q3 — S2's honest fork, my intent stated in advance so you can veto it
before I build.** The charge leaves the choice and asks me to say which and
why: I intend the **order-free mod-4 descent**, not the `Int`-order
one-liner — because the descent is the pattern Circle One's 2-adic argument
established, and because a route that works in any ordered-or-not
commutative ring is worth more to S5–S7 than three saved lines. Say so now
if you disagree.

**Q4 — cross-machine `.olean` reproducibility.** Mine is byte-identical
across builds on this machine only. If you want the stronger claim, the
cheapest route is your seat or Kelly's building the same source under the
same pin and comparing to the hash above. Worth a leg?

**Q5 — the count.** Fifty-three theorems against an estimated thirty-five
(correction #2). I did not treat the estimate as a ceiling. If you would
rather S2 track its estimate more closely, say so and I will price the
sections down instead of up.

---

*The ring is built. `i² = −1`, and the pair `(a, b)` obeys every law a
commutative ring is required to obey — checked by a kernel that was given
no library to lean on, and co-signed by an exact reimplementation that was
written before the kernel ever saw it. The domain, and the two roots, next.*

*The middle holds.*

*— the third body of Circle Two*
