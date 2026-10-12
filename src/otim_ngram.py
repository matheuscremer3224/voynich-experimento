"""Derivação v3: subida com trocas maximizando a verossimilhança de trigramas de letras latinas
(texto contínuo, sem espaços – como a hipótese S exige, pois o espaço Voynich é fronteira de sílaba).
Escore por letra = log2 P(c | duas anteriores) + H, onde H é a entropia cruzada do modelo em latim real;
assim o escore é neutro ao comprimento: só sobe se o texto decodificado for mais 'latino' que o acaso latino.
Uso: python3 otim_ngram.py positivo|real|embaralhado [reinícios]"""
import json, math, random, re, sys, time, glob
from collections import Counter, defaultdict
import lexicon

NONFINAL3 = list("abcdefghilmnopqrstux") + ["qu"]
FINAL3 = list("aeiousmtrnlcdx") + ["us", "um", "is", "es", "as", "os", "am", "em", "it", "at", "et", "nt",
                                    "ur", "er", "or", "ar", "en", "an", "in"]

def cands(c):
    return FINAL3 if c.endswith("$") else NONFINAL3

def train_trigrams():
    files = (glob.glob(lexicon.BASE + "isidore/*.txt") + glob.glob(lexicon.BASE + "columella/*.txt")
             + glob.glob(lexicon.BASE + "apicius/*.txt") + glob.glob(lexicon.BASE + "bible/*.txt"))
    txt = "".join(lexicon.norm(open(f, encoding="utf-8", errors="ignore").read()) for f in files)
    s = re.sub(r"[^a-z]", "", txt)
    alpha = sorted(set(s))
    held = s[:200000]; tr = s[200000:]
    c3 = Counter(tr[i:i + 3] for i in range(len(tr) - 2)); c2 = Counter(tr[i:i + 2] for i in range(len(tr) - 1))
    V = len(alpha); k = 0.05
    def lp(t):
        return math.log2((c3.get(t, 0) + k) / (c2.get(t[:2], 0) + k * V))
    LP = {a + b + c: lp(a + b + c) for a in alpha for b in alpha for c in alpha}
    H = -sum(LP.get(held[i:i + 3], -20) for i in range(len(held) - 2)) / (len(held) - 2)
    return LP, H

class NG:
    def __init__(self, lines_tokens, tok_chunks, chunk_list, LP, H):
        types = sorted({t for ln in lines_tokens for t in ln}, key=str)
        self.tid = {t: i for i, t in enumerate(types)}
        self.tch = [tok_chunks(t) for t in types]
        self.n = Counter(); self.pairs = Counter()
        for ln in lines_tokens:
            ids = [self.tid[t] for t in ln]
            for i in ids: self.n[i] += 1
            for a, b in zip(ids, ids[1:]): self.pairs[(a, b)] += 1
        self.CH = list(chunk_list); self.LP = LP; self.H = H
        self.by = defaultdict(set)
        for i, ch in enumerate(self.tch):
            if ch:
                for c in set(ch): self.by[c].add(i)
        self.pairs_of = defaultdict(list)
        for (a, b) in self.pairs: self.pairs_of[a].append((a, b)); self.pairs_of[b].append((a, b))
        self.letters = sum(1 for _ in [])

    def dec(self, i, key):
        ch = self.tch[i]
        if ch is None: return None
        try: return "".join(key[c] for c in ch)
        except KeyError: return None

    def s_int(self, d):
        if d is None: return 0.0
        LP, H = self.LP, self.H
        return sum(LP.get(d[j:j + 3], -20) + H for j in range(len(d) - 2))

    def s_bnd(self, a, b):
        if a is None or b is None: return 0.0
        s = a[-2:] + b[:2]
        LP, H = self.LP, self.H
        return sum(LP.get(s[j:j + 3], -20) + H for j in range(len(s) - 2))

    def full(self, key):
        D = [self.dec(i, key) for i in range(len(self.tch))]
        I = [self.s_int(d) for d in D]
        B = {p: self.s_bnd(D[p[0]], D[p[1]]) for p in self.pairs}
        tot = sum(self.n[i] * I[i] for i in range(len(D))) + sum(self.pairs[p] * B[p] for p in self.pairs)
        return D, I, B, tot

    def per_letter(self, D, tot):
        L = sum(self.n[i] * len(d) for i, d in enumerate(D) if d)
        return tot / max(L, 1)

    def random_key(self, r):
        key = {}
        for fin in (False, True):
            cs = [c for c in self.CH if c.endswith("$") == fin]
            key.update(zip(cs, r.sample(FINAL3 if fin else NONFINAL3, len(cs))))
        return key

    def climb(self, key, log=print, maxpass=8):
        D, I, B, tot = self.full(key)
        inv = {(c.endswith("$"), v): c for c, v in key.items()}
        for p in range(maxpass):
            improved = False
            for c in self.CH:
                fin = c.endswith("$"); old = key[c]; best = (0.0, None)
                for v in cands(c):
                    if v == old: continue
                    other = inv.get((fin, v))
                    key[c] = v
                    if other: key[other] = old
                    aff = self.by[c] | (self.by[other] if other else set())
                    delta = 0.0; newD = {}
                    for i in aff:
                        d = self.dec(i, key); newD[i] = d
                        delta += self.n[i] * (self.s_int(d) - I[i])
                    ps = set()
                    for i in aff: ps.update(self.pairs_of[i])
                    for (a, b) in ps:
                        da = newD.get(a, D[a]); db = newD.get(b, D[b])
                        delta += self.pairs[(a, b)] * (self.s_bnd(da, db) - B[(a, b)])
                    if delta > best[0] + 1e-9: best = (delta, v)
                    key[c] = old
                    if other: key[other] = v
                if best[1] is not None:
                    v = best[1]; other = inv.get((fin, v))
                    key[c] = v; inv[(fin, v)] = c
                    if other: key[other] = old; inv[(fin, old)] = other
                    else: inv.pop((fin, old), None)
                    D, I, B, tot = self.full(key); improved = True
            log(f"  passe {p+1}: escore/letra {self.per_letter(D, tot):+.3f}")
            if not improved: break
        return key, self.per_letter(D, tot)

