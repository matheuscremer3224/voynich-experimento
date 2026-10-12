"""Fase 10e – Controles de justiça para as palavras-chave de página:
(1) latim em 'páginas' do mesmo tamanho médio das páginas voynichianas de cada seção;
(2) Voynich com as grafias variantes fundidas (t=k, f=p, sh=ch, bancadas, séries de e e de i colapsadas), para o caso de
    uma mesma palavra ser escrita de vários jeitos."""
import random, re, statistics as st
from collections import defaultdict
import gerador, lexicon
from agrupamento2 import page_words, keywords

def skel(w):
    w = re.sub(r"c[tpf]h", "ckh", w).replace("sh", "ch").replace("t", "k").replace("f", "p")
    return re.sub(r"e+", "e", re.sub(r"i+", "i", w))

def latin_pages(size):
    pages = []
    for book in ("12", "16", "17"):
        ws = re.findall(r"[a-z]+", lexicon.norm(open(lexicon.BASE + f"isidore/{book}.txt", encoding="utf-8", errors="ignore").read()))
        for i in range(0, len(ws) - size, size):
            ch = ws[i:i + size]
            pages.append({"folio": f"{book}-{i}", "I": book, "L": "A", "lines": [("P", ch[k:k + 9], k == 0) for k in range(0, size, 9)]})
    return pages

rng = random.Random(9)
V = gerador.real_pages()
grp = lambda pg: (pg["I"], pg["L"]) if pg["I"] in ("H", "B", "S") else None
VS = [{**pg, "lines": [(t, [skel(w) for w in ws], p) for t, ws, p in pg["lines"]]} for pg in V]
for name, pages in [("Voynich", V), ("Voynich grafias fundidas", VS)]:
    for g, pgs in sorted(page_words(pages, grp).items(), key=lambda x: str(x[0])):
        sz = st.mean(len(ws) for _, ws in pgs)
        obs, exp, n, ex = keywords(pgs, rng)
        print(f"{name:25s} {str(g):12s} {len(pgs):3d} págs, {sz:5.0f} palavras/pág | palavras-chave {obs:3d} (acaso {exp:4.1f}) de {n}")
for size in (120, 200, 330):
    LP = latin_pages(size)
    res = []
    for g, pgs in sorted(page_words(LP, lambda pg: pg["I"]).items()):
        obs, exp, n, ex = keywords(pgs[:30], rng)
        res.append(f"livro {g}: {obs} (acaso {exp:.1f}) de {n}")
    print(f"Isidoro, páginas de {size} palavras (30 por livro) | " + " ; ".join(res))
