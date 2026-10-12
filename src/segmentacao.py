"""Fase 8c – Se o Voynich fosse latim com espaços em outro lugar, onde estariam os espaços?
Mesmo texto latino, cinco maneiras de cortar: palavra, sílaba, 'C*V' (corte depois de cada vogal), 'V+C*' (corte antes
de cada consoante inicial de sílaba... i.e. rima+ataque seguinte) e pedaços de 2 letras. Para cada corte: razão
MI(junção)/MI(dentro), previsibilidade do espaço, comprimento médio e razão tipo/ocorrência."""
import re, random, math
from collections import Counter
import fase1
from espaco import stream_with_breaks, evaluate, mi_net

def syl(w):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", w) or [w]

def cuts(words, kind):
    if kind == "palavra": return words
    s = "".join(words)
    if kind == "sílaba": return [x for w in words for x in syl(w)]
    if kind == "C*V (corte após vogal)": return re.findall(r"[^aeiou]*[aeiou]+", s)
    if kind == "V*C* (corte antes de vogal)": return re.findall(r"[aeiou]*[^aeiou]+", s)
    if kind == "sílaba sem fronteira de palavra": return [x for x in syl(s)]
    if kind == "2 letras": return [s[i:i + 2] for i in range(0, len(s) - 1, 2)]
    if kind == "3 letras": return [s[i:i + 3] for i in range(0, len(s) - 2, 3)]

if __name__ == "__main__":
    lat = fase1.latin_words(80000)
    for kind in ["palavra", "sílaba", "sílaba sem fronteira de palavra", "C*V (corte após vogal)", "V*C* (corte antes de vogal)", "2 letras", "3 letras"]:
        toks = [t for t in cuts(lat, kind) if t][:60000]
        lines = [toks[i:i + 9] for i in range(0, len(toks), 9)]
        j = [(a[-1], b[0]) for ln in lines for a, b in zip(ln, ln[1:])]
        inn = [(t[0], t[-1]) for t in toks if len(t) >= 3]
        mj, mw = mi_net(j), (mi_net(inn) if inn else float("nan"))
        ev = evaluate(stream_with_breaks(lines, list), 2)
        L = [len(t) for t in toks]
        print(f"{kind:34s} junção {mj:.3f}  dentro {mw:.3f}  razão {mj/mw if mw==mw and mw>0 else float('nan'):5.2f}  "
              f"F1 espaço {ev['F1']:.2f}  incerteza {ev['frac_incerteza_restante']:.0%}  compr {sum(L)/len(L):.2f}  TTR {len(set(toks))/len(toks):.3f}")
