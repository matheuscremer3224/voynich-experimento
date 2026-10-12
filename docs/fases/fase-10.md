# Fase 10 – Significado ou texto sem língua?

[← Fase 9](fase-09.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 11 →](fase-11.md)

> **Em uma frase:** Um 'falsificador' de seis regras imita quase tudo; só o agrupamento por páginas resiste.

**A pergunta.** Um texto sem significado, gerado por regras, consegue imitar o Voynich?

**O que foi feito.** O agente construiu geradores de texto sem conteúdo e aplicou a eles as mesmas medidas do manuscrito. Testou também se os rótulos se comportam como nomes, usando como controle um texto com significado conhecido (Isidoro de Sevilha).

**O que deu.** Um gerador de seis regras mecânicas reproduziu entropia, comprimento das palavras, riqueza do vocabulário, o espaço silábico, o `-m` de margem e a divisão A/B. Os rótulos se comportaram como os do gerador, não como nomes. Mas o agrupamento das palavras por páginas, igual ao de um texto real, nenhum gerador reproduziu: foram 27 variações sem sucesso.

**Por que importa.** O placar ficou empatado. O agrupamento por páginas virou o principal argumento a favor de haver conteúdo.

- **Código:** [`gerador.py`](../../src/gerador.py), [`rotulos_especificidade.py`](../../src/rotulos_especificidade.py), [`controle_rotulos_latim.py`](../../src/controle_rotulos_latim.py), [`agrupamento.py`](../../src/agrupamento.py), [`agrupamento2.py`](../../src/agrupamento2.py), [`agrupamento3.py`](../../src/agrupamento3.py), [`deriva.py`](../../src/deriva.py), [`copia2.py`](../../src/copia2.py), [`copia3_grade.py`](../../src/copia3_grade.py), [`repertorio_grade.py`](../../src/repertorio_grade.py)
- **Saídas:** [`results/fase-10/`](../../results/fase-10/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 10 – Significado ou texto sem língua?

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

### Resumo atualizado (Fase 10)

**Hipótese:** a família silábica de tabela fixa continua descartada. Entre notação com significado e texto sem conteúdo, o placar está empatado: os rótulos favorecem o texto sem conteúdo, e o agrupamento difuso por páginas favorece a existência de conteúdo.

**Melhor frase traduzida:** continua sendo f2r.2 → *et eis cis*, sem valor de prova.

**Teste:** um gerador sem conteúdo de seis regras reproduz quase toda a superfície do texto, mas não o agrupamento difuso por páginas (+0,025 contra +0,109; o latim com significado dá +0,113). Nenhuma das 27 variantes de autocitação ou repertório chegou lá sem quebrar outra medida.

**Confiança:** chave < 1%, tradução < 1%, conteúdo × sem conteúdo ≈ 50/50, livro como compêndio médico pelas figuras ≈ 35%, texto dizendo o que as figuras sugerem ≈ 20%.

**Ponto mais fraco:** os geradores são meus e simples. Um gerador melhor (por exemplo, o algoritmo de autocitação de Timm e Schinner, com os parâmetros deles) pode reproduzir o agrupamento difuso, e o placar mudaria.

---

[← Fase 9](fase-09.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 11 →](fase-11.md)
