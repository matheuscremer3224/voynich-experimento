"""Fase 10i – G-repertório: o escriba tem um repertório de palavras cujo peso decai devagar (meia-vida em palavras) e
cresce a cada uso; cada palavra nova vem do repertório (prob. 1-p) ou do G-casas2 (prob. p). Sem conteúdo."""
import random, itertools, json
import gerador
from copia3_grade import summary, V, M
rng = random.Random(5)
out = {}
for pf, hl in itertools.product([0.3, 0.5, 0.7], [300, 1000, 3000]):
    gerador.P_FRESH = pf; gerador.MEIA_VIDA = hl
    G = gerador.generate(V, M, "repertorio", seed=51)
    r = summary(G, rng); out[f"p={pf} meia-vida={hl}"] = r
    print(f"novas={pf} meia-vida={hl}", {k: round(v, 3) for k, v in r.items()})
json.dump(out, open("repertorio_grade.json", "w"), indent=1)
