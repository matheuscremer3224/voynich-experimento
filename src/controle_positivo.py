"""Controle positivo: o método consegue achar uma cifra silábica VERDADEIRA?
Latim real (Isidoro XVII) -> sílabas -> cada sílaba vira uma 'palavra' cifrada por substituição aleatória de letras
(com marca de posição final, como na chave). O mesmo otimizador e o mesmo segmentador são aplicados.
Mede: cobertura com a chave verdadeira, cobertura achada pelo otimizador, e ordem real x embaralhada."""
import random, re, json, sys, time
from collections import Counter, defaultdict
from chave import NONFINAL, FINAL, segment
import lexicon

LEX = lexicon.load()
BASE = lexicon.BASE
rng = random.Random(5)

def syl(w):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", w) or [w]

txt = lexicon.norm(open(BASE + "isidore/17.txt", encoding="utf-8", errors="ignore").read())
words = re.findall(r"[a-z]+", txt)
# linhas de ~8 'palavras' cifradas (sílabas), sem quebrar palavra latina entre linhas
lines = []; cur = []
for w in words:
    s = syl(w)
    if len(cur) + len(s) > 9 and cur:
        lines.append(cur); cur = []
    cur.extend(s)
    if len(lines) >= 1600: break
letters = sorted(set("".join(words)))
symbols = [f"S{i}" for i in range(len(letters))]
perm = symbols[:]; rng.shuffle(perm)
enc = dict(zip(letters, perm))
def encode(s):
    t = [enc[c] for c in s]; t[-1] = t[-1] + "$"; return tuple(t)
true_key = {}
for c, sname in enc.items():
    true_key[sname] = c; true_key[sname + "$"] = c
cipher_lines = [[encode(s) for s in ln] for ln in lines]

def cov(lines_, key):
    tot = c = m = 0
    for ln in lines_:
        d = []
        for w in ln:
            try: d.append("".join(key[x] for x in w))
            except KeyError: d.append(None)
        for j, i, f in segment(d, LEX):
            tot += i - j
            if f:
                c += i - j
                if i - j > 1: m += i - j
    return c / tot, m / tot

def shuffled(lines_):
    flat = [w for ln in lines_ for w in ln]; rng.shuffle(flat); out = []; k = 0
    for ln in lines_:
        out.append(flat[k:k + len(ln)]); k += len(ln)
    return out

if __name__ == "__main__":
    print("linhas", len(cipher_lines), "palavras cifradas", sum(map(len, cipher_lines)))
    print("chave verdadeira: real", cov(cipher_lines, true_key), " embaralhado", cov(shuffled(cipher_lines), true_key))
    # otimizador (mesma lógica de otimiza.py) partindo do acaso
    types = sorted({w for ln in cipher_lines for w in ln}); tid = {w: i for i, w in enumerate(types)}
    L2 = [[tid[w] for w in ln] for ln in cipher_lines]
    CH = sorted({x for w in types for x in w})
    by = defaultdict(list)
    for i, w in enumerate(types):
        for x in set(w): by[x].append(i)
    def dect(i, key):
        try: return "".join(key[x] for x in types[i])
        except KeyError: return None
    def score(dec):
        tot = c = 0
        for ln in L2:
            for j, i, f in segment([dec[k] for k in ln], LEX):
                tot += i - j
                if f: c += i - j
        return c / tot
    best_overall = None
    for rs in range(2):
        r = random.Random(100 + rs)
        key = {x: r.choice(FINAL if x.endswith("$") else NONFINAL) for x in CH}
        dec = [dect(i, key) for i in range(len(types))]; best = score(dec)
        for p in range(6):
            imp = False
            for x in CH:
                old = key[x]; cb = (best, old)
                for v in (FINAL if x.endswith("$") else NONFINAL):
                    if v == old: continue
                    key[x] = v
                    for i in by[x]: dec[i] = dect(i, key)
                    s = score(dec)
                    if s > cb[0] + 1e-9: cb = (s, v)
                key[x] = cb[1]
                for i in by[x]: dec[i] = dect(i, key)
                if cb[1] != old: best = cb[0]; imp = True
            print(f" reinício {rs} passe {p+1}: {best:.3f}", flush=True)
            if not imp: break
        acc = sum(key[x] == true_key[x] for x in CH) / len(CH)
        print(f"reinício {rs}: cobertura achada {best:.3f}; símbolos com valor verdadeiro {acc:.0%}")
        if best_overall is None or best > best_overall[0]: best_overall = (best, dict(key))
    key = best_overall[1]
    r_, m_ = cov(cipher_lines, key); rs_, ms_ = cov(shuffled(cipher_lines), key)
    print(f"chave achada: real {r_:.3f} (multi {m_:.3f})  embaralhado {rs_:.3f} (multi {ms_:.3f})")
    json.dump({"true_real": cov(cipher_lines, true_key), "true_shuf": cov(shuffled(cipher_lines), true_key),
               "found_real": (r_, m_), "found_shuf": (rs_, ms_)}, open("controle_positivo.json", "w"))
