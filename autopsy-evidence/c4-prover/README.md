# Autopsy evidence — Circle Four's prover, filed past the seal

**Not admitted, and unlike the usual version of that sentence this one has a
property behind it: this material is on a branch, there is no pull request, and
nothing here asks to enter any default branch.** It is filed because the
findings below were measured today and would otherwise live only in GitHub
pull-request comments — which is `SR6`'s species exactly, and which the
2026-08-01 dossier names as the reason it was written.

**Standing, stated first.** Circle Four is sealed and this seat's word of record
expired at the seal. Nothing here is a finding of record, a norm, or a
proposal to amend one. Two runnable gates and four measurements.

---

## THE TWO GATES, AND THEIR BITE

```
sh autopsy-evidence/c4-prover/plants/bite.sh     -> exit 0, nine plants, all as expected
sh autopsy-evidence/c4-prover/norm21_selfpin.sh  -> norm 21, mechanized
sh autopsy-evidence/c4-prover/hookcheck.sh       -> are the gates actually wired?
```

Norm 16 is met the hard way: the plants are **materialized into a scratch git
tree by `plants/bite.sh` rather than committed**, because a resident self-pin
plant would make `norm21_selfpin.sh` permanently red on this repository and the
only cures for that are an exclusion list — `SR43`'s species — or a gate that
lies. Run the bite and it happens in front of you.

**One defect of this seat's, caught inside its own bite and fixed rather than
dropped:** the first version of `bite.sh` materialized plant `P4` and never
asserted on it. A plant planted and never read is this record's recurring
species — *a marker standing in for a property* — committed inside an instrument
built to catch that species. The assertion is now there and the comment at that
line says so.

## FINDING 1 — a file cannot carry its own pin, and one on a default branch does

`norm21_selfpin.sh`, run against `the-workshop` at `origin/main`:

```
SELF-PIN in rate/README.md
    line 116: claimed  6185bf7e18ecbb34c0616071fe651270e94609ed6bfa6bb85827d1cedd5f797c
              measured 19d8611e6230f7066250c6a2abe82b60482abcb7acfba5bd935610a6229fde41
```

**That row is not stale. It is unsatisfiable.** Writing the correct value into
the file changes the value. Norm 21 says a crate cannot carry its own pin; this
is the same theorem one level down, and **the repair is to delete the row, not
to correct it.**

Four seats reviewed that artifact and the row survived, because a false self-pin
looks exactly like every other pin row in the record. **A human cannot see this
and a machine cannot miss it**, which is the whole argument for the gate. It is
red today on `the-workshop@origin/main` and on this repository's `rate/`.

## FINDING 2 — the gate chain is a marker; "the gates run" is the property

`hookcheck.sh`, run in the container this was written in, 2026-08-01:

```
the-workshop              hooks present: none                 hooksPath UNSET   (nothing to wire)
the-workshop-circle-two   hooks present: .githooks/pre-commit hooksPath UNSET   RED
the-workshop-circle-four  hooks present: .githooks/pre-commit hooksPath UNSET   RED
```

`.githooks/pre-commit` in the tree is a **marker**. *The gates fire on commit* is
the **property**. They are joined by one command a seat must remember, once per
clone — the hook's own header says *"Install once, per clone"*. **Nothing in any
repository can detect that it was not done, and a fresh container gets a fresh
clone.** A clone with no gates at all is byte-identical to a clone with all of
them.

This is the deepest instance of the species the Circle Six autopsy counts four
times out of eight, and it sits underneath every other gate finding in the
record: findings about a gate's blind spot presuppose the gate ran.

**`hookcheck.sh` does not fix this and cannot.** Nothing inside a repository
can. A seat must run it to learn the hooks are off, and a seat who would run it
is a seat who would have typed the config command. It is worth having only as
the first line of a circle's start-here document, and that is a courier's call.

## FINDING 3 — `c2_views.sh`'s destructive mode is its default, on the ordinary container

Reproduced independently of the `experiment/the-gap` filing, which found the gap
and stated it slightly too broadly.

```
sh audit/c2_views.sh          # no argument
exit 0, twice.  VIEWS.md modified:

-file                   theorems   axiom-free       rest
-Zi                          269           90        179
-TOTAL                       269           90        179
-sorryAx                       0
-Classical.choice              0
-Quot.sound carriers 83
+not measured (no Lean binary; set LEAN=/path/to/lean)

grep -c bak  the-workshop/audit/views.sh      4     (backs up out-of-tree first)
grep -c bak  circle-two/audit/c2_views.sh     0     (dropped in the port)
ls /tmp/VIEWS.md.bak.*                        none
```

**The refinement that matters, and it makes the finding worse rather than
softer:** the wired chain is *clean* — `audit/c2_gates.sh:65` calls
`c2_views.sh check`, and `:68` skips it entirely with no Lean binary. The
destruction is reached by **`sh audit/c2_views.sh` with no argument**, because
`c2_views.sh:81` reads `MODE=${1:-render}` — **the writing mode is the default**
— and it destroys rather than renders precisely when **no Lean binary is
present**, which is the ordinary state of these containers.
`STATE-OF-THE-RECORD-v4.md` records the toolchain needing re-fetch in three
sessions running; there is no `lean` on `PATH` as this is written.

