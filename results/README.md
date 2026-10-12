# Resultados

[← README](../README.md) · [Código](../src/) · [As fases](../docs/fases/)

As saídas originais dos scripts, uma pasta por fase. São textos e tabelas exatamente como os programas os gravaram, sem edição. As Fases 2, 6, 7, 14 e 17 foram de raciocínio e interpretação e não têm saídas de código.

| Pasta | Fase | O que tem | Arquivo principal |
|---|---|---|---|
| [`fase-01/`](fase-01/) | Análise própria | As contagens com ZL (vírgula como espaço e como junção) e com RF | `out_fase1_ZL_split.txt` |
| [`fase-03/`](fase-03/) | A chave | A chave congelada, as tabelas descartadas, as tabelas nula e do controle positivo, e os registros dos otimizadores | `out_tabelas_final.txt`, `chave_final.json` |
| [`fase-04/`](fase-04/) | Tradução | Os quatro trechos decodificados palavra a palavra | `out_fase4.txt` |
| [`fase-05/`](fase-05/) | Teste | Texto real × embaralhado, ZL e RF, e o teste amplo fora do treino | `out_fase5_v3.txt`, `out_fase5b.txt` |
| [`fase-08/`](fase-08/) | Experimentos em aberto | Espaço, segmentação, código arbitrário, variante S′ em latim, italiano e alemão, `k`/`t` e `-m` | `out_espaco.txt`, `out_sprime_voynich.txt` |
| [`fase-09/`](fase-09/) | Tabelas por dialeto e três línguas | Teste da ordem por dialeto e em catalão, francês antigo e occitano, com os controles positivos | `out_ordem_*.txt`, `out_controles_linguas.txt` |
| [`fase-10/`](fase-10/) | Significado ou sem língua | Geradores sem conteúdo, rótulos, agrupamento, grades de parâmetros | `out_gerador_final.txt`, `out_agrupamento2.txt` |
| [`fase-11/`](fase-11/) | Texto × figuras | Teste de Mantel, palavra × traço visual, poder do teste, medidas de cor | `out_imagem_texto.txt` |
| [`fase-12/`](fase-12/) | Rótulos farmacêuticos | Comparação com as palavras de abertura do herbário | `out_farma_herbal.txt` |
| [`fase-13/`](fase-13/) | Origem do agrupamento | Grafias fundidas e blocos de páginas | `out_agrupamento_grafia.txt` |
| [`fase-15/`](fase-15/) | Gerador honesto | As 30 combinações da deriva lexical | `out_deriva_lexical.txt` |
| [`fase-16/`](fase-16/) | Cifra com sorteio (versão simplificada) | Calibração dos testes | `out_naibbe_calibracao.txt` |
| [`fase-18/`](fase-18/) | Naibbe original, com agentes | Ver abaixo | `coordenador_tabela_final.md` |

## Fase 18 em detalhe

Esta pasta guarda também o processo, não só os números. Por isso dá para conferir o que cada agente recebeu e produziu.

| Arquivo | O que é |
|---|---|
| `LEIA_AGENTES.md` | As regras comuns entregues aos agentes auxiliares |
| `criterios.md` | Os critérios de decisão, registrados **antes** de rodar |
| `cifrador_*`, `comparador_*`, `controle_*` | Tabelas, dados e registro de cada um dos três agentes paralelos |
| `coordenador_decisao.md` | A aplicação mecânica dos critérios (deu CONTRA) |
| `cetico_entrada/` | Exatamente o que o Cético recebeu na primeira rodada: só tabelas, dados e a conclusão provisória |
| `cetico_parecer.md` | O parecer do Cético (8 objeções) |
| `criterios_v2.md` | Os critérios da rodada corretiva, registrados depois do parecer e antes dos testes novos |
| `coordenador_T*.json`, `coordenador_extras.json`, `log_*.txt` | Os testes corretivos |
| `cetico_entrada2/`, `cetico_parecer2.md` | A segunda rodada do Cético |
| `coordenador_respostas_cetico.md` | O que foi feito com cada objeção, nas duas rodadas |
| `coordenador_tabela_final.md` | A tabela comparativa final, métrica por métrica |

Os arquivos de processo citam caminhos como `/home/claude/voynich/...`, do ambiente onde o trabalho rodou. No repositório, eles correspondem a `src/` e `results/fase-18/`.
