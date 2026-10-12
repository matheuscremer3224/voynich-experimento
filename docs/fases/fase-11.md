# Fase 11 – O texto acompanha as figuras?

[← Fase 10](fase-10.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 12 →](fase-12.md)

> **Em uma frase:** Páginas com plantas parecidas não têm texto parecido.

**A pergunta.** Se o texto fala das plantas desenhadas, páginas com desenhos parecidos têm vocabulário parecido?

**O que foi feito.** O agente mediu as cores de 112 páginas de plantas (área pintada, verde, azul, vermelho, ocre; flor azul no alto, raiz vermelha embaixo) e comparou com a semelhança do texto. Fez também um teste dirigido: alguma palavra aparece justamente nas páginas com certo traço? Antes, mediu o poder do teste, injetando uma palavra artificial.

**O que deu.** Correlação perto de zero em todos os recortes. Nenhuma palavra ligada a um traço resistiu à correção estatística. O teste acharia uma palavra assim em 86 a 90% das vezes.

**Por que importa.** Exclui um texto que descreva com regularidade as cores e partes desenhadas. Não exclui qualquer forma de descrição.

- **Código:** [`imagem_texto.py`](../../src/imagem_texto.py), [`imagem_palavras.py`](../../src/imagem_palavras.py), [`imagem_poder.py`](../../src/imagem_poder.py)
- **Saídas:** [`results/fase-11/`](../../results/fase-11/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 11 – O texto acompanha as figuras?

Se o texto fala das plantas desenhadas, páginas com plantas parecidas deveriam ter vocabulário parecido. Testei isso nas 112 páginas herbais de f1 a f66. Nesse trecho, a página do PDF é a página ZL + 2; conferi pelos números de fólio a lápis em f10r, f25r, f40r, f50r, f57r, f65r e f66r.

**Como medi a imagem.** Separei a pintura do pergaminho no espaço de cor Lab, tomando como referência a cor do pergaminho de cada página. Conferi as máscaras a olho em f1v, f2r, f3v e f9r. Daí tirei oito medidas: área pintada; proporções de verde, azul, vermelho e ocre; azul no terço superior (flores); cor quente no terço inferior (raízes); cor quente no topo.

**Como medi o texto.** Cosseno entre vetores tf-idf de palavras, com as grafias como estão e com as variantes fundidas.

**Resultado 1: semelhança geral.** A correlação entre semelhança de imagem e de texto (teste de Mantel, 2.000 permutações) ficou em torno de zero em todos os recortes:
- todos os pares: −0,028;
- mesmo dialeto, cadernos diferentes: +0,032 (P = 0,26);
- só A, cadernos diferentes: −0,003;
- mesmo caderno: +0,018.

Fundir as grafias não mudou nada. O desvio do nulo é 0,047, então um acoplamento acima de cerca de 0,1 está excluído.

**Resultado 2: palavra ligada a um traço visual.** Fiz também um teste dirigido, mais forte: alguma palavra aparece justamente nas páginas com flor azul, raiz vermelha ou ocre, topo vermelho ou ocre, ou planta grande? Usei teste exato de Fisher para cada palavra presente em 8 ou mais páginas. A correção para comparações múltiplas embaralha os traços entre páginas do mesmo caderno. Nenhuma associação resistiu:
- a melhor foi a palavra `d` com raiz vermelha (15 de 40 páginas contra 7 de 72; p corrigido 0,037–0,050), um entre oito testes;
- verifiquei que não é efeito do texto contornando o desenho: `d` não fica mais perto das interrupções de figura (12% contra 10%).

**Poder do teste.** Injetando uma palavra artificial, ele a acharia em 86–90% das vezes se ela estivesse em metade das páginas com o traço e em 10% das demais, e em 100% se estivesse em 70%.

**Conclusão da fase.** Não há sinal de que o texto descreva cor de flor ou de raiz, nem de que páginas de plantas parecidas tenham texto parecido. Não tenho um herbário ilustrado com texto conhecido para servir de controle positivo. Por isso, o que o resultado exclui é um texto que nomeie com regularidade as cores e partes desenhadas, não qualquer forma de descrição.

---

[← Fase 10](fase-10.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 12 →](fase-12.md)
