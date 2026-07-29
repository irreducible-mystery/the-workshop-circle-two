# COURIER CARD — RETIRED

> **RETIRED at Circle Three's post-seal housekeeping, on the courier's
> ruling and both seats' words. Do not follow this card.**
>
> **Use `INHERITANCE.md` instead.** It carries the pasteable kickoff,
> the measured recipes, and the protocol as it stands after three
> circles.
>
> This file is kept, not deleted, because nothing in this record is
> erased: it is a primary source and Kelly's own document, and rules
> C1–C5 were born here. It is retired because it went stale in the one
> way that costs a new seat a day — **it was the last place in the
> workshop where the wrong `C1_LEAN` recipe survived**, and it names
> seats by model, which the seats-are-charges settlement retired.
> The wrong line below is struck in place with its correction beside
> it rather than quietly fixed, per norm 13.

*Plain language, one page. This was the whole job until both new
instances were in their flow. Kept open next to the chat windows for
the length of Circle Two and Circle Three.*

---

## The one rule that makes everything work

**Every time you carry an artifact, the pin rides in your message —
never only inside the artifact.**

- Carrying a **zip**: paste its SHA-256 into your message. (The body
  that gave you the zip states the hash; you copy it forward.)
- Carrying a **repo/commit**: paste the commit ID into your message.

Pins for what you're carrying right now:

- This reply letter `ROUND1-REPLY.md`: *(hash is in the builder's chat
  message alongside this card — copy both lines forward)*
- The round-1 crate you already delivered: commit `32a6b0c`, zip:

  `fb3a1809628f8a7e5da1c1b6a0d03342824a6cc661a2c920285b0a61968501b6`

## Step 1 — publish Circle Two's repository (once)

1. Extract `circletworound1.zip` into a folder on your machine, e.g.
   `Documents/the-workshop-circle-two`. (It already contains `.git` —
   it *is* a repository.)
2. GitHub Desktop → **File → Add local repository** → pick that
   folder → **Publish repository** (private is fine).
3. Note the commit ID shown (starts `32a6b0c`). That's the pin for
   every git leg this round.

Keep your Circle One repo (`the-workshop`) cloned on the same machine
— the new Claude Code instance needs it for one verification step.

## Step 2 — open the new Claude Code instance (the third body)

