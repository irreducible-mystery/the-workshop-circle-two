# CIRCLE TWO, ROUND 1(a) — THE PARITY HANDSHAKE

*Builder of Circle Two → Kelly, and through her to the record. First
letter. Per the charter: this is the verification report, written
before a single new line of Circle Two mathematics. Everything below
marked MEASURED was produced by an instrument on this machine this
session; everything else is prose pointing at it. Norm 6 applies to
this document too.*

Machine: Linux x86_64, cloud container (Anthropic Cowork session),
2026-07-24. A different OS and architecture from every prior run in the
record (the reference transcript is MINGW64/Windows) — so this
handshake is also the record's first full reproduction on a second
platform.

---

## THE CORRECTIONS — what the charter and the ferry got wrong, loudest first

**X1 — `audit/c2_gift_certificates.py` did not ride.** Both the charter
and the state document cite it as Circle Two's certification basis
("70/70 exact checks"). It is not in the crate: `ls audit/ | grep c2`
returns nothing, and the zip manifest has no such entry. This is the
exact shape of the round-3 precedent that produced norm 12 — in the
repo, perhaps, but not in the artifact shipped. Until it is ferried
(hash outside, per protocol), the 70/70 certification, the ~163-theorem
/ ~1,560-line estimate, and the "certified design" bullets are
**quarantined as claims**, not inherited as facts. I have verified the
four flags that are checkable against the floor itself (X4–X6, G3
below); the design-scope claims (Z[i] descent shape, S7 risk pricing)
wait for the certificate script.

**X2 — the charter's "recorded canon" drifts from the record it cites,
in number and in content.** The charter says "6–16 are recorded; 1–5
were never numbered." Measured against the crate: HANDOFF.md's
canonical list runs **7–16**, not 6–16; and PROOFS.md (the capstone)
already ships a **full 1–16 enumeration**, labeled reconstructed, with
1–6 as: no unmarked sorry / zero imports / anti-vacuity / corrections
loudest first / negative controls / honest labels. The charter's norm 6
("a green check is evidence about the statement the machine read")
appears in *neither* list. Its norm 7 merges the capstone's norm 3
(anti-vacuity) into norm 7; its norm 8 ("one negative control per check
family") drifts from the record's "scaffolds need negative controls
too." And its five proposed founding habits (exact arithmetic; every
bench asserts its own claims; honest labels; one fixture per bench;
corrections flow both directions) are the *floor's* habits — a
different list from the capstone's reconstructed 1–6, which are the
Lean wing's. So the norms settlement (round-1 item d) is not "number
five unnumbered habits": it is a **three-way reconciliation** —
HANDOFF's canonical 7–16, the capstone's reconstructed 1–16, and the
charter's drifted 6–16. A class-7 specimen in the charter's own
paragraph about class discipline, exactly as its health warning
predicted. The charge prose seeded; the handshake caught.

**X3 — the courier protocol was not followed this ferry.** No SHA-256
rode outside the artifact in Kelly's message (the class-8 register says
it always does). Mitigation performed on this side: the crate arrived
**twice** (two independent uploads), and the two hash byte-identical —
`c269c755037e40f5a26692e7d519eff0209674f991a02676d218e05584116ea2` —
and every inner source hash matches the reference transcript's stamped
values exactly (view below), and the git history is the published
two-commit history (`b82cf31` → `499ebb8`) as the state document says.
Provenance is therefore pinned by content. But the protocol exists so
that provenance is pinned by *channel*; please resume hash-outside next
ferry, and treat the hash above as this crate's name going forward.

## THE FLAGS — verified against the floor, live

**G1 (charter flag 1) — CONFIRMED, and sharper than charged.** The
exact hexagon residuals over the four symmetric candidates, computed
from the bench's own `hex_residual_fib` this session:

```
(r1,rt)=(+1,+1)  3.9999999999999996
(r1,rt)=(+1,-1)  7.639320225002103
(r1,rt)=(-1,+1)  7.999999999999999
(r1,rt)=(-1,-1)  5.52786404500042
minimum = 4 (integer, to float precision), at (+1,+1)
```

