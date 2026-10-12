"""Controle com significado conhecido: Isidoro, Etimologias XII (animais), XVI (pedras) e XVII (plantas).
Cada parágrafo numerado '[n]' vira uma 'página'; o rótulo é a primeira palavra (em geral o nome da coisa descrita),
retirada do texto. Mede eco e concentração ('lift') com as mesmas funções usadas no Voynich."""
import re
from collections import defaultdict
import lexicon
from rotulos_especificidade import analyze, lift_test
text = defaultdict(list); labs = defaultdict(list); k = 0
for book in ("12", "16", "17"):
    raw = open(lexicon.BASE + f"isidore/{book}.txt", encoding="utf-8", errors="ignore").read()
    for par in re.split(r"\[\d+\]", raw)[1:]:
        ws = re.findall(r"[a-z]+", lexicon.norm(par))
        if len(ws) < 8: continue
        k += 1; labs[k].append(ws[0]); text[k].extend(ws[1:])
print("parágrafos-página:", k)
analyze(text, labs, "Isidoro (rótulo = nome da coisa descrita)")
lift_test(text, labs, "Isidoro (rótulo = nome da coisa descrita)")
