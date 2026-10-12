"""Fase 10a – Dois geradores de texto SEM conteúdo, com o mesmo leiaute de páginas, parágrafos, linhas e rótulos do
manuscrito, e a mesma bateria de medidas aplicada ao Voynich.
  G-casas : palavras geradas por uma cadeia de Markov de ordem 2 sobre unidades, ajustada por seção (com recuo para o
            modelo geral); a primeira unidade de cada palavra depende da última da palavra anterior (regra de emenda);
            distribuições próprias para início de linha, início de parágrafo e rótulo; a linha é preenchida até a largura
            da linha real, e a palavra que não cabe vira forma em -m (daiin->dam, chol->chom) se couber, senão é descartada.
  G-cópia : 'autocitação' – cada palavra nova é, com prob. 1-p, uma cópia modificada (0–2 trocas de unidade, prefixo
            ou final) de uma palavra já escrita na mesma página; com prob. p, uma palavra nova do G-casas. Rótulos também
            são copiados do texto da página com prob. 0,5. Mesmo preenchimento de linha.
Nada é ajustado palavra a palavra; os únicos parâmetros livres (p, q) estão no topo."""
import math, random, re, statistics as st, sys, json
from collections import Counter, defaultdict
from ivtff import parse, units

P_FRESH = 0.35      # G-cópia: fração de palavras novas
Q_M = 0.6           # chance de usar a forma em -m quando a palavra não cabe
BETA = 5.0

def real_pages(path="ZL.txt"):
    L, pv = parse(path)
    pages = {}
    for l in L:
        p = pages.setdefault(l.folio, {"folio": l.folio, "I": pv[l.folio].get("I"), "L": pv[l.folio].get("L"), "lines": []})
        ws = [w for w in l.split if "?" not in w]
        if not ws: continue
        typ = "L" if l.ltype[0] == "L" else "P" if l.ltype[0] == "P" else "O"
        par = (l.pos in "@*") or ("<%>" in l.raw)
        p["lines"].append((typ, ws, par))
    return list(pages.values())

class SlotModel:
    def __init__(self, pages, dial=False):
        self.dial = dial
        self.tr = defaultdict(lambda: defaultdict(Counter)); self.pool = defaultdict(Counter)
        self.junc = defaultdict(lambda: defaultdict(Counter)); self.jpool = defaultdict(Counter)
        self.first = defaultdict(lambda: defaultdict(Counter))      # [sec][kind] kind in line, par, label
        self.fpool = defaultdict(Counter)
        for pg in pages:
            s = (pg["I"], pg["L"]) if self.dial else pg["I"]
            for typ, ws, par in pg["lines"]:
                for i, w in enumerate(ws):
                    u = units(w); seq = ["^", "^"] + u + ["$"]
                    if self.dial and typ == "P" and i == len(ws) - 1 and w.endswith("m"):
                        continue                      # a forma em -m é produzida pela regra de margem, não pela cadeia
                    for k in range(2, len(seq)):
                        st_ = (seq[k - 2], seq[k - 1]); self.tr[s][st_][seq[k]] += 1
                        self.pool[(pg["L"], st_) if self.dial else st_][seq[k]] += 1
                    if typ == "L":
                        self.first[s]["label"][u[0]] += 1; self.fpool["label"][u[0]] += 1
                    elif i == 0:
                        kind = "par" if par else "line"
                        self.first[s][kind][u[0]] += 1; self.fpool[kind][u[0]] += 1
                    else:
                        last = units(ws[i - 1])[-1]
                        self.junc[s][last][u[0]] += 1; self.jpool[last][u[0]] += 1

    def _draw(self, cs, cp, rng):
        keys = sorted(set(cs) | set(cp)); ns = sum(cs.values()); npool = sum(cp.values())   # ordem fixa: reprodutível
        if not keys:                     # contexto nunca visto no treino: início de palavra mais comum
            return rng.choice(["o", "ch", "d", "q", "s", "y"])
        weights = [cs.get(k, 0) + BETA * cp.get(k, 0) / max(npool, 1) for k in keys]
        return rng.choices(keys, weights)[0]

    def word(self, sec, rng, kind="mid", last=None, dial=None):
        if kind == "mid":
            u1 = self._draw(self.junc[sec].get(last, Counter()), self.jpool.get(last) or self.fpool["line"], rng)
        else:
            if not self.first[sec][kind] and not self.fpool[kind]:
                kind = "line" if (self.first[sec]["line"] or self.fpool["line"]) else "par"
            u1 = self._draw(self.first[sec][kind], self.fpool[kind], rng)
        seq = ["^", u1]
        for _ in range(14):
            st_ = (seq[-2], seq[-1])
            key = (dial, st_) if self.dial else st_
            if key not in self.pool:
                if self.dial and any(k[1] == st_ for k in [(dial, st_)]) is False and st_ in self.tr[sec]:
                    key = None
                else:
                    break
            cp = self.pool[key] if key is not None else Counter()
            nxt = self._draw(self.tr[sec].get(st_, Counter()), cp, rng)
            if nxt == "$": break
            seq.append(nxt)
        return "".join(seq[1:])

