"""Fase 8a – Qual tamanho de unidade cifrada reproduz o padrão 1 (o espaço que liga)?
Latim real é cifrado usando como 'livro de código' o PRÓPRIO vocabulário voynichiano (com as frequências reais),
de modo que a estrutura interna das palavras é idêntica à do Voynich. A única variável é o que cada palavra Voynich
representa: uma letra, um par de letras, uma sílaba ou uma palavra latina. Medimos o que sai."""
import math, random, re, glob, sys
from collections import Counter, defaultdict
from ivtff import parse, units
import lexicon

rng = random.Random(1420)

def mi(pairs):
    n = len(pairs); a = Counter(x for x, _ in pairs); b = Counter(y for _, y in pairs); ab = Counter(pairs)
    return sum(c / n * math.log2((c / n) / ((a[x] / n) * (b[y] / n))) for (x, y), c in ab.items())

def mi_net(pairs, k=5):
    base = []
    xs = [x for x, _ in pairs]; ys = [y for _, y in pairs]
    for _ in range(k):
        ys2 = ys[:]; rng.shuffle(ys2); base.append(mi(list(zip(xs, ys2))))
    return mi(pairs), sum(base) / k

def h2(seq):
    bi = Counter(zip(seq, seq[1:])); uni = Counter(seq[:-1]); n = sum(bi.values())
    return -sum(c / n * math.log2(c / uni[a]) for (a, b), c in bi.items())

def measure(lines, name, out=print):
    words = [w for ln in lines for w in ln]
    cross = [(a[-1], units(b)[0]) for ln in lines for a, b in zip(ln, ln[1:])]
    inner = [(units(w)[0], w[-1]) for w in words if len(units(w)) >= 3]
    c, cb = mi_net(cross); i, ib = mi_net(inner)
    seq = []
    for w in words: seq.extend(list(w)); seq.append("_")
    rep = sum(a == b for ln in lines for a, b in zip(ln, ln[1:])) / max(1, sum(len(ln) - 1 for ln in lines))
    cnt = Counter(words)
    hap = sum(1 for v in cnt.values() if v == 1) / len(cnt)
    r = {"n": len(words), "cross": c - cb, "inner": i - ib, "ratio": (c - cb) / max(i - ib, 1e-9),
         "ttr": len(cnt) / len(words), "hapax": hap, "h2": h2(seq), "rep": rep}
    out(f"{name:34s} n={r['n']:6d}  MI através {r['cross']:.3f}  MI dentro {r['inner']:.3f}  razão {r['ratio']:4.2f}  "
        f"TTR {r['ttr']:.3f}  hápax {r['hapax']:.0%}  h2 {r['h2']:.2f}  repetição {r['rep']:.2%}")
    return r

def syl(w):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", w) or [w]

def latin_text():
    files = sorted(glob.glob(lexicon.BASE + "isidore/*.txt"))
    txt = " ".join(lexicon.norm(open(f, encoding="utf-8", errors="ignore").read()) for f in files)
    return re.findall(r"[a-z]+", txt)

def make_units(kind, words, n_target):
    if kind == "palavra":
        return words[:n_target]
    if kind == "sílaba":
        out = []
        for w in words:
            out.extend(syl(w))
            if len(out) >= n_target: break
        return out[:n_target]
    stream = "".join(words[:n_target])          # contínuo, sem espaços (cifra verbosa sem fronteiras)
    if kind == "letra":
        return list(stream[:n_target])
    if kind == "par":
        s = "".join(words[:n_target * 2 // 5 + 10])
        return [s[i:i + 2] for i in range(0, len(s) - 1, 2)][:n_target]
    if kind == "letra+espaço":                  # letra, com a fronteira de palavra também cifrada como unidade
        s = "_".join(words)
        return list(s[:n_target])

def codebook(unit_freq, vfreq):
    """Distribui o vocabulário voynichiano entre as unidades latinas, equilibrando frequências (guloso por déficit)."""
    units_ = sorted(unit_freq, key=lambda u: -unit_freq[u]); V = sorted(vfreq, key=lambda w: -vfreq[w])
    TU = sum(unit_freq.values()); TV = sum(vfreq.values())
    book = defaultdict(list)
    if len(units_) <= len(V):
        import heapq
        got = Counter()
        for u, w in zip(units_, V):                 # cada unidade recebe ao menos uma grafia
            book[u].append(w); got[u] += vfreq[w] / TV
        heap = [(-(unit_freq[u] / TU - got[u]), u) for u in units_]; heapq.heapify(heap)
        for w in V[len(units_):]:
            d, u = heapq.heappop(heap)
            book[u].append(w); got[u] += vfreq[w] / TV
            heapq.heappush(heap, (-(unit_freq[u] / TU - got[u]), u))
    else:                                       # mais unidades que palavras: várias unidades por palavra
        import heapq
        heap = [(-vfreq[w] / TV, w) for w in V]; heapq.heapify(heap)
        got = Counter()
        for u in units_:
            d, w = heapq.heappop(heap)
            book[u].append(w); got[w] += unit_freq[u] / TU
            heapq.heappush(heap, (-(vfreq[w] / TV - got[w]), w))
    return book

def encode(units_seq, book, vfreq, line_len):
    choice = {u: (ws, [vfreq[w] for w in ws]) for u, ws in book.items()}
    out = [rng.choices(*choice[u])[0] for u in units_seq]
    lines = []; k = 0
    for L in line_len:
        if k >= len(out): break
        lines.append(out[k:k + L]); k += L
    return lines

if __name__ == "__main__":
    L, _ = parse("ZL.txt")
    vlines = [[w for w in l.split if "?" not in w] for l in L if l.ltype[0] == "P"]
    vlines = [ln for ln in vlines if ln]
    vfreq = Counter(w for ln in vlines for w in ln)
    N = sum(vfreq.values()); line_len = [len(ln) for ln in vlines]
    res = {}
    res["voynich"] = measure(vlines, "Voynich (ZL, texto corrido)")
    flat = [w for ln in vlines for w in ln]; rng.shuffle(flat); sh = []; k = 0
    for Ln in line_len: sh.append(flat[k:k + Ln]); k += Ln
    res["voynich_emb"] = measure(sh, "Voynich com palavras embaralhadas")
    words = latin_text()
    for kind in ("letra", "letra+espaço", "par", "sílaba", "palavra"):
        us = make_units(kind, words, N)
        uf = Counter(us)
        book = codebook(uf, vfreq)
        lines = encode(us, book, vfreq, line_len)
        res[kind] = measure(lines, f"latim cifrado, 1 palavra = {kind} ({len(uf)} tipos)")
    import json; json.dump(res, open("unidade_resultados.json", "w"), indent=1)
