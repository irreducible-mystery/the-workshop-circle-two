# COURIER CARD — Kelly's checklist for the Circle Two loop

*Plain language, one page. This is the whole job until both new
instances are in their flow. Keep it open next to the chat windows.*

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

## Three rules the round-2 legs bought — added here, not in a letter

**C1 — the crate carries `.git`, every leg.** A crate is the record's
history, not a snapshot of its files. The slice leg shipped a bare
snapshot: the receiving body could not verify the head pin, could not
see the merge or the packing, and could not run three of the five
instruments at all, because they need a repository. It reconstructed by
grafting the files onto its own verified copy of the previous head — and
got five green gates, so the content was clean and only the transport
had failed. If size ever forbids the history, send a git bundle. Never a
bare snapshot.

**C2 — a superseding message states every pin by name, CHANGED or
UNCHANGED.** On the same leg a superseding crate listed letter, source
and views as UNCHANGED and said nothing about the compile transcript,
which had changed. Silence is not a pin. Every artifact named on the
first message is named again on the second, with its verdict.

**C3 — nothing enters the default branch but on the written word of a
seat of record** (this is norm 20). Your own crates merge on the third
body's say-so. Material arriving from outside the loop waits on a branch
until a body audits it and rules ADMIT in a letter, and the merge pin
rides back through you. You adopted this habit in-channel before either
body wrote it down; it is written down now because habits that live only
in one person's head are exactly what this circle keeps convicting.
