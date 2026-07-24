"""Bench 5 — THE INTERACTION.

Claims checked:
(1) Identity computed from relating alone: two machines with different anatomy
    (one state vs two) are provably the same process — bisimilar — because no
    admissible interaction distinguishes them. Yoneda, made operational.
(2) The participant sees more than the spectator: two machines with IDENTICAL
    trace sets (the complete archive of possible histories) are NOT bisimilar —
    interaction detects a difference the record of outcomes cannot.

Status: exact, by partition refinement (the standard algorithm), machine-verified.
"""


def refine(states, trans):
    block = {s: 0 for s in states}
    nblocks = 1
    while True:
        sigs = {}
        for s in states:
            sig = (block[s], frozenset((lab, block[t]) for lab, t in trans[s]))
            sigs.setdefault(sig, []).append(s)
        if len(sigs) == nblocks:
            return block
        nblocks = len(sigs)
        block = {}
        for i, key in enumerate(sorted(sigs.keys(), key=repr)):
            for s in sigs[key]:
                block[s] = i


def bisimilar(t1, r1, t2, r2):
    trans = {**t1, **t2}
    block = refine(list(trans.keys()), trans)
    return block[r1] == block[r2]


def traces(trans, root):
    out, stack = set(), [(root, ())]
    while stack:
        s, pre = stack.pop()
        if not trans[s]:
            out.add(pre)
        for lab, t in trans[s]:
            stack.append((t, pre + (lab,)))
    return out


def demonstrate(say):
    # (1) different anatomy, same process
    A1 = {"p": [("a", "p")]}
    A2 = {"q0": [("a", "q1")], "q1": [("a", "q0")]}
    same = bisimilar(A1, "p", A2, "q0")
    say(f"  anatomy vs identity: a 1-state loop and a 2-state loop — bisimilar: {same}")
    assert same

    # (2) same archive, different process
    B1 = {"s0": [("coin", "s1")],
          "s1": [("coffee", "s2"), ("tea", "s3")], "s2": [], "s3": []}
    B2 = {"t0": [("coin", "t1"), ("coin", "t2")],
          "t1": [("coffee", "t3")], "t2": [("tea", "t4")], "t3": [], "t4": []}
    tr1, tr2 = traces(B1, "s0"), traces(B2, "t0")
    same2 = bisimilar(B1, "s0", B2, "t0")
    say(f"  spectator's archive: trace sets equal: {tr1 == tr2}  {sorted(tr1)}")
    say(f"  participant's test:  bisimilar: {same2} — after the coin, machine 2 is in")
    say("  a state that refuses one of the drinks; only interacting can find that out.")
    assert tr1 == tr2 and not same2
    say("  moral: identity = indistinguishability under every admissible relating;")
    say("         and the relating sees strictly more than the record of outcomes.")


if __name__ == "__main__":
    demonstrate(print)
