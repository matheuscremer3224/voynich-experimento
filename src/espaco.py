"""Fase 8b – O espaço Voynich é fronteira de palavra ou quebra ortográfica?
1) Previsibilidade: tira os espaços e tenta recolocá-los só pelo contexto local de glifos (modelo treinado na metade
   par das linhas, testado na ímpar). Compara com o mesmo exercício em latim.
2) Tipo de dependência entre palavras vizinhas: junção (fim->começo), começo->começo, fim->fim."""
import math, random, re
from collections import Counter, defaultdict
from ivtff import parse, units
import fase1

rng = random.Random(5)

def stream_with_breaks(lines, tok):
    """lista de linhas; cada linha -> (lista de unidades, conjunto de posições com espaço depois da unidade i)"""
    out = []
    for ws in lines:
        us = []; br = set()
        for w in ws:
            us.extend(tok(w)); br.add(len(us) - 1)
        br.discard(len(us) - 1)
        out.append((us, br))
    return out

def feats(us, i, k):
    left = tuple(us[max(0, i - k + 1):i + 1]); right = tuple(us[i + 1:i + 1 + k])
    return left, right

def evaluate(data, k):
    train = data[0::2]; test = data[1::2]
    c = defaultdict(lambda: [0, 0])
    for us, br in train:
        for i in range(len(us) - 1):
            f = feats(us, i, k); c[f][1 if i in br else 0] += 1
    # recuo para contexto menor quando não visto
    c1 = defaultdict(lambda: [0, 0])
    for us, br in train:
        for i in range(len(us) - 1):
            f = (tuple(us[i:i + 1]), tuple(us[i + 1:i + 2])); c1[f][1 if i in br else 0] += 1
    tp = fp = fn = tn = 0; H = 0.0; n = 0
    for us, br in test:
        for i in range(len(us) - 1):
            f = feats(us, i, k)
            a, b = c[f] if f in c else c1[(tuple(us[i:i + 1]), tuple(us[i + 1:i + 2]))]
            p = (b + 0.5) / (a + b + 1)
            y = i in br
            pred = p > 0.5
            tp += pred and y; fp += pred and not y; fn += (not pred) and y; tn += (not pred) and not y
            H += -math.log2(p if y else 1 - p); n += 1
    prec = tp / max(tp + fp, 1); rec = tp / max(tp + fn, 1)
    base = (tp + fn) / n
    Hb = -(base * math.log2(base) + (1 - base) * math.log2(1 - base))
    return {"F1": 2 * prec * rec / max(prec + rec, 1e-9), "prec": prec, "rec": rec, "acc": (tp + tn) / n,
            "taxa_espaco": base, "bits_por_posicao": H / n, "bits_sem_contexto": Hb, "frac_incerteza_restante": (H / n) / Hb}

def mi(pairs):
    n = len(pairs); a = Counter(x for x, _ in pairs); b = Counter(y for _, y in pairs); ab = Counter(pairs)
    return sum(c / n * math.log2((c / n) / ((a[x] / n) * (b[y] / n))) for (x, y), c in ab.items())

def mi_net(pairs):
    xs = [x for x, _ in pairs]; ys = [y for _, y in pairs]; r = []
    for _ in range(5):
        y2 = ys[:]; rng.shuffle(y2); r.append(mi(list(zip(xs, y2))))
    return mi(pairs) - sum(r) / 5

if __name__ == "__main__":
    L, _ = parse("ZL.txt")
    for comma in ("split", "join"):
        V = [[w for w in (l.split if comma == "split" else l.join) if "?" not in w] for l in L if l.ltype[0] == "P"]
        V = [v for v in V if len(v) > 1]
        dv = stream_with_breaks(V, units)
        for k in (1, 2):
            r = evaluate(dv, k)
            print(f"Voynich (vírgula={comma}) contexto ±{k}: F1 {r['F1']:.3f} (precisão {r['prec']:.3f}, revocação {r['rec']:.3f}); "
                  f"incerteza restante {r['frac_incerteza_restante']:.0%} ({r['bits_por_posicao']:.3f} de {r['bits_sem_contexto']:.3f} bits)")
    lat = fase1.latin_words(60000)
    LL = [lat[i:i + 9] for i in range(0, len(lat), 9)]
    dl = stream_with_breaks(LL, list)
    for k in (1, 2, 3):
        r = evaluate(dl, k)
        print(f"Latim contexto ±{k}: F1 {r['F1']:.3f} (precisão {r['prec']:.3f}, revocação {r['rec']:.3f}); "
              f"incerteza restante {r['frac_incerteza_restante']:.0%}")
    # mesma quantidade de 'unidades' por palavra: latim com sílabas como 'palavras'
    def syl(w):
        return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", w) or [w]
    S = [[s for w in lat[i:i + 4] for s in syl(w)] for i in range(0, len(lat), 4)]
    ds = stream_with_breaks(S, list)
    for k in (1, 2):
        r = evaluate(ds, k)
        print(f"Latim com espaço entre SÍLABAS ±{k}: F1 {r['F1']:.3f}; incerteza restante {r['frac_incerteza_restante']:.0%}")
    # tipos de dependência entre vizinhos
    V = [[w for w in l.split if "?" not in w] for l in L if l.ltype[0] == "P"]
    def deps(lines, tok):
        j = [(w1[-1], tok(w2)[0]) for ln in lines for w1, w2 in zip(ln, ln[1:])]
        ff = [(tok(w1)[0], tok(w2)[0]) for ln in lines for w1, w2 in zip(ln, ln[1:])]
        ll = [(w1[-1], w2[-1]) for ln in lines for w1, w2 in zip(ln, ln[1:])]
        return mi_net(j), mi_net(ff), mi_net(ll)
    print("Voynich: MI junção (fim->começo) %.3f | começo->começo %.3f | fim->fim %.3f" % deps(V, units))
    print("Latim:   MI junção (fim->começo) %.3f | começo->começo %.3f | fim->fim %.3f" % deps(LL, list))
    # MI entre glifos adjacentes DENTRO da palavra, para comparação com a junção
    inside = [(u[i], u[i + 1]) for ln in V for w in ln for u in [units(w)] for i in range(len(u) - 1)]
    print("Voynich: MI entre unidades adjacentes dentro da palavra %.3f" % mi_net(inside))
    acr = [(units(w1)[-1], units(w2)[0]) for ln in V for w1, w2 in zip(ln, ln[1:])]
    print("Voynich: MI entre a última unidade e a primeira da seguinte %.3f" % mi_net(acr))
