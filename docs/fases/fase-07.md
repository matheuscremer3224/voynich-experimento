# Fase 7 – Veredito do desafio original

[← Fase 6](fase-06.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 8 →](fase-08.md)

> **Em uma frase:** Confiança para a chave, a tradução e a interpretação, e o que derrubaria a hipótese.

**A pergunta.** Quanto confiar em cada resultado, e qual o próximo experimento?

**O que foi feito.** O agente deu níveis de confiança e listou o que derrubaria a hipótese e o que testar a seguir.

**O que deu.** Chave cerca de 2%, tradução abaixo de 1%, interpretação geral cerca de 40% (pelas figuras). A hipótese S foi rebaixada para cerca de 5%. O padrão que a motivou (o espaço que liga) continuou de pé e pediu novos testes.

**Por que importa.** Aqui terminava o desafio de 7 fases. Com o 'continue', a investigação seguiu pelas perguntas deixadas em aberto.

- **Código:** nenhum (fase de texto e interpretação)
- **Saídas:** nenhuma (fase sem saídas de código)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 7 – Veredito

Na **chave**, minha confiança é muito baixa, cerca de 2%: o teste decisivo falhou, e o controle positivo mostra que, com a hipótese certa e uma chave certa, a diferença seria de dezenas de pontos. Na **tradução**, a confiança é praticamente nula, abaixo de 1%: as formas "lidas" são palavras curtas e frequentes que o texto embaralhado também produz. Na **interpretação**, ela é moderada (cerca de 40%) quanto à função geral do livro, porque se apoia nas figuras e na estrutura, não na chave, e baixa (cerca de 15%) quanto a autoria e público. A **hipótese S** em si (palavra Voynich = sílaba latina com homófonos) eu rebaixo para cerca de 5%. O padrão que a motivou continua de pé (o espaço liga mais do que separa), mas a forma "sílaba de latim" não produziu a assinatura que deveria.

O que derrubaria a hipótese, em parte já derrubou: a falta de leituras de várias sílabas que dependam da ordem é a refutação que obtive para a minha chave. Ela cai de vez se uma derivação mais forte, com um modelo de palavras latinas e não só de trigramas, também não abrir distância entre o texto real e o embaralhado. A R1 cai se a proporção entre `k` e `t`, ou entre `ch` e `sh`, mudar de forma sistemática com o assunto dentro da mesma mão, porque aí eles seriam letras e não grafias. E o "sinal de fecho" deixa de ser posicional se `-m` aparecer no meio de linhas longas tanto quanto no fim.

O próximo experimento seria construir geradores silábicos homofônicos (de 2 a 4 grafias por sílaba) sobre latim, italiano do norte e occitano ou catalão (por causa dos meses), e ver se algum deles reproduz ao mesmo tempo os cinco padrões da Fase 1: h2 perto de 2,2, mais informação através do espaço do que dentro da palavra, razão tipo/ocorrência de 0,21, o fecho de linha e a divisão A/B. Se nenhum reproduzir o primeiro padrão sem estragar os outros, a família de hipóteses silábicas está descartada, e a próxima candidata seria a H3, um código de tabela em que o espaço separa campos e não sílabas.

### Resumo

**Hipótese:** o Voynich seria um silabário verboso e homofônico sobre o latim (palavra = sílaba; `k`/`t`, `ch`/`sh`, `p`/`f` e as bancadas são grafias de um mesmo valor; A e B são tabelas de escribas diferentes).

**Melhor frase traduzida:** f2r.2 `s<->shor.cthy` (com a interrupção de figura `<->` valendo espaço) → *et eis cis* → "e, a eles, aquém", três palavras lidas seguidas que não formam oração.

**Teste:** no trecho novo f78r, 24,1% de palavras válidas contra 21,9% com a ordem embaralhada (f4r: 39,1% contra 39,1%; fora do treino: 23,0% contra 22,5%), quando um latim cifrado de verdade daria 77% contra 48%.

**Confiança:** chave ≈ 2%, tradução < 1%, interpretação geral ≈ 40%.

**Ponto mais fraco:** a chave lê o texto embaralhado tão bem quanto o original. As suas "palavras lidas" são palavras latinas curtas e frequentes postas uma a uma, não latim.

---

[← Fase 6](fase-06.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 8 →](fase-08.md)
