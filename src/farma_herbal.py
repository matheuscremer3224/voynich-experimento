"""Fase 12 – Os rótulos da seção farmacêutica (desenhos de raízes, folhas e frascos) são nomes de plantas do herbário?
Se a primeira palavra de cada página herbal for o nome da planta (como nos herbários da época), rótulos farmacêuticos
deveriam coincidir com essas 'palavras de cabeça' mais do que rótulos de outras seções (zodíaco, astronomia, cosmologia),
que têm a mesma morfologia de rótulo mas outro assunto. Três critérios de igualdade, fixados antes de rodar:
  exata; grafias fundidas (t=k, f=p, sh=ch, bancadas, séries de e/i); 'miolo' (grafias fundidas, sem o primeiro e o
  último pedaço – desconta um ornamento inicial de parágrafo e a terminação).
Medida: fração dos rótulos de cada grupo que coincide com alguma palavra de cabeça herbal; e a mesma fração contra
palavras herbais comuns (não de cabeça). Significância por permutação dos rótulos entre os grupos."""
import random, re
from collections import Counter, defaultdict
from ivtff import parse, units

def skel(w):
    w = re.sub(r"c[tpf]h", "ckh", w).replace("sh", "ch").replace("t", "k").replace("f", "p")
    return re.sub(r"e+", "e", re.sub(r"i+", "i", w))

def core(w):
    u = units(skel(w))
    return "".join(u[1:-1]) if len(u) >= 4 else None

L, pv = parse("ZL.txt")
heads = []; herbal_other = Counter(); seen = set()
for l in L:
    if pv[l.folio].get("I") != "H" or l.ltype[0] != "P": continue
    ws = [w for w in l.split if "?" not in w]
    if not ws: continue
    if l.folio not in seen:
        seen.add(l.folio); heads.append(ws[0]); rest = ws[1:]
    else:
        rest = ws
    herbal_other.update(rest)
labels = defaultdict(list)
for l in L:
    if l.ltype[0] == "L":
        sec = pv[l.folio].get("I")
        for w in l.split:
            if "?" not in w and len(units(w)) >= 3: labels[sec].append(w)
groups = {"farmacêutica": labels["P"], "zodíaco+astron.+cosmol.": labels["Z"] + labels["A"] + labels["C"]}
print(f"palavras de cabeça herbais: {len(heads)} | rótulos: " + ", ".join(f"{g} {len(v)}" for g, v in groups.items()))

crit = {"exata": lambda w: w, "grafias fundidas": skel, "miolo": core}
rng = random.Random(12)
for cname, fn in crit.items():
    H = {fn(w) for w in heads if fn(w)}
    O = {fn(w) for w in herbal_other if fn(w) and herbal_other[w] >= 1} - H
    def rate(ws, S):
        xs = [fn(w) for w in ws]; xs = [x for x in xs if x]
        return sum(x in S for x in xs) / max(len(xs), 1)
    a, b = groups["farmacêutica"], groups["zodíaco+astron.+cosmol."]
    ra, rb = rate(a, H), rate(b, H)
    oa, ob = rate(a, O), rate(b, O)
    pool = a + b; diffs = []
    for _ in range(5000):
        rng.shuffle(pool); diffs.append(rate(pool[:len(a)], H) - rate(pool[len(a):], H))
    p = (1 + sum(d >= ra - rb for d in diffs)) / 5001
    print(f"[{cname:16s}] coincidem com palavra de cabeça herbal: farmacêutica {ra:.1%} x outros rótulos {rb:.1%} (P = {p:.3f}) | "
          f"com palavra herbal comum: {oa:.1%} x {ob:.1%} | razão cabeça/comum: {ra/max(oa,1e-9):.2f} x {rb/max(ob,1e-9):.2f}")
    if cname == "exata":
        print("   coincidências exatas da farmacêutica:", sorted({w for w in a if w in H}))
