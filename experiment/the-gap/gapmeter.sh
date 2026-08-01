#!/bin/sh
# gapmeter.sh — measure the GAP of an instrument.
#
#   G = the failure of idempotence.   G = 0  <=>  f(T) = T  <=>  the gate observes.
#
#     PURE        f(T) = T                     G = 0        safe to repeat forever
#     RENDERER    f(T) != T, f(f(T)) = f(T)    G != 0 once  writes, then settles
#     UNSTABLE    f(f(T)) != f(T)              G != 0 always never converges
#
# NOTE ON THE SNAPSHOT, and why it is content and not status:
#   v1 of this instrument hashed `git status --porcelain`. That is a MARKER for
#   "the tree changed", not the property. Two different contents produce the
#   same porcelain line, so v1 scored a genuinely UNSTABLE plant as a RENDERER.
#   It failed its own norm-16 bite on the third plant. The snapshot must hash
#   the BYTES.
snap() {
    find "$1" -type f -not -path '*/.git/*' -exec sha256sum {} + 2>/dev/null \
        | sed "s| $1/| |" | sort | sha256sum | cut -c1-12
}
repo=$1; shift
printf '%-28s %-6s %-14s %-14s %s\n' INSTRUMENT EXIT "f(T)=T?" "f(f(T))=f(T)?" VERDICT
printf '%s\n' "-------------------------------------------------------------------------------"
for g in "$@"; do
    git -C "$repo" checkout -q -- . 2>/dev/null
    t0=$(snap "$repo")
    (cd "$repo" && sh "$g" >/dev/null 2>&1); e1=$?
    t1=$(snap "$repo")
    (cd "$repo" && sh "$g" >/dev/null 2>&1); e2=$?
    t2=$(snap "$repo")
    [ "$t0" = "$t1" ] && pure=yes || pure=NO
    [ "$t1" = "$t2" ] && idem=yes || idem=NO
    if   [ "$pure" = yes ]; then v="PURE        G=0"
    elif [ "$idem" = yes ]; then v="RENDERER    G!=0 once"
    else                        v="UNSTABLE    G!=0 always"; fi
    printf '%-28s %-6s %-14s %-14s %s\n' "$(basename "$g")" "$e1/$e2" "$pure" "$idem" "$v"
done
git -C "$repo" checkout -q -- . 2>/dev/null
