# SEAT B → SEAT P: corrections letter, sub-round 4 (the hexagon layer)

Input: `Zi_statements_v5.txt` (sha256 `d195b3de0ead00799b4e913eeba4f6a71c900c6209859b947e1132c37387e3bb`),
statements only. Instrument: `verify_zi_s4.py` — 36/36, exit 0. Every S4
claim re-derived coefficientwise in Z[i][fr, fi, rr, ri]; root censuses by
the independent norm route; Z[i]/5 by direct modular squaring; the plant
(R applied at (1,0) instead of (1,1)) bitten by the off-diagonal sweep.

The crop — three items, in decreasing weight:

## 1. Nat-subtraction hazard in `control_Zi_mod5_splits` (docstring fix requested)

The statement encodes the real part of (a+bi)² mod 5 as
`(a*a + 5*5 - b*b) % 5`. Over **Nat**, subtraction truncates at zero, so
this encoding is correct **only because** `b ∈ List.range 5` bounds
`b*b ≤ 16 < 25 = 5*5`; outside that range the expression would silently
truncate and count wrong roots. Seat B verified safety within the stated
nest (and cross-checked by direct modular squaring on residue pairs — the
same four roots each side: √1 = {(0,2),(0,3),(1,0),(4,0)},
√−1 = {(0,1),(0,4),(2,0),(3,0)}). The theorem as stated is TRUE, but the
`+ 5*5` guard is load-bearing and invisible. **Request: one docstring
sentence recording that the offset makes Nat subtraction safe on the
range-5 nest.** No statement change needed.

## 2. `filter_nest_2_of_4` is arithmetic only (observation, no change requested)

The theorem body is `2 + 2 = 4`; the actual filter verdicts (which two of
the four are conj-fixed) live in `flatland_filter`. This matches the
nest-tying convention of prior sub-rounds (the count theorem ties the
arithmetic, the content theorem supplies the verdicts), and the docstring
already cross-references. Recorded so a future reader does not mistake the
count theorem for the content theorem.

## 3. Independence report (positive finding, no change)

Seat B's root censuses for `R_over_boson_class` / `R_over_semion_class`
deliberately did NOT use seat P's factorization route: instead
N(r²) = N(r)² = 1 forces N(r) = 1, the norm-1 census is the complete box
[−1,1]² (complete because a² ≤ 1 forces |a| ≤ 1, not by hope), and squaring
the four units sorts them 2/2. Both routes name the same sets. The
factorization (r−i)(r+i) = r²+1 was additionally verified coefficientwise
as its own claim. Two independent derivations agree — the strongest kind
of PASS this seat can issue.

— seat B (blind: statements v5 only; bench and seat P proofs unseen)
