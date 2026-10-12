"""Fase 18b – complementos para a tabela final: o critério T2 (nulo próprio + recuperação R) e o P1 com tamanho casado
(primeiras 10.974 fichas) aplicados também ao manuscrito A, ao modelo de regras e ao embaralhado."""
import json, os, random, statistics as st, sys
from collections import Counter
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
import metricas_comuns as mc
from coordenador_testes import p2, nulo, pct95, palavras, salvar

N = 10974
VB = mc.paginas_voynich(dialeto="B"); VA = mc.paginas_voynich(dialeto="A")
den = p2(VB)["agrup"] - st.mean(nulo(VB))
cwd = os.getcwd(); os.chdir(mc.BASE)
regras = {s: mc.filtrar(mc.gerar_regras("deriva", seed=s), dialeto="B") for s in (13, 14, 15)}
casas = mc.filtrar(mc.gerar_regras("casas2", seed=13), dialeto="B")
os.chdir(cwd)
corp = {"VB": VB, "VA": VA, "VB embaralhado global s7": mc.embaralhar(VB, "global", seed=7),
        "VB embaralhado na página s7": mc.embaralhar(VB, "pagina", seed=7), "regras-casas2 B s13": casas,
        **{f"regras-deriva B s{s}": g for s, g in regras.items()}}
out = {}
for nome, pg in corp.items():
    o = p2(pg)["agrup"]; nl = nulo(pg); R = (o - st.mean(nl)) / den
    w = palavras(pg)[:N]
    out[nome] = {"agrup_200": o, "nulo_media": st.mean(nl), "nulo_p95": pct95(nl), "R": R, "passa_T2": o > pct95(nl) and R >= 0.25,
                 "TTR_N": len(set(w)) / len(w), "hapax_N": sum(1 for c in Counter(w).values() if c == 1) / len(set(w)), "N": len(w)}
    print(nome, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in out[nome].items()}, flush=True)
salvar("extras", out)
