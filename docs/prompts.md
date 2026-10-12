# Os prompts que dirigiram o trabalho

[← README](../README.md) · [Diário](../DIARIO.md)

Estes são, na ordem, os prompts técnicos que eu enviei ao agente, copiados do registro da sessão. Ficaram de fora as
mensagens curtas de conversa (como "continue" entre uma fase e outra). Os prompts 1 e 3
foram planejados com o agente orientador (uma conversa separada do Claude; veja "Quem fez o quê" no README). A segunda parte traz os
prompts que o agente coordenador escreveu para os agentes auxiliares na Fase 18.

Para quem quer aprender com eles, o que mais fez diferença:
- **Regras que impedem o agente de se enganar:** citar só texto real, fixar a chave antes de ler, separar resultado de
  palpite e comparar sempre com um controle embaralhado (prompt 1).
- **Deixar o agente seguir sozinho depois que o método está definido:** entre as Fases 8 e 17, bastaram mensagens curtas
  de continuação; o próprio agente escolheu a próxima pergunta a partir do que ficou em aberto.
- **Uma pergunta só por fase, com critério escrito antes de rodar** (prompts 2 e 3).
- **Um revisor isolado do raciocínio**, que recebe só as tabelas (prompt 3).
- **Um plano B explícito**, para o agente não fingir que fez o que não conseguiu (prompts 3 e 4).

---

## Parte 1 – Prompts do usuário

### 1. O desafio (início da sessão, com três anexos: as duas transliterações e o PDF das imagens)

```text
<contexto>
O Manuscrito Voynich (Beinecke MS 408) nunca foi decifrado. Quero que você
faça a sua própria tentativa, do zero, como um desafio sério ao seu raciocínio.
Em anexo estão três materiais:
1. ZL3b-n.txt: transliteração Zandbergen-Landini em EVA. É a fonte principal
   para qualquer sequência de glifos, contagem ou teste.
2. RF1b-er.txt: transliteração de referência em EVA básico. Use-a como
   conferência. Quando as duas divergirem num trecho que importa para o seu
   argumento, aponte fólio e linha e diga qual leitura você adotou.
3. Um PDF com as imagens dos fólios. Use-o apenas para o que é visual:
   desenhos, posição dos rótulos, layout e relação entre texto e figura.
Não transcreva glifos a partir das imagens.
</contexto>

<formato_dos_arquivos>
As transliterações estão no formato IVTFF. Antes de qualquer contagem:
- Cada linha de texto começa com um localizador entre < >, que indica fólio,
  linha e tipo de trecho (P = parágrafo, L = rótulo, C = texto em círculo,
  R = texto radial). Use-o para citar e para separar rótulos de texto corrido.
- Ponto (.) separa palavras. Vírgula (,) marca espaço incerto: rode as
  contagens das duas formas e diga se o resultado muda.
- Códigos como @185; são caracteres raros e chaves { } indicam ligaduras.
  Trate cada um como uma unidade.
- Linhas de comentário e variáveis de página são metadados, não texto.
- As variáveis de página informam seção, dialeto Currier e escriba. Use-as
  para comparar A com B.
Descreva em uma frase como você limpou os arquivos antes de analisar.
</formato_dos_arquivos>

<objetivo>
Construir um sistema de decifração original, aplicá-lo a trechos reais e
entregar uma tradução e uma interpretação próprias do manuscrito, com a sua
melhor aposta sobre o que o livro diz e para que servia.
</objetivo>

<regras>
1. Use o conhecimento existente (datação 1404–1438, dialetos Currier A e B,
   cinco escribas, baixa entropia h2, estrutura prefixo-raiz-sufixo) apenas
   como ponto de partida. Não resuma a história nem repita soluções já
   propostas (Newbold, Bax, Cheshire, Ardıç, Hauer e Kondrak etc.). Se a sua
   hipótese coincidir com alguma, diga onde ela diverge.
2. Não responda que a tarefa é impossível e não se esconda em ressalvas.
   Comprometa-se com uma hipótese e leve-a até o fim.
3. Cite apenas sequências EVA que existam nos arquivos anexados, com fólio e
   linha. Nunca invente texto do manuscrito.
4. As regras do seu sistema devem ser fixas e explícitas. Uma vez definidas,
   não as ajuste palavra a palavra para forçar sentido.
5. Separe sempre o que é resultado do seu método do que é palpite.
</regras>

<metodo>
Fase 1 – Análise própria. Calcule com código frequência e posição dos glifos,
estrutura interna das palavras, palavras mais comuns por seção, diferenças
entre A e B, e o comportamento dos rótulos junto às figuras. Aponte de 3 a 5
padrões que você considera mais reveladores.

Fase 2 – Hipóteses concorrentes. Formule três explicações diferentes para o
sistema (por exemplo: cifra verbosa sobre latim ou italiano, língua natural em
alfabeto inventado, notação abreviada, sistema numérico ou de classificação).
Para cada uma, diga que padrão da Fase 1 ela explica e qual ela não explica.
Escolha uma e justifique.

Fase 3 – A chave. Escreva o sistema completo: tabela de correspondências,
regras de leitura, língua de destino e como tratar A e B.

Fase 4 – Tradução. Aplique a chave, linha a linha, a:
  a) o primeiro parágrafo do f1r;
  b) uma página herbal com rótulo e desenho;
  c) os rótulos de uma página do zodíaco;
  d) um parágrafo da seção de receitas.
Formato: EVA → forma intermediária → português. Marque cada palavra como
"lida", "incerta" ou "não resolvida". Nos itens b e c, confira no PDF se a
leitura combina com a figura e diga quando não combina.

Fase 5 – Teste. Sem alterar a chave, aplique-a a um trecho que você ainda não
usou. Informe a proporção de palavras que geram resultado válido e compare com
um controle (a mesma chave sobre o texto com as palavras embaralhadas). Se a
chave funcionar igualmente bem no controle, diga isso com clareza.

Fase 6 – Interpretação. Com base no que você leu, diga o que é o livro, quem
o fez, para quem, e o que cada seção contém.

Fase 7 – Veredito. Dê um nível de confiança para a chave, para a tradução e
para a interpretação. Liste o que derrubaria a sua hipótese e qual seria o
próximo experimento.
</metodo>

<formato_de_saida>
Texto corrido com um título por fase. Tabelas apenas para a chave e para as
traduções linha a linha. Termine com um resumo de cinco linhas: a hipótese, a
melhor frase traduzida, o resultado do teste, a confiança e o ponto mais fraco.
</formato_de_saida>
```

