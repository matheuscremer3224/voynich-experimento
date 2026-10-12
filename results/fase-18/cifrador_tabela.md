# Fase 18 – Cifrador: Naibbe original sobre textos reais

Gerado por cifrador_rodar.py (PYTHONHASHSEED=0). Sementes da Naibbe: 1, 2, 3. Decifra e estabilidade com mc.semear(1) antes de cada chamada.

## (i) Naibbe – mediana entre as sementes 1–3

| Métrica | isidoro17 | plinio16 | apicius | hyginus | cesar | dante | europarl_it |
|---|---|---|---|---|---|---|---|
| fichas de texto | 31376 | 32652 | 24186 | 35014 | 33944 | 22959 | 61484 |
| h2 (bits) | 2.12 | 2.12 | 2.12 | 2.11 | 2.12 | 2.13 | 2.12 |
| comprimento médio (unid.) | 4.99 | 4.98 | 4.97 | 5.00 | 4.98 | 4.91 | 4.94 |
| razão tipo/ocorrência | 0.201 | 0.197 | 0.217 | 0.188 | 0.188 | 0.224 | 0.127 |
| formas únicas | 50% | 49% | 51% | 48% | 48% | 49% | 42% |
| inclinação de Zipf | -0.90 | -0.90 | -0.90 | -0.89 | -0.89 | -0.88 | -0.89 |
| MI junção ÷ MI dentro | 0.03 | 0.03 | 0.04 | 0.03 | 0.03 | 0.03 | 0.04 |
| F1 do espaço | 0.93 | 0.92 | 0.92 | 0.93 | 0.93 | 0.92 | 0.93 |
| repetição imediata | 0.11% | 0.13% | 0.14% | 0.17% | 0.16% | 0.20% | 0.22% |
| agrupamento (páginas de 200) | -0.003 | -0.002 | +0.002 | -0.000 | -0.002 | +0.003 | -0.002 |
| agrupamento em blocos de 8 | -0.005 | +0.003 | +0.009 | +0.007 | +0.006 | +0.006 | -0.000 |
| palavras-chave de página | 0.0% | 0.0% | 0.1% | 0.0% | 0.1% | 0.0% | 0.0% |
| vizinhas − distantes | +0.001 | +0.003 | +0.005 | +0.004 | +0.001 | +0.002 | +0.003 |
| agrupamento (páginas naturais) | -0.002 | +0.001 | +0.008 | +0.011 | +0.004 | +0.004 | +0.005 |
| eco dos rótulos (própria página) | 46% | 48% | 49% | 59% | 50% | 45% | 89% |
| concentração dos rótulos ecoados | 0.015 | 0.015 | 0.019 | 0.029 | 0.021 | 0.015 | 0.139 |
| … de fichas da página | 0.080 | 0.081 | 0.094 | 0.094 | 0.081 | 0.109 | 0.229 |

## (ii) Textos claros (sem cifra)

| Métrica | isidoro17 | plinio16 | apicius | hyginus | cesar | dante | europarl_it |
|---|---|---|---|---|---|---|---|
| fichas de texto | 8721 | 8730 | 6632 | 9295 | 8974 | 8538 | 16531 |
| h2 (bits) | 3.31 | 3.35 | 3.17 | 3.31 | 3.28 | 3.10 | 3.15 |
| comprimento médio (unid.) | 5.64 | 5.88 | 5.72 | 5.92 | 5.95 | 4.15 | 5.81 |
| razão tipo/ocorrência | 0.399 | 0.468 | 0.253 | 0.361 | 0.354 | 0.309 | 0.209 |
| formas únicas | 74% | 73% | 60% | 65% | 66% | 67% | 55% |
| inclinação de Zipf | -0.88 | -0.73 | -1.01 | -0.80 | -0.83 | -0.94 | -0.90 |
| MI junção ÷ MI dentro | 0.11 | 0.08 | 0.19 | 0.18 | 0.12 | 0.34 | 0.22 |
| F1 do espaço | 0.75 | 0.70 | 0.82 | 0.75 | 0.76 | 0.77 | 0.83 |
| repetição imediata | 0.01% | 0.00% | 0.02% | 0.04% | 0.00% | 0.04% | 0.01% |
| agrupamento (páginas de 200) | +0.085 | +0.040 | +0.189 | +0.104 | +0.101 | +0.056 | +0.096 |
| agrupamento em blocos de 8 | +0.087 | +0.020 | +0.106 | +0.116 | +0.059 | +0.007 | +0.115 |
| palavras-chave de página | 3.0% | 3.5% | 7.5% | 8.4% | 1.9% | 1.1% | 2.2% |
| vizinhas − distantes | +0.063 | +0.022 | +0.088 | +0.060 | +0.058 | +0.015 | +0.064 |
| agrupamento (páginas naturais) | +0.068 | +0.027 | +0.149 | +0.132 | +0.092 | +0.046 | +0.144 |
| eco dos rótulos (própria página) | 24% | 26% | 39% | 37% | 26% | 14% | 100% |
| concentração dos rótulos ecoados | 1.000 | 0.111 | 0.091 | 0.105 | 0.048 | 0.049 | 0.640 |
| … de fichas da página | 0.393 | 0.546 | 0.166 | 0.382 | 0.335 | 0.392 | 0.376 |

## (iii) Decifração e estabilidade (semente 1)

| Texto | língua | decifra | estab_frac | estab_grafias | estab_n |
|---|---|---|---|---|---|
| isidoro17 | latim | 100.0% | 0.070 | 19.0 | 108 |
| plinio16 | latim | 100.0% | 0.083 | 15.0 | 94 |
| apicius | latim | 100.0% | 0.063 | 18.0 | 122 |
| hyginus | latim | 100.0% | 0.073 | 17.0 | 117 |
| cesar | latim | 100.0% | 0.074 | 15.5 | 142 |
| dante | italiano | 100.0% | 0.094 | 16.0 | 136 |
| europarl_it | italiano | 100.0% | 0.067 | 19.0 | 267 |

## (iv) Mínimo – máximo entre as 3 sementes

| Texto | TTR | zipf | agrup_200 | bloco8_200 | viz_200 |
|---|---|---|---|---|---|
| isidoro17 | 0.200 – 0.202 | -0.90 – -0.89 | -0.003 – +0.004 | -0.010 – -0.002 | +0.001 – +0.003 |
| plinio16 | 0.197 – 0.198 | -0.90 – -0.89 | -0.003 – -0.000 | +0.001 – +0.005 | -0.002 – +0.005 |
| apicius | 0.217 – 0.219 | -0.91 – -0.90 | +0.001 – +0.007 | +0.002 – +0.019 | +0.004 – +0.008 |
| hyginus | 0.186 – 0.189 | -0.90 – -0.89 | -0.002 – +0.002 | +0.005 – +0.010 | +0.002 – +0.004 |
| cesar | 0.187 – 0.189 | -0.91 – -0.89 | -0.002 – +0.005 | -0.005 – +0.007 | +0.000 – +0.003 |
| dante | 0.218 – 0.227 | -0.88 – -0.87 | +0.002 – +0.005 | +0.003 – +0.011 | +0.000 – +0.002 |
| europarl_it | 0.126 – 0.128 | -0.89 – -0.89 | -0.003 – -0.002 | -0.002 – +0.004 | -0.001 – +0.005 |
