"""Fase 18 – COMPARADOR: mede o manuscrito (ZL3b) com as métricas comuns, por dialeto, seção, cruzamentos e mãos,
e constrói a régua de variação interna de B (e de A, informativa) conforme criterios.md.
Rodar: cd src/fase18 && PYTHONHASHSEED=0 python3 comparador_rodar.py
"""
import json, math, os, sys, time, traceback, warnings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import metricas_comuns as mc

AQUI = os.path.dirname(os.path.abspath(__file__))
REGUA_METRICAS = ["TTR", "hapax", "zipf", "agrup_200", "bloco8_200", "viz_200", "h2", "compr", "razao", "F1esp", "rep"]
MIN_FICHAS = 3000
SECOES = {"H": "herbal", "P": "farmacêutica", "B": "biológica", "S": "receitas/estrelas", "Z": "zodíaco",
          "A": "astronômica", "C": "cosmológica", "T": "só texto"}

avisos = []      # (contexto, mensagem) – avisos e erros, registrados com exatidão
nans = {}        # nome -> métricas NaN
guardas = {}     # nome -> lista de funções cuja exceção virou NaN (só na 2ª tentativa)


def nan(v):
    return isinstance(v, float) and v != v


# ---- Guardas (não alteram nenhum arquivo nem nenhuma métrica calculada) ----
# Em alguns subconjuntos mc.medir aborta inteiro com StatisticsError numa sub-rotina que não tem dados
# (rotulos_especificidade.analyze sem nenhum rótulo ecoado; agrupamento.clustering sem palavra com 10+ ocorrências).
# Política: 1ª tentativa SEM guarda; só se ela abortar, repete com GUARDA ligada, em que essas duas funções, ao
# levantarem StatisticsError, devolvem NaN para os valores que elas mesmas produzem. As demais métricas saem do código
# original sem mudança (analyze é a última etapa de battery e tem rng próprio; clustering não usa rng).
import statistics as _st
import rotulos_especificidade as _RE   # mesmo objeto de módulo que gerador.battery importa
_GUARDA = {"on": False, "disparos": []}
_orig_analyze, _orig_clustering = _RE.analyze, mc.clustering


def _analyze_guard(*a, **k):
    try:
        return _orig_analyze(*a, **k)
    except _st.StatisticsError as e:
        if not _GUARDA["on"]:
            raise
        _GUARDA["disparos"].append(f"rotulos_especificidade.analyze: {e} -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN")
        x = float("nan")
        return {"nlab": x, "echo": x, "conc": x, "conc_null": x, "p": x, "freq": x, "freq_null": x}


def _clustering_guard(pages):
    try:
        return _orig_clustering(pages)
    except _st.StatisticsError as e:
        if not _GUARDA["on"]:
            raise
        _GUARDA["disparos"].append(f"agrupamento.clustering: {e} -> índice de agrupamento (agrup/bloco8, natural ou _200) = NaN")
        return float("nan"), 0


_RE.analyze = _analyze_guard
mc.clustering = _clustering_guard


_RW = {}   # ResourceWarning repetido (arquivo não fechado no parser) – consolidado numa linha só no fim


def _registrar_warnings(ctx, ws):
    vistos = {}
    for x in ws:
        m = f"AVISO {x.category.__name__}: {x.message} ({os.path.basename(x.filename)}:{x.lineno})"
        if issubclass(x.category, ResourceWarning):
            _RW.setdefault(m, set()).add(ctx); continue
        vistos[m] = vistos.get(m, 0) + 1
    for m, c in vistos.items():
        avisos.append((ctx, m + (f" [×{c}]" if c > 1 else "")))


def medir(nome, **filtro):
    t0 = time.time()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        pags = mc.paginas_voynich(**filtro)
        nP = sum(len(l) for p in pags for t, l, _ in p["lines"] if t == "P")
        r = None
        try:
            r = mc.medir(pags, nome)
        except Exception as e:
            msg = "".join(traceback.format_exception_only(type(e), e)).strip()
            tb = traceback.extract_tb(e.__traceback__)[-2:]
            onde = " <- ".join(f"{os.path.basename(f.filename)}:{f.lineno} {f.name}" for f in reversed(tb))
            avisos.append((nome, f"ERRO na 1ª tentativa (sem guarda) em mc.medir: {msg} [{onde}]"))
            print(f"[ERRO] {nome}: {msg} [{onde}] -> repetindo com guarda", flush=True)
            _GUARDA["on"] = True; _GUARDA["disparos"] = []
            try:
                r = mc.medir(pags, nome)
                guardas[nome] = sorted(set(_GUARDA["disparos"]))
                for g in guardas[nome]:
                    avisos.append((nome, "GUARDA disparou: " + g))
            except Exception as e2:
                msg2 = "".join(traceback.format_exception_only(type(e2), e2)).strip()
                tb2 = traceback.extract_tb(e2.__traceback__)[-1]
                avisos.append((nome, f"ERRO também com guarda: {msg2} [{os.path.basename(tb2.filename)}:{tb2.lineno}] "
                                     f"– subconjunto não medido ({len(pags)} páginas, {nP} fichas de texto corrido 'P')"))
                print(f"[ERRO] {nome}: com guarda também falhou: {msg2}", flush=True)
                r = {"n": float(nP), "nao_medido": 1.0}
            finally:
                _GUARDA["on"] = False
        _registrar_warnings(nome, w)
    r["paginas"] = float(len(pags))
    if not r.get("nao_medido"):
        nn = sorted(k for k, v in r.items() if nan(v))
        if nn:
            nans[nome] = nn
        print(f"{nome:<14} páginas={len(pags):>3} n={r['n']:>7.0f}  {time.time() - t0:5.1f}s  NaN: {nn}", flush=True)
    return r


