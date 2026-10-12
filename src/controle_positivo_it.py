"""Controle positivo em italiano (Europarl): fluxo contínuo silabado, cifra por substituição de letras."""
import random, re
import lingua
rng = random.Random(8)
def syl(s):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", s)
words = lingua.read("it")[:12000]
stream = "".join(words); sy = syl(stream)
lines = [sy[i:i + 9] for i in range(0, len(sy), 9)][:1600]
letters = sorted(set(stream)); symbols = [f"S{i}" for i in range(len(letters))]; perm = symbols[:]; rng.shuffle(perm)
enc = dict(zip(letters, perm))
def encode(s):
    t = [enc[c] for c in s]; t[-1] = t[-1] + "$"; return tuple(t)
true_key = {}
for c, s in enc.items(): true_key[s] = c; true_key[s + "$"] = c
cipher_lines = [[encode(s) for s in ln] for ln in lines]
