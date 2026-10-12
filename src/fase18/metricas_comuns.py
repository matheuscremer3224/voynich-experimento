"""Fase 18 – CÓDIGO DE MÉTRICAS ÚNICO, compartilhado por todos os agentes. Não reimplemente nada: importe daqui.

Uso típico:
    import sys; sys.path.insert(0, "src/fase18")   # ou o caminho até esta pasta
    import metricas_comuns as mc
    pags = mc.paginas_voynich(dialeto="B")                    # manuscrito
    r = mc.medir(pags, "Voynich B")                           # dicionário de métricas
    pars = mc.ler_texto("apicius")                            # parágrafos (listas de palavras) de um texto
    mc.semear(1); pn = mc.paginas_de_texto(pars, "naibbe", secao="apicius")   # cifra com a Naibbe original
    print(mc.tabela_md({"Voynich B": r, ...}))

Estrutura de 'página': {"folio": str, "I": seção, "L": dialeto, "lines": [(tipo, [palavras], inicio_de_paragrafo)]},
tipo "P" = texto corrido, "L" = rótulo. Todas as métricas são calculadas só sobre linhas "P" (os rótulos entram apenas
nas métricas de eco).

DEFINIÇÕES (as mesmas das Fases 1–17):
  h2           entropia condicional (bits) de letra dado a letra anterior, espaço contando como símbolo
  compr, dp    média e desvio do comprimento das palavras em unidades glíficas (ch, sh, cth, ckh, cph, cfh = 1)
  TTR          tipos / ocorrências; hapax = fração dos tipos com 1 ocorrência
  zipf         inclinação de log(freq) × log(posto) nas 1.000 formas mais frequentes
  razao        MI(última letra de w_n ; 1ª unidade de w_n+1) ÷ MI(1ª unidade ; última letra da mesma palavra, 3+ unid.),
               ambas descontado o valor com pares embaralhados
  F1esp        F1 ao recolocar os espaços a partir de ±2 unidades de contexto (treino nas linhas pares, teste nas ímpares)
  rep, quase   palavras vizinhas idênticas; vizinhas que diferem em uma unidade
  agrup        índice de agrupamento por página: média, nas palavras com 10+ ocorrências na seção, de
               (páginas esperadas ao acaso − páginas observadas) / esperadas
  bloco8       o mesmo índice com blocos de 8 páginas vizinhas
  chave_frac   fração das palavras com 5+ ocorrências na seção que têm metade ou mais das ocorrências numa só página
  viz          cosseno médio entre páginas vizinhas menos o cosseno entre páginas a 5+ de distância
  *_200        as quatro métricas de página acima, recalculadas depois de repaginar tudo em páginas de 200 fichas
               (corrige diferenças de tamanho de página entre corpora)
  eco, eco_acaso, conc_rot, conc_nulo   rótulos (3+ unidades): reaparecem no texto da própria página / de outra;
               concentração (fração das ocorrências que cai na página) dos ecoados × de fichas quaisquer da página
"""
import io, math, os, random, re, statistics as st, sys
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # a pasta src/
sys.path.insert(0, BASE)
import config
SAIDA = config.SAIDA_FASE18                                          # results/fase-18 (entradas e saídas da fase)
REPO = config.NAIBBE_REPO
LL = config.LATIN_LIBRARY
EP = config.EUROPARL
sys.path.insert(0, BASE)
import gerador
from ivtff import units
from agrupamento import clustering
from agrupamento2 import keywords, adjacency, folio_key

# ---------------- Naibbe original (sem alterações) ----------------
_NB = None
def _naibbe():
    global _NB
    if _NB is None:
        cwd = os.getcwd(); os.chdir(REPO); sys.path.insert(0, REPO)
        import naibbe_v2 as NB, decrypt_naibbe as DN, pandas as pd
        df = pd.read_csv("references/naibbe_tables.csv")
        _NB = (NB, DN, DN.build_reverse_mappings(df))
        os.chdir(cwd)
    return _NB

def semear(seed):
    """fixa os sorteios da Naibbe (baralho e re-espaçamento usam o módulo random global)."""
    random.seed(seed)