### 2. Fase 18: a cifra Naibbe original

```text
Fase 18. Você não precisa do PDF: as tabelas da cifra Naibbe estão publicadas pelo autor. Clone o repositório: git clone https://github.com/greshko/naibbe-cipher. Use naibbe_v2.py (cifra) e decrypt_naibbe.py (decifração), com as tabelas exatamente como estão no código, sem recalibrar. Rode o teste que você deixou pendente: cifre latim real com a Naibbe e verifique se o resultado produz palavras estáveis, vocabulário natural e agrupamento por trechos, usando as mesmas métricas das fases anteriores. Compare lado a lado com o manuscrito e com o seu modelo de texto gerado por regras. Depois atualize as quatro estimativas de confiança e diga quanto cada uma mudou e por quê. Se o clone falhar por bloqueio de rede, pare e me avise; eu anexo o ZIP.
```

### 3. Fase 18: com agentes em paralelo

```text
<objetivo>
Executar a Fase 18 usando agentes auxiliares em paralelo, com você como
coordenador. A pergunta da fase é a que você deixou em aberto: a cifra Naibbe,
com as tabelas originais de Greshko, produz a partir de latim real um texto com
palavras estáveis, vocabulário natural e agrupamento por trechos? O resultado
deve mover, para cima ou para baixo, as suas quatro estimativas de confiança.
</objetivo>

<material>
- Seu trabalho até aqui: relatorio_completo.md, código e saídas das 17 fases.
- Transliterações ZL3b-n.txt e RF1b-er.txt, já em uso.
- Cifra Naibbe: git clone https://github.com/greshko/naibbe-cipher
  Use naibbe_v2.py e decrypt_naibbe.py com as tabelas como estão, sem recalibrar.
</material>

<agentes>
Lance quatro agentes. Cada um começa sem contexto, então entregue a cada um os
arquivos de que precisa, a definição exata das métricas das fases anteriores e
o formato de saída esperado.

1. Cifrador. Cifra com a Naibbe pelo menos três textos latinos e um italiano de
   gêneros diferentes (herbário, receituário, astrologia, prosa comum), com
   várias sementes aleatórias. Calcula as mesmas métricas das fases anteriores.
2. Comparador. Calcula as mesmas métricas sobre o manuscrito, separando dialeto
   A, dialeto B e cada seção. Reporta também a variação interna do manuscrito,
   para servir de régua.
3. Controle. Calcula as mesmas métricas sobre o seu modelo de texto gerado por
   regras e sobre texto embaralhado.
4. Cético. Só entra depois que os três primeiros terminarem. Recebe apenas as
   tabelas de resultados e a conclusão provisória, sem o raciocínio que levou
   a ela. Tarefa: encontrar erros de cálculo, métricas que não discriminam
   nada, comparações injustas e explicações alternativas.
</agentes>

<regras_do_coordenador>
- Todos usam exatamente o mesmo código de métricas. Escreva-o uma vez e
  distribua; não deixe cada agente reimplementar.
- Defina antes de rodar o que contaria como resultado a favor da hipótese de
  cifra e o que contaria contra. Registre isso por escrito e não mude depois.
- Não suavize o parecer do cético. Se ele encontrar um erro, corrija e rode de
  novo antes de concluir.
- Lembre que a Naibbe foi calibrada sobre o dialeto B. Um desempenho pior no
  dialeto A é esperado e não conta como evidência contra.
- Se uma fonte estiver bloqueada, procure repositório do autor, preprint e
  material suplementar antes de me pedir um arquivo.
</regras_do_coordenador>

<plano_b>
Se você não tiver como lançar agentes auxiliares nesta conversa, diga isso em
uma linha e execute os quatro papéis em sequência. Nesse caso, faça a etapa do
cético relendo apenas as tabelas finais, e liste pelo menos três objeções
concretas antes de aceitar qualquer conclusão.
</plano_b>

<entrega>
1. Uma tabela comparando manuscrito (A e B), Naibbe sobre latim, modelo de
   regras e texto embaralhado, métrica por métrica.
2. O parecer do cético e o que você fez com cada objeção.
3. As quatro estimativas de confiança atualizadas, com o valor anterior, o
   novo e o motivo da mudança.
4. O relatorio_completo.md com a Fase 18 acrescentada e um novo zip.
Termine com três linhas: o que mudou, o que continua em aberto e qual seria a
Fase 19.
</entrega>
```

