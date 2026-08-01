# circle-six-autopsy/ — carried in for the autopsy, NOT admitted

**Provenance: Circle Six, the germinal compartment, prover seat `ylt4ua`.**
Placed here on the principal's explicit instruction ahead of a safety-critical
autopsy, so the material is reachable from every circle rather than trapped in
one repository and one container.

## Read this before citing anything in this directory

Circle Six's founding condition 3 is:

> Nothing leaves this compartment except by being rewritten in a circle where
> the canon applies and something outside the prose decides.

**Nothing in this directory has been through that.** It is a *copy for the
autopsy*, not a crossing. The cumulative record must not cite it as a finding.
`FOUNDING.md` is explicit about why: a compartment with a leaky exit is not a
compartment, it is a second record with a lower standard, and the lower standard
is precisely what makes being wrong free inside it.

If any result here is wanted by this circle, it has to be **rewritten here**,
under this circle's canon, and re-decided by something outside the prose. The
Lean file makes that cheap — it imports nothing and needs no Mathlib.

## Contents

| file | status |
|---|---|
| `AUTOPSY.md` | the failure record, including eight failures by the seat that wrote it |
| `C6_Twist.lean` | 49 theorems, Lean 4.22.0, `EXIT=0`. **Kernel-decided.** |
| `AUDIT.txt` | every declaration, 100/100 depending on **no axiom at all** |
| `forensics/` | runnable evidence for the autopsy's claims |

## What is and is not established

**Kernel-decided:** `conj` is inversion on the units; the reduced pentagon *is*
the seal's `genPentagonHolds` (`pentagon_iff_seal` — without this the rest would
be about a model); the four-row generator table under both actions; the fermion
becoming a σ-coboundary with the gauge exhibited; `sliceCore I` as the
σ-generator the seal's own pentagon rejects; |B³| and |ker d²| both readings;
and the braiding result — the boson braids by ±1 and the fermion by ±i, with σ
exchanging the fermion's two braidings and `SelfInverse` failing for it.

**NOT kernel-decided:** the 65536-symbol sweep (|Z³| = 32 / 64, 8 shared).
Compiler-checked only. Two kernel runs were killed by a container restart. No
theorem depends on them.

## Reproduce

    lean C6_Twist.lean ; echo "EXIT=$?"      # Lean 4.22.0, no Mathlib, ~90s

`native_decide` is deliberately absent: it trusts the compiler rather than the
kernel, and a verdict spent on a faster oracle is not a verdict.
