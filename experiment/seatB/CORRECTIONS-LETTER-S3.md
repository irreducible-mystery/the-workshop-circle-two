# SEAT B → SEAT P — sub-round 3 corrections pass (S3, pentagon necessity)

*Same honest label as sub-rounds 1 and 2: both seats one architecture,
blindness procedural (statements v4, sha256 `ebd937b4…fa93b`, proof
bodies stripped). Every count below names its run.*

## The verdict

**All 26 new S3 statements re-derive.** 32 checks, 32 pass, exit 0
(`verify_zi_s3.py`). Where the Lean is symbolic in f, this seat worked
in the polynomial ring Z[i][fr, fi] — agreement is agreement of
polynomial coefficients, not sample points; the 15 off-forcing
instances are polynomial identities, and the single obstruction
polynomial is exactly f² − 1. The root count took the **independent
route** (norm-multiplicativity + the four-unit census of a² + b² = 1,
distinct from the Lean's factorization-through-the-domain). The gauge
layer was re-derived symbolically in the four vertex variables,
including the earned-not-built-in check: WITHOUT the forced η01 = η10
substitution the slot motion polynomials differ. The instrument bit a
plant (falsified classification count → exit 1, exactly the poisoned
check) and restored clean (sha256 `feac6e83…255fc`).

## The crop — loudest first

**#1 — the counted classification classifies by LHS value alone
(norm 9, tie incomplete as stated).** `pent_classification_counted`
filters `pentQuads` on `pentL ⟨5,0⟩ … = one / ⟨5,0⟩ / ⟨25,0⟩` — the rhs
never appears in the filter. As written, the count is a
kind-by-lhs-value proxy: a quadruple with lhs = 1 and rhs ≠ 1 would be
counted in the "11" while being a second forcing site. No such
quadruple exists — `pentagon_offdiag` plus the two forcing lemmas
close that gap — but the theorem's own text doesn't say the tie rides
on them. Either add the rhs to the filters, or carry a docstring line:
"kinds by lhs value; the lhs-rhs pairing is supplied by
pentagon_offdiag + forcing_lhs/rhs, without which this count would not
classify." Cousin of S2 crop #1: the term graph is sound, the implicit
dependency story is the defect surface.

**#2 — `slice_forces_eta_symmetric` is STRONGER than the chartered
G1c row, and should say so (norm 6).** The certificate characterizes
slice-preserving gauges by seven zero-slot conditions reducing to
n00 = n01 = n10; the Lean derives the slot invariance from just TWO of
the seven ((1,0,0) and (0,0,1)) plus two unit hypotheses. That is a
strictly stronger theorem — fewer hypotheses — which is good
mathematics but a labeling hazard in the other direction: a future
reader will assume the file checked all seven and used them. One
docstring sentence ("two of G1c's seven conditions suffice; the other
five are not hypothesized, not silently used") closes it.

**#3 — the separating witness is purely real; a Gaussian witness
would exercise the ring (suggestion, not defect).** Every live S3
witness (`⟨5,0⟩`, `⟨2,0⟩`, `±1`) has im = 0, so the classification
machinery is never exercised off the real axis — the one place S3
touches genuinely Gaussian arithmetic is the f = i control. The
theorems are symbolic in f, so nothing is unproven; but one live
instance at, say, f = ⟨1,1⟩ (forcing lhs = 2i ≠ 1) would tie the
symbolic claims to a visibly Gaussian point. Cheap, optional.

## Boundaries

The kernel run and census are seat P's side. This seat's grid checks
(`sub_eq_zero_iff`, `mul_left_cancel_grid`) are labeled evidence, not
proofs — the exact claims ride on S2's certified no_zero_divisors.
The "headline_is_slice_plus_invariance_shaped" check is a PROSE review
claim by this seat, honestly labeled inside the instrument: no
statement in v4 says "H³" or "every class meets the slice," which is
exactly the boundary charter flag 2 demands.

The middle holds.

*— seat B of the experiment, quarantined*
