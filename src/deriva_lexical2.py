"""Fase 15b – grade fina em torno da região promissora do gerador de deriva lexical."""
import random, itertools, json
import gerador
from deriva_lexical import generate_lex
from copia3_grade import summary
from agrupamento import clustering
from agrupamento_grafia import blocks
V = gerador.real_pages(); M = gerador.SlotModel(V, dial=True)
rng = random.Random(6); res = {}
for p, Lp, sg in itertools.product([0.4, 0.5, 0.6], [3, 6, 10], [1.4, 1.7]):
    G = generate_lex(V, M, p, Lp, sg, pool_size=6000)
    s = summary(G, rng); s["bloco8"] = clustering(blocks(G, 8))[0]; res[f"p={p} L={Lp} s={sg}"] = s
    print(f"repertório={p} correlação={Lp} σ={sg}", {k: round(v, 3) for k, v in s.items()}, flush=True)
json.dump(res, open("deriva_lexical2.json", "w"), indent=1)