def limpar(o):
    """JSON estrito: NaN/inf -> null, tuplas -> listas."""
    if isinstance(o, dict):
        return {k: limpar(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [limpar(v) for v in o]
    if isinstance(o, float) and (o != o or math.isinf(o)):
        return None
    return o


def regua(sub, medidas, nomes_secoes):
    """[mín, máx] da união dos mínimos e máximos das subamostras e dos valores das seções com 3.000+ fichas."""
    out, fontes = {}, {}
    usadas = [s for s in nomes_secoes if medidas.get(s) and medidas[s]["n"] >= MIN_FICHAS]
    for m in REGUA_METRICAS:
        vals, src = [], []
        lo, _, hi = sub[m]
        for v, s in ((lo, "sub_min"), (hi, "sub_max")):
            if not nan(v):
                vals.append(v); src.append(s)
            else:
                avisos.append(("régua", f"subamostra {s} de {m} é NaN – excluída da união"))
        for s in usadas:
            v = medidas[s].get(m)
            if v is None or nan(v):
                avisos.append(("régua", f"{s}: {m} é NaN – excluído da união"))
                continue
            vals.append(v); src.append(s)
        out[m] = [min(vals), max(vals)] if vals else [float("nan"), float("nan")]
        fontes[m] = {"min_de": src[vals.index(min(vals))] if vals else None,
                     "max_de": src[vals.index(max(vals))] if vals else None}
    return out, fontes, usadas


def main():
    t0 = time.time()
    medidas = {}
    # 1) inteiro, dialetos, seções
    medidas["inteiro"] = medir("inteiro")
    for d in ("A", "B"):
        medidas[d] = medir(d, dialeto=d)
    for s in SECOES:
        medidas[f"sec_{s}"] = medir(f"sec_{s}", secao=s)
    # 2) cruzamentos dialeto × seção
    for d, s in (("B", "H"), ("B", "B"), ("B", "S"), ("A", "H"), ("A", "P")):
        medidas[f"{d}x{s}"] = medir(f"{d}x{s}", dialeto=d, secao=s)
    # 3) mãos
    for h in ("1", "2", "3"):
        medidas[f"mao_{h}"] = medir(f"mao_{h}", mao=h)

    # 4) variação interna
    subs = {}
    for d in ("A", "B"):
        t1 = time.time()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            subs[d] = mc.subamostras(mc.paginas_voynich(dialeto=d), d, reps=10)
            _registrar_warnings(f"subamostras {d}", w)
        nn = sorted(k for k, v in subs[d].items() if any(nan(x) for x in v))
        print(f"subamostras {d}: {time.time() - t1:5.1f}s  métricas com NaN: {nn}", flush=True)
        if nn:
            nans[f"subamostras_{d}"] = nn

    # 5) réguas
    for m, ctxs in _RW.items():
        avisos.append(("geral", f"{m} – emitido em todas as {len(ctxs)} chamadas a mc.paginas_voynich "
                                f"(arquivo aberto sem fechar no parser; não afeta os valores)"))
    regua_B, fontes_B, usadas_B = regua(subs["B"], medidas, ["BxH", "BxB", "BxS"])
    regua_A, fontes_A, usadas_A = regua(subs["A"], medidas, ["AxH", "AxP"])
    excl_B = [s for s in ["BxH", "BxB", "BxS"] if s not in usadas_B]
    excl_A = [s for s in ["AxH", "AxP"] if s not in usadas_A]

    res = {"medidas": medidas, "subamostras": subs, "regua_B": regua_B, "regua_A": regua_A,
           "regua_meta": {"B": {"secoes_usadas": usadas_B, "secoes_excluidas_<3000": excl_B, "fontes": fontes_B},
                          "A": {"secoes_usadas": usadas_A, "secoes_excluidas_<3000": excl_A, "fontes": fontes_A},
                          "min_fichas": MIN_FICHAS, "reps": 10, "frac": 0.5},
           "nan": nans, "guardas": guardas, "avisos": avisos,
           "nota": ("NaN gravado como null (JSON estrito). 'paginas' = número de páginas do subconjunto. "
                    "'guardas': subconjuntos em que mc.medir abortou na 1ª tentativa e foi repetido com guarda "
                    "(a função listada devolveu NaN em vez de abortar); 'nao_medido' = abortou mesmo com guarda.")}
    with open(os.path.join(mc.SAIDA, "comparador_resultados.json"), "w", encoding="utf-8") as f:
        json.dump(limpar(res), f, ensure_ascii=False, indent=1)

    # 6) tabelas
    nome_col = {"inteiro": "Inteiro", "A": "Dialeto A", "B": "Dialeto B"}
    nome_col.update({f"sec_{s}": f"{s} ({SECOES[s]})" for s in SECOES})
    t_i = {nome_col[k]: medidas[k] for k in ["inteiro", "A", "B"] + [f"sec_{s}" for s in SECOES] if medidas.get(k)}
    cruz = {"B×H": "BxH", "B×B": "BxB", "B×S": "BxS", "A×H": "AxH", "A×P": "AxP", "Mão 1": "mao_1", "Mão 2": "mao_2", "Mão 3": "mao_3"}
    t_ii = {k: medidas[v] for k, v in cruz.items() if medidas.get(v)}

    def fmt(v):
        return "–" if v is None or nan(v) else f"{v:.4f}"

    def linhas_regua(rg, sub, fontes):
        out = ["| Métrica | mínimo | máximo | (subamostras: mín / mediana / máx) | mín vem de | máx vem de |",
               "|---|---|---|---|---|---|"]
        for m in REGUA_METRICAS:
            lo, me, hi = sub[m]
            out.append(f"| {m} | {fmt(rg[m][0])} | {fmt(rg[m][1])} | {fmt(lo)} / {fmt(me)} / {fmt(hi)} | "
                       f"{fontes[m]['min_de']} | {fontes[m]['max_de']} |")
        return "\n".join(out)

    pag = lambda d: " | ".join(f"{k}: {v['paginas']:.0f} pág." for k, v in d.items())
    md = ["# Fase 18 – Comparador: o manuscrito (ZL3b) medido com as métricas comuns", "",
          "Gerado por comparador_rodar.py (PYTHONHASHSEED=0). '–' = NaN (subconjunto pequeno demais para a métrica).", "",
          "## (i) Inteiro, dialetos e seções", "", mc.tabela_md(t_i), "", "Páginas: " + pag(t_i), "",
          "## (ii) Cruzamentos dialeto × seção e mãos", "", mc.tabela_md(t_ii), "", "Páginas: " + pag(t_ii), "",
          "## (iii) Réguas de variação interna (criterios.md)", "",
          f"União de: mínimos e máximos de 10 subamostras de metade das páginas (mc.subamostras, frac=0,5) + "
          f"seções com {MIN_FICHAS}+ fichas. Sem alargamento.", "",
          f"### Régua de B (decide) – seções usadas: {', '.join(usadas_B) or 'nenhuma'}"
          + (f"; excluídas por terem < {MIN_FICHAS} fichas: {', '.join(excl_B)}" if excl_B else ""), "",
          linhas_regua(regua_B, subs["B"], fontes_B), "",
          f"### Régua de A (só informativa) – seções usadas: {', '.join(usadas_A) or 'nenhuma'}"
          + (f"; excluídas por terem < {MIN_FICHAS} fichas: {', '.join(excl_A)}" if excl_A else ""), "",
          linhas_regua(regua_A, subs["A"], fontes_A), ""]
    if guardas:
        md += ["## Subconjuntos medidos com guarda", "",
               "mc.medir abortou (StatisticsError) na 1ª tentativa; repetido com guarda em que só a função indicada "
               "devolve NaN em vez de abortar. As demais métricas saem do código original sem mudança.", ""]
        md += [f"- {k}: {'; '.join(v)}" for k, v in guardas.items()] + [""]
    nm = [k for k, v in medidas.items() if v and v.get("nao_medido")]
    if nm:
        md += ["## Subconjuntos não medidos (abortaram mesmo com guarda)", ""]
        md += [f"- {k}: {medidas[k]['paginas']:.0f} páginas, {medidas[k]['n']:.0f} fichas de texto corrido" for k in nm] + [""]
    if nans:
        md += ["## Métricas NaN por subconjunto", ""] + [f"- {k}: {', '.join(v)}" for k, v in nans.items()] + [""]
    if avisos:
        md += ["## Avisos e erros", ""] + [f"- {c}: {m}" for c, m in avisos] + [""]
    with open(os.path.join(mc.SAIDA, "comparador_tabela.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"\nTotal {time.time() - t0:.1f}s; avisos/erros: {len(avisos)}")
    for c, m in avisos:
        print(f"  {c}: {m}")


if __name__ == "__main__":
    main()
