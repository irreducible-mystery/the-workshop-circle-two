# CORRECTIONS LETTER — Round Three

*From SuperNinja instance 2 (meta-auditor, REGISTER row 7) to Kelly, courier,
for carriage to the third body. Loudest first (norm 4). Four items: three
CORRECTIONS (defects to repair) and one CHARGE (forward work authorized —
"S7a is GO"). I recommend; I do not apply. Nothing here edits the kernel or a
frozen source; each item names who adjudicates the repair and how it is
verified. All pins are measured on the shipped artifacts (norm 12).*

---

## Reading order (loudest first, norm 4)

| # | kind | item | consequence class | source | frozen? |
|---|---|---|---|---|---|
| 1 | CORRECTION | §10 characterization slip (specimen C) | a **false math sentence in the headline record** | `FINAL-EXPERIMENT-REPORT.md` §10 | **YES — needs Kelly's sanction** |
| 2 | CORRECTION | statements truncation (specimen B) | **mangled propositions** in what seat B reads | courier `extract_statements.py` → `Zi_statements_v7.txt` | no (courier, LIVE) |
| 3 | CORRECTION | prose leak into statements (specimen A) | **narrative noise** in the statements file | courier `extract_statements.py` → `Zi_statements_v7.txt` | no (courier, LIVE) |
| 4 | CHARGE | the slice lemma (G1c) | the **oldest declared exclusion**, now reachable | REGISTER row 2 | no (new in-kernel work) |

The ordering rationale: item 1 is a *wrong sentence in the closing record*
(the loudest thing a record can carry); items 2 and 3 *corrupt then merely
clutter* the statements file seat B reads; item 4 is not a defect at all but
the round's forward move, placed last because it opens work rather than
closing a wound.

---

## 1. CORRECTION — the §10 characterization slip (specimen C) · LOUDEST

**Where.** `FINAL-EXPERIMENT-REPORT.md`, §10 Closing.

**The defect.** The closing distinguishes boson from fermion by saying the
fermion's −1 makes double-occupation vanish. But **double-occupation
vanishing is common to boson AND fermion** — it follows from commutativity
alone (`pauli_double_occupation_dies`: `ab − ba = 0` is a
tautology-by-commutativity, true for every element of a commutative ring). It
does **not** separate the two statistics. The real distinction is the
**symmetrized occupancy**: the boson admits the doubly-occupied state
(`control_boson_no_exclusion`: `⟨2,0⟩ ≠ 0`), the fermion excludes it. The
headline record states a distinction its own instruments do not support.

**Why loudest.** This is the shared-blind-spot the REGISTER row 8 prediction
named: *"a characterization slip in the settlement or register prose, every
noun resolving, the edge supplied by the model."* Every noun in the §10
sentence resolves; the sentence is still wrong. It is a false mathematical
claim in the document that closes the experiment. **Scored: REGISTER row 8
CONFIRMED** — the prediction was correct, and the true-stranger pass found the
species it forecast.

**The repair.** In §10, replace the tautology-based distinction with the true
one: double-occupation vanishing is common to both statistics
(commutativity); the exclusion that separates them is the symmetrized
occupancy — boson accepts `⟨2,0⟩`, fermion forbids it.

**Frozen-source caveat.** `FINAL-EXPERIMENT-REPORT.md` is a frozen primary
source. Per the canon's frozen-source law, **I do not touch it**; this crop
needed **Kelly's explicit sanction** to be applied.

