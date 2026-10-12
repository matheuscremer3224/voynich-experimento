"""Fase 16 – Calibração: meus testes de significado (Fases 10–13) sobreviveriam a uma cifra homofônica com escolhas ao
acaso, do tipo proposto por Greshko (cifra 'Naibbe', 2025)? Implementação própria e simplificada, não a dele.
Texto com significado conhecido: Isidoro XII, XVI e XVII (rótulo = primeira palavra de cada parágrafo).
  N0  latim sem cifra
  N1  cada palavra latina cifrada inteira, letra a letra, com uma de 3 tabelas sorteada a cada letra (mesma palavra ->
      várias grafias); espaços entre palavras mantidos
  N2  estilo Naibbe: cada palavra partida ao acaso em pedaços de 1 ou 2 letras; cada pedaço vira uma 'palavra' cifrada
      por uma de 3 tabelas sorteadas (espaço entre pedaços)
Medidas: concentração e frequência dos rótulos ecoados; agrupamento por página (páginas de 300 palavras latinas);
palavras-chave de página; razão tipo/ocorrência."""
import random, re, statistics as st
from collections import Counter, defaultdict
import lexicon
from rotulos_especificidade import analyze
from agrupamento import clustering
from agrupamento2 import keywords

rng = random.Random(1420)
SYM = list("abcdefghiklmnopqrstuvxyz")
letters = list("abcdefghilmnopqrstuxz")
def make_tables(units_, k=3):
    tabs = []
    for _ in range(k):
        used = set(); t = {}
        for u in units_:
            while True:
                code = "".join(rng.choice(SYM) for _ in range(rng.choice([2, 3])))
                if code not in used: used.add(code); t[u] = code; break
        tabs.append(t)
    return tabs
T1 = make_tables(letters)
bigr = [a + b for a in letters for b in letters]
T2 = make_tables(letters + bigr)

def enc_word_N1(w):
    return "".join(rng.choice(T1)[c] for c in w if c in T1[0])

def enc_word_N2(w):
    out = []; i = 0
    while i < len(w):
        n = 2 if (i + 1 < len(w) and rng.random() < 0.5) else 1
        ch = w[i:i + n]; i += n
        if ch in T2[0]: out.append(rng.choice(T2)[ch])
    return out

def corpus():
    paras = []
    for book in ("12", "16", "17"):
        raw = open(lexicon.BASE + f"isidore/{book}.txt", encoding="utf-8", errors="ignore").read()
        for par in re.split(r"\[\d+\]", raw)[1:]:
            ws = re.findall(r"[a-z]+", lexicon.norm(par))
            if len(ws) >= 8: paras.append((book, ws))
    return paras

def build(mode, paras):
    text = defaultdict(list); labs = defaultdict(list); stream = defaultdict(list)
    for k, (book, ws) in enumerate(paras):
        def E(w):
            if mode == "N0": return [w]
            if mode == "N1": return [enc_word_N1(w)]
            return enc_word_N2(w)
        labs[k].extend(E(ws[0])); body = [x for w in ws[1:] for x in E(w)]
        text[k].extend(body); stream[book].extend(body)
    pages = []
    for book, toks in stream.items():
        size = 300 if mode != "N2" else 600
        for i in range(0, len(toks) - size, size):
            ch = toks[i:i + size]
            pages.append({"folio": f"{book}-{i}", "I": book, "L": "A", "lines": [("P", ch[j:j + 9], j == 0) for j in range(0, size, 9)]})
    return text, labs, pages

if __name__ == "__main__":
    paras = corpus()
    for mode, name in [("N0", "latim sem cifra"), ("N1", "homofônica por letra, palavras inteiras"), ("N2", "estilo Naibbe (pedaços de 1–2 letras)")]:
        text, labs, pages = build(mode, paras)
        a = analyze(text, labs, name, reps=50, out=lambda s: None)
        idx, n = clustering(pages)
        kw = []
        by = defaultdict(list)
        for pg in pages: by[pg["I"]].append((pg["folio"], [w for t, l, _ in pg["lines"] for w in l]))
        for g, pgs in by.items():
            o, e, nn, _ = keywords(pgs[:30], rng, reps=10); kw.append((o, e, nn))
        toks = [w for v in text.values() for w in v]
        print(f"{name:42s} rótulo ecoado: concentração {a['conc']:.3f} x fichas {a['conc_null']:.3f}, frequência {a['freq']:.0f} x {a['freq_null']:.0f} | "
              f"agrupamento {idx:+.3f} | palavras-chave {sum(x[0] for x in kw)} (acaso {sum(x[1] for x in kw):.1f}) de {sum(x[2] for x in kw)} | TTR {len(set(toks))/len(toks):.3f}")