def nb_encrypt(text, respaced=True):
    """cifra um trecho com naibbe_v2 (tabelas e parâmetros do autor). Devolve (fichas cifradas, fichas claras re-espaçadas)."""
    NB, DN, _ = _naibbe()
    buf = io.StringIO(); cleaned = NB.clean_line(text)
    if not cleaned: return [], []
    toks = NB.encrypt_naibbe(cleaned, NB.naibbe_tables, NB.placeholder_to_glyph, use_78=NB.USE_78_CARD_DECK, pre_plaintext_file=buf)
    line = " ".join(toks)
    if respaced: line = NB.respace_line(line, NB.SPACE_REMOVAL_RATE)
    return line.split(), buf.getvalue().split()

def decifrar_check(paragrafos, n=300):
    """fração das fichas que decrypt_naibbe.py (modo básico) devolve exatamente como o texto claro re-espaçado."""
    NB, DN, (U, P, S, A) = _naibbe(); ok = tot = 0
    for ws in paragrafos[:n]:
        toks, plain = nb_encrypt(" ".join(ws), respaced=False)
        for c, p in zip(toks, plain):
            tot += 1; ok += DN.decrypt_naibbe_token(c, U, P, S, A, basic=True) == p
    return ok / max(tot, 1)

def estabilidade_naibbe(paragrafos, n=1500):
    """palavras do texto claro com 10+ ocorrências: fração das ocorrências cifradas pela grafia mais comum, e
    mediana do número de grafias diferentes (cada palavra cifrada isoladamente)."""
    rend = defaultdict(Counter)
    for ws in paragrafos[:n]:
        for w in ws:
            t, _ = nb_encrypt(w, respaced=False); rend[w.lower()][" ".join(t)] += 1
    vals = [c.most_common(1)[0][1] / sum(c.values()) for c in rend.values() if sum(c.values()) >= 10]
    nf = [len(c) for c in rend.values() if sum(c.values()) >= 10]
    return {"estab_frac": st.mean(vals) if vals else float("nan"), "estab_grafias": st.median(nf) if nf else float("nan"), "estab_n": len(vals)}