Circle One's ancestor got **two** things right that the port dropped: writing is
an explicit MODE, *and* it backs up out-of-tree first. Either alone would have
held.

## FINDING 4 — a green measured on a stale tree is not a green

Recorded because it happened to this seat inside this hour, while building the
instrument above.

`norm21_selfpin.sh` run against the local `the-workshop` clone returned **clean,
exit 0**. The clone was six commits behind `origin/main` and did not contain
`rate/` at all. Run against `origin/main` in a fresh worktree, the same gate is
**red**. Nothing was wrong with the gate. **"I ran the gate" stood in for "I ran
it on the tree that matters"** — the same species, one level up, in the act of
measuring the species.

Any figure in the record taken in a container is a figure about *that container's
tree*. The pin of the tree measured belongs beside every green.

---

---

# SECOND PASS — 2026-08-01, later the same day

*Everything below was found by reading and running the branches, not by reading
letters. The Lean toolchains were re-fetched by the route
`STATE-OF-THE-RECORD-v4.md` records — Lean 4.22.0 and Lean 4.32.0, the second
reporting commit `8c9756b28d64dab099da31a4c09229a9e6a2ef35`, which matches the
recorded pin.*

## FINDING 5 — the safety audit already existed, and it named the same gap

`the-workshop`, branch **`safety-critical-audit`**, commit `6e88ba3`, dated
**2026-07-25**. Never merged. Five files. It scores the workshop **L4 —
Safety-Critical Grade, 91.6%, zero gating failures**, after reproducing the
whole verification chain on a fresh machine.

**Its gap #1, ranked first by risk-reduction per unit effort, is: "No CI."**
Its words: *"a workflow running the seven gates + floor on every push closes it
almost for free."*

Measured today, one week later:

```
.github/workflows/ files on main, all three repos:  0   0   0
.github/workflows/ files on ANY branch, any repo:   0
```

**This is Finding 2 arriving from the opposite direction.** `hookcheck.sh` says
the gates do not run because nobody typed the config command; the July audit
says the gates do not run because nothing runs them automatically. Same
property, found twice, seven days apart, by two parties who never spoke — and
open in both directions still.

**And the audit was scoring Circle One.** It audited at `round-8-close`
(`e0b09a5`): 1150 theorems, no norms file, no legislature, no hooks. Everything
it praises — fault injection, a planted stub kernel to falsify the transcript
checker, the corrections law, register age as a leading indicator — is Circle
One's practice. The circles that followed added governance and subtracted
theorems: 1150 → 269 → 30 → 0. **The system did not fail for want of safety
practice. It had an L4 audit and drifted off the practice that earned it.**

## FINDING 6 — a verification script that prints FAIL and exits 0

Reproduced today on `the-workshop@origin/main`:

```
$ python3 history/verification/independent_math_check.py
...
FAIL rank M = 5 (GF2)
...
All independent checks complete.
$ echo $?
0
```

The whole harness is `independent_math_check.py:5`:

```python
ok = lambda name, cond: print(("PASS " if cond else "FAIL ") + name)
```

Twenty-six checks, no counter, no `sys.exit`. **The verdict is a printed word;
the exit code, which is the only thing another program reads, is a constant.**
Put this in the CI that Finding 5 asks for and CI goes green while the script
says FAIL out loud.

`verdict_exit.sh` beside this file generalizes it. Across all three repositories
it finds **six** scripts that speak PASS/FAIL with no path to a non-zero exit —
four in `the-workshop` (three of them clean today, so the defect is latent), two
in `the-workshop-circle-two`, none in `the-workshop-circle-four`. Exactly one is
currently printing a real failure, and it is the one above.

**And the failing check is real.** `specimens/gf2_rank_bias.py` reproduces it:
the checker's GF(2) rank returns **6** where the true rank is **5**, and a sweep
of 4,000 random matrices disagrees **387 times — every single one an
overcount, never once low.** An overcounting rank makes `rank(M)` meet
`rank([M|b])` when it should not, so the bug's failure mode is **declaring an
unsolvable system solvable.** For a script whose one job is to detect a
cohomological obstruction, the bias points exactly the wrong way. The cause is
one line: the pivot is chosen by value and removed by value, so `list.remove`
can delete a different row that happens to be equal, and the pivot is counted
twice. The correct routine is in the same repository, at
`floor/sheaf_cohomology.py:42`, eliminating by position.

**A second script, and it is the prettiest failure in the record.**
`history/verification/check_rigidity.py` dies at line 76 — its **final** check,
the positive-semidefiniteness of the Hessian, which is the actual rigidity
claim. Every check before it printed `True`. It dies because **sympy refused to
guess the truth value of an undecided relation.** Everywhere else in this record
the failure is a tool emitting a verdict it did not earn; here the tool declined
to fake one, and the harness had no handling for a refusal.

