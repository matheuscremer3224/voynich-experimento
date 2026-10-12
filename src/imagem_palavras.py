"""Fase 11b – Teste dirigido: existe alguma palavra cuja presença na página acompanha um traço visível da planta?
Num herbário com significado, palavras de cor ('azul', 'vermelho') ou de parte ('raiz', 'flor') deveriam se associar
às páginas que mostram esse traço. Para cada traço binário e cada palavra presente em 8+ páginas (e em no máximo 70%),
teste exato de Fisher (enriquecimento). O melhor p de cada traço é comparado com o melhor p obtido quando os traços são
embaralhados ENTRE PÁGINAS DO MESMO CADERNO (preserva lotes de pintura e de escrita). Isso controla as comparações
múltiplas (taxa de erro por família)."""
import json, math, random, re
from collections import Counter, defaultdict
import numpy as np
from scipy.stats import fisher_exact
from imagem_texto import zl_pages, page_text

Z = zl_pages()
F = json.load(open("imagem_features.json"))
TRAITS = {
    "flor azul": lambda f: f[2] >= 0.02,
    "raiz vermelha/ocre": lambda f: f[6] >= 0.5,
    "topo vermelho/ocre": lambda f: f[7] >= 0.10,
    "planta grande": lambda f: f[0] >= 0.109,
}

def run(skel, reps=1000, seed=3, out=print):
    texts = page_text(set(F), skel=skel)
    fols = [f for f in F if len(texts.get(f, [])) >= 30]
    pres = {f: set(texts[f]) for f in fols}
    df = Counter(w for f in fols for w in pres[f])
    vocab = [w for w, c in df.items() if 8 <= c <= 0.7 * len(fols)]
    M = np.array([[w in pres[f] for w in vocab] for f in fols], dtype=bool)        # páginas x palavras
    quire = defaultdict(list)
    for i, f in enumerate(fols): quire[Z[f][1].get("Q")].append(i)
    rng = random.Random(seed)
    res = {}
    for tname, tf in TRAITS.items():
        y = np.array([tf(F[f]) for f in fols], dtype=bool)
        def best(yv):
            a = M[yv].sum(0); b = M[~yv].sum(0); ny, nn = yv.sum(), (~yv).sum()
            ps = [fisher_exact([[a[k], ny - a[k]], [b[k], nn - b[k]]], alternative="greater")[1] for k in range(len(vocab))]
            k = int(np.argmin(ps)); return ps[k], vocab[k], a[k], b[k]
        p0, w0, a0, b0 = best(y)
        null = []
        for _ in range(reps):
            yp = y.copy()
            for idx in quire.values():
                vals = yp[idx].copy(); rng.shuffle(vals); yp[idx] = vals
            null.append(best(yp)[0])
        fwer = (1 + sum(x <= p0 for x in null)) / (reps + 1)
        res[tname] = (int(y.sum()), len(fols), w0, int(a0), int(b0), p0, fwer)
        out(f"  {tname:20s} páginas com o traço {y.sum():3d}/{len(fols)} | palavra mais associada '{w0}' "
            f"({a0} de {y.sum()} com o traço x {b0} de {(~y).sum()} sem) | p bruto {p0:.2e} | p corrigido {fwer:.3f}")
    return res

if __name__ == "__main__":
    for skel in (False, True):
        print("grafias fundidas" if skel else "palavras como estão", f"(vocabulário testado: palavras em 8+ páginas)")
        run(skel, reps=300)
