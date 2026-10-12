"""Controle positivo da variante S′: latim de Isidoro silabado como fluxo contínuo (sílabas atravessam as fronteiras de
palavra), cada sílaba cifrada por substituição de letras com marca de posição final. Linhas de ~9 sílabas."""
import random, re
import lexicon
rng = random.Random(6)
BASE = lexicon.BASE
def syl(s):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", s)
txt = lexicon.norm(open(BASE + "isidore/17.txt", encoding="utf-8", errors="ignore").read())
words = re.findall(r"[a-z]+", txt)
stream = "".join(words[:9000])
sy = syl(stream)
lines = [sy[i:i + 9] for i in range(0, len(sy), 9)][:1600]
letters = sorted(set(stream))
symbols = [f"S{i}" for i in range(len(letters))]; perm = symbols[:]; rng.shuffle(perm)
enc = dict(zip(letters, perm))
def encode(s):
    t = [enc[c] for c in s]; t[-1] = t[-1] + "$"; return tuple(t)
true_key = {}
for c, s in enc.items(): true_key[s] = c; true_key[s + "$"] = c
cipher_lines = [[encode(s) for s in ln] for ln in lines]
