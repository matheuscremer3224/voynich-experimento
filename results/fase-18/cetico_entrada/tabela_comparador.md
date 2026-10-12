# Fase 18 – Comparador: o manuscrito (ZL3b) medido com as métricas comuns

Gerado por comparador_rodar.py (PYTHONHASHSEED=0). '–' = NaN (subconjunto pequeno demais para a métrica).

## (i) Inteiro, dialetos e seções

| Métrica | Inteiro | Dialeto A | Dialeto B | H (herbal) | P (farmacêutica) | B (biológica) | S (receitas/estrelas) | Z (zodíaco) | A (astronômica) | C (cosmológica) | T (só texto) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fichas de texto | 34977 | 11300 | 23128 | 11538 | 2318 | 6251 | 11603 | 0 | 279 | 697 | 2291 |
| h2 (bits) | 2.14 | 2.19 | 2.02 | 2.21 | 2.09 | 1.82 | 2.04 | – | 2.20 | 2.08 | 2.08 |
| comprimento médio (unid.) | 4.45 | 4.13 | 4.61 | 4.12 | 4.40 | 4.52 | 4.74 | – | 4.56 | 4.49 | 4.42 |
| razão tipo/ocorrência | 0.205 | 0.292 | 0.210 | 0.295 | 0.411 | 0.226 | 0.284 | – | 0.792 | 0.603 | 0.419 |
| formas únicas | 69% | 70% | 68% | 70% | 72% | 67% | 69% | – | 85% | 77% | 71% |
| inclinação de Zipf | -1.04 | -0.96 | -1.07 | -0.97 | -0.72 | -1.09 | -0.98 | – | -0.33 | -0.53 | -0.72 |
| MI junção ÷ MI dentro | 2.02 | 1.34 | 2.47 | 1.54 | 0.98 | 2.47 | 2.95 | – | 0.84 | 2.56 | 1.57 |
| F1 do espaço | 0.90 | 0.87 | 0.91 | 0.87 | 0.86 | 0.91 | 0.89 | – | 0.73 | 0.87 | 0.85 |
| repetição imediata | 0.92% | 0.98% | 0.91% | 0.94% | 0.86% | 1.16% | 0.80% | – | 0.45% | 1.36% | 0.87% |
| agrupamento (páginas de 200) | +0.093 | +0.085 | +0.097 | +0.086 | +0.075 | +0.094 | +0.091 | – | – | +0.167 | +0.150 |
| agrupamento em blocos de 8 | +0.032 | +0.026 | +0.034 | +0.023 | -0.004 | -0.002 | +0.050 | – | – | +0.000 | +0.132 |
| palavras-chave de página | 3.2% | 4.1% | 2.8% | 2.0% | 12.8% | 1.5% | 0.3% | – | – | – | 13.8% |
| vizinhas − distantes | +0.096 | +0.072 | +0.108 | +0.053 | +0.077 | +0.082 | +0.095 | – | – | – | +0.216 |
| agrupamento (páginas naturais) | +0.094 | +0.079 | +0.101 | +0.078 | +0.088 | +0.096 | +0.101 | – | – | +0.123 | +0.143 |
| eco dos rótulos (própria página) | 11% | 7% | 19% | 0% | 7% | 21% | 0% | – | 4% | 19% | 13% |
| concentração dos rótulos ecoados | 0.031 | 0.047 | 0.039 | – | 0.138 | 0.080 | – | – | 0.500 | 0.367 | 0.233 |
| … de fichas da página | 0.076 | 0.140 | 0.091 | – | 0.386 | 0.140 | – | – | 0.938 | 0.777 | 0.782 |

Páginas: Inteiro: 227 pág. | Dialeto A: 114 pág. | Dialeto B: 83 pág. | H (herbal): 129 pág. | P (farmacêutica): 16 pág. | B (biológica): 19 pág. | S (receitas/estrelas): 25 pág. | Z (zodíaco): 12 pág. | A (astronômica): 8 pág. | C (cosmológica): 11 pág. | T (só texto): 7 pág.

## (ii) Cruzamentos dialeto × seção e mãos

