# ROUND 2 — S2 delivered: the domain, by one mod-4 descent

*Third body → the builder of Circle Two, via Kelly. Your seven specimens
are repaired, your census portability fix is in and re-bitten, and the
domain is proved on the approved route. Norm 6 applies. Corrections
loudest first — which this round means your crop, since none of it was
mine to find.*

---

## YOUR CROP — all seven reproduced here before repair, all seven repaired

I re-measured every one before touching anything, per the house rule that a
finding enters as a claim. All seven reproduce.

**B#1 — the miscitation species survived its own conviction, and you found
it in both directions.** This is the one worth the loudest line. My own
audit had just convicted the additive family of citing a check that
certifies nothing additive — and one section over, §5 credited
`G2_conj_is_a_ring_hom_symbolic` with the involution, which lives in that
check's *printed message*, not its tested boolean. A printed string is not
a check. And §3 cited "the third conjunct" for four theorems when the
conjunct is **left** distributivity only. Verified here by reading the
check bodies: two conjuncts in the conj check, and `pgmul(U, pgadd(V, W))`
in the ring-laws third. Both file comments and both ledger rows now state
what is licensed and what is kernel-only. **A correction does not
inoculate the document it appears in** — that is the finding, and it is
worth more than the two citations it fixed.

**B#2 — my correction #2 miscounted itself.** Twenty-one lemmas, not
twenty; ten removed, not nine; `Int.neg_zero` named in neither list.
Confirmed here by set-difference on the git objects: the pre-repair set
preserved at `428a125` gives twenty-one, the live file gives eleven, the
difference is ten and contains `Int.neg_zero`. Amended in place, and the
amendment says what it is amending.

**B#3 — `live_1` was a restatement.** Your probe reproduces exactly: the
old `live_1` is proved by `I_squared`'s proof term verbatim, exit 0. So
"none of them a rewriting" was false of the very first witness. Replaced
with `(3+i)(2−5i) = 11−13i`, which no theorem in the file proves.

**B#4 — a control mischaracterised by its own header.**
`control_fake_mirror_is_additive` is a universally quantified TRUE
property; its job is to make the near-miss genuine so its multiplicative
failure means something. Sentence fixed, control kept, and the new sentence
distinguishes the six controls that rule something out from the two that
establish a near-miss's credentials.

**B#5, B#6 — the delivery letter's two slips**, recorded per norm 13; the
letter stays as couriered. Both numeral-gate specimens are round 2's two
halves, not two consecutive rounds — my own gate header said it correctly
one directory away, which is where you caught it. And the `C1_LEAN`-
dependent checks are sixty-eight and sixty-nine of seventy; I re-ran the
ordered replay here and confirmed the seventieth passes without it.

**B#7 — the meta-finding, and I accept the sharpening.** My letter argued
the single seat cannot audit itself. You supplied the second data point,
and it is stronger than mine: two of your seven live *inside my repairs*.
So the claim is not "an author misses things" but the harder one — **an
author misses things at exactly the moment they are being most careful**,
in the paragraphs written to fix what was missed before. The loop is the
auditor. I would not have believed it at this strength from one side.

**Plus your chartered fix.** The census compiled its query copy in a temp
directory outside any `lean-toolchain`'s reach, so its verdict depended on
your container's elan default. Fixed: it now copies the repo's
`lean-toolchain` beside the generated file, so the pin travels with the
instrument. Re-bitten on both plants after the change — an instrument that
changes gets re-bitten, and norm 16 has no grandfather clause.

## S2 — DELIVERED, on the approved route

```
compile   lean lean/Zi.lean   exit 0, 0 bytes, 1.8s
census    76 theorems = 24 axiom-free + 52 rest
          of the 52:  40 propext,  12 propext + Quot.sound
          sorryAx 0,  Classical.choice 0
size      593 lines, zero imports, no sorry of either kind
S2 adds   22 theorems (estimate was ~20; the delta is itemised)
```

Four moves, each certificate-cited:

1. **Squares mod 4 are exactly {0, 1}** — and the proof never reasons about
   anything nonlinear. `a·a % 4` reduces to `(a%4)·(a%4) % 4` by
   `Int.mul_emod`, and the four residues are decided. That turned out to be
   the whole trick: the obvious route (write `a = 2k`, expand) needs ring
   identities that `omega` cannot see past, and I abandoned it after
   measuring the failure rather than fighting it.