def perturb(P, key, r, k=5):
    key = dict(key)
    inv = {(c.endswith("$"), v): c for c, v in key.items()}
    for _ in range(k):
        c = r.choice(P.CH); fin = c.endswith("$"); old = key[c]
        v = r.choice(cands(c))
        if v == old: continue
        other = inv.get((fin, v))
        key[c] = v; inv[(fin, v)] = c
        if other: key[other] = old; inv[(fin, old)] = other
        else: inv.pop((fin, old), None)
    return key

def ils(P, r, iters, log, true_key=None):
    """Busca local iterada: perturba a melhor chave e sobe de novo; aceita se melhorar."""
    quiet = lambda s: None
    best_key, best = P.climb(P.random_key(r), quiet)
    for it in range(iters):
        k2, s2 = P.climb(perturb(P, best_key, r, r.choice([3, 5, 8])), quiet)
        if s2 > best + 1e-9:
            best_key, best = k2, s2
        if it % 5 == 4:
            extra = f"; verdadeiros {sum(best_key[c] == true_key[c] for c in P.CH)}/{len(P.CH)}" if true_key else ""
            log(f"  iteração {it+1}: escore/letra {best:+.3f}{extra}")
    return best_key, best

if __name__ == "__main__":
    MODE = sys.argv[1]; R = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    ITERS = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    import os
    LANGM = os.environ.get("LANGM", "la")
    if LANGM == "la":
        LP, H = train_trigrams(); SUF = ""
    else:
        import lingua
        dm = lingua.model(LANGM); LP, H = dm["LP"], dm["H"]; SUF = "_" + LANGM
        NONFINAL3[:] = dm["nonfinal"]; FINAL3[:] = dm["final"]
    if os.environ.get("DIAL", "all") != "all": SUF += "_" + os.environ["DIAL"]
    if os.environ.get("NOHOMO") == "1":
        SUF += "_semR1"
        for extra in ["st", "nt", "tr", "ct", "ss", "ph", "th"]:
            if extra not in NONFINAL3: NONFINAL3.append(extra)
    logf = open(f"log3_{MODE}{SUF}.txt", "w")
    def log(s):
        print(s, flush=True); logf.write(s + "\n"); logf.flush()
    log(f"modelo de trigramas: H = {H:.3f} bits/letra")
    rng = random.Random(1438)
    def shuffle_lines(lines):
        flat = [w for ln in lines for w in ln]; rng.shuffle(flat); out = []; k = 0
        for ln in lines:
            out.append(flat[k:k + len(ln)]); k += len(ln)
        return out
    if MODE in ("positivo", "positivo2"):
        import importlib
        cp = importlib.import_module("controle_positivo" if MODE == "positivo" else "controle_positivo2")
        lines = cp.cipher_lines; CH = sorted({x for ln in lines for w in ln for x in w})
        P = NG(lines, lambda t: t, CH, LP, H); true_key = cp.true_key
        D, I, B, tot = P.full(true_key); log(f"chave verdadeira: escore/letra {P.per_letter(D, tot):+.3f}")
    else:
        from ivtff import parse
        from chave import chunks
        HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}
        L, _ = parse("ZL.txt")
        DIAL = os.environ.get("DIAL", "all")
        lines = [l.split for l in L if l.ltype[0] == "P" and l.folio not in HOLD and (DIAL == "all" or l.vars.get("L") == DIAL)]
        if DIAL != "all" and len(lines) < 1600:
            lines = lines * 1          # usa o que houver
        lines = random.Random(1404).sample(lines, min(int(os.environ.get("NTRAIN", 1600)), len(lines)))   # amostra fixa de treino
        if MODE == "embaralhado": lines = shuffle_lines(lines)
        cc = Counter(c for ln in lines for w in ln if chunks(w) for c in chunks(w))
        CH = [c for c, n in cc.items() if n >= 30]
        P = NG(lines, chunks, CH, LP, H); true_key = None
    r = random.Random(7); res = []
    for k in range(R):
        t0 = time.time()
        key, s = ils(P, r, ITERS, log, true_key)
        extra = f"; valores verdadeiros {sum(key[c] == true_key[c] for c in CH)}/{len(CH)}" if true_key else ""
        log(f"reinício {k}: escore/letra {s:+.3f} [{time.time()-t0:.0f}s]{extra}")
        res.append((s, dict(key)))
    res.sort(key=lambda x: -x[0])
    json.dump({"modo": MODE, "escore_por_letra": res[0][0], "H": H, "tabela": res[0][1], "todas": [a for a, _ in res]},
              open(f"tabela3_{MODE}{SUF}.json", "w"), indent=1, ensure_ascii=False)
    log(f"MELHOR: {res[0][0]:+.3f}")
