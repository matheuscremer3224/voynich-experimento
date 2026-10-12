# Fase 18 – Tabela comparativa final

Valores: manuscrito (ZL3b, vírgula = espaço); Naibbe = mediana das sementes 1–3 em cada texto e, depois, mediana dos 5 textos latinos (faixa entre textos na coluna seguinte); regras-deriva = mediana das sementes 13–15; embaralhados = mediana das sementes 7–8. Régua de B = [mín; máx] registrado em criterios.md.

| Métrica | Prop. | Régua de B | VA | VB | Naibbe original, latim | faixa Naibbe (5 textos) | Naibbe original, italiano (Dante) | Naibbe com deriva (α=10), latim ‡ | Latim sem cifra (P1 e P2 = código palavra a palavra) † | Regras-deriva B | Regras-casas2 B | VB embaralhado global | VB embaralhado na página |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fichas de texto | – | – | 11.300 | 23.128 | 32.652 | 24.186 a 35.014 | 22.959 | 32.609 | 8.730 | 22.138 | 22.282 | 23.128 | 23.128 |
| h2 (bits) | P3 | [1,82; 2,10] | 2,19 | 2,02 | 2,12 | 2,11 a 2,12 | 2,13 | 2,12 | 3,31 | 2,04 | 2,02 | 2,02 | 2,02 |
| comprimento médio (unid.) | P3 | [4,36; 4,76] | 4,13 | 4,61 | 4,98 | 4,97 a 5,00 | 4,91 | – | 5,88 | 4,56 | 4,54 | 4,61 | 4,61 |
| razão tipo/ocorrência | P1 | [0,226; 0,384] | 0,292 | 0,210 | 0,197 | 0,188 a 0,217 | 0,224 | 0,196 | 0,361 | 0,191 | 0,220 | 0,210 | 0,210 |
| formas únicas (hapax) | P1 | [66,9%; 71,7%] | 69,7% | 68,4% | 49,0% | 47,7% a 50,6% | 49,0% | 49,3% | 66,1% | 60,7% | 70,2% | 68,4% | 68,4% |
| inclinação de Zipf | P1 | [-1,09; -0,84] | -0,96 | -1,07 | -0,90 | -0,90 a -0,89 | -0,88 | -0,90 | -0,83 | -1,04 | -1,12 | -1,07 | -1,07 |
| MI na junção ÷ MI dentro | P3 | [1,89; 2,84] | 1,34 | 2,47 | 0,03 | 0,03 a 0,04 | 0,03 | 0,04 | 0,12 | 2,47 | 2,23 | 0,02 | 0,02 |
| F1 ao recolocar o espaço | P3 | [0,888; 0,907] | 0,869 | 0,906 | 0,927 | 0,924 a 0,931 | 0,922 | 0,930 | 0,753 | 0,903 | 0,899 | 0,917 | 0,918 |
| repetição imediata | P3 | [0,71%; 1,16%] | 0,98% | 0,91% | 0,14% | 0,11% a 0,17% | 0,20% | 0,21% | 0,01% | 0,81% | 1,14% | 0,49% | 0,68% |
| agrupamento por página (200 fichas) | P2 | [+0,076; +0,107] | +0,085 | +0,097 | -0,002 | -0,003 a +0,002 | +0,003 | +0,040 | +0,101 | +0,060 | +0,002 | -0,002 | +0,072 |
| agrupamento em blocos de 8 | P2 | [-0,009; +0,051] | +0,026 | +0,034 | +0,006 | -0,005 a +0,009 | +0,006 | +0,050 | +0,087 | +0,037 | +0,002 | +0,003 | +0,032 |
| vizinhas − distantes | P2 | [+0,032; +0,116] | +0,072 | +0,108 | +0,003 | +0,001 a +0,005 | +0,002 | +0,067 | +0,060 | +0,118 | +0,001 | -0,006 | +0,104 |
| palavras-chave de página | – | – | 4,1% | 2,8% | 0,0% | 0,0% a 0,1% | 0,0% | – | 3,5% | 2,3% | 1,1% | 1,2% | 3,1% |
| **T2: recuperação R do agrupamento (passam)** | P2 | ≥ 0,25 e > p95 do nulo | +0,86 (1/1) | +1,00 (1/1) | -0,01 (0/5) | – | – | +0,41 (5/5) | +1,05 (5/5) | +0,63 (3/3) | +0,03 (0/1) | +0,01 (0/1) | +0,75 (1/1) |
| **T3: TTR nas primeiras 10.974 fichas** | P1 | sub. de B: [0,261; 0,294] | 0,296 | 0,234 | 0,317 | – | – | – | – | 0,221 | 0,237 | 0,233 | 0,234 |
| **T3: hapax nas primeiras 10.974 fichas** | P1 | sub. de B: [68,0%; 70,3%] | 69,9% | 69,0% | 61,1% | – | – | – | – | 62,4% | 69,3% | 68,3% | 68,9% |
| decifração por decrypt_naibbe.py | – | – | – | – | 100% | – | 100% | 100% | – | – | – | – | – |

† O código palavra a palavra (cada tipo latino → tipo de VB de mesmo posto) tem P1 e P2 idênticos aos do latim sem cifra (verificado em T1); suas colunas de P3 dependem do vocabulário de destino e não são mostradas aqui. Nas linhas T3, o código tem menos de 10.974 fichas.
‡ Variante, NÃO a cifra original: mesmas tabelas e glifos, mas os pesos das tabelas são sorteados por página (Dirichlet com α = 10 × pesos do autor). Mantém a verificação de ambiguidade e a decifração de 100%.
As subamostras de B que definem a régua do T3 são metades de páginas sorteadas, espalhadas pelas seções; uma janela contínua de VB com o mesmo tamanho dá TTR 0,234 (coluna VB). As duas referências reprovam a Naibbe.