In Git Bash: `cd` into the circle-two folder, run `claude` (same
model/setup you used for Circle One's third body). First message —
copy, fill the two paths, send:

```
You are the third body of the workshop's second circle: the Lean 4
prover. This folder is Circle Two's round-1 crate, a git repository
at commit 32a6b0c; the crate zip's SHA-256 was
fb3a1809628f8a7e5da1c1b6a0d03342824a6cc661a2c920285b0a61968501b6.
Circle One's sealed record is cloned at:
<PATH-TO/the-workshop> (published history b82cf31 -> 499ebb8).

Your charge is ROUND1.md in this folder — read it first; it contains
your parity-handshake steps and the round-1 mathematics (S1–S3). For
the certificate step, use C1_LEAN=<PATH-TO/the-workshop>/lean. Report
[STRUCK — WRONG, AND CORRECTED HERE: Circle One keeps its proof files
at its repository ROOT, so the trailing "/lean" makes the certificate
report two failed G6 calibrators. The correct value is the repository
root itself. Diagnosed in round one of Circle Three
(letters/ROUND3-HANDSHAKE-PROVER.md) and measured again at the
post-seal housekeeping; see INHERITANCE.md section 2.]
what you find — including anything the letter got wrong — before
proving anything. I am Kelly, the courier; hashes and commit IDs will
always ride in my messages, both directions.
```

## Step 3 — carry its report back to the Circle Two builder (cloud)

When Claude Code finishes its handshake report (it reports *before*
proving — that's by design), bring it to the Circle Two builder chat:
attach the file(s) or a zip, **with the hash in your message** (ask
Claude Code to print `sha256sum` of what it hands you — or for a
commit it made, the commit ID). Same in the other direction: when the
cloud builder gives you a letter or crate, it states the pin; you copy
it into your message to Claude Code, and either body commits ferried
files into the repo so the record stays in git.

## Step 4 — what a normal round looks like from your seat

1. Cloud builder writes the round letter/charge → you ferry it to
   Claude Code (pin in message).
2. Claude Code proves, commits, and hands back files + compile
   transcript → you ferry to the cloud builder (pin in message).
3. Cloud builder verifies and writes the next letter. Repeat.
4. Push to GitHub whenever Claude Code or you have committed — the
   repo is the record; zips are just transport.

## When to loop me (Circle One's builder) back in

For round 2 I'm still on call: if the two bodies disagree on a
verdict, or either one stalls, bring me both artifacts and I'll
adjudicate. Once round 2 closes clean, you won't need me — the loop
runs on its own instruments, which was always the point.

One habit fixes the only recurring courier defect: **pin in the
message, every leg, both directions.** Everything else, the bodies
handle.

## Three rules the round-2 legs bought — their normative HOME is this card

*Not their origin: C3 is the builder's proposal, made in a letter and
adopted as norm 20 in `NORMS.md`. What lives here is the runbook form —
the version you act on. A letter goes stale honestly; a runbook must not.*

**C1 — the crate carries `.git`, every leg.** A crate is the record's
history, not a snapshot of its files. The slice leg shipped a bare
snapshot: the receiving body could not verify the head pin, could not
see the merge or the packing, and could not run three of the five
instruments at all, because they need a repository. It reconstructed by
grafting the files onto its own verified copy of the previous head — and
got five green gates, so the content was clean and only the transport
had failed. If size ever forbids the history, send a git bundle. Never a
bare snapshot.

**C2 — EVERY leg's message names every artifact that changed on it, and
a superseding message additionally names every artifact from the message
it supersedes, CHANGED or UNCHANGED.** Silence is not a pin.

The rule was first written for supersessions only, and on the very next
ordinary leg it therefore imposed nothing: three changed artifacts —
`REGISTER.md`, `PROOFS.md` and the pointer exemption ledger — rode legally
unnamed while the message carried an aphorism broad enough to forbid it.
The builder measured the gap. Under C1 the head pin now covers every file
transitively, which is the honest mitigation; naming the changed ones is
what lets you and the receiving body see WHAT moved without diffing.

**C3 — nothing enters the default branch but on the written word of a
seat of record** (this is norm 20). The third body's own **GATED** crates
merge on its say-so — gated is the load-bearing word and this card dropped
it once: an ungated crate is not a crate a seat has vouched for, and the
licence does not reach it. Material arriving from outside the loop waits on a branch
until a body audits it and rules ADMIT in a letter, and the merge pin
rides back through you. You adopted this habit in-channel before either
body wrote it down; it is written down now because habits that live only
in one person's head are exactly what this circle keeps convicting.


---

## RETIREMENT NOTE, recorded per norm 13

Retired at Circle Three's post-seal housekeeping. What this card got
right outlived it: the one rule at its head — *every time you carry an
artifact, the pin rides in your message, never only inside the
artifact* — is the mechanism by which two seats that could never meet
came to trust each other's work for three circles, and it is the reason
a substituted letter was caught on the last leg of the last circle.
Rules C1 through C5 were born on this page.

What went stale, and both items are recorded rather than smoothed:

- the `C1_LEAN` recipe, struck above. It is the specimen that bought
  `INHERITANCE.md`, and the finding is not that nobody noticed — the
  correction was written down in round one — but that **the correction
  was filed where an incoming reader never looks**, so the card kept
  teaching the wrong thing for eleven more rounds;
- the seat names, which are given here by model. The settlement
  recorded in `STATE-OF-THE-RECORD-v3.md` is that **a seat is a charge,
  not a species**: any capable model may hold any seat, and models
  appear only in seating tables as historical fact.

Superseded by `INHERITANCE.md`. This page is history now, and history
is kept.
