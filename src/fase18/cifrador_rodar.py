"""Fase 18 - CIFRADOR: cifra textos reais com a Naibbe original (naibbe_v2 + tabelas do autor, sem recalibrar)
e mede com metricas_comuns. Rodar com:
    cd src/fase18 && PYTHONHASHSEED=0 python3 cifrador_rodar.py
"""
import json, math, os, statistics as st, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import metricas_comuns as mc

AQUI = os.path.dirname(os.path.abspath(__file__))
SEMENTES = [1, 2, 3]
EXTREMOS = ["TTR", "zipf", "agrup_200", "bloco8_200", "viz_200"]


def eh_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def eh_nan(v):
    return isinstance(v, float) and v != v


def mediana(dicts):
    """mediana de cada métrica numérica entre as sementes (ignora NaN; NaN se todas forem NaN)."""
    out = {}
    chaves = [k for k in dicts[0] if all(k in d for d in dicts)]
    for k in chaves:
        vals = [d[k] for d in dicts]
        if not all(eh_num(v) for v in vals):
            continue
        ok = [float(v) for v in vals if not eh_nan(v)]
        out[k] = st.median(ok) if ok else float("nan")
    return out


def limpar(o):
    """NaN/inf -> None para JSON válido."""
    if isinstance(o, dict):
        return {str(k): limpar(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [limpar(v) for v in o]
    if isinstance(o, float) and (o != o or math.isinf(o)):
        return None
    return o


def fmt(v, f="{:.4f}"):
    return "–" if v is None or eh_nan(v) else f.format(v)


def main():
    t0 = time.time()
    res = {}
    for nome, (genero, lingua, arqs) in mc.TEXTOS.items():
        print(f"\n=== {nome} ({genero}, {lingua}; {len(arqs)} arquivo(s)) ===", flush=True)
        pars = mc.ler_texto(nome)
        npal = sum(len(p) for p in pars)
        print(f"  parágrafos={len(pars)} palavras={npal}", flush=True)
        ent = {"genero": genero, "lingua": lingua, "n_paragrafos": len(pars), "n_palavras_claro": npal}

        ent["claro"] = mc.medir(mc.paginas_de_texto(pars, "claro", secao=nome), nome + " claro")
        print(f"  claro ok ({time.time() - t0:.0f}s)", flush=True)

        ent["naibbe"] = {}
        for s in SEMENTES:
            mc.semear(s)
            pg = mc.paginas_de_texto(pars, "naibbe", secao=nome)
            ent["naibbe"][str(s)] = mc.medir(pg, f"{nome} naibbe s{s}")
            print(f"  naibbe s{s} ok: páginas={len(pg)} n={ent['naibbe'][str(s)].get('n'):.0f} ({time.time() - t0:.0f}s)", flush=True)
        ent["naibbe_mediana"] = mediana([ent["naibbe"][str(s)] for s in SEMENTES])

        mc.semear(1)
        ent["decifra"] = mc.decifrar_check(pars)
        mc.semear(1)
        ent["estab"] = mc.estabilidade_naibbe(pars)
        print(f"  decifra={ent['decifra']:.4f} estab={ent['estab']} ({time.time() - t0:.0f}s)", flush=True)
        res[nome] = ent

    with open(os.path.join(mc.SAIDA, "cifrador_resultados.json"), "w", encoding="utf-8") as f:
        json.dump(limpar(res), f, ensure_ascii=False, indent=1)

    # ---------------- tabelas ----------------
    nomes = list(res)
    md = ["# Fase 18 – Cifrador: Naibbe original sobre textos reais", "",
          "Gerado por cifrador_rodar.py (PYTHONHASHSEED=0). Sementes da Naibbe: 1, 2, 3. "
          "Decifra e estabilidade com mc.semear(1) antes de cada chamada.", "",
          "## (i) Naibbe – mediana entre as sementes 1–3", "",
          mc.tabela_md({n: res[n]["naibbe_mediana"] for n in nomes}), "",
          "## (ii) Textos claros (sem cifra)", "",
          mc.tabela_md({n: res[n]["claro"] for n in nomes}), "",
          "## (iii) Decifração e estabilidade (semente 1)", "",
          "| Texto | língua | decifra | estab_frac | estab_grafias | estab_n |", "|---|---|---|---|---|---|"]
    for n in nomes:
        e = res[n]["estab"]
        md.append(f"| {n} | {res[n]['lingua']} | {fmt(res[n]['decifra'], '{:.1%}')} | {fmt(e['estab_frac'], '{:.3f}')} | "
                  f"{fmt(e['estab_grafias'], '{:.1f}')} | {e['estab_n']} |")
    md += ["", "## (iv) Mínimo – máximo entre as 3 sementes", "",
           "| Texto | " + " | ".join(EXTREMOS) + " |", "|---|" + "---|" * len(EXTREMOS)]
    for n in nomes:
        cells = []
        for k in EXTREMOS:
            vals = [res[n]["naibbe"][str(s)].get(k) for s in SEMENTES]
            vals = [v for v in vals if eh_num(v) and not eh_nan(v)]
            f = "{:.3f}" if k == "TTR" else ("{:.2f}" if k == "zipf" else "{:+.3f}")
            cells.append(f"{f.format(min(vals))} – {f.format(max(vals))}" if vals else "–")
        md.append(f"| {n} | " + " | ".join(cells) + " |")
    md.append("")
    with open(os.path.join(mc.SAIDA, "cifrador_tabela.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("\n".join(md))
    print(f"\nTempo total: {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
