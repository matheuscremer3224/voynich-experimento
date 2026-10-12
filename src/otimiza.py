"""Derivação da tabela (Fase 3): subida por coordenadas que maximiza a cobertura léxica latina no TREINO.
Depois de escolhida, a tabela é congelada em chave_final.json e não é mais tocada.
Uso: python3 otimiza.py real|embaralhado  (o modo 'embaralhado' é o controle nulo: mesmo otimizador, ordem das palavras destruída)."""
import json, math, random, sys, time
from collections import Counter, defaultdict
from ivtff import parse
from chave import chunks, candidates, NONFINAL, FINAL, segment
import lexicon

MODE = sys.argv[1] if len(sys.argv) > 1 else "real"
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 1
HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}   # páginas da Fase 4 e da Fase 5 ficam fora do treino
MINCH = 30
LEX = lexicon.load()

L, pv = parse("ZL.txt")
train = [l.split for l in L if l.ltype[0] == "P" and l.folio not in HOLD]
rng = random.Random(1438)
sample = list(train)
if MODE == "embaralhado":
    flat = [w for ws in sample for w in ws]; rng.shuffle(flat); out = []; k = 0
    for ws in sample:
        out.append(flat[k:k + len(ws)]); k += len(ws)
    sample = out

cc = Counter(c for ws in train for w in ws if chunks(w) for c in chunks(w))
CH = [c for c, n in cc.items() if n >= MINCH]
types = sorted({w for ws in sample for w in ws})
tid = {w: i for i, w in enumerate(types)}
tch = [chunks(w) for w in types]
lines = [[tid[w] for w in ws] for ws in sample]
by_chunk = defaultdict(list)
for i, ch in enumerate(tch):
    if ch:
        for c in set(ch): by_chunk[c].append(i)

def dec_type(i, table):
    ch = tch[i]
    if ch is None: return None
    try: return "".join(table[c] for c in ch)
    except KeyError: return None

def score(dec):
    cov = 0; multi = 0; tot = 0
    for ln in lines:
        d = [dec[i] for i in ln]
        for j, i, form in segment(d, LEX):
            tot += i - j
            if form:
                cov += i - j
                if i - j > 1: multi += i - j
    return cov / tot, multi / tot

def init_table(kind, r):
    t = {}
    if kind == "freq":
        lat_order = list("eiautsrnomcldpbqgfhx")
        nf = sorted([c for c in CH if not c.endswith("$")], key=lambda c: -cc[c])
        for k, c in enumerate(nf): t[c] = lat_order[k % len(lat_order)]
        for c in CH:
            if c.endswith("$"): t[c] = r.choice(["us", "um", "is", "a", "e", "it", "et", "es", "am", "em"])
    else:
        for c in CH: t[c] = r.choice(candidates(c))
    return t

def climb(table, log, maxpass=5):
    dec = [dec_type(i, table) for i in range(len(types))]
    best, bm = score(dec)
    for p in range(maxpass):
        improved = False
        order = sorted(CH, key=lambda c: -cc[c])
        for c in order:
            old = table[c]; cur_best = (best, old)
            for v in candidates(c):
                if v == old: continue
                table[c] = v
                for i in by_chunk[c]: dec[i] = dec_type(i, table)
                s, m = score(dec)
                if s > cur_best[0] + 1e-9: cur_best = (s, v)
            table[c] = cur_best[1]
            for i in by_chunk[c]: dec[i] = dec_type(i, table)
            if cur_best[1] != old:
                best = cur_best[0]; improved = True
        bm = score(dec)[1]
        log(f"  passe {p+1}: cobertura {best:.4f} (multipalavra {bm:.4f})")
        if not improved: break
    return table, best, bm

if __name__ == "__main__":
    r = random.Random(SEED)
    logf = open(f"log_otimiza_{MODE}_{SEED}.txt", "w")
    def log(s):
        print(s); logf.write(s + "\n"); logf.flush()
    log(f"modo={MODE} seed={SEED} pedaços otimizados={len(CH)} linhas={len(lines)} tipos={len(types)} léxico={len(LEX)}")
    results = []
    kinds = ["freq", "rand", "rand"] if SEED == 1 else ["rand", "rand", "rand"]
    for k, kind in enumerate(kinds):
        t0 = time.time()
        table, s, m = climb(init_table(kind, r), log)
        log(f"reinício {k} ({kind}): cobertura {s:.4f} multipalavra {m:.4f} [{time.time()-t0:.0f}s]")
        results.append((s, m, table))
    results.sort(key=lambda x: -x[0])
    s, m, table = results[0]
    json.dump({"modo": MODE, "seed": SEED, "cobertura_treino": s, "multipalavra_treino": m, "tabela": table,
               "todas": [(a, b) for a, b, _ in results]}, open(f"tabela_{MODE}_{SEED}.json", "w"), indent=1, ensure_ascii=False)
    log(f"MELHOR: {s:.4f} / multipalavra {m:.4f}")
