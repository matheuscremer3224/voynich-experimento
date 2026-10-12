"""Fase 18 – tabela final (entrega 1): manuscrito A e B, Naibbe sobre latim, modelo de regras e embaralhado, métrica por
métrica, mais as linhas dos testes corretivos. Só lê os JSON dos agentes e do coordenador."""
import json, os, statistics as st
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "results", "fase-18")
J = lambda n: json.load(open(os.path.join(SAIDA, n)))
cif, cmp_, ctl = J("cifrador_resultados.json"), J("comparador_resultados.json"), J("controle_resultados.json")
t123, t5, ext = J("coordenador_T1T2T3.json"), J("coordenador_T5.json"), J("coordenador_extras.json")
LAT = ["isidoro17", "plinio16", "apicius", "hyginus", "cesar"]
R = cmp_["regua_B"]

def med(vals):
    v = [x for x in vals if x is not None]; return st.median(v) if v else None
def faixa(vals):
    v = [x for x in vals if x is not None]; return (min(v), max(v)) if v else None

COL = {
    "VA": cmp_["medidas"]["A"],
    "VB": cmp_["medidas"]["B"],
    "Naibbe original, latim": {k: med([cif[t]["naibbe_mediana"].get(k) for t in LAT]) for k in cif["isidoro17"]["naibbe_mediana"]},
    "Naibbe original, italiano (Dante)": cif["dante"]["naibbe_mediana"],
    "Naibbe com deriva (α=10), latim ‡": {k: med([t5["ii"]["dirichlet 10"][t].get(k) for t in LAT]) for k in t5["ii"]["dirichlet 10"]["isidoro17"] if k not in ("passa_T2",)},
    "Latim sem cifra (P1 e P2 = código palavra a palavra) †": {k: med([cif[t]["claro"].get(k) for t in LAT]) for k in cif["isidoro17"]["claro"]},
    "Regras-deriva B": ctl["medianas"]["regras-deriva mediana B"],
    "Regras-casas2 B": ctl["regras"]["regras-casas2 s13 B"],
    "VB embaralhado global": ctl["medianas"]["VB global mediana"],
    "VB embaralhado na página": ctl["medianas"]["VB pagina mediana"],
}
FAIXA_NB = {k: faixa([cif[t]["naibbe_mediana"].get(k) for t in LAT]) for k in cif["isidoro17"]["naibbe_mediana"]}
# critério T2 (R) e tamanho casado
Rcol = {"VA": ext["VA"]["R"], "VB": 1.0,
        "Naibbe original, latim": med([med([t123["T2"][t][f"naibbe s{s}"]["R"] for s in (1, 2, 3)]) for t in LAT]),
        "Naibbe com deriva (α=10), latim ‡": med([t5["ii"]["dirichlet 10"][t]["R"] for t in LAT]),
        "Latim sem cifra (P1 e P2 = código palavra a palavra) †": med([t123["T2"][t]["código"]["R"] for t in LAT]),
        "Regras-deriva B": med([ext[f"regras-deriva B s{s}"]["R"] for s in (13, 14, 15)]),
        "Regras-casas2 B": ext["regras-casas2 B s13"]["R"],
        "VB embaralhado global": ext["VB embaralhado global s7"]["R"], "VB embaralhado na página": ext["VB embaralhado na página s7"]["R"]}
Pcol = {"VA": sum([ext["VA"]["passa_T2"]]), "VB": 1,
        "Naibbe original, latim": sum(t123["decisao_v2"]["passa_T2"][t] for t in LAT),
        "Naibbe com deriva (α=10), latim ‡": t5["ii"]["dirichlet 10"]["n_passa_T2"],
        "Latim sem cifra (P1 e P2 = código palavra a palavra) †": sum(t123["T2"][t]["código"]["passa"] for t in LAT),
        "Regras-deriva B": sum(ext[f"regras-deriva B s{s}"]["passa_T2"] for s in (13, 14, 15)),
        "Regras-casas2 B": int(ext["regras-casas2 B s13"]["passa_T2"]),
        "VB embaralhado global": int(ext["VB embaralhado global s7"]["passa_T2"]), "VB embaralhado na página": int(ext["VB embaralhado na página s7"]["passa_T2"])}
