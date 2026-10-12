# Conclusão provisória do coordenador

**CONTRA.** Pela regra registrada (criterios_registrados.md), a cifra Naibbe com as tabelas e parâmetros originais, aplicada a cinco textos latinos reais, não reproduz o agrupamento lexical por trechos do manuscrito (P2) nem as propriedades de vocabulário (P1). Efeito previsto nas estimativas: 'texto gerado por regras' de ≈70% para 75–80%; 'o texto contém a informação das figuras' de 10–15% para ≈10%; chave (<1%) e tradução (<1%) sem mudança; leitura do livro pelas figuras (≈35%) sem mudança.

Régua de B (do Comparador). Textos latinos: isidoro17, plinio16, apicius, hyginus, cesar. Informativos: dante, europarl_it.

| Texto | P1 | P2 | P3 (contexto) | métricas fora da régua |
|---|---|---|---|---|
| isidoro17 | falha | falha | falha | TTR=0.2014 [0.2264; 0.3844]; hapax=49.89% [66.86%; 71.69%]; agrup_200=-0.0026 [+0.0759; +0.1066]; viz_200=+0.0013 [+0.0325; +0.1160]; h2=2.1173 [1.8152; 2.1030]; compr=4.9909 [4.3628; 4.7571]; razao=0.0321 [1.8948; 2.8375]; F1esp=0.9273 [0.8880; 0.9067]; rep=0.11% [0.71%; 1.16%] |
| plinio16 | falha | falha | falha | TTR=0.1967 [0.2264; 0.3844]; hapax=49.00% [66.86%; 71.69%]; agrup_200=-0.0024 [+0.0759; +0.1066]; viz_200=+0.0035 [+0.0325; +0.1160]; h2=2.1178 [1.8152; 2.1030]; compr=4.9789 [4.3628; 4.7571]; razao=0.0279 [1.8948; 2.8375]; F1esp=0.9250 [0.8880; 0.9067]; rep=0.13% [0.71%; 1.16%] |
| apicius | falha | falha | falha | TTR=0.2170 [0.2264; 0.3844]; hapax=50.64% [66.86%; 71.69%]; agrup_200=+0.0020 [+0.0759; +0.1066]; viz_200=+0.0049 [+0.0325; +0.1160]; h2=2.1167 [1.8152; 2.1030]; compr=4.9696 [4.3628; 4.7571]; razao=0.0400 [1.8948; 2.8375]; F1esp=0.9245 [0.8880; 0.9067]; rep=0.14% [0.71%; 1.16%] |
| hyginus | falha | falha | falha | TTR=0.1876 [0.2264; 0.3844]; hapax=47.72% [66.86%; 71.69%]; agrup_200=-0.0003 [+0.0759; +0.1066]; viz_200=+0.0035 [+0.0325; +0.1160]; h2=2.1129 [1.8152; 2.1030]; compr=4.9969 [4.3628; 4.7571]; razao=0.0288 [1.8948; 2.8375]; F1esp=0.9286 [0.8880; 0.9067]; rep=0.17% [0.71%; 1.16%] |
| cesar | falha | falha | falha | TTR=0.1881 [0.2264; 0.3844]; hapax=47.81% [66.86%; 71.69%]; agrup_200=-0.0018 [+0.0759; +0.1066]; viz_200=+0.0014 [+0.0325; +0.1160]; h2=2.1161 [1.8152; 2.1030]; compr=4.9819 [4.3628; 4.7571]; razao=0.0289 [1.8948; 2.8375]; F1esp=0.9312 [0.8880; 0.9067]; rep=0.16% [0.71%; 1.16%] |
| dante (inf.) | falha | falha | falha | TTR=0.2239 [0.2264; 0.3844]; hapax=48.99% [66.86%; 71.69%]; agrup_200=+0.0025 [+0.0759; +0.1066]; viz_200=+0.0017 [+0.0325; +0.1160]; h2=2.1308 [1.8152; 2.1030]; compr=4.9101 [4.3628; 4.7571]; razao=0.0349 [1.8948; 2.8375]; F1esp=0.9219 [0.8880; 0.9067]; rep=0.20% [0.71%; 1.16%] |
| europarl_it (inf.) | falha | falha | falha | TTR=0.1265 [0.2264; 0.3844]; hapax=42.36% [66.86%; 71.69%]; agrup_200=-0.0023 [+0.0759; +0.1066]; viz_200=+0.0027 [+0.0325; +0.1160]; h2=2.1233 [1.8152; 2.1030]; compr=4.9367 [4.3628; 4.7571]; razao=0.0439 [1.8948; 2.8375]; F1esp=0.9302 [0.8880; 0.9067]; rep=0.22% [0.71%; 1.16%] |

Mesmo teste aplicado às referências (informativo):

| Referência | P1 | P2 | P3 | fora da régua |
|---|---|---|---|---|
| Voynich B inteiro | falha | passa | passa | TTR |
| Voynich A inteiro | passa | passa | falha | h2, compr, razao, F1esp |
| regras-deriva mediana B | falha | falha | passa | TTR, hapax, agrup_200, viz_200 |
| VB global mediana | falha | falha | falha | TTR, agrup_200, viz_200, razao, F1esp, rep |
| VB pagina mediana | falha | falha | falha | TTR, agrup_200, razao, F1esp, rep |

Textos latinos que passam em P1 e P2: 0 de 5. Que falham em P2: 5 de 5.

**Decisão pela regra registrada: CONTRA.**
