# The GAP

    ◇² = ◇ + G

One equation. `G` is the **gap** — a free parameter, swept over every number
system that will hold it. Everything below is about what happens to the two
roots as `G` moves.

---

## The two invariants

For any two distinct roots `x`, `y`:

    x + y = 1                    ALWAYS, every gap, every ring
    x · y = -G                   ALWAYS
    (x - y)² = 1 + 4G            the discriminant IS the squared distance

**`φ + ψ = 1` and `φ × ψ = −1` are not facts about the golden ratio.** They are
the case `G = 1` of a law that holds at every gap. Kernel-proved:
`lean/Vieta.lean`.

## The branch point

`1 + 4G` vanishes at **`G = −1/4`**, and the third identity above says exactly
what that means: **the two roots collide.**

    over ℝ    1 + 4G = 0 ↔ G = −1/4, and then x² = x − ¼ ↔ x = ½   (unique)
    over ℤ    1 + 4G = 0 has NO solution, and 2x = 1 has NO solution

The branch point is **present and unique in ℝ** and **absent from ℤ**. Both
proved. So:

> **−1/4 is not a property of the equation. It is a property of the equation
> together with the number system it is asked in.**

`lean-mathlib/Branch.lean`, `lean/Reflexive.lean`.

## What −1/4 is, in twelve dialects

| reading | what −1/4 is there |
|---|---|
| algebra | discriminant zero; the roots collide |
| Galois | where the involution loses its internal witness |
| analysis | a branch point whose **monodromy is the mirror** |
| deformation | derivative zero — Hensel, dual numbers and Grassmann all report it |
| geometry | where the solution variety becomes reducible |
| ODE | **where the logarithm is born** (`r^{1/2}` and `r^{1/2} log r`) |
| scaling | continuous → **discrete** scale invariance; a scale appears from a scale-free equation |
| spectral | the **ground-state energy**: `A² − A ≥ −¼` for every self-adjoint `A`, sharp |
| band theory | a **van Hove singularity** — the density of states diverges as `(g+¼)^{-1/2}` |
| dynamics | the **tangent bifurcation**; the **cusp of the Mandelbrot set**; logistic `r = 1` |
| combinatorics | the **Catalan radius** — the `4ⁿ` in the tree-counting asymptotic |
| continued fractions | the convergence boundary; **rotation number zero** |

And two number systems where it does not exist at all:

- **characteristic 2** — `x² + x` is additive, so no gap ever has a double root.
  The obstruction becomes a **parity**: exactly half the gaps are unreachable.
- **the tropical semiring** — `1 + 4G` needs a subtraction max-plus does not
  have. There is **at most one root for every gap**, so there is nothing for a
  mirror to exchange. **Chirality requires subtraction.**

Both kernel-proved: `lean/ArtinSchreier.lean`, `lean/Tropical.lean`.

## Above and below

    G > -1/4    two REAL roots. Orderable. An observer inside can say which is larger.
    G = -1/4    one root, 1/2. Nothing to tell apart.
    G < -1/4    a CONJUGATE PAIR. No larger. Only a convention separates them.

Below the branch point the gap alone fixes the size: **‖z‖² = −G**, so the
common modulus is `√(−G)`. At `G = −1`: **z³ = −1, z⁶ = 1, ‖z‖ = 1** — the roots
are primitive sixth roots of unity. `lean-mathlib/Modulus.lean`.

## The mirror grows with the room

Solving `x² = x + G` for `G < −1/4`:

| algebra | dim | solution set |
|---|---|---|
| ℝ | 1 | **nothing** |
| ℂ | 2 | **2 points** — a conjugate pair |
| ℍ | 4 | **a 2-sphere** |
| 𝕆 | 8 | **a 6-sphere** |
| sedenions | 16 | **a 14-sphere** — and zero divisors change nothing |

Over ℂ no element conjugates `i` to `−i`: the mirror is **outer**.
Over ℍ, `j·i·j⁻¹ = −i`: the mirror is **inner** — a rotation.

> **Chirality is what an observer calls a sphere it is too small to turn.**

The mechanism is one theorem: **every imaginary component `t` of a solution
satisfies `(2·Re(x) − 1)·t = 0`.** Either the real part sits exactly at the
collision, or the imaginary part vanishes. Over a field containing `½` the first
branch opens and you get the sphere; over `ℤ` it cannot, so every solution is
real and **the sphere is absent rather than unfound.** `lean/Quadratic.lean`.

## Each named gap is the collision, somewhere

    -1/4 ≡ +1  (mod 5)      the GOLDEN gap IS the collision in characteristic 5
    -1/4 ≡ -1  (mod 3)
    -1/4 ≡  i  (mod 17)