Pden = {"VA": 1, "VB": 1, "Naibbe original, latim": 5, "Naibbe com deriva (α=10), latim ‡": 5,
        "Latim sem cifra (P1 e P2 = código palavra a palavra) †": 5, "Regras-deriva B": 3, "Regras-casas2 B": 1, "VB embaralhado global": 1, "VB embaralhado na página": 1}
TN = {"VA": (ext["VA"]["TTR_N"], ext["VA"]["hapax_N"]), "VB": (ext["VB"]["TTR_N"], ext["VB"]["hapax_N"]),
      "Naibbe original, latim": (med([t123["T3"][t]["mediana_TTR"] for t in LAT]), med([t123["T3"][t]["mediana_hapax"] for t in LAT])),
      "Regras-deriva B": (med([ext[f"regras-deriva B s{s}"]["TTR_N"] for s in (13, 14, 15)]), med([ext[f"regras-deriva B s{s}"]["hapax_N"] for s in (13, 14, 15)])),
      "Regras-casas2 B": (ext["regras-casas2 B s13"]["TTR_N"], ext["regras-casas2 B s13"]["hapax_N"]),
      "VB embaralhado global": (ext["VB embaralhado global s7"]["TTR_N"], ext["VB embaralhado global s7"]["hapax_N"]),
      "VB embaralhado na página": (ext["VB embaralhado na página s7"]["TTR_N"], ext["VB embaralhado na página s7"]["hapax_N"])}

LIN = [("n", "fichas de texto", "{:,.0f}", "–"), ("h2", "h2 (bits)", "{:.2f}", "P3"), ("compr", "comprimento médio (unid.)", "{:.2f}", "P3"),
       ("TTR", "razão tipo/ocorrência", "{:.3f}", "P1"), ("hapax", "formas únicas (hapax)", "{:.1%}", "P1"),
       ("zipf", "inclinação de Zipf", "{:.2f}", "P1"), ("razao", "MI na junção ÷ MI dentro", "{:.2f}", "P3"),
       ("F1esp", "F1 ao recolocar o espaço", "{:.3f}", "P3"), ("rep", "repetição imediata", "{:.2%}", "P3"),
       ("agrup_200", "agrupamento por página (200 fichas)", "{:+.3f}", "P2"), ("bloco8_200", "agrupamento em blocos de 8", "{:+.3f}", "P2"),
       ("viz_200", "vizinhas − distantes", "{:+.3f}", "P2"), ("chave_frac_200", "palavras-chave de página", "{:.1%}", "–")]
def f(fmt, v):
    if v is None or (isinstance(v, float) and v != v): return "–"
    return fmt.format(v).replace(",", "X").replace(".", ",").replace("X", ".")
nomes = list(COL)
md = ["# Fase 18 – Tabela comparativa final", "",
      "Valores: manuscrito (ZL3b, vírgula = espaço); Naibbe = mediana das sementes 1–3 em cada texto e, depois, mediana dos "
      "5 textos latinos (faixa entre textos na coluna seguinte); regras-deriva = mediana das sementes 13–15; embaralhados = "
      "mediana das sementes 7–8. Régua de B = [mín; máx] registrado em criterios.md.", "",
      "| Métrica | Prop. | Régua de B | " + " | ".join(nomes[:3]) + " | faixa Naibbe (5 textos) | " + " | ".join(nomes[3:]) + " |",
      "|---|---|---|" + "---|" * (len(nomes) + 1)]
for k, lab, fmt, prop in LIN:
    rg = f"[{f(fmt, R[k][0])}; {f(fmt, R[k][1])}]" if k in R else "–"
    fx = FAIXA_NB.get(k); fxs = f"{f(fmt, fx[0])} a {f(fmt, fx[1])}" if fx else "–"
    cells = [f(fmt, COL[n].get(k)) for n in nomes]
    md.append(f"| {lab} | {prop} | {rg} | " + " | ".join(cells[:3]) + f" | {fxs} | " + " | ".join(cells[3:]) + " |")