| Métrica | B×H | B×B | B×S | A×H | A×P | Mão 1 | Mão 2 | Mão 3 |
|---|---|---|---|---|---|---|---|---|
| fichas de texto | 3473 | 6251 | 10851 | 8020 | 2318 | 10548 | 10832 | 11721 |
| h2 (bits) | 2.10 | 1.82 | 2.02 | 2.16 | 2.09 | 2.17 | 1.96 | 2.04 |
| comprimento médio (unid.) | 4.36 | 4.52 | 4.76 | 4.01 | 4.40 | 4.10 | 4.46 | 4.73 |
| razão tipo/ocorrência | 0.384 | 0.226 | 0.283 | 0.312 | 0.411 | 0.291 | 0.228 | 0.284 |
| formas únicas | 72% | 67% | 69% | 70% | 72% | 69% | 68% | 69% |
| inclinação de Zipf | -0.84 | -1.09 | -1.00 | -1.02 | -0.72 | -0.99 | -1.15 | -0.98 |
| MI junção ÷ MI dentro | 1.89 | 2.47 | 2.84 | 1.43 | 0.98 | 1.29 | 2.00 | 2.93 |
| F1 do espaço | 0.89 | 0.91 | 0.89 | 0.87 | 0.86 | 0.87 | 0.91 | 0.90 |
| repetição imediata | 0.71% | 1.16% | 0.82% | 1.04% | 0.86% | 1.01% | 1.01% | 0.79% |
| agrupamento (páginas de 200) | +0.076 | +0.094 | +0.093 | +0.091 | +0.075 | +0.088 | +0.090 | +0.085 |
| agrupamento em blocos de 8 | -0.007 | -0.002 | +0.051 | +0.035 | -0.004 | +0.027 | +0.003 | +0.056 |
| palavras-chave de página | 3.7% | 1.5% | 0.3% | 1.2% | 12.8% | 4.1% | 8.3% | 0.6% |
| vizinhas − distantes | +0.041 | +0.082 | +0.095 | +0.066 | +0.077 | +0.072 | +0.115 | +0.093 |
| agrupamento (páginas naturais) | +0.075 | +0.096 | +0.104 | +0.080 | +0.088 | +0.082 | +0.090 | +0.102 |
| eco dos rótulos (própria página) | 0% | 21% | 0% | 0% | 7% | 7% | 21% | 0% |
| concentração dos rótulos ecoados | – | 0.080 | – | – | 0.138 | 0.050 | 0.053 | – |
| … de fichas da página | – | 0.140 | – | – | 0.386 | 0.150 | 0.096 | – |

Páginas: B×H: 32 pág. | B×B: 19 pág. | B×S: 23 pág. | A×H: 95 pág. | A×P: 16 pág. | Mão 1: 113 pág. | Mão 2: 46 pág. | Mão 3: 33 pág.

## (iii) Réguas de variação interna (criterios.md)

União de: mínimos e máximos de 10 subamostras de metade das páginas (mc.subamostras, frac=0,5) + seções com 3000+ fichas. Sem alargamento.

### Régua de B (decide) – seções usadas: BxH, BxB, BxS

| Métrica | mínimo | máximo | (subamostras: mín / mediana / máx) | mín vem de | máx vem de |
|---|---|---|---|---|---|
| TTR | 0.2264 | 0.3844 | 0.2608 / 0.2650 / 0.2939 | BxB | BxH |
| hapax | 0.6686 | 0.7169 | 0.6799 / 0.6898 / 0.7027 | BxB | BxH |
| zipf | -1.0860 | -0.8432 | -1.0825 / -1.0371 / -1.0180 | BxB | BxH |
| agrup_200 | 0.0759 | 0.1066 | 0.0791 / 0.0865 / 0.1066 | BxH | sub_max |
| bloco8_200 | -0.0093 | 0.0512 | -0.0093 / 0.0198 / 0.0349 | sub_min | BxS |
| viz_200 | 0.0325 | 0.1160 | 0.0325 / 0.0828 / 0.1160 | sub_min | sub_max |
| h2 | 1.8152 | 2.1030 | 2.0071 / 2.0230 / 2.0457 | BxB | BxH |
| compr | 4.3628 | 4.7571 | 4.5690 / 4.6077 / 4.6486 | BxH | BxS |
| razao | 1.8948 | 2.8375 | 2.0138 / 2.4085 / 2.7989 | BxH | BxS |
| F1esp | 0.8880 | 0.9067 | 0.8909 / 0.8965 / 0.9021 | BxH | BxB |
| rep | 0.0071 | 0.0116 | 0.0073 / 0.0093 / 0.0105 | BxH | BxB |

### Régua de A (só informativa) – seções usadas: AxH; excluídas por terem < 3000 fichas: AxP