**STATUS: APPLIED (Kelly's sanction, Round 3).** The §10 sentence has been
cropped and replaced with the true distinction (double-occupation vanishing
= commutativity, common to both; the separator = symmetrized occupancy,
boson admits ⟨2,0⟩ ≠ 0 and fermion excludes it). The divergence is recorded
in the document's header note, in this letter, and (on carriage to git) in
the commit message. Every clause of the replacement was checked against the
two named theorems and holds (norm 6). This is the only content change to
`FINAL-EXPERIMENT-REPORT.md` since its S6 freeze.

**Adjudicator.** Kelly sanctions the crop; seat B confirms the replacement
sentence against the two instruments (`pauli_double_occupation_dies` and
`control_boson_no_exclusion`) — that the new sentence's every clause is a
consequence the named theorems actually carry (norm 6). The divergence
(editing a frozen source) is recorded in the source header, the commit
message, and the report, every time (HANDOFF divergence rule).

---

## 2. CORRECTION — statements truncation (specimen B)

**Where.** Courier `courier/extract_statements.py` → `Zi_statements_v7.txt`.

**The defect.** Three declarations are shipped **incomplete** in the
statements file seat B reads:
- two `let eta`-opening theorems are cut at the *binder* `:=` (the
  `let ID := …` inside the statement), not at the proof `:=`, so their real
  proposition is truncated away;
- a single-line `def twist … := Rz2 r a a` is shipped **bodyless** (its
  defining body stripped).

**Why this loud.** Truncation **corrupts the meaning** of what seat B reads:
a theorem shown without its proposition, or a def shown without its body, is
not noise — it is a different (and false, or vacuous) statement wearing the
right name. Louder than item 3 because item 3 only adds text; this removes it.

**Root cause (diagnosed, not assumed).** The extractor's `def` continuation
loop stops at the first blank line, and its `theorem` loop cuts at the first
`:=` — so a statement whose own text contains an earlier `:=` (a `let`
binder) or a one-line body is severed. This is an **extractor-logic property**,
byte-identical to a fresh re-extraction — a fidelity bug, not corruption in
transit (the re-extraction is byte-identical, T1 PASS).

**The repair.** Fix the extractor so (a) a `theorem` whose statement opens
`let ID := …` is captured through to the **proof** `:=`, not the binder `:=`;
and (b) a single-line `def … := body` keeps its body. Then re-cut
`Zi_statements_v7.txt`.

**Adjudicator.** Gate 4 T2 (`audit/s7c_transcription.sh`) goes **green** on the
re-cut, with T1 still **byte-identical** to the fresh extraction of the
(unchanged) kernel. That pair is the acceptance: the fix removed the
truncation and introduced no drift.

---

## 3. CORRECTION — prose leak into statements (specimen A)

**Where.** Courier `courier/extract_statements.py` → `Zi_statements_v7.txt`.

**The defect.** A block of S5 docstring **narrative bled past** the
proof-stripper into the statements file (16 leaked prose lines, measured by
the purity gate). Seat B, reading statements only, sees prose interleaved with
propositions.

**Why quietest of the three.** A leak **adds** text; it clutters but does not
change any proposition's meaning. A careful seat B can tell prose from a
statement; still, the statements file's contract is *statements only*, and it
is violated.

**Root cause.** Same extractor family as item 2: the proof-stripper's block
boundaries let a docstring's narrative lines through when the docstring abuts
a statement. Also an extractor-logic property (byte-identical on
re-extraction).

**The repair.** Repair the proof-stripper so S5 (and any) docstring narrative
cannot bleed into the statements file; re-cut `Zi_statements_v7.txt`.

**Adjudicator.** Gate 3 (`audit/s7c_statements_purity.sh`) goes **green** AND
gate 4 T1 stays **byte-identical** to the fresh extraction of the unchanged
kernel.

*Items 2 and 3 are the same root family the stranger audit flagged as
courier-fidelity; a single extractor revision can discharge both, but each has
its own green-light adjudicator above.*

---

## 4. CHARGE — the slice lemma (G1c) · forward work, "S7a is GO"

**This is not a defect.** It is the round's forward move, authorized by
Kelly's "S7a is GO," carried here so the whole of Round Three travels as one
letter. The full statement, measured reach, recommended route, and named
adjudicator are in the standalone **`CHARGE-S7a-SLICE-LEMMA.md`**; this entry
is the one-paragraph pointer.

**Charge.** Prove in the zero-import kernel a precise ℤ[i]-level form of the
G1c slice lemma — *every gauge class of a Z₂-fusion 3-cocycle contains an
`Fz2 f`-normalized representative* — closing REGISTER row 2's oldest declared
exclusion. The design probes measure this **TRUE and IN zero-import reach**
(finite, `decide`-able); the norm-6 impossibility clause fires only for the
continuous U(1) version, which the charge does not target. **Adjudicator: seat
B of Round Three**, under this same corrections-letter protocol with the
REGISTER as court; the 6-step acceptance sequence and the ruling seat B must
make (does the ℤ[i]-unit lemma close row 2, or does U(1) survive as a named
residue?) are in the charge §5. **No Lean is written; I do not prove it.**

---

## Pins (measured, first 12 chars; full 64-char in the sub-round reports)

**Corrections evidence (S7c gates + plants + probe):**

```
20d68206d9ef  audit/s7c_pointers.sh
04ed6be70a2e  audit/s7c_numerals.sh
bf3f1ec51344  audit/s7c_statements_purity.sh      ← item 3 adjudicator (A)
36edcc02a1de  audit/s7c_transcription.sh          ← item 2 adjudicator (B)
ee76269b349c  audit/s7c_prose_gates.sh            ← suite harness
393c1674d2e9  audit/s7c_frozen_exempt.txt
dae70d98b74f  audit/plant_pointers.sh
98b9f0d3bc5d  audit/plant_numerals.sh
fc25ae5c65be  audit/plant_purity.sh
5a23b23a9af5  audit/plant_transcription.sh
282261c1fdc3  seatP/probes/s7c_design_probe.py
```
*(the two exemption files are deliberately NOT pinned in place — a self-hash
is a fixed point; they are audited by the gates' exemption-integrity checks.)*

**Charge artifacts (S7a):**

```
b1d88dcfdf68  CHARGE-S7a-SLICE-LEMMA.md
4a7f78f943a4  seatP/probes/s7a_cocycle_reach.py   ← authoritative reach probe
83fa1fd695c3  seatP/probes/s7a_design_probe.py    ← superseded diagnostic
828163b07963  seatP/probes/s7a_reach_refine.py    ← superseded diagnostic
```

To verify any pin: run `sha256sum <path>` and compare the first twelve chars.

*— SuperNinja instance 2, meta-auditor, Round Three. I recommend; I do not
apply. The middle holds.*
