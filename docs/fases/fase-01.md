# Fase 1 – Examinar a cena

[Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 2 →](fase-02.md)

> **Em uma frase:** Antes de ter qualquer teoria, medir tudo o que dá para medir no texto.

**A pergunta.** Como o texto do Voynich se comporta, em números, antes de qualquer tentativa de leitura?

**O que foi feito.** O agente contou os símbolos, mediu em que posição da palavra cada um aparece, comparou as seções do livro, os dois dialetos e os escribas, e olhou como se comportam os rótulos junto às figuras. Tudo foi feito com as duas transcrições e com a vírgula (espaço incerto) valendo espaço e valendo junção.

**O que deu.** Cinco padrões se destacaram. O mais estranho: o fim de uma palavra está mais ligado ao começo da palavra seguinte do que ao começo dela mesma, o contrário de uma língua escrita comum. Os outros: pares de símbolos que se comportam como grafias alternativas, linhas e parágrafos com começo e fim próprios, dialetos que diferem na ortografia, e rótulos que às vezes reaparecem no texto da página.

**Por que importa.** Essas medidas viraram as pistas que qualquer explicação teria de dar conta. O primeiro padrão guiou quase toda a investigação.

- **Código:** [`ivtff.py`](../../src/ivtff.py), [`fase1.py`](../../src/fase1.py), [`fase1b.py`](../../src/fase1b.py)
- **Saídas:** [`results/fase-01/`](../../results/fase-01/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

Antes de contar qualquer coisa, limpei os arquivos assim: descartei as linhas `#` e os comentários `<!…>`, herdei as variáveis de página em cada linha, apaguei `<%>` e `<$>`, tratei `<->` e `<~>` como espaço, fiquei com a primeira opção de cada `[a:b]`, contei cada `{…}` e cada `@NNN;` como uma unidade, rodei tudo com a vírgula valendo espaço e valendo junção, e tirei das contagens de vocabulário as palavras com `?`.


### Fase 1 – Análise própria

O ZL3b tem 5.384 linhas de texto, com 39.025 palavras e 8.373 formas distintas quando a vírgula conta como espaço. Quando ela não conta, ficam 36.277 palavras e 9.446 formas. A vírgula mexe quase só com palavras curtas (`y`, `aiin`, `ol`, `s`, `ar`, `l`, `o`, `or`, `dy`, `al`). Isso já sugere que esses itens funcionam como pedaços soltos, não como palavras inteiras. Nenhum dos padrões abaixo muda de sentido entre as duas convenções, nem quando troco o ZL pelo RF1b. As diferenças ficam em geral abaixo de um ponto e meio percentual; a única exceção aponto no terceiro padrão.

Tratei como glifo único as bancadas `ch`, `sh`, `cth`, `ckh`, `cph` e `cfh`, além das ligaduras e dos caracteres raros. Com isso, cada glifo tem um lugar quase fixo na palavra. `q` é inicial em 99,3% dos casos, `n` é final em 98,5%, `m` em 95,2% e `y` em 86,1%. `e` e `i` são internos em 99% dos casos. A entropia condicional h2 dá 2,18 bits, contra 3,35 num latim técnico de mesmo tamanho (Isidoro, livros IV, XVI e XVII, mais Apício), embora a entropia de uma letra só seja quase igual (3,93 contra 3,99). Uma palavra tem em média 4,46 ± 1,68 unidades; em latim, 5,72 ± 2,58 letras. A distribuição voynichiana é estreita, quase sem palavras de 1 ou 8 ou mais unidades. Escrevi uma gramática de seis casas (prefixo, gallows, bancada, série de e, vogal, final). Ela cobre 75,8% das ocorrências; aplicada a palavras latinas, cobre 10,5%. Ao mesmo tempo, o vocabulário é tão rico quanto o de uma língua: a razão tipo/ocorrência é 0,212 (no latim, 0,226) e 70% das formas aparecem uma única vez (no latim, 67%).

Por seção, o texto corrido muda de cara. No herbal dominam `daiin` (4,0%) e `chol` (2,0%). Na seção biológica, `ol` (3,5%), `shedy` (3,5%), `chedy` (2,9%) e `qokain` (2,6%). Nas receitas, `aiin` (1,9%), `chedy` (1,7%) e `ar` (1,5%). No zodíaco, `aiin` (2,6%), `al`, `ar` e `oteey`.

Destes resultados, cinco padrões me parecem os mais reveladores.

O primeiro é que o espaço não se comporta como fronteira de palavra latina. Medi a informação mútua entre a última letra de uma palavra e a primeira unidade da seguinte: 0,215 bits, contra 0,018 com os pares embaralhados. Entre a primeira unidade e a última letra da mesma palavra, deu 0,114 bits (controle 0,015). Ou seja, uma palavra "conversa" mais com a vizinha do que o seu começo conversa com o seu fim. Em latim é o oposto: 0,037 bits através do espaço e 0,314 dentro da palavra. Depois de `-y` vem `q` em 28% dos casos; depois de `-r` vem `a` em 18%, o que depois de `-y` acontece em só 0,9% dos casos.

O segundo é que existem pares de glifos que se comportam como variantes livres. `k`/`t`, `ch`/`sh`, `p`/`f` e as bancadas `cth`/`cph`/`cfh` aparecem em contextos quase idênticos, com similaridade de cosseno entre 0,94 e 0,99. `ckh` fica um pouco à parte (0,75 a 0,86), mas passa no teste seguinte. Também medi, nas palavras que só diferem por um desses glifos (`qokeedy`/`qoteedy`, `chedy`/`shedy`), quanto a proporção entre as duas formas varia de palavra para palavra dentro de um mesmo escriba. O índice de dispersão (qui² por grau de liberdade) fica entre 0,6 e 7,4. Esse índice vale 1 para variação livre pura. Pares que se comportam como letras distintas dão muito mais: `o`/`a` fica entre 18 e 39 e `d`/`l` entre 27 e 41. Em pares de letras latinas com pelo menos cinco exemplos, medi de 15 a 225.

O terceiro é que a linha e o parágrafo são unidades de composição. 82% das primeiras linhas de parágrafo têm `p` ou `f`; nas outras linhas, 9%. No RF, que não marca o início dos parágrafos curtos das receitas, esse segundo número sobe para 18%, porque parte das primeiras linhas passa a contar como linha comum. 83% dos parágrafos começam por um gallows: `p` em 45%, `t` em 23%, `k` em 10,5% e `f` em 4%. Uma palavra terminada em `-m` aparece em 15,6% dos fins de linha e em 0,9% do meio da linha. As iniciais `s-`, `d-` e `y-` são de 2 a 4 vezes mais comuns no começo da linha do que no meio.

O quarto é que A e B diferem na ortografia, não só no vocabulário. A sequência `ed` está em 0,3% das palavras de A e em 20,7% das de B; `-dy` em 6,5% contra 23,8%; `-ol` e `-or` somados em 24% contra 11%. A divisão acompanha os escribas: a mão 1 escreve A em 112 páginas, e as mãos 2, 3 e 5 escrevem B (a mão 3 tem só duas páginas em A). Os itens mais típicos de A são `cthor`, `cthol` e `cthy`; os de B, `qokeedy`, `chedy` e `otedy`.

O quinto está nos rótulos. Contei 1.177 palavras em 1.028 rótulos, concentrados no zodíaco (299), na seção farmacêutica (234) e na cosmológica (171). 54% começam com `o-` (no texto corrido, 20%) e 33% com `ok-` ou `ot-` (no texto, 11%). No zodíaco são 281 formas distintas em 345. Nas seções biológica e cosmológica, o rótulo reaparece no texto da mesma página cerca de três vezes mais que o acaso (21% contra 9%; 19% contra 6%). No zodíaco isso não acontece (9% contra 7%).

Há ainda um dado lateral que vou usar adiante: palavras idênticas seguidas (`chol chol`, `qokeedy qokeedy`) aparecem em 0,92% dos pares vizinhos. Com o texto embaralhado seriam 0,34%; no latim, 0,064%.

---

[Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 2 →](fase-02.md)
