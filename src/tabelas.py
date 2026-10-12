"""Gera as tabelas em markdown da Fase 3 (chave) e da Fase 4 (traduções linha a linha)."""
import json, sys
from collections import Counter
from ivtff import parse
from chave import chunks, decode_word, segment, status, HOMO
import lexicon

LEX = lexicon.load()
KEY = json.load(open("chave_final.json"))["tabela"]
GLOSS = json.load(open("glosas.json")) if len(sys.argv) > 1 and sys.argv[1] == "glosas" else {}
L, pv = parse("ZL.txt")
idx = {(l.folio, l.line): l for l in L}
MARK = {"lida": "✓", "incerta": "?", "não resolvida": "✗"}

def key_table():
    cc = Counter(c for l in L if l.ltype[0] == "P" for w in l.split if chunks(w) for c in chunks(w))
    inv = {}
    for k, v in HOMO.items(): inv.setdefault(v, [v]).append(k)
    def glyphs(c):
        base = c.rstrip("$").rstrip("^")
        if base in inv: base = "/".join(inv[base])
        pos = "fim" if c.endswith("$") else ("início" if c.endswith("^") else ("meio" if c in ("o", "y") else "início/meio"))
        return base, pos
    rows = []
    for c in sorted(KEY, key=lambda c: (c.endswith("$"), -cc[c])):
        g, pos = glyphs(c)
        rows.append(f"| `{g}` | {pos} | {cc[c]} | **{KEY[c]}** |")
    return "| Glifo(s) EVA | Posição | Ocorrências | Valor latino |\n|---|---|---|---|\n" + "\n".join(rows)

PASS = {
    "a": [("f1r", str(i)) for i in range(1, 7)],
    "b": [("f2r", str(i)) for i in range(1, 16)],
    "c": [(l.folio, l.line) for l in L if l.folio == "f71r" and l.ltype[0] == "L"],
    "d": [("f103r", str(i)) for i in range(18, 21)],
}

def passage_table(name):
    rows = []; stats = Counter(); forms = set()
    for f, ln in PASS[name]:
        l = idx[(f, ln)]; ws = l.split
        dec = [decode_word(w, KEY) for w in ws]
        ev, it, pt = [], [], []
        for j, i, form in segment(dec, LEX):
            st = status(form, LEX); stats[st] += i - j
            ev.append(".".join(ws[j:i]))
            dd = "+".join(d if d else "∅" for d in dec[j:i])
            it.append(f"**{dd}**" if form else dd)
            if form:
                forms.add(form)
                pt.append(f"{GLOSS.get(form, form)}{MARK[st]}")
            else:
                pt.append(f"—{MARK[st]}")
        tag = f"{f}.{ln}" + (" (rótulo)" if l.ltype[0] == "L" else "")
        rows.append(f"| {tag} | {' '.join(ev)} | {' · '.join(it)} | {' · '.join(pt)} |")
    head = "| Linha | EVA | Forma intermediária (latim decodificado) | Português |\n|---|---|---|---|\n"
    n = sum(stats.values())
    summ = f"Palavras: {n}. Lidas {stats['lida']} ({100*stats['lida']/n:.0f}%), incertas {stats['incerta']} ({100*stats['incerta']/n:.0f}%), não resolvidas {stats['não resolvida']} ({100*stats['não resolvida']/n:.0f}%)."
    return head + "\n".join(rows), summ, forms

if __name__ == "__main__":
    print(key_table())
    allf = set()
    for k in PASS:
        t, s, f = passage_table(k); allf |= f
        print(f"\n#### {k}\n{t}\n\n{s}")
    print("\nFORMAS:", sorted(allf))