### 4. Publicação deste repositório

```text
<objetivo>
Publicar todo o nosso trabalho sobre o Manuscrito Voynich como um repositório
no meu GitHub (conta matheuscremer3224), registrando em detalhe o que foi feito
até agora. O repositório também é uma peça de portfólio: deve mostrar que eu
sei conduzir pesquisa, análise e relatório usando agentes de IA.
</objetivo>

<publico>
Pessoas curiosas, sem formação em linguística, criptografia ou estatística, e
recrutadores avaliando o meu trabalho. Elas precisam entender o que foi feito,
achar interessante e conseguir conferir que foi bem feito.
</publico>

<repositorio>
Nome: voynich-experimento
Visibilidade: privado no início. Eu torno público depois de revisar.
Descrição curta: "Experimento: até onde um agente de IA chega tentando
decifrar o Manuscrito Voynich, com método, testes e resultados honestos."
</repositorio>

<como_publicar>
Use o primeiro caminho que funcionar e diga qual usou:
1. Navegador do aplicativo Claude, onde já estou logado no GitHub. Crie o
   repositório e os arquivos pela interface web.
2. Conector do GitHub ou git com acesso autenticado, se você tiver.
3. Se nenhum funcionar, não finja que publicou: entregue um zip com a
   estrutura completa e um passo a passo de como eu subo pelo site.
Nunca peça nem digite senha ou token. Antes de criar o repositório e antes de
cada publicação, mostre o que vai subir e espere o meu ok.
</como_publicar>

<estrutura>
- README.md: a porta de entrada, para leigos (regras abaixo).
- DIARIO.md: linha do tempo, uma entrada por fase, da 1 até a atual.
- docs/fases/fase-01.md em diante: um arquivo por fase.
- docs/relatorio_completo.md: o relatório técnico integral.
- docs/glossario.md: cada termo técnico explicado em uma ou duas frases.
- docs/prompts.md: os prompts que eu usei para dirigir o trabalho.
- src/: todo o código, com instruções de como rodar.
- results/: tabelas e saídas de cada fase.
- DADOS.md: onde baixar as transliterações, as imagens do manuscrito e a cifra
  Naibbe, com links e citações. Não inclua esses arquivos no repositório.
- LICENSE: MIT para o código.
</estrutura>

<regras_do_readme>
- Tom de conversa, frases curtas, sem jargão. Termo técnico inevitável ganha
  explicação na mesma frase e entrada no glossário.
- Ordem: o que é o Manuscrito Voynich e por que ninguém o leu; o que este
  experimento tentou; o que descobrimos até agora; como o trabalho foi feito;
  o que não funcionou; como reproduzir; fontes.
- Logo no início, em destaque: o texto NÃO foi decifrado. Mostre as
  estimativas de confiança atuais em linguagem comum.
- Explique o método como trabalho de detetive, com uma analogia do dia a dia
  para cada etapa.
- A seção "o que não funcionou" tem o mesmo destaque do que funcionou. É ela
  que dá credibilidade ao estudo.
- Seção "Quem fez o quê": eu defini as perguntas, escrevi os prompts,
  coordenei os agentes e decidi os rumos; a análise e o código foram
  produzidos por agentes Claude sob a minha direção.
```