Verified as double roots: char 5 `G=1` → unique root 3; char 3 `G=−1` → unique
root 2; char 17 `G=4` → unique root 9. And the sharpest one:

> **Both `4` and `13` square to `−1` mod 17, and only one of them is the
> collision.** Which one you call `i` decides which — and nothing inside the
> field decides it for you.

`lean/Characteristic.lean`.

## Variation cannot beat commitment

For gaps drawn from `{+G, −G}`, under **every** schedule — random, periodic,
quasiperiodic, adversarial, or clairvoyant:

    |f_n|  ≤  the constant-gap-G recurrence, term by term

and the constant schedule **attains** it. For `G = 1` that bound is exactly the
Fibonacci numbers, so **nothing ever exceeds `φ`.** A gap that can see the whole
future gains nothing over one that reads only the present sign.

`lean/Ceiling.lean`, `lean-mathlib/GeneralCeiling.lean`.

The floor is the same formula at the other gap: **ceiling `s₊(G)`, floor
`|s₊(−G)|`**, both attained by constant schedules — *for symmetric gap sets.*
Break the symmetry and a **word** beats every constant. (Computed, not proved.)

## The object and its own time-evolution obey the same law

The transfer matrix advancing the system one step satisfies

    M² = M + g·I

— **the gap equation itself**, by Cayley–Hamilton. That is why every scheduling
question collapses back onto the same two roots. `lean-mathlib/TransferWord.lean`.

And the determinant identity, in sequence form with no matrix machinery:
`W(n+1) = −sₙ·W(n)`. For unit gaps the Casoratian never changes size, so **two
independent solutions stay independent forever** — growth and decay are locked
together and no schedule can make both decay. `lean-mathlib/Casoratian.lean`.

## The one thing that exists only at −1/4

In `ℝ[ε]/(ε²)`: **`½ + ε` solves the gap equation at `G = −¼`**, and conversely
**any solution with non-zero nilpotent part forces `G = −¼` and `Re = ½`.**

The Jordan block, the logarithm in the ODE, and the blocked first-order
deformation are one object. `lean-mathlib/Golden.lean`.

And the contrast beside it: **the golden gap's root is irrational; the
collision's root is exactly `1/2`.** The gap at which the object can no longer
tell its own roots apart is the one whose root is simplest.

---

# How to attack this

**107 theorems. 66 in core Lean, 41 with Mathlib. Every file exits 0. The axiom
census carries `propext`, `Classical.choice` and `Quot.sound` and nothing else —
no `sorryAx`, no `ofReduceBool`.**

    cd lean && sh check.sh                                  # core, no dependencies
    cd lean-mathlib && MATHLIB=<built mathlib4> sh check.sh  # needs Mathlib 4.22.0
    python3 sweeps/sweepN.py                                 # any sweep, standard library only

**The seams, named, so you do not have to find them:**

1. **`sweeps/` is computed, not proved.** Nineteen scripts. The exact results
   (characteristic collisions, Catalan coefficients, reflexive conditions,
   Cayley–Dickson identities, tropical counts) are integer or rational
   arithmetic. The numerical ones (monodromy, zero spacings, winding parities,
   Lyapunov exponents, orbits) agree with prediction to the digits shown and
   **no further claim is made for them.**

2. **Not proved at all, and these are stopping points rather than oversights:**
   the **joint spectral radius** for asymmetric gap sets (a limsup over all
   words; attainment by a periodic word is the finiteness property, false in
   general); the **Lyapunov and large-deviation results** (Viswanath's constant,
   the three growth rates, the rate function — ergodic theory); the **Catalan
   coefficient extraction** (formal power series).

3. **Three claims in the sweeps were wrong and are corrected in place, not
   deleted.** Sweep 69 and 70 retract two summary lines contradicted by their own
   tables. Sweep 25 retracts a third. The corrections are the interesting part.

4. **The kernel refused four things I had asserted in prose:** a quaternion claim
   stated without its hypothesis; `Fin 8` root counts asserted from memory (I had
   conflated `x² = 1`, which has four roots mod 8, with the gap equation, which
   has two); a `decide` with no enumeration instance; and a constant that does
   not exist in this Mathlib build. **Three of the four left `sorryAx` in files
   that still exited 0** — the census was the only thing that saw them.

5. **Where a number is stated, the code that produced it is here.** If a number
   in this README disagrees with the script, **the script wins.**

`provenance/` holds the complete session transcript, the failure record, the
claims ledger and the timestamps. The mathematics does not depend on any of it.
