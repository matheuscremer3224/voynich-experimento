"""Fase 10c – As palavras se concentram em certas páginas mais do que um gerador local (ajustado por seção) produz?
Índice de agrupamento: para cada palavra com 10+ ocorrências na seção, compara o número de páginas onde ela aparece com
o esperado se suas ocorrências caíssem ao acaso nas páginas da seção (proporcional ao tamanho da página).
Índice = média de (esperado − observado) / esperado. Calibração: o mesmo índice num texto com significado (Isidoro,
livros XII, XVI e XVII, em 'páginas' de ~300 palavras) e no gerador local ajustado a esse texto."""
import random, re, statistics as st
from collections import Counter, defaultdict
from ivtff import units
import gerador, lexicon

def clustering(pages):
    by = defaultdict(list)
    for pg in pages:
        ws = [w for typ, line, _ in pg["lines"] if typ == "P" for w in line]
        if ws: by[pg["I"]].append(ws)
    vals = []
    for sec, pgs in by.items():
        N = sum(map(len, pgs)); sizes = [len(p) for p in pgs]
        tot = Counter(w for p in pgs for w in p)
        sets = [set(p) for p in pgs]
        for w, c in tot.items():
            if c < 10: continue
            exp = sum(1 - (1 - n / N) ** c for n in sizes)
            obs = sum(w in s for s in sets)
            vals.append((exp - obs) / exp)
    return st.mean(vals), len(vals)

def latin_pages():
    pages = []
    for book in ("12", "16", "17"):
        raw = open(lexicon.BASE + f"isidore/{book}.txt", encoding="utf-8", errors="ignore").read()
        ws = re.findall(r"[a-z]+", lexicon.norm(raw))
        for i in range(0, len(ws) - 300, 300):
            chunk = ws[i:i + 300]
            lines = [("P", chunk[k:k + 9], k == 0) for k in range(0, 300, 9)]
            pages.append({"folio": f"{book}-{i}", "I": book, "L": "A", "lines": lines})
    return pages

if __name__ == "__main__":
    V = gerador.real_pages()
    m2 = gerador.SlotModel(V, dial=True)
    G = gerador.generate(V, m2, "casas2", seed=13)
    m1 = gerador.SlotModel(V)
    C = gerador.generate(V, m1, "copia", seed=12)
    LP = latin_pages()
    mL = gerador.SlotModel(LP)
    LG = gerador.generate(LP, mL, "casas", seed=5)
    for name, pg in [("Voynich", V), ("G-casas2 (sem conteúdo)", G), ("G-cópia (autocitação)", C),
                     ("Latim de Isidoro (com significado)", LP), ("Gerador local ajustado ao latim", LG)]:
        idx, n = clustering(pg)
        print(f"{name:38s} índice de agrupamento por página {idx:+.3f}  ({n} palavras)")
