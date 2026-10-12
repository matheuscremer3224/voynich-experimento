# Fase 14 – Síntese

[← Fase 13](fase-13.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 15 →](fase-15.md)

> **Em uma frase:** O placar de todos os testes: o peso pende para um texto sem conteúdo linguístico recuperável.

**A pergunta.** Somando tudo, qual explicação os dados favorecem?

**O que foi feito.** O agente juntou os resultados das Fases 8 a 13 em três colunas: contra uma língua de tabela fixa, a favor de texto sem conteúdo, e a favor de conteúdo.

**O que deu.** Cerca de 65 contra 35 a favor de um texto sem conteúdo linguístico recuperável nas palavras. O que impedia de fechar a questão era o agrupamento por trechos.

**Por que importa.** Definiu o próximo alvo: um gerador honesto que reproduza o agrupamento sem copiar palavras do próprio texto.

- **Código:** nenhum (fase de texto e interpretação)
- **Saídas:** nenhuma (fase sem saídas de código)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 14 – Síntese

Desde a Fase 8, cada teste novo foi desenhado para separar "notação com significado" de "texto sem conteúdo linguístico". O placar ficou assim.

**Contra uma língua escrita por tabela fixa:**
- seis línguas (latim, italiano, alemão, catalão, francês antigo, occitano), com tabela única ou uma por dialeto: a ordem das palavras nunca importou mais do que +1,7 ponto;
- nos controles positivos, uma cifra desse tipo dá de +33 a +54 pontos.

**A favor de texto sem conteúdo** (ou de um conteúdo que não está nas palavras):
- um gerador de seis regras mecânicas imita quase toda a superfície do texto (Fase 10);
- os rótulos se comportam como os do gerador, não como nomes num texto real (Fase 10);
- o texto não acompanha as figuras, com um teste que tinha poder para isso (Fase 11);
- os rótulos farmacêuticos não coincidem com as palavras de cabeça do herbário (Fase 12);
- o vocabulário deriva devagar ao longo do códice, em vez de mudar a cada planta (Fase 13).

**A favor de algum conteúdo, ou de um processo que não consegui imitar:**
- o agrupamento lexical por trechos, no grau de um texto real, que meus geradores sem conteúdo não reproduziram sem quebrar outra medida (Fases 10 e 13).

**Minha posição final.** O peso das evidências está agora do lado de um texto sem conteúdo linguístico recuperável na palavra, em cerca de 65 contra 35. A forma mais econômica é um texto escrito por regras de aparência silábica, com convenções de linha e de parágrafo, e com um repertório de palavras que evolui ao longo da cópia. O mais provável é que tenha sido produzido para acompanhar um livro ilustrado de herbário, banhos e astrologia médica, com aparência de saber cifrado. O que impede de fechar a questão é o agrupamento lexical por trechos: um gerador melhor do que os meus precisa reproduzi-lo sem importar palavras do próprio texto.

**O que isso significa para a interpretação.** As figuras continuam dizendo o que o livro aparenta ser. A confiança nessa leitura das imagens fica em cerca de 35%. Mas a confiança de que o texto contenha essa informação em forma linguística cai para cerca de 15%.

### Resumo final (Fases 1 a 14)

**Hipótese:** comecei com um silabário homofônico sobre o latim. Foi refutado, junto com variantes em seis línguas e por dialeto. A hipótese mais econômica agora é um texto sem conteúdo linguístico, gerado por regras de aparência silábica, com um repertório de palavras que deriva ao longo da cópia.

**Melhor frase traduzida:** f2r.2 → *et eis cis* ("e, a eles, aquém"), sem valor de prova.

**Teste:** nenhuma chave passou no teste da ordem (≤ +1,7 ponto contra +33 a +54 nos controles positivos). O texto não acompanha as figuras, os rótulos não se comportam como nomes, e um gerador de seis regras imita quase toda a superfície.

**Confiança:** chave < 1%, tradução < 1%, texto sem conteúdo linguístico recuperável ≈ 65%, livro de herbário/banhos/astrologia médica pelas figuras ≈ 35%, texto contendo essa informação ≈ 15%.

**Ponto mais fraco:** o agrupamento lexical por trechos de páginas ainda não foi reproduzido por nenhum gerador sem conteúdo. Se um gerador honesto (sem copiar palavras do próprio texto) não conseguir reproduzi-lo, a balança volta a pender para o conteúdo.

---

[← Fase 13](fase-13.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 15 →](fase-15.md)
