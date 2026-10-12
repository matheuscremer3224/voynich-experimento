"""Fase 9 – teste da ordem para uma chave qualquer (por dialeto e por língua).
Uso: [NOHOMO=1] python3 teste_ordem.py <tabela.json> <dialeto A|B|all> <língua la|it|de|ca|fro|oc> <NTRAIN usado no treino>
Linhas de teste = parágrafos do dialeto fora das páginas reservadas e fora da amostra de treino (mesma semente).
Métricas: S′ (letras cobertas por palavras de 4+ letras, segmentação contínua) e R4 (palavras Voynich cobertas por
formas atestadas, agrupando palavras Voynich inteiras). Controle: palavras embaralhadas dentro de cada página."""
import json, random, statistics as st, sys
from collections import defaultdict
from ivtff import parse
from chave import decode_word, segment
import sprime, lexicon

keyf, dial, lang, ntrain = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
KEY = json.load(open(keyf))["tabela"]
sprime.set_lang(lang)
LEXL = lexicon.load() if lang == "la" else __import__("lingua").model(lang)["lex"]
L, _ = parse("ZL.txt")
HOLD = {"f1r", "f2r", "f71r", "f103r", "f4r", "f78r"}
cand = [l for l in L if l.ltype[0] == "P" and l.folio not in HOLD and (dial == "all" or l.vars.get("L") == dial)]
lines_all = [l.split for l in cand]
sample = random.Random(1404).sample(lines_all, min(ntrain, len(lines_all))); sid = set(map(id, sample))
pages = defaultdict(list)
for l in cand:
    if id(l.split) not in sid: pages[l.folio].append(l.split)
for f in HOLD - {"f1r", "f2r", "f71r", "f103r"}:          # f4r (A) e f78r (B) também entram, se forem do dialeto
    ls = [l for l in L if l.folio == f and l.ltype[0] == "P" and (dial == "all" or l.vars.get("L") == dial)]
    if ls: pages[f] = [l.split for l in ls]
groups = list(pages.values())
dec = lambda w: decode_word(w, KEY)

def r4(groups_):
    tot = cov = 0
    for g in groups_:
        for ws in g:
            d = [dec(w) for w in ws]
            for j, i, f in segment(d, LEXL):
                tot += i - j; cov += (i - j) if f else 0
    return cov / tot

rng = random.Random(31)
n = sum(len(ws) for g in groups for ws in g)
print(f"chave {keyf} | dialeto {dial} | língua {lang} | {n} palavras de teste")
sprime.test(groups, dec, "  S′ (segmentação contínua)", reps=20)
real = r4(groups)
sims = [r4(sprime.shuffle_within(groups, rng)) for _ in range(20)]
m, sd = st.mean(sims), st.pstdev(sims)
print(f"  R4 (palavras Voynich inteiras)                             real {real:.1%} | embaralhado {m:.1%} ± {sd:.1%} | diferença {100*(real-m):+.1f} pts (P={sum(x>=real for x in sims)/20:.2f})")
