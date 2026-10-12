"""Modelos de outras línguas-alvo (italiano e alemão, Europarl/NLTK) para repetir a busca da chave e o teste S′.
Normalização: minúsculas, acentos removidos, ß->ss, só a–z."""
import glob, json, math, os, re, unicodedata
from collections import Counter

from config import EUROPARL as EP
DIRS = {"it": "italian", "de": "german"}
from config import UD_TREEBANKS as UD
UDDIRS = {"ca": "UD_Catalan-AnCora", "fro": "UD_Old_French-SRCMF", "oc": "UD_Occitan-TTB"}

def norm(t):
    t = t.lower().replace("ß", "ss")
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c))

def read(lang):
    if lang in UDDIRS:
        out = []
        for f in sorted(glob.glob(UD + UDDIRS[lang] + "/*.conllu")):
            for line in open(f, encoding="utf-8"):
                if line.startswith("# text ="): out.append(norm(line[8:]))
        return re.findall(r"[a-z]+", " ".join(out))
    out = []
    for f in sorted(glob.glob(EP + DIRS[lang] + "/*")):
        raw = open(f, "rb").read()
        try: s = raw.decode("utf-8")
        except UnicodeDecodeError: s = raw.decode("latin-1")
        out.append(norm(s))
    return re.findall(r"[a-z]+", " ".join(out))

def model(lang):
    path = f"modelo_{lang}.json"
    if os.path.exists(path):
        d = json.load(open(path)); return d
    words = read(lang)
    s = "".join(words); alpha = sorted(set(s)); nh = min(200000, len(s) // 10); held = s[:nh]; tr = s[nh:]
    c3 = Counter(tr[i:i + 3] for i in range(len(tr) - 2)); c2 = Counter(tr[i:i + 2] for i in range(len(tr) - 1))
    V = len(alpha); k = 0.05
    LP = {a + b + c: math.log2((c3.get(a + b + c, 0) + k) / (c2.get(a + b, 0) + k * V)) for a in alpha for b in alpha for c in alpha}
    H = -sum(LP.get(held[i:i + 3], -20) for i in range(len(held) - 2)) / (len(held) - 2)
    wc = Counter(words)
    lex = {w: n for w, n in wc.items() if n >= 2 and re.search("[aeiouy]", w)}
    letters = [c for c, _ in Counter(s).most_common() if c in alpha]
    fin2 = [e for e, _ in Counter(w[-2:] for w in words if len(w) > 2).most_common(19)]
    d = {"lang": lang, "n_words": len(words), "LP": LP, "H": H, "lex": lex,
         "nonfinal": letters[:24], "final": letters[:14] + fin2}
    json.dump(d, open(path, "w"))
    return d

if __name__ == "__main__":
    import sys
    for lang in (sys.argv[1:] or ("it", "de")):
        d = model(lang)
        print(lang, "palavras", d["n_words"], "formas", len(d["lex"]), "H", round(d["H"], 3), "não-finais", d["nonfinal"], "finais", d["final"])
