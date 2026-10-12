# Fase 18 – Critérios registrados antes de rodar (não serão mudados depois)

Registrado pelo coordenador em 11/10/2026, antes de lançar os agentes. Única exposição prévia a resultados da Naibbe:
um teste de fumaça do código com Apício, semente 1 (usado só para verificar que o módulo funciona). Os critérios
abaixo são relativos ao manuscrito e não foram escolhidos para favorecer nem prejudicar esse caso.

## Pergunta
A cifra Naibbe (naibbe_v2.py + references/naibbe_tables.csv, parâmetros do autor, sem recalibrar), aplicada a textos
latinos reais, produz (P1) palavras estáveis e vocabulário natural e (P2) agrupamento lexical por trechos de páginas,
no nível do manuscrito?

## Régua
Dialeto B do manuscrito (a Naibbe foi calibrada sobre B; um desempenho pior em relação ao dialeto A não conta contra).
Intervalo de referência de cada métrica = [mínimo, máximo] da união de:
 (a) 10 subamostras de metade das páginas de B (mc.subamostras, frac = 0,5);
 (b) as seções de B com 3.000+ fichas: herbal B, biológica, receitas.
Sem alargamento adicional.

## Propriedades e métricas (definições em metricas_comuns.py)
- P1 – palavras estáveis e vocabulário natural: TTR, hapax, zipf.
- P2 – agrupamento por trechos: agrup_200, bloco8_200, viz_200 (páginas re-cortadas em 200 fichas para todos).
- P3 – superfície local (contexto, não decide): h2, compr, razao, F1esp, rep.

Um texto "passa" numa propriedade se a mediana entre as sementes de TODAS as suas métricas cair dentro do intervalo
de referência. "Falha" se ao menos uma métrica cair fora.

## Decisão (sobre os textos latinos; o italiano é informativo)
- A FAVOR da hipótese de cifra: 3 ou mais textos latinos passam em P1 e em P2.
- CONTRA: 3 ou mais textos latinos falham em P2.
- INCONCLUSIVO: qualquer outro caso.

## Efeito declarado nas estimativas de confiança (valores atuais: chave <1%, tradução <1%,
## texto gerado por regras ≈70%, livro de herbário/banhos/astrologia pelas figuras ≈35%)
- A FAVOR: "texto gerado por regras" cai para ≤50%; a confiança de que o texto contém a informação das figuras sobe
  de 10–15% para cerca de 25%; chave e tradução não mudam (nenhuma chave foi achada); interpretação do livro ±5.
- CONTRA: "texto gerado por regras" sobe para 75–80%; conteúdo cai para cerca de 10%; os demais não mudam.
- INCONCLUSIVO: nenhuma estimativa muda mais de 5 pontos.

## Sanidade das métricas
As métricas de P2 têm de separar o manuscrito do texto embaralhado entre páginas (o agrupamento deve cair a ~0).
Se não separarem, a métrica não serve e é retirada antes da decisão, com registro.
