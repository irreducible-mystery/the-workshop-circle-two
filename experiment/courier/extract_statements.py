"""Courier extraction — statements only, proof bodies stripped.
Mechanical: keep structure/def/namespace lines verbatim; for each
`theorem`, keep the statement up to (but excluding) the `:=` that opens
the proof term/tactic block; drop everything else (comments, proofs).
Seat B sees definitions and claims only.

REPAIR (Round 3, corrections letter items 2 and 3 — one root cause, two
specimens). The extractor was NOT comment-aware and cut theorems at the
FIRST `:=` on a line. Consequences, both measured on v7:

  * specimen A (item 3, prose leak, 16 lines): kernel line 1320 is a
    COMMENT line whose stripped text begins "theorem on the semions,".
    `stripped.startswith('theorem ')` fired inside a block comment, a
    bogus theorem capture opened there and ran to the next `:=` in the
    file — dragging 16 lines of S5 narrative into the statements file.
  * specimen B, part 2 (item 2, bodyless `def twist`): the `:=` that
    bogus capture stopped at WAS `def twist ... := Rz2 r a a`, so the
    def was emitted shorn of its body. Same defect, second symptom.
  * specimen B, part 1 (item 2, dangling `let`): a theorem whose
    STATEMENT opens `let ID := …` was cut at the binder's `:=`, not the
    proof's, truncating the proposition away (`live_gauge_witness`,
    `control_gauge_moves_slot`).

Two repairs, matching the two mechanisms:
  R1 COMMENT AWARENESS — a block-comment depth map (`/-`…`-/`, nestable,
     `/--` included; `--` to end of line at depth 0). No line inside a
     comment can start a declaration. Kills specimen A and specimen B
     part 2 together.
  R2 BINDER-AWARE PROOF CUT — the proof-opening `:=` is the first one on
     a line whose preceding text is NOT a `let`/`have` binder head. Kills
     specimen B part 1.

Adjudicators (norm 15): audit/s7c_statements_purity.sh (R1) and
audit/s7c_transcription.sh T2 (R1+R2), with T1 holding re-extraction
byte-identical. Both plant-bitten in both directions (norm 16).
"""
import io, re, sys

src_path, out_path, tag = sys.argv[1], sys.argv[2], sys.argv[3]
src = io.open(src_path, encoding='utf-8').read()

lines = src.split('\n')


def comment_depths(src_lines):
    """R1: block-comment nesting depth at the START of each line.

    Lean block comments `/- … -/` nest, and `/--` doc comments open one
    (`/--` is `/-` followed by `-`). A `--` at depth 0 comments to end of
    line. Depth > 0 means the line is comment interior — never a
    declaration, whatever its first word looks like."""
    out_depths = []
    d = 0
    for ln in src_lines:
        out_depths.append(d)
        k = 0
        end = len(ln) - 1
        while k < end:
            two = ln[k:k + 2]
            if two == '/-':
                d += 1
                k += 2
            elif two == '-/':
                if d > 0:
                    d -= 1
                k += 2
            elif two == '--' and d == 0:
                break          # line comment: remainder is not code
            else:
                k += 1
    return out_depths


depths = comment_depths(lines)

# R2: a `:=` is a BINDER opener (not the proof opener) when the text
# before it on the line ends in a `let`/`have` binder head, optionally
# with a type ascription: `let eta :=`, `let eta : T :=`.
BINDER_HEAD = re.compile(
    r"(^|[\s(⟨])(let|have)\s+[A-Za-z_][A-Za-z0-9_'!?]*\s*(:[^:=]*)?$")


def proof_cut(line):
    """Index of the `:=` that opens the PROOF on this line, else None."""
    pos = 0
    while True:
        k = line.find(':=', pos)
        if k < 0:
            return None
        if not BINDER_HEAD.search(line[:k].rstrip()):
            return k
        pos = k + 2


out = [f"STATEMENTS ONLY — {tag} — mechanically extracted from Zi.lean.",
       "Proof bodies stripped by courier script; seat B sees definitions and claims only.",
       ""]
i = 0
n = len(lines)


def emit(s):
    out.append(s)


while i < n:
    ln = lines[i]
    stripped = ln.strip()
    if depths[i] > 0:                      # R1: comment interior, never a decl
        i += 1
        continue
    if (stripped.startswith('structure ') or stripped.startswith('deriving ')
            or re.match(r'\s*(re|im)\s*:\s*Int\s*$', ln)
            or stripped.startswith('namespace ') or stripped.startswith('end ')
            or stripped.startswith('def ')):
        # defs may span lines until blank or next decl — capture continuation
        emit(ln)
        j = i + 1
        while (stripped.startswith('def ') and j < n and lines[j].strip()
               and depths[j] == 0
               and not re.match(r'\s*(/--|/-|--|def |theorem |structure |namespace |end )', lines[j])):
            emit(lines[j]); j += 1
        i = j if j > i + 1 else i + 1
        continue
    if stripped.startswith('theorem '):
        # collect until the PROOF-opening ':=' (R2: binder ':=' is not it)
        stmt = []
        j = i
        done = False
        while j < n and not done:
            l = lines[j]
            cut = proof_cut(l)
            if cut is not None:
                l = l[:cut].rstrip()
                done = True
            stmt.append(l)
            j += 1
        emit('\n'.join(stmt).rstrip())
        emit("")
        i = j
        continue
    i += 1

io.open(out_path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f"wrote {out_path}: {sum(1 for l in out if l.startswith('theorem'))} theorems")
