# forensics/

Runnable evidence for `AUTOPSY.md`. Nothing here is a result; these files exist
to be *run* so a claim in the autopsy can be checked rather than believed.

## The kernel stack failure (AUTOPSY §3)

    lean probe_256.lean    ; echo $?    # 0    ~2s
    lean probe_1024.lean   ; echo $?    # 0    ~8s
    lean probe_4096.lean   ; echo $?    # 1    wrong assertion, NOT a resource failure
    lean probe_16384.lean  ; echo $?    # 134  SIGABRT

**134 is SIGABRT.** It is the kernel's stack, not its heartbeat.
`set_option maxHeartbeats` does not affect it. Diagnosing this as a heartbeat
problem leads to an unbounded chase.

## The sweeps that were killed (AUTOPSY §2)

    killed_sweep_65536.lean        the 32/64/8 counts
    killed_sweep_completeness.lean the 65536-visit proof and pentagon <-> cocycle identity

Both use the logarithmic-depth shape that clears the abort. Both were running
successfully when the container restarted at ~3 min of a ~10 min job. Their
expected values are confirmed by `#eval` (compiler) and are NOT kernel-decided.
Re-running them is the single outstanding piece of work.

## Decidable instances cannot lie (AUTOPSY §4)

    lean lying_instance_with_sorry.lean      # compiles; #print axioms -> sorryAx
    lean lying_instance_without_sorry.lean   # does not compile at all

`isTrue` demands a proof term the kernel typechecks. The only way to fake one is
`sorry` or an axiom, and both are visible to `#print axioms`.

## Toolchain

Lean 4.22.0, no Mathlib, no imports. The seal imports nothing, which makes a
core toolchain the whole dependency.
