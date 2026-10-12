"""Fase 8d – Variante S′: o espaço Voynich é corte silábico de um fluxo contínuo (as fronteiras de palavra latinas
NÃO coincidem com espaços Voynich). Então a R4 muda: a linha decodificada vira uma cadeia contínua de letras e é
segmentada em palavras latinas letra a letra. Mesma chave congelada; mesmo teste da ordem.
Métrica fixada antes de rodar: fração das letras cobertas por formas latinas atestadas de 4+ letras."""
import json, random, re, statistics as st, sys
from collections import defaultdict
from ivtff import parse
from chave import decode_word
import lexicon

LEX = lexicon.load()
LONG = {w for w, f in LEX.items() if len(w) >= 4 and f >= 2}

def set_lang(lang):
    """Troca o léxico de palavras longas (la = latim; it/de = Europarl)."""
    global LONG
    if lang == "la":
        LONG = {w for w, f in LEX.items() if len(w) >= 4 and f >= 2}
    else:
        import lingua
        LONG = {w for w, f in lingua.model(lang)["lex"].items() if len(w) >= 4 and f >= 2}
MAXW = 16

def cover(s):
    """DP: máximo de letras cobertas por palavras do léxico com 4+ letras."""
    n = len(s); best = [0] * (n + 1)
    for i in range(1, n + 1):
        b = best[i - 1]
        for j in range(max(0, i - MAXW), i - 3):
            if s[j:i] in LONG:
                v = best[j] + (i - j)
                if v > b: b = v
        best[i] = b
    return best[n]

def measure_lines(lines_dec):
    cov = tot = 0
    for parts in lines_dec:
        s = "".join(p for p in parts if p)
        cov += cover(s); tot += len(s)
    return cov / max(tot, 1)

def shuffle_within(groups, rng):
    out = []
    for lines in groups:
        flat = [w for ln in lines for w in ln]; rng.shuffle(flat); k = 0; g = []
        for ln in lines:
            g.append(flat[k:k + len(ln)]); k += len(ln)
        out.append(g)
    return out

def test(groups, dec, name, reps=20, out=print):
    rng = random.Random(77)
    real = measure_lines([[dec(w) for w in ln] for g in groups for ln in g])
    sims = [measure_lines([[dec(w) for w in ln] for g in shuffle_within(groups, rng) for ln in g]) for _ in range(reps)]
    m, sd = st.mean(sims), st.pstdev(sims)
    p = sum(x >= real for x in sims) / reps
    out(f"{name:58s} real {real:.1%} | embaralhado {m:.1%} ± {sd:.1%} | diferença {100*(real-m):+.1f} pts (P={p:.2f})")
    return real, m, sd, p

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "voynich"
    lang = sys.argv[2] if len(sys.argv) > 2 else "la"
    if mode == "voynich" and lang != "la":
        set_lang(lang)
        KEY = json.load(open(f"tabela3_real_{lang}.json"))["tabela"]
        dec = lambda w: decode_word(w, KEY)
        L, _ = parse("ZL.txt")
        HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}
        allp = [l for l in L if l.ltype[0] == "P" and l.folio not in HOLD]
        sample = random.Random(1404).sample([l.split for l in allp], 1600); sid = set(map(id, sample))
        pages = defaultdict(list)
        for l in allp:
            if id(l.split) not in sid: pages[l.folio].append(l.split)
        test(list(pages.values()), dec, f"Voynich, fora do treino (chave {lang})")
        for f in ("f4r", "f78r"):
            test([[l.split for l in L if l.folio == f and l.ltype[0] == "P"]], dec, f"Voynich {f} (chave {lang})")
    elif mode == "voynich":
        KEY = json.load(open("chave_final.json"))["tabela"]
        dec = lambda w: decode_word(w, KEY)
        L, _ = parse("ZL.txt")
        HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}
        allp = [l for l in L if l.ltype[0] == "P" and l.folio not in HOLD]
        sample = random.Random(1404).sample([l.split for l in allp], 1600); sid = set(map(id, sample))
        pages = defaultdict(list)
        for l in allp:
            if id(l.split) not in sid: pages[l.folio].append(l.split)
        test(list(pages.values()), dec, "Voynich, 20 mil palavras fora do treino (chave final)")
        for f in ("f4r", "f78r"):
            test([[l.split for l in L if l.folio == f and l.ltype[0] == "P"]], dec, f"Voynich {f}")
        NULL = json.load(open("tabela3_embaralhado.json"))["tabela"]
        test(list(pages.values()), lambda w: decode_word(w, NULL), "Voynich, fora do treino (chave nula)")
