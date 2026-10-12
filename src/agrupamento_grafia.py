"""Fase 13 – O agrupamento difuso por páginas vem do vocabulário (tema ou deriva de palavras) ou só da ortografia
(hábitos de grafia que mudam com o tempo: k/t, ch/sh, comprimento das séries de e)? Se for ortografia, fundir as
variantes deveria derrubar o índice; se for vocabulário, ele deveria resistir. Também mede quanto do índice sobrevive
quando se compara só páginas de cadernos diferentes (o que é deriva lenta some se as páginas forem distantes)."""
import re, statistics as st, random
from collections import Counter, defaultdict
import gerador
from agrupamento import clustering, latin_pages
from imagem_texto import zl_pages

def skel(w):
    w = re.sub(r"c[tpf]h", "ckh", w).replace("sh", "ch").replace("t", "k").replace("f", "p")
    return re.sub(r"e+", "e", re.sub(r"i+", "i", w))

def skel2(w):          # além disso, finais equivalentes e o/a
    w = skel(w).replace("a", "o")
    return re.sub(r"(dy|y|l|r|n|m|s)$", "#", w)

def apply(pages, fn):
    return [{**pg, "lines": [(t, [fn(w) for w in ws], p) for t, ws, p in pg["lines"]]} for pg in pages]

def blocks(pages, k):
    out = []; by = defaultdict(list)
    for pg in pages: by[(pg["I"], pg["L"])].append(pg)
    for g, pgs in by.items():
        for i in range(0, len(pgs), k):
            chunk = pgs[i:i + k]
            out.append({"folio": chunk[0]["folio"], "I": chunk[0]["I"], "L": chunk[0]["L"], "lines": [x for p in chunk for x in p["lines"]]})
    return out

if __name__ == "__main__":
    V = gerador.real_pages()
    for name, fn in [("palavras como estão", lambda w: w), ("variantes fundidas (k=t, ch=sh, e/i colapsados)", skel),
                     ("fusão forte (também o=a e finais)", skel2)]:
        print(f"Voynich, {name:48s} índice {clustering(apply(V, fn))[0]:+.3f}")
    LP = latin_pages()
    print(f"Latim, palavras como estão                               índice {clustering(LP)[0]:+.3f}")
    print(f"Latim, fusão forte análoga (vogais colapsadas, finais)   índice {clustering(apply(LP, lambda w: re.sub(r'[aeiou]+', 'a', w)[:-1] or w))[0]:+.3f}")
    for k in (1, 2, 4, 8):
        print(f"Voynich em blocos de {k} páginas vizinhas: índice {clustering(blocks(V, k))[0]:+.3f}  |  latim: {clustering(blocks(LP, k))[0]:+.3f}")