cells = [f"{f('{:+.2f}', Rcol[n])} ({Pcol[n]}/{Pden[n]})" if n in Rcol else "–" for n in nomes]
md.append("| **T2: recuperação R do agrupamento (passam)** | P2 | ≥ 0,25 e > p95 do nulo | " + " | ".join(cells[:3]) + " | – | " + " | ".join(cells[3:]) + " |")
cells = [f"{f('{:.3f}', TN[n][0])}" if n in TN else "–" for n in nomes]
md.append("| **T3: TTR nas primeiras 10.974 fichas** | P1 | sub. de B: [0,261; 0,294] | " + " | ".join(cells[:3]) + " | – | " + " | ".join(cells[3:]) + " |")
cells = [f"{f('{:.1%}', TN[n][1])}" if n in TN else "–" for n in nomes]
md.append("| **T3: hapax nas primeiras 10.974 fichas** | P1 | sub. de B: [68,0%; 70,3%] | " + " | ".join(cells[:3]) + " | – | " + " | ".join(cells[3:]) + " |")
t3b = J("coordenador_T3b.json")
w = {"VB": t3b["VB"], "Naibbe original, latim": {k: [None, med([t3b[f"naibbe {t} s1"][k][1] for t in LAT]), None] for k in ("TTR", "hapax")},
     "Regras-deriva B": {k: [None, med([t3b[f"regras-deriva B s{s_}"][k][1] for s_ in (13, 14, 15)]), None] for k in ("TTR", "hapax")}}
for k, lab, fm in (("TTR", "TTR", "{:.3f}"), ("hapax", "hapax", "{:.1%}")):
    cells = [f(fm, w[n][k][1]) if n in w else "–" for n in nomes]
    rg = f"VB: [{f(fm, t3b['VB'][k][0])}; {f(fm, t3b['VB'][k][2])}]"
    md.append(f"| **T3b: {lab} em janelas contíguas de 10.974 fichas (mediana)** | P1 | {rg} | " + " | ".join(cells[:3]) + " | – | " + " | ".join(cells[3:]) + " |")
dec = [f"{min(t5['ii']['dirichlet 10'][t]['decifra'] for t in LAT):.0%}"]
md.append("| decifração por decrypt_naibbe.py | – | – | – | – | " + f"{min(cif[t]['decifra'] for t in LAT):.0%} | – | {cif['dante']['decifra']:.0%} | {dec[0]} | – | – | – | – | – |")
md += ["", "† O código palavra a palavra (cada tipo latino → tipo de VB de mesmo posto) tem P1 e P2 idênticos aos do latim "
       "sem cifra (verificado em T1); suas colunas de P3 dependem do vocabulário de destino e não são mostradas aqui. Nas "
       "linhas T3, o código tem menos de 10.974 fichas.",
       "‡ Variante, NÃO a cifra original: mesmas tabelas e glifos, mas os pesos das tabelas são sorteados por página "
       "(Dirichlet com α = 10 × pesos do autor). Mantém a verificação de ambiguidade e a decifração de 100%. Com α = 5 e α = 3 "
       "(coordenador_T5b.json) o agrupamento chega ao nível de VB (R de 0,73 a 1,28), mas a vizinhança (0,093 a 0,197) e os "
       "blocos de 8 (0,071 a 0,155) passam do ponto: as três métricas de P2 juntas dentro da régua em 0 de 10 casos "
       "(agrupamento e vizinhança juntos em 1 de 10). Com α = 1 a decifração cai a 99,97%.",
       "As subamostras de B que definem a régua do T3 são metades de páginas sorteadas, espalhadas pelas seções; "
       "uma janela contínua de VB com o mesmo tamanho dá TTR 0,234 (coluna VB). A régua justa (T3b, pedida na 2ª rodada do "
       "Cético) usa as 49 janelas contíguas de VB: TTR [0,229; 0,285], hapax [67,9%; 70,2%]. A Naibbe fica fora nas duas "
       "(TTR de todas as suas janelas ≥ 0,303); o modelo de regras fica dentro no TTR e fora no hapax (63,4% contra ≥ 67,9%)."]
open(os.path.join(SAIDA, "coordenador_tabela_final.md"), "w").write("\n".join(md) + "\n")
print("\n".join(md))
