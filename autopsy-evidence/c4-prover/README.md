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
