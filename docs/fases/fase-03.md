# Fase 3 – Montar a chave

[← Fase 2](fase-02.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 4 →](fase-04.md)

> **Em uma frase:** Uma tabela de correspondências escolhida por um algoritmo, com regras fixas e congelada antes da leitura.

**A pergunta.** Qual seria a tabela de leitura, se a hipótese S estiver certa?

**O que foi feito.** O agente fixou cinco regras de leitura (grafias equivalentes, divisão em pedaços, tabela, junção de sílabas, critério de 'palavra lida'). Depois deixou um programa escolher a tabela que torna o texto decodificado mais parecido com latim. A tabela foi congelada e ganhou uma 'impressão digital' (SHA-256), para provar que não mudou depois. Antes, o próprio método foi testado num latim cifrado de propósito, com chave conhecida.

**O que deu.** Houve três versões. A primeira degenerou: todo o texto virava 'a, e, an, en, ne'. A segunda não teria achado a chave nem no latim cifrado de propósito (acertou 1 ou 2 de 39 valores). A terceira acertou 30 de 39 nesse teste e foi a adotada. As duas descartadas estão registradas.

**Por que importa.** O teste com chave conhecida (controle positivo) é o que dá valor aos resultados negativos que vieram depois: o método conseguiria achar uma chave desse tipo se ela existisse.

- **Código:** [`lexicon.py`](../../src/lexicon.py), [`chave.py`](../../src/chave.py), [`otimiza.py`](../../src/otimiza.py), [`otim_core.py`](../../src/otim_core.py), [`otimiza2.py`](../../src/otimiza2.py), [`otim_ngram.py`](../../src/otim_ngram.py), [`controle_positivo.py`](../../src/controle_positivo.py), [`tabelas.py`](../../src/tabelas.py)
- **Saídas:** [`results/fase-03/`](../../results/fase-03/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 3 – A chave

A língua de destino é o latim, na ortografia dos manuscritos do século XV (ae e oe viram e, j vira i, v vira u, y vira i, k vira c). Escolhi o latim porque é a língua dos herbários, receituários e tratados de medicina astrológica feitos entre 1404 e 1438 na Europa central e no norte da Itália. "Válido" quer dizer que a forma existe, com frequência mínima de 2, num léxico de 48.224 formas que montei com 1,26 milhão de palavras da Latin Library (Isidoro, Columela, Apício, Vulgata, Tomás de Aquino e Guilherme de Conches).

As regras de leitura estão fixas desde antes de eu ler qualquer trecho:

**R1, homófonos.** `t` lê-se como `k`, `f` como `p`, `sh` como `ch`, e `cth`, `cph` e `cfh` como `ckh`. É o segundo padrão da Fase 1.

**R2, pedaços.** Uma série de `i` mais a consoante seguinte (`iin`, `ir`, `iir`…) é um pedaço. Uma série de `e` (`e`, `ee`, `eee`) é um pedaço. `dy` no fim da palavra é um pedaço. Cada outra unidade é um pedaço. `o` e `y` iniciais têm valor próprio, e todo pedaço final também (são as terminações).

**R3, tabela.** Cada pedaço vira uma letra ou terminação latina pela tabela abaixo. Se um pedaço não tem valor na tabela, a palavra fica não resolvida. Isso vale para ligaduras, caracteres raros, glifos com apóstrofo, séries de `i` fora do lugar e qualquer pedaço com menos de 30 ocorrências no treino.

**R4, sílabas.** Cada palavra Voynich é uma sílaba. Uma palavra latina ocupa de uma a quatro palavras Voynich seguidas, na mesma linha. A divisão escolhida é a que cobre mais palavras Voynich com formas latinas atestadas (programação dinâmica; no empate, vence a forma mais frequente).

**R5, estado.** "Lida" é uma forma com frequência de pelo menos 5 no corpus; "incerta", de 2 a 4; "não resolvida", nenhuma forma atestada.

**A e B.** Usam a mesma tabela. A diferença entre eles é preferência de escriba entre grafias e terminações (B prefere `-dy` e as séries de `e`; A prefere `-ol` e `-or`), não outra língua. A previsão é que a cobertura fique parecida nos dois. No texto todo, ficou em 28% em A e 21% em B.

Não escolhi os valores letra por letra. Fixei o que era permitido: letras latinas e *qu* para os pedaços internos; letras e 19 terminações para os finais; e nunca o mesmo valor para dois pedaços. Depois deixei um algoritmo escolher a tabela que torna o texto decodificado mais parecido com latim corrido, segundo um modelo de trigramas de letras (busca local iterada com 40 perturbações). O treino usou 1.600 linhas, sem nenhuma página das Fases 4 e 5. Em seguida congelei a tabela (SHA-256 começando por `006e30eff1ca9c6a`).

Antes dessa houve duas derivações, e registro por que as descartei. A primeira maximizava a cobertura léxica sem restrição e degenerou antes de qualquer leitura: todos os finais viraram vazio e o texto inteiro passou a ser lido como *a, e, an, en, ne*. A segunda já tinha a regra de valores distintos. Cheguei a aplicá-la aos trechos e ao teste, e ela também não separou o texto real do embaralhado (f4r: 46,9% contra 47,1%; f78r: 49,3% contra 49,8%). Mas o motivo para descartá-la foi outro: falhou no controle positivo. Aplicada a latim de verdade cifrado por sílabas com uma chave conhecida, acertou só 1 ou 2 dos 39 valores, ou seja, o método não teria achado a chave nem se ela existisse. A terceira acertou 30 dos 39 nesse mesmo controle. É a que vale, e todas as tabelas abaixo usam só ela.

| Glifo(s) EVA | Posição | Ocorrências | Valor latino |
|---|---|---|---|
| `ch/sh` | início/meio | 14162 | **e** |
| `o` | meio | 13997 | **i** |
| `k/t` | início/meio | 13977 | **t** |
| `a` | início/meio | 12680 | **u** |
| `e` | início/meio | 8983 | **r** |
| `o` | início | 6978 | **a** |
| `q` | início/meio | 5300 | **qu** |
| `d` | início/meio | 4960 | **s** |
| `l` | início/meio | 4011 | **n** |
| `ee` | início/meio | 3892 | **d** |
| `ckh/cth/cph/cfh` | início/meio | 1918 | **c** |
| `p/f` | início/meio | 1561 | **l** |
| `y` | início | 1462 | **o** |
| `r` | início/meio | 1235 | **m** |
| `s` | início/meio | 1110 | **g** |
| `y` | meio | 403 | **p** |
| `eee` | início/meio | 342 | **h** |
| `ir` | início/meio | 97 | **b** |
| `y` | fim | 7722 | **is** |
| `dy` | fim | 6237 | **um** |
| `l` | fim | 5380 | **us** |
| `r` | fim | 4616 | **s** |
| `iin` | fim | 3804 | **nt** |
| `in` | fim | 1643 | **it** |
| `o` | fim | 1135 | **i** |
| `s` | fim | 1091 | **et** |
| `m` | fim | 852 | **er** |
| `d` | fim | 569 | **am** |
| `ir` | fim | 413 | **m** |
| `iiin` | fim | 156 | **t** |
| `k/t` | fim | 138 | **in** |
| `iir` | fim | 118 | **r** |
| `n` | fim | 115 | **en** |
| `g` | fim | 113 | **es** |

---

[← Fase 2](fase-02.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 4 →](fase-04.md)
