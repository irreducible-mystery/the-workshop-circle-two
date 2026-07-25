"""Courier extraction — statements only, proof bodies stripped.
Mechanical: keep structure/def/namespace lines verbatim; for each
`theorem`, keep the statement up to (but excluding) the `:=` that opens
the proof term/tactic block; drop everything else (comments, proofs).
Seat B sees definitions and claims only."""
import io, re, sys

src_path, out_path, tag = sys.argv[1], sys.argv[2], sys.argv[3]
src = io.open(src_path, encoding='utf-8').read()

lines = src.split('\n')
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
    if (stripped.startswith('structure ') or stripped.startswith('deriving ')
            or re.match(r'\s*(re|im)\s*:\s*Int\s*$', ln)
            or stripped.startswith('namespace ') or stripped.startswith('end ')
            or stripped.startswith('def ')):
        # defs may span lines until blank or next decl — capture continuation
        emit(ln)
        j = i + 1
        while (stripped.startswith('def ') and j < n and lines[j].strip()
               and not re.match(r'\s*(/--|/-|--|def |theorem |structure |namespace |end )', lines[j])):
            emit(lines[j]); j += 1
        i = j if j > i + 1 else i + 1
        continue
    if stripped.startswith('theorem '):
        # collect until ':=' at depth 0 of the statement
        stmt = []
        j = i
        done = False
        while j < n and not done:
            l = lines[j]
            if ':=' in l:
                l = l[:l.index(':=')].rstrip()
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