M_RE = re.compile(r"(a|o|e)?i*n$|l$|r$")

def to_m(w):
    if re.search(r"[ao]i*n$", w): return re.sub(r"([ao])i*n$", r"\1m", w)
    if re.search(r"i+n$", w): return re.sub(r"i+n$", "m", w)
    if re.search(r"[lr]$", w) and len(w) > 1: return w[:-1] + "m"
    return None

MUT_PAIRS = [("k", "t"), ("p", "f"), ("ch", "sh"), ("cth", "ckh"), ("e", "ee"), ("o", "a"), ("l", "r"), ("d", "l"), ("s", "d")]
PREF = ["", "qo", "o", "y", "d", "s", "ch", "sh"]
FINS = ["y", "dy", "ey", "edy", "l", "r", "iin", "ain", "ol", "or", "al", "ar", "eey", "aiin"]

def mutate(w, rng):
    u = units(w)
    t = rng.random()
    if t < 0.45 and u:
        i = rng.randrange(len(u)); a = u[i]
        opts = [b for x, y in MUT_PAIRS for b in ((y,) if a == x else (x,) if a == y else ())]
        if opts: u[i] = rng.choice(opts); return "".join(u)
    if t < 0.7:
        s = "".join(u)
        for p in sorted(PREF, key=len, reverse=True):
            if p and s.startswith(p) and len(s) > len(p) + 1:
                return rng.choice(PREF) + s[len(p):]
        return rng.choice(PREF) + s
    s = "".join(u)
    for f in sorted(FINS, key=len, reverse=True):
        if s.endswith(f) and len(s) > len(f):
            return s[:-len(f)] + rng.choice(FINS)
    return s + rng.choice(FINS)

MUT3 = 0.5
SLOT_PAIRS = [("k", "t"), ("p", "f"), ("ch", "sh"), ("cth", "ckh"), ("e", "ee"), ("o", "a"), ("l", "r")]
FINS3 = ["y", "dy", "ey", "edy", "l", "r", "iin", "ain", "ol", "or", "al", "ar", "eey", "aiin", "s", "m"]

def mutate_slot(w, rng):
    """troca que mantém a palavra dentro da gramática: um glifo pelo seu par, ou um final por outro final comum."""
    u = units(w)
    if rng.random() < 0.6:
        idx = [i for i, a in enumerate(u) if any(a in pr for pr in SLOT_PAIRS)]
        if idx:
            i = rng.choice(idx); a = u[i]
            u[i] = [y if a == x else x for x, y in SLOT_PAIRS if a in (x, y)][0]
            return "".join(u)
    s = "".join(u)
    for f in sorted(FINS3, key=len, reverse=True):
        if s.endswith(f) and len(s) > len(f):
            return s[:-len(f)] + rng.choice([x for x in FINS3 if x != "m"])
    return s

def fill_line(target, make, rng, allow_m=True):
    """gera palavras com make(prev) até a largura target (em letras EVA, contando espaços)."""
    out = []; width = 0
    while True:
        w = make(out[-1] if out else None)
        need = len(w) + (1 if out else 0)
        if width + need <= target or not out:
            out.append(w); width += need
            if width >= target: break
            continue
        m = to_m(w) if allow_m else None
        if m and rng.random() < Q_M and width + len(m) + 1 <= target + 1:
            out.append(m)
        break
    return out

C_LOCAL = 0.01      # G-casas2: chance de repetir/variar a palavra anterior
Q_MARGEM = 0.35     # G-casas2: chance de comprimir em -m a última palavra de uma linha cheia

