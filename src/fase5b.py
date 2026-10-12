"""Fase 5b – teste amplo: todas as linhas de parágrafo fora do treino (exceto Fase 4), ordem real x embaralhada
dentro de cada página; chave final x chave nula (treinada em texto embaralhado)."""
import json, random, statistics as st, sys
from collections import defaultdict
from ivtff import parse
from chave import decode_word, segment
import lexicon
LEX = lexicon.load()
L, _ = parse("ZL.txt")
HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}
allp = [l for l in L if l.ltype[0] == "P" and l.folio not in HOLD]
train_ids = set(map(id, random.Random(1404).sample([l.split for l in allp], 1600)))
# reconstrói a amostra de treino exatamente como em otim_ngram.py
lines_all = [l.split for l in allp]
sample = random.Random(1404).sample(lines_all, 1600)
sid = set(id(x) for x in sample)
test = [l for l in allp if id(l.split) not in sid]
P4 = {"f1r", "f2r", "f71r", "f103r"}
def run(key, comma):
    pages = defaultdict(list)
    for l in test:
        pages[l.folio].append(l.split if comma == "split" else l.join)
    def meas(pg):
        tot = cov = multi = 0
        for lines in pg.values():
            for ws in lines:
                dec = [decode_word(w, key) for w in ws]
                for j, i, f in segment(dec, LEX):
                    tot += i - j
                    if f:
                        cov += i - j
                        if i - j > 1: multi += i - j
        return cov / tot, multi / tot, tot
    real = meas(pages)
    rng = random.Random(9); sims = []
    for _ in range(30):
        sp = {}
        for p, lines in pages.items():
            flat = [w for ws in lines for w in ws]; rng.shuffle(flat); out = []; k = 0
            for ws in lines:
                out.append(flat[k:k + len(ws)]); k += len(ws)
            sp[p] = out
        sims.append(meas(sp))
    m = st.mean(s[0] for s in sims); sd = st.pstdev(s[0] for s in sims); mm = st.mean(s[1] for s in sims)
    p = sum(s[0] >= real[0] for s in sims) / len(sims)
    return real, (m, sd, mm, p)
for name, path in [("chave final", "chave_final.json"), ("chave nula (treinada no texto embaralhado)", "tabela3_embaralhado.json")]:
    key = json.load(open(path))["tabela"]
    for comma in ("split", "join"):
        real, (m, sd, mm, p) = run(key, comma)
        print(f"{name} | vírgula={comma}: n={real[2]} real {real[0]:.1%} (multi {real[1]:.1%}) | embaralhado {m:.1%} ± {sd:.1%} (multi {mm:.1%}) | diferença {100*(real[0]-m):+.1f} pts, P={p:.2f}")
