# S7C DESIGN NOTE — extend the prose gates to the row-8 boundary (`experiment/**`)

*Meta-auditor (REGISTER row 7) → the record. Norm 15: design probe +
named adjudicator written and measured BEFORE any gate is edited.*

## 0. Sanctioned scope divergence (recorded per house rule)

The predecessor's `HANDOFF-ROUND3.md` recommended **S7a-first** (prove the
G1c slice lemma before touching the prose gates). This seat recommended
**S7c-first**, on the strength of the STRANGER-AUDIT finding: the live
row-8 characterization slip lives in `experiment/**` prose, and **no
instrument scans that prose today**. Kelly chose this seat's recommendation:

> "charge for Round Three — S7c+S7a (your rec) please"

That is a sanctioned scope divergence from the predecessor's ordering. It is
recorded here (0), and will be recorded again in every new artifact's source
header, in the commit message, and in the Round Three report.

## 1. What S7c is, and is NOT

**IS:** bring `experiment/**/*.md` under the existing pointer / numeral /
views gates, so the prose this seat stranger-audited is *scanned* by the same
resolve/value/proximity instruments the front-door prose already faces.

**IS NOT:** a meaning checker. The gates are value/resolve/proximity-level
(GATES-NOTE.md; the gate headers say so in their own words). The README
row-8 slip the STRANGER-AUDIT flagged — "the Z₂ catalog complete over Z[i]",
an *unearned universal* in a true-shaped sentence — is a **meaning** miss.
Bringing `experiment/**` into scope makes the gates *scan* that class of
prose; it does **not** give them the power to catch a meaning slip. S7c's
honest deliverable is (a) the scanning gap closed for the classes the gates
CAN check, and (b) a measured, declared statement of the residual meaning
gap. No overclaim. This paragraph is the norm-15 "what it does not check."

## 2. The named adjudicator (norm 15)

The adjudicator of S7c is **not** the design probe. It is the four ported
gates themselves — `c2_pointers.sh`, `c2_numerals.sh`, `c2_views.sh`,
`c2_gates.sh` — run against the extended scope, plus norm-16 plants fired
*inside* `experiment/**` and restored clean. The probe only forecasts the
adjudicator's verdict so the implementation is designed against a measured
target rather than an imagined one.

## 3. Measured baseline (this branch, before any change)

Branch `superninja/dual-seat-round3` (based on
`superninja/dual-seat-experiment-s1`).

- Current scanned surface: 6 top-level `*.md` + 2 `letters/*.md` = **8 docs**.
- `pointers`: **PASS**, 149 occurrences, 92 unique tokens, **0 unresolved**.
- `numerals`: PASS. `tree`: PASS.
- `experiment/**`: **110 tracked files, 37 of them `*.md`, entirely
  unscanned.** This is the row-8 boundary, stated as out-of-scan in every
  gate header ("`floor/*.md` … out of scope by design"; the doc glob is
  top-level `*.md` + `letters/**`).

## 4. Measured blast radius of a naïve scope extension

Forecast method: the existing pointer gate, copied into `audit/` so its
`$SELF_DIR`-relative exempt path still loads (a first forecast run from
`/tmp` silently ran with an **empty** exemption list and produced a false
832-unresolved figure — caught and discarded; recorded here as a norm-16
near-miss on my own instrument).

Correctly-loaded forecast, scope = current + `experiment/**`:

- 45 docs scanned; 1156 occurrences; **691 unique tokens**; **680
  unresolved occurrences / 464 unique unresolved tokens.**

Classification of the 464 unique unresolved tokens:

| class | count | why it fails today | resolution source S7c must teach |
|---|---:|---|---|
| identifier-shaped (theorem/def names) | 234 | gate harvests Lean names only from `lean/*.lean`; the experiment's Lean lives at `experiment/seatP/Zi.lean` | harvest declarations from `experiment/seatP/Zi.lean` (and any `experiment/**/*.lean`) when scanning experiment docs |
| hex-pin-shaped | 110 | not git objects in a fresh clone; not in the top-level exempt file | resolve against a pin ledger recorded in `experiment/**` (pins are cited across reports; e.g. the v7-statements pin `97faef58…` resolves to `SUBROUND6-REPORT.md` / `CORRECTIONS-LETTER-S6.md`) |
| path-shaped | 122 | some are real experiment files; some are relative refs (`courier/extract`, `VIEWS.md`) | resolve paths relative to the citing doc's directory within `experiment/**`, and against the experiment file tree |

Of the 234 identifiers, **103 resolve immediately** once
`experiment/seatP/Zi.lean` is harvested. The remaining 131 are a mix of
hex pins my forecast regex over-admitted as identifiers, markdown
filenames, and prose-split fragments — to be handled by the pin/path
sources above or, where genuinely a one-off, a **reasoned exemption**
(never a reasonless one; a reasonless exemption line fails the gate).

Numeral-gate forecast on the new docs: **107 distinct bare multi-digit
numerals** enter as value obligations (each must match an instrument-derived
value or carry a reasoned exemption).

## 5. Design decision (measured, not imagined)

A naïve glob flip would redden the gate with 680 findings and tempt a wall
of reasonless exemptions — the exact permissive failure the norms forbid.
Instead S7c teaches the gates the experiment's **own resolution sources**,
so that a citation which is genuinely grounded resolves *mechanically*, and
only a citation that is genuinely dangling reddens. Concretely, when a doc
under `experiment/**` is scanned:

1. **Lean names** are harvested from `experiment/**/*.lean` (namespace-aware,
   same harvester the gate already uses for `lean/*.lean`).
2. **Paths** resolve relative to the citing doc's directory *and* to
   `experiment/` root, in addition to repo root.
3. **Pins** resolve against a declared experiment pin ledger (the
   `PIN-TRACKER.md` entries plus report-recorded pins), harvested — not
   hand-listed — so a new pin is covered the day it lands.
4. Anything still unresolved gets a **reasoned exemption** or reddens the
   gate. The target end state is **0 unresolved, PASS**, reached by
   *resolution*, not by blanket exemption.

The scope boundary itself moves from "top-level + `letters/`" to
"top-level + `letters/` + `experiment/`", with `floor/` (inherited C1
material, REGISTER class 1/6) still out by design.

## 6. Acceptance gates for S7c (must all hold on shipped artifacts)

- extended `pointers`/`numerals`/`views` run **PASS, 0 unresolved/unsourced**
  on the full scope including `experiment/**`;
- resolution achieved by harvested sources + reasoned exemptions only — no
  reasonless exemption line (that itself fails the gate);
- **norm 16 both directions:** a planted dangling pointer AND a planted
  bare stale count, each placed *inside* `experiment/**`, are BITTEN
  (exit 1, named finding); both restores verified clean (PASS);
- the residual **meaning** gap (§1) declared, not papered over;
- corrections letter + crop; Round Three report block; PIN-TRACKER block;
  every pin measured on the shipped artifact.

## 7. What this note deliberately leaves for the adjudicator

This note does not assert any gate passes. Per norm 16 and REGISTER row 8's
own quarantine doctrine, the extended gates are new instruments; their
outputs are **claims to verify, not results to report**, until each has run
clean and bitten a plant on the shipped tree. This note is the design; the
gates are the judge.