MEIA_VIDA = 1000    # G-repertório: meia-vida (em palavras) do peso de uma palavra no repertório do escriba
JANELA2 = 300       # G-cópia2: copia de qualquer uma das últimas 300 palavras escritas, mesmo de páginas anteriores

def generate(pages, model, mode, seed=1):
    rng = random.Random(seed); gen = []
    history = []        # G-cópia2: tudo o que já foi escrito no códice, em ordem
    rep = {}; clock = [0]; lam = 0.5 ** (1.0 / MEIA_VIDA)   # G-repertório: pesos com decaimento exponencial
    for pg in pages:
        s = (pg["I"], pg["L"]) if model.dial else pg["I"]; npg = {"folio": pg["folio"], "I": pg["I"], "L": pg["L"], "lines": []}
        widths = sorted(len(".".join(ws)) for typ, ws, _ in pg["lines"] if typ == "P")
        full = widths[int(0.5 * len(widths))] if widths else 0
        written = []
        def fresh(prev, kind):
            if kind == "mid":
                return model.word(s, rng, "mid", units(prev)[-1], dial=pg["L"])
            return model.word(s, rng, kind, dial=pg["L"])
        def make_factory(first_kind):
            state = {"first": True}
            def make(prev):
                kind = first_kind if state["first"] else "mid"
                state["first"] = False
                if mode == "casas2" and prev and rng.random() < C_LOCAL:
                    w = prev
                    if rng.random() < 0.5: w = mutate(w, rng)
                    return w or fresh(prev, kind)
                if mode == "copia2" and history and rng.random() > P_FRESH:
                    w = rng.choice(history[-JANELA2:])
                    for _ in range(rng.choice([1, 1, 1, 2, 2])): w = mutate(w, rng)
                    if w: return w
                if mode == "repertorio":
                    clock[0] += 1
                    if clock[0] % 500 == 0:          # renormaliza e poda o repertório
                        f = lam ** 500
                        for k in list(rep):
                            rep[k] *= f
                            if rep[k] < 1e-3: del rep[k]
                    boost = lam ** -(clock[0] % 500)
                    if rep and rng.random() > P_FRESH:
                        ks = list(rep); w = rng.choices(ks, [rep[k] for k in ks])[0]
                    else:
                        w = fresh(prev, kind)
                    rep[w] = rep.get(w, 0.0) + boost
                    return w
                if mode == "copia3" and history and rng.random() > P_FRESH:
                    w = rng.choice(history[-JANELA2:])           # cópia com mutação que respeita as casas
                    if rng.random() < MUT3: w = mutate_slot(w, rng)
                    if w: return w
                if mode == "copia" and written and rng.random() > P_FRESH:
                    src = rng.choice(written[-60:])
                    w = src
                    for _ in range(rng.choice([0, 1, 1, 2])): w = mutate(w, rng)
                    if not w: w = fresh(prev, kind)
                else:
                    w = fresh(prev, kind)
                return w
            return make
        for typ, ws, par in pg["lines"]:
            if typ == "L":
                if mode in ("copia", "copia2", "copia3") and written and rng.random() < 0.5:
                    lab = [mutate(rng.choice(written), rng) if rng.random() < 0.5 else rng.choice(written) for _ in ws]
                else:
                    lab = [model.word(s, rng, "label") for _ in ws]
                npg["lines"].append(("L", lab, False))
                continue
            target = len(".".join(ws))
            line = fill_line(target, make_factory("par" if par else "line"), rng,
                             allow_m=(mode not in ("casas2", "copia3", "repertorio") or target >= full))
            if mode in ("casas2", "copia3", "repertorio") and target >= full and line and not line[-1].endswith("m") and rng.random() < Q_MARGEM:
                m = to_m(line[-1])
                if m: line[-1] = m
            written.extend(line); history.extend(line)
            npg["lines"].append((typ, line, par))
        gen.append(npg)
    return gen

# ---------------- bateria de medidas ----------------
def mi(pairs):
    n = len(pairs); a = Counter(x for x, _ in pairs); b = Counter(y for _, y in pairs); ab = Counter(pairs)
    return sum(c / n * math.log2((c / n) / ((a[x] / n) * (b[y] / n))) for (x, y), c in ab.items())