---

## Parte 2 – Prompts do coordenador para os agentes auxiliares (Fase 18)

O coordenador escreveu um código único de métricas (`src/fase18/metricas_comuns.py`), uma folha de regras comuns
([`results/fase-18/LEIA_AGENTES.md`](../results/fase-18/LEIA_AGENTES.md)) e os critérios de decisão
([`results/fase-18/criterios.md`](../results/fase-18/criterios.md)) antes de lançar os agentes. Os caminhos
`/home/claude/voynich/...` são os do ambiente em que o trabalho rodou; no repositório, correspondem a `src/` e
`results/fase-18/`. Um caminho temporário do ambiente foi abreviado para `[clone local de naibbe-cipher]`; o resto está como foi enviado.

### Cifrador

```text
Você é o CIFRADOR da Fase 18 de uma análise estatística do Manuscrito Voynich. Comece lendo /home/claude/voynich/fase18/LEIA_AGENTES.md (regras comuns) e o docstring de /home/claude/voynich/fase18/metricas_comuns.py (definições das métricas e funções). Não edite esses arquivos, nem o repositório da cifra Naibbe, nem nada fora de /home/claude/voynich/fase18/.

Tarefa: cifrar textos reais com a cifra Naibbe original de Greshko (o módulo já a importa do clone em [clone local de naibbe-cipher], com as tabelas e os parâmetros do autor, sem recalibrar) e medir o resultado com as métricas comuns.

Passos (escreva um script cifrador_rodar.py em /home/claude/voynich/fase18 e rode com `cd /home/claude/voynich/fase18 && PYTHONHASHSEED=0 python3 cifrador_rodar.py`):
1. `import metricas_comuns as mc` (o script está na mesma pasta).
2. Textos: todos de mc.TEXTOS — latinos: isidoro17 (herbário), plinio16 (herbário), apicius (receituário), hyginus (astronomia/astrologia), cesar (prosa comum); italianos: dante (Divina Commedia), europarl_it (prosa moderna). Leia cada um com `pars = mc.ler_texto(nome)` (até 9.000 palavras).
3. Para cada texto:
   a. linha de base sem cifra: `r = mc.medir(mc.paginas_de_texto(pars, "claro", secao=nome), nome + " claro")`;
   b. para as sementes 1, 2 e 3: `mc.semear(s); pg = mc.paginas_de_texto(pars, "naibbe", secao=nome); r = mc.medir(pg, f"{nome} naibbe s{s}")`;
   c. a mediana de cada métrica numérica entre as 3 sementes;
   d. com `mc.semear(1)`: `mc.decifrar_check(pars)` (fração decifrada corretamente pelo decrypt_naibbe.py do autor) e `mc.estabilidade_naibbe(pars)`.
4. Salve /home/claude/voynich/fase18/cifrador_resultados.json com a estrutura {texto: {"genero", "lingua", "claro": {...}, "naibbe": {"1": {...}, "2": {...}, "3": {...}}, "naibbe_mediana": {...}, "decifra": x, "estab": {...}}}. Use os valores de gênero e língua de mc.TEXTOS.
5. Salve /home/claude/voynich/fase18/cifrador_tabela.md com:
   (i) `mc.tabela_md({...})` com as medianas da Naibbe, uma coluna por texto;
   (ii) a mesma tabela para os textos claros;
   (iii) uma tabela pequena com decifra, estab_frac e estab_grafias por texto;
   (iv) para cada texto, o mínimo e o máximo entre as 3 sementes de TTR, zipf, agrup_200, bloco8_200 e viz_200.
6. A mensagem final deve trazer os caminhos dos arquivos, a tabela (i), a tabela (iii) e até 10 linhas de observações factuais: o que é estável entre sementes, e qualquer aviso ou erro. A Naibbe imprime "Total ambiguity retries", o que é normal. Não tire conclusões sobre o Voynich; você ainda não viu os números dele.

Se algo falhar (arquivo ausente, exceção), relate exatamente o erro e o que conseguiu rodar; não invente números.
```

