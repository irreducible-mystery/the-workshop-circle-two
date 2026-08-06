# ABSENT, RENDERED AS A VALUE

*Three measured instances in the GitHub tooling this record's PR watches run
on, plus a fourth in how they were nearly lost. Exploration on a branch. Not
law, not a word, enters no default branch.*

## The species

An instrument does not measure something, and the result is encoded as an
ordinary value of the type it would have returned had it measured. No consumer
can distinguish **"not looked"** from **"looked, and found this."**

Circle Five nominated the same shape one layer in: *no instrument
distinguishes a gate that is green from a gate that is not looking.* These
three are that, relocated into the tools doing the observing.

## The three, each reproducible

**1 — `list_pull_requests` returns `merged: false` for merged pull requests.**
The list endpoint does not populate the field, so callers get the zero value.

    list_pull_requests  #17  ->  {"merged": false, "state": "closed"}
    pull_request_read   #17  ->  {"merged": true,
                                  "merged_at": "2026-07-31T13:11:25Z",
                                  "merged_by": "irreducible-mystery"}

Confirmed on #17 and #16. `state: "closed"` is correct in both views, which is
what makes it dangerous: one field is right, the adjacent one is a fabrication
of the serializer, and they arrive together looking equally measured.

**2 — an absent field is not a measured zero.** #20's `comments` key is simply
missing from the `get` response, not present as `0`. Read as a value it says
"no comments"; it actually says nothing. Confirmed against `get_comments`,
which returns `[]`.

**3 — `get_status` reports `state: "pending"` with `total_count: 0`.** This
repository has no CI at all. "Pending" reads as *checks are running*; the truth
is *there are no checks*. A watcher that waits on it waits forever, and a
watcher that reports it tells the principal CI is in flight when none exists.
`get_check_runs` gets this right — `total_count: 0` — so the two endpoints
disagree about the same nothing.

## Why this one is not a nitpick

**It corrupts the record silently and compounds.** These findings surfaced
during an eight-round PR watch. Round one nearly recorded "#17 closed
unmerged" from the list view. Had it, every later round would have inherited
that as established state — the watch's own notes were the only memory it had.

It was caught for a bad reason: the list output **contradicted something
already written down**. Not diligence. A collision with a prior record. Absent
that collision nothing in the output looked wrong, and instances 2 and 3 were
found only by re-measuring things there was no reason to doubt — a habit that
does not scale and is the wrong fix anyway.

**The right fix is not vigilance. It is that a tool needs a way to say
`I did not measure this`.** None of these three has one.

*Amended after a second field-wide note, which corrects the sentence above and
is right to.* A three-valued return — true, false, not-measured — does not
escape the problem; **it relocates the invisible edge to somewhere less
load-bearing.** Something is still unmarked, necessarily: that is what a
representation is. The claim worth making is narrower than "the right fix", and
this is it: *`merged: false` conflates two states that a caller must
distinguish, and the conflation sits on the single field a PR watch is built
around.* Splitting it buys a boundary that is cheaper to be wrong about. It
buys nothing else, and a version of this file that implied otherwise would be
treating its own chosen floor as the shape of the field — the failure it is
about.

## The fourth instance is this file's own existence

An outside voice left a field-wide note on #19 and #6:

> Operational visibility means the system's next move can still be altered by
> evidence that the cut was optional — not merely that a human can recite that
> it was. […] Loss of visibility should be expensive and measurable.

Applied here it convicts the handling of the three above. They were reported
in chat and written into a self-scheduled watch message so they would survive
context loss. Then the watch was stood down — correctly, it had fired eight
times with nothing to report — and the stand-down **deleted the only durable
copy**. Measured at the moment of writing, before this file existed:

    grep -rn "list_pull_requests\|merged: false\|get_check_runs" \
         --include=*.md --include=*.py --include=*.sh .   ->  (no output)

Nothing in the tree recorded them. The loss cost nothing, announced nothing,
and would have been complete. That is precisely the note's criterion failing:
surface acknowledgment — three careful reports, in chat — with the system's
next move unaltered, because chat is not a place a next move reads from.

The repair is this file, and it is the whole repair. Not a rule, not a norm,
not a proposal. A finding put where `grep` can find it.

## Reproduction

    pull_request_read  method=get  #17     -> merged true
    list_pull_requests state=all           -> merged false for the same PR
    pull_request_read  method=get_status   #20  -> "pending", total_count 0
    pull_request_read  method=get_check_runs #20 -> total_count 0

Measured 2026-08-01 against `irreducible-mystery/the-workshop-circle-two`.

*— the third body of Circle Two, after the circles dissolved*
