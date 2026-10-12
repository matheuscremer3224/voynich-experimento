# Fase 9 – Tabelas por dialeto e mais três línguas

[← Fase 8](fase-08.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 10 →](fase-10.md)

> **Em uma frase:** Uma tabela para cada dialeto e três línguas medievais novas: nada aparece.

**A pergunta.** A leitura falha porque A e B precisam de tabelas diferentes, ou porque a língua é outra?

**O que foi feito.** O agente derivou do zero uma tabela só para o dialeto A e outra só para o B, e tabelas para catalão, francês antigo e occitano. Antes, rodou o controle positivo de cada língua.

**O que deu.** Nos controles, o método enxergaria uma cifra desse tipo (diferença de 33 a 45 pontos). No Voynich, a diferença ficou entre 0,0 e 1,7 ponto em todas as variantes.

**Por que importa.** A família de silabários de tabela fixa ficou descartada em seis línguas. Sobraram duas explicações: uma notação com significado que nenhuma tabela fixa capta, ou um texto sem conteúdo linguístico.

- **Código:** [`teste_ordem.py`](../../src/teste_ordem.py), [`controle_positivo_lang.py`](../../src/controle_positivo_lang.py), [`lingua.py`](../../src/lingua.py), [`otim_ngram.py`](../../src/otim_ngram.py)
- **Saídas:** [`results/fase-09/`](../../results/fase-09/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 9 – Tabelas por dialeto e mais três línguas

Na Fase 8 a R1 caiu: `k`/`t` e `ch`/`sh` mudam de proporção com a seção, dentro da mesma mão. Com isso ficaram duas saídas para a família silábica, e testei as duas com as mesmas regras e o mesmo critério de antes.

A primeira saída é uma tabela que muda conforme o dialeto. Derivei do zero uma tabela só para A e outra só para B, sem fundir glifo nenhum (`k`, `t`, `p`, `f`, `ch`, `sh` e as quatro bancadas, cada um com valor próprio). Usei o mesmo algoritmo, o latim como alvo, 1.000 linhas de treino em A e 1.600 em B. O teste foi feito nas linhas de cada dialeto que ficaram fora do treino (3.794 palavras em A e 7.642 em B).

A segunda saída é outra língua. Re-derivei a tabela global, também sem fundir glifos, para catalão (AnCora), francês antigo (SRCMF, textos medievais como a *Chanson de Roland*) e occitano (TTB). Os três corpora vêm dos treebanks Universal Dependencies. Antes de olhar o Voynich, rodei o controle positivo de cada língua com a chave verdadeira, isto é, o próprio texto silabado como fluxo contínuo, para ver se o método enxergaria uma cifra desse tipo:

| Teste | Métrica S′ (contínua): real × embaralhado | Métrica R4 (palavras inteiras): real × embaralhado |
|---|---|---|
| Controle positivo catalão (chave verdadeira) | 64,9% × 19,7% (+45,2) | — |
| Controle positivo francês antigo | 66,7% × 33,4% (+33,3) | — |
| Controle positivo occitano | 45,3% × 10,9% (+34,3) | — |
| Voynich A, tabela só de A (latim, sem R1) | 41,5% × 40,3% (+1,1) | 17,5% × 17,3% (+0,2) |
| Voynich B, tabela só de B (latim, sem R1) | 35,4% × 34,1% (+1,3) | 15,6% × 15,5% (+0,1) |
| Voynich, tabela catalã | 39,0% × 38,6% (+0,5) | 12,7% × 12,7% (0,0) |
| Voynich, tabela de francês antigo | 50,8% × 49,2% (+1,6) | 21,0% × 20,8% (+0,1) |
| Voynich, tabela occitana | 26,9% × 25,2% (+1,7) | 11,6% × 11,3% (+0,3) |

O resultado é o mesmo das Fases 5 e 8. Separar os dialetos e parar de fundir glifos não faz aparecer nada. Trocar a língua por um romance medieval, ou por uma das línguas sugeridas pelos nomes dos meses, também não. A diferença entre a ordem real e a embaralhada fica entre +0,5 e +1,7 ponto na métrica contínua e entre 0,0 e +0,3 na de palavras inteiras, do tamanho da que uma chave treinada em texto embaralhado produz (+1,4). Num texto cifrado de verdade, ela seria de 33 a 54 pontos.

**Onde isso deixa o problema.** A família silábica de tabela fixa está descartada em seis línguas (latim, italiano, alemão, catalão, francês antigo, occitano), com tabela única ou com uma tabela por dialeto. Nenhum resultado estrutural mudou: o espaço como corte silábico de um fluxo contínuo, a regra de emenda na junção e o `-m` de fim de linha. Das três explicações da Fase 8, a primeira (uma língua que não testei) perdeu força, porque as línguas mais plausíveis para a época e o lugar já foram. Sobram as outras duas. Pode ser uma notação cuja correspondência muda mais do que por dialeto (por página, por posição na linha ou por uma regra de contexto). Ou pode ser um texto sem conteúdo linguístico, feito com regras de aparência silábica. Com testes de tabela fixa, não consigo mais distinguir entre essas duas.

**O que eu faria a seguir, se fosse continuar.** Testaria a segunda explicação contra a terceira diretamente, em vez de buscar mais chaves. Construiria um gerador sem conteúdo (palavras montadas pela gramática de casas da Fase 1, com regra de emenda na junção e `-m` por falta de espaço) e mediria se ele reproduz também o que é mais difícil de imitar sem significado. Isso inclui os rótulos das seções biológica e cosmológica, que reaparecem três vezes mais que o acaso no texto da própria página, e o vocabulário que muda com o assunto. Se o gerador reproduzir tudo, a hipótese de texto sem língua passa a ser a mais econômica. Se falhar justamente nos ecos entre rótulo e texto, a hipótese de notação com significado continua de pé, mas com uma correspondência que nenhuma tabela fixa capta.

### Resumo atualizado (Fase 9)

**Hipótese:** a notação silábica de tabela fixa está descartada em seis línguas, com ou sem tabelas por dialeto. O que fica são três fatos estruturais: o espaço como corte silábico de um fluxo contínuo, a regra de emenda na junção e o `-m` como abreviatura de fim de linha.

**Melhor frase traduzida:** nenhuma das novas tabelas produziu uma frase melhor que f2r.2 → *et eis cis*, que continua sem valor de prova.

**Teste:** a diferença entre ordem real e embaralhada ficou entre 0,0 e 1,7 ponto em todas as variantes, contra 33 a 54 pontos nos controles positivos.

**Confiança:** chave < 1%, tradução < 1%, estrutura do espaço ≈ 50%, `-m` como abreviatura ≈ 70%, interpretação geral do livro ≈ 35%. Baixei esta última um pouco, porque a explicação de texto sem língua ganhou peso relativo.

**Ponto mais fraco:** todos os testes supõem uma correspondência estável dentro de cada dialeto. Uma notação que muda por página ou por contexto passaria por eles sem ser vista.

---

[← Fase 8](fase-08.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 10 →](fase-10.md)