### Comparador

```text
Você é o COMPARADOR da Fase 18 de uma análise estatística do Manuscrito Voynich. Comece lendo /home/claude/voynich/fase18/LEIA_AGENTES.md (regras comuns), o docstring de /home/claude/voynich/fase18/metricas_comuns.py (definições e funções) e /home/claude/voynich/fase18/criterios.md (como a régua será usada). Não edite esses arquivos nem nada fora de /home/claude/voynich/fase18/.

Tarefa: medir o próprio manuscrito (transliteração ZL3b, já carregada pelo módulo) com as métricas comuns, separando dialeto e seção, e construir a régua de variação interna que os critérios exigem.

Passos (escreva comparador_rodar.py em /home/claude/voynich/fase18 e rode com `cd /home/claude/voynich/fase18 && PYTHONHASHSEED=0 python3 comparador_rodar.py`):
1. `import metricas_comuns as mc`.
2. Meça com `mc.medir(pages, nome)`:
   - manuscrito inteiro: `mc.paginas_voynich()`;
   - dialeto A e dialeto B: `mc.paginas_voynich(dialeto="A")`, `(dialeto="B")`;
   - cada seção: `mc.paginas_voynich(secao=X)` para X em H, P, B, S, Z, A, C, T (H = herbal, P = farmacêutica, B = biológica, S = receitas/estrelas, Z = zodíaco, A = astronômica, C = cosmológica, T = só texto);
   - os cruzamentos dialeto × seção: B×H, B×B, B×S, A×H, A×P;
   - as mãos 1, 2 e 3: `mc.paginas_voynich(mao="1")` etc.
   Algumas métricas de página saem como NaN em subconjuntos pequenos; isso é esperado, então registre e siga.
3. Variação interna: `mc.subamostras(mc.paginas_voynich(dialeto="B"), "B", reps=10)` e o mesmo para A. Cada uma devolve {métrica: (mín, mediana, máx)}.
4. Régua de B, exatamente como em criterios.md: para TTR, hapax, zipf, agrup_200, bloco8_200, viz_200, h2, compr, razao, F1esp e rep, o intervalo [mínimo, máximo] da união de (a) os mínimos e máximos das subamostras de B e (b) os valores de B×H, B×B e B×S, desde que essa seção tenha 3.000 ou mais fichas (campo "n"). Faça o mesmo para A, apenas como informação, usando as subamostras de A e A×H, A×P com 3.000+ fichas.
5. Salve /home/claude/voynich/fase18/comparador_resultados.json com {"medidas": {nome: métricas}, "subamostras": {"A": ..., "B": ...}, "regua_B": {métrica: [mín, máx]}, "regua_A": {...}}.
6. Salve /home/claude/voynich/fase18/comparador_tabela.md com:
   (i) `mc.tabela_md` com inteiro, A, B e as seções;
   (ii) os cruzamentos e as mãos;
   (iii) a régua de B e a de A, uma linha por métrica, com mínimo e máximo.
7. A mensagem final deve trazer os caminhos, a tabela (i), a régua de B e até 10 linhas de observações factuais (por exemplo, quais métricas variam muito entre seções). Reporte erros e avisos com exatidão; não invente números.
```

