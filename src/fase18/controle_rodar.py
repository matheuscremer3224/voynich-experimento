"""Fase 18 – CONTROLE. Mede, com metricas_comuns, (1) o modelo de texto gerado por regras (deriva, sementes 13–15;
casas2, semente 13), inteiro e por dialeto, e (2) o manuscrito embaralhado ('global' e 'pagina', sementes 7 e 8),
mais a referência sem embaralhar. Saídas: controle_resultados.json e controle_tabela.md.
Rodar:  cd src/fase18 && PYTHONHASHSEED=0 python3 controle_rodar.py"""
import json, math, os, statistics as st, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import metricas_comuns as mc

# Contorno (sem editar nada): deriva_lexical importa copia3_grade, que no import chama gerador.real_pages() com o
# caminho relativo "ZL.txt"; isso só funciona com o diretório corrente em src/. Pré-importamos lá.
os.chdir(mc.BASE)
import deriva_lexical  # noqa: F401
os.chdir(AQUI)

T0 = time.time()
def log(*a):
    print(f"[{time.time() - T0:6.1f}s]", *a, flush=True)

def nan(v):
    return isinstance(v, float) and v != v

def mediana(runs):
    """mediana, métrica a métrica, de uma lista de dicionários de medir(); ignora NaN (e registra quantos)."""
    out, avisos = {}, []
    for k in runs[0]:
        vals = [r[k] for r in runs if isinstance(r.get(k), float)]
        ok = [v for v in vals if not nan(v)]
        if len(ok) < len(vals): avisos.append(f"{k}: {len(vals) - len(ok)} NaN de {len(vals)}")
        out[k] = st.median(ok) if ok else float("nan")
    return out, avisos

