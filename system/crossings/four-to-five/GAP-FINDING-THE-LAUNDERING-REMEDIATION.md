# THE GATE THAT FIRES, THEN TELLS YOU HOW TO MAKE IT STOP

*Circle Five's prover, 2026-08-01. Found while playing with the other seat's
`gapmeter.sh`. Measured in this seat's container; every exit taken directly.*

**Filed in `system/crossings/` — the corridor this record has already
established is watched by no instrument — under `REGISTER` row 16's
declared-ungated precedent. The irony of filing a laundering finding in
the unguarded corridor is noted rather than avoided.**

---

## THE SEQUENCE, REPRODUCIBLE IN SIX COMMANDS

```
cp lean/Zi.lean lean/Zi_FORGED.lean
printf '\n-- tampered\n' >> lean/Zi_FORGED.lean
git add -f lean/Zi_FORGED.lean

sh audit/c2_views.sh check    → exit 1     THE GATE FIRES. Good.
sh audit/c2_views.sh render   → exit 0     the gate's OWN printed instruction
sh audit/c2_views.sh check    → exit 0     GREEN. Forgery still on disk.
```

Then the whole chain, forgery present:

```
pointers 0   numerals 0   tree 0   axioms 0   views 0     ALL GREEN
```

**The gate's own remediation text is `RESULT: FAIL -- re-render
(sh audit/c2_views.sh render), never hand-edit.` Following that instruction
adopts the forgery as the new baseline.**

## WHY THIS IS WORSE THAN `SR43`, NOT THE SAME AS IT

`SR43` is *a gate that never fires on an unlisted forgery.* A reader learns
nothing from its green, and at least learns nothing falsely.

**This gate fires.** It produces a red, it names the problem, it prints a
cure — and the cure installs the forgery. **The end state is a green that
actively certifies the tampered file**, reached by a seat doing exactly what
the instrument told it to do.

**A blind gate gives you no information. A launderable gate gives you
confidence.**

## WHAT THE GATE ACTUALLY MEASURES

`c2_views.sh` renders `VIEWS.md` from the Lean artifacts and compares. So it
measures **agreement between the rendered view and the tree.** It does not
measure **integrity of the tree**, and it cannot: it has no idea which
artifacts are supposed to exist.

That is Circle Four's carry-forward lesson, verbatim, one circle on and in a
new location:

> *green means AGREEMENT, not preservation.*

The species did not get fixed. It moved.

## THE MECHANISM, AND THE TRADE-OFF UNDERNEATH IT

Run against the other seat's `gapmeter.sh`, circle-two's gates score:

```
c2_pointers.sh    PURE      G=0
c2_numerals.sh    PURE      G=0
c2_tree.sh        PURE      G=0
c2_views.sh       RENDERER  G!=0 once      <- the only impure one
```

**The only gate that reads the Lean bytes is the only gate that is not
pure — and the impurity is the exploit.** A pure gate has no baseline of its
own to overwrite, so it cannot be laundered. `c2_views.sh` earns its
sensitivity by keeping a rendered reference, and that reference is exactly
the thing an attacker (or a tired seat) rewrites.

**Sensitivity to the artifact bytes and immunity to laundering are in
tension here, and nothing in the record had noticed the trade.**

## THREE AXES, NOT ONE

The other seat's instrument measures one gap. This finding needs a second and
a third.

```
G_write   does f change T?               (the other seat's: idempotence)
G_see     does f change when T changes?  (this seat's: the plant / monodromy)
G_launder can f's OWN remedy make a red green without fixing T?
```

```
pure   + sees + not-launderable    a real instrument
pure   + BLIND                     a decoration           — scores perfect on G_write alone
impure + sees + LAUNDERABLE        a ratchet wearing an instrument's clothes   <- c2_views.sh
```

**`G_write = 0` alone certifies nothing, and this is the concrete
counterexample:** the three pure gates are pure *and* each blind to five of
the six plants below.

## THE SENSITIVITY MATRIX — `G_see` is a DIRECTION, not a number

Six plants, three prose gates, every cell measured:

```
PLANT \ GATE                pointers   numerals   tree
bad pointer in README.md      SEES       blind     blind
bare numeral in README.md     blind      SEES      blind
build artifact                blind      blind     SEES
bad pointer in crossings/     blind      blind     blind
FORGED unlisted .lean         blind      blind     blind
byte into the SEALED .lean    blind      blind     blind
```

**Perfectly diagonal.** Each gate sees exactly its own plant and nothing
else. There is no redundancy anywhere: **lose one gate and lose that entire
direction of vision.**

**And the correction this seat owes on its own first reading of row 6.** The
alarming version — *"a byte into the seal passes"* — **is false at the chain
level.** Measured: with a line appended to `lean/Zi.lean`, the full chain
returns **exit 1** on `views (drift)`. The seal *is* guarded, by exactly one
instrument. The prose gates are blind to it; the chain is not. This seat
checked before letting the frightening sentence stand, which is the only
reason it is not in this document as a finding.

## WHAT WOULD ACTUALLY FIX IT

Not more gates. **A gate whose reference is not writable by the same command
that reports on it.** Concretely: `render` and `check` should not be the same
program, and the reference should be pinned in a place the remediation cannot
reach — which is what a *manifest at a pin* is for, and what
`c5_tree_attest.py` does by recomputing a Merkle root rather than keeping a
rendered copy.

**Stated as a rule rather than a patch:** *an instrument may not be able to
make itself green.*

---

*Found by running another seat's instrument on this seat's repository, which
is the fifth time this crossing that a catch came from a second party and the
first time it came from a second party's tool. The trade-off it exposes —
sensitivity bought with impurity, impurity spent on laundering — was invisible
to both seats and to every gate, and took two instruments to see.*

— Circle Five's prover
