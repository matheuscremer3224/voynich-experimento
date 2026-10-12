"""Controle positivo genérico (chave verdadeira): texto da língua silabado como fluxo contínuo e cifrado por
substituição de letras; mede a diferença real x embaralhado na métrica S′ com o léxico da própria língua.
Uso: python3 controle_positivo_lang.py ca fro oc"""
import random, re, sys
import lingua, sprime
def syl(s):
    return re.findall(r"[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?", s)
for lang in sys.argv[1:]:
    rng = random.Random(9)
    words = lingua.read(lang)[-12000:]          # trecho do FIM do corpus (o léxico vem do corpus todo)
    sy = syl("".join(words)); lines = [sy[i:i + 9] for i in range(0, len(sy), 9)][:1600]
    sprime.set_lang(lang)
    groups = [lines[i:i + 20] for i in range(0, len(lines), 20)]
    sprime.test(groups, lambda w: w, f"Controle positivo {lang}, chave verdadeira", reps=10)