### Controle

```text
Você é o CONTROLE da Fase 18 de uma análise estatística do Manuscrito Voynich. Comece lendo /home/claude/voynich/fase18/LEIA_AGENTES.md (regras comuns) e o docstring de /home/claude/voynich/fase18/metricas_comuns.py (definições e funções). Não edite esses arquivos nem nada fora de /home/claude/voynich/fase18/.

Tarefa: medir dois tipos de controle com as métricas comuns.
- Um modelo de texto gerado por regras, sem conteúdo: palavras geradas por uma cadeia ajustada ao manuscrito, com o mesmo leiaute de páginas, mais uma deriva lenta do vocabulário. Ele é produzido por `mc.gerar_regras`.
- Texto do próprio manuscrito embaralhado, que serve para ver se as métricas discriminam alguma coisa.

Passos (escreva controle_rodar.py em /home/claude/voynich/fase18 e rode com `cd /home/claude/voynich/fase18 && PYTHONHASHSEED=0 python3 controle_rodar.py`):
1. `import metricas_comuns as mc`.
2. Modelo de regras: `G = mc.gerar_regras("deriva", seed=s)` para s em 13, 14 e 15, e `mc.gerar_regras("casas2", seed=13)`. Meça cada um inteiro (`mc.medir(G, nome)`) e também filtrado por dialeto: `mc.filtrar(G, dialeto="B")` e `mc.filtrar(G, dialeto="A")`. Para "deriva", calcule a mediana das 3 sementes em cada recorte (inteiro, A, B).
3. Embaralhado: `V = mc.paginas_voynich()`, `VB = mc.paginas_voynich(dialeto="B")`, `VA = mc.paginas_voynich(dialeto="A")`. Meça `mc.embaralhar(X, "global", seed=s)` e `mc.embaralhar(X, "pagina", seed=s)` para X em V, VB e VA, com s em 7 e 8. "global" embaralha as palavras entre páginas da mesma seção e dialeto; "pagina" embaralha só dentro de cada página. Meça também VB e VA sem embaralhar, como referência.
4. Verificação de sanidade: diga se agrup_200, bloco8_200 e viz_200 caem a cerca de zero no embaralhamento "global" e se ficam perto do original no embaralhamento "pagina". Diga também se razao e rep caem nos dois embaralhamentos.
5. Salve /home/claude/voynich/fase18/controle_resultados.json com todas as medidas e as medianas.
6. Salve /home/claude/voynich/fase18/controle_tabela.md com:
   (i) `mc.tabela_md` com regras-deriva (mediana) inteiro, A e B; regras-casas2 inteiro e B; VB original; VB global; VB página; VA original; VA global;
   (ii) o mínimo e o máximo entre sementes de TTR, zipf, agrup_200, bloco8_200 e viz_200 para regras-deriva B.
7. A mensagem final deve trazer os caminhos, a tabela (i), o resultado da verificação de sanidade e até 10 linhas de observações factuais. Reporte erros com exatidão; não invente números.
```

### Cético, primeira rodada (lançado só depois dos três primeiros)

