"""Fase 8e – Testes de falsificação da R1 (homófonos) e do fecho de linha (-m)."""
import math, random
from collections import Counter, defaultdict
from ivtff import parse, units

L, pv = parse("ZL.txt")
P = [l for l in L if l.ltype[0] == "P"]

# R1: dentro da mesma mão, a proporção t/(k+t) (e sh/(ch+sh)) muda com a seção, nas MESMAS palavras-par?
def pair_counts(lines, x, y):
    wc = Counter(w for l in lines for w in l.split if "?" not in w)
    rows = {}
    for w, c in wc.items():
        u = units(w); idx = [i for i, g in enumerate(u) if g == x]
        if len(idx) != 1 or y in u: continue
        v = u[:]; v[idx[0]] = y; w2 = "".join(v)
        rows[(w, w2)] = (c, wc.get(w2, 0))
    return rows

def section_test(hand, x, y, minn=8):
    by = defaultdict(list)
    for l in P:
        if l.vars.get("H") == hand: by[l.vars.get("I")].append(l)
    secs = [s for s in by if sum(len(l.split) for l in by[s]) > 1500]
    if len(secs) < 2: return None
    tabs = {s: pair_counts(by[s], x, y) for s in secs}
    common = [k for k in tabs[secs[0]] if all(k in tabs[s] for s in secs)]
    common = [k for k in common if all(sum(tabs[s][k]) >= 3 for s in secs) and sum(sum(tabs[s][k]) for s in secs) >= minn]
    if not common: return None
    # Cochran–Mantel–Haenszel-like: proporção agregada por seção nas mesmas palavras-par
    out = {}
    for s in secs:
        a = sum(tabs[s][k][0] for k in common); b = sum(tabs[s][k][1] for k in common)
        out[s] = (a, b, a / (a + b))
    # qui² de homogeneidade 2xS
    A = sum(v[0] for v in out.values()); B = sum(v[1] for v in out.values()); N = A + B
    chi = 0
    for s, (a, b, _) in out.items():
        n = a + b
        for obs, tot in ((a, A), (b, B)):
            e = n * tot / N; chi += (obs - e) ** 2 / e
    return len(common), out, chi, len(secs) - 1

if __name__ == "__main__":
    print("R1 – proporção da 1ª forma, nas mesmas palavras-par, por seção, dentro de cada mão")
    for hand in ("1", "2", "3"):
        for x, y in (("k", "t"), ("ch", "sh"), ("o", "a"), ("l", "r")):
            r = section_test(hand, x, y)
            if r:
                n, out, chi, df = r
                print(f"  mão {hand} {x}/{y}: {n} pares; " + "; ".join(f"{s}: {v[2]:.2f} (n={v[0]+v[1]})" for s, v in out.items())
                      + f"; qui² {chi:.1f} com {df} g.l.")
    print("\nFecho de linha (-m)")
    end_m = []; long_mid_m = 0; long_mid_n = 0
    for l in P:
        ws = [w for w in l.split if "?" not in w]
        if len(ws) < 3: continue
        end_m.append((len("".join(ws)), ws[-1].endswith("m")))
    end_m.sort()
    q = len(end_m) // 4
    for i, name in enumerate(["linhas mais curtas", "2º quartil", "3º quartil", "linhas mais longas"]):
        part = end_m[i * q:(i + 1) * q]
        print(f"  {name:18s}: fim em -m {100*sum(m for _, m in part)/len(part):.1f}%  (média {sum(n for n,_ in part)/len(part):.0f} glifos)")
    # -m antes de uma interrupção de figura (<->) no meio da linha
    before_gap = Counter(); other_mid = Counter()
    for l in P:
        segs = [s for s in l.raw.split("<->")]
        if len(segs) < 2: continue
        from ivtff import clean_text, words_of
        for s in segs[:-1]:
            ws = words_of(clean_text(s), "split")
            if ws:
                before_gap["m" if ws[-1].endswith("m") else "x"] += 1
                for w in ws[:-1]: other_mid["m" if w.endswith("m") else "x"] += 1
    print(f"  palavra antes de uma interrupção de figura no meio da linha termina em -m: {100*before_gap['m']/sum(before_gap.values()):.1f}% "
          f"(n={sum(before_gap.values())}); demais palavras dessas linhas: {100*other_mid['m']/sum(other_mid.values()):.1f}%")
    # -m no fim de parágrafo vs fim de linha comum
    pend = [l for l in P if "<$>" in l.raw]; nend = [l for l in P if "<$>" not in l.raw]
    f = lambda ls: 100 * sum(1 for l in ls if l.split and l.split[-1].endswith("m")) / len(ls)
    print(f"  fim de parágrafo termina em -m: {f(pend):.1f}%  |  fim de linha comum: {f(nend):.1f}%")