def limpo(o):
    if isinstance(o, dict): return {k: limpo(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [limpo(v) for v in o]
    if nan(o): return None
    return o

R = {"regras": {}, "embaralhado": {}, "original": {}, "medianas": {}, "avisos": []}

# ---------------- 1. modelo de regras ----------------
GER = [("deriva", 13), ("deriva", 14), ("deriva", 15), ("casas2", 13)]
for tipo, s in GER:
    t = time.time(); G = mc.gerar_regras(tipo, seed=s)
    log(f"gerado {tipo} s{s}: {len(G)} páginas em {time.time() - t:.1f}s")
    for rec, pags in (("inteiro", G), ("A", mc.filtrar(G, dialeto="A")), ("B", mc.filtrar(G, dialeto="B"))):
        nome = f"regras-{tipo} s{s} {rec}"
        r = mc.medir(pags, nome); r["paginas"] = float(len(pags))
        R["regras"][nome] = r
        log(f"  {nome}: n={r['n']:.0f} pág={len(pags)} TTR={r['TTR']:.3f} agrup_200={r['agrup_200']:+.3f}")

for rec in ("inteiro", "A", "B"):
    m, av = mediana([R["regras"][f"regras-deriva s{s} {rec}"] for s in (13, 14, 15)])
    R["medianas"][f"regras-deriva mediana {rec}"] = m
    R["avisos"] += [f"regras-deriva {rec}: {a}" for a in av]

# ---------------- 2. manuscrito: original e embaralhado ----------------
X = {"V": mc.paginas_voynich(), "VB": mc.paginas_voynich(dialeto="B"), "VA": mc.paginas_voynich(dialeto="A")}
for xn, pags in X.items():
    r = mc.medir(pags, f"{xn} original"); r["paginas"] = float(len(pags))
    R["original"][f"{xn} original"] = r
    log(f"{xn} original: n={r['n']:.0f} pág={len(pags)} agrup_200={r['agrup_200']:+.3f}")
    for nivel in ("global", "pagina"):
        runs = []
        for s in (7, 8):
            E = mc.embaralhar(pags, nivel, seed=s)
            nome = f"{xn} {nivel} s{s}"
            r = mc.medir(E, nome); r["paginas"] = float(len(E))
            if r["n"] != R["original"][f"{xn} original"]["n"]:
                R["avisos"].append(f"{nome}: n={r['n']} difere do original")
            R["embaralhado"][nome] = r; runs.append(r)
            log(f"  {nome}: agrup_200={r['agrup_200']:+.3f} bloco8_200={r['bloco8_200']:+.3f} viz_200={r['viz_200']:+.3f}")
        m, av = mediana(runs)
        R["medianas"][f"{xn} {nivel} mediana"] = m
        R["avisos"] += [f"{xn} {nivel}: {a}" for a in av]

# ---------------- 3. verificação de sanidade ----------------
P2 = ["agrup_200", "bloco8_200", "viz_200"]
QUEDA = ["razao", "rep"]
san = {"regra": "global ~0: |mediana embaralhada| <= 10% de |original|; pagina ~original: desvio <= 25% do original; "
                "'cai' = valor embaralhado < original nas duas sementes", "detalhe": {}}
for xn in X:
    o = R["original"][f"{xn} original"]
    for nivel in ("global", "pagina"):
        for k in P2 + QUEDA:
            vs = [R["embaralhado"][f"{xn} {nivel} s{s}"][k] for s in (7, 8)]
            med = R["medianas"][f"{xn} {nivel} mediana"][k]
            d = {"original": o[k], "s7": vs[0], "s8": vs[1], "mediana": med,
                 "fracao_do_original": med / o[k] if o[k] else float("nan"),
                 "cai_nas_duas": all(v < o[k] for v in vs)}
            if k in P2:
                d["perto_de_zero"] = abs(med) <= 0.10 * abs(o[k])
                d["perto_do_original"] = abs(med - o[k]) <= 0.25 * abs(o[k])
            san["detalhe"][f"{xn} {nivel} {k}"] = d
R["sanidade"] = san
R["tempo_total_s"] = time.time() - T0
R["contorno"] = ("deriva_lexical pré-importado com cwd=src/ porque copia3_grade.py lê 'ZL.txt' por "
                 "caminho relativo no import")

with open(os.path.join(mc.SAIDA, "controle_resultados.json"), "w") as f:
    json.dump(limpo(R), f, indent=1, ensure_ascii=False)

# ---------------- 4. tabelas ----------------
MD = R["medianas"]; RG = R["regras"]; OR = R["original"]
tab_i = {
    "Regras-deriva inteiro (med. s13–15)": MD["regras-deriva mediana inteiro"],
    "Regras-deriva A (med.)": MD["regras-deriva mediana A"],
    "Regras-deriva B (med.)": MD["regras-deriva mediana B"],
    "Regras-casas2 inteiro (s13)": RG["regras-casas2 s13 inteiro"],
    "Regras-casas2 B (s13)": RG["regras-casas2 s13 B"],
    "VB original": OR["VB original"],
    "VB global (med. s7,s8)": MD["VB global mediana"],
    "VB página (med. s7,s8)": MD["VB pagina mediana"],
    "VA original": OR["VA original"],
    "VA global (med. s7,s8)": MD["VA global mediana"],
}
fmt = {k: f for k, _, f in mc.PRINCIPAIS}
lab = {k: l for k, l, _ in mc.PRINCIPAIS}
ii = ["| Métrica | mínimo | mediana | máximo | s13 | s14 | s15 |", "|---|---|---|---|---|---|---|"]
for k in ("TTR", "zipf", "agrup_200", "bloco8_200", "viz_200"):
    vs = [RG[f"regras-deriva s{s} B"][k] for s in (13, 14, 15)]
    cel = [min(vs), st.median(vs), max(vs)] + vs
    ii.append(f"| {lab[k]} ({k}) | " + " | ".join(fmt[k].format(v) for v in cel) + " |")

iii = ["| Corpus | nível | métrica | original | s7 | s8 | mediana | mediana/original | ~0? | ~original? | cai nas duas? |",
       "|---|---|---|---|---|---|---|---|---|---|---|"]
sim = lambda b: "sim" if b else "não"
for key, d in san["detalhe"].items():
    xn, nivel, k = key.split()
    f_ = fmt.get(k, "{:.3f}")
    iii.append(f"| {xn} | {nivel} | {k} | {f_.format(d['original'])} | {f_.format(d['s7'])} | {f_.format(d['s8'])} | "
               f"{f_.format(d['mediana'])} | {d['fracao_do_original']:.2f} | "
               f"{sim(d['perto_de_zero']) if 'perto_de_zero' in d else '–'} | "
               f"{sim(d['perto_do_original']) if 'perto_do_original' in d else '–'} | {sim(d['cai_nas_duas'])} |")

with open(os.path.join(mc.SAIDA, "controle_tabela.md"), "w") as f:
    f.write("# Fase 18 – Controle\n\n")
    f.write("## (i) Modelo de regras e manuscrito embaralhado\n\n")
    f.write(mc.tabela_md(tab_i) + "\n\n")
    f.write("## (ii) Regras-deriva, dialeto B: variação entre sementes\n\n" + "\n".join(ii) + "\n\n")
    f.write("## (iii) Verificação de sanidade (embaralhamento)\n\n")
    f.write("Regra usada: " + san["regra"] + ".\n\n" + "\n".join(iii) + "\n")
    if R["avisos"]:
        f.write("\n## Avisos\n\n" + "\n".join("- " + a for a in R["avisos"]) + "\n")

print(mc.tabela_md(tab_i)); print(); print("\n".join(ii)); print(); print("\n".join(iii))
print("avisos:", R["avisos"])
log("fim")
