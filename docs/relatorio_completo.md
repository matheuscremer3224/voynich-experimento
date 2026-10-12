# Manuscrito Voynich: uma tentativa própria de decifração (hipótese S)

> **Nota sobre caminhos.** Este é o relatório técnico integral, escrito pelo agente ao longo das 18 fases. Nos trechos que citam arquivos, `fase18/` corresponde a [`src/fase18/`](../src/fase18/) (código) e a [`results/fase-18/`](../results/fase-18/) (tabelas, critérios e pareceres). Os demais scripts estão em [`src/`](../src/) e as saídas em [`results/`](../results/). Termos técnicos: [glossário](glossario.md).


Antes de contar qualquer coisa, limpei os arquivos assim: descartei as linhas `#` e os comentários `<!…>`, herdei as variáveis de página em cada linha, apaguei `<%>` e `<$>`, tratei `<->` e `<~>` como espaço, fiquei com a primeira opção de cada `[a:b]`, contei cada `{…}` e cada `@NNN;` como uma unidade, rodei tudo com a vírgula valendo espaço e valendo junção, e tirei das contagens de vocabulário as palavras com `?`.

## Fase 1 – Análise própria

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

## Fase 2 – Hipóteses concorrentes

**H1: língua natural num alfabeto inventado** (palavra = palavra, glifo = letra). Explica o vocabulário rico e com cara de língua (tipo/ocorrência e hápax iguais aos do latim), as palavras típicas de cada seção e os rótulos que reaparecem no texto da própria página. Não explica a h2 baixa, a distribuição estreita de comprimentos, os pares de variantes livres nem, principalmente, o primeiro padrão. Numa língua escrita com espaços, a informação fica dentro da palavra, e no Voynich ela está atravessando o espaço.

**H2: silabário verboso e homofônico sobre o latim.** Aqui cada palavra Voynich é uma sílaba (ou grupo de letras), os pares `k`/`t`, `ch`/`sh`, `p`/`f` e as bancadas são grafias alternativas de um mesmo valor, e uma palavra latina ocupa uma ou mais palavras Voynich seguidas. Explica a h2 baixa e o comprimento estreito, porque cada sílaba segue um molde. Explica os homófonos. Vai na direção certa no primeiro padrão: descontado o controle, numa sequência de sílabas latinas a razão entre a informação através da fronteira e dentro da unidade é 0,6, bem acima do 0,09 das palavras latinas. Mesmo assim fica abaixo do 2,0 do Voynich. O `-m` de fim de linha vira um sinal de fecho de palavra, como as abreviaturas que os copistas concentravam no fim da linha. A/B vira uma diferença de preferência entre tabelas de homófonos de escribas diferentes. O que não explica bem: o latim dividido em sílabas tem tipo/ocorrência de 0,049, e o Voynich, mesmo depois de fundir os homófonos, fica em 0,169. Seriam precisas cerca de três grafias por sílaba além das que identifiquei. Também não explica rótulos de uma palavra só: um nome de planta ou de estrela teria várias sílabas.

**H3: sistema de notação ou classificação** (um código de tabela com prefixo de classe, núcleo e sufixo de ordem). Explica as casas fixas, a independência entre começo e fim da palavra, os rótulos do zodíaco quase todos distintos e com prefixo comum (`ot-`/`ok-`), as repetições e os gallows como cabeçalho de parágrafo. Não explica que 35 mil palavras de texto corrido tenham a distribuição de frequências e a riqueza de uma língua, nem que o vocabulário mude por seção como mudaria um assunto.

**Escolho H2.** É a única que dá conta do padrão mais estranho (o espaço que liga em vez de separar) e da estrutura de homófonos. E faz uma previsão dura e barata de testar: se as palavras são sílabas de palavras latinas, a ordem importa, e embaralhar as palavras tem de destruir as leituras de várias sílabas. O controle pedido na Fase 5 passa a ser, portanto, o teste decisivo da hipótese.

Onde ela coincide com propostas anteriores e onde diverge. A ideia de cifra verbosa com várias tabelas lembra a cifra "Naibbe" (Greshko, 2025), que gera texto com cara de Voynich a partir de latim ou italiano usando unidades de uma ou duas letras. Já a ideia de que cada palavra seja uma sílaba lembra a velha conjectura de uma língua monossilábica. A minha diverge em quatro pontos. A unidade é a sílaba, não a letra. As classes de homófonos foram medidas nos dados, e não supostas. A tabela é escolhida por um algoritmo e congelada antes de ler os trechos. E a ordem das palavras é usada como teste de falsificação. Não uso anagramas, micrografia nem leitura palavra a palavra.

## Fase 3 – A chave

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

## Fase 4 – Tradução

Legenda: ✓ lida, ? incerta, ✗ não resolvida. ∅ marca uma palavra que não decodifica (algum pedaço não tem valor). Na coluna intermediária, as formas atestadas estão em negrito, e o sinal + junta palavras Voynich que formaram uma só palavra latina. Quando o ZL e o RF divergem, adotei sempre o ZL, com a vírgula valendo espaço, e cito abaixo de cada tabela as divergências que mudam a leitura.

**a) f1r, primeiro parágrafo (linhas 1 a 6)**

| Linha | EVA | Forma intermediária (latim decodificado) | Português |
|---|---|---|---|
| f1r.1 | fachys ykal ar ataiin shol shory cthres y.kor sholdy | luepet · otuus · us · utunt · **eius** · eimis · cmret · **is+tis** · einum | —✗ · —✗ · —✗ · —✗ · dele✓ · —✗ · —✗ · a-estes✓ · —✗ |
| f1r.2 | sory ckhar or y kair chtaiin shar ase cthar cthar dan | gimis · cus · as · **is** · **tum** · etunt · eus · ∅ · cus · cus · suen | —✗ · —✗ · —✗ · ele/vais✓ · então✓ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ |
| f1r.3 | syaiir sheky or ykaiin shod cthoary cthes daraiin sy | gpur · ertis · as · otunt · eiam · ciumis · cret · **sumunt** · gis | —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · tomam✓ · —✗ |
| f1r.4 | soiin oteey oteos roloty cthiar daiin okaiin or okan | gint · atdis · atriet · minitis · ∅ · **sunt** · atunt · as · atuen | —✗ · —✗ · —✗ · —✗ · —✗ · são✓ · —✗ · —✗ · —✗ |
| f1r.5 | sair y chear cthaiin cphar cfhaiin | gum · **is** · erus · cunt · cus · cunt | —✗ · ele/vais✓ · —✗ · —✗ · —✗ · —✗ |
| f1r.6 | ydaraishy | ∅ | —✗ |

Palavras: 46. Lidas 8 (17%), incertas 0 (0%), não resolvidas 38 (83%).

Divergências. Em f1r.5, o ZL tem `sair,y`, que dá *gum* + *is* (✓); o RF tem `sairy`, que dá *gubis* (✗). Em f1r.2, o ZL tem `or,y` (*as* + *is*), e o RF `ory`, que dá *amis* (✗). Em f1r.1, o ZL traz `[cth:oto]res` (adotei `cth`) e o RF `ctoses`; nenhuma das duas resolve. Lido em sequência, o parágrafo dá "dele … a estes / ele … então / … tomam / … são / … ele". Não sai uma oração.

**b) f2r, página herbal com rótulo e desenho**

| Linha | EVA | Forma intermediária (latim decodificado) | Português |
|---|---|---|---|
| f2r.1 | kydainy ypchol daiin otchal ypchaiin ckholsy | ∅ · oleius · **sunt** · ateuus · oleunt · cingis | —✗ · —✗ · são✓ · —✗ · —✗ · —✗ |
| f2r.2 | dorchory chkar s shor cthy {cto} | simeimis · etus · **et** · **eis** · **cis** · ∅ | —✗ · —✗ · e✓ · a-eles✓ · aquém✓ · —✗ |
| f2r.3 | qotaiin cthey y chor chy ydy chaiin | quitunt · cris · **is** · **eis** · **eis** · oum · **eunt** | —✗ · —✗ · ele/vais✓ · a-eles✓ · a-eles✓ · —✗ · vão✓ |
| f2r.4 | {c'o}aiidy chtod dy cphy dals chokaiin d | ∅ · **etiam** · um · **cis** · sunet · eitunt · am | —✗ · também✓ · —✗ · aquém✓ · —✗ · —✗ · —✗ |
| f2r.5 | otochor al shodaiin chol dan ytchaiin dan | atieis · uus · eisunt · **eius** · suen · oteunt · suen | —✗ · —✗ · —✗ · dele✓ · —✗ · —✗ · —✗ |
| f2r.6 | saiin dain d dkol sor ytoldy dchol dchy cthy | gunt · suit · am · stius · gis · otinum · seius · seis · **cis** | —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · aquém✓ |
| f2r.7 | shor ckhy daiiny chol dan | **eis** · **cis** · ∅ · **eius** · suen | a-eles✓ · aquém✓ · —✗ · dele✓ · —✗ |
| f2r.8 | kydain shaiin qoy s shol fodan yksh olsheey daiildy | tpsuit · **eunt** · quiis · **et** · **eius** · lisuen · ∅ · anedis · ∅ | —✗ · vão✓ · —✗ · e✓ · dele✓ · —✗ · —✗ · —✗ · —✗ |
| f2r.9 | dls sho kol sheey qokey ykody so chol yky dain daiisol | snet · **ei** · tius · **edis** · quitris · **otium** · gi · **eius** · otis · suit · ∅ | —✗ · a-ele✓ · —✗ · do-templo/comes✓ · —✗ · ócio✓ · —✗ · dele✓ · —✗ · —✗ · —✗ |
| f2r.10 | qo'ky cholaiin shol sheky daiin cthey keol saiin e'a'iin | ∅ · einunt · **eius** · ertis · **sunt** · cris · trius · gunt · ∅ | —✗ · —✗ · dele✓ · —✗ · são✓ · —✗ · —✗ · —✗ · —✗ |
| f2r.11 | ychain dal chy dalor shan dan olsaiin sheey ckhor | oeuit · **suus** · **eis** · sunis · euen · suen · angunt · **edis** · **cis** | —✗ · seu✓ · a-eles✓ · —✗ · —✗ · —✗ · —✗ · do-templo/comes✓ · aquém✓ |
| f2r.12 | okol chy chor cthor yor an chan saiin chety chyky sal | atius · **eis** · **eis** · **cis** · ois · uen · euen · gunt · ertis · eptis · guus | —✗ · a-eles✓ · a-eles✓ · aquém✓ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ |
| f2r.13 | sho ykeey chey daiin chcthy | **ei** · otdis · **eris** · **sunt** · ecis | a-ele✓ · —✗ · serás✓ · são✓ · —✗ |
| f2r.14 (rótulo) | ytoail | ∅ | —✗ |
| f2r.15 (rótulo) | ios an on | ∅ · uen · aen | —✗ · —✗ · —✗ |

Palavras: 105. Lidas 34 (32%), incertas 0 (0%), não resolvidas 71 (68%).

Conferência no PDF. A planta tem três cabeças de flor com brácteas e florzinhas cor de palha (como uma centáurea ou um cardo), folhas recortadas em lobos pontudos, caule avermelhado e raiz vermelha ramificada. O rótulo `ytoail` está na ponta de uma folha do lado direito. A leitura não combina com a figura. O rótulo fica não resolvido, porque o último pedaço (`il`) não tem valor. O texto vira uma sopa de pronomes e verbos de ligação (*eius, eis, sunt, cis, et*), sem nenhuma palavra de planta (*herba, folium, flos, radix, semen*). O segundo rótulo (`ios.an.on`) não consegui localizar na imagem, nesta resolução, e ele também não resolve.

Divergências. Em f2r.4, o ZL tem `chtod,dy` (*etiam* + *um*) e o RF `chtoddy` (*etisum*, ✗); portanto o *etiam* depende de uma vírgula. Em f2r.9, o ZL tem `dls,sho` (… + *ei* ✓) e o RF `dlssho` (✗); o ZL tem `chol,yky` (*eius* ✓ + *otis*) e o RF `cholyky` (✗). Diferenças só entre `k` e `t`, como `chokaiin`/`chotaiin`, desaparecem pela R1.

**c) f71r, rótulos do zodíaco (Áries claro)**

