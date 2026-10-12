"""Derivação v2 (com injetividade). Modos:
  real        – treino no texto Voynich em ordem real  -> gera a chave candidata
  embaralhado – controle nulo: mesmo treino com a ordem das palavras destruída
  positivo    – controle positivo: latim real cifrado por sílabas (cifra conhecida), mesmo otimizador
"""
import json, random, sys, time
from collections import Counter
from ivtff import parse
from chave import chunks
from otim_core import Problem
import lexicon

MODE = sys.argv[1]; RESTARTS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
LEX = lexicon.load()
HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}
rng = random.Random(1438)
logf = open(f"log2_{MODE}.txt", "w")
def log(s):
    print(s, flush=True); logf.write(s + "\n"); logf.flush()

def shuffle_lines(lines):
    flat = [w for ln in lines for w in ln]; rng.shuffle(flat); out = []; k = 0
    for ln in lines:
        out.append(flat[k:k + len(ln)]); k += len(ln)
    return out

if MODE in ("real", "embaralhado"):
    L, _ = parse("ZL.txt")
    lines = [l.split for l in L if l.ltype[0] == "P" and l.folio not in HOLD]
    if MODE == "embaralhado": lines = shuffle_lines(lines)
    cc = Counter(c for ln in lines for w in ln if chunks(w) for c in chunks(w))
    CH = [c for c, n in cc.items() if n >= 30]
    P = Problem(lines, chunks, LEX, CH)
    true_key = None
else:
    import controle_positivo as cp
    lines = cp.cipher_lines
    CH = sorted({x for ln in lines for w in ln for x in w})
    P = Problem(lines, lambda t: t, LEX, CH)
    true_key = cp.true_key
    log(f"chave verdadeira: {P.score([P.dec(i, true_key) for i in range(len(P.tch))])}")

log(f"modo={MODE} pedaços={len(CH)} linhas={len(lines)}")
res = []
r = random.Random(11)
for k in range(RESTARTS):
    t0 = time.time()
    key, s, m = P.climb(P.random_key(r), log)
    extra = ""
    if true_key: extra = f"; valores verdadeiros recuperados {sum(key[c] == true_key[c] for c in CH)}/{len(CH)}"
    log(f"reinício {k}: cobertura {s:.4f} multipalavra {m:.4f} [{time.time()-t0:.0f}s]{extra}")
    res.append((s, m, dict(key)))
res.sort(key=lambda x: -x[0])
json.dump({"modo": MODE, "cobertura_treino": res[0][0], "multipalavra_treino": res[0][1], "tabela": res[0][2],
           "todas": [(a, b) for a, b, _ in res]}, open(f"tabela2_{MODE}.json", "w"), indent=1, ensure_ascii=False)
log(f"MELHOR: {res[0][0]:.4f} / multipalavra {res[0][1]:.4f}")
