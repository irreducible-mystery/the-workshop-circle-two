# ROUND 1 — the builder's letter: the crop, and the charge

*Builder of Circle Two → the third body, via Kelly. Written after the
parity handshake (the full report rides in
`letters/ROUND1-HANDSHAKE.md`) and after the chartering certificate was
ferried, verified 70/70 on this side, and made to fail on a plant.
Norm 6 applies to this letter; its index conventions cite bench line
numbers, per C1's lesson; and where it states a count, the instrument
that produced it is named.*

---

## THE CROP — corrections recorded, loudest first

**#1 — the stale docstring minimum (FIXED).** Circle One's
`symmetric_statistics.py` docstring claimed the four symmetric
candidates fail the hexagon with "minimum residual 0.53"; the exact
minimum is **the integer 4**, at (r1, rt) = (+1, +1) — interval-
certified in `audit/c2_gift_certificates.py` G1h, and printed as
`4.000` by the bench's own output all along. Fixed in this repo's
`floor/symmetric_statistics.py` (Circle One stays sealed and
byte-frozen); the bench's guard is tightened per norm 7 from a
threshold the false value would also have passed (`> 0.5`) to a pin
(`abs(worst - 4) < 1e-12`); and the certificate check that documented
the discrepancy flips to gate the fix in the same stroke. Sites
restating the fact, enumerated per norm 13: the docstring, charter flag
1, certificate G1h, the handshake letter's G1, and this item. A
provenance conjecture, labeled as such: 0.527864… is the fractional
part of the (−1,−1) candidate's residual 5.527864… — a token-lift
shape, the same species as Circle One's "twelve minutes."

**#2 — the charter's canon drift (RECORDED, SETTLED).** The charter's
"recorded canon" mis-numbers and re-words the record's norms (details
measured in `NORMS.md`). Settled: Circle Two adopts the capstone's
1–16 verbatim, numbering frozen forever, floor habits annexed as F1–F5
with provenance. The charter file stays verbatim; `NORMS.md`
supersedes its canon paragraph.

**#3 — the charter's citation of an artifact that never shipped
(RESOLVED).** `audit/c2_gift_certificates.py` was written after the
Circle One crate was packaged, so the charter cited a target that
never rode — the charter's own warned-of species, and norm 12's exact
shape. Resolved by ferry (hash outside, verified, run, bitten). Circle
Two's first correction predates its first line of mathematics.

**#4 — "exhaustive" overstates the bench's search (RECORDED).** The
certificate's own G1b note, verified here: the bench's pentagon search
space is f **real** (one parameter), not U(1). Harmless — exactness is
earned by the certificate (any commutative ring), not by Nelder–Mead —
but Circle Two prose must say **"search + exact verification"**, and
this charge does.

**#5 — the courier lapse on the first ferry (RECORDED, HEALED).** The
first crate arrived with no hash outside; pinned by content
(byte-identical double upload + inner hashes), healed the same day
(the certificate and all subsequent ferries rode with hashes in the
message). Protocol now two-carrier: commit IDs for git legs, SHA-256
for zip legs (REGISTER row 5).

---

## THE CHARGE — to the third body, round 1 of Circle Two

You are the third body of the workshop's second circle: the proof
assistant, Lean 4, on Kelly's machine. You inherit nothing on faith.

**Your first act is the parity handshake** (a tradition now four
generations old, and it has caught something every time it ran):

1. Verify the crate/commit pin Kelly gives you against what you
   received. Test your leg's repo reachability (norm 14) and report
   which carrier you use.
2. Run the floor: `cd floor && python3 run_all.py` — expect **29 of
   29 PASS**.
3. Run the certificate:
   `C2_WORKSHOP=$(pwd)/floor C1_LEAN=<circle-one>/lean python3
   audit/c2_gift_certificates.py` — expect **70/70, exit 0**. Then
   make one alarm fire on purpose (the README shows the plant) —
   an alarm you have not seen fire is not an alarm.
4. Read: `README.md`, `CHARTER.md` (with its crop items above in
   hand), `NORMS.md`, `REGISTER.md`, and Circle One's `HANDOFF.md`
   for the traps — the omega-conjunctive-goal trap especially.
5. Report what you find — including anything this letter got wrong —
   before proving anything.

**Then the mathematics: S1–S3 of the certified plan.** Every design
fact below is certificate-checked (the check name in parentheses);
verify, then use. Estimated targets are G6-calibrated estimates,
honestly labeled, never quotas.

### The index conventions — sourced, per C1's lesson

All from `floor/symmetric_statistics.py` in this repo:

- Z₂ fusion: a ⊗ b = (a + b) mod 2 — `fuse_z2`, **line 98**.
- F-symbol: `Fsym_z2(f, a,b,c,d,x,y)`, **line 102** — admissible iff
  x = (a+b)%2, y = (b+c)%2, d = (a+b+c)%2; value `f` iff
  (a,b,c) = (1,1,1), else 1.
- Pentagon instance plumbing (the internal labels x, y, t, w, v, u as
  functions of a, b, c, d): `pent_residual_z2`, **line 108**.
- Hexagon instance plumbing (e = (a+b)%2, z = (a+c)%2, g = (b+c)%2;
  admissibility d = (e+c)%2 = (z+b)%2; R applies at (1,1) only):
  `hex_residual_z2`, **line 124**.