# ---------------- textos ----------------
def _norm(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return t.replace("j", "i").replace("v", "u")

TEXTOS = {   # nome -> (gênero, língua, arquivos)
    "isidoro17": ("herbário (plantas e agricultura)", "latim", [LL + "isidore/17.txt"]),
    "plinio16": ("herbário (árvores)", "latim", [REPO + "/input/examples/nathist_book16.txt"]),
    "apicius": ("receituário (culinária)", "latim", [LL + f"apicius/apicius{i}.txt" for i in range(1, 6)]),
    "hyginus": ("astronomia/astrologia", "latim", [LL + f"hyginus/hyginus{i}.txt" for i in range(1, 5)]),
    "cesar": ("prosa narrativa comum", "latim", [LL + "caesar/gall1.txt", LL + "caesar/gall2.txt"]),
    "dante": ("poesia (Divina Commedia)", "italiano", [REPO + "/input/examples/divina_commedia.txt"]),
    "europarl_it": ("prosa moderna", "italiano", sorted(__import__("glob").glob(EP + "italian/*"))[:40]),
}
JUNK = ("the latin library", "the classics page", "christian latin")

def ler_texto(nome, max_palavras=9000):
    """parágrafos (listas de palavras normalizadas a–z) de um texto da lista TEXTOS, até max_palavras."""
    pars = []; n = 0
    for f in TEXTOS[nome][2]:
        raw = open(f, "rb").read()
        try: s = raw.decode("utf-8")
        except UnicodeDecodeError: s = raw.decode("latin-1")
        blocks = re.split(r"\n\s*\n|\[\s*\d+\s*\]", s)
        for b in blocks:
            if any(j in b.lower() for j in JUNK): continue
            ws = re.findall(r"[a-z]+", _norm(b))
            ws = [w for w in ws if not re.fullmatch(r"[ivxlcdm]+", w) or len(w) > 4]
            if len(ws) >= 8:
                pars.append(ws); n += len(ws)
                if n >= max_palavras: return pars
    return pars

def paginas_de_texto(paragrafos, modo, secao="X", palavras_por_pagina=100, rotulos=True):
    """agrupa parágrafos em páginas de ~N palavras do texto claro. modo='claro' ou 'naibbe'. Se rotulos=True, a 1ª palavra
    de cada parágrafo vira rótulo (linha 'L') e sai do texto. Texto em linhas de 9 fichas."""
    pages = []; cur = None; n = 0; k = 0
    for ws in paragrafos:
        if cur is None or n >= palavras_por_pagina:
            if cur: pages.append(cur)
            k += 1; cur = {"folio": f"{secao}-{k:05d}", "I": secao, "L": "-", "lines": []}; n = 0
        lab, body = (ws[:1], ws[1:]) if rotulos else ([], ws)
        if modo == "naibbe":
            lab = nb_encrypt(" ".join(lab))[0] if lab else []; body = nb_encrypt(" ".join(body))[0]
        if lab: cur["lines"].append(("L", lab, False))
        for j in range(0, len(body), 9): cur["lines"].append(("P", body[j:j + 9], j == 0))
        n += len(ws)
    if cur: pages.append(cur)
    return pages

# ---------------- manuscrito, regras, embaralhado ----------------
def paginas_voynich(dialeto=None, secao=None, mao=None):
    """páginas do ZL3b (vírgula = espaço). dialeto 'A'/'B', seção I ('H','P','B','S','Z','A','C','T'), mão '1'..'5'."""
    import json
    from ivtff import parse
    L, pv = parse(os.path.join(BASE, "ZL.txt"))
    pages = gerador.real_pages(os.path.join(BASE, "ZL.txt"))
    out = []
    for pg in pages:
        v = pv[pg["folio"]]
        if dialeto and v.get("L") != dialeto: continue
        if secao and v.get("I") != secao: continue
        if mao and v.get("H") != mao: continue
        out.append(pg)
    return out

def gerar_regras(tipo="deriva", seed=13):
    """meu modelo de texto gerado por regras, com o leiaute do manuscrito. tipo 'casas2' ou 'deriva' (deriva lexical,
    p=0,6, correlação 3 páginas, σ=1,4 – a melhor configuração da Fase 15)."""
    V = gerador.real_pages(os.path.join(BASE, "ZL.txt")); M = gerador.SlotModel(V, dial=True)
    if tipo == "casas2": return gerador.generate(V, M, "casas2", seed=seed)
    from deriva_lexical import generate_lex
    return generate_lex(V, M, 0.6, 3, 1.4, seed=seed, pool_size=6000)

def embaralhar(pages, nivel="global", seed=7):
    """embaralha as palavras de texto corrido. 'global': entre todas as páginas de mesma seção e dialeto (destrói
    agrupamento por página); 'pagina': só dentro de cada página (preserva o agrupamento, destrói a ordem)."""
    rng = random.Random(seed)
    out = [{**pg, "lines": [(t, list(l), p) for t, l, p in pg["lines"]]} for pg in pages]
    groups = defaultdict(list)
    for pg in out: groups[(pg["I"], pg["L"]) if nivel == "global" else pg["folio"]].append(pg)
    for g, pgs in groups.items():
        flat = [w for pg in pgs for t, l, _ in pg["lines"] if t == "P" for w in l]; rng.shuffle(flat); k = 0
        for pg in pgs:
            new = []
            for t, l, p in pg["lines"]:
                if t == "P": new.append((t, flat[k:k + len(l)], p)); k += len(l)
                else: new.append((t, l, p))
            pg["lines"] = new
    return out

def filtrar(pages, dialeto=None, secao=None):
    return [p for p in pages if (not dialeto or p["L"] == dialeto) and (not secao or p["I"] == secao)]

# ---------------- métricas ----------------
def repaginar(pages, fichas=200):
    """re-corta o texto corrido em páginas de N fichas, dentro de cada seção×dialeto, na ordem original."""
    groups = defaultdict(list)
    for pg in pages: groups[(pg["I"], pg["L"])].append(pg)
    out = []
    for (I, Lg), pgs in groups.items():
        flat = [w for pg in pgs for t, l, _ in pg["lines"] if t == "P" for w in l]
        for i in range(0, len(flat) - fichas + 1, fichas):
            ch = flat[i:i + fichas]
            out.append({"folio": f"{I}{Lg}-{i:06d}", "I": I, "L": Lg, "lines": [("P", ch[j:j + 9], j == 0) for j in range(0, fichas, 9)]})
    return out

def _blocks(pages, k):
    out = []; by = defaultdict(list)
    for pg in pages: by[(pg["I"], pg["L"])].append(pg)
    for g, pgs in by.items():
        for i in range(0, len(pgs), k):
            ch = pgs[i:i + k]
            out.append({"folio": ch[0]["folio"], "I": ch[0]["I"], "L": ch[0]["L"], "lines": [x for p in ch for x in p["lines"]]})
    return out

def _page_metrics(pages, rng):
    by = defaultdict(list)
    for pg in pages:
        ws = [w for t, l, _ in pg["lines"] if t == "P" for w in l]
        if len(ws) >= 40: by[(pg["I"], pg["L"])].append((pg["folio"], ws))
    kw = nn = 0; adj = []
    for g, pgs in by.items():
        pgs.sort(key=lambda x: folio_key(x[0]) if x[0].startswith("f") else x[0])
        if len(pgs) < 8: continue
        o, e, n, _ = keywords(pgs, rng, reps=5); kw += o; nn += n
        a, f = adjacency(pgs); adj.append(a - f)
    agr = clustering([{**p, "I": (p["I"], p["L"])} for p in pages])[0]
    b8 = clustering([{**p, "I": (p["I"], p["L"])} for p in _blocks(pages, 8)])[0]
    return {"agrup": agr, "bloco8": b8, "chave_frac": kw / nn if nn else float("nan"), "viz": st.mean(adj) if adj else float("nan")}

def zipf_slope(words):
    c = sorted(Counter(words).values(), reverse=True)[:1000]
    xs = [math.log(r) for r in range(1, len(c) + 1)]; ys = [math.log(v) for v in c]
    mx, my = st.mean(xs), st.mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)

