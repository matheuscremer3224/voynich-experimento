"""Otimizador com restrição de injetividade (versão 2 da derivação da chave).
Motivo: a versão 1, sem restrição, colapsou numa solução degenerada (todos os finais -> '' e 6 letras para tudo),
que 'lê' qualquer coisa como a/e/an/en/ne. Restrições fixadas ANTES de ver qualquer tradução:
  * pedaços não-finais distintos -> letras latinas distintas (cada letra usada no máximo uma vez);
  * pedaços finais distintos -> terminações distintas; terminação vazia proibida.
Movimento: trocar o valor de um pedaço (se o valor já estiver em uso, os dois pedaços trocam entre si)."""
import random
from collections import defaultdict
from chave import segment

NONFINAL = list("abcdefghilmnopqrstux") + ["qu", "con", "per", "pro"]
FINAL = ["a", "e", "i", "o", "u", "s", "m", "t", "r", "n", "l", "c", "d", "x", "us", "um", "is", "es", "as", "os",
         "am", "em", "im", "ur", "it", "at", "et", "nt", "ent", "ant", "unt", "tur", "rum", "bus", "ibus", "orum",
         "arum", "que", "er", "or", "ar", "en", "on", "an", "in", "io", "ia", "ie", "ii"]

def cands(c):
    return FINAL if c.endswith("$") else NONFINAL

class Problem:
    def __init__(self, lines_tokens, tok_chunks, lex, chunk_list):
        types = sorted({t for ln in lines_tokens for t in ln}, key=str)
        self.tid = {t: i for i, t in enumerate(types)}
        self.tch = [tok_chunks(t) for t in types]
        self.lines = [[self.tid[t] for t in ln] for ln in lines_tokens]
        self.CH = list(chunk_list)
        self.by = defaultdict(list)
        for i, ch in enumerate(self.tch):
            if ch:
                for c in set(ch): self.by[c].append(i)
        self.lex = lex

    def dec(self, i, key):
        ch = self.tch[i]
        if ch is None: return None
        try: return "".join(key[c] for c in ch)
        except KeyError: return None

    def score(self, D):
        tot = cov = multi = 0
        for ln in self.lines:
            for j, i, f in segment([D[k] for k in ln], self.lex):
                tot += i - j
                if f:
                    cov += i - j
                    if i - j > 1: multi += i - j
        return cov / tot, multi / tot

    def random_key(self, r):
        key = {}
        for group in (False, True):
            cs = [c for c in self.CH if c.endswith("$") == group]
            vals = r.sample(FINAL if group else NONFINAL, len(cs))
            key.update(zip(cs, vals))
        return key

    def climb(self, key, log=print, maxpass=6, order=None):
        D = [self.dec(i, key) for i in range(len(self.tch))]
        best, bm = self.score(D)
        inv = {}
        for c, v in key.items(): inv[(c.endswith("$"), v)] = c
        for p in range(maxpass):
            improved = False
            for c in (order or self.CH):
                fin = c.endswith("$"); old = key[c]; cb = (best, None)
                for v in cands(c):
                    if v == old: continue
                    other = inv.get((fin, v))
                    key[c] = v
                    if other: key[other] = old
                    aff = set(self.by[c]) | (set(self.by[other]) if other else set())
                    saved = {i: D[i] for i in aff}
                    for i in aff: D[i] = self.dec(i, key)
                    s, m = self.score(D)
                    if s > cb[0] + 1e-9: cb = (s, v)
                    key[c] = old
                    if other: key[other] = v
                    for i, d in saved.items(): D[i] = d
                if cb[1] is not None:
                    v = cb[1]; other = inv.get((fin, v))
                    key[c] = v; inv[(fin, v)] = c
                    if other: key[other] = old; inv[(fin, old)] = other
                    else: inv.pop((fin, old), None)
                    for i in set(self.by[c]) | (set(self.by[other]) if other else set()): D[i] = self.dec(i, key)
                    best = cb[0]; improved = True
            bm = self.score(D)[1]
            log(f"  passe {p+1}: cobertura {best:.4f} (multipalavra {bm:.4f})")
            if not improved: break
        return key, best, bm
