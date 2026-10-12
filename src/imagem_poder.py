"""Fase 11c – Poder do teste dirigido: se existisse uma palavra de cor que aparecesse em p1 das páginas com o traço e em
p0 das demais, com que frequência o procedimento (com a mesma correção por permutação dentro do caderno) a detectaria?"""
import json, random
from collections import defaultdict
import numpy as np
from scipy.stats import fisher_exact
from imagem_texto import zl_pages, page_text
from imagem_palavras import TRAITS, F, Z
texts = page_text(set(F)); fols = [f for f in F if len(texts.get(f, [])) >= 30]
pres = {f: set(texts[f]) for f in fols}
from collections import Counter
df = Counter(w for f in fols for w in pres[f]); vocab = [w for w, c in df.items() if 8 <= c <= 0.7 * len(fols)]
M = np.array([[w in pres[f] for w in vocab] for f in fols], dtype=bool)
quire = defaultdict(list)
for i, f in enumerate(fols): quire[Z[f][1].get("Q")].append(i)
rng = random.Random(11)
for tname in ("flor azul", "raiz vermelha/ocre"):
    y = np.array([TRAITS[tname](F[f]) for f in fols], dtype=bool)
    null = []
    for _ in range(300):
        yp = y.copy()
        for idx in quire.values():
            v = yp[idx].copy(); rng.shuffle(v); yp[idx] = v
        a = M[yp].sum(0); b = M[~yp].sum(0); ny, nn = yp.sum(), (~yp).sum()
        null.append(min(fisher_exact([[a[k], ny - a[k]], [b[k], nn - b[k]]], alternative="greater")[1] for k in range(len(vocab))))
    crit = np.percentile(null, 5)
    for p1, p0 in [(0.7, 0.1), (0.5, 0.1), (0.4, 0.1), (0.3, 0.1), (0.5, 0.25)]:
        hits = 0
        for _ in range(500):
            x = np.where(y, np.array([rng.random() < p1 for _ in y]), np.array([rng.random() < p0 for _ in y]))
            a, b = x[y].sum(), x[~y].sum()
            p = fisher_exact([[a, y.sum() - a], [b, (~y).sum() - b]], alternative="greater")[1]
            hits += p <= crit
        print(f"{tname:20s} palavra em {int(p1*100)}% das páginas com o traço e {int(p0*100)}% das demais: detectada em {100*hits/500:.0f}% das simulações")