| Métrica | mínimo | máximo | (subamostras: mín / mediana / máx) | mín vem de | máx vem de |
|---|---|---|---|---|---|
| TTR | 0.3125 | 0.3664 | 0.3513 / 0.3596 / 0.3664 | AxH | sub_max |
| hapax | 0.7043 | 0.7267 | 0.7086 / 0.7167 / 0.7267 | AxH | sub_max |
| zipf | -1.0244 | -0.9479 | -0.9799 / -0.9637 / -0.9479 | AxH | sub_max |
| agrup_200 | 0.0504 | 0.0991 | 0.0504 / 0.0649 / 0.0991 | sub_min | sub_max |
| bloco8_200 | 0.0071 | 0.0475 | 0.0071 / 0.0264 / 0.0475 | sub_min | sub_max |
| viz_200 | 0.0221 | 0.0796 | 0.0221 / 0.0505 / 0.0796 | sub_min | sub_max |
| h2 | 2.1572 | 2.2145 | 2.1587 / 2.1945 / 2.2145 | AxH | sub_max |
| compr | 4.0145 | 4.1727 | 4.0926 / 4.1299 / 4.1727 | AxH | sub_max |
| razao | 1.2727 | 1.4481 | 1.2727 / 1.3640 / 1.4481 | sub_min | sub_max |
| F1esp | 0.8419 | 0.8672 | 0.8419 / 0.8572 / 0.8654 | sub_min | AxH |
| rep | 0.0082 | 0.0111 | 0.0082 / 0.0097 / 0.0111 | sub_min | sub_max |

## Subconjuntos medidos com guarda

mc.medir abortou (StatisticsError) na 1ª tentativa; repetido com guarda em que só a função indicada devolve NaN em vez de abortar. As demais métricas saem do código original sem mudança.

- sec_H: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- sec_S: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- sec_A: agrupamento.clustering: mean requires at least one data point -> índice de agrupamento (agrup/bloco8, natural ou _200) = NaN
- BxH: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- BxS: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- AxH: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- mao_3: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN

## Subconjuntos não medidos (abortaram mesmo com guarda)

- sec_Z: 12 páginas, 0 fichas de texto corrido

## Métricas NaN por subconjunto

- sec_H: conc_nulo, conc_rot, freq_nulo, freq_rot
- sec_S: conc_nulo, conc_rot, freq_nulo, freq_rot
- sec_A: agrup, agrup_200, bloco8, bloco8_200, chave_frac, chave_frac_200, viz, viz_200
- sec_C: chave_frac, chave_frac_200, viz, viz_200
- sec_T: chave_frac, viz
- BxH: conc_nulo, conc_rot, freq_nulo, freq_rot
- BxS: conc_nulo, conc_rot, freq_nulo, freq_rot
- AxH: conc_nulo, conc_rot, freq_nulo, freq_rot
- mao_3: conc_nulo, conc_rot, freq_nulo, freq_rot

## Avisos e erros

- sec_H: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: no median for empty data [statistics.py:637 median <- rotulos_especificidade.py:38 analyze]
- sec_H: GUARDA disparou: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- sec_S: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: no median for empty data [statistics.py:637 median <- rotulos_especificidade.py:38 analyze]
- sec_S: GUARDA disparou: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- sec_Z: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: mean requires at least one data point [statistics.py:490 mean <- gerador.py:250 battery]
- sec_Z: ERRO também com guarda: statistics.StatisticsError: mean requires at least one data point [statistics.py:490] – subconjunto não medido (12 páginas, 0 fichas de texto corrido 'P')
- sec_A: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: mean requires at least one data point [statistics.py:490 mean <- agrupamento.py:26 clustering]
- sec_A: GUARDA disparou: agrupamento.clustering: mean requires at least one data point -> índice de agrupamento (agrup/bloco8, natural ou _200) = NaN
- BxH: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: no median for empty data [statistics.py:637 median <- rotulos_especificidade.py:38 analyze]
- BxH: GUARDA disparou: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- BxS: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: no median for empty data [statistics.py:637 median <- rotulos_especificidade.py:38 analyze]
- BxS: GUARDA disparou: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- AxH: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: no median for empty data [statistics.py:637 median <- rotulos_especificidade.py:38 analyze]
- AxH: GUARDA disparou: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- mao_3: ERRO na 1ª tentativa (sem guarda) em mc.medir: statistics.StatisticsError: no median for empty data [statistics.py:637 median <- rotulos_especificidade.py:38 analyze]
- mao_3: GUARDA disparou: rotulos_especificidade.analyze: no median for empty data -> conc_rot, conc_nulo, freq_rot, freq_nulo = NaN
- geral: AVISO ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/claude/voynich/ZL.txt' mode='r' encoding='latin-1'> (ivtff.py:55) – emitido em todas as 21 chamadas a mc.paginas_voynich (arquivo aberto sem fechar no parser; não afeta os valores)
