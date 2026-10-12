"""Fase 10h – G-cópia3: autocitação através das páginas com mutações que respeitam as casas, sobre o G-casas2.
Grade pequena de 2 parâmetros (fração de palavras novas, tamanho da janela); procura uma combinação que reproduza ao
mesmo tempo o agrupamento por página, as poucas palavras-chave, a semelhança entre vizinhas, TTR, h2 e repetição."""
import random, statistics as st, itertools, json
import gerador
from agrupamento import clustering
from agrupamento2 import page_words, keywords, adjacency
V = gerador.real_pages(); M = gerador.SlotModel(V, dial=True)
grp = lambda pg: (pg["I"], pg["L"]) if pg["I"] in ("H", "B", "S") else None
def summary(pages, rng):
    idx, _ = clustering(pages); kw = 0; kwe = 0; adj = []
    for g, pgs in page_words(pages, grp).items():
        if len(pgs) < 8: continue
        o, e, n, _ = keywords(pgs, rng, reps=10); kw += o; kwe += e
        a, f = adjacency(pgs); adj.append(a - f)
    para = [w for pg in pages for t, ws, _ in pg["lines"] if t == "P" for w in ws]
    from collections import Counter
    pairs = [(a, b) for pg in pages for t, ws, _ in pg["lines"] if t == "P" for a, b in zip(ws, ws[1:])]
    seq = []
    for w in para: seq.extend(w); seq.append("_")
    import math
    bi = Counter(zip(seq, seq[1:])); uni = Counter(seq[:-1]); n = sum(bi.values())
    h2 = -sum(c / n * math.log2(c / uni[a]) for (a, b), c in bi.items())
    return {"agrup": idx, "chave": kw, "chave_acaso": kwe, "viz-dist": st.mean(adj), "TTR": len(set(para)) / len(para), "h2": h2,
            "rep": sum(a == b for a, b in pairs) / len(pairs)}
if __name__ == "__main__":
  rng = random.Random(4)
  out = {"Voynich": summary(V, rng)}
  print("Voynich", {k: round(v, 3) for k, v in out["Voynich"].items()})
  for pf, jan, mut in itertools.product([0.5, 0.7, 0.85], [60, 300, 1500], [0.3, 0.7]):
    gerador.P_FRESH = pf; gerador.JANELA2 = jan; gerador.MUT3 = mut
    G = gerador.generate(V, M, "copia3", seed=41)
    r = summary(G, rng); out[f"p={pf} janela={jan} mut={mut}"] = r
    print(f"novas={pf} janela={jan} mutação={mut}", {k: round(v, 3) for k, v in r.items()})
  json.dump(out, open("copia3_grade.json", "w"), indent=1)
