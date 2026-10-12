# Fase 15 – Um gerador honesto reproduz o agrupamento?

[← Fase 14](fase-14.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 16 →](fase-16.md)

> **Em uma frase:** Sim: um gerador cujo vocabulário muda devagar de página em página chega perto do manuscrito em todas as medidas.

**A pergunta.** O agrupamento por trechos exige significado, ou um processo mecânico também o produz?

**O que foi feito.** O agente construiu um gerador que não copia palavra nenhuma do manuscrito. Cada seção tem um repertório de palavras inventadas pelo próprio gerador, e o peso de cada palavra muda devagar de uma página para a seguinte. Foram testadas 30 combinações de parâmetros.

**O que deu.** Uma das combinações chegou perto do Voynich em todas as medidas ao mesmo tempo: agrupamento por página +0,101 contra +0,109, vocabulário e entropia parecidos. Não é perfeito (sobram palavras-chave de página e as páginas vizinhas se parecem demais), mas basta para mostrar que o agrupamento não exige conteúdo.

**Por que importa.** O último argumento a favor de conteúdo deixou de ser evidência. A confiança em 'texto gerado por regras' subiu para cerca de 70%.

- **Código:** [`deriva_lexical.py`](../../src/deriva_lexical.py), [`deriva_lexical2.py`](../../src/deriva_lexical2.py)
- **Saídas:** [`results/fase-15/`](../../results/fase-15/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 15 – Um gerador honesto reproduz o agrupamento por trechos?

O último argumento a favor de conteúdo era o agrupamento lexical por trechos de páginas. Nenhum gerador sem conteúdo o tinha reproduzido sem quebrar outra medida. Construí então um gerador "honesto", que não copia palavra nenhuma do texto real.

Cada seção e dialeto tem um repertório de 3.000 a 6.000 tipos de palavra, gerados pela própria cadeia do G-casas2. O peso de cada tipo faz um passeio aleatório lento de uma página para a seguinte. Cada palavra do texto vem desse repertório (com probabilidade p, respeitando a regra de emenda) ou é nova, tirada da cadeia. Testei 30 combinações de três parâmetros:
- p, a fração de palavras vindas do repertório;
- o alcance da correlação, em páginas;
- σ, a força da deriva.

| | Agrupamento por página | Palavras-chave de página (acaso) | Vizinhas − distantes (cosseno) | Razão tipo/ocorrência | h2 | Agrupamento em blocos de 8 |
|---|---|---|---|---|---|---|
| Voynich | +0,109 | 20 (5,8) | 0,059 | 0,205 | 2,14 | +0,088 |
| Deriva lexical, p = 0,6, alcance 3 páginas, σ = 1,4 | +0,101 | 38 (6,1) | 0,080 | 0,193 | 2,16 | +0,107 |
| Deriva lexical, p = 0,4, alcance 3, σ = 1,7 | +0,085 | 41 (5,2) | 0,073 | 0,204 | 2,17 | +0,091 |
| Melhor autocitação com agrupamento ≥ 0,1 (Fase 10) | +0,133 | 115 (6,7) | 0,037 | 0,191 | 2,20 | – |

A deriva lexical lenta, sem conteúdo e sem cópia, chega perto do ponto do Voynich em todas as medidas ao mesmo tempo, coisa que a autocitação e o repertório com reforço não conseguiam. Não é um ajuste perfeito: ainda sobram palavras-chave (38 contra 20) e as vizinhas se parecem um pouco demais. Mas mostra que o agrupamento por trechos não exige conteúdo. Ele é o que se espera de um escriba cujas preferências de palavra mudam devagar ao longo da cópia. Um texto com significado e assunto que muda devagar também produziria esse agrupamento; o ponto é que ele deixou de ser evidência a favor do conteúdo.

---

[← Fase 14](fase-14.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 16 →](fase-16.md)