```text
Você é o CÉTICO de uma análise estatística. Seu trabalho é atacar a conclusão provisória abaixo, sem diplomacia. Escreva tudo em português.

O QUE ESTÁ EM JOGO
Testou-se se a cifra Naibbe (Greshko 2025, Cryptologia: cifra de substituição homofônica que cifra latim/italiano em texto parecido com o Manuscrito Voynich; o autor a calibrou sobre o dialeto B do manuscrito), rodada com as tabelas e parâmetros originais do autor sobre textos latinos reais, reproduz três propriedades do manuscrito: palavras estáveis/vocabulário natural (P1), agrupamento lexical por trechos de páginas (P2) e superfície local (P3, só contexto). Compara-se com o manuscrito (dialetos A e B, seções), com um "modelo de regras" (gerador de texto sem conteúdo, 'deriva lexical') e com o manuscrito embaralhado. Desempenho pior que o dialeto A NÃO conta contra a Naibbe, porque ela foi calibrada sobre B.

MATERIAL (leia TUDO, e SOMENTE isto): a pasta /home/claude/voynich/fase18/cetico_entrada/
 - conclusao_provisoria.md  (a conclusão que você deve atacar)
 - criterios_registrados.md (regra de decisão registrada antes de rodar)
 - definicoes_metricas.md   (o que cada métrica mede)
 - tabela_cifrador.md, tabela_comparador.md, tabela_controle.md (resultados)
 - dados_*.json (os mesmos resultados em bruto, para você conferir contas)
Não abra nenhum outro arquivo do sistema (nem scripts, nem código, nem outras pastas): você deve julgar só pelas tabelas, como um revisor externo. Você pode rodar Python (python3) sobre os arquivos dessa pasta para refazer contas, cruzar números e testar coerência interna. Não edite nada nessa pasta; se precisar escrever, use só o arquivo de saída abaixo.

SUA TAREFA – procurar, com números das tabelas:
 1. Erros de cálculo ou de transcrição (números que não batem entre tabela e JSON, entre tabelas, ou que são internamente impossíveis/estranhos).
 2. Métricas que não discriminam nada (que dão o mesmo valor para coisas que deveriam diferir, ou que separam coisas por um motivo trivial).
 3. Comparações injustas (tamanho de amostra diferente, régua estreita ou larga demais, régua que o próprio manuscrito ou o modelo de regras reprova, diferenças de pré-processamento, estrutura de páginas/parágrafos diferente, etc.).
 4. Explicações alternativas para os resultados (outra coisa que produziria o mesmo padrão sem que a conclusão seja verdadeira).
 5. Se a conclusão sobrevive ou não, e se o efeito previsto nas estimativas é proporcional ao que os dados mostram.

FORMATO DA SAÍDA: escreva /home/claude/voynich/fase18/cetico_parecer.md com:
 - Pelo menos 6 objeções numeradas. Para cada uma: tipo (erro de cálculo / métrica que não discrimina / comparação injusta / explicação alternativa), a evidência numérica citando tabela e célula, gravidade (DERRUBA a conclusão / ENFRAQUECE / COSMÉTICA) e um teste concreto e executável que a resolveria (o que rodar, com que controle, e que resultado manteria ou derrubaria a conclusão).
 - Uma seção final "Veredito do Cético": a conclusão sobrevive, sobrevive com ressalvas, ou cai? O efeito nas estimativas é exagerado, adequado ou tímido? Diga o que, em sua opinião, o coordenador NÃO pode afirmar com base nisto.
Não suavize. Se achar que a conclusão está certa mas por motivos errados, diga. Se achar que uma objeção é fraca, não a inclua só para fazer número; mas procure de verdade.

Na mensagem final, cole o parecer inteiro.
```

### Cético, segunda rodada (depois dos testes corretivos)

```text
Segunda rodada, curta: rodei os testes que você propôs e quero seu parecer sobre as correções, sem suavizar.

Material novo (leia só isto e o que já leu): /home/claude/voynich/fase18/cetico_entrada2/
 - criterios_v2.md: registrado depois do seu parecer e antes de rodar;
 - coordenador_respostas_cetico.md: o que foi feito com cada objeção;
 - coordenador_tabela_final.md;
 - conclusao_revisada.md;
 - coordenador_*.json: dados brutos dos testes T1–T7b e extras.
Pode rodar Python sobre esses arquivos para conferir contas. Não abra scripts nem outras pastas.

Escreva /home/claude/voynich/fase18/cetico_parecer2.md com no máximo uns 40 linhas:
 (a) para cada objeção 1–8, se a resposta a resolve: sim / em parte / não, em uma linha cada;
 (b) qualquer erro novo de cálculo ou de desenho nos testes corretivos, com número e célula;
 (c) se a conclusão revisada e o efeito nas estimativas estão proporcionais: diga o que mudaria, se mudaria.
Cole o parecer inteiro na mensagem final.

Address this before completing your current task.
```

Os pareceres do Cético estão em [`results/fase-18/cetico_parecer.md`](../results/fase-18/cetico_parecer.md) e
[`results/fase-18/cetico_parecer2.md`](../results/fase-18/cetico_parecer2.md). O que foi feito com cada objeção está em
[`results/fase-18/coordenador_respostas_cetico.md`](../results/fase-18/coordenador_respostas_cetico.md).
