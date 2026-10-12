"""Fase 10d – De onde vem o agrupamento por página: tema de cada página ou deriva gradual de hábitos de escrita?
(a) 'Palavras-chave de página': palavras com 5+ ocorrências na seção, das quais metade ou mais numa só página;
    comparado com o esperado se as ocorrências caíssem ao acaso (simulação).
(b) Semelhança de vocabulário (cosseno) entre páginas vizinhas na ordem dos fólios x páginas distantes da mesma seção.
Deriva => vizinhas bem mais parecidas; tema por página => palavras-chave sem vizinhança especial."""
import math, random, statistics as st
from collections import Counter, defaultdict
import gerador
from agrupamento import latin_pages

def folio_key(f):
    import re
    m = re.match(r"f(\d+)([rv])(\d*)", f)
    return (int(m.group(1)), m.group(2), int(m.group(3) or 0)) if m else (999, f, 0)

def page_words(pages, group):
    by = defaultdict(list)
    for pg in pages:
        g = group(pg)
        if g is None: continue
        ws = [w for typ, line, _ in pg["lines"] if typ == "P" for w in line]
        if len(ws) >= 40: by[g].append((pg["folio"], ws))
    for g in by: by[g].sort(key=lambda x: folio_key(x[0]))
    return by

def keywords(pgs, rng, reps=30):
    sizes = [len(ws) for _, ws in pgs]; N = sum(sizes)
    tot = Counter(w for _, ws in pgs for w in ws)
    cand = [w for w, c in tot.items() if c >= 5]
    counts = [Counter(ws) for _, ws in pgs]
    obs = sum(1 for w in cand if max(c[w] for c in counts) >= 0.5 * tot[w])
    sim = []
    pidx = [i for i, n in enumerate(sizes) for _ in range(n)]
    for _ in range(reps):
        k = 0
        for w in cand:
            draws = Counter(rng.choice(pidx) for _ in range(tot[w]))
            k += max(draws.values()) >= 0.5 * tot[w]
        sim.append(k)
    return obs, st.mean(sim), len(cand), [w for w in cand if max(c[w] for c in counts) >= 0.5 * tot[w]]

def cos(a, b):
    ks = set(a) & set(b)
    return sum(a[k] * b[k] for k in ks) / math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()))

def adjacency(pgs):
    cs = [Counter(ws) for _, ws in pgs]
    adj = [cos(cs[i], cs[i + 1]) for i in range(len(cs) - 1)]
    far = [cos(cs[i], cs[j]) for i in range(len(cs)) for j in range(i + 5, len(cs))]
    return st.mean(adj), st.mean(far) if far else float("nan")

if __name__ == "__main__":
    rng = random.Random(8)
    V = gerador.real_pages()
    G = gerador.generate(V, gerador.SlotModel(V, dial=True), "casas2", seed=13)
    C = gerador.generate(V, gerador.SlotModel(V), "copia", seed=12)
    grp = lambda pg: (pg["I"], pg["L"]) if pg["I"] in ("H", "B", "S") else None
    LP = latin_pages()
    for name, pages, gfun in [("Voynich", V, grp), ("G-casas2", G, grp), ("G-cópia", C, grp), ("Isidoro", LP, lambda pg: pg["I"])]:
        by = page_words(pages, gfun)
        for g, pgs in sorted(by.items(), key=lambda x: str(x[0])):
            if len(pgs) < 8: continue
            obs, exp, n, ex = keywords(pgs, rng)
            a, f = adjacency(pgs)
            print(f"{name:9s} {str(g):12s} páginas {len(pgs):3d} | palavras-chave de página {obs:3d} (acaso {exp:5.1f}) de {n:4d} "
                  f"| cosseno vizinhas {a:.3f} x distantes {f:.3f}" + (f" | ex.: {', '.join(ex[:6])}" if name == "Voynich" else ""))
