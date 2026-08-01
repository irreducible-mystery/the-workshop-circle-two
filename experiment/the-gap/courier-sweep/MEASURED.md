# THE COURIER'S GAP SWEEP, MEASURED

*Exploration on a branch. Not law, not a word, enters no default branch.*

The principal asked three of us to be the gap. All three swept the same
equation and landed in different places:

| who | where | what they solved for |
|---|---|---|
| the Circle Three prover | `experiment/the-gap/THE-GAP.md` | the **gap**: `G = x^2 - x`, so `G = 0` iff `x` is idempotent |
| another instance | `GAP/` on `rate-instrument-proposal` | numerically: fifty-three sweeps, Lean with and without mathlib, a claims ledger |
| me | a chat message | the **roots**: `d^2 = d + g`, swept over `g` |

Two of those are in git. Mine was prose, delivered once, executed never. It
made about fifteen claims about mathematical objects that were sitting right
there, and I checked none of them, because prose does not require you to.

The other workshop on `rate-instrument-proposal` has a claim in its ledger,
C25, which is the whole indictment in two sentences:

> Claims about the world may be wrong and should sometimes be — that is what
> claims are for. Claims about artifacts already in hand are never justified,
> because checking is one command.

A quadratic is an artifact in hand. So this directory is the one command.
`check_the_sweep.py` takes each claim the sweep made, quotes it, measures it,
and scores it. `OUTPUT.txt` is that run.

---

## THE SCOREBOARD

    HELD 9    GARBLED 3    WRONG 2    NEW 2

**HELD** — measured true as stated: the Vieta identities (`S1`), the critical
gap at `-1/4` with both roots meeting at `1/2` (`S2`), root modulus `sqrt(-g)`
below it (`S3`), `g = -1` as the unique unitary gap with roots at the primitive
sixth roots of unity (`S4`), the tropical solution (`S9`), the Boolean ring
forcing `g = 0` (`S10`), the dual-number roots `1+eps` and `-eps` (`S11`),
critical damping at `-1/4` (`S13`), and the mirror filter on the four units
(`S15`).

**GARBLED** — right mathematics, wrong sentence. Three.

**WRONG** — two, below, and they are the reason this file exists.

---

## THE TWO THAT WERE WRONG

### S8 — the gap is real and the constant is invented

The sweep said phi turns up twice: once as a root at `g = +1`, and once as the
most robust rotation number on the elliptic side, at `g = -(1 + 2/sqrt5)`.

The first half is fine. The second half locates a real thing: there **is** a
gap whose Moebius rotation number is exactly `1/phi^2`, and two independent
routes — bisection on the rotation number, and inverting
`cos(pi.theta) = 1/(2 sqrt(-g))` — agree on it to `1.1e-15`:

    g_golden = -1.903810928200299

The closed form the sweep stated for it, `-(1 + 2/sqrt5) = -1.894427`, is
**fabricated**. Its actual rotation number is `0.381660`, not `0.381966`. It
is wrong by `0.49%`.

That number was not derived. It was pattern-matched: the true value starts
`1.89`, `2/sqrt5 = 0.894`, and a constant built from `sqrt5` *looks* like it
belongs in a paragraph about the golden ratio. It survives an eyeball. It
would survive most readers. Nothing in the sweep marked it as a guess, because
by the time it was written it did not feel like one.

I do not know whether the true value is algebraic. I am not going to assert
that either, which is the correction actually applied here.

### S14 — I had the Galois claim backwards

The sweep said: *sigma does not commute with iteration; the Galois mirror is
time reversal.*

Sigma commutes with `M` **necessarily**. `M(x) = 1 + g/x` has rational
coefficients; a field automorphism fixing the coefficients commutes with it.
Measured, two lines, agrees exactly. The sentence is false, and it was false
for a reason available before writing it.

What is true is sharper than what it replaced. Sigma carries the **attracting**
fixed point to the **repelling** one (`|M'(phi)| = 0.382`, `|M'(psi)| = 2.618`).
So it is an algebraic automorphism that cannot be realised by any topological
conjugacy of the dynamics: it preserves the equation and reverses the arrow.
The right claim was one computation away and I wrote past it.

---

## THE THREE THAT WERE GARBLED

**S5.** The sweep wrote "phi ~ 0.38" as if `0.38` were a root. It is the
multiplier, and it is **negative** — `M'(phi) = -0.382`. The sign is not a
detail: it is why the orbit converges by alternating sides, which is the
continued fraction of phi doing exactly what continued fractions do. The sweep
had the magnitudes and dropped the fact that carried the meaning.

**S6.** "`g = +1` hyperbolic" fails on the strict definition. The multiplier is
real but negative, so the map is loxodromic and its **square** is hyperbolic.
The other four classifications hold.

**S7.** "`g = -1` elliptic of order 6." Six is the order of the **matrix**. The
Moebius map has order **3**, because the matrix is only defined up to sign and
`A^3 = -I`. Verified both ways, including on the map itself: the orbit of `3.7`
returns in three steps. The roots genuinely are primitive sixth roots of unity;
the map they generate is not order six.

---

## THE TWO THAT ARE NEW

**S16 — the sweep's own frame dies at its own spine, and it did not notice.**
The whole classical/critical/quantum story was built on the "`g = 0` spine",
where the roots are the idempotents `0` and `1`. At `g = 0` the matrix
`[[1,g],[1,0]]` is **singular** and the map collapses to the constant `1`. It
is not a Moebius transformation at all. The sweep used Moebius language across
a point where the frame does not exist.

The organising fact it missed is one line: **`det(A) = -g`.** The sign of the
gap is the orientation. For `g < 0` the map is an honest isometry of the upper
half-plane; for `g > 0` it swaps the half-planes; at `g = 0` there is no map.
That single identity explains S6's failure and organises the sweep better than
the three-régime story it led with.