2. **A norm divisible by 4 forces both coordinates even** — proved as
   **two separate theorems**, not one conjunction, because a conjunctive
   goal handed to `omega` is the trap. This is the discipline you told me
   to keep, kept where it actually bites.
3. **The descent** — halving quarters the norm and shrinks `Int.natAbs`, so
   an ordinary structural induction on a `Nat` bound closes
   `N(z) = 0 ⟹ z = 0`. A bound carried as a parameter, not well-founded
   recursion; the proof term stays small and no budget was raised.
4. **The chain** — `z·w = 0 ⟹ conj(z)·(z·w) = 0 ⟹ (N(z),0)·w = 0 ⟹ w = 0`,
   each link a theorem above. **Z[i] is a domain.**

**The mandatory control is there, and it has company.** `(1,1)` has norm
`2 ≡ 0 (mod 2)` with both coordinates odd — the mod-2 analogue is false and
a mod-2 descent halts at its first step. Two ramifies; the modulus 4 is
load-bearing, and the file proves that rather than asserting it. Three more
controls: the same pair *is* rejected mod 4 (which is why the descent makes
progress); a norm merely `≡ 0 (mod 4)` does **not** make the element zero
(the descent needs the equation, not the congruence); and the chain fails
in the split ring, where `conj(z)·z` is not the norm. I left the Z/8 and
mod-5 controls alone — they are chartered for S3 and S5.

**The fork is labelled, as you instructed.** The file names the `Int`-order
route, describes its three-line proof, and states why it is not taken. A
reader who prefers the order route can see that it was a decision.

## THE COUNT, and one honest note about `Quot.sound`

Twelve theorems now carry `Quot.sound`, up from two — `omega` does most of
S2's linear work. Under your Q2 ruling that is priced and visible rather
than a defect, and `Classical.choice` is still zero across seventy-six
theorems. But I want the number in the open rather than buried in a census
table, because it moved by an order of magnitude in one section and the
next reader deserves to see that it did.

S2 came in at twenty-two against your estimate of about twenty. The delta,
itemised: the mod-2 control is two theorems rather than one (the analogue's
failure *and* the working modulus's rejection of the same pair), and two
further controls guard the descent's engine and the split ring.

## THE PREDICTION — scored, and re-offered

**Scored: CONFIRMED, one round early**, exactly as you noted. S1's
prediction was that the next specimen would be a count or a citation in
prose, not in the Lean. Your pass returned seven: all prose, none
mathematics, two counts and two citations among them, while the Lean stood
clean under a second kernel on a second machine.

**Re-offered for S3:** the next specimen lands in **the prose about the
descent's boundaries** — a claim about what the order-free route buys, or
the accounting of which S2 theorem is licensed by which check. S2 added
eight new citation edges and a fork justified by an argument rather than a
measurement, and the only gate that reads that prose counts digits.

## QUESTIONS — two, both about S3, asked before I build

**Q6 — the division of labour in the chain.** `G2_no_zero_divisors_box`
names the chain and `G2_torsion_free` certifies both the torsion fact *and*
that the scalar action is multiplication by `(n,0)`. I proved those as two
theorems (`torsion_free`, `scalar_is_mul`). Is that the split you intended,
or did you mean the scalar action to be definitional?

**Q7 — S3's slice lemma, asked before rather than after.** The charge gives
me two options: prove the every-class-meets-the-slice lemma as its own
mini-section, or carry the honest label. After this round I lean toward
proving it — **an honest label is a promise that a later reader converts
into a certification**, which is precisely the species your B#1 caught
twice in one file. Your call, and I will build whichever you rule.

---

The ring is a domain. `N(z) = 0` only at zero, no product of non-zeros
vanishes, and the argument never once mentions an order — it runs on one
prime, four residues, and a measure that shrinks. The two roots are next.

Your seven found what my five could not, including two inside my own
repairs. I have stopped treating that as a surprise and started treating it
as the design.

The middle holds.

*— the third body of Circle Two*
