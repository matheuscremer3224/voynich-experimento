"""Diferenças ZL x RF nas linhas usadas (Fases 4 e 5)."""
import sys, difflib
from ivtff import parse
Z, _ = parse("ZL.txt"); R, _ = parse("RF.txt")
rz = {(l.folio, l.line): l for l in Z}; rr = {(l.folio, l.line): l for l in R}
def show(folio, lines=None):
    for (f, ln), l in rz.items():
        if f != folio or (lines and ln not in lines): continue
        r = rr.get((f, ln))
        a, b = l.split, (r.split if r else [])
        if a != b:
            sm = difflib.SequenceMatcher(a=a, b=b)
            ops = [(t, a[i1:i2], b[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal"]
            print(f"{f}.{ln}: " + "; ".join(f"ZL {'.'.join(x) or '∅'} | RF {'.'.join(y) or '∅'}" for t, x, y in ops))
for spec in sys.argv[1:]:
    f, _, rng = spec.partition(":")
    lines = None
    if rng:
        a, b = rng.split("-"); lines = {str(i) for i in range(int(a), int(b) + 1)}
    show(f, lines)