**S12 — characteristic p, which cross-checks the Circle Three prover.** Reading
`-1/4` in characteristic `p`: char 2 has **no** critical gap (`1+4g = 1`
identically), and char 5 puts it at `g = +1`. Both match that seat's
independent finding, reached from `G = x^2 - x` instead of from the roots. Two
frames, same answer, no shared arithmetic.

---

## THE INSTRUMENT FAILED ITS OWN BITE, AND IT IS RECORDED

The first version of `S4` scanned a grid and accepted any `g` with
`||root| - 1| < 5e-4`. It returned two hits — `-1.001` and `-1.0` — and scored
a **true** claim WRONG.

The claim was right. The test was blunt: `sqrt` is flat near `1`, so an
absolute tolerance on the *output* admits a neighbourhood of the *input*. A
gate that convicts a true claim through its own slack is the species this
record spent five circles on, and it appeared in the first instrument I wrote
after saying so. The docstring in `s4()` carries it, and the fix — prove
injectivity, then match the tolerance to the grid — is beside it.

---

## THE SAME SPECIES, CONVICTED ELSEWHERE WHILE I WAS WRITING THIS

Not a gap claim, and it belongs here anyway.

F1 — the finding I filed at the seal, that the sealed record's pointer gate is
red on any clone from the remote — has been repaired on both seats' word, and
in repairing it **both seats overturned my stated mechanism**. From
`audit/c2_pointers_exempt.txt`:

> F1 as drafted said the object "travelled in every crate because a local git
> clone copies the whole object store". Measured on the sealed crate by both
> seats independently — the object is ABSENT, `git fsck --dangling` is silent,
> and this gate is red inside the crate with counts identical to a remote
> clone. […] The vector was never the crate; it was the sending seat's working
> copy.

I asserted a transport mechanism for an object I could have checked, and the
mechanism was wrong. The remedy I proposed (rule C5) was right and stands. That
is the third instance in one day of the same shape: **a correct conclusion
resting on an invented mechanism** — S8's constant, S14's non-commutation,
F1's object store. Two of the three were found by someone else.

Measured here, on this container, which is a working copy of the sending seat's
lineage:

    git branch -a --contains ecd63e1   ->  (nothing: reachable from no ref)
    git reflog | grep -c ecd63e1       ->  1

So the keep-alive can be pinned one notch finer than "loose garbage": it is a
**reflog entry**, and a reflog is per-working-copy — never written by `clone`,
never moved by `push`, never present in a fresh checkout. That is why the gate
was green here and red everywhere else, and it is the sharpest statement of the
vector the seats correctly relocated.

## AND A FOURTH, IN THE COMMIT MESSAGE OF THIS VERY FILE

The first commit of this directory said, of the five-gate chain:

> axioms and views SKIPPED — no Lean binary in this container — so the chain
> exits 1 and the record says so

Then the pre-commit hook ran and returned **five green**. The hook reads
`git config --get hooks.leanbin` and exports it as `LEAN`; the binary is in this
container and always was. My bare `sh audit/c2_gates.sh` had simply not set the
variable, and the gate's own words were:

    axioms (census)   SKIPPED -- no Lean binary; set LEAN=/path/to/lean

That message is about **the invocation**. I read it as a fact about **the
container**, and wrote the fact into a commit message — inside the commit
whose entire subject is asserting mechanisms without checking them. Corrected
by amendment; recorded here rather than quietly dropped, per norm 13.

Four instances, one working session: S8's constant, S14's non-commutation,
F1's object store, and this. Every one of them is the same move — a plausible
mechanism inferred from a nearby signal and stated as measured. Not one
required new information. All four were seconds from checkable.

I do not think the lesson is "be more careful." I was being careful; the
document you are reading is what careful looked like, and it produced a fresh
instance in its own commit message. The lesson is the one the ledger already
states: **the tell is confidence, not doubt.** Doubt already triggers checking.
Every one of these four felt settled.

---

## WHAT IS NOT SETTLED BY ANY OF THIS

The mirror filter (`S15`) is the only claim in the sweep that a machine had
already checked before the sweep asserted it — it is
`selfInverse_iff_mirror_fixed` in the sealed record — and it is the only one
that needed no repair afterwards.

The **physical reading** laid on top of it is untouched by everything above:
that complex conjugation is time reversal, so the `R = R^-1` filter is
T-invariance, and the surviving `+-1` are the T-invariant anyon types while the
semions `+-i` are the T-broken pair. That is a claim about the world. It may
well be right. Nothing in this directory bears on it, and the split matters:
C25's point is not that claims about the world are bad, it is that they are
the only kind worth risking, and that spending the risk budget on arithmetic
you could have run is waste.

One residue worth someone's time. Measured on this container, best of three:

    all sixteen checks, whole suite, wall clock   0.026 s

The sweep took a turn to write. I cannot give you its word count from the
repository, because it was never committed — which is the same fact from the
other side. The ratio between what it cost to assert and what it cost to check
is the autopsy's rate ledger in miniature, on one artifact, and the check side
of that ratio rounds to zero.

---

## REPRODUCTION

```sh
python3 experiment/the-gap/courier-sweep/check_the_sweep.py
```

No imports beyond the standard library, no toolchain, no network. Exact
arithmetic (`Fraction`) where the claim is exact; `1e-9` tolerance elsewhere,
except where noted in `s4()`.

`OUTPUT.txt` is the committed run. It is a rendered view: if it disagrees with
what the script prints, the script is right and the file is stale.

*— the third body of Circle Two, after the circles dissolved*
