"""Fase 18 – Coordenador: aplica criterios.md, de forma mecânica, aos resultados do Cifrador, Comparador e Controle.
Não mede nada: só lê os JSON e compara cada mediana com a régua de B. Saída: coordenador_decisao.md e .json."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "results", "fase-18")
SUF = sys.argv[1] if len(sys.argv) > 1 else ""          # sufixo opcional para rodadas corrigidas (ex.: "_v2")
cif = json.load(open(os.path.join(SAIDA, f"cifrador_resultados{SUF}.json")))
cmp_ = json.load(open(os.path.join(SAIDA, f"comparador_resultados{SUF}.json")))
ctl = json.load(open(os.path.join(SAIDA, f"controle_resultados{SUF}.json")))
R = cmp_["regua_B"]
PROP = {"P1": ["TTR", "hapax", "zipf"], "P2": ["agrup_200", "bloco8_200", "viz_200"],
        "P3": ["h2", "compr", "razao", "F1esp", "rep"]}
LATIM = [k for k, v in cif.items() if v["lingua"] == "latim"]
OUTROS = [k for k in cif if k not in LATIM]

def dentro(m, x):
    lo, hi = R[m][0], R[m][1]
    return x is not None and lo <= x <= hi

def avaliar(med):
    out = {}
    for p, ms in PROP.items():
        falhas = [m for m in ms if not dentro(m, med.get(m))]
        out[p] = {"passa": not falhas, "falhas": falhas}
    return out

linhas = []
res = {}
for t in LATIM + OUTROS:
    res[t] = avaliar(cif[t]["naibbe_mediana"])

# o mesmo teste aplicado às referências (informativo; não entra na decisão)
def med_ctl(chave):
    return ctl[chave] if chave in ctl else None
ref = {}
for nome, m in [("Voynich B inteiro", cmp_["medidas"]["B"]), ("Voynich A inteiro", cmp_["medidas"]["A"])]:
    ref[nome] = avaliar(m)
for chave, m in ctl.get("medianas", {}).items():
    if " B" in chave or "VB" in chave:
        ref[chave] = avaliar(m)

n_p1p2 = sum(res[t]["P1"]["passa"] and res[t]["P2"]["passa"] for t in LATIM)
n_falha_p2 = sum(not res[t]["P2"]["passa"] for t in LATIM)
if n_p1p2 >= 3:
    dec = "A FAVOR"
elif n_falha_p2 >= 3:
    dec = "CONTRA"
else:
    dec = "INCONCLUSIVO"

fmt = lambda m, x: "–" if x is None else (f"{x:.2%}" if m in ("hapax", "rep") else f"{x:+.4f}" if m in ("agrup_200", "bloco8_200", "viz_200") else f"{x:.4f}")
md = ["# Fase 18 – Aplicação mecânica de criterios.md", "",
      f"Régua de B (do Comparador). Textos latinos: {', '.join(LATIM)}. Informativos: {', '.join(OUTROS)}.", "",
      "| Texto | P1 | P2 | P3 (contexto) | métricas fora da régua |", "|---|---|---|---|---|"]
for t in LATIM + OUTROS:
    r = res[t]
    fora = []
    for p in ("P1", "P2", "P3"):
        for m in r[p]["falhas"]:
            fora.append(f"{m}={fmt(m, cif[t]['naibbe_mediana'].get(m))} [{fmt(m, R[m][0])}; {fmt(m, R[m][1])}]")
    lab = lambda p: "passa" if r[p]["passa"] else "falha"
    md.append(f"| {t}{'' if t in LATIM else ' (inf.)'} | {lab('P1')} | {lab('P2')} | {lab('P3')} | {'; '.join(fora)} |")
md += ["", "Mesmo teste aplicado às referências (informativo):", "", "| Referência | P1 | P2 | P3 | fora da régua |", "|---|---|---|---|---|"]
for nome, r in ref.items():
    lab = lambda p: "passa" if r[p]["passa"] else "falha"
    md.append(f"| {nome} | {lab('P1')} | {lab('P2')} | {lab('P3')} | {', '.join(r['P1']['falhas'] + r['P2']['falhas'] + r['P3']['falhas'])} |")
md += ["", f"Textos latinos que passam em P1 e P2: {n_p1p2} de {len(LATIM)}. Que falham em P2: {n_falha_p2} de {len(LATIM)}.",
       "", f"**Decisão pela regra registrada: {dec}.**"]
open(os.path.join(SAIDA, f"coordenador_decisao{SUF}.md"), "w").write("\n".join(md) + "\n")
json.dump({"decisao": dec, "por_texto": res, "referencias": ref, "n_p1p2": n_p1p2, "n_falha_p2": n_falha_p2},
          open(os.path.join(SAIDA, f"coordenador_decisao{SUF}.json"), "w"), indent=1)
print("\n".join(md))
