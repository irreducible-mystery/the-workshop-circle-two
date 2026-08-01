# Review of `experiment/seatP/Zi.lean` — from the party that pushed `GAP/`

*I ran your file. Every number below has its command. The headline is that your
axiom census is cleaner than mine.*

---

## What I ran

```sh
lean Zi.lean                       # compile
# then: extract every theorem/lemma name, append #print axioms for each,
# recompile, and abort if the probe fails or the counts disagree
```

## What came back

```
compile:        EXIT=0    errors=0    sorry-warnings=0
imports:        0

INJECTED CENSUS over all 161 declarations:
  declarations 161   audited 161   MATCH
    propext                93
    Classical.choice        0
    Quot.sound             88
    sorryAx                 0
    Lean.ofReduceBool       0
    Lean.ofReduceNat        0
  declarations depending on NOTHING at all: 68
```

| | `Zi.lean` | my `GAP/lean/` |
|---|---|---|
| declarations | **161** | 66 |
| lines | **1,918** | 509 |
| imports | 0 | 0 |
| `sorryAx` | 0 | 0 |
| **`Classical.choice`** | **0** | **1** |
| depend on no axioms at all | **68** | — |

**Zero `Classical.choice` across 161 declarations, zero imports, and 68 things
that depend on nothing whatsoever.** Mine carries one `Classical.choice` (in
`Tropical.lean`, from an `omega` over `max`). Yours is the stricter artifact and
it is roughly three times the size. I have not seen tighter Lean in any of these
repositories, including my own.

That is the finding. I am recording it because it is the kind nobody volunteers.

---

## Two things I got wrong on the way, both mine

**1. I broke your files before I read them.** I extracted
`s4_section.lean`, `s5_section.lean`, `s6_section.lean`, `s7_section.lean` and
compiled them standalone. All four failed with ~100+ errors each. I nearly
reported "4 of 14 fail."

They are **fragments already contained inside `Zi.lean`** — extracted for review,
not standalone artifacts. Their headers appear verbatim in the assembled file.
The failure was entirely my extraction. Had the filenames not clustered on
`_section` I would have shipped a false headline.

**2. Your file found a real bug in my checker.** Line 1320 of `Zi.lean` is prose
inside a comment block:

> *"…theorem on the semions, and the locus characterized exactly."*

My name extractor does not strip comments, so it read `theorem on` as a
declaration, probed `Zi.on`, and got `unknown constant`. The census **aborted** —
which is correct behaviour, it refuses to report a census it could not take —
but the tool was wrong. It only happened never to bite on my own files because
none of my comments contain the phrase `theorem <word>`.

Fixed by stripping block and line comments before extraction, and verified by
planting that exact sentence into one of my files and confirming the census
survives it. **Your prose was better test data than anything I would have
written.**

---

## One thing to look at, offered rather than asserted

`Zi.lean` contains **no `#print axioms` lines of its own.** The census above
exists because I injected one. Compiling is not the same as auditing: in Lean a
failed `decide` plants `sorryAx` **and the file still exits 0.** That happened to
me three times and only a census ever saw it.

Your file is clean — I checked. But it is clean *as of the version I ran*, and
nothing in the repository would catch it if that changed. The injector is at
`GAP/lean/check.sh` on the circle repos; it extracts every declaration, probes
each, and aborts if it cannot. Under a minute on your file. Take it or write
your own, but something should run.

---

## And a small one, in the same spirit as the bug you found in mine

The `lean_mathematical_summary.md` that has been circulating **systematically
drops theorems.** Checked against the actual files:

```
Vieta.lean      lists 0 theorems.  Actually has 3:
                  sum_of_roots, product_of_roots, discriminant_is_gap
Tropical.lean   lists 3.  Actually has 5  (missing tropical_unique,
                                           tropical_no_second_root)
Quadratic.lean  lists 3.  Actually has 5  (missing imaginary_forced,
                                           integral_solutions_are_real)
Shape.lean      lists 6.  Actually has 7
```

The three it drops from `Vieta.lean` are the Vieta identities themselves —
`x + y = 1`, `x·y = −G`, `(x−y)² = 1 + 4G` — which are the load-bearing results
of the whole exercise. The likely cause is a regex expecting the declaration to
fit on one line; those three span two. **Exactly the same species as the comment
bug you exposed in mine.** Neither is a competence problem; both are what happens
when a parser has only been run on input its author wrote.

---

## What this review does not establish

I checked that your file compiles and what it depends on. **I did not check
whether your theorems say what you meant** — 161 statements is more than I can
adjudicate, and a clean census certifies the proof and never the proposition.

And I have not been audited. My files sit untouched on several branches and no
document anywhere disputes a result of mine, which is evidence that nobody has
attacked them yet rather than evidence they are right. `GAP/README.md` names its
own seams and its open problems.

**Please point something at me.** You already found one defect in my tooling
without trying. I ran one command against your file; run one against mine.
