"""Fase 1 – análise estatística própria das transliterações (ZL principal, RF conferência)."""
import math, random, re, sys, json
from collections import Counter, defaultdict
from ivtff import parse, units

random.seed(1404)
SECT = {"H": "herbal", "P": "farmacêutica", "B": "biológica", "S": "estrelas/receitas",
        "Z": "zodíaco", "A": "astronômica", "C": "cosmológica", "T": "só texto"}

def has_q(w):
    return "?" in w

def entropy(counter):
    n = sum(counter.values())
    return -sum(c / n * math.log2(c / n) for c in counter.values())

def cond_entropy(seq):
    """h2 = H(X_n | X_{n-1}) sobre uma sequência de símbolos."""
    bi = Counter(zip(seq, seq[1:]))
    uni = Counter(seq[:-1])
    n = sum(bi.values())
    return -sum(c / n * math.log2(c / uni[a]) for (a, b), c in bi.items())

def text_stream(words, unit_mode):
    seq = []
    for w in words:
        seq.extend(units(w) if unit_mode else list(w))
        seq.append("_")
    return seq

def latin_words(maxw=None):
    import glob
    from config import LATIN_LIBRARY as base
    txt = ""
    for f in [base + "isidore/17.txt", base + "isidore/4.txt", base + "isidore/16.txt", base + "apicius/apicius1.txt",
              base + "apicius/apicius2.txt", base + "apicius/apicius3.txt"]:
        txt += open(f, encoding="utf-8", errors="ignore").read() + " "
    txt = txt.lower().replace("v", "u").replace("j", "i")
    ws = re.findall(r"[a-z]+", txt)
    return ws[:maxw] if maxw else ws