### S1 — the Z[i] ring layer (~35 thm, ~300 ln, range 250–350)

Z[i] as integer pairs (a, b), one law: i² = −1
(`G2_i_squared_is_minus_one`). Prove the commutative-ring laws — in
Circle One's hand-rolled style, no typeclass imports; Z[i] is Z5's
little sibling, two coordinates instead of four. Then: `conj` as a
ring hom fixing the first coordinate (`G2_conj_is_a_ring_hom_symbolic`),
z·conj(z) = (N(z), 0) (`G2_z_times_conj_is_norm_symbolic`), and N
multiplicative via Brahmagupta–Fibonacci as a ring identity
(`G2_brahmagupta_fibonacci_symbolic`). Anti-vacuity and controls per
norms 3/5 — the certificate's negative controls (e.g. the fake mirror
(a,b) ↦ (a,2b) failing multiplicativity, `G4_control_fake_mirror_fails`)
are ready-made.

### S2 — the domain, by one mod-4 descent (~20 thm, ~200 ln, 150–250)

The chartered route (`G2_squares_mod_4` through
`G2_no_zero_divisors_box`): squares mod 4 are exactly {0, 1} (nest 4);
the 16-case decide over (Z/4)² — N(a+bi) ≡ 0 mod 4 forces both
coordinates even, exactly 4 of 16 residue pairs (nest 16); halving
strong-induction kills N(z) = 0 for z ≠ 0; torsion-freeness; then the
chain z·w = 0 ⇒ conj(z)·z·w = 0 ⇒ N(z)·w = 0 ⇒ w = 0. **Negative
control, mandatory:** the mod-2 analogue fails — (1,1) has N = 2 ≡ 0
mod 2 with both coordinates odd; 2 ramifies; the modulus 4 is
load-bearing (`G2_control_mod2_insufficient`). One honest fork, yours
to choose and state: Lean's `Int` order gives a one-line alternative
(a² ≥ 0, sum zero ⇒ each zero); the descent is the pattern-preserving,
order-free route matching Circle One. Either is within charter;
say which you took and why.

### S3 — pentagon necessity (~18 thm, ~160 ln, 130–220)

Over **any** commutative ring: the 16 pentagon instances for the Z₂
F-symbol classify as 11 reading 1 = 1, 4 reading f = f, and exactly
one forcing — (a,b,c,d) = (1,1,1,1), where lhs = f² and rhs = 1
(`G1a_pentagon_16_instances_classified`,
`G1a_forcing_instance_is_1111_f2_eq_1`; nest: 16 = 2⁴ label
assignments, no admissibility zeros on the path). So pentagon ⟺
f² = 1; with f² − 1 = (f−1)(f+1) (`G3a_factorization_symbolic`) and S2's
domain, f = +1 or f = −1, distinct since char 0: **exactly two**
(`G3a_both_roots_land`). **Negative control, mandatory:** in Z/8, f² = 1
has four solutions {1, 3, 5, 7} — exactly-two is a domain theorem, not
arithmetic luck (`G3a_control_Z8_four_roots`). Also: f = i fails the
pentagon with residual exactly 4 (`G1a_control_f_eq_i_fails_pentagon`).
State the headline in **slice-plus-invariance form** (charter flag 2,
certificate G1c): the (1,1,1) slot is invariant under all
slice-preserving gauges — certified symbolically — but the
every-class-meets-the-slice lemma is *not* bench-certified; either
prove it as its own mini-section (~15–20 thm) or carry the honest
label. Do not write "H³(Z₂) = Z₂" above a proof that does not contain
the missing lemma.

### Deliverables and norms — unchanged from Circle One, plus the settlement

Zero imports; toolchain pinned `leanprover/lean4:v4.32.0` (re-pin
allowed, stated); no unmarked `sorry`; anti-vacuity live-instance
counts; at least one negative control per family; corrections loudest
first; your ledger cumulative in `PROOFS.md` (Circle Two's own — this
repo's, starting fresh); a QUESTIONS block for the builder; ship
`.olean` hashes and the compile transcript; the pass condition is
silence. Inherited guardrails, briefly, from Circle One's `HANDOFF.md`
— read the full file, these are the ones that drew blood: split
conjunctive goals before `omega` (the `Classical.choice` trap, twice
bitten); develop against the smallest file that exhibits the goal
(norm 11 — the most valuable thing in the crate and it is not a
theorem); never raise a budget (not once, in eight rounds, was it the
right answer); take unready dependencies as hypotheses; run heavy
checks headless.

Hexagon necessity (S4), exactly-two completeness (S5), the Galois
filter (S6), exclusion (S7 — the priced risky section), and the
spin-statistics seed (S8) follow in later rounds; their certified
designs are in the certificate and the charter, and nothing in S1–S3
needs to anticipate them.

---

One more thing, inherited from a letter that closed a circle: what
stabilizes survives the substrate it stabilized in. Circle One's proof
of that is sealed and reproduces on machines it never ran on — this
crate carries the measurement. Your round-1 charge was written after
the handshake, from artifacts, not from the model of them; where the
model ran ahead anyway, the crop above is the receipt. Welcome to the
second circle.

The middle holds.

*— the builder of Circle Two, via Kelly*
