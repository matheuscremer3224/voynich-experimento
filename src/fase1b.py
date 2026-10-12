"""Fase 1b – dependências: entre casas da palavra e através do espaço."""
import math, random, re
from collections import Counter
from ivtff import parse, units
random.seed(7)
L, pv = parse("ZL.txt")
para = [l for l in L if l.ltype[0] == "P"]
def mi(pairs):
    n = len(pairs); a = Counter(x for x, _ in pairs); b = Counter(y for _, y in pairs); ab = Counter(pairs)
    return sum(c / n * math.log2((c / n) / ((a[x] / n) * (b[y] / n))) for (x, y), c in ab.items())
def mi_shuf(pairs, k=10):
    xs = [x for x, _ in pairs]; ys = [y for _, y in pairs]; r = []
    for _ in range(k):
        random.shuffle(ys); r.append(mi(list(zip(xs, ys))))
    return sum(r) / k
# 1) através do espaço: última letra da palavra n x primeira unidade da palavra n+1
cross = []
for l in para:
    ws = [w for w in l.split if "?" not in w]
    for a, b in zip(ws, ws[1:]):
        cross.append((a[-1], units(b)[0]))
print(f"MI(última letra de w_n ; 1ª unidade de w_n+1) = {mi(cross):.3f} bits; com pares embaralhados {mi_shuf(cross):.3f}")
# 2) dentro da palavra: prefixo (1ª unidade) x final (última letra), palavras com >=3 unidades
inner = []
for l in para:
    for w in l.split:
        u = units(w)
        if "?" not in w and len(u) >= 3: inner.append((u[0], w[-1]))
print(f"MI(1ª unidade ; última letra) dentro da palavra = {mi(inner):.3f} bits; embaralhado {mi_shuf(inner):.3f}")
# tabelas: o que segue -y, -n, -l, -r
c = Counter(cross)
for end in "ynlr":
    tot = sum(v for (x, y), v in c.items() if x == end)
    top = sorted(((v, y) for (x, y), v in c.items() if x == end), reverse=True)[:6]
    print(f"  depois de -{end} (n={tot}): " + ", ".join(f"{y} {100*v/tot:.0f}%" for v, y in top))
# latim
import fase1
lat = fase1.latin_words(60000)
lc = [(a[-1], b[0]) for a, b in zip(lat, lat[1:])]
print(f"Latim: MI(última letra; 1ª letra da seguinte) = {mi(lc):.3f}; embaralhado {mi_shuf(lc):.3f}")
li = [(w[0], w[-1]) for w in lat if len(w) >= 3]
print(f"Latim: MI(1ª letra; última) dentro da palavra = {mi(li):.3f}; embaralhado {mi_shuf(li):.3f}")
# 3) sílabas latinas: razão tipo/token se cada 'palavra' fosse uma sílaba
def syl(w):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", w) or [w]
sy = [s for w in lat for s in syl(w)][:38000]
print(f"Latim segmentado em sílabas: {len(sy)} tokens, TTR {len(set(sy))/len(sy):.3f}, tamanho médio {sum(map(len,sy))/len(sy):.2f}")