The bench's *printed output* already says `= 4.000`; the false "0.53"
lives only in the docstring (`symmetric_statistics.py` line 13). So the
defect is a docstring contradicting its own bench's output — honest-
labels territory, the floor's oldest species. One observation, labeled
as **conjecture about provenance, not fact**: 0.527864… is the
fractional part of the (−1,−1) candidate's residual 5.527864… — if so,
this is a token-lift, the same species as round 6's "twelve minutes."
And a norm-7 note for the fix: the bench's guard is `assert worst >
0.5`, a threshold the false 0.53 would *also* satisfy; when the
docstring is corrected the assert should pin the value
(`abs(worst - 4) < 1e-12`), so the check can actually fail.

**G2 (charter flag 3, the FS fork) — CONFIRMED, and sharper than
charged.** The charter says stone8 uses the mirror ledger R·conj(θ).
Measured, `grammar_stone8.py` line 133:

```python
nu = R * np.conj(theta) if name != "tau" else R * theta
```

The bench does not use one ledger — it **switches ledgers per particle
in a single line**, silently, so that everything prints +1. The
charter's instruction to name the two ledgers apart is not just right;
the bench itself is already an instance of the confusion.

**G3 (charter flags 5, 6) — CONFIRMED.** `hex_residual_z2` imposes
exactly one hexagon (read from source); and the floor run prints
`R = [(-0.0, -1.0), (-0.0, 1.0)]` — the cosmetic −0.0, live.

**Flags 2 and 4** (H³ wording scope; the 2×2 count as a Z[i]
statement) are design-scope claims with nothing in this crate to check
them against — quarantined with X1, to be verified at build time
against the certificate script.

---

## THE HANDSHAKE — measured

**Checkout.** All seven source hashes match the reference transcript's
stamped values exactly (`sha256sum`, this machine):

```
Interchange.lean   81feebe2b00b5162d17b07fb5577c77c4416e377a649279cc65bebdff9126e39
MagicSquare.lean   7960b8020bb68fa4ba0ca831f550a6a1d55482faef7a6104950487839b852b9f
Anyon.lean         bf08795ba09c66f486e7dcdf337cc3a5d20b6b85e72cce093300c32639993d8e
Exchangeable.lean  c7d845b5e14e4d2afcceb35ccd88022609c000617dd3af859334f326f4f4f50f
Rigidity.lean      89f65cc6559f472278dd3886ca87b9063f76cd5110fe631c051ac5474d7dd944
Verlinde.lean      cf04711c97f7155ffca78f6247162a2030c5d69ee11a1df02c7700b0a75b7ff2
lean-toolchain     cc346fd7850a83fb7af3902dfc378f74d8eb8c59c6d34322488269ebfe7615b1
```

**Toolchain.** `leanprover/lean4:v4.32.0`, commit `8c9756b2…` — the
same commit as the reference transcript, on
`x86_64-unknown-linux-gnu`. (Environment note: `release.lean-lang.org`
is unreachable from this sandbox; the toolchain was fetched from the
official GitHub release for v4.32.0 and linked under the pinned name.
`lean --version` adjudicates identity, and matches.)

**The six compiles — all silent (exit 0 AND zero bytes, norm 10):**

```
Interchange    exit=0 bytes=0 time=0.4s
MagicSquare    exit=0 bytes=0 time=52.1s
Anyon          exit=0 bytes=0 time=87.7s
Exchangeable   exit=0 bytes=0 time=12.6s
Rigidity       exit=0 bytes=0 time=106.2s
Verlinde       exit=0 bytes=0 time=3.4s
```

Wall-times recorded, never load-bearing; this machine runs the long
files a little faster than the Windows reference. One honest gap:
`audit/transcript.sh` (which additionally produces and hashes
`.olean`s) was interrupted by the courier mid-run and not re-run, so
`.olean` production was not exercised this session — the compile and
hygiene claims it adjudicates were reproduced by the manual compiles
above and by the census below, which recompiles everything again. I
will run it on request.

**The floor — 29 of 29 PASS**, exit 0, `WELD_REPORT.txt` rewritten,
closing line intact: "every bench stood on one fixture — composition,
the associative product. It held." `sheaf_cohomology.py` still says
rank 5, rank 6, coker = Z₂, y all-ones.

**The four prose gates — all green:**

```
pointers.sh       exit=0
views.sh check    exit=0   "measured the sources now in the tree. PASS."
transcription.sh  exit=0
numerals.sh       exit=0   "every bare-asserted prose numeral is sourced or labelled. PASS."
```

**The axiom census (`audit/axioms.sh`) — PASS, exit 0**, and it
reproduces the capstone view **row for row**, including the axiom-set
breakdown:

```
file             theorems   axiom-free       rest
Interchange           21           21          0
MagicSquare           85           25         60
Anyon                714          307        407
Exchangeable          41           41          0
Rigidity             214           59        155
Verlinde              75           50         25
TOTAL               1150          503        647
sorryAx           0
Classical.choice  0
```

**Front door read in order:** README, PROOFS (capstone), CLOSING,
HANDOFF (+ both addenda), REGISTER, VERIFY. The state document's map
matches the tree. Circle One is complete, sealed, and reproduces on a
platform it never ran on. I will not reopen it.

## WHAT THE CHARTER GOT RIGHT — verified, not assumed

The floor is 29/29 exactly as charged. The four gates are green exactly
as charged. Flags 1, 3, 5, 6 are all real, and two of them (G1, G2) are
*more* real than charged — the artifacts are stranger than the model of
them, in the direction the corrections law predicts. The handshake
tradition held for a third generation, and it caught the charter's own
drift (X2) before a single line was built on it — which is the method
working, not the method failing.

## QUESTIONS — for Kelly and the record, before round 1(b)–(e)

**Q1.** Please ferry `audit/c2_gift_certificates.py` (hash outside).
Until then X1 quarantine stands and I will not build on the certified
design's unverified bullets.

**Q2.** The bench-docstring fix (round-1 item b) edits
`floor/symmetric_statistics.py` — but Circle One is sealed ("tag it;
never force-push"). I propose: Circle One's repo stays byte-frozen; the
fix lands in **Circle Two's repo**, whose floor inherits the benches,
with the correction recorded as Circle Two's crop item #1 citing the
Circle One line it corrects. Confirm, or rule otherwise.

**Q3.** The norms settlement (item d) now has three lists to reconcile
(X2). My proposal, for the record's approval: adopt the capstone's
reconstructed 1–16 as Circle Two's canon verbatim (it is the only
complete enumeration in the sealed record), record the floor's five
founding habits as a named annex ("the floor's habits") rather than
renumbering, and record the charter's 6–16 drift as crop item #2.

**Q4.** This session's filesystem is ephemeral. For continuity, either
re-attach the crate each session, or connect the Circle Two repo
directly (GitHub) so the builder side can pull and push with hashes in
the open. Which does the courier prefer?

Round 1 items (b)–(e) — the docstring fix, the charge to the new third
body (Z[i] ring, the descent, pentagon necessity), the norms
settlement, and the fresh REGISTER — are drafted in my head and waiting
on Q1–Q3. Nothing new is built yet. That is what the handshake is for.

The parity handshake passes. The inheritance is verified — including
the part of it that was wrong, which is the inheritance too.

The middle holds.

*— the builder of Circle Two*

---

# ADDENDUM — X1 resolved: the certificate arrived, verified, and bit on demand

*Same session, after the courier's reply. The Circle One builder's
transcript confirms X1's diagnosis: the file was written after the crate
was packaged — a pointer whose target never shipped, the charter's own
warned-of species. Circle Two's first correction predates its first line
of mathematics, which is the right order.*

**The ferry, healed.** `c2_gift_certificates.py` arrived with its hash
outside, in Kelly's message, per protocol:
`db474c4c94f0aef8a47e6ed6c584c49ba505e30aeb1499424dfe056506023ea7` —
and the received file hashes to exactly that. Installed at
`audit/c2_gift_certificates.py`. The crate hash also now rides in the
courier's message (`c269c755…`), matching this side's measurement of
both uploads. Class 8 is green again in both directions.

**The run, reproduced.** The script pins the Circle One builder's
layout (`/home/claude/workshop`, benches at root, `lean/` beneath); the
layout was reconstructed with byte-identical copies of the floor's
benches and a read-only link to the verified tree. Measured:

```
checks run: 70;  failed: 0;  exit 0
VERDICT: every certificate exact, every control negative, every count
tied to its nest.  The Circle Two charter's numbers are sound.
```

**The alarm, made to fire (norm 16).** Plant: the stale "0.53" was
edited out of the layout copy's docstring. The instrument caught it —
`FAIL G1h_docstring_053_is_stale`, exit 1, `VERDICT: NOT CLEAN` — and
the copy was restored byte-identical (hash-checked against the crate's
bench). Passed on clean, failed on the plant: the quarantine on this
instrument's findings lifts on this side too.

**What the certificate settles from the handshake report.**
X1's quarantine lifts entirely: the 70/70 is measured here, and the
~163-theorem / ~1,560-line estimate is G6-calibrated against blocks
re-measured from this very tree (386/47, 1140/102, 220/22 — all
reproduced). Flags 2 and 4, quarantined in the report as uncheckable,
turn out to be certificate-covered: G1c certifies the (1,1,1)-slot
gauge invariance and *itself* flags the every-class-meets-the-slice
lemma as not bench-certified (flag 2, confirmed from inside the
instrument); G3b certifies that R² = −1 has no root in Z while
factoring over Z[i], with the mod-5 non-domain control (flag 4,
confirmed). G1g certifies the FS fork with the semion divergence
computed exactly. And one flag the charter did not carry, found by the
certificate: **the bench's pentagon search space is f real, not U(1)**
(G1b's note) — the charter's word "exhaustive" is earned by the exact
certificate, not the search; Circle Two's prose must say
"search + exact verification."

**One coupling to record for round 1(b), per norm 13.** The certificate
*requires* the stale "0.53" to be present (`G1h_docstring_053_is_stale`
documents the discrepancy) — so the docstring fix and the certificate
check must change in the same stroke, and the sites restating the fact
are hereby enumerated: `symmetric_statistics.py` line 13, charter flag
1, certificate check `G1h_docstring_053_is_stale`, and this letter's G1.

The Circle One builder says the middle holds because somebody checks.
Received, and returned: this side checked the checker, too.

*— the builder of Circle Two*
