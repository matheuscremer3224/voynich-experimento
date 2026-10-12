"""Fase 10f – G-deriva: o mesmo gerador sem conteúdo (G-casas2), mas com parâmetros que mudam devagar ao longo do
códice. Cada página é gerada por um modelo ajustado às páginas VIZINHAS da mesma seção e dialeto (até 3 fólios para
cada lado, peso 3) mais o resto da seção (peso 1) — nunca à própria página, para não copiar palavras dela."""
import random
from collections import defaultdict
import gerador
from agrupamento import clustering
from agrupamento2 import page_words, keywords, adjacency, folio_key

def generate_drift(pages, seed=21, radius=3, weight=3):
    rng_seed = seed
    groups = defaultdict(list)
    for pg in pages: groups[(pg["I"], pg["L"])].append(pg)
    for g in groups: groups[g].sort(key=lambda p: folio_key(p["folio"]))
    out = {}
    for g, pgs in groups.items():
        for i, pg in enumerate(pgs):
            neigh = [pgs[j] for j in range(max(0, i - radius), min(len(pgs), i + radius + 1)) if j != i]
            rest = [p for j, p in enumerate(pgs) if j != i]
            train = neigh * weight + rest
            if len(rest) < 3:                       # seção/dialeto quase vazio: recorre ao códice todo (sem a página)
                train = [p for p in pages if p is not pg]
            model = gerador.SlotModel(train, dial=True)
            out[pg["folio"]] = gerador.generate([pg], model, "casas2", seed=rng_seed + i)[0]
    return [out[pg["folio"]] for pg in pages]

if __name__ == "__main__":
    import json
    V = gerador.real_pages()
    D = generate_drift(V)
    G = gerador.generate(V, gerador.SlotModel(V, dial=True), "casas2", seed=13)
    rng = random.Random(8)
    grp = lambda pg: (pg["I"], pg["L"]) if pg["I"] in ("H", "B", "S") else None
    for name, pages in [("Voynich", V), ("G-casas2", G), ("G-deriva", D)]:
        idx, n = clustering(pages)
        print(f"{name:9s} agrupamento por página {idx:+.3f}")
        for g, pgs in sorted(page_words(pages, grp).items(), key=lambda x: str(x[0])):
            if len(pgs) < 8: continue
            obs, exp, nn, ex = keywords(pgs, rng); a, f = adjacency(pgs)
            print(f"   {str(g):12s} palavras-chave {obs:2d} (acaso {exp:4.1f}) de {nn:3d} | cosseno vizinhas {a:.3f} x distantes {f:.3f}")
    b = gerador.battery(D, "G-deriva")
    json.dump(b, open("deriva_bateria.json", "w"), indent=1)
    keys = ["h2", "compr", "TTR", "hapax", "razao", "F1esp", "rep", "quase", "m_curtas", "m_longas", "m_meio", "par_gallows",
            "ed_A", "ed_B", "JS_H_B", "eco", "eco_acaso", "conc_rot", "conc_nulo", "freq_rot", "freq_nulo"]
    print("G-deriva bateria: " + "; ".join(f"{k}={b[k]:.3f}" for k in keys))
