# Circle Six — failure record, prover seat `ylt4ua`

Written for the autopsy, by the seat that produced the failures in §1. Every
figure here is reproducible from this repository; where something is
second-hand it is marked **REPORTED** and is not evidence.

---

## 1. This seat's own failures, in order

Six were already declared in `ROUND-ONE.md`. Two more happened after it was
written. All eight are below because a failure record that omits the author's
is a testimonial.

| # | failure | how it was caught | cost |
|---|---|---|---|
| 1 | Ran four instruments and wrote "all four gates green." There are **five**; `c5_tree_attest.py` was never run. | counter-prover's independent count | wrong claim published |
| 2 | Reported `authored prose: 3490` from `inheritance_budget.sh` — inflated by this seat's own uncommitted files sitting in the tree being audited. | re-measuring tracked-only | wrong figure published |
| 3 | Took a 4-word count discrepancy for a disagreement. It was `wc -w` dropping bare multibyte tokens in a byte locale. | isolating the tokens | ~10 min; became finding §4 of ROUND-ONE |
| 4 | Reported a generator from an arbitrary `min` tie-break. `i` and `-i` are one class. | noticing the tie-break was in the output | wrong-shaped claim |
| 5 | Published "31 stripped names." There are **32**; the filter required an underscore or apostrophe to recognise a proof name, so `z3ext` was dropped for having the wrong *shape* rather than for resolving. | counter-prover's list | wrong figure published |
| 6 | Published "69 occurrences." That is the count of `_` placeholders. **A verification run explicitly warned the coincidence would read as a copy error, and this seat carried it anyway.** | re-counting | wrong figure published |
| 7 | Printed `CLEAN-CLONE COMPILE EXIT=0` when the clone had **failed on auth** and the `cd` fell through, so it compiled the working tree. A false green, self-inflicted, in a verification step. | reading the output instead of the exit code | caught before publication |
| 8 | Asserted `sweep2`'s expected tuple in a kernel job before ever evaluating it. Would have burned a ten-minute kernel run on a guess. | checking with `#eval` first | caught before running |

**The species that recurs: a marker standing in for a property.** #3 (`>` for
carried prose), #5 (name *shape* for name *resolution*), #6 (a coincidental
count for the count), #7 (printed text for exit status). Four of eight. This is
the same species `FOUNDING.md` already convicts twice in the carried
instruments, and `CHARGE.md`'s footnote convicts once more.

**Failure #7 is the safety-relevant one.** It is the only one where the checking
apparatus itself emitted a green that meant nothing. Everything else was a wrong
number; #7 was a wrong *verdict*.

## 2. Environmental failures

- **Container restart killed two kernel sweeps** at ~3 minutes of a ~10 minute
  job. Nothing was lost permanently only because the non-sweep results had been
  banked — but at the moment of the restart the entire Lean corpus existed only
  in a session-local scratchpad and had never been committed. **That was a
  choice, not an accident, and it was the wrong one.** Work is now committed as
  soon as it compiles.
- The 65536 sweep is **still not kernel-decided** as a result. `lean/C6_Twist.lean`
  says so in its header and no theorem depends on it.

## 3. The kernel failure mode, reproduced

This cost hours across two seats and is the single most transferable finding
here, so it is committed as runnable evidence in `forensics/`.

```
probe_256.lean    -> exit 0    2.3s
probe_1024.lean   -> exit 0    8.3s
probe_4096.lean   -> exit 1   20.2s     (wrong assertion, not a resource failure)
probe_16384.lean  -> exit 134 42.9s     SIGABRT
```

`exit 134` is **SIGABRT — the kernel's stack, not its heartbeat.** The pattern
is the obvious unary recursion:

```lean
def countUpTo (p : Nat → Bool) : Nat → Nat → Nat
  | 0,   acc => acc
  | k+1, acc => countUpTo p k (if p k then acc + 1 else acc)
```

**`set_option maxHeartbeats` does not touch it and never will.** A seat that
diagnoses this as a heartbeat problem will add heartbeat options indefinitely
and the abort will not move. The fix is to change the recursion shape so depth
is logarithmic:

```lean
def sweep : Nat → Nat → Counts
  | 0,   lo => at1 lo
  | d+1, lo => Counts.add (sweep d lo) (sweep d (lo + pow2 d))
```

Depth 16 instead of 65536. Depth 12 kernel-decides in 37s; the same shape at
depth 16 was running successfully when the container restarted. Also decode each
symbol **once** into a structure rather than dividing per access.

## 4. What a green means here, and what it does not

`EXIT=0` on a Lean file means the kernel accepted every proof in it. It does
**not** mean the theorems say what their names suggest, and it does not mean the
file covers what a reader assumes. Two guards are in place and both are
mechanical:

- **`pentagon_iff_seal`** — the reduced pentagon that gets swept **is** the
  seal's `genPentagonHolds`, admissibility guard and Int label arithmetic
  included. Without it a green would certify a statement about a model of the
  seal rather than the seal.
- **`lean/AUDIT.txt`** — every declaration in the file, not a sample: 100
  declarations, **100 depending on no axiom at all**. No `propext`, no
  `Classical.choice`, no `Quot.sound`, no `sorryAx`, no `native_decide`.

`native_decide` is deliberately absent. It trusts the compiler rather than the
kernel, and a compartment whose only rule is "something outside the prose
decides" cannot spend its verdict on a faster oracle.

**The one decision point that is not an axiom**, stated because it is the only
one: every `decide` routes through two hand-written `Decidable` instances. They
cannot lie — `isTrue` demands a proof term the kernel typechecks. This is
demonstrated rather than asserted, in `forensics/`:

```
lying_instance_with_sorry.lean     -> compiles, and #print axioms reports sorryAx
lying_instance_without_sorry.lean  -> does not compile at all
```

So a hidden decision must surface as an axiom, and the audit reports zero.

## 5. Second-hand material — REPORTED, not evidence

The following reached this seat only as a pasted transcript of another seat's
session. It is recorded because it is autopsy-relevant and because the failure
mode in §3 corroborates part of it, but **this seat did not observe any of it**
and none of it should be treated as established:

- **REPORTED:** a workflow deadlocked because two long-running agents were given
  a schema forcing a final structured-output call, hit their limit before
  emitting it, and therefore never returned — an unresolved promise rather than
  a throw, so the barrier waited indefinitely. Nothing errored; it hung quietly.
- **REPORTED:** agent concurrency capped at `min(16, cores − 2)` = **2** on a
  4-core box, so two hung agents blocked everything queued behind them.
- **REPORTED:** ~30 minutes spent adding heartbeat options to a file failing
  with `(deterministic) timeout at whnf, maximum heartbeats`. §3 is the reason
  that can be an unwinnable chase if the underlying failure is the stack.

**Where this seat's own record bears on it:** failure #7 above is the same
species as a hung agent reported as progress — an apparatus emitting a signal
that does not mean what it appears to mean. That species appears on both sides
of this compartment.

## 6. State at the time of writing

| | |
|---|---|
| kernel-decided | 49 theorems, `lean/C6_Twist.lean`, EXIT=0, 100/100 declarations axiom-free |
| compiler-only (`#eval`), NOT kernel | the 65536 sweep: \|Z³\| = 32 / 64, 8 shared, `pentagon ↔ isCocycle false` across the space |
| Python-only | everything in `probe/`, superseded where `lean/` covers it |
| through the exit | **nothing** |

The forfeit in `FOUNDING.md` still applies in full: if nothing leaves through
the exit by the time Circle Five seals, this compartment produced nothing and
lapses. A kernel-decided result inside the compartment is not an exit.