def mi_net(pairs, rng):
    xs = [x for x, _ in pairs]; ys = [y for _, y in pairs]; r = []
    for _ in range(3):
        y2 = ys[:]; rng.shuffle(y2); r.append(mi(list(zip(xs, y2))))
    return mi(pairs) - sum(r) / 3

def battery(pages, name):
    rng = random.Random(0)
    para = [(pg, ws, par) for pg in pages for typ, ws, par in pg["lines"] if typ == "P"]
    words = [w for _, ws, _ in para for w in ws]
    res = {}
    seq = []
    for w in words: seq.extend(w); seq.append("_")
    bi = Counter(zip(seq, seq[1:])); uni = Counter(seq[:-1]); n = sum(bi.values())
    res["h2"] = -sum(c / n * math.log2(c / uni[a]) for (a, b), c in bi.items())
    L = [len(units(w)) for w in words]; res["compr"] = st.mean(L); res["dp"] = st.pstdev(L)
    cnt = Counter(words); res["TTR"] = len(cnt) / len(words); res["hapax"] = sum(1 for v in cnt.values() if v == 1) / len(cnt)
    j = [(a[-1], units(b)[0]) for _, ws, _ in para for a, b in zip(ws, ws[1:])]
    wi = [(units(w)[0], w[-1]) for w in words if len(units(w)) >= 3]
    res["MIj"] = mi_net(j, rng); res["MIw"] = mi_net(wi, rng); res["razao"] = res["MIj"] / max(res["MIw"], 1e-9)
    from espaco import stream_with_breaks, evaluate
    ev = evaluate(stream_with_breaks([ws for _, ws, _ in para if len(ws) > 1], units), 2); res["F1esp"] = ev["F1"]
    pairs = [(a, b) for _, ws, _ in para for a, b in zip(ws, ws[1:])]
    res["rep"] = sum(a == b for a, b in pairs) / len(pairs)
    def d1(a, b):
        ua, ub = units(a), units(b)
        if ua == ub: return False
        if len(ua) == len(ub): return sum(x != y for x, y in zip(ua, ub)) == 1
        if abs(len(ua) - len(ub)) == 1:
            s, t = (ua, ub) if len(ua) < len(ub) else (ub, ua)
            return any(s == t[:i] + t[i + 1:] for i in range(len(t)))
        return False
    res["quase"] = sum(d1(a, b) for a, b in pairs) / len(pairs)
    lines = sorted((len(".".join(ws)), ws[-1].endswith("m")) for _, ws, _ in para if len(ws) >= 3)
    q = len(lines) // 4
    res["m_curtas"] = sum(m for _, m in lines[:q]) / q; res["m_longas"] = sum(m for _, m in lines[-q:]) / q
    mids = [w for _, ws, _ in para for w in ws[1:-1]]; res["m_meio"] = sum(w.endswith("m") for w in mids) / len(mids)
    pf = [ws[0] for _, ws, par in para if par]; res["par_gallows"] = sum(units(w)[0] in ("p", "t", "k", "f") for w in pf) / max(len(pf), 1)
    A = [w for pg, ws, _ in para if pg["L"] == "A" for w in ws]; B = [w for pg, ws, _ in para if pg["L"] == "B" for w in ws]
    res["ed_A"] = sum("ed" in w for w in A) / max(len(A), 1); res["ed_B"] = sum("ed" in w for w in B) / max(len(B), 1)
    # divergência entre herbal e biológica (Jensen-Shannon de palavras, suavizado)
    H = Counter(w for pg, ws, _ in para if pg["I"] == "H" for w in ws); Bi = Counter(w for pg, ws, _ in para if pg["I"] == "B" for w in ws)
    voc = set(H) | set(Bi); nh, nb = sum(H.values()), sum(Bi.values())
    js = 0
    for w in voc:
        p_ = (H[w] + .1) / (nh + .1 * len(voc)); q_ = (Bi[w] + .1) / (nb + .1 * len(voc)); m_ = (p_ + q_) / 2
        js += .5 * p_ * math.log2(p_ / m_) + .5 * q_ * math.log2(q_ / m_)
    res["JS_H_B"] = js
    # rótulos: eco na própria página x página aleatória; concentração dos ecoados
    text = defaultdict(list); labs = defaultdict(list)
    for pg in pages:
        for typ, ws, _ in pg["lines"]:
            (labs if typ == "L" else text)[pg["folio"]].extend(ws)
    tp = {p: set(v) for p, v in text.items()}; pgs = [p for p in tp if len(text[p]) > 50]
    same = tot = rnd = 0
    for p, ls in labs.items():
        for w in ls:
            if len(units(w)) < 3: continue
            tot += 1; same += w in tp.get(p, set()); rnd += w in tp[rng.choice(pgs)]
    res["eco"] = same / max(tot, 1); res["eco_acaso"] = rnd / max(tot, 1)
    sec_of = {pg["folio"]: pg["I"] for pg in pages}
    for S in ("B", "C"):
        sm = tt = rr = 0; spg = [p for p in pgs if sec_of[p] == S]
        for p, ls in labs.items():
            if sec_of[p] != S or not spg: continue
            for w in ls:
                if len(units(w)) < 3: continue
                tt += 1; sm += w in tp.get(p, set()); rr += w in tp[rng.choice(spg)]
        res[f"eco_{S}"] = sm / max(tt, 1); res[f"eco_{S}_acaso"] = rr / max(tt, 1)
    from rotulos_especificidade import analyze
    a = analyze(text, labs, name, reps=50, out=lambda s: None)
    res["conc_rot"] = a["conc"]; res["conc_nulo"] = a["conc_null"]; res["freq_rot"] = a["freq"]; res["freq_nulo"] = a["freq_null"]
    return res

