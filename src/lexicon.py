"""Léxico latino de referência (formas atestadas) a partir de textos da Latin Library (cópia CLTK no GitHub).
Normalização medieval: minúsculas, j->i, v->u, ae/oe->e, y->i, k->c. Numerais romanos e cabeçalhos removidos."""
import glob, re, json, os
from collections import Counter

from config import LATIN_LIBRARY as BASE
OUT = os.path.join(os.path.dirname(__file__), "lexicon_latim.json")
ROMAN = re.compile(r"^m{0,4}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|u?i{0,3})$")
JUNK = ("the latin library", "the classics page", "christian latin", "medieval latin", "neo-latin")

def norm(t):
    t = t.lower().replace("j", "i").replace("v", "u").replace("æ", "e").replace("œ", "e")
    t = t.replace("ae", "e").replace("oe", "e").replace("y", "i").replace("k", "c")
    return t

def build():
    files = (glob.glob(BASE + "isidore/*.txt") + glob.glob(BASE + "columella/*.txt") + glob.glob(BASE + "apicius/*.txt")
             + glob.glob(BASE + "bible/*.txt") + glob.glob(BASE + "aquinas/*.txt") + glob.glob(BASE + "wmconches*.txt"))
    c = Counter()
    for f in files:
        for line in open(f, encoding="utf-8", errors="ignore"):
            if any(j in line.lower() for j in JUNK):
                continue
            for w in re.findall(r"[a-zA-Zæœ]+", line):
                w = norm(w)
                if ROMAN.match(w) and w not in ("di", "mi", "dic", "mix", "lic", "civ", "dim", "mil", "cid"):
                    if len(w) <= 4 or set(w) <= set("ivxlcdmu"):
                        continue
                c[w] += 1
    two = set("et in ad ut de ex si ab me eo se te ei ne id ea ac tu es at os an en re ob mi hi da is io do he di ha eu".split())
    lex = {w: n for w, n in c.items() if n >= 2 and re.search("[aeiou]", w)
           and (len(w) > 2 or w in ("a", "e", "o") or w in two)}
    json.dump({"n_tokens": sum(c.values()), "files": len(files), "lex": lex}, open(OUT, "w"))
    return lex

def load():
    if not os.path.exists(OUT):
        build()
    return json.load(open(OUT))["lex"]

if __name__ == "__main__":
    lex = build()
    d = json.load(open(OUT))
    print("arquivos", d["files"], "tokens", d["n_tokens"], "formas (freq>=2)", len(lex))
    print(sorted(lex.items(), key=lambda x: -x[1])[:40])
    print("2 letras:", sorted([w for w in lex if len(w) == 2], key=lambda w: -lex[w])[:60])
