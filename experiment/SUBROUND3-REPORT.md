# SUB-ROUND 3 — S3, pentagon necessity (quarantined)

*SuperNinja, dual-seat experiment, third sub-round. Same protocol,
same honest label: one architecture, both chairs, seat boundary
procedural. Everything below marked measured was produced by an
instrument this session.*

## What shipped

- **Seat P:** S3 appended to `Zi.lean` — 26 new theorems, plus the
  crop's Gaussian witness (84 total, 868 lines): the bench F-symbol and
  pentagon plumbing transcribed from `floor/symmetric_statistics.py`
  lines 102/108 (cited, per C1's lesson); the 15 off-forcing instances
  as identities in a symbolic f; the forcing instance at (1,1,1,1) with
  lhs = f², rhs = 1; **pentagon ⟺ f² = 1** at the instance level; the
  counted classification (11, 4, 1) at a separating witness, tied to
  nest 16; the factorization (f−1)(f+1) = f²−1 symbolically; **exactly
  two via S2's domain** (`pentagon_exactly_two`); the gauge layer —
  slot motion, slice-forces-symmetry, **slot invariance**
  (division-free, cleared form, cancellation through the domain);
  live witnesses on and off the real axis; controls: **Z/8 four roots**
  (nest 8, tied), **f = i fails with residual exactly 4**, f = 2 fails,
  and a gauge control (non-slice-preserving η moves the slot).
  Compile: **exit 0, zero bytes, ~2.1s.** Census: **84 covered,
  0 sorryAx, 0 Classical.choice** — clean on the first full compile;
  the S2 lesson was applied at write time and the trap did not fire.
  Final pin: `Zi.lean` sha256
  `49e850e1f04333552c97633ef5afdae903757b75ea8473eddc8a46c553ab7e8a`.
- **Courier:** statements v4 extracted mechanically (83 theorems
  pre-crop, sha256 `ebd937b4…fa93b`; v4-final post-crop, 84, sha256
  `1314192c…2114`); the extraction script now in the tree
  (`courier/extract_statements.py`).
- **Seat B:** `verify_zi_s3.py` — **32 checks, 32 pass, exit 0.**
  Polynomial-exact where the Lean is symbolic: the classification
  re-derived in Z[i][fr, fi] (coefficients, not sample points); the
  single obstruction polynomial confirmed to be exactly f² − 1; the
  root count by the **independent route** (norm-multiplicativity + the
  four-unit census); the gauge layer symbolic in four vertex variables,
  including the earned-not-built-in check (without η01 = η10 the slot
  motion polynomials differ). Plant bitten (falsified classification
  count → exit 1, the poisoned check named), restored clean
  (sha256 `feac6e83…255fc`).

## The wording boundary held (charter flag 2)

The headline is stated in **slice-plus-invariance form** and nowhere
else: `pentagon_exactly_two` (two solutions on the normalized slice,
distinct by char 0) + `gauge_slot_invariant` (the slot is a gauge
invariant of the slice, so the classes are genuinely distinct). No
statement in the file says "H³(Z₂) = Z₂" or "every class meets the
slice" — that lemma is not proven and not bench-certified, and the
file's own docstrings carry the label. Seat B's instrument includes a
prose-review check of exactly this boundary, honestly labeled as a
review claim.

## Seat B's crop (letter in tree)

1. The counted classification filters by **lhs value alone** — sound,
   but the tie to instance-classification rides on `pentagon_offdiag`
   + the forcing lemmas; the docstring now says so (the recurring
   species: term graph sound, implicit dependency story the defect
   surface — third sighting in three sub-rounds).
2. `slice_forces_eta_symmetric` is **stronger than the certificate's
   G1c row** — two of the seven zero-slot conditions suffice; labeled
   now, so no future reader assumes all seven were used.
3. Every live witness was purely real; a Gaussian witness added
   (`live_gaussian_witness`, f = 1+i: forcing lhs = 2i) — the symbolic
   claims now tie to a point that exercises the imaginary coordinate.

## One honest dead-end, preserved

The first draft of the gauge section omitted the η01 unit hypothesis
(the certificate's "η : Z₂ × Z₂ → units" was the missing
transcription) and could not close without it; the dead-end is
documented in the compile transcript. This is the S3 species the
charge predicted — prose-adjacent structure (what the certificate
*means* by "units") is where the dual-seat mode works hardest.

## Running score, three sub-rounds in

| | S1 | S2 | S3 |
|---|---|---|---|
| theorems | 42 | 57 | **84** |
| kernel | silent, ~0.6s | silent, ~1.5s | silent, ~2.1s |
| census | 0/0, plant bitten | 0/0, **live ALARM fired** (×6, repaired) | 0/0, clean first compile (lesson held) |
| seat B checks | 47/47 | 24/24 | **32/32, polynomial-exact** |
| seat B route | exact reimpl. | two independent routes | symbolic ring + independent unit census |
| crop | 1 conviction | 2 labels + 1 deferral judged | 2 labels + 1 witness added |
| corrections law | confirmed | confirmed (third bite, alarm held) | confirmed in-flight (dead-end at transcription, repaired pre-ship) |

The chartered S1–S3 arc — the ring, the domain, pentagon necessity —
is now rehearsed end to end: **84 theorems, kernel-silent, census
clean, every claim re-derived cross-seat, every instrument plant-bitten
both directions.** What remains of the round-1 charge scope is the
hexagon layer (R² = F, the four units, the flatland filter as a Galois
statement) — S4-shaped work that the charge assigns beyond S1–S3; the
experiment stops at the chartered boundary unless the seats of record
extend it.

The middle holds.

*— SuperNinja, sub-round 3, quarantined*
