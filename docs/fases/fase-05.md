# Fase 5 – O teste decisivo

[← Fase 4](fase-04.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 6 →](fase-06.md)

> **Em uma frase:** A chave lê o texto embaralhado tão bem quanto o original. A hipótese S cai.

| ![Fólio 78r, uma das duas páginas novas do teste decisivo](../imagens/f78r.jpg) |
|---|
| Fólio 78r, uma das duas páginas novas do teste decisivo |

<sub>Imagens: Beinecke Rare Book & Manuscript Library, Yale University, MS 408 (domínio público).</sub>

**A pergunta.** A chave lê melhor o texto na ordem real do que o mesmo texto com as palavras embaralhadas?

**O que foi feito.** A chave foi aplicada a duas páginas nunca usadas antes e às 20.239 palavras que ficaram fora do treino. Cada resultado foi comparado com o mesmo texto embaralhado (centenas de sorteios) e com uma 'chave nula', treinada no texto já embaralhado.

**O que deu.** Texto real 23,0%; embaralhado 22,5%. Num latim cifrado de verdade, o mesmo método dá 77% contra 48%. As leituras de várias sílabas, que eram o coração da hipótese, praticamente não existem (cerca de 1%, contra cerca de 50% esperados).

**Por que importa.** É o primeiro grande resultado negativo, e ele é confiável porque o teste tinha poder: no latim cifrado, a diferença aparece com folga.

- **Código:** [`fase5.py`](../../src/fase5.py), [`fase5b.py`](../../src/fase5b.py)
- **Saídas:** [`results/fase-05/`](../../results/fase-05/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 5 – Teste

Escolhi como trechos novos o f4r (herbal, A, mão 1) e o f78r (biológica, B, mão 2). Nenhum dos dois entrou no treino nem na Fase 4. Abaixo, os resultados no ZL com a vírgula valendo espaço; os controles usam 200 sorteios cada.

No **f4r**, 39,1% das palavras dão forma latina atestada, todas "lidas". Com a ordem das palavras embaralhada, dá 39,1% ± 0,2%. Em nenhum caso duas palavras Voynich se juntaram numa palavra latina.

No **f78r**, deu 24,1% (16,6% lidas e 7,6% incertas), com 3,4% das palavras em grupos de várias palavras. Embaralhado, 21,9% ± 0,6% (1,1% em grupos). São 2,2 pontos de diferença, e nenhum sorteio alcança o texto real. Só que a diferença vem de cinco grupos (`ol.tedy` e `ol.kedy` → *austrum* três vezes, `ched.ar` → *eramus*, `o.l` → *ius*), e três deles atravessam um espaço que o ZL marca como incerto. Com a vírgula valendo junção, o f78r cai para 20,4% contra 19,5% ± 0,4% (P = 0,07). No RF, 25,4% contra 24,4% ± 0,6% (P = 0,09).

Para ter mais potência, apliquei a chave às 20.239 palavras de parágrafo que ficaram fora do treino. Deu 23,0% no texto real contra 22,5% embaralhado (+0,5 ponto; grupos de várias palavras: 1,2% contra 0,7%). Com a vírgula valendo junção, a diferença cai para +0,2 ponto. Os +0,5 ponto são estatisticamente detectáveis: nenhum dos 30 sorteios chega lá. Mas uma chave "nula", treinada pelo mesmo algoritmo no texto já embaralhado, também dá um efeito do mesmo tipo (+0,1 e 0,0). Parte da diferença vem, portanto, da própria estrutura sequencial do Voynich, e não do latim. Embaralhando os glifos dentro de cada palavra, a validade cai para 8% a 9%. Isso só mostra que a tabela foi ajustada à forma das palavras voynichianas; não diz nada sobre significado.

O controle positivo mostra o que a hipótese previa. Pego latim de Isidoro, cifro por sílabas com uma chave conhecida e decifro com o mesmo algoritmo: dá 77,4% em ordem real contra 48,4% embaralhado, com 49,5% das palavras em grupos de várias sílabas. Com a chave verdadeira, 95,2% contra 54,8%.

**A conclusão é clara: a chave funciona praticamente igual no controle.** A diferença entre real e embaralhado ficou entre 0,2 e 0,5 ponto, quando a hipótese previa cerca de 29. E as leituras de várias sílabas, que eram o coração da hipótese, quase não existem (cerca de 1%, contra cerca de 50%). O que aparece como leitura são palavras Voynich frequentes associadas uma a uma a palavras latinas curtas.

Dois sintomas internos confirmam. O texto decodificado inteiro tem só 256 formas latinas distintas; cinco delas fazem 46% das leituras; *est* nunca aparece e *in* aparece em 0,03% das palavras, quando no latim são 2,2% e 2,4%. E a nota de "latinidade" da chave (+0,044 bit por letra acima da média do latim) não quer dizer latim. O texto decodificado tem h2 de 2,47 bits, contra 3,51 do latim sem espaços: é previsível demais, e é isso que o modelo de trigramas premia. As duas primeiras derivações mostram o mesmo de outro ângulo: o otimizador treinado no texto embaralhado alcançou a mesma cobertura que o treinado no texto real (61,7% contra 61,9% na primeira; 43,8% contra 40,7% na segunda).

---

[← Fase 4](fase-04.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 6 →](fase-06.md)