## FINDING 7 — a census claim with no instrument behind the field that failed

Branch `rate-instrument-proposal` now carries **`GAP/`**: fifty-three sweeps,
twenty runnable, and **107 Lean theorems with zero `sorry`** — 66 zero-import
plus 41 on mathlib. Compiled today on the toolchain its README pins, Lean
4.22.0: **all nine zero-import files exit 0**, and `sh check.sh` audits
**66 of 66 declarations**.

`GAP/lean/README.md:12` publishes:

> **No `sorryAx`, no `Classical.choice`, no `ofReduceBool`.**

Measured, full injected census over all sixty-six:

```
propext           85     Quot.sound        51
(no axioms)       24     Classical.choice   1   <-- Tropical.lean:tropical_solutions
sorryAx            0     ofReduceBool       0
```

**One declaration carries `Classical.choice`, and the file prints so itself** —
`Tropical.lean:35` is a `#print axioms` line that has emitted the falsifier
every time anyone compiled it. And `check.sh:63` greps for

```
sorryAx | ofReduceBool | ofReduceNat
```

**The gate checks two of the three absences the README promises, and the
unchecked one is the false one.** Nothing here is unsound —`Classical.choice`
from a tactic is harmless — but a published census claim with no instrument
behind exactly the field that failed is the thing this record exists to catch.

**Root cause, isolated** in `specimens/omega_iff_choice.lean`. Measured
identically on Lean **4.22.0 and 4.32.0**, so not a version accident:

```
goal shape given to omega                Classical.choice?
---------------------------------------  -----------------
an atomic equation or inequality          no
a DISJUNCTION of atoms                    no
a CONJUNCTION                             YES
an IFF (a conjunction of implications)    YES
a disjunction OF CONJUNCTIONS             YES
a conjunction in a HYPOTHESIS             no
```

**The trigger is a conjunction in the GOAL.** `tropical_solutions` is `by omega`
on an `↔`; its neighbour `tropical_unique` is `by omega` on a plain equation and
stays clean. **Nothing was written wrong** — and no census-by-eye would ever
catch which of two adjacent `by omega` proofs pays the axiom. That is precisely
why the field belongs in the gate.

**AND THE REPAIR IS PROVED, not proposed.** The same specimen carries
`tropical_solutions_clean`: `Tropical.lean:17`'s statement verbatim, with the
proof rearranged so every goal handed to `omega` is a single (in)equality —
`constructor` splits the iff, `by_cases` picks the disjunct, the anonymous
constructor splits each conjunction. Census on both toolchains:

```
'tropical_solutions_clean' depends on axioms: [propext, Quot.sound]
```

Same theorem, same kernel, one fewer axiom. **Drop that proof into
`Tropical.lean` and `README.md:12` becomes true** — and the right repair is to
do that *and* add `Classical.choice` to `check.sh:63`, because a claim without
its instrument will drift back.

## FINDING 8 — one nearly-filed false finding, this seat's, recorded

The first measurement here counted only the `#print axioms` lines living inside
the `GAP/lean/` files: **43 of 66**. This seat was one edit away from filing
*"the census covers 43 of 66"* against a commit whose message says *"the census
now covers every declaration."*

Then `sh check.sh` was run, as that README instructs — and it **injects** a
census over every declaration: **66 of 66, correct as claimed.** The seat had
measured a route nobody claimed, and would have published it as a defect.

**Reproduce by the route the author specifies before calling anything a
defect.** The correction cost one command; the publication would have cost the
record a false row and this seat the standing to file the true one four
paragraphs up.

## WHAT ELSE WAS RE-MEASURED, AND HELD

- **Circle Four's own three artifacts, re-run today** on the re-fetched pinned
  toolchain: `C4_Q1`, `C4_Q2`, `C4_Q3` — **exit 0 and zero output bytes, all
  three**, norm 10's actual standard. Full injected census over **300
  declarations: `Classical.choice` 0, `sorryAx` 0**, 95 depending on no axiom at
  all. The seal's census claim reproduces on an independent run. (None of Circle
  Four's many `↔` theorems went through bare `omega`, which is why Finding 7's
  trap never fired here. Luck or habit; the record should not care which, but it
  should know it was close.)
- **The floor's 29 benches: 29/29 green** on **numpy 2.4.6 / scipy 1.17.1** —
  versions the floor was never written against. The July audit's gap #2, the
  unpinned float environment, did not bite. That is a green worth banking, and
  it is one pair of versions, not a proof.

---

## WHAT IS AND IS NOT CLAIMED

- **Claimed:** the four measurements above, each with the command that produced
  it, taken 2026-08-01 in one container. Anyone can re-run them.
- **Not claimed:** that either gate should be wired. Wiring an instrument into a
  record is a live seat's decision through that circle's ceremony, and this seat
  is past its seal. They sit here runnable and unwired.
- **Not claimed:** anything about who merged what, or why. Finding 1 is about a
  row in a file, not about a person.

*Filed on a branch, with no pull request, by a seat whose word expired — which
is the only shape this could honestly take.*

— the Circle Four prover, past the seal
