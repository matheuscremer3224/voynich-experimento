# Código

[← README](../README.md) · [Onde baixar os dados](../DADOS.md) · [Resultados](../results/)

Todo o código do experimento, em Python 3. Cada script reproduz uma parte de uma fase. As saídas originais de cada um estão em [`results/`](../results/), separadas por fase.

## Preparar

```bash
pip install -r requirements.txt        # numpy, scipy, pandas, Pillow
```

1. Baixe as transcrições e coloque-as em `src/ZL.txt` e `src/RF.txt` (veja [DADOS.md](../DADOS.md)).
2. Para as fases que comparam com outras línguas, baixe os corpora para `dados_externos/` (ou ajuste as variáveis de ambiente descritas em [`config.py`](config.py)).
3. Rode tudo **de dentro desta pasta**, com `PYTHONHASHSEED=0`. Os sorteios são feitos com sementes fixas; essa variável fixa também a ordem interna do Python e garante os mesmos números do relatório.

```bash
cd src
PYTHONHASHSEED=0 python3 fase1.py ZL.txt split > saida_fase1.txt
```

Os scripts gravam as suas saídas na pasta em que rodam (os da Fase 18, em `results/fase-18/`).

## O que precisa de quê

| Precisa de | Fases |
|---|---|
| Só as transcrições (`ZL.txt`, `RF.txt`) | 1, 3 a 5 (o léxico latino já vem pronto em `lexicon_latim.json`), 8 (parte), 10, 12, 13, 15 |
| Latin Library | refazer o léxico e o modelo de latim (3), controles positivos (3, 8), Isidoro nas Fases 10, 13 e 16, Fase 18 |
| Europarl / Universal Dependencies | 8 (italiano, alemão), 9 (catalão, francês antigo, occitano), 18 (italiano moderno) |
| Imagens do manuscrito | 11 (só `imagem_texto.py`; os outros scripts usam `imagem_features.json`, que já vem pronto) |
| Repositório da cifra Naibbe | 18 |

## Scripts por fase

| Fase | Script | O que faz | Como rodar |
|---|---|---|---|
| todas | `ivtff.py` | Lê e limpa os arquivos IVTFF: endereços, variáveis de página, leituras alternativas, ligaduras, caracteres raros, vírgula como espaço ou junção | (módulo) |
| todas | `config.py` | Onde ficam os dados externos | (módulo) |
| 1 | `fase1.py` | Frequência e posição dos glifos, entropia, comprimento, gramática de casas, seções, A×B, escribas, rótulos, efeitos de linha, repetição | `python3 fase1.py ZL.txt split` (ou `join`; ou `RF.txt split`) |
| 1, 2 | `fase1b.py` | Informação mútua através do espaço e dentro da palavra; vocabulário de sílabas latinas | `python3 fase1b.py` |
| 3 | `lexicon.py` | Léxico latino de referência (48 mil formas); grava `lexicon_latim.json` | `python3 lexicon.py` |
| 3 | `chave.py` | As regras fixas da chave (R1 a R5) | (módulo) |
| 3 | `otimiza.py` | Derivação v1 da chave, que degenerou (mantida para registro) | `python3 otimiza.py real 1` |
| 3 | `otim_core.py`, `otimiza2.py` | Derivação v2, descartada por falhar no controle positivo | `python3 otimiza2.py real` |
| 3 | `otim_ngram.py` | **Derivação final (v3)**: busca local com modelo de trigramas latinos; modos `real`, `embaralhado` (chave nula) e `positivo` | `python3 otim_ngram.py real` |
| 3 | `controle_positivo.py` | Latim cifrado por sílabas com chave conhecida (controle positivo) | `python3 controle_positivo.py` |
| 3, 4 | `tabelas.py` | Imprime a chave congelada e as glosas | `python3 tabelas.py glosas` |
| 4 | `fase4.py` | Aplica a chave aos quatro trechos da Fase 4 | `python3 fase4.py` |
| 5 | `fase5.py` | Teste em f4r e f78r contra texto embaralhado, ZL e RF, vírgula como espaço e como junção | `python3 fase5.py` |
| 5 | `fase5b.py` | Teste nas 20.239 palavras fora do treino; chave final × chave nula | `python3 fase5b.py` |
| 8 | `espaco.py` | Previsibilidade do espaço e tipo de dependência entre vizinhos | `python3 espaco.py` |
| 8 | `segmentacao.py` | O mesmo latim cortado de seis jeitos | `python3 segmentacao.py` |
| 8 | `unidade.py` | Latim cifrado com o vocabulário do Voynich como livro de código | `python3 unidade.py` |
| 8 | `sprime.py` | Variante S′ (fluxo contínuo) | `python3 sprime.py voynich la` (ou `it`, `de`) |
| 8 | `controle_positivo2.py`, `controle_positivo_it.py` | Controles positivos da S′ (latim, italiano) | `python3 controle_positivo2.py` |
| 8, 9 | `lingua.py` | Modelos de italiano, alemão, catalão, francês antigo e occitano | `python3 lingua.py it de` |
| 8 | `testes_r1_m.py` | `k`/`t` por seção dentro da mão; `-m` de fim de linha | `python3 testes_r1_m.py` |
| 8 | `diffs.py` | Divergências entre ZL e RF em trechos citados | `python3 diffs.py f1r:1-6 f2r` |
| 9 | `teste_ordem.py` | Teste da ordem para qualquer tabela, dialeto e língua | `NOHOMO=1 python3 teste_ordem.py tabela3_real_A_semR1.json A la 1000` |
| 9 | `controle_positivo_lang.py` | Controles positivos em catalão, francês antigo e occitano | `python3 controle_positivo_lang.py ca fro oc` |
| 10 | `gerador.py` | Geradores sem conteúdo (G-casas, G-casas2, G-cópia…) e a bateria de medidas | `python3 gerador.py` |
| 10 | `rotulos_especificidade.py`, `controle_rotulos_latim.py` | Os rótulos são nomes característicos da página? Voynich × Isidoro | `python3 rotulos_especificidade.py` |
| 10 | `agrupamento.py`, `agrupamento2.py`, `agrupamento3.py` | Agrupamento por página, palavras-chave de página, vizinhança, controles | `python3 agrupamento.py` |
| 10 | `deriva.py`, `copia2.py`, `copia3_grade.py`, `repertorio_grade.py` | Geradores com deriva, autocitação e repertório; grades de parâmetros | `python3 copia3_grade.py` |
| 11 | `imagem_texto.py` | Medidas de cor das pinturas e teste de Mantel texto × imagem (precisa das imagens) | `python3 imagem_texto.py` |
| 11 | `imagem_palavras.py`, `imagem_poder.py` | Palavra × traço visual e poder do teste | `python3 imagem_palavras.py` |
| 12 | `farma_herbal.py` | Rótulos farmacêuticos × palavras de abertura do herbário | `python3 farma_herbal.py` |
| 13 | `agrupamento_grafia.py` | Agrupamento com grafias fundidas e em blocos de páginas | `python3 agrupamento_grafia.py` |
| 15 | `deriva_lexical.py`, `deriva_lexical2.py` | Gerador honesto com deriva lexical lenta | `python3 deriva_lexical.py` |
| 16 | `naibbe_calibracao.py` | Calibração com versões simplificadas de cifras com sorteio (não é a cifra do autor) | `python3 naibbe_calibracao.py` |

