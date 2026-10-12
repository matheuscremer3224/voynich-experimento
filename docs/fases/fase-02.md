# Fase 2 – Listar suspeitos

[← Fase 1](fase-01.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 3 →](fase-03.md)

> **Em uma frase:** Três explicações concorrentes para o sistema de escrita, e a escolha de uma para testar a fundo.

**A pergunta.** Que tipo de sistema explicaria as pistas da Fase 1?

**O que foi feito.** O agente formulou três hipóteses: uma língua natural num alfabeto inventado; um silabário (cada palavra do Voynich seria uma sílaba de latim, com várias grafias para a mesma sílaba); e um sistema de classificação ou notação. Para cada uma, listou que pistas ela explica e quais não explica.

**O que deu.** A escolhida foi o silabário sobre o latim (chamada de hipótese S). Era a única que explicava o padrão mais estranho, o espaço que liga em vez de separar. E fazia uma previsão fácil de testar: se as palavras são sílabas, embaralhar as palavras tem de destruir a leitura.

**Por que importa.** Escolher uma hipótese que pode ser derrubada por um teste barato é o que permite avançar. Foi o que aconteceu na Fase 5.

- **Código:** [`fase1b.py`](../../src/fase1b.py)
- **Saídas:** nenhuma (fase sem saídas de código)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 2 – Hipóteses concorrentes

**H1: língua natural num alfabeto inventado** (palavra = palavra, glifo = letra). Explica o vocabulário rico e com cara de língua (tipo/ocorrência e hápax iguais aos do latim), as palavras típicas de cada seção e os rótulos que reaparecem no texto da própria página. Não explica a h2 baixa, a distribuição estreita de comprimentos, os pares de variantes livres nem, principalmente, o primeiro padrão. Numa língua escrita com espaços, a informação fica dentro da palavra, e no Voynich ela está atravessando o espaço.

**H2: silabário verboso e homofônico sobre o latim.** Aqui cada palavra Voynich é uma sílaba (ou grupo de letras), os pares `k`/`t`, `ch`/`sh`, `p`/`f` e as bancadas são grafias alternativas de um mesmo valor, e uma palavra latina ocupa uma ou mais palavras Voynich seguidas. Explica a h2 baixa e o comprimento estreito, porque cada sílaba segue um molde. Explica os homófonos. Vai na direção certa no primeiro padrão: descontado o controle, numa sequência de sílabas latinas a razão entre a informação através da fronteira e dentro da unidade é 0,6, bem acima do 0,09 das palavras latinas. Mesmo assim fica abaixo do 2,0 do Voynich. O `-m` de fim de linha vira um sinal de fecho de palavra, como as abreviaturas que os copistas concentravam no fim da linha. A/B vira uma diferença de preferência entre tabelas de homófonos de escribas diferentes. O que não explica bem: o latim dividido em sílabas tem tipo/ocorrência de 0,049, e o Voynich, mesmo depois de fundir os homófonos, fica em 0,169. Seriam precisas cerca de três grafias por sílaba além das que identifiquei. Também não explica rótulos de uma palavra só: um nome de planta ou de estrela teria várias sílabas.

**H3: sistema de notação ou classificação** (um código de tabela com prefixo de classe, núcleo e sufixo de ordem). Explica as casas fixas, a independência entre começo e fim da palavra, os rótulos do zodíaco quase todos distintos e com prefixo comum (`ot-`/`ok-`), as repetições e os gallows como cabeçalho de parágrafo. Não explica que 35 mil palavras de texto corrido tenham a distribuição de frequências e a riqueza de uma língua, nem que o vocabulário mude por seção como mudaria um assunto.

**Escolho H2.** É a única que dá conta do padrão mais estranho (o espaço que liga em vez de separar) e da estrutura de homófonos. E faz uma previsão dura e barata de testar: se as palavras são sílabas de palavras latinas, a ordem importa, e embaralhar as palavras tem de destruir as leituras de várias sílabas. O controle pedido na Fase 5 passa a ser, portanto, o teste decisivo da hipótese.

Onde ela coincide com propostas anteriores e onde diverge. A ideia de cifra verbosa com várias tabelas lembra a cifra "Naibbe" (Greshko, 2025), que gera texto com cara de Voynich a partir de latim ou italiano usando unidades de uma ou duas letras. Já a ideia de que cada palavra seja uma sílaba lembra a velha conjectura de uma língua monossilábica. A minha diverge em quatro pontos. A unidade é a sílaba, não a letra. As classes de homófonos foram medidas nos dados, e não supostas. A tabela é escolhida por um algoritmo e congelada antes de ler os trechos. E a ordem das palavras é usada como teste de falsificação. Não uso anagramas, micrografia nem leitura palavra a palavra.

---

[← Fase 1](fase-01.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 3 →](fase-03.md)