| Linha | EVA | Forma intermediária (latim decodificado) | Português |
|---|---|---|---|
| f71r.2 (rótulo) | oteos arar | atriet · umus | —✗ · —✗ |
| f71r.3 (rótulo) | okldam | atnsuer | —✗ |
| f71r.4 (rótulo) | oteoaldy | atriunum | —✗ |
| f71r.5 (rótulo) | oteolar | atrinus | —✗ |
| f71r.6 (rótulo) | okeoaly | atriunis | —✗ |
| f71r.7 (rótulo) | otaleky | atunrtis | —✗ |
| f71r.8 (rótulo) | otalsar | atungus | —✗ |
| f71r.9 (rótulo) | cheary | erumis | —✗ |
| f71r.10 (rótulo) | oteotey rary | atritris · mumis | —✗ · —✗ |
| f71r.11 (rótulo) | otalaly | atununis | —✗ |
| f71r.13 (rótulo) | otolchdy | atineum | —✗ |
| f71r.14 (rótulo) | otoloaram | atiniumuer | —✗ |
| f71r.15 (rótulo) | oteeol | atdius | —✗ |
| f71r.16 (rótulo) | otolchd | atineam | —✗ |
| f71r.17 (rótulo) | otaldar | atunsus | —✗ |

Palavras: 17. Lidas 0 (0%), incertas 0 (0%), não resolvidas 17 (100%).

