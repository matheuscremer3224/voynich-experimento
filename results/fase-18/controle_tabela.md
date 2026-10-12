# Fase 18 – Controle

## (i) Modelo de regras e manuscrito embaralhado

| Métrica | Regras-deriva inteiro (med. s13–15) | Regras-deriva A (med.) | Regras-deriva B (med.) | Regras-casas2 inteiro (s13) | Regras-casas2 B (s13) | VB original | VB global (med. s7,s8) | VB página (med. s7,s8) | VA original | VA global (med. s7,s8) |
|---|---|---|---|---|---|---|---|---|---|---|
| fichas de texto | 33388 | 10737 | 22138 | 33593 | 22282 | 23128 | 23128 | 23128 | 11300 | 11300 |
| h2 (bits) | 2.16 | 2.21 | 2.04 | 2.15 | 2.02 | 2.02 | 2.02 | 2.02 | 2.19 | 2.19 |
| comprimento médio (unid.) | 4.40 | 4.09 | 4.56 | 4.38 | 4.54 | 4.61 | 4.61 | 4.61 | 4.13 | 4.13 |
| razão tipo/ocorrência | 0.193 | 0.267 | 0.191 | 0.214 | 0.220 | 0.210 | 0.210 | 0.210 | 0.292 | 0.292 |
| formas únicas | 62% | 64% | 61% | 71% | 70% | 68% | 68% | 68% | 70% | 70% |
| inclinação de Zipf | -1.03 | -0.94 | -1.04 | -1.09 | -1.12 | -1.07 | -1.07 | -1.07 | -0.96 | -0.96 |
| MI junção ÷ MI dentro | 2.29 | 1.61 | 2.47 | 2.10 | 2.23 | 2.47 | 0.02 | 0.02 | 1.34 | -0.00 |
| F1 do espaço | 0.89 | 0.86 | 0.90 | 0.89 | 0.90 | 0.91 | 0.92 | 0.92 | 0.87 | 0.88 |
| repetição imediata | 0.81% | 0.82% | 0.81% | 1.15% | 1.14% | 0.91% | 0.49% | 0.68% | 0.98% | 0.54% |
| agrupamento (páginas de 200) | +0.058 | +0.051 | +0.060 | +0.000 | +0.002 | +0.097 | -0.002 | +0.072 | +0.085 | -0.005 |
| agrupamento em blocos de 8 | +0.028 | +0.016 | +0.037 | -0.002 | +0.002 | +0.034 | +0.003 | +0.032 | +0.026 | +0.000 |
| palavras-chave de página | 3.3% | 4.8% | 2.3% | 2.0% | 1.1% | 2.8% | 1.2% | 3.1% | 4.1% | 0.7% |
| vizinhas − distantes | +0.106 | +0.086 | +0.118 | -0.001 | +0.001 | +0.108 | -0.006 | +0.104 | +0.072 | +0.008 |
| agrupamento (páginas naturais) | +0.070 | +0.051 | +0.079 | +0.004 | +0.006 | +0.101 | -0.006 | +0.101 | +0.079 | -0.006 |
| eco dos rótulos (própria página) | 22% | 22% | 38% | 23% | 35% | 19% | 20% | 19% | 7% | 8% |
| concentração dos rótulos ecoados | 0.016 | 0.038 | 0.022 | 0.016 | 0.025 | 0.039 | 0.030 | 0.039 | 0.047 | 0.039 |
| … de fichas da página | 0.085 | 0.201 | 0.096 | 0.068 | 0.072 | 0.091 | 0.087 | 0.103 | 0.140 | 0.150 |

## (ii) Regras-deriva, dialeto B: variação entre sementes

| Métrica | mínimo | mediana | máximo | s13 | s14 | s15 |
|---|---|---|---|---|---|---|
| razão tipo/ocorrência (TTR) | 0.191 | 0.191 | 0.194 | 0.194 | 0.191 | 0.191 |
| inclinação de Zipf (zipf) | -1.04 | -1.04 | -1.04 | -1.04 | -1.04 | -1.04 |
| agrupamento (páginas de 200) (agrup_200) | +0.057 | +0.060 | +0.064 | +0.060 | +0.057 | +0.064 |
| agrupamento em blocos de 8 (bloco8_200) | +0.033 | +0.037 | +0.040 | +0.033 | +0.037 | +0.040 |
| vizinhas − distantes (viz_200) | +0.106 | +0.118 | +0.122 | +0.122 | +0.106 | +0.118 |