ROWS = [("h2", "h2 (bits)", "{:.2f}"), ("compr", "comprimento médio (unid.)", "{:.2f}"), ("dp", "desvio do comprimento", "{:.2f}"),
        ("TTR", "razão tipo/ocorrência", "{:.3f}"), ("hapax", "formas que aparecem uma vez", "{:.0%}"),
        ("razao", "MI junção ÷ MI dentro", "{:.2f}"), ("F1esp", "F1 ao recolocar o espaço", "{:.2f}"),
        ("rep", "repetição imediata", "{:.2%}"), ("quase", "vizinhos que diferem em 1 unidade", "{:.2%}"),
        ("m_curtas", "-m no fim: linhas curtas", "{:.1%}"), ("m_longas", "-m no fim: linhas longas", "{:.1%}"),
        ("m_meio", "-m no meio da linha", "{:.1%}"), ("par_gallows", "parágrafo começa com gallows", "{:.0%}"),
        ("ed_A", "'ed' em A", "{:.1%}"), ("ed_B", "'ed' em B", "{:.1%}"), ("JS_H_B", "divergência herbal × biológica (JS)", "{:.3f}"),
        ("eco", "rótulo reaparece na própria página", "{:.0%}"), ("eco_acaso", "… numa página qualquer", "{:.0%}"),
        ("eco_B", "eco na própria página (biológica)", "{:.0%}"), ("eco_B_acaso", "… outra página da mesma seção", "{:.0%}"),
        ("eco_C", "eco na própria página (cosmológica)", "{:.0%}"), ("eco_C_acaso", "… outra página da mesma seção", "{:.0%}"),
        ("conc_rot", "concentração dos rótulos ecoados", "{:.3f}"), ("conc_nulo", "… de fichas da página", "{:.3f}"),
        ("freq_rot", "frequência global dos ecoados", "{:.0f}"), ("freq_nulo", "… de fichas da página", "{:.0f}")]

if __name__ == "__main__":
    pages = real_pages()
    model = SlotModel(pages)
    res = {"Voynich": battery(pages, "Voynich")}
    res["G-casas"] = battery(generate(pages, model, "casas", seed=11), "G-casas")
    res["G-cópia"] = battery(generate(pages, model, "copia", seed=12), "G-cópia")
    model2 = SlotModel(pages, dial=True)
    res["G-casas2"] = battery(generate(pages, model2, "casas2", seed=13), "G-casas2")
    json.dump(res, open("gerador_resultados.json", "w"), indent=1)
    print("| Medida | Voynich | G-casas | G-casas2 | G-cópia |\n|---|---|---|---|---|")
    for k, lab, fmt in ROWS:
        print(f"| {lab} | " + " | ".join(fmt.format(res[g][k]) for g in ("Voynich", "G-casas", "G-casas2", "G-cópia")) + " |")
    # amostra de linhas geradas
    g = generate(pages[:3], model, "copia", seed=12)
    for pg in g[:2]:
        for typ, ws, par in pg["lines"][:3]: print(pg["folio"], typ, ".".join(ws))