Conferência no PDF. No centro há um carneiro claro, e embaixo dele está escrito *abril* em letra latina, por outra mão. Há 15 figuras femininas em dois anéis (10 por fora, 5 por dentro), a maioria dentro de tinas listradas, cada uma segurando uma estrela; o rótulo sai da estrela. Não combina: nenhum dos 15 rótulos é lido. Todos começam por *at-* (o `o-` inicial vale *a* e `t` vale *t*), que é o prefixo `ot-`/`ok-` do quinto padrão. O resto não forma nome de estrela, número nem dia. Divergências: em f71r.10, o ZL tem `oteotey.rary` e o RF `oteokey.sary` (a primeira palavra fica igual pela R1; *mumis*/*gumis*, ambas ✗). Em f71r.17, o ZL tem `otaldar` (✗) e o RF `otal.dar`, onde `dar` sai *sus*, "porco" (✓). É exatamente o tipo de acerto casual que a R5 impede de virar interpretação.

**d) f103r, sexto parágrafo da seção de receitas (linhas 18 a 20)**

| Linha | EVA | Forma intermediária (latim decodificado) | Português |
|---|---|---|---|
| f103r.18 | polchedy qokeol okain checthy oteeylshedy okain qokain qokalshedy oteys | linerum · quitrius · atuit · ercis · atdpnerum · atuit · quituit · quitunerum · atrpet | —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ |
| f103r.19 | okaiin chey qoy shey qokaiin chedy qokain oteol lkar okaral lkldy lr | atunt · **eris** · quiis · **eris** · quitunt · **erum** · quituit · atrius · ntus · atumuus · ntnum · ns | —✗ · serás✓ · —✗ · serás✓ · —✗ · o-senhor? · —✗ · —✗ · —✗ · —✗ · —✗ · —✗ |
| f103r.20 | ychain shckhy qokaiin shey qokaiin shedy olor | oeuit · ecis · quitunt · **eris** · quitunt · **erum** · anis | —✗ · —✗ · —✗ · serás✓ · —✗ · o-senhor? · —✗ |

Palavras: 28. Lidas 3 (11%), incertas 2 (7%), não resolvidas 23 (82%).

f103r é uma página só de texto, com uma estrela na margem esquerda marcando cada parágrafo; este é o sexto. Divergências: `qokalshedy`/`qotalshedy` (f103r.18) e `okaral`/`otaral` (f103r.19) ficam iguais pela R1. `oteol`/`oteal` (f103r.19) dão *atrius*/*atruus*, ambas ✗.

## Fase 5 – Teste

Escolhi como trechos novos o f4r (herbal, A, mão 1) e o f78r (biológica, B, mão 2). Nenhum dos dois entrou no treino nem na Fase 4. Abaixo, os resultados no ZL com a vírgula valendo espaço; os controles usam 200 sorteios cada.

No **f4r**, 39,1% das palavras dão forma latina atestada, todas "lidas". Com a ordem das palavras embaralhada, dá 39,1% ± 0,2%. Em nenhum caso duas palavras Voynich se juntaram numa palavra latina.

No **f78r**, deu 24,1% (16,6% lidas e 7,6% incertas), com 3,4% das palavras em grupos de várias palavras. Embaralhado, 21,9% ± 0,6% (1,1% em grupos). São 2,2 pontos de diferença, e nenhum sorteio alcança o texto real. Só que a diferença vem de cinco grupos (`ol.tedy` e `ol.kedy` → *austrum* três vezes, `ched.ar` → *eramus*, `o.l` → *ius*), e três deles atravessam um espaço que o ZL marca como incerto. Com a vírgula valendo junção, o f78r cai para 20,4% contra 19,5% ± 0,4% (P = 0,07). No RF, 25,4% contra 24,4% ± 0,6% (P = 0,09).

Para ter mais potência, apliquei a chave às 20.239 palavras de parágrafo que ficaram fora do treino. Deu 23,0% no texto real contra 22,5% embaralhado (+0,5 ponto; grupos de várias palavras: 1,2% contra 0,7%). Com a vírgula valendo junção, a diferença cai para +0,2 ponto. Os +0,5 ponto são estatisticamente detectáveis: nenhum dos 30 sorteios chega lá. Mas uma chave "nula", treinada pelo mesmo algoritmo no texto já embaralhado, também dá um efeito do mesmo tipo (+0,1 e 0,0). Parte da diferença vem, portanto, da própria estrutura sequencial do Voynich, e não do latim. Embaralhando os glifos dentro de cada palavra, a validade cai para 8% a 9%. Isso só mostra que a tabela foi ajustada à forma das palavras voynichianas; não diz nada sobre significado.

O controle positivo mostra o que a hipótese previa. Pego latim de Isidoro, cifro por sílabas com uma chave conhecida e decifro com o mesmo algoritmo: dá 77,4% em ordem real contra 48,4% embaralhado, com 49,5% das palavras em grupos de várias sílabas. Com a chave verdadeira, 95,2% contra 54,8%.

**A conclusão é clara: a chave funciona praticamente igual no controle.** A diferença entre real e embaralhado ficou entre 0,2 e 0,5 ponto, quando a hipótese previa cerca de 29. E as leituras de várias sílabas, que eram o coração da hipótese, quase não existem (cerca de 1%, contra cerca de 50%). O que aparece como leitura são palavras Voynich frequentes associadas uma a uma a palavras latinas curtas.

Dois sintomas internos confirmam. O texto decodificado inteiro tem só 256 formas latinas distintas; cinco delas fazem 46% das leituras; *est* nunca aparece e *in* aparece em 0,03% das palavras, quando no latim são 2,2% e 2,4%. E a nota de "latinidade" da chave (+0,044 bit por letra acima da média do latim) não quer dizer latim. O texto decodificado tem h2 de 2,47 bits, contra 3,51 do latim sem espaços: é previsível demais, e é isso que o modelo de trigramas premia. As duas primeiras derivações mostram o mesmo de outro ângulo: o otimizador treinado no texto embaralhado alcançou a mesma cobertura que o treinado no texto real (61,7% contra 61,9% na primeira; 43,8% contra 40,7% na segunda).

## Fase 6 – Interpretação

Separo o que digo em três camadas.

**O que a chave leu.** Quase nada que sustente uma interpretação. Os trechos viram sequências de pronomes, verbos de ligação e partículas (*sunt, eius, eis, et, cis, eris*). Não há uma frase gramatical, nenhuma palavra de planta no herbal, nenhum nome de estrela no zodíaco, nenhuma medida ou verbo de preparo na receita. Pelo teste da Fase 5, isso é ruído, e não uso nenhuma dessas leituras como evidência.

**O que a análise mostra sem depender da chave.** Isto é resultado do método, com confiança moderada. O texto foi composto em unidades fixas: o parágrafo abre com um gallows, a linha fecha com `-m` e tem começo próprio (`s-`, `d-`, `y-`). Isso é típico de um texto copiado de um modelo e diagramado, não improvisado na página. Há dois sistemas de escrita do mesmo tipo, A e B, que coincidem com escribas diferentes. A mão 1 escreveu o herbal A e a seção farmacêutica. A mão 2 fez a seção biológica e parte do herbal B; a 3, as receitas e outra parte do herbal B; a 5, mais algumas páginas do herbal B. A mão 4 fez os diagramas astronômicos, cosmológicos e o zodíaco. Os rótulos se comportam de dois jeitos. No zodíaco são formas quase todas únicas, com prefixo comum. Nas seções biológica e cosmológica são palavras que o texto ao lado repete, como legendas que remetem ao parágrafo.

**A minha melhor aposta (palpite).** O livro é um compêndio prático de medicina natural, na linha dos *tacuina* e dos livros de segredos do começo do século XV. Ele tem um herbário de plantas medicinais, uma página por planta, com nome, partes e virtudes (seção herbal). Tem um guia de banhos e águas medicinais (seção biológica, com as figuras em tinas e canais). Tem um calendário de medicina astrológica: as 30 figuras por signo seriam os 30 graus ou dias, cada um com seu rótulo, dizendo quando convém sangrar, colher ou tomar um banho. A seção astronômica e a cosmológica trariam os diagramas do céu e dos elementos que sustentam esse calendário. A farmacêutica mostra partes de plantas e frascos rotulados, isto é, os ingredientes já preparados. E a última seção é um receituário em entradas curtas, uma por estrela. Quem o fez foi uma oficina de pelo menos cinco copistas, trabalhando para um autor ou encomendante que dominava herbário, banhos e astrologia médica, provavelmente um médico ou boticário da Europa central ou do norte da Itália. Os nomes dos meses em grafia românica (como o *abril* do f71r) indicam um usuário de fala românica em algum momento da vida do livro. O destinatário seria esse mesmo praticante e a sua casa: um livro de uso privado, com receitas e calendários de valor comercial ou de reputação, numa escrita que um aprendiz da casa aprenderia e um estranho não.

## Fase 7 – Veredito

Na **chave**, minha confiança é muito baixa, cerca de 2%: o teste decisivo falhou, e o controle positivo mostra que, com a hipótese certa e uma chave certa, a diferença seria de dezenas de pontos. Na **tradução**, a confiança é praticamente nula, abaixo de 1%: as formas "lidas" são palavras curtas e frequentes que o texto embaralhado também produz. Na **interpretação**, ela é moderada (cerca de 40%) quanto à função geral do livro, porque se apoia nas figuras e na estrutura, não na chave, e baixa (cerca de 15%) quanto a autoria e público. A **hipótese S** em si (palavra Voynich = sílaba latina com homófonos) eu rebaixo para cerca de 5%. O padrão que a motivou continua de pé (o espaço liga mais do que separa), mas a forma "sílaba de latim" não produziu a assinatura que deveria.

O que derrubaria a hipótese, em parte já derrubou: a falta de leituras de várias sílabas que dependam da ordem é a refutação que obtive para a minha chave. Ela cai de vez se uma derivação mais forte, com um modelo de palavras latinas e não só de trigramas, também não abrir distância entre o texto real e o embaralhado. A R1 cai se a proporção entre `k` e `t`, ou entre `ch` e `sh`, mudar de forma sistemática com o assunto dentro da mesma mão, porque aí eles seriam letras e não grafias. E o "sinal de fecho" deixa de ser posicional se `-m` aparecer no meio de linhas longas tanto quanto no fim.

O próximo experimento seria construir geradores silábicos homofônicos (de 2 a 4 grafias por sílaba) sobre latim, italiano do norte e occitano ou catalão (por causa dos meses), e ver se algum deles reproduz ao mesmo tempo os cinco padrões da Fase 1: h2 perto de 2,2, mais informação através do espaço do que dentro da palavra, razão tipo/ocorrência de 0,21, o fecho de linha e a divisão A/B. Se nenhum reproduzir o primeiro padrão sem estragar os outros, a família de hipóteses silábicas está descartada, e a próxima candidata seria a H3, um código de tabela em que o espaço separa campos e não sílabas.

## Resumo

**Hipótese:** o Voynich seria um silabário verboso e homofônico sobre o latim (palavra = sílaba; `k`/`t`, `ch`/`sh`, `p`/`f` e as bancadas são grafias de um mesmo valor; A e B são tabelas de escribas diferentes).

**Melhor frase traduzida:** f2r.2 `s<->shor.cthy` (com a interrupção de figura `<->` valendo espaço) → *et eis cis* → "e, a eles, aquém", três palavras lidas seguidas que não formam oração.

**Teste:** no trecho novo f78r, 24,1% de palavras válidas contra 21,9% com a ordem embaralhada (f4r: 39,1% contra 39,1%; fora do treino: 23,0% contra 22,5%), quando um latim cifrado de verdade daria 77% contra 48%.

**Confiança:** chave ≈ 2%, tradução < 1%, interpretação geral ≈ 40%.

**Ponto mais fraco:** a chave lê o texto embaralhado tão bem quanto o original. As suas "palavras lidas" são palavras latinas curtas e frequentes postas uma a uma, não latim.

## Fase 8 – Continuação: os experimentos que ficaram em aberto

Rodei os testes que a Fase 7 deixou pendentes, mais dois que eles mesmos pediram. As regras de cada teste, e o critério de queda, foram fixados antes de rodar.

**8.1 Onde o espaço cai.** Tirei os espaços do texto e tentei recolocá-los só pelo contexto local de glifos, com um modelo treinado nas linhas pares e testado nas ímpares. Fiz o mesmo exercício com o mesmo texto latino cortado de vários jeitos:

| Corte | Razão MI junção / MI dentro | F1 ao recolocar o espaço | Incerteza que sobra |
|---|---|---|---|
| Voynich (vírgula = espaço) | 2,0 | 0,90 | 25% |
| Latim, espaço entre palavras | 0,09 | 0,77 | 49% |
| Latim, espaço entre sílabas da palavra | 0,62 | 0,90 | 33% |
| Latim, sílabas de um fluxo sem espaços | 1,51 | 0,97 | 18% |
| Latim, corte depois de cada vogal | 5,3 | 1,00 | 13% |
| Latim, pedaços fixos de 3 letras | 3,0 | 0,17 | ≈100% (o contexto não ajuda) |

O espaço voynichiano é bem mais previsível que o espaço entre palavras latinas. O corte latino que mais se parece com ele, nas duas medidas ao mesmo tempo, é a divisão em sílabas de um texto corrido sem fronteiras de palavra: sílabas que atravessam as palavras (*et in* → *e·tin*). Medi também o tipo de dependência entre vizinhos. A ligação é da junção (fim de uma palavra → começo da seguinte: 0,199 bit), muito mais que de começo com começo (0,076) ou de fim com fim (0,017). Ou seja, não parece cópia de uma palavra para a seguinte; parece uma regra de emenda entre pedaços de um fluxo contínuo. Um terceiro experimento reforça isso. Cifrei latim usando como livro de código o próprio vocabulário voynichiano, com as frequências reais, e cada unidade latina (letra, par de letras, sílaba ou palavra) recebendo grafias arbitrárias. Em todos os casos a dependência na junção some (0,00 bit) e a repetição imediata cai para 0,11–0,18%. Uma cifra de código arbitrário, do tipo nomenclátor, não produz o padrão 1: ele exige que a grafia obedeça a regras de glifo nas bordas das palavras.

**8.2 Variante S′.** Isso pedia uma última chance para a família silábica. Se as sílabas atravessam as palavras, a minha R4 (uma palavra latina = palavras Voynich inteiras e seguidas) estaria errada mesmo com a chave certa. Na S′, a linha decodificada vira uma cadeia contínua de letras e é segmentada letra a letra. Fixei a métrica antes: fração das letras cobertas por palavras atestadas de quatro letras ou mais. A tabela é a mesma, congelada.

No controle positivo (Isidoro silabado como fluxo contínuo e cifrado), a chave verdadeira dá 75,3% em ordem real contra 32,0% embaralhado (+43 pontos). A chave que o meu algoritmo recupera sozinho, acertando 32 dos 39 valores, dá 69,0% contra 32,9% (+36 pontos). Em italiano (Europarl), a chave verdadeira dá 68,2% contra 14,2% (+54 pontos). O método, portanto, tem força de sobra para ver uma cifra silábica de fluxo contínuo.

No Voynich, com a chave latina, deu 45,3% no texto real contra 44,6% embaralhado (+0,7 ponto), nas 20 mil palavras fora do treino. A chave nula, treinada no texto embaralhado, dá +1,4: mais que a chave "boa". No f78r deu +3,3 e no f4r +2,3 (P = 0,20). Re-derivei a chave do zero para italiano e alemão (Europarl), com o mesmo algoritmo, o mesmo treino e as terminações mais comuns de cada língua. Italiano: 22,0% contra 20,9% (+1,1 ponto). Alemão: 22,7% contra 22,0% (+0,8); no f78r, o texto embaralhado chega a ganhar (−2,9). Nas três línguas a diferença fica do tamanho da que a chave nula produz, dezenas de vezes menor que a dos controles positivos (+36 a +54 pontos).

**8.3 A R1 (homófonos) cai.** Comparei a proporção entre as duas formas, nas mesmas palavras-par, entre seções de uma mesma mão. Na mão 1, `k` responde por 52% dos pares `k`/`t` no herbal e por 82% na seção farmacêutica (qui² 89,7 com 1 g.l.). Na mão 2, 72% no herbal, 72% na biológica e 58% no texto corrido (qui² 26,8 com 2 g.l.). Em `ch`/`sh`, a mão 1 não muda de forma significativa (64% contra 69%, qui² 3,6), mas a mão 2 muda (70%, 54%, 57%; qui² 24,5). Pelo critério que eu mesmo fixei, `k` e `t` não são grafias livres do mesmo valor. São variantes condicionadas, pelo assunto ou pelo momento da cópia, ou letras distintas de distribuição muito parecida. A fusão `k` = `t` da chave estava errada.

**8.4 O `-m` de fim de linha sobrevive e fica mais claro.** A chance de a linha terminar em `-m` cresce com o comprimento da linha: 8,5% no quarto mais curto, 10,8%, 17,4% e 25,5% no quarto mais longo. Nas últimas linhas de parágrafo, que costumam ser curtas, cai para 9,2%, contra 16,7% nas linhas comuns. Antes de uma interrupção de figura, no meio da linha, fica em 2,4%, contra 1,1% nas demais palavras. Além disso, o radical de uma palavra final em `-m` aparece no meio da linha sobretudo com `-iin` (52% dos casos), `-l` (20%), `-r` (15%) e `-in` (10%): `dam` ↔ `daiin`, `am` ↔ `aiin`, `otam` ↔ `otaiin`, `qokam` ↔ `qokaiin`. O `-m` é uma forma comprimida de `-iin`, `-l` e `-r`, usada quando falta espaço na margem direita, exatamente como as abreviaturas de fim de linha dos copistas. É um fato do sistema de escrita, que vale qualquer que seja a língua. A minha chave, aliás, deu valores diferentes para `-m` (*er*) e `-iin` (*nt*), mais um sinal de que está errada.

**8.5 Os rótulos do zodíaco não formam série.** Se fossem números ou nomes de dias em código, rótulos vizinhos no círculo deveriam ser mais parecidos entre si. A distância normalizada é 0,662 entre vizinhos, 0,679 entre não vizinhos da mesma página e 0,713 entre páginas diferentes. A diferença entre vizinhos e não vizinhos não chega a ser significativa (P = 0,054). Há um parentesco por página, não uma sequência.

**8.6 Veredito revisto.** Fica assim:

A **hipótese S**, com sílabas latinas alinhadas às palavras, está descartada. A **variante S′**, com sílabas de um fluxo contínuo, também está descartada, com latim, italiano e alemão. A **R1** caiu.

O que sobrevive são resultados estruturais, sem depender de chave. O espaço voynichiano se comporta como um corte silábico de um fluxo sem fronteiras de palavra (confiança moderada, cerca de 50%). Existe uma regra de emenda entre pedaços vizinhos. O `-m` é abreviatura de fim de linha (cerca de 70%). As variantes `k`/`t` e `ch`/`sh` dependem da seção dentro da mão.

Restam três explicações, e não consigo separá-las com o que tenho. Primeira: uma notação silábica de uma língua que não testei. Segunda: uma notação silábica cuja correspondência não é uma tabela fixa (valores que mudam com a seção, como os próprios `k`/`t` sugerem). Terceira: um texto sem conteúdo linguístico, gerado por regras de aparência silábica. As duas primeiras manteriam viva a interpretação do livro como compêndio médico; a terceira a tornaria um objeto de outra natureza (um livro feito para parecer cifrado).

Minha confiança fica em cerca de 1% para a chave, abaixo de 1% para a tradução e em cerca de 40% para a interpretação geral, que continua apoiada nas figuras.

O próximo passo útil seria derivar tabelas separadas para A e B (e por mão), já que `k`/`t` não são livres, e repetir o teste da ordem. Depois, estender a busca a outras línguas candidatas, a começar por occitano ou catalão, por causa dos meses.

## Resumo atualizado

**Hipótese:** a família silábica (S e S′) caiu para latim, italiano e alemão. O que fica é estrutural: o espaço é um corte silábico num fluxo sem fronteiras de palavra, com uma regra de emenda entre os pedaços e uma abreviatura de fim de linha (`-m` no lugar de `-iin`, `-l` e `-r`).

**Melhor frase traduzida:** continua sendo f2r.2 → *et eis cis*, e continua sem valor de prova.

**Teste:** com a segmentação contínua, +0,7 ponto em latim, +1,1 em italiano e +0,8 em alemão, contra +36 a +54 nos controles positivos; a chave nula, treinada em texto embaralhado, dá +1,4.

**Confiança:** chave ≈ 1%, tradução < 1%, espaço como corte silábico ≈ 50%, `-m` como abreviatura ≈ 70%, interpretação geral do livro ≈ 40%.

**Ponto mais fraco:** só testei tabelas fixas e três línguas. Uma tabela que mude por seção, ou uma língua que não testei, ainda escapam.

## Fase 9 – Tabelas por dialeto e mais três línguas

Na Fase 8 a R1 caiu: `k`/`t` e `ch`/`sh` mudam de proporção com a seção, dentro da mesma mão. Com isso ficaram duas saídas para a família silábica, e testei as duas com as mesmas regras e o mesmo critério de antes.

A primeira saída é uma tabela que muda conforme o dialeto. Derivei do zero uma tabela só para A e outra só para B, sem fundir glifo nenhum (`k`, `t`, `p`, `f`, `ch`, `sh` e as quatro bancadas, cada um com valor próprio). Usei o mesmo algoritmo, o latim como alvo, 1.000 linhas de treino em A e 1.600 em B. O teste foi feito nas linhas de cada dialeto que ficaram fora do treino (3.794 palavras em A e 7.642 em B).

A segunda saída é outra língua. Re-derivei a tabela global, também sem fundir glifos, para catalão (AnCora), francês antigo (SRCMF, textos medievais como a *Chanson de Roland*) e occitano (TTB). Os três corpora vêm dos treebanks Universal Dependencies. Antes de olhar o Voynich, rodei o controle positivo de cada língua com a chave verdadeira, isto é, o próprio texto silabado como fluxo contínuo, para ver se o método enxergaria uma cifra desse tipo:

| Teste | Métrica S′ (contínua): real × embaralhado | Métrica R4 (palavras inteiras): real × embaralhado |
|---|---|---|
| Controle positivo catalão (chave verdadeira) | 64,9% × 19,7% (+45,2) | — |
| Controle positivo francês antigo | 66,7% × 33,4% (+33,3) | — |
| Controle positivo occitano | 45,3% × 10,9% (+34,3) | — |
| Voynich A, tabela só de A (latim, sem R1) | 41,5% × 40,3% (+1,1) | 17,5% × 17,3% (+0,2) |
| Voynich B, tabela só de B (latim, sem R1) | 35,4% × 34,1% (+1,3) | 15,6% × 15,5% (+0,1) |
| Voynich, tabela catalã | 39,0% × 38,6% (+0,5) | 12,7% × 12,7% (0,0) |
| Voynich, tabela de francês antigo | 50,8% × 49,2% (+1,6) | 21,0% × 20,8% (+0,1) |
| Voynich, tabela occitana | 26,9% × 25,2% (+1,7) | 11,6% × 11,3% (+0,3) |

O resultado é o mesmo das Fases 5 e 8. Separar os dialetos e parar de fundir glifos não faz aparecer nada. Trocar a língua por um romance medieval, ou por uma das línguas sugeridas pelos nomes dos meses, também não. A diferença entre a ordem real e a embaralhada fica entre +0,5 e +1,7 ponto na métrica contínua e entre 0,0 e +0,3 na de palavras inteiras, do tamanho da que uma chave treinada em texto embaralhado produz (+1,4). Num texto cifrado de verdade, ela seria de 33 a 54 pontos.

**Onde isso deixa o problema.** A família silábica de tabela fixa está descartada em seis línguas (latim, italiano, alemão, catalão, francês antigo, occitano), com tabela única ou com uma tabela por dialeto. Nenhum resultado estrutural mudou: o espaço como corte silábico de um fluxo contínuo, a regra de emenda na junção e o `-m` de fim de linha. Das três explicações da Fase 8, a primeira (uma língua que não testei) perdeu força, porque as línguas mais plausíveis para a época e o lugar já foram. Sobram as outras duas. Pode ser uma notação cuja correspondência muda mais do que por dialeto (por página, por posição na linha ou por uma regra de contexto). Ou pode ser um texto sem conteúdo linguístico, feito com regras de aparência silábica. Com testes de tabela fixa, não consigo mais distinguir entre essas duas.

**O que eu faria a seguir, se fosse continuar.** Testaria a segunda explicação contra a terceira diretamente, em vez de buscar mais chaves. Construiria um gerador sem conteúdo (palavras montadas pela gramática de casas da Fase 1, com regra de emenda na junção e `-m` por falta de espaço) e mediria se ele reproduz também o que é mais difícil de imitar sem significado. Isso inclui os rótulos das seções biológica e cosmológica, que reaparecem três vezes mais que o acaso no texto da própria página, e o vocabulário que muda com o assunto. Se o gerador reproduzir tudo, a hipótese de texto sem língua passa a ser a mais econômica. Se falhar justamente nos ecos entre rótulo e texto, a hipótese de notação com significado continua de pé, mas com uma correspondência que nenhuma tabela fixa capta.

## Resumo atualizado (Fase 9)

**Hipótese:** a notação silábica de tabela fixa está descartada em seis línguas, com ou sem tabelas por dialeto. O que fica são três fatos estruturais: o espaço como corte silábico de um fluxo contínuo, a regra de emenda na junção e o `-m` como abreviatura de fim de linha.

**Melhor frase traduzida:** nenhuma das novas tabelas produziu uma frase melhor que f2r.2 → *et eis cis*, que continua sem valor de prova.

**Teste:** a diferença entre ordem real e embaralhada ficou entre 0,0 e 1,7 ponto em todas as variantes, contra 33 a 54 pontos nos controles positivos.

**Confiança:** chave < 1%, tradução < 1%, estrutura do espaço ≈ 50%, `-m` como abreviatura ≈ 70%, interpretação geral do livro ≈ 35%. Baixei esta última um pouco, porque a explicação de texto sem língua ganhou peso relativo.

**Ponto mais fraco:** todos os testes supõem uma correspondência estável dentro de cada dialeto. Uma notação que muda por página ou por contexto passaria por eles sem ser vista.

## Fase 10 – Significado ou texto sem língua?

Até aqui, nenhuma tabela fixa leu o texto, e restaram duas explicações: uma notação com significado, cuja correspondência nenhuma tabela fixa capta, ou um texto sem conteúdo linguístico. Nesta fase tentei separar as duas. Construí geradores de texto sem conteúdo, apliquei a eles a mesma bateria de medidas usada no Voynich e fiz dois testes calibrados com um texto de significado conhecido.

**10.1 Um gerador sem conteúdo imita quase tudo.** O G-casas2 monta palavras com uma cadeia de Markov sobre as unidades de glifo, ajustada por seção e por dialeto. Tem seis regras mecânicas: emenda na junção (a primeira unidade depende da última da palavra anterior); começos próprios de linha e de parágrafo; preenchimento até a largura da linha real; `-m` por falta de margem; repetição ocasional da palavra anterior; e rótulos gerados à parte. O gerador é ajustado ao próprio Voynich, então reproduzir as estatísticas locais não prova nada sozinho; o que interessa é onde ele falha. Para comparação, o G-cópia faz "autocitação": cada palavra nova é, quase sempre, uma cópia modificada de uma palavra já escrita na página.

| Medida | Voynich | G-casas2 (sem conteúdo) | G-cópia (autocitação) |
|---|---|---|---|
| h2 (bits) | 2,14 | 2,15 | 2,43 |
| comprimento médio (unidades) | 4,45 | 4,38 | 4,55 |
| razão tipo/ocorrência | 0,205 | 0,214 | 0,289 |
| MI na junção ÷ MI dentro da palavra | 2,02 | 2,10 | 1,09 |
| F1 ao recolocar o espaço | 0,90 | 0,89 | 0,88 |
| repetição imediata | 0,92% | 1,15% | 0,39% |
| `-m` no fim: linhas curtas / longas / meio da linha | 8,6% / 25,3% / 0,9% | 6,5% / 19,1% / 0,9% | 10,9% / 13,4% / 2,6% |
| parágrafo começa com gallows | 82% | 82% | 46% |
| `ed` em A / em B | 0,3% / 20,7% | 0,1% / 20,3% | 5,9% / 13,5% |
| divergência herbal × biológica (JS) | 0,399 | 0,387 | 0,391 |
| rótulo reaparece no texto da página / de outra página | 11% / 7% | 23% / 14% | 32% / 10% |

Com poucas regras e nenhum significado, o G-casas2 reproduz a entropia, o comprimento, a riqueza de vocabulário, o espaço como corte silábico, a regra de emenda, o `-m` de margem, os gallows de parágrafo, a divisão A/B e a diferença entre seções. Ele erra para mais no eco dos rótulos (23% contra 11%), porque gera rótulos curtos e comuns demais.

**10.2 Os rótulos não se comportam como nomes.** Num texto com significado, o rótulo de uma figura (o nome da planta, da estrela, do frasco) deveria reaparecer como palavra característica daquela página: rara no livro e concentrada ali. Testei isso com um controle de significado conhecido. Nas *Etimologias* de Isidoro (livros XII, XVI e XVII), tratei cada parágrafo como página e a primeira palavra, em geral o nome da coisa descrita, como rótulo.

| | Rótulo ecoado: fração das ocorrências que caem na página | Fichas quaisquer da página | Frequência global do rótulo ecoado | Fichas da página |
|---|---|---|---|---|
| Isidoro (rótulo = nome) | 0,667 | 0,191 | 2 | 6 |
| Voynich | 0,031 | 0,076 | 92 | 22 |
| G-casas2 (sem conteúdo) | 0,016 | 0,068 | 124 | 20 |

No texto com significado, os rótulos que reaparecem são palavras raras e presas à sua página. No Voynich é o contrário: os rótulos que reaparecem são palavras comuns, menos concentradas na página do que uma ficha qualquer dela. Pareando por frequência global, também não ficam acima das outras palavras da página em nenhuma seção. O Voynich cai do lado do gerador sem conteúdo. Ou os rótulos não são nomes das coisas desenhadas, ou não são escritos da mesma forma no texto.

**10.3 Mas as páginas têm vocabulário próprio, e isso nenhum gerador sem conteúdo reproduziu.** Medi quanto as palavras frequentes se concentram em certas páginas, comparando com o espalhamento ao acaso na seção (índice de agrupamento):

| Texto | Índice de agrupamento por página |
|---|---|
| Voynich | +0,109 |
| Latim de Isidoro (com significado) | +0,113 |
| G-casas2 (sem conteúdo, estacionário) | +0,025 |
| G-deriva (parâmetros que mudam com as páginas vizinhas) | +0,025 |
| Gerador local ajustado ao próprio latim | +0,002 |
| G-cópia (autocitação dentro da página) | +0,169 |

O Voynich se agrupa por página tanto quanto um texto com significado. Um gerador local, mesmo ajustado ao latim, apaga esse agrupamento. O tipo de agrupamento, porém, é peculiar. Há poucas "palavras-chave de página" (palavras com metade ou mais das ocorrências numa só página): 20 nas quatro seções grandes, contra 7,8 esperadas ao acaso. Isso dá cerca de 2% das palavras candidatas, contra 6% a 11% no Isidoro com páginas de tamanho parecido. Fundir as grafias variantes não muda o quadro. Além disso, páginas vizinhas na ordem dos fólios são mais parecidas que páginas distantes (cosseno 0,647 contra 0,607 na biológica, 0,339 contra 0,278 no herbal A). É um agrupamento difuso, que se estende por trechos de páginas vizinhas, e não um vocabulário preso a cada página.

Tentei imitar isso sem conteúdo, com duas famílias de geradores e grades de parâmetros fixadas antes de olhar o resultado:
- **Autocitação através das páginas**, com mutações que respeitam a gramática de casas (18 combinações).
- **Repertório do escriba com pesos que decaem** (9 combinações).

Nenhuma das 27 combinações chegou ao ponto do Voynich. As que alcançam agrupamento de 0,1 produzem de 114 a 336 palavras-chave de página (contra 20), e várias também derrubam a riqueza de vocabulário (razão tipo/ocorrência de 0,10 a 0,19, contra 0,205). As que acertam o número de palavras-chave ficam com agrupamento de 0,02 a 0,05.

**10.4 Veredito revisto.** Cada explicação ganhou um argumento.

A favor do texto sem conteúdo: um gerador de seis regras imita quase toda a superfície do texto, e os rótulos se comportam como os do gerador, não como nomes num texto real.

A favor de haver conteúdo (ou algum processo que ainda não modelei): o vocabulário se agrupa por trechos de páginas no mesmo grau de um texto com significado, de um jeito difuso que nenhum dos meus geradores sem conteúdo conseguiu reproduzir sem quebrar outra medida. Uma notação com significado e grafia variável faria isso. Um escriba cujo vocabulário de enchimento muda devagar, de um jeito que eu não modelei, também poderia fazer.

Fico em aproximadamente 50% para cada lado. A interpretação do livro como compêndio médico (herbário, banhos, astrologia médica, receitas) continua apoiada nas figuras, e mantenho a confiança em cerca de 35%. A confiança de que o texto diz o que as figuras sugerem cai para cerca de 20%.

**Próximo experimento.** O teste mais direto de significado que ainda não fiz é o acoplamento entre texto e imagem. Se o texto fala das figuras, páginas herbais com plantas parecidas (pela cor das flores, pela forma da raiz ou da folha, medidas nas imagens do PDF) deveriam ter vocabulário mais parecido, descontado o efeito de serem vizinhas. Um teste de Mantel entre semelhança de imagem e semelhança de texto, com a proximidade dos fólios como covariável, separaria as duas explicações melhor do que qualquer estatística só de texto. A primeira etapa é conferir a correspondência entre fólios e páginas do PDF, porque o manuscrito tem folhas faltando e dobráveis.

## Resumo atualizado (Fase 10)

**Hipótese:** a família silábica de tabela fixa continua descartada. Entre notação com significado e texto sem conteúdo, o placar está empatado: os rótulos favorecem o texto sem conteúdo, e o agrupamento difuso por páginas favorece a existência de conteúdo.

**Melhor frase traduzida:** continua sendo f2r.2 → *et eis cis*, sem valor de prova.

**Teste:** um gerador sem conteúdo de seis regras reproduz quase toda a superfície do texto, mas não o agrupamento difuso por páginas (+0,025 contra +0,109; o latim com significado dá +0,113). Nenhuma das 27 variantes de autocitação ou repertório chegou lá sem quebrar outra medida.

**Confiança:** chave < 1%, tradução < 1%, conteúdo × sem conteúdo ≈ 50/50, livro como compêndio médico pelas figuras ≈ 35%, texto dizendo o que as figuras sugerem ≈ 20%.

**Ponto mais fraco:** os geradores são meus e simples. Um gerador melhor (por exemplo, o algoritmo de autocitação de Timm e Schinner, com os parâmetros deles) pode reproduzir o agrupamento difuso, e o placar mudaria.

## Fase 11 – O texto acompanha as figuras?

Se o texto fala das plantas desenhadas, páginas com plantas parecidas deveriam ter vocabulário parecido. Testei isso nas 112 páginas herbais de f1 a f66. Nesse trecho, a página do PDF é a página ZL + 2; conferi pelos números de fólio a lápis em f10r, f25r, f40r, f50r, f57r, f65r e f66r.

**Como medi a imagem.** Separei a pintura do pergaminho no espaço de cor Lab, tomando como referência a cor do pergaminho de cada página. Conferi as máscaras a olho em f1v, f2r, f3v e f9r. Daí tirei oito medidas: área pintada; proporções de verde, azul, vermelho e ocre; azul no terço superior (flores); cor quente no terço inferior (raízes); cor quente no topo.

**Como medi o texto.** Cosseno entre vetores tf-idf de palavras, com as grafias como estão e com as variantes fundidas.

**Resultado 1: semelhança geral.** A correlação entre semelhança de imagem e de texto (teste de Mantel, 2.000 permutações) ficou em torno de zero em todos os recortes:
- todos os pares: −0,028;
- mesmo dialeto, cadernos diferentes: +0,032 (P = 0,26);
- só A, cadernos diferentes: −0,003;
- mesmo caderno: +0,018.

Fundir as grafias não mudou nada. O desvio do nulo é 0,047, então um acoplamento acima de cerca de 0,1 está excluído.

**Resultado 2: palavra ligada a um traço visual.** Fiz também um teste dirigido, mais forte: alguma palavra aparece justamente nas páginas com flor azul, raiz vermelha ou ocre, topo vermelho ou ocre, ou planta grande? Usei teste exato de Fisher para cada palavra presente em 8 ou mais páginas. A correção para comparações múltiplas embaralha os traços entre páginas do mesmo caderno. Nenhuma associação resistiu:
- a melhor foi a palavra `d` com raiz vermelha (15 de 40 páginas contra 7 de 72; p corrigido 0,037–0,050), um entre oito testes;
- verifiquei que não é efeito do texto contornando o desenho: `d` não fica mais perto das interrupções de figura (12% contra 10%).

**Poder do teste.** Injetando uma palavra artificial, ele a acharia em 86–90% das vezes se ela estivesse em metade das páginas com o traço e em 10% das demais, e em 100% se estivesse em 70%.

**Conclusão da fase.** Não há sinal de que o texto descreva cor de flor ou de raiz, nem de que páginas de plantas parecidas tenham texto parecido. Não tenho um herbário ilustrado com texto conhecido para servir de controle positivo. Por isso, o que o resultado exclui é um texto que nomeie com regularidade as cores e partes desenhadas, não qualquer forma de descrição.

## Fase 12 – Os rótulos farmacêuticos nomeiam as plantas do herbário?

Nos herbários da época, a página costuma abrir com o nome da planta. Se os rótulos da seção farmacêutica (desenhos de raízes, folhas e frascos) forem nomes de plantas, deveriam coincidir com as primeiras palavras das páginas herbais. Deveriam coincidir mais do que os rótulos de outras seções, que têm a mesma morfologia de rótulo mas outro assunto.

Comparei 235 rótulos farmacêuticos e 659 rótulos de zodíaco, astronomia e cosmologia com as 128 palavras de cabeça herbais. Usei três critérios fixados antes:
- **exato:** farmacêutica 0,0%, outros rótulos 0,2%;
- **grafias fundidas:** 0,0% contra 0,5%;
- **"miolo"** (sem o primeiro e o último pedaço, para descontar um ornamento inicial e a terminação): 3,7% contra 5,6% (P = 0,87).

Nenhum rótulo farmacêutico é igual a uma palavra de cabeça herbal, e no critério mais frouxo eles coincidem menos que os outros rótulos. Não há sinal de que os rótulos farmacêuticos nomeiem as plantas do herbário, ao menos na posição em que um herbário poria o nome.

## Fase 13 – De onde vem o agrupamento por páginas?

O agrupamento por páginas era o único indício a favor de conteúdo que tinha sobrado da Fase 10. Duas perguntas sobre ele:

**É vocabulário ou só ortografia?** Se fosse mudança de hábitos de grafia (`k`/`t`, `ch`/`sh`, séries de `e`), fundir as variantes o derrubaria. Não derruba: o índice vai de +0,109 para +0,108 e, numa fusão mais forte (`o` = `a` e finais equivalentes), para +0,103. O agrupamento é de vocabulário.

**É de página ou de trecho longo?** Juntei páginas vizinhas em blocos e recalculei:

| Blocos de | Voynich | Latim de Isidoro |
|---|---|---|
| 1 página | +0,109 | +0,113 |
| 2 páginas | +0,107 | +0,114 |
| 4 páginas | +0,091 | +0,096 |
| 8 páginas | +0,088 | +0,060 |

No latim, o agrupamento cai quando os blocos passam a misturar assuntos. No Voynich, ele resiste em trechos de oito páginas. Junto com a escassez de palavras presas a uma página (Fase 10), o quadro é de um vocabulário que muda devagar ao longo do códice, não de um vocabulário próprio de cada planta ou de cada receita.

## Fase 14 – Síntese

Desde a Fase 8, cada teste novo foi desenhado para separar "notação com significado" de "texto sem conteúdo linguístico". O placar ficou assim.

**Contra uma língua escrita por tabela fixa:**
- seis línguas (latim, italiano, alemão, catalão, francês antigo, occitano), com tabela única ou uma por dialeto: a ordem das palavras nunca importou mais do que +1,7 ponto;
- nos controles positivos, uma cifra desse tipo dá de +33 a +54 pontos.

**A favor de texto sem conteúdo** (ou de um conteúdo que não está nas palavras):
- um gerador de seis regras mecânicas imita quase toda a superfície do texto (Fase 10);
- os rótulos se comportam como os do gerador, não como nomes num texto real (Fase 10);
- o texto não acompanha as figuras, com um teste que tinha poder para isso (Fase 11);
- os rótulos farmacêuticos não coincidem com as palavras de cabeça do herbário (Fase 12);
- o vocabulário deriva devagar ao longo do códice, em vez de mudar a cada planta (Fase 13).

**A favor de algum conteúdo, ou de um processo que não consegui imitar:**
- o agrupamento lexical por trechos, no grau de um texto real, que meus geradores sem conteúdo não reproduziram sem quebrar outra medida (Fases 10 e 13).

**Minha posição final.** O peso das evidências está agora do lado de um texto sem conteúdo linguístico recuperável na palavra, em cerca de 65 contra 35. A forma mais econômica é um texto escrito por regras de aparência silábica, com convenções de linha e de parágrafo, e com um repertório de palavras que evolui ao longo da cópia. O mais provável é que tenha sido produzido para acompanhar um livro ilustrado de herbário, banhos e astrologia médica, com aparência de saber cifrado. O que impede de fechar a questão é o agrupamento lexical por trechos: um gerador melhor do que os meus precisa reproduzi-lo sem importar palavras do próprio texto.

**O que isso significa para a interpretação.** As figuras continuam dizendo o que o livro aparenta ser. A confiança nessa leitura das imagens fica em cerca de 35%. Mas a confiança de que o texto contenha essa informação em forma linguística cai para cerca de 15%.

## Resumo final (Fases 1 a 14)

**Hipótese:** comecei com um silabário homofônico sobre o latim. Foi refutado, junto com variantes em seis línguas e por dialeto. A hipótese mais econômica agora é um texto sem conteúdo linguístico, gerado por regras de aparência silábica, com um repertório de palavras que deriva ao longo da cópia.

**Melhor frase traduzida:** f2r.2 → *et eis cis* ("e, a eles, aquém"), sem valor de prova.

**Teste:** nenhuma chave passou no teste da ordem (≤ +1,7 ponto contra +33 a +54 nos controles positivos). O texto não acompanha as figuras, os rótulos não se comportam como nomes, e um gerador de seis regras imita quase toda a superfície.

**Confiança:** chave < 1%, tradução < 1%, texto sem conteúdo linguístico recuperável ≈ 65%, livro de herbário/banhos/astrologia médica pelas figuras ≈ 35%, texto contendo essa informação ≈ 15%.

**Ponto mais fraco:** o agrupamento lexical por trechos de páginas ainda não foi reproduzido por nenhum gerador sem conteúdo. Se um gerador honesto (sem copiar palavras do próprio texto) não conseguir reproduzi-lo, a balança volta a pender para o conteúdo.

## Fase 15 – Um gerador honesto reproduz o agrupamento por trechos?

O último argumento a favor de conteúdo era o agrupamento lexical por trechos de páginas. Nenhum gerador sem conteúdo o tinha reproduzido sem quebrar outra medida. Construí então um gerador "honesto", que não copia palavra nenhuma do texto real.

Cada seção e dialeto tem um repertório de 3.000 a 6.000 tipos de palavra, gerados pela própria cadeia do G-casas2. O peso de cada tipo faz um passeio aleatório lento de uma página para a seguinte. Cada palavra do texto vem desse repertório (com probabilidade p, respeitando a regra de emenda) ou é nova, tirada da cadeia. Testei 30 combinações de três parâmetros:
- p, a fração de palavras vindas do repertório;
- o alcance da correlação, em páginas;
- σ, a força da deriva.

| | Agrupamento por página | Palavras-chave de página (acaso) | Vizinhas − distantes (cosseno) | Razão tipo/ocorrência | h2 | Agrupamento em blocos de 8 |
|---|---|---|---|---|---|---|
| Voynich | +0,109 | 20 (5,8) | 0,059 | 0,205 | 2,14 | +0,088 |
| Deriva lexical, p = 0,6, alcance 3 páginas, σ = 1,4 | +0,101 | 38 (6,1) | 0,080 | 0,193 | 2,16 | +0,107 |
| Deriva lexical, p = 0,4, alcance 3, σ = 1,7 | +0,085 | 41 (5,2) | 0,073 | 0,204 | 2,17 | +0,091 |
| Melhor autocitação com agrupamento ≥ 0,1 (Fase 10) | +0,133 | 115 (6,7) | 0,037 | 0,191 | 2,20 | – |

A deriva lexical lenta, sem conteúdo e sem cópia, chega perto do ponto do Voynich em todas as medidas ao mesmo tempo, coisa que a autocitação e o repertório com reforço não conseguiam. Não é um ajuste perfeito: ainda sobram palavras-chave (38 contra 20) e as vizinhas se parecem um pouco demais. Mas mostra que o agrupamento por trechos não exige conteúdo. Ele é o que se espera de um escriba cujas preferências de palavra mudam devagar ao longo da cópia. Um texto com significado e assunto que muda devagar também produziria esse agrupamento; o ponto é que ele deixou de ser evidência a favor do conteúdo.

## Fase 16 – E se for uma cifra com escolhas ao acaso?

O usuário trouxe a pesquisa de 2026 e a cifra "Naibbe" de Greshko. Ela gera texto com cara de Voynich a partir de latim ou italiano, partindo as palavras em pedaços e sorteando tabelas com dados ou cartas. Isso levanta uma objeção séria aos meus testes de significado: numa cifra assim, o mesmo nome sairia com grafias diferentes a cada vez, e os testes das Fases 10 a 13 dariam negativo mesmo com conteúdo.

Fiz uma calibração com uma versão minha, simplificada, não a dele. Cifrei o Isidoro de dois jeitos e rodei os mesmos testes:

| | Rótulo ecoado: concentração (fichas) | Agrupamento por página | Palavras-chave de página (acaso) | Razão tipo/ocorrência |
|---|---|---|---|---|
| Latim sem cifra | 0,667 (0,200) | +0,112 | 50 (4,1) | 0,326 |
| Homofônica por letra, palavra inteira, 3 tabelas sorteadas | 1,000 (0,830), quase sem ecos | +0,004 | 1 (1,8) | 0,760 |
| Estilo Naibbe: pedaços de 1–2 letras, 3 tabelas sorteadas | 0,001 (0,003) | +0,019 | 5 (2,3) | 0,006 |
| Voynich | 0,031 (0,076) | +0,109 | 20 (5,8) | 0,205 |

A objeção procede para os testes de rótulo e de palavras-chave: as duas cifras apagam esses sinais, como acontece no Voynich. Mas elas também apagam o agrupamento por página e desfiguram o vocabulário. Uma multiplica as formas (razão tipo/ocorrência 0,76); a outra as reduz a quase nada (0,006).

O Voynich tem vocabulário de tamanho natural e agrupamento de texto real. Suas palavras se comportam como unidades lexicais estáveis, que voltam com a mesma grafia e se concentram em trechos. Não se comportam como pedaços cifrados com sorteio. Uma cifra do tipo Naibbe, para explicar o manuscrito, precisaria reproduzir também essas duas propriedades, e a minha versão simplificada não reproduz. A de Greshko pode ser mais bem calibrada; esse é o teste a fazer com ela.

## Fase 17 – Onde eu concordo e onde discordo do que foi feito em 2026

Sobre o resumo trazido pelo usuário, com o que os meus dados permitem dizer:

- **"Obedece à Lei de Zipf e se agrupa por seções como um livro real".** Concordo com o fato e discordo da conclusão. Meus números confirmam um vocabulário de língua natural (razão tipo/ocorrência 0,205 contra 0,226 no latim; 70% de formas únicas contra 67%) e um agrupamento por página igual ao do latim (+0,109 contra +0,113). Mas um gerador sem conteúdo de seis regras reproduz a distribuição de frequências e as diferenças entre seções (Fase 10), e a deriva lexical lenta reproduz o agrupamento por trechos (Fase 15). Zipf e agrupamento não provam significado. Além disso, o jeito como o Voynich se agrupa (trechos longos, poucas palavras próprias de cada página) é diferente do de um texto real (Fase 13).
- **"Paradoxo da baixa entropia: 97% das palavras seguem uma fôrma".** O número depende da gramática usada; a minha, de seis casas, cobre 75,8% das ocorrências. E não vejo paradoxo. A baixa entropia e a fôrma rígida são exatamente o que se obtém quando o espaço corta pedaços de aparência silábica de um fluxo contínuo: o espaço voynichiano tem a previsibilidade de um corte silábico, F1 de 0,90 (Fase 8). Um gerador com essas regras dá h2 de 2,15 contra 2,14 do manuscrito.
- **"Cinco calígrafos".** É compatível com o que medi. As mãos coincidem com os dialetos A e B, e cada mão muda a proporção de `k`/`t` conforme a seção (Fase 8). Até onde sei, a identificação dos cinco escribas vem da paleografia de Lisa Fagin Davis (2020). Não verifiquei a atribuição à visão computacional.
- **"A IA esbarra na falta de uma Pedra de Roseta".** Aqui discordo com mais força. Para saber se há uma língua codificada, não é preciso Pedra de Roseta; é preciso controle positivo. Os meus mostram que o método enxergaria uma cifra silábica de tabela fixa em seis línguas (+33 a +54 pontos no teste da ordem). Mostram também que enxergaria uma palavra de cor usada com regularidade nas páginas com aquela cor (86–90% de detecção). Quando o sinal não aparece num teste com poder, a ausência é informação. O problema não é falta de dado de treino: no nível da palavra, o texto não se comporta como língua codificada.

## Veredito (Fases 1 a 17)

**Resultados que ficam, com confiança alta:**
- nenhuma substituição silábica de tabela fixa, em seis línguas, com tabela única ou por dialeto, lê o texto;
- o espaço é um corte de aparência silábica num fluxo contínuo, com uma regra de emenda entre as palavras;
- `-m` é uma abreviatura de margem, no lugar de `-iin`, `-l` e `-r`;
- as palavras são unidades estáveis, com vocabulário de tamanho natural, que derivam devagar ao longo do códice.

**Minha melhor explicação, com confiança de cerca de 70%:** o texto foi produzido por regras, e não por uma língua. Pedaços de aparência silábica, convenções de linha e de parágrafo, e um repertório de palavras que muda ao longo da cópia, distribuído entre escribas com hábitos próprios. É um livro ilustrado de herbário, banhos e astrologia médica, com aparência de saber cifrado.

**O que segue em aberto, com cerca de 30%:** uma notação com significado cuja correspondência não é uma tabela fixa e que, ainda assim, mantém palavras estáveis. Nem a minha versão de cifra com sorteio nem uma tabela fixa explicam isso. A versão bem calibrada da cifra Naibbe é o melhor candidato a testar.

## Resumo (Fases 1 a 17)

**Hipótese:** o silabário homofônico sobre o latim foi refutado, junto com as variantes em seis línguas e por dialeto. A explicação mais econômica é um texto gerado por regras de aparência silábica, com repertório que deriva, sem conteúdo linguístico recuperável.

**Melhor frase traduzida:** f2r.2 → *et eis cis*, sem valor de prova.

**Teste:** nenhuma chave passou no teste da ordem (≤ +1,7 ponto contra +33 a +54 nos controles). Não há acoplamento texto–imagem, e o teste tinha poder para isso. Os rótulos não se comportam como nomes. Um gerador de seis regras com deriva lexical reproduz a superfície e o agrupamento por trechos.

**Confiança:** chave < 1%, tradução < 1%, texto gerado por regras ≈ 70%, livro de herbário/banhos/astrologia pelas figuras ≈ 35%, texto contendo essa informação ≈ 10–15%.

**Ponto mais fraco:** a cifra Naibbe bem calibrada não foi testada. Se ela produzir palavras estáveis, vocabulário natural e agrupamento por trechos a partir de latim ou italiano reais, a balança volta para o conteúdo, e o caminho passa a ser decifrá-la por sorteio de tabelas, não por tabela fixa.

## Fase 18 – A cifra Naibbe original, sobre latim real

**O que foi testado.** Esta fase usou a cifra de Greshko exatamente como publicada, e não a minha versão simplificada da Fase 16. Clonei o repositório do autor e usei `naibbe_v2.py` para cifrar e `decrypt_naibbe.py` para decifrar, com as tabelas de `references/naibbe_tables.csv` e os parâmetros do autor, sem recalibrar nada:
- texto claro re-espaçado em pedaços de 1 ou 2 letras;
- 6 tabelas sorteadas por um baralho de 78 cartas;
- verificação de ambiguidade;
- 3% dos espaços removidos.

Cifrei cinco textos latinos de gêneros diferentes, com as sementes 1 a 3 (cerca de 9 mil palavras de cada):
- Isidoro, *Etimologias* XVII (plantas e agricultura);
- Plínio, *História Natural* XVI (árvores; o próprio exemplo do repositório);
- Apício (receitas);
- Higino, *Astronomia* (astronomia e astrologia);
- César, *Guerra das Gálias* I–II (prosa comum).

Cifrei também dois textos italianos, só como informação: Dante e Europarl. A decifração recuperou 100% das fichas em todos os textos, o que confirma que a cifra foi rodada corretamente.

**Como foi organizado.** O trabalho foi dividido entre três agentes em paralelo e um quarto depois:
- o **Cifrador** cifrou e mediu os textos;
- o **Comparador** mediu o manuscrito, inteiro, por dialeto, por seção e por mão, e montou a régua de variação interna de B;
- o **Controle** mediu o modelo de regras e o manuscrito embaralhado;
- o **Cético** entrou depois, recebendo só as tabelas e a conclusão provisória.

Todos usaram um único módulo de métricas (`fase18/metricas_comuns.py`), com as mesmas definições das fases anteriores. Antes de rodar, registrei por escrito os critérios de decisão e o efeito de cada resultado nas estimativas (`fase18/criterios.md`). A régua é o dialeto B, porque a Naibbe foi calibrada sobre ele; um desempenho pior que o do dialeto A não conta contra.

**Duas definições.** "Estabilidade" é a fração das ocorrências de cada palavra latina frequente (10 ou mais ocorrências, cifrada isoladamente) que sai com a sua grafia mais comum. "Recuperação R" é quanto do agrupamento por página um corpus mostra acima dos seus próprios embaralhamentos, medido como fração do que o dialeto B mostra acima dos dele (B = 1).

### Resultado

| | VB | VA | Naibbe original, latim (5 textos) | Naibbe com deriva por página (variante) | Latim sem cifra = código palavra a palavra | Regras-deriva B | Regras sem deriva B | VB embaralhado |
|---|---|---|---|---|---|---|---|---|
| Razão tipo/ocorrência | 0,210 | 0,292 | 0,197 (0,188–0,217) | 0,196 | 0,361 | 0,191 | 0,220 | 0,210 |
| Formas únicas (hapax) | 68,4% | 69,7% | 49,0% (47,7–50,6%) | 49,3% | 66,1% | 60,7% | 70,2% | 68,4% |
| Mesmo tamanho (10.974 fichas): razão tipo/ocorrência | 0,260 [0,229–0,285] | – | 0,318 | – | – | 0,240 | – | – |
| Mesmo tamanho: hapax | 68,8% [67,9–70,2%] | – | 61,7% | – | – | 63,4% | – | – |
| MI na junção ÷ MI dentro da palavra | 2,47 | 1,34 | 0,03 | 0,04 | 0,12 | 2,47 | 2,23 | 0,02 |
| Repetição imediata | 0,91% | 0,98% | 0,14% | 0,21% | 0,01% | 0,81% | 1,14% | 0,49% |
| Agrupamento por página (200 fichas) | +0,097 | +0,085 | −0,002 | +0,040 | +0,101 | +0,060 | +0,002 | −0,002 |
| Vizinhas − distantes | +0,108 | +0,072 | +0,003 | +0,067 | +0,060 | +0,118 | +0,001 | −0,006 |
| Recuperação R (passam no critério) | 1,00 | 0,86 | −0,01 (0 de 5) | 0,41 (5 de 5) | 1,05 (5 de 5) | 0,63 (3 de 3) | 0,03 (0 de 1) | 0,01 (0 de 1) |
| Decifração | – | – | 100% | 100% | – | – | – | – |

Notas sobre a tabela:
- Os valores são medianas das sementes de cada texto.
- Os colchetes da linha "mesmo tamanho" dão a faixa das 49 janelas contínuas de VB.
- A variante não é a cifra original: tem as mesmas tabelas e glifos, mas os pesos das tabelas são sorteados por página (Dirichlet, α = 10).
- A tabela completa, com a régua, as seções e o italiano, está em `fase18/coordenador_tabela_final.md`.

A Naibbe original produz uma superfície local parecida, mas não igual: h2 de 2,12 contra 2,02, e palavras de 5,0 contra 4,6 unidades. Falha nas três propriedades pedidas:
- **Palavras estáveis.** Uma palavra latina frequente sai com a grafia mais comum em só 6 a 8% das vezes, espalhada por 15 a 19 grafias diferentes.
- **Vocabulário natural.** No mesmo tamanho, o vocabulário tem tipos demais (razão tipo/ocorrência 0,318, contra no máximo 0,285 em qualquer janela de VB) e poucas formas únicas (62% contra 68–70%).
- **Agrupamento por trechos.** É zero: o mesmo valor do manuscrito embaralhado.

A causa é uma só: cada ficha é um pedaço de 1 ou 2 letras com tabela sorteada sem memória.

### Decisão registrada e o parecer do Cético

Pela regra registrada antes, o resultado foi **CONTRA**: os 5 textos latinos falham no agrupamento. O efeito previsto era "texto gerado por regras" de 70% para 75–80%. O Cético refez todas as contas e não achou erro de cálculo. Achou problemas no desenho do teste e os sustentou com números. Os critérios da rodada corretiva foram registrados antes de rodar os testes (`fase18/criterios_v2.md`). O que fiz com cada objeção:

1. **A régua não tinha poder** (DERRUBA a justificativa). Aceito. A régua reprovava o latim sem cifra e, portanto, qualquer código palavra a palavra; reprovava também o próprio dialeto B no TTR e o modelo de regras. Confirmei que um código palavra a palavra recebe CONTRA em 5 de 5. Troquei o critério pela recuperação R contra os embaralhamentos de cada corpus. O critério novo aprova B, aprova o código em 5 de 5 e reprova o embaralhado. A Naibbe original continua falhando em 5 de 5 (4 de 4 sem Apício, o texto do teste de fumaça). O efeito previsto nas estimativas não foi aplicado.
2. **O agrupamento separa "com deriva" de "sem deriva", não "regras" de "cifra"** (DERRUBA o efeito em "regras"). Aceito e confirmado. O modelo de regras sem deriva falha igual à Naibbe (R 0,03). Uma Naibbe com deriva nos pesos das tabelas passa:
   - com α = 10, R = 0,41;
   - com α de 3 a 5, R vai de 0,73 a 1,28;
   - a decifração continua em 100%.

   Nem ela nem o meu modelo acertam o perfil completo, porque as duas exageram a semelhança entre páginas vizinhas. O agrupamento por trechos não discrimina entre cifra e regras: os dois só precisam de deriva.
3. **O TTR mede o tamanho da amostra** (ENFRAQUECE). Aceito. Refiz a comparação no mesmo tamanho. A régua que propus primeiro, feita de páginas sorteadas, ainda reprovava o próprio B contínuo; o Cético apontou isso na segunda rodada, e passei a usar as 49 janelas contínuas de B. A Naibbe continua fora nas duas medidas, com folga de pelo menos 0,018 no TTR. O mesmo teste mostra que **o meu modelo de regras também falha no hapax** (63% contra 68–70%). Isso fica registrado como problema aberto dele.
4. **Uma métrica cega e uma sanidade não cumprida** (COSMÉTICA). Aceito.
   - O índice de blocos de 8 páginas não separa o manuscrito do embaralhado e saiu da decisão.
   - A vizinhança passou a ser só informativa.
   - Cerca de um quarto do agrupamento em 200 fichas é repetição próxima dentro da página: embaralhar dentro da página mantém o índice nas páginas naturais (0,101), mas baixa o de 200 fichas de 0,097 para 0,072. A propriedade passou a se chamar "agrupamento em trechos de até ~200 fichas".
5. **Uma causa só explica tudo, e a superfície local é a prova mais limpa** (ENFRAQUECE). Aceito em parte. No agrupamento, a Naibbe é indistinguível do próprio embaralhamento (|z| < 2 em 5 de 5). Na junção e na repetição, não: z de +4 a +6 e de −5 a −7. Esses desvios, porém, são ínfimos (cerca de 1% da distância até B) ou vão no sentido contrário ao do manuscrito: a Naibbe se repete *menos* que o acaso, e o manuscrito, mais. O que separa a Naibbe do manuscrito sem depender de régua é a junção entre palavras: 0,02 a 0,15 em todas as variantes, contra 2,47. Nenhuma forma de deriva corrige isso.
6. **O modelo de regras era avaliado dentro da amostra** (ENFRAQUECE). Testei e a objeção não se confirmou: treinado com metade de B e medido na outra metade, a distância do modelo sobe só 1,38 vez (0,24 para 0,33), abaixo do limite de 2 registrado. Fora da amostra, a junção do modelo fica entre 2,13 e 2,71. A distância da Naibbe no mesmo tamanho é de 1,14 a 1,23. Ressalvas:
   - são só 4 rodadas;
   - o leiaute das linhas vem das páginas de destino;
   - a Naibbe não teve orçamento de reajuste das tabelas.
7. **Os textos não têm estrutura de entradas** (ENFRAQUECE "conteúdo"). Inconclusivo. Paginei Isidoro e Apício por entrada, mas o índice de blocos depende do número de blocos por seção (3 a 4 em B, 10 a 14 no latim). Igualando isso, desiguala-se o número de fichas por seção. Com textos de 9 mil palavras não há comparação justa. O efeito registrado para esse caso era zero.
8. **Regra assimétrica e exposição prévia a Apício** (COSMÉTICA). Aceito. Sem Apício, o resultado é o mesmo. Fica para a próxima fase registrar uma regra simétrica e a previsão de base antes de rodar.

Na segunda rodada, o Cético deu as objeções 1, 2, 4, 6 e 8 por resolvidas, a 3 e a 5 em parte, e a 7 como inconclusiva com efeito zero. Apontou quatro erros nos testes corretivos, todos corrigidos acima:
- a régua de TTR feita de páginas sorteadas;
- a falta de teto no critério de agrupamento;
- 99,97%, e não 100%, de decifração com α = 1;
- um mínimo de hapax mal transcrito.

Apontou também que o meu critério de permutabilidade mede significância e não tamanho do efeito. Por isso o número da linha nova abaixo é ≤ 1%, e não os 2–5% que a regra registrada daria. A divergência fica declarada. Os pareceres completos estão em `fase18/cetico_parecer.md` e `fase18/cetico_parecer2.md`; o que foi feito com cada ponto, em `fase18/coordenador_respostas_cetico.md`.

### Estimativas de confiança

| | Antes | Agora | Mudança | Por quê |
|---|---|---|---|---|
| Chave correta | < 1% | < 1% | 0 | Nenhuma chave para o manuscrito foi testada. A Naibbe tem chave conhecida, mas não gera texto como o do manuscrito. |
| Tradução válida | < 1% | < 1% | 0 | Mesmo motivo. |
| Texto gerado por regras | ≈ 70% | ≈ 70% | 0 | A regra registrada pedia 75–80%, mas não tinha poder. O agrupamento por trechos também é alcançado por uma cifra com deriva e não favorece as regras. A validação cruzada não achou inflação, e o meu modelo também falha no hapax casado. Nada novo a favor, nada novo contra. |
| Livro de herbário, banhos e astrologia pelas figuras | ≈ 35% | ≈ 35% | 0 | Nenhum teste tocou as figuras. |
| O texto contém a informação das figuras | 10–15% | 9–14% | −1 | Caiu uma das propostas de cifra mais elaboradas. Um código palavra a palavra e uma cifra encadeada não foram testados, e o código passa no critério de agrupamento. |
| *Nova:* a Naibbe original gerou o manuscrito | – | ≤ 1% | – | Falha no agrupamento (R ≈ 0), na junção (0,03 contra 2,47), na repetição e no vocabulário no mesmo tamanho. As variantes com deriva consertam o agrupamento, mas não a junção nem o hapax. |

### Hipótese registrada, não testada (sugestão do usuário)

As figuras podem ter sido feitas para despistar: alguém por volta de 1400 escondendo informação da Igreja e usando as imagens para enganar os leitores. Fica registrada, sem adesão. Um fato dos nossos dados é compatível com ela: em B, os rótulos reaparecem no texto da própria página em 19% dos casos, e em 20% com o texto embaralhado entre as páginas, ou seja, ao acaso. O mesmo fato é compatível com texto gerado por regras, e por enquanto não separa as duas. Ela só teria força se o texto mostrasse conteúdo de língua desacoplado das figuras, coisa que nenhum teste com poder mostrou até aqui.

## Veredito final (Fases 1 a 18)

**Resultados que ficam, com confiança alta:**
- nenhuma substituição silábica de tabela fixa, em seis línguas, lê o texto;
- o espaço é um corte de aparência silábica com regra de emenda: no dialeto B, a dependência na junção entre palavras é 2,5 vezes a de dentro da palavra;
- `-m` é abreviatura de margem;
- as palavras são unidades estáveis, com vocabulário de tamanho natural;
- a cifra Naibbe original, com as tabelas do autor, não gera texto como o do manuscrito: zera o agrupamento, apaga a dependência na junção e espalha cada palavra por 15 a 19 grafias.

**Minha melhor explicação, com cerca de 70%:** texto gerado por regras, com repertório que deriva ao longo da cópia. O ponto fraco dele é real: o vocabulário tem menos formas únicas que o do manuscrito no mesmo tamanho.

**O que segue em aberto:** uma notação com significado que mantenha palavras estáveis *e* a dependência na junção. A Naibbe não serve. Um código palavra a palavra ou uma cifra encadeada, em que a tabela de cada palavra depende do fim da anterior, ainda não foram testados com uma régua capaz de aprová-los.

## Resumo final

**Hipótese:** o silabário homofônico de tabela fixa foi refutado. A cifra Naibbe original, testada sobre latim real com as tabelas do autor, também não explica o manuscrito. A explicação mais econômica continua sendo um texto gerado por regras com repertório que deriva.

**Melhor frase traduzida:** f2r.2 → *et eis cis*, sem valor de prova.

**Teste:** nenhuma chave passou no teste da ordem. A Naibbe cifra e decifra latim perfeitamente, mas fica a −0,01 do agrupamento do manuscrito (escala em que B = 1) e a 0,03 contra 2,47 na junção entre palavras. Uma variante com deriva recupera o agrupamento, mas não a junção.

**Confiança:** chave < 1%; tradução < 1%; texto gerado por regras ≈ 70%; livro de herbário/banhos/astrologia pelas figuras ≈ 35%; texto contendo essa informação ≈ 9–14%; a Naibbe original como mecanismo ≤ 1%.

**Ponto mais fraco:** o agrupamento por trechos não decide nada; só exige deriva. A decisão passa a depender da junção entre palavras e da forma do vocabulário, e nesta última o meu próprio modelo também falha.