## (iii) Verificação de sanidade (embaralhamento)

Regra usada: global ~0: |mediana embaralhada| <= 10% de |original|; pagina ~original: desvio <= 25% do original; 'cai' = valor embaralhado < original nas duas sementes.

| Corpus | nível | métrica | original | s7 | s8 | mediana | mediana/original | ~0? | ~original? | cai nas duas? |
|---|---|---|---|---|---|---|---|---|---|---|
| V | global | agrup_200 | +0.093 | +0.000 | -0.003 | -0.001 | -0.02 | sim | não | sim |
| V | global | bloco8_200 | +0.032 | -0.005 | +0.003 | -0.001 | -0.03 | sim | não | sim |
| V | global | viz_200 | +0.096 | +0.006 | +0.005 | +0.006 | 0.06 | sim | não | sim |
| V | global | razao | 2.02 | 0.03 | 0.03 | 0.03 | 0.01 | – | – | sim |
| V | global | rep | 0.92% | 0.53% | 0.46% | 0.49% | 0.54 | – | – | sim |
| V | pagina | agrup_200 | +0.093 | +0.075 | +0.077 | +0.076 | 0.81 | não | sim | sim |
| V | pagina | bloco8_200 | +0.032 | +0.029 | +0.030 | +0.029 | 0.93 | não | sim | sim |
| V | pagina | viz_200 | +0.096 | +0.095 | +0.097 | +0.096 | 1.00 | não | sim | não |
| V | pagina | razao | 2.02 | 0.03 | 0.04 | 0.04 | 0.02 | – | – | sim |
| V | pagina | rep | 0.92% | 0.73% | 0.78% | 0.76% | 0.82 | – | – | sim |
| VB | global | agrup_200 | +0.097 | -0.002 | -0.003 | -0.002 | -0.02 | sim | não | sim |
| VB | global | bloco8_200 | +0.034 | +0.004 | +0.001 | +0.003 | 0.08 | sim | não | sim |
| VB | global | viz_200 | +0.108 | -0.005 | -0.007 | -0.006 | -0.05 | sim | não | sim |
| VB | global | razao | 2.47 | 0.01 | 0.02 | 0.02 | 0.01 | – | – | sim |
| VB | global | rep | 0.91% | 0.46% | 0.51% | 0.49% | 0.54 | – | – | sim |
| VB | pagina | agrup_200 | +0.097 | +0.073 | +0.070 | +0.072 | 0.74 | não | não | sim |
| VB | pagina | bloco8_200 | +0.034 | +0.030 | +0.035 | +0.032 | 0.94 | não | sim | não |
| VB | pagina | viz_200 | +0.108 | +0.103 | +0.105 | +0.104 | 0.96 | não | sim | sim |
| VB | pagina | razao | 2.47 | 0.03 | 0.01 | 0.02 | 0.01 | – | – | sim |
| VB | pagina | rep | 0.91% | 0.69% | 0.66% | 0.68% | 0.75 | – | – | sim |
| VA | global | agrup_200 | +0.085 | -0.003 | -0.007 | -0.005 | -0.06 | sim | não | sim |
| VA | global | bloco8_200 | +0.026 | -0.002 | +0.003 | +0.000 | 0.01 | sim | não | sim |
| VA | global | viz_200 | +0.072 | +0.009 | +0.008 | +0.008 | 0.11 | não | não | sim |
| VA | global | razao | 1.34 | -0.03 | 0.03 | -0.00 | -0.00 | – | – | sim |
| VA | global | rep | 0.98% | 0.49% | 0.60% | 0.54% | 0.56 | – | – | sim |
| VA | pagina | agrup_200 | +0.085 | +0.083 | +0.086 | +0.085 | 0.99 | não | sim | não |
| VA | pagina | bloco8_200 | +0.026 | +0.025 | +0.023 | +0.024 | 0.92 | não | sim | sim |
| VA | pagina | viz_200 | +0.072 | +0.071 | +0.067 | +0.069 | 0.97 | não | sim | sim |
| VA | pagina | razao | 1.34 | 0.02 | 0.04 | 0.03 | 0.02 | – | – | sim |
| VA | pagina | rep | 0.98% | 0.79% | 0.86% | 0.83% | 0.85 | – | – | sim |
