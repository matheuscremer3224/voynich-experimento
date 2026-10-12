"""Fase 10g – G-cópia2: autocitação com janela que atravessa páginas (últimas 300 palavras do códice) e 1–2 mutações."""
import random, json
import gerador
from agrupamento import clustering
from agrupamento2 import page_words, keywords, adjacency
V = gerador.real_pages()
C2 = gerador.generate(V, gerador.SlotModel(V, dial=True), "copia2", seed=31)
rng = random.Random(8)
grp = lambda pg: (pg["I"], pg["L"]) if pg["I"] in ("H", "B", "S") else None
idx, n = clustering(C2); print(f"G-cópia2 agrupamento por página {idx:+.3f}")
for g, pgs in sorted(page_words(C2, grp).items(), key=lambda x: str(x[0])):
    if len(pgs) < 8: continue
    obs, exp, nn, ex = keywords(pgs, rng); a, f = adjacency(pgs)
    print(f"   {str(g):12s} palavras-chave {obs:2d} (acaso {exp:4.1f}) de {nn:3d} | cosseno vizinhas {a:.3f} x distantes {f:.3f}")
b = gerador.battery(C2, "G-cópia2"); json.dump(b, open("copia2_bateria.json", "w"), indent=1)
keys = ["h2", "compr", "dp", "TTR", "hapax", "razao", "F1esp", "rep", "quase", "m_curtas", "m_longas", "m_meio", "par_gallows",
        "ed_A", "ed_B", "JS_H_B", "eco", "eco_acaso", "conc_rot", "conc_nulo", "freq_rot", "freq_nulo"]
print("G-cópia2 bateria: " + "; ".join(f"{k}={b[k]:.3f}" for k in keys))
