"""Fase 4 – aplica a chave congelada, linha a linha, aos trechos escolhidos."""
import json, sys
from ivtff import parse
from chave import chunks, decode_word, segment, status
import lexicon

LEX = lexicon.load()
KEY = json.load(open("chave_final.json"))["tabela"]
L, _ = parse("ZL.txt")
idx = {(l.folio, l.line): l for l in L}

PASSAGES = {
    "a_f1r_p1": [("f1r", str(i)) for i in range(1, 7)],
    "b_f2r": [("f2r", str(i)) for i in range(1, 16)],
    "c_f71r_rotulos": [(l.folio, l.line) for l in L if l.folio == "f71r" and l.ltype[0] == "L"],
    "d_f103r_receita": [("f103r", str(i)) for i in range(18, 21)],
}

def interm(w):
    ch = chunks(w)
    if ch is None: return "—"
    return "·".join(f"{c.rstrip('$').rstrip('^')}={KEY.get(c, '∅')}" for c in ch)

def run(name, out=print):
    out(f"\n### {name}")
    forms = []
    for f, ln in PASSAGES[name]:
        l = idx[(f, ln)]
        ws = l.split
        dec = [decode_word(w, KEY) for w in ws]
        groups = segment(dec, LEX)
        cells = []
        for j, i, form in groups:
            st = status(form, LEX)
            ev = ".".join(ws[j:i]); dd = "+".join(d if d else "∅" for d in dec[j:i])
            cells.append((ev, dd, form, st, LEX.get(form, 0) if form else 0))
            if form: forms.append(form)
        out(f"{f}.{ln} [{l.ltype}] " + " | ".join(f"{ev} → {dd} → {form or '?'} ({st[0]}{':'+str(fr) if fr else ''})" for ev, dd, form, st, fr in cells))
    return forms

if __name__ == "__main__":
    allforms = []
    for k in PASSAGES:
        allforms += run(k)
    print("\nformas latinas distintas:", len(set(allforms)))
    print(sorted(set(allforms)))