def main(path="ZL.txt", comma="split", out=print):
    L, pv = parse(path)
    get = (lambda l: l.split) if comma == "split" else (lambda l: l.join)
    para = [l for l in L if l.ltype[0] == "P"]
    labels = [l for l in L if l.ltype[0] == "L"]
    allw = [w for l in L for w in get(l)]
    pw = [w for l in para for w in get(l)]
    clean = [w for w in allw if not has_q(w)]
    res = {}
    out(f"\n===== {path} | vírgula={comma} =====")
    out(f"linhas {len(L)}  tokens {len(allw)}  tipos {len(set(allw))}  tokens-parágrafo {len(pw)}  tokens-rótulo {sum(len(get(l)) for l in labels)}")
    res["tokens"], res["types"] = len(allw), len(set(allw))

    # --- glifos e posição
    uc = Counter(); pos = defaultdict(Counter)
    for w in clean:
        u = units(w)
        for i, g in enumerate(u):
            uc[g] += 1
            p = "só" if len(u) == 1 else ("ini" if i == 0 else ("fim" if i == len(u) - 1 else "meio"))
            pos[g][p] += 1
    out("\nUnidades glíficas (top 22) e % por posição na palavra [ini/meio/fim/só]:")
    tot = sum(uc.values())
    for g, c in uc.most_common(22):
        p = pos[g]; s = sum(p.values())
        out(f"  {g:5s} {c:6d} {100*c/tot:5.1f}%  ini {100*p['ini']/s:5.1f}  meio {100*p['meio']/s:5.1f}  fim {100*p['fim']/s:5.1f}  só {100*p['só']/s:4.1f}")
    res["units"] = uc.most_common(40)

    # --- entropia
    ev = text_stream(clean, False); un = text_stream(clean, True)
    lat = latin_words()
    nlat = len(ev)
    lw = []; n = 0
    for w in lat:
        lw.append(w); n += len(w) + 1
        if n >= nlat: break
    lt = text_stream(lw, False)
    out("\nEntropia (bits): h1 = incondicional, h2 = condicional ao símbolo anterior (espaço conta como símbolo)")
    for name, s in [("Voynich EVA-letras", ev), ("Voynich unidades", un), ("Latim (Isidoro XVII/IV/XVI + Apício), mesmo tamanho", lt)]:
        out(f"  {name:52s} alfabeto {len(set(s)):3d}  h1 {entropy(Counter(s)):.2f}  h2 {cond_entropy(s):.2f}")
    res["h2_eva"] = cond_entropy(ev); res["h2_lat"] = cond_entropy(lt)

    # --- comprimento de palavra
    def lenstats(ws, f):
        ls = [f(w) for w in ws]; m = sum(ls) / len(ls)
        sd = (sum((x - m) ** 2 for x in ls) / len(ls)) ** .5
        return m, sd, Counter(ls)
    mv, sv, cv = lenstats(clean, lambda w: len(units(w)))
    me, se, ce = lenstats(clean, len)
    ml, sl, cl = lenstats(lw, len)
    out(f"\nComprimento médio: Voynich {me:.2f}±{se:.2f} letras EVA, {mv:.2f}±{sv:.2f} unidades; Latim {ml:.2f}±{sl:.2f} letras")
    out("  distribuição (unidades) " + " ".join(f"{k}:{100*cv[k]/len(clean):.1f}" for k in range(1, 11)))
    out("  distribuição (latim)    " + " ".join(f"{k}:{100*cl[k]/len(lw):.1f}" for k in range(1, 13)))
    out(f"  razão tipo/token: Voynich {len(set(clean))/len(clean):.3f}  Latim (mesmo nº de palavras) {len(set(lat[:len(clean)]))/len(clean):.3f}")
    hap_v = sum(1 for w, c in Counter(clean).items() if c == 1); hap_l = sum(1 for w, c in Counter(lat[:len(clean)]).items() if c == 1)
    out(f"  hapax: Voynich {hap_v} ({100*hap_v/len(set(clean)):.0f}% dos tipos)  Latim {hap_l} ({100*hap_l/len(set(lat[:len(clean)])):.0f}%)")

    # --- gramática de casas (definida uma vez, explícita)
    G = re.compile(r"^(q?o|y|d|s|l|r)?"            # casa 1: prefixo
                   r"(k|t|p|f|ckh|cth|cph|cfh)?"    # casa 2: gallows (simples ou bancado)
                   r"(ch|sh)?"                      # casa 3: bancada
                   r"(e{1,3})?"                     # casa 4: e-série
                   r"(k|t|p|f|ckh|cth)?"            # casa 2b: gallows tardio
                   r"(o|a)?"                        # casa 5: vogal
                   r"(i{1,3}n|i{1,3}r|in|n|r|l|m|s|d|dy|y|ly|ry|ey|g)?$")  # casa 6: final
    cov_tok = sum(1 for w in clean if G.match(w)) / len(clean)
    types = set(clean)
    cov_typ = sum(1 for w in types if G.match(w)) / len(types)
    out(f"\nGramática de 6 casas: cobre {100*cov_tok:.1f}% dos tokens e {100*cov_typ:.1f}% dos tipos")
    gl = sum(1 for w in lw if G.match(w)) / len(lw)
    out(f"  (controle: a mesma gramática aplicada a palavras latinas, letras como EVA: {100*gl:.1f}%)")
    res["grammar_cov"] = cov_tok

    # --- palavras por seção
    out("\nPalavras mais comuns por seção (só parágrafos/círculos/radiais, sem rótulos):")
    bysec = defaultdict(Counter)
    for l in L:
        if l.ltype[0] != "L":
            for w in get(l):
                if not has_q(w): bysec[l.vars.get("I", "?")][w] += 1
    for s in "HPBSZACT":
        c = bysec[s]; n = sum(c.values())
        if n: out(f"  {SECT[s]:18s} n={n:5d}: " + ", ".join(f"{w} {100*k/n:.1f}" for w, k in c.most_common(8)))

    # --- A vs B
    lang = defaultdict(Counter)
    for l in L:
        if l.ltype[0] == "P":
            for w in get(l):
                if not has_q(w): lang[l.vars.get("L", "?")][w] += 1
    A, B = lang["A"], lang["B"]; nA, nB = sum(A.values()), sum(B.values())
    out(f"\nCurrier A (n={nA}) vs B (n={nB}), texto corrido:")
    out("  top A: " + ", ".join(f"{w} {100*c/nA:.1f}" for w, c in A.most_common(10)))
    out("  top B: " + ", ".join(f"{w} {100*c/nB:.1f}" for w, c in B.most_common(10)))
    def lo(w):
        a, b = A[w] + .5, B[w] + .5
        return math.log2((a / nA) / (b / nB))
    voc = [w for w in set(A) | set(B) if A[w] + B[w] >= 40]
    sv_ = sorted(voc, key=lo)
    out("  mais típicas de A (log2 razão): " + ", ".join(f"{w} {lo(w):+.1f}" for w in sv_[::-1][:10]))
    out("  mais típicas de B (log2 razão): " + ", ".join(f"{w} {lo(w):+.1f}" for w in sv_[:10]))
    def feat(c, n, f):
        return 100 * sum(k for w, k in c.items() if f(w)) / n
    feats = [("começa com qo", lambda w: w.startswith("qo")), ("contém ee", lambda w: "ee" in w),
             ("contém ed", lambda w: "ed" in w), ("termina em dy", lambda w: w.endswith("dy")),
             ("termina em aiin/ain", lambda w: w.endswith("ain") or w.endswith("aiin")),
             ("termina em ol", lambda w: w.endswith("ol")), ("termina em or", lambda w: w.endswith("or")),
             ("começa com ch/sh", lambda w: w[:2] in ("ch", "sh")), ("contém gallows k/t/p/f", lambda w: bool(re.search("[ktpf]", w)))]
    for name, f in feats:
        out(f"  {name:24s} A {feat(A, nA, f):5.1f}%   B {feat(B, nB, f):5.1f}%")
    res["AB"] = {name: (feat(A, nA, f), feat(B, nB, f)) for name, f in feats}

    # --- escribas
    out("\nEscribas ($H), texto corrido: % de palavras terminadas em -dy / -aiin|ain / -ol|or / começando com qo")
    hand = defaultdict(Counter)
    for l in L:
        if l.ltype[0] == "P":
            for w in get(l):
                if not has_q(w): hand[l.vars.get("H", "?")][w] += 1
    for h in sorted(hand):
        c = hand[h]; n = sum(c.values())
        if n > 300:
            out(f"  mão {h}: n={n:5d}  dy {feat(c,n,lambda w:w.endswith('dy')):4.1f}  aiin {feat(c,n,lambda w:w.endswith('ain') or w.endswith('aiin')):4.1f}  ol/or {feat(c,n,lambda w:w.endswith('ol') or w.endswith('or')):4.1f}  qo {feat(c,n,lambda w:w.startswith('qo')):4.1f}  ee {feat(c,n,lambda w:'ee' in w):4.1f}")

    # --- rótulos
    lab = [w for l in labels for w in get(l) if not has_q(w)]
    labsec = Counter(l.vars.get("I") for l in labels)
    out(f"\nRótulos: {len(lab)} palavras em {len(labels)} rótulos; por seção: " + ", ".join(f"{SECT.get(k,k)} {v}" for k, v in labsec.most_common()))
    def initdist(ws):
        c = Counter(units(w)[0] for w in ws); n = len(ws)
        return {g: 100 * k / n for g, k in c.items()}
    di, dp = initdist(lab), initdist([w for w in pw if not has_q(w)])
    out("  1ª unidade (rótulo vs texto corrido): " + ", ".join(f"{g} {di.get(g,0):.0f}/{dp.get(g,0):.0f}" for g in ["o", "ch", "sh", "q", "d", "y", "s", "k", "t", "p", "f", "a", "l", "r", "cth", "ckh"]))
    out(f"  começam com ok-/ot-: rótulos {100*sum(1 for w in lab if w[:2] in ('ok','ot'))/len(lab):.1f}%  texto {100*sum(1 for w in pw if w[:2] in ('ok','ot'))/len(pw):.1f}%")
    out(f"  comprimento médio (unid.): rótulos {sum(len(units(w)) for w in lab)/len(lab):.2f}  texto {sum(len(units(w)) for w in pw if not has_q(w))/len([w for w in pw if not has_q(w)]):.2f}")
    ptypes = Counter(w for w in pw)
    labt = set(lab)
    inpara = sum(1 for w in labt if w in ptypes)
    out(f"  tipos de rótulo que também ocorrem no texto corrido: {inpara}/{len(labt)} ({100*inpara/len(labt):.0f}%)")
    labrep = Counter(lab)
    out(f"  rótulos (palavra) que se repetem: {sum(1 for c in labrep.values() if c>1)} tipos; mais repetidos: " + ", ".join(f"{w}×{c}" for w, c in labrep.most_common(8)))
    out(f"  terminam em -y: rótulos {100*sum(1 for w in lab if w.endswith('y'))/len(lab):.0f}%  texto {100*sum(1 for w in pw if w.endswith('y'))/len(pw):.0f}%; em -ar/-al: rótulos {100*sum(1 for w in lab if w[-2:] in ('ar','al'))/len(lab):.0f}%  texto {100*sum(1 for w in pw if w[-2:] in ('ar','al'))/len(pw):.0f}%")

    # --- posição na linha
    out("\nEfeitos de linha (texto corrido):")
    first = Counter(); last = Counter(); mid = Counter(); parfirst = Counter(); nlines = 0
    for l in para:
        ws = [w for w in get(l) if not has_q(w)]
        if len(ws) < 3: continue
        nlines += 1
        first[units(ws[0])[0]] += 1; last[ws[-1][-1]] += 1
        for w in ws[1:-1]: mid[units(w)[0]] += 1
        if l.pos in "@*" or "<%>" in l.raw: parfirst[units(ws[0])[0]] += 1
    nm = sum(mid.values()); npf = sum(parfirst.values())
    for g in ["p", "f", "t", "k", "s", "d", "y", "o", "q", "ch", "sh"]:
        out(f"  1ª palavra começa com {g:3s}: início de linha {100*first[g]/nlines:5.1f}%  meio {100*mid[g]/nm:5.1f}%  início de parágrafo {100*parfirst[g]/npf:5.1f}%")
    endm = Counter();
    for l in para:
        for w in get(l)[1:-1]:
            endm[w[-1]] += 1
    nem = sum(endm.values())
    for g in ["m", "g", "y", "n", "l", "r", "s"]:
        out(f"  última letra da palavra = {g}: fim de linha {100*last[g]/nlines:5.1f}%  meio {100*endm[g]/nem:5.1f}%")
    # gallows p/f por linha de parágrafo
    pf_first = sum(1 for l in para if (l.pos in "@*" or "<%>" in l.raw) and re.search("[pf]", "".join(get(l))))
    pf_other = sum(1 for l in para if not (l.pos in "@*" or "<%>" in l.raw) and re.search("[pf]", "".join(get(l))))
    n_first = sum(1 for l in para if l.pos in "@*" or "<%>" in l.raw); n_other = len(para) - n_first
    out(f"  linhas com p ou f: 1ª linha de parágrafo {100*pf_first/n_first:.0f}%  demais linhas {100*pf_other/n_other:.0f}%")

    # --- repetição
    rep = 0; pairs = 0
    for l in para:
        ws = get(l)
        for a, b in zip(ws, ws[1:]):
            pairs += 1; rep += (a == b)
    sim = []
    for _ in range(20):
        r2 = 0
        allp = [w for l in para for w in get(l)]
        random.shuffle(allp)
        i = 0
        for l in para:
            ws = allp[i:i + len(get(l))]; i += len(get(l))
            r2 += sum(a == b for a, b in zip(ws, ws[1:]))
        sim.append(r2)
    exp = sum(sim) / len(sim)
    latrep = sum(a == b for a, b in zip(lat, lat[1:])) / (len(lat) - 1)
    out(f"\nRepetição imediata (w, w) no texto corrido: {rep} pares em {pairs} ({100*rep/pairs:.2f}%); esperado com palavras embaralhadas {100*exp/pairs:.2f}%; latim {100*latrep:.3f}%")
    rc = Counter()
    for l in para:
        ws = get(l)
        for a, b in zip(ws, ws[1:]):
            if a == b: rc[a] += 1
    out("  mais repetidas: " + ", ".join(f"{w}×{c}" for w, c in rc.most_common(10)))
    # quase-repetição: vizinhos que diferem por 1 unidade
    def d1(a, b):
        ua, ub = units(a), units(b)
        if ua == ub: return False
        if len(ua) == len(ub): return sum(x != y for x, y in zip(ua, ub)) == 1
        if abs(len(ua) - len(ub)) == 1:
            s, t = (ua, ub) if len(ua) < len(ub) else (ub, ua)
            return any(s == t[:i] + t[i+1:] for i in range(len(t)))
        return False
    near = sum(d1(a, b) for l in para for a, b in zip(get(l), get(l)[1:]))
    allp = [w for l in para for w in get(l)]; random.shuffle(allp)
    near_s = sum(d1(a, b) for a, b in zip(allp, allp[1:]))
    out(f"  vizinhos que diferem em 1 unidade: {100*near/pairs:.2f}% (embaralhado {100*near_s/(len(allp)-1):.2f}%)")
    res["rep"] = (rep / pairs, exp / pairs)
    return res

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "ZL.txt"
    comma = sys.argv[2] if len(sys.argv) > 2 else "split"
    main(path, comma)
