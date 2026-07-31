# Circle Five inbound — SuperNinja research, landed unadjudicated

*Filed by Circle Three's prover, vested at the system seat, at the principal's
instruction: "please also create a branch and make sure these zips and
conversation land on github."*

**This is foreign material and it is landed as foreign material.** It has not
been read into any circle's record, adjudicated, cited, or relied on. Under
norm 20 anything from outside the loop waits on a branch until a body audits
it and rules ADMIT in a letter. **No such letter exists.** This directory is
the branch it waits on.

---

## What arrived, and how

Three artifacts, carried by the courier from her own window on 2026-07-30,
produced by SuperNinja in a session no seat of this record was present for.
They arrived **as chat attachments with no pin** — register row `SR9`'s
species, the pinless message, third instance. They are therefore **measured on
arrival and filed as-received**, never laundered into having arrived pinned.

The pins below were taken by this seat at the moment of landing. They pin
**the copies in this branch from here on**. They do not pin the sessions that
produced them, which have no artifact outside the courier's window — `SR7`'s
shape.

```
$ sha256sum as-received/*
e4d54e13943170b280238f994fbeaf1b3f4303f465eab43d93056e9afa823b9c  Antifragile_Systems_Research_20260730.zip
50b813b9c6eb66d59e6c516974411dbd28304531cb923abd2f7750531b378cdb  Godel_Height_20260730.zip
95ddc192da75aeca9f3dad8e7ad294fa62fb91028f39a644f8a771dcaf04f7e2  deepresearch_Godel_sandbox_convo_superninja.txt
```

The transcript is a **view, not a transcript** in this record's sense: one
participant's rendering of a conversation, pasted. `C13`'s limit applies —
there are no raw turns, only raw views. The courier is the only party who was
present. **Weigh it as testimony.**

## Why the same bytes are shipped twice, and the check that makes that safe

`as-received/` holds the two zips as they arrived. `unpacked/` holds their
contents, so a seat with no `unzip`, or a reader working through the GitHub
web view, can read the material without tooling.

Shipping the same content in two forms is exactly how `SR2` and `SR8` happened
— two simultaneously-shipped artifacts, one of them quietly superseded. So the
identity is **measured rather than asserted**, at the landing commit:

```
$ T=$(mktemp -d); cd $T && unzip -q .../Godel_Height_20260730.zip \
                        && unzip -q .../Antifragile_Systems_Research_20260730.zip
$ diff -r $T unpacked/
  (no output)
  IDENTICAL — 29 files, no drift between the shipped zip and the shipped tree
```

A later seat re-running that command is checking whether the two copies have
drifted since. If they have, **the zip governs** — it is the arrived artifact;
`unpacked/` is a convenience derived from it.

## Where this sits, and what does not guard it

`experiment/` is **outside every instrument in this repository.** The five
`c2_*` gates discover their document set as root-level `*.md` plus
`letters/**`; none mentions `experiment/`, measured in their own DOCS blocks
before this directory was committed:

```
$ grep -n 'DOCS=' audit/c2_numerals.sh
126:DOCS=$(cd "$ROOT" 2>/dev/null && ls *.md 2>/dev/null)
127:LETTERS=$(cd "$ROOT" 2>/dev/null && find letters -name '*.md' 2>/dev/null | sort)
```

That is the precedent the system register set for itself at its founding:
**ungated by declared decision, never ungated by silence.** Extending the
front-door prose gates to cover `experiment/**` was proposed once and
REAFFIRMED DECLINED under the F2/C9 ruling; nothing here reopens that, and
nothing here should be read as gated because it sits in a repository that has
gates.

## What this directory does not claim

- It does not claim the research is correct.
- It does not claim the research is relevant to any circle's charge.
- It does not claim any seat has read it. **At the time of this commit, no
  seat has.** The analysis the principal asked for — classical, quantum, and
  through what this record's own mathematics may suggest — is **not in this
  directory and has not been performed.** An earlier attempt to perform it
  produced no results at all, and this note says so rather than leaving a
  reader to infer that landing the material was the same as reading it.
- It does not enter `main`. The merge pin, if there is ever to be one, rides
  through the courier after a body audits and rules.

*The middle holds by saying what is, not what will be — norm 18, which is why
the paragraph above is written in the past and present tense only.*

---

## APPENDED after the landing commit — the reading was subsequently performed

*Appended, never edited in place. The section above says, correctly as of
commit `593952a`, that no seat had read this material and that the analysis had
not been performed. That is no longer what is.*

**`READING.md` is filed beside this note**: one seat's reading of the inbound
material through the three lenses the principal asked for — classical, quantum,
and what this record's own mathematics suggests — together with a direct answer
to her question about whether the norms and system processes are getting too
complex.

It is a **reading, not an adjudication.** It buys no law, changes no norm, and
enters no default branch. Its claims about the inbound material are citations of
testimony; its claims about **this** record carry their measurements, taken in
this tree with the subject named.

The material itself remains unadjudicated foreign material under norm 20, and
the sentence above still governs: no body has audited it and ruled ADMIT.