def medir(pages, nome="", seed=5):
    """todas as métricas, num dicionário. Métricas de linha (-m, gallows de parágrafo, ed) também saem, mas só fazem
    sentido para o manuscrito e para o modelo de regras."""
    rng = random.Random(seed)
    b = gerador.battery(pages, nome)
    words = [w for pg in pages for t, l, _ in pg["lines"] if t == "P" for w in l]
    b["n"] = len(words); b["zipf"] = zipf_slope(words)
    b.update(_page_metrics(pages, rng))
    rp = repaginar(pages, 200)
    pm = _page_metrics(rp, rng)
    b.update({k + "_200": v for k, v in pm.items()})
    return {k: (float(v) if isinstance(v, (int, float)) else v) for k, v in b.items()}

def subamostras(pages, nome="", reps=10, frac=0.5, seed=9):
    """variação interna: métricas em 'reps' subconjuntos aleatórios de metade das páginas (sem reposição).
    Devolve {métrica: (mínimo, mediana, máximo)}."""
    rng = random.Random(seed); runs = []
    for r in range(reps):
        sub = sorted(rng.sample(pages, max(8, int(frac * len(pages)))), key=lambda p: pages.index(p))
        runs.append(medir(sub, nome, seed=seed + r))
    keys = [k for k in runs[0] if isinstance(runs[0][k], float)]
    return {k: (min(x[k] for x in runs), st.median(x[k] for x in runs), max(x[k] for x in runs)) for k in keys}

PRINCIPAIS = [("n", "fichas de texto", "{:.0f}"), ("h2", "h2 (bits)", "{:.2f}"), ("compr", "comprimento médio (unid.)", "{:.2f}"),
              ("TTR", "razão tipo/ocorrência", "{:.3f}"), ("hapax", "formas únicas", "{:.0%}"), ("zipf", "inclinação de Zipf", "{:.2f}"),
              ("razao", "MI junção ÷ MI dentro", "{:.2f}"), ("F1esp", "F1 do espaço", "{:.2f}"), ("rep", "repetição imediata", "{:.2%}"),
              ("agrup_200", "agrupamento (páginas de 200)", "{:+.3f}"), ("bloco8_200", "agrupamento em blocos de 8", "{:+.3f}"),
              ("chave_frac_200", "palavras-chave de página", "{:.1%}"), ("viz_200", "vizinhas − distantes", "{:+.3f}"),
              ("agrup", "agrupamento (páginas naturais)", "{:+.3f}"), ("eco", "eco dos rótulos (própria página)", "{:.0%}"),
              ("conc_rot", "concentração dos rótulos ecoados", "{:.3f}"), ("conc_nulo", "… de fichas da página", "{:.3f}")]

def tabela_md(res, linhas=PRINCIPAIS):
    nomes = list(res)
    out = ["| Métrica | " + " | ".join(nomes) + " |", "|---|" + "---|" * len(nomes)]
    for k, lab, fmt in linhas:
        cells = []
        for n in nomes:
            v = res[n].get(k)
            cells.append("–" if v is None or (isinstance(v, float) and v != v) else fmt.format(v))
        out.append(f"| {lab} | " + " | ".join(cells) + " |")
    return "\n".join(out)
