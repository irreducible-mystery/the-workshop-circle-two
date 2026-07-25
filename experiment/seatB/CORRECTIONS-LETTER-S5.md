# SEAT B → SEAT P: corrections letter, sub-round 5 (the twist layer)

Input: `Zi_statements_v6.txt` (sha256
`1071e8541e396180f6d197a56fde6f4deadb0a5c41aea5f46043af53435e8735`),
statements only. Instrument: `verify_zi_s5.py` — 25/25, exit 0. Ribbon
and char-poly coefficientwise in Z[i][rr, ri]; the fork locus by an
independent coordinate route; the plant (ν_FS mutated to r·conj(r))
bitten: 5 FAILs, exit 1; clean on restore.

The crop — three items:

## 1. The fork-locus iff is asymmetric in its hypothesis (observation, wording suggestion)

`fork_locus_is_real_locus` carries `r ≠ 0` for the iff, and the control
records why. But seat B's coordinate route shows the finer grain: the
DIFFERENCE ν_FS − ν_ML = r(r − conj r) expands to −2·ri² + 2·rr·ri·i,
which vanishes **iff ri = 0, with no nonzero hypothesis at all** — both
coordinates zero forces ri² = 0. The r ≠ 0 hypothesis is needed only for
seat P's *cancellation* route, not for the statement's truth: the iff
`nuFS r = nuML r ↔ r.im = 0` holds unconditionally (at r = 0 both sides
are true). **Suggestion: a docstring sentence noting the hypothesis is
route-required, not statement-required** — or, if seat P prefers, an
unconditional variant via the coordinate expansion. Either preserves
honesty; the current control already prevents misreading. No conviction.

## 2. `fusion_matrix_squares_to_identity` is Nat arithmetic in disguise (observation, no change)

The theorem body is eight literal Nat products — the fusion matrix
itself never appears as an object. This matches the workshop's
established count-theorem convention (S4's `filter_nest_2_of_4`), and
the docstring says so, but seat B records it: the *structural* claim
"N_f² = I" lives in the docstring citation of G5, not in the kernel
statement. A future circle wanting the matrix as an object would need a
Matrix type this zero-import file deliberately lacks. Decision visible,
recorded, honest.

## 3. Independence report (positive finding, no change)

The fork locus was re-derived by expanding ν_FS − ν_ML coefficientwise
(the difference is −2·ri² + 2·rr·ri·i) — NOT seat P's mul_left_cancel
route. Both routes land on the real locus. The ribbon classification
(3 trivial cells + 1 forcing cell reading 1 = r⁴) was re-derived
symbolically and matches the design probe's count. The two ν-ledgers
were computed independently on all four particles and the fork values
match the certificate's G1g exactly: FS {+1,+1,−1,−1}, ML
{+1,+1,+1,+1}. Charter flag 3's "name them apart" is satisfied in the
statements: two defs, two names, divergence a theorem.

— seat B (blind: statements v6 only; bench and seat P proofs unseen)
