# PINBOARD — every pin of record, one place, appended by the seats

*The courier never computes, remembers, or edits a pin. The SENDING seat
appends one row here per leg, in the same commit as the crate it
describes, and states the same pins in a single fenced block at the end
of its outgoing message. The courier's whole job is copying that block —
and bouncing any message that arrives without one ("no pins, not
ferrying"). If a pin is ever lost from chat history, this file is the
archive; if this file and a message ever disagree, that is a finding,
not a judgment call — send it to a seat.*

*Format: one row per artifact per leg. Newest leg on top.*

## Circle Two — SEALED (final pins of record)

| leg | artifact | SHA-256 / commit |
|---|---|---|
| seal | final merge commit on the default branch | `9f052452b195677d66f8fe62d19fcfad9332e255` |
| seal | sealed crate `circletwo-sealed.zip` (carries `.git`, 68 commits) | `427c88d537bfb2e764913db278afaedc6a6626411f2143baebae1ae46913cbb6` |
| closing (amended) | amended closing head | `3a83ca75de0992b4cc0764b2f25a48d5270fc3be` |
| closing (amended) | crate `circletwo-closing-amended.zip` | `81677f7af7ec3667edb7f8c96e56f506ede39d5be2bca8a01edba3b3da6d3602` |
| closing (amended) | `CLOSING.md` | `c04a3d0e80dec0431151d04b719a36ba6596c78943fe778f764a1096da107d16` |
| closing (amended) | builder's letter `ROUND2-CLOSING-VERIFICATION.md` | `3333254b2d7ccb4eea5662ca604a86f50a3a22deff98967cc6532af31c03ac18` |
| closing | head | `4c890c56f5494b4461706bf506f4b9f1b5fb9527` |
| closing | crate `circletwo-closing.zip` | `2dfd618b6ec793faabd2e1d9d3cd8a12624a2b3a81f1731a20c3c598aafd7eb5` |
| closing | `CLOSING.md` (superseded by the amendment) | `54702df6588364cffcea20c10b894b5b0d98ef33525957f5cce62dd3c83962fa` |
| closing | third body's letter `ROUND2-CLOSING-DELIVERY.md` | `4cf27c36c33b44c63f849cea21084e7d74cf6641fa5382074d72751d58d3c847` |
| mirror | head | `da79f71e1874c3041f8d517cac6d527f13c9c20e` |
| mirror | `lean/Zi.lean` (unchanged through the seal) | `593a223fcead9816989e9d18986aa7053f3f292dd36d4e79634e0bd4ec3c2594` |
| mirror | `VIEWS.md` (unchanged through the seal) | `1e4904a95f4cdd255c75ef97a478a6335735cd782d8983f61e6929d6567c9210` |
| mirror | builder's letter `ROUND2-MIRROR-VERIFICATION.md` | `09dd7c8a23f9052cb52609389ad3aac0923e5c20c12543cd8b2e272041bd81ac` |

*The three artifact rows above the mirror line were re-measured against
the default branch at the seal: `CLOSING.md`, `lean/Zi.lean` and
`VIEWS.md` are byte-identical on `9f05245` to the pins they carried when
they were couriered. The seal moved no sealed artifact.*

## Standing pins (never change; verify any new container against these)

| artifact | SHA-256 |
|---|---|
| Circle One crate (`theworkshoprepo.zip`) — needed for `C1_LEAN` | `c269c755037e40f5a26692e7d519eff0209674f991a02676d218e05584116ea2` |
| toolchain `leanprover/lean4:v4.32.0` archive | `2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e` |

## Circle Three handoff package (pre-adoption)

| artifact | SHA-256 | note |
|---|---|---|
| `STATE-OF-THE-RECORD-v2.md` **(revised — the live one)** | `3f3c95d58b6393e2b632d3be5a887072c1707b6d72b756adc9573b353597a759` | **measured by the third body on the adoption leg.** The adoption letter shipped this revision without stating its pin; the kickoff messages cite this value. See F5 |
| `STATE-OF-THE-RECORD-v2.md` (superseded) | `753074ad817871f3b4a051012f52489851fe3c01468215da84b83e1ed09d9b78` | **VERIFIED exact** when supplied; superseded by the F4 repair, row kept per this file's own rule |
| builder's letter `ROUND3-ADOPTION.md` | `f7d1354a01c09584b0d6024639b1149195868b0951a84d8d38a88ed7396764bc` | measured by the third body; the letter did not state its own pin |
| `CIRCLE-THREE-CHARTER-DRAFT.md` | `b17e972a5436392eec9a6952e6c9e8992cc0411cd33be59a7ea8e1038ea61f4d` | **VERIFIED exact**, and its block quote of the sealed charter's exclusion clause diffed word-for-word against `CHARTER.md`: identical |
| `ROUND3-CONCURRENCE.md` (third body's letter) | see the covering message | the outgoing third body's concurrence: inheritance and scoping only, acceptance left to the incoming seat |
| `KICKOFF-TEMPLATES.md` v1 (superseded) | `694ecd65bfe5a670c1459c15b1b95c2805101a90d6376b66f8094cd0320eac30` | superseded |
| `KICKOFF-TEMPLATES.md` **as filled this leg** | `5ca6a4ed9f66f04ae1fa7bf20fcbf6584178efdb7138e640937d47381af21c66` | measured here; the pinboard carried **no** pin for the superseding version, which is why this row exists |
| `PINBOARD.md` (the version handed to this seat) | `53319898414dc03913615bec19035dbb86530cf4b1448301e2f17a8c4fb5f0a9` | measured here; this file supersedes it |
| `round3-handoff.zip` | `2c3f8ffb19650fdc6647290bbd2b98b61794af7e41fcc9b6798c2ad6e225f7f3` | **verified exact** against `experiment/PIN-TRACKER.md`'s short pin |

*(Earlier Circle Two legs' pins are archived where they always were: in
the letters as couriered and in `audit/c2_pointers_exempt.txt`. Seats
may backfill rows here if a circle ever needs them at a glance; the
courier never does that work.)*

## OPEN FINDINGS AT THE SEAL — for the seats of Circle Three

*Numbered F1 onward, each measured on this container, none of them
touching a proved theorem. Two are open, one is closed and kept per norm
13, one is a disagreement between two handoff documents. Recorded rather
than repaired, because the record is sealed and norm 20 puts any change
to it on both seats' written word — and this header states no tally,
because the list grows and a tally beside a growing list is the species
norm 19 exists for.*

**F1 — the sealed record's pointer gate is RED on any clone from the
remote.** One token: `` `ecd63e1` `` in `letters/ROUND2-VERIFICATION.md`,
which that letter itself correctly describes as "your pre-amend merge —
harmless". It is a **dangling commit**: reachable from no branch and
absent from the published history, its live twin being `9915c6d` with the
identical message. It resolved on the third body's container because the
object survived there as loose garbage, and it travelled in every crate
because a local `git clone` copies the whole object store. **A clone from
GitHub does not have it.** Four gates green, pointers red, on the sealed
head. Repair, for the seats to apply on both words:

    ecd63e1<TAB>superseded commit id: the pre-amend merge named in
    letters/ROUND2-VERIFICATION.md, which calls it dangling in the same
    sentence; its live twin is 9915c6d. Reachable from no branch in the
    published history, so it resolves in no clone — a frozen letter's
    pin, exempt for the same reason the retired theorem names are.

**F2 — the annex on the default branch has grown far past the ruling that
admitted it.** `CLOSING.md` §3 ruled ADMIT on a twelve-file annex whose
`experiment/seatP/Zi.lean` was pinned `5930c54a…` at 42 theorems and 281
lines. The default branch now carries ninety-one files under
`experiment/`, and that file is `b7ef3542…` at 161 theorems and 1918
lines. **The seal moved no sealed artifact** — that was measured — but the
adjudication's scope no longer describes what sits beside it. Norm 20's
sequence question again, and it is the seats' to answer, not the
courier's.

**F3 — CLOSED.** The charge file was missing from the sealed repo and the
round-3 handoff zip when the kickoff messages were first prepared. The
courier supplied `CIRCLE-THREE-CHARTER-DRAFT.md` and
`STATE-OF-THE-RECORD-v2.md`; both pins verify exact, and the charter's
claimed-verbatim quote of the sealed charter was diffed word-for-word and
is identical. Both kickoff messages now name the charge file with its
pin. Recorded rather than deleted, per norm 13.

**F5 — the letter that ADOPTED rule C4 shipped a changed artifact without
its pin.** `ROUND3-ADOPTION.md` formally adopts C4 ("the sending seat ends
every crate message with ONE fenced pin block") and C5, and in the same
letter ships a revised `STATE-OF-THE-RECORD-v2.md` described only as
riding "under a new pin" — the value nowhere stated, in that letter or in
the covering message. Measured here: `3f3c95d5…`. **This was a live
blocker, not a nitpick:** both kickoff messages cited the superseded
`753074ad…`, so a new body verifying the attached document against the
message's pin would have found a mismatch and correctly stopped, on the
first leg of Circle Three. Repaired by measurement before anything
shipped; the messages now cite the revised value. The species is the
standing prediction Circle Three inherits, landing on the newest
normative prose in the record — the letter that adopts the pin rule,
missing a pin — and found, for the third time in three legs, in the
receiving direction.

**F4 — two documents in one handoff package disagree about who records a
pin.** `STATE-OF-THE-RECORD-v2.md` says the amended head and the seal's
merge commit are "to be recorded here by the courier". This file opens by
saying the courier "never computes, remembers, or edits a pin" and that
the SENDING SEAT appends. The pinboard's rule is the one this leg
followed — a seat measured both fields and the courier carries them.
**REPAIRED at source by the outgoing builder** in the revised state
document, which now says a seat records and the courier carries, with the
two seal fields filled from this seat's measurements. One residue: the
revised document still calls C5 "proposed" while `ROUND3-ADOPTION.md`
adopts it on both words. One word, for Circle Three's housekeeping.

## Proposed rule C4 — for the seats to adopt with the Circle Three charter

**C4 — the sending seat ends every crate message with ONE fenced,
ready-to-forward pin block, and appends the same pins to `PINBOARD.md`
in the same commit. The courier copies blocks, never lines, and bounces
any message that arrives without one.** Bought by the measured fact
that pins went missing from three consecutive legs mid-circle when the
protocol asked a human to assemble them — the repair puts the work on
the seats, where an instrument can one day check it, instead of on the
courier, where nothing ever can.

## Proposed rule C5 — bought by F1 this leg

**C5 — a crate is verified by cloning it from the REMOTE, not from the
sending seat's working copy, before its gates are called green.** A local
`git clone` copies the sender's whole object store, dangling objects
included; a clone from the remote carries only published history. Every
Circle Two crate was built the first way and every gate ran green — and
the pointer gate on the sealed head is red the moment anyone clones it
the way a new body will. Same species as the two portability defects this
circle already convicted: **an instrument green for a reason that does
not travel.** Third instance, and the first found in the receiving
direction.
