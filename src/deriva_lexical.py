"""Fase 15 – Um gerador 'honesto' para a deriva lexical: nenhuma palavra é copiada do texto real.
Cada seção×dialeto tem um repertório de 3.000 tipos gerados pela própria cadeia do G-casas2. O peso (log) de cada tipo
faz um passeio aleatório lento de página em página (correlação exp(-1/Lpág)). Cada palavra do texto vem do repertório
com prob. p (respeitando a regra de emenda: primeiro sorteia a unidade inicial, depois um tipo do repertório que comece
por ela) ou é nova, da cadeia. Mede agrupamento por página e por blocos de 8, palavras-chave de página, vizinhança,
TTR, h2 e repetição."""
import math, random, itertools, json, re
from collections import Counter, defaultdict
import numpy as np
import gerador
from gerador import units, fill_line, to_m
from copia3_grade import summary
from agrupamento import clustering
from agrupamento_grafia import blocks
from agrupamento2 import folio_key

def generate_lex(pages, model, p_pool, Lp, sigma, seed=61, pool_size=3000):
    rng = random.Random(seed); nprng = np.random.default_rng(seed)
    groups = defaultdict(list)
    for pg in pages: groups[(pg["I"], pg["L"])].append(pg)
    out = {}
    for g, pgs in groups.items():
        pgs = sorted(pgs, key=lambda p: folio_key(p["folio"]))
        types = [model.word(g, rng, "mid", rng.choice(["y", "n", "l", "r"]), dial=g[1]) for _ in range(pool_size)]
        tc = Counter(types); vocab = list(tc); base = np.log(np.array([tc[w] for w in vocab], float))
        x = nprng.normal(0, sigma, len(vocab)); rho = math.exp(-1.0 / Lp)
        by_first = defaultdict(list)
        for i, w in enumerate(vocab): by_first[units(w)[0]].append(i)
        for pg in pgs:
            x = rho * x + math.sqrt(1 - rho * rho) * nprng.normal(0, sigma, len(vocab))
            wts = np.exp(base + x)
            npg = {"folio": pg["folio"], "I": pg["I"], "L": pg["L"], "lines": []}
            widths = sorted(len(".".join(ws)) for t, ws, _ in pg["lines"] if t == "P")
            full = widths[int(0.5 * len(widths))] if widths else 0
            for typ, ws, par in pg["lines"]:
                if typ == "L":
                    npg["lines"].append(("L", [model.word(g, rng, "label", dial=g[1]) for _ in ws], False)); continue
                state = {"first": True}
                def make(prev):
                    kind = ("par" if par else "line") if state["first"] else "mid"; state["first"] = False
                    if kind == "mid" and rng.random() < p_pool:
                        last = units(prev)[-1]
                        u1 = model._draw(model.junc[g].get(last, Counter()), model.jpool.get(last) or model.fpool["line"], rng)
                        idx = by_first.get(u1)
                        if idx:
                            w_ = wts[idx]; return vocab[idx[int(nprng.choice(len(idx), p=w_ / w_.sum()))]]
                    return model.word(g, rng, kind, units(prev)[-1] if (kind == "mid" and prev) else None, dial=g[1]) if kind == "mid" else model.word(g, rng, kind, dial=g[1])
                target = len(".".join(ws))
                line = fill_line(target, make, rng, allow_m=target >= full)
                if target >= full and line and not line[-1].endswith("m") and rng.random() < gerador.Q_MARGEM:
                    m = to_m(line[-1]); line[-1] = m or line[-1]
                npg["lines"].append((typ, line, par))
            out[pg["folio"]] = npg
    return [out[p["folio"]] for p in pages]

if __name__ == "__main__":
    V = gerador.real_pages(); M = gerador.SlotModel(V, dial=True)
    rng = random.Random(6)
    sV = summary(V, rng); sV["bloco8"] = clustering(blocks(V, 8))[0]
    print("Voynich", {k: round(v, 3) for k, v in sV.items()})
    res = {"Voynich": sV}
    for p, Lp, sg in itertools.product([0.5, 0.8], [5, 15, 40], [1.0, 2.0]):
        G = generate_lex(V, M, p, Lp, sg)
        s = summary(G, rng); s["bloco8"] = clustering(blocks(G, 8))[0]
        res[f"p={p} L={Lp} s={sg}"] = s
        print(f"repertório={p} correlação={Lp} pág. σ={sg}", {k: round(v, 3) for k, v in s.items()})
    json.dump(res, open("deriva_lexical.json", "w"), indent=1)
