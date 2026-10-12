"""Motor da chave: hipótese S ("silabário verboso homofônico sobre latim").

Regras fixas (não mudam depois de congeladas):
  R1 Homófonos: t=k, f=p, sh=ch, cth=cph=cfh=ckh (classes com contexto ~idêntico e razão estável dentro de cada escriba).
  R2 Pedaços: série de i + consoante seguinte (iin, ir...) = 1 pedaço; série de e (e/ee/eee) = 1 pedaço; dy final = 1 pedaço;
     demais unidades = 1 pedaço. O primeiro pedaço 'o' ou 'y' ganha marca de início (^); o último pedaço ganha marca de fim ($).
  R3 Cada pedaço vira uma cadeia latina pela tabela (TABELA). Pedaço sem entrada na tabela -> palavra não resolvida.
  R4 Uma palavra Voynich = uma sílaba (ou grupo de letras) do latim. Uma palavra latina = 1 a 4 palavras Voynich seguidas,
     dentro da mesma linha. A segmentação é escolhida por programação dinâmica que maximiza o número de palavras Voynich
     cobertas por formas latinas atestadas (empate: forma mais frequente).
  R5 Estado: 'lida' = forma latina com frequência >= 5 no corpus de referência; 'incerta' = frequência 2-4;
     'não resolvida' = sem forma atestada.
"""
import json, math, os, re
from functools import lru_cache
from ivtff import units

HOMO = {"t": "k", "f": "p", "sh": "ch", "cth": "ckh", "cph": "ckh", "cfh": "ckh"}
if os.environ.get("NOHOMO") == "1":      # Fase 9: a R1 caiu, então nenhum glifo é fundido com outro
    HOMO = {}
KNOWN = set("q o a e d l r s ch k p ckh y i n m g".split()) | ({"t", "f", "sh", "cth", "cph", "cfh"} if os.environ.get("NOHOMO") == "1" else set())

def normalize_units(w):
    return [HOMO.get(u, u) for u in units(w)]

@lru_cache(maxsize=None)
def chunks(w):
    u = normalize_units(w)
    if any(x not in KNOWN for x in u):
        return None                                   # ligadura, raro, ilegível
    out = []; i = 0
    while i < len(u):
        x = u[i]
        if x == "i":
            j = i
            while j < len(u) and u[j] == "i": j += 1
            run = "i" * min(j - i, 3)
            if j < len(u) and u[j] in ("n", "r", "l", "m", "s", "d"):
                out.append(run + u[j]); i = j + 1
            else:
                out.append(run); i = j
        elif x == "e":
            j = i
            while j < len(u) and u[j] == "e": j += 1
            out.append("e" * min(j - i, 3)); i = j
        elif x == "d" and i == len(u) - 2 and u[i + 1] == "y":
            out.append("dy"); i += 2
        else:
            out.append(x); i += 1
    if out and out[0] in ("o", "y") and len(out) > 1:
        out[0] = out[0] + "^"
    out[-1] = out[-1] + "$"
    return tuple(out)

NONFINAL = list("abcdefghilmnopqrstux") + ["qu", "con", "per", "pro"]
FINAL = ["", "a", "e", "i", "o", "u", "s", "m", "t", "r", "n", "l", "c", "d", "x", "us", "um", "is", "es", "as", "os",
         "am", "em", "im", "ur", "it", "at", "et", "nt", "ent", "ant", "unt", "tur", "rum", "bus", "ibus", "orum",
         "arum", "que", "er", "or", "ar", "en", "on", "an", "in", "io", "ia", "ie", "ii"]

def candidates(chunk):
    return FINAL if chunk.endswith("$") else NONFINAL

def decode_word(w, table):
    ch = chunks(w)
    if ch is None: return None
    try:
        return "".join(table[c] for c in ch)
    except KeyError:
        return None

def segment(dec, lex, maxg=4):
    """dec: lista de cadeias decodificadas (ou None) de uma linha. Devolve lista de grupos (i, j, forma ou None)."""
    n = len(dec)
    best = [(-1.0, None)] * (n + 1); best[0] = (0.0, None)
    for i in range(1, n + 1):
        cand = (best[i - 1][0], (i - 1, None))           # palavra i não coberta
        s = ""
        for j in range(i - 1, max(-1, i - 1 - maxg), -1):
            if dec[j] is None: break
            s = dec[j] + s
            f = lex.get(s)
            if f:
                sc = best[j][0] + (i - j) + 0.001 * math.log10(f)
                if sc > cand[0]: cand = (sc, (j, s))
        best[i] = cand
    groups = []; i = n
    while i > 0:
        j, form = best[i][1]
        groups.append((j, i, form)); i = j
    return groups[::-1]

def status(form, lex):
    if form is None: return "não resolvida"
    return "lida" if lex[form] >= 5 else "incerta"

def coverage(lines_words, table, lex):
    tot = cov = multi = 0
    for ws in lines_words:
        dec = [decode_word(w, table) for w in ws]
        for j, i, form in segment(dec, lex):
            tot += i - j
            if form:
                cov += i - j
                if i - j > 1: multi += i - j
    return cov / max(tot, 1), multi / max(tot, 1), tot

def save(table, path):
    json.dump(table, open(path, "w"), indent=1, ensure_ascii=False)

def load(path):
    return json.load(open(path))