Os arquivos `.json` desta pasta são entradas de algum script: a chave congelada (`chave_final.json`), as tabelas descartadas e de controle (`chave_v0_degenerada.json`, `chave_v2_injetiva.json`, `tabela*.json`), as glosas, o léxico latino, a correspondência entre fólios e páginas do PDF e as medidas de cor das imagens.

## Fase 18 (`fase18/`)

Organizada como um pequeno sistema de agentes. Todos usam o mesmo módulo de medidas, e as entradas e saídas ficam em [`results/fase-18/`](../results/fase-18/).

| Script | Papel | O que faz |
|---|---|---|
| `metricas_comuns.py` | código único | Todas as medidas, a leitura dos textos, a cifra Naibbe original (importada do repositório do autor, sem alterações), os geradores e o embaralhamento |
| `cifrador_rodar.py` | Cifrador | Cifra 5 textos latinos e 2 italianos com a Naibbe (sementes 1 a 3) e mede tudo |
| `comparador_rodar.py` | Comparador | Mede o manuscrito inteiro, por dialeto, seção e mão, e monta a régua de variação interna |
| `controle_rodar.py` | Controle | Mede o modelo de regras e o manuscrito embaralhado |
| `coordenador_decisao.py` | coordenador | Aplica, de forma mecânica, os critérios registrados antes (`criterios.md`) |
| `coordenador_testes.py` | coordenador | Os testes corretivos pedidos pelo Cético: `T1T2T3`, `T4`, `T5`, `T5b`, `T3b`, `T6`, `T7`, `T7b` |
| `coordenador_extras.py` | coordenador | O critério corrigido aplicado também ao manuscrito, ao modelo de regras e ao embaralhado |
| `coordenador_tabela_final.py` | coordenador | Monta a tabela comparativa final |

Ordem para refazer tudo:

```bash
cd src/fase18
export PYTHONHASHSEED=0
python3 cifrador_rodar.py && python3 comparador_rodar.py && python3 controle_rodar.py
python3 coordenador_decisao.py
python3 coordenador_testes.py T1T2T3 T4 T5 T5b T3b T6 T7 T7b
python3 coordenador_extras.py
python3 coordenador_tabela_final.py
```

`coordenador_decisao.py` e `coordenador_tabela_final.py` só leem os JSON já gravados em `results/fase-18/`. Rodam sem nenhum dado externo.

## Conferência antes da publicação

A partir de uma cópia limpa deste repositório, com os dados baixados como em DADOS.md, refizemos `fase1.py`, `fase5.py`, `espaco.py`, `imagem_palavras.py`, `farma_herbal.py`, `coordenador_decisao.py` e `coordenador_tabela_final.py`, mais uma cifragem completa com a Naibbe e as medidas do dialeto B. Todas as saídas saíram idênticas às guardadas em `results/`.

O código foi escrito por agentes Claude ao longo do experimento, fase a fase. Nesta versão publicada, a única mudança foi trocar caminhos fixos do ambiente original por `config.py`.
