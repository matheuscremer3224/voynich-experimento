"""Fase 18b – testes corretivos pedidos pelo Cético (criterios_v2.md). Usa só metricas_comuns para medir.
Rodar:  cd src/fase18 && PYTHONHASHSEED=0 python3 coordenador_testes.py T1T2T3   (ou T4, T5, T6, T7)
Cada teste grava coordenador_<teste>.json."""
import io, json, math, os, random, statistics as st, sys, time
from collections import Counter, defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import metricas_comuns as mc

LATIM = ["isidoro17", "plinio16", "apicius", "hyginus", "cesar"]
NULO_SEMENTES = list(range(100, 120))
CMP = json.load(open(os.path.join(mc.SAIDA, "comparador_resultados.json")))
REGUA = CMP["regua_B"]

def limpar(o):
    if isinstance(o, dict): return {str(k): limpar(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [limpar(v) for v in o]
    if isinstance(o, float) and (o != o or math.isinf(o)): return None
    return o

def salvar(nome, obj):
    json.dump(limpar(obj), open(os.path.join(mc.SAIDA, f"coordenador_{nome}.json"), "w"), ensure_ascii=False, indent=1)

def p2(pages, seed=5):
    """só as métricas de página em páginas de 200 fichas (mesmo código de mc.medir)."""
    return mc._page_metrics(mc.repaginar(pages, 200), random.Random(seed))

def palavras(pages):
    return [w for pg in pages for t, l, _ in pg["lines"] if t == "P" for w in l]

def nulo(pages, metrica="agrup", reps=NULO_SEMENTES):
    vals = [p2(mc.embaralhar(pages, "global", seed=s))[metrica] for s in reps]
    return vals

def pct95(vals):
    v = sorted(vals); k = 0.95 * (len(v) - 1); f = math.floor(k)
    return v[f] + (v[min(f + 1, len(v) - 1)] - v[f]) * (k - f)

# --------------------------------------------------------------------------------------------------------------
def codigo_palavra(pars_pages, VB):
    """T1: código palavra a palavra – cada tipo latino vira o tipo de VB de mesmo posto de frequência."""
    lat = Counter(w for pg in pars_pages for t, l, _ in pg["lines"] for w in l)
    vb = Counter(palavras(VB))
    rl = sorted(lat, key=lambda w: (-lat[w], w)); rv = sorted(vb, key=lambda w: (-vb[w], w))
    assert len(rl) <= len(rv), (len(rl), len(rv))
    mapa = dict(zip(rl, rv))
    return [{**pg, "lines": [(t, [mapa[w] for w in l], p) for t, l, p in pg["lines"]]} for pg in pars_pages]

def avaliar_v1(med):
    PROP = {"P1": ["TTR", "hapax", "zipf"], "P2": ["agrup_200", "bloco8_200", "viz_200"]}
    return {p: all(REGUA[m][0] <= med[m] <= REGUA[m][1] for m in ms if med.get(m) is not None) and
               all(med.get(m) is not None for m in ms) for p, ms in PROP.items()}

def T1T2T3():
    t0 = time.time(); out = {"T1": {}, "T2": {}, "T3": {}}
    VB = mc.paginas_voynich(dialeto="B")
    # referência do T2: VB e seu nulo
    vb_or = p2(VB)["agrup"]; vb_nul = nulo(VB)
    den = vb_or - st.mean(vb_nul)
    out["T2"]["VB"] = {"orig": vb_or, "nulo_media": st.mean(vb_nul), "nulo_p95": pct95(vb_nul), "nulo_dp": st.pstdev(vb_nul), "R": 1.0,
                       "passa": vb_or > pct95(vb_nul)}
    vbg = mc.embaralhar(VB, "global", seed=7)
    g_or = p2(vbg)["agrup"]; g_nul = nulo(vbg)
    out["T2"]["VB embaralhado (s7)"] = {"orig": g_or, "nulo_media": st.mean(g_nul), "nulo_p95": pct95(g_nul),
                                        "R": (g_or - st.mean(g_nul)) / den, "passa": g_or > pct95(g_nul) and (g_or - st.mean(g_nul)) / den >= 0.25}
    print(f"VB R=1 orig={vb_or:.4f} nulo={st.mean(vb_nul):+.4f} p95={pct95(vb_nul):+.4f}  ({time.time()-t0:.0f}s)", flush=True)
    # régua casada do T3
    Nc = int(CMP["subamostras"]["B"]["n"][1])
    rc = {"TTR": CMP["subamostras"]["B"]["TTR"], "hapax": CMP["subamostras"]["B"]["hapax"]}
    out["T3"]["_regua"] = {"N": Nc, "TTR": [rc["TTR"][0], rc["TTR"][2]], "hapax": [rc["hapax"][0], rc["hapax"][2]]}
    for nome in LATIM:
        pars = mc.ler_texto(nome)
        claro = mc.paginas_de_texto(pars, "claro", secao=nome)
        cod = codigo_palavra(claro, VB)
        mcod = mc.medir(cod, nome + " código")
        out["T1"][nome] = {"metricas": {k: mcod[k] for k in ("TTR", "hapax", "zipf", "agrup_200", "bloco8_200", "viz_200", "n")},
                           "v1": avaliar_v1(mcod)}
        res = {}
        for rot, pg in [("código", cod)] + [(f"naibbe s{s}", None) for s in (1, 2, 3)]:
            if pg is None:
                mc.semear(int(rot[-1])); pg = mc.paginas_de_texto(pars, "naibbe", secao=nome)
                if rot.endswith("1"): naibbe1 = pg
                w = palavras(pg)[:Nc]
                out["T3"].setdefault(nome, {})[rot] = {"TTR": len(set(w)) / len(w),
                                                       "hapax": sum(1 for c in Counter(w).values() if c == 1) / len(set(w)), "N": len(w)}
            o = p2(pg)["agrup"]; nl = nulo(pg)
            R = (o - st.mean(nl)) / den
            res[rot] = {"orig": o, "nulo_media": st.mean(nl), "nulo_p95": pct95(nl), "nulo_dp": st.pstdev(nl), "R": R,
                        "passa": (o > pct95(nl)) and R >= 0.25}
            print(f"{nome:10s} {rot:9s} agrup_200={o:+.4f} nulo={st.mean(nl):+.4f} p95={pct95(nl):+.4f} R={R:+.3f} passa={res[rot]['passa']}  ({time.time()-t0:.0f}s)", flush=True)
        out["T2"][nome] = res
        t3 = out["T3"][nome]
        for k in ("TTR", "hapax"):
            t3["mediana_" + k] = st.median(t3[f"naibbe s{s}"][k] for s in (1, 2, 3))
        t3["passa"] = all(out["T3"]["_regua"][k][0] <= t3["mediana_" + k] <= out["T3"]["_regua"][k][1] for k in ("TTR", "hapax"))
        # P1 do código no mesmo tamanho (o código tem ~9 mil fichas; usa todas)
        wc = palavras(cod)
        t3["código (todas as fichas)"] = {"TTR": len(set(wc)) / len(wc), "hapax": sum(1 for c in Counter(wc).values() if c == 1) / len(set(wc)), "N": len(wc)}
    # decisão v2
    falha_t2 = {n: st.median([out["T2"][n][f"naibbe s{s}"]["R"] for s in (1, 2, 3)]) for n in LATIM}
    passa_t2 = {n: sum(out["T2"][n][f"naibbe s{s}"]["passa"] for s in (1, 2, 3)) >= 2 for n in LATIM}
    poder = {"VB passa": out["T2"]["VB"]["passa"],
             "código passa em ≥3/5": sum(out["T2"][n]["código"]["passa"] for n in LATIM) >= 3,
             "VB embaralhado falha": not out["T2"]["VB embaralhado (s7)"]["passa"]}
    n_falha = sum(not passa_t2[n] for n in LATIM)
    n_fav = sum(passa_t2[n] and out["T3"][n]["passa"] for n in LATIM)
    if not all(poder.values()): dec = "INCONCLUSIVO (T2 sem poder)"
    elif n_fav >= 3: dec = "A FAVOR"
    elif n_falha >= 3: dec = "CONTRA"
    else: dec = "INCONCLUSIVO"
    sem_ap = [n for n in LATIM if n != "apicius"]
    out["decisao_v2"] = {"poder_T2": poder, "R_mediano_naibbe": falha_t2, "passa_T2": passa_t2, "n_falha_T2": n_falha,
                         "n_passa_T2_e_T3": n_fav, "decisao": dec,
                         "sem_apicius": {"n_falha_T2": sum(not passa_t2[n] for n in sem_ap), "de": len(sem_ap)},
                         "T1_v1_codigo": {n: out["T1"][n]["v1"] for n in LATIM}}
    salvar("T1T2T3", out); print(json.dumps(out["decisao_v2"], ensure_ascii=False, indent=1)); print(f"{time.time()-t0:.0f}s")

# --------------------------------------------------------------------------------------------------------------
def T4():
    """sanidade completa: embaralhado global fora da régua? e o embaralhamento dentro de blocos de 200 fichas."""
    out = {}
    VB = mc.paginas_voynich(dialeto="B")
    ctl = json.load(open(os.path.join(mc.SAIDA, "controle_resultados.json")))
    g = ctl["medianas"]["VB global mediana"]; pgm = ctl["medianas"]["VB pagina mediana"]
    out["global_fora_da_regua"] = {m: {"valor": g[m], "regua": REGUA[m], "fora": not (REGUA[m][0] <= g[m] <= REGUA[m][1])}
                                   for m in ("agrup_200", "bloco8_200", "viz_200")}
    rp = mc.repaginar(VB, 200)
    for s in (7, 8):
        sh = mc.embaralhar(rp, "pagina", seed=s)          # cada bloco de 200 fichas é uma 'página'
        out[f"dentro_de_blocos_200_s{s}"] = mc._page_metrics(mc.repaginar(sh, 200), random.Random(5))
    out["original"] = mc._page_metrics(rp, random.Random(5))
    out["dentro_da_pagina_natural (Controle)"] = {k: pgm[k] for k in ("agrup", "agrup_200", "viz_200", "bloco8_200")}
    out["original_natural"] = {k: CMP["medidas"]["B"][k] for k in ("agrup", "agrup_200", "viz_200", "bloco8_200")}
    salvar("T4", out); print(json.dumps(limpar(out), ensure_ascii=False, indent=1))

# --------------------------------------------------------------------------------------------------------------
def T5(vars_override=None, nome_saida="T5"):
    t0 = time.time(); out = {"i": {}, "ii": {}}
    NB, DN, (U, P, S, A) = mc._naibbe()
    VB = mc.paginas_voynich(dialeto="B")
    vb_or = p2(VB)["agrup"]; vb_nul = st.mean(nulo(VB)); den = vb_or - vb_nul
    out["den"] = den
    # (i) nulo próprio, semente 1
    METR = ("agrup_200", "viz_200", "razao", "rep", "F1esp")
    def met5(pg):
        b = mc.gerador.battery(pg, "x"); pm = p2(pg)
        return {"agrup_200": pm["agrup"], "viz_200": pm["viz"], "razao": b["razao"], "rep": b["rep"], "F1esp": b["F1esp"]}
    for nome in (LATIM if vars_override is None else []):
        pars = mc.ler_texto(nome); mc.semear(1); pg = mc.paginas_de_texto(pars, "naibbe", secao=nome)
        o = met5(pg); nl = [met5(mc.embaralhar(pg, "global", seed=s)) for s in NULO_SEMENTES]
        z = {m: (o[m] - st.mean(x[m] for x in nl)) / (st.pstdev([x[m] for x in nl]) or float("nan")) for m in METR}
        out["i"][nome] = {"orig": o, "nulo_media": {m: st.mean(x[m] for x in nl) for m in METR},
                          "nulo_dp": {m: st.pstdev([x[m] for x in nl]) for m in METR}, "z": z,
                          "permutavel": all(abs(v) < 2 for v in z.values() if v == v)}
        print(nome, {m: round(v, 2) for m, v in z.items()}, f"({time.time()-t0:.0f}s)", flush=True)
    if vars_override is None:
        out["i"]["n_permutaveis"] = sum(out["i"][n]["permutavel"] for n in LATIM)
        salvar(nome_saida, out)
    # (ii) variantes com deriva
    pesos = NB.CARD_WEIGHTS[True]; tabs = list(pesos); p_aut = [pesos[t] / sum(pesos.values()) for t in tabs]

    class Sorteio:
        """escolhe a tabela de cada glifo; 'dirichlet' (pesos por página) ou 'memoria' (repete a última escolha)."""
        def __init__(self, modo, par, rng):
            self.modo, self.par, self.rng = modo, par, rng; self.mem = {}; self.nova_pagina()
        def nova_pagina(self):
            if self.modo == "dirichlet" and self.par != float("inf"):
                g = [self.rng.gammavariate(self.par * p, 1.0) for p in p_aut]; s = sum(g)
                self.w = [x / s for x in g] if s > 0 else p_aut
            else:
                self.w = p_aut
        def tabela(self):
            return self.rng.choices(tabs, self.w)[0]

    def cifrar(cleaned, sor):
        ngrams = NB.respace_plaintext(cleaned, None); ct = []
        for tok in ngrams:
            if len(tok) == 1:
                if sor.modo == "memoria" and tok in sor.mem and sor.rng.random() < sor.par: t = sor.mem[tok]
                else: t = sor.tabela()
                sor.mem[tok] = t
                ct.append(NB.placeholder_to_glyph[NB.naibbe_tables[t][("unigram", tok)]])
            else:
                reuse = sor.modo == "memoria" and tok in sor.mem and sor.rng.random() < sor.par
                for k in range(NB.MAX_BIGRAM_RETRIES):
                    tp, ts = sor.mem[tok] if (reuse and k == 0) else (sor.tabela(), sor.tabela())
                    cp, cs = NB.naibbe_tables[tp][("prefix", tok[0])], NB.naibbe_tables[ts][("suffix", tok[1])]
                    comb = NB.placeholder_to_glyph[cp] + NB.placeholder_to_glyph[cs]
                    if comb in NB.unigram_glyphs: continue
                    if any(pair != (cp, cs) for pair in NB.bigram_catalog.get(comb, set())): continue
                    break
                sor.mem[tok] = (tp, ts); ct.append(comb)
        return ct, ngrams

    def paginas_variante(pars, secao, sor, ppp=100):
        """mesma paginação de mc.paginas_de_texto (rótulo = 1ª palavra do parágrafo, linhas de 9 fichas)."""
        pages = []; cur = None; n = 0; k = 0; ok = tot = 0
        for ws in pars:
            if cur is None or n >= ppp:
                if cur: pages.append(cur)
                k += 1; cur = {"folio": f"{secao}-{k:05d}", "I": secao, "L": "-", "lines": []}; n = 0; sor.nova_pagina()
            lab, body = ws[:1], ws[1:]
            outs = []
            for part in (lab, body):
                cl = NB.clean_line(" ".join(part))
                if not cl: outs.append([]); continue
                toks, plain = cifrar(cl, sor)
                for c, p_ in zip(toks, plain):                       # decifração com decrypt_naibbe.py
                    tot += 1; ok += DN.decrypt_naibbe_token(c, U, P, S, A, basic=True) == p_
                outs.append(NB.respace_line(" ".join(toks), NB.SPACE_REMOVAL_RATE).split())
            if outs[0]: cur["lines"].append(("L", outs[0], False))
            for j in range(0, len(outs[1]), 9): cur["lines"].append(("P", outs[1][j:j + 9], j == 0))
            n += len(ws)
        if cur: pages.append(cur)
        return pages, ok / max(tot, 1)

    VARS = [("dirichlet", float("inf")), ("dirichlet", 100), ("dirichlet", 10), ("dirichlet", 1),
            ("memoria", 0.5), ("memoria", 0.9)]
    if vars_override: VARS = vars_override
    for modo, par in VARS:
        rot = f"{modo} {par}"; out["ii"][rot] = {}
        for nome in LATIM:
            pars = mc.ler_texto(nome); random.seed(1)
            pg, dec = paginas_variante(pars, nome, Sorteio(modo, par, random.Random(11)))
            m = mc.medir(pg, rot + " " + nome)
            o = m["agrup_200"]; nl = nulo(pg); R = (o - st.mean(nl)) / den
            ws = palavras(pg)
            out["ii"][rot][nome] = {"decifra": dec, "agrup_200": o, "nulo_p95": pct95(nl), "R": R,
                                    "passa_T2": o > pct95(nl) and R >= 0.25,
                                    **{k: m[k] for k in ("TTR", "hapax", "zipf", "viz_200", "bloco8_200", "razao", "rep", "F1esp", "h2", "n")}}
            print(f"{rot:16s} {nome:10s} dec={dec:.3f} agrup_200={o:+.4f} R={R:+.2f} hapax={m['hapax']:.3f} TTR={m['TTR']:.3f} razao={m['razao']:.2f} viz={m['viz_200']:+.3f} ({time.time()-t0:.0f}s)", flush=True)
        out["ii"][rot]["n_passa_T2"] = sum(out["ii"][rot][n]["passa_T2"] for n in LATIM)
        salvar(nome_saida, out)
    print(f"{time.time()-t0:.0f}s")

# --------------------------------------------------------------------------------------------------------------
def T6():
    """validação cruzada do modelo de regras (deriva lexical, parâmetros da Fase 15)."""
    t0 = time.time()
    import gerador
    os.chdir(mc.BASE)                                     # deriva_lexical importa copia3_grade, que lê ZL.txt por caminho relativo
    from deriva_lexical import generate_lex
    from agrupamento2 import folio_key
    V = gerador.real_pages(os.path.join(mc.BASE, "ZL.txt"))
    B = sorted([p for p in V if p["L"] == "B"], key=lambda p: folio_key(p["folio"]))
    metade = {1: {p["folio"] for p in B[0::2]}, 2: {p["folio"] for p in B[1::2]}}
    METR = ["TTR", "hapax", "zipf", "h2", "compr", "razao", "F1esp", "rep"]
    larg = {m: REGUA[m][1] - REGUA[m][0] for m in METR}
    Mtudo = gerador.SlotModel(V, dial=True)
    out = {"metricas": METR, "largura_regua": larg, "rodadas": []}
    for alvo in (1, 2):
        dest = [p for p in V if p["folio"] in metade[alvo]]
        treino = [p for p in V if p["folio"] not in metade[alvo]]
        Mtr = gerador.SlotModel(treino, dial=True)
        real = mc.medir(dest, f"B metade {alvo} real")
        for seed in (13, 14):
            gin = mc.medir(generate_lex(dest, Mtudo, 0.6, 3, 1.4, seed=seed, pool_size=6000), "dentro")
            gout = mc.medir(generate_lex(dest, Mtr, 0.6, 3, 1.4, seed=seed, pool_size=6000), "fora")
            Din = st.mean(abs(gin[m] - real[m]) / larg[m] for m in METR)
            Dout = st.mean(abs(gout[m] - real[m]) / larg[m] for m in METR)
            out["rodadas"].append({"alvo": alvo, "seed": seed, "real": {m: real[m] for m in METR + ["agrup_200", "viz_200"]},
                                   "dentro": {m: gin[m] for m in METR + ["agrup_200", "viz_200"]},
                                   "fora": {m: gout[m] for m in METR + ["agrup_200", "viz_200"]}, "D_dentro": Din, "D_fora": Dout})
            print(f"metade {alvo} s{seed}: D_dentro={Din:.3f} D_fora={Dout:.3f} ({time.time()-t0:.0f}s)", flush=True)
    out["D_dentro"] = st.mean(r["D_dentro"] for r in out["rodadas"]); out["D_fora"] = st.mean(r["D_fora"] for r in out["rodadas"])
    cif = json.load(open(os.path.join(mc.SAIDA, "cifrador_resultados.json")))
    VBm = CMP["medidas"]["B"]
    out["D_naibbe_vs_VB"] = {n: st.mean(abs(cif[n]["naibbe_mediana"][m] - VBm[m]) / larg[m] for m in METR) for n in LATIM}
    out["inflacao"] = out["D_fora"] >= 2 * out["D_dentro"]
    salvar("T6", out); print({k: out[k] for k in ("D_dentro", "D_fora", "inflacao", "D_naibbe_vs_VB")})

# --------------------------------------------------------------------------------------------------------------
def T7():
    out = {}
    for nome in ("isidoro17", "apicius"):
        pars = mc.ler_texto(nome)
        for modo in ("claro", "naibbe"):
            mc.semear(1)
            pg = mc.paginas_de_texto(pars, modo, secao=nome, palavras_por_pagina=60)
            m = mc.medir(pg, f"{nome} {modo} entradas")
            ag, b8 = m["agrup"], m["bloco8"]
            out[f"{nome} {modo}"] = {"paginas": len(pg), "fichas_por_pagina": m["n"] / len(pg), "agrup": ag, "bloco8": b8,
                                     "razao_b8_agrup": b8 / ag if ag > 0 else None, "viz": m["viz"], "agrup_200": m["agrup_200"],
                                     "local_como_VB": (ag >= 0.075 and ag > 0 and b8 / ag <= 0.5)}
            print(nome, modo, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in out[f"{nome} {modo}"].items()}, flush=True)
    VB = CMP["medidas"]["B"]; BxH = CMP["medidas"]["BxH"]
    out["VB natural"] = {"agrup": VB["agrup"], "bloco8": VB["bloco8"], "razao_b8_agrup": VB["bloco8"] / VB["agrup"],
                         "fichas_por_pagina": VB["n"] / 83}
    out["BxH natural"] = {"agrup": BxH["agrup"], "bloco8": BxH["bloco8"], "razao_b8_agrup": BxH["bloco8"] / BxH["agrup"]}
    salvar("T7", out); print(json.dumps(limpar(out), ensure_ascii=False, indent=1))

def T5b():
    """2ª rodada do Cético: α entre 3 e 5 – P2 no nível de VB nas três métricas ao mesmo tempo?"""
    T5(vars_override=[("dirichlet", 5), ("dirichlet", 3)], nome_saida="T5b")

def T3b():
    """2ª rodada do Cético: régua de TTR/hapax feita de TODAS as janelas contíguas de VB com 10.974 fichas (passo 250),
    na ordem do manuscrito, e as mesmas janelas no modelo de regras e na Naibbe."""
    N = 10974
    def janelas(ws, passo=250):
        out = []
        for i in range(0, len(ws) - N + 1, passo):
            w = ws[i:i + N]; c = Counter(w)
            out.append((len(c) / N, sum(1 for v in c.values() if v == 1) / len(c)))
        return out
    res = {}
    VB = mc.paginas_voynich(dialeto="B")
    jv = janelas(palavras(VB))
    res["VB"] = {"n_janelas": len(jv), "TTR": [min(x[0] for x in jv), st.median(x[0] for x in jv), max(x[0] for x in jv)],
                 "hapax": [min(x[1] for x in jv), st.median(x[1] for x in jv), max(x[1] for x in jv)]}
    cwd = os.getcwd(); os.chdir(mc.BASE)
    for s in (13, 14, 15):
        g = mc.filtrar(mc.gerar_regras("deriva", seed=s), dialeto="B"); j = janelas(palavras(g))
        res[f"regras-deriva B s{s}"] = {"TTR": [min(x[0] for x in j), st.median(x[0] for x in j), max(x[0] for x in j)],
                                        "hapax": [min(x[1] for x in j), st.median(x[1] for x in j), max(x[1] for x in j)]}
    os.chdir(cwd)
    for nome in LATIM:
        pars = mc.ler_texto(nome); mc.semear(1); j = janelas(palavras(mc.paginas_de_texto(pars, "naibbe", secao=nome)))
        res[f"naibbe {nome} s1"] = {"TTR": [min(x[0] for x in j), st.median(x[0] for x in j), max(x[0] for x in j)],
                                    "hapax": [min(x[1] for x in j), st.median(x[1] for x in j), max(x[1] for x in j)]}
    for k, v in res.items():
        v["TTR_dentro_VB"] = res["VB"]["TTR"][0] <= v["TTR"][1] <= res["VB"]["TTR"][2]
        v["hapax_dentro_VB"] = res["VB"]["hapax"][0] <= v["hapax"][1] <= res["VB"]["hapax"][2]
        print(k, {a: ([round(x, 3) for x in b] if isinstance(b, list) else b) for a, b in v.items()}, flush=True)
    salvar("T3b", res)

def T7b():
    """correção do T7: o índice de blocos de 8 depende do número de blocos por grupo (seção×dialeto). Em VB os grupos
    têm 19–32 páginas naturais (3–4 blocos); nos textos latinos, um grupo só com 82–113 páginas (10–14 blocos).
    Aqui os textos são partidos em grupos consecutivos com o tamanho dos grupos de B (32, 19, 23 páginas, em ciclo)."""
    out = {}
    tam = [32, 19, 23]
    def regrupar(pg):
        res = []; i = 0; g = 0
        while i < len(pg):
            n = tam[g % 3]; bloco = pg[i:i + n]
            if len(bloco) >= 8: res += [{**p, "I": f"g{g}"} for p in bloco]
            i += n; g += 1
        return res
    for nome in ("isidoro17", "apicius", "plinio16", "hyginus", "cesar"):
        pars = mc.ler_texto(nome)
        for modo in ("claro", "naibbe"):
            mc.semear(1)
            pg = regrupar(mc.paginas_de_texto(pars, modo, secao=nome, palavras_por_pagina=60))
            pm = mc._page_metrics(pg, random.Random(5))
            ag, b8 = pm["agrup"], pm["bloco8"]
            out[f"{nome} {modo}"] = {"paginas": len(pg), "grupos": len({p['I'] for p in pg}), "agrup": ag, "bloco8": b8,
                                     "razao_b8_agrup": b8 / ag if ag > 0 else None,
                                     "local_como_VB": (ag >= 0.075 and b8 / ag <= 0.5) if ag > 0 else False}
            print(nome, modo, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in out[f"{nome} {modo}"].items()}, flush=True)
    # o mesmo para VB (grupos naturais) e para o modelo de regras B (mesmo leiaute)
    VB = mc.paginas_voynich(dialeto="B")
    pm = mc._page_metrics(VB, random.Random(5)); out["VB natural"] = {"agrup": pm["agrup"], "bloco8": pm["bloco8"], "razao_b8_agrup": pm["bloco8"] / pm["agrup"]}
    salvar("T7b", out); print(json.dumps(limpar(out), ensure_ascii=False, indent=1))

if __name__ == "__main__":
    for t in sys.argv[1:]:
        globals()[t]()
