"""Fase 11 – Acoplamento texto–imagem nas páginas herbais (f1–f66, onde a página do PDF = página ZL + 2, conferido pelos
números de fólio a lápis em f10r, f25r, f40r, f50r, f57r, f65r e f66r).
Imagem: composição de cor da pintura (pixels saturados): verde, azul, vermelho, ocre/amarelo; cor no terço inferior
(raízes) e no terço superior (flores); área pintada. Texto: cosseno entre vetores tf-idf de palavras.
Teste: correlação de Spearman entre semelhança de imagem e de texto nos pares de páginas de CADERNOS DIFERENTES e do
MESMO dialeto (para tirar o efeito de produção em lote e de escriba); significância por permutação das imagens entre
páginas (teste de Mantel)."""
import json, math, random, re, statistics as st, sys
from collections import Counter, defaultdict
import numpy as np
from PIL import Image
from ivtff import parse

def lab(a):
    a = a / 255.0
    a = np.where(a > 0.04045, ((a + 0.055) / 1.055) ** 2.4, a / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = a @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return 116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])

def masks(path):
    im = np.asarray(Image.open(path).convert("RGB")).astype(float)
    h, w, _ = im.shape
    im = im[int(.05 * h):int(.95 * h), int(.10 * w):int(.86 * w)]       # corta lombada, bordas e fundo
    L, A, B = lab(im)
    a0, b0 = np.median(A), np.median(B)                                  # cor do pergaminho da própria página
    dA, dB = A - a0, B - b0
    green = (dA < -7) & (L > 25)
    blue = (dB < -12) & (L > 15)
    red = (dA > 12) & (L > 30)
    ochre = (dB > 15) & (dA <= 12) & (L > 50) & ~red
    return green, blue, red, ochre

def features(path):
    green, blue, red, ochre = masks(path)
    paint = green | blue | red | ochre
    n = paint.sum() + 1; hh = paint.shape[0]; top = slice(0, hh // 3); bot = slice(2 * hh // 3, hh)
    return [paint.mean(), green.sum() / n, blue.sum() / n, red.sum() / n, ochre.sum() / n,
            blue[top].sum() / (paint[top].sum() + 1), (red[bot].sum() + ochre[bot].sum()) / (paint[bot].sum() + 1),
            (red[top].sum() + ochre[top].sum()) / (paint[top].sum() + 1)]

def zl_pages():
    rows = json.load(open("zl_paginas.json"))
    return {f: (p, v) for f, p, v in rows}

def page_text(folios, comma="split", skel=False):
    L, _ = parse("ZL.txt"); t = defaultdict(list)
    for l in L:
        if l.folio in folios and l.ltype[0] == "P":
            ws = [w for w in (l.split if comma == "split" else l.join) if "?" not in w]
            if skel:
                ws = [re.sub(r"e+", "e", re.sub(r"i+", "i", re.sub(r"c[tpf]h", "ckh", w).replace("sh", "ch").replace("t", "k").replace("f", "p"))) for w in ws]
            t[l.folio].extend(ws)
    return t

def tfidf(texts):
    D = len(texts); df = Counter(w for ws in texts.values() for w in set(ws))
    vec = {}
    for f, ws in texts.items():
        c = Counter(ws); v = {w: (1 + math.log(k)) * math.log(D / df[w]) for w, k in c.items() if df[w] < D}
        nrm = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[f] = {w: x / nrm for w, x in v.items()}
    return vec

def cos(a, b):
    if len(a) > len(b): a, b = b, a
    return sum(x * b.get(w, 0) for w, x in a.items())

def spearman(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1])

def mantel(fols, imgsim, txtsim, pair_ok, reps=2000, seed=1):
    rng = random.Random(seed)
    pairs = [(i, j) for i in range(len(fols)) for j in range(i + 1, len(fols)) if pair_ok(fols[i], fols[j])]
    t = np.array([txtsim[i][j] for i, j in pairs])
    def r_for(perm):
        return spearman(np.array([imgsim[perm[i]][perm[j]] for i, j in pairs]), t)
    ident = list(range(len(fols))); r0 = r_for(ident)
    null = []
    for _ in range(reps):
        p = ident[:]; rng.shuffle(p); null.append(r_for(p))
    pval = (1 + sum(x >= r0 for x in null)) / (reps + 1)
    return r0, pval, len(pairs), float(np.mean(null)), float(np.std(null))

if __name__ == "__main__":
    Z = zl_pages()
    herb = [f for f, (p, v) in Z.items() if v.get("I") == "H" and int(re.match(r"f(\d+)", f).group(1)) <= 66]
    feats = {f: features(f"pdfimg/p{Z[f][0] + 2:03d}.jpg") for f in herb}
    json.dump(feats, open("imagem_features.json", "w"))
    for skel in (False, True):
        texts = page_text(set(herb), skel=skel)
        fols = [f for f in herb if len(texts.get(f, [])) >= 30]
        X = np.array([feats[f] for f in fols]); X = (X - X.mean(0)) / (X.std(0) + 1e-9)
        imgsim = -np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))       # semelhança = -distância
        V = tfidf({f: texts[f] for f in fols})
        txtsim = [[cos(V[a], V[b]) for b in fols] for a in fols]
        Q = {f: Z[f][1].get("Q") for f in fols}; LG = {f: Z[f][1].get("L") for f in fols}
        tag = "grafias fundidas" if skel else "palavras como estão"
        for name, ok in [("todos os pares", lambda a, b: True),
                         ("mesmo dialeto, cadernos diferentes", lambda a, b: LG[a] == LG[b] and Q[a] != Q[b]),
                         ("só A, cadernos diferentes", lambda a, b: LG[a] == LG[b] == "A" and Q[a] != Q[b]),
                         ("mesmo caderno (efeito de lote)", lambda a, b: Q[a] == Q[b])]:
            r, p, n, m, s = mantel(fols, imgsim, txtsim, ok)
            print(f"[{tag}] {name:36s} pares {n:5d}  Spearman {r:+.3f}  (nulo {m:+.3f} ± {s:.3f})  P = {p:.4f}")
