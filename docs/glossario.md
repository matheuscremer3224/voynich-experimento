# Glossário

Cada termo técnico usado no projeto, explicado em uma ou duas frases, em ordem alfabética.

[← Voltar ao README](../README.md)

---

**Agente auxiliar (ou subagente).** Um agente lançado por outro agente para cuidar de uma parte do trabalho. Começa sem saber nada da conversa e recebe só o que o coordenador lhe entrega.

**Agente de IA.** Um programa de inteligência artificial que não só responde perguntas, mas executa tarefas em várias etapas: escreve e roda código, lê arquivos, testa e corrige. Aqui, os agentes foram instâncias do Claude, da Anthropic.

**Agrupamento por página (índice de).** Mede se as palavras frequentes se concentram em certas páginas mais do que o acaso faria. Vale cerca de zero num texto embaralhado e é positivo num texto real, porque o assunto muda de uma página para outra.

**Agrupamento por trechos.** O mesmo fenômeno numa escala maior: páginas vizinhas compartilham vocabulário, como capítulos de um livro.

**Autocitação.** Ideia, defendida por outros pesquisadores (Timm e Schinner), de que o escriba do Voynich criava cada palavra copiando com pequenas mudanças uma palavra já escrita perto dali.

**Bancada (bench).** Nome dado a pares de glifos do Voynich que parecem uma letra dupla, como `ch` e `sh`. Neste projeto, contam como uma unidade só.

**Busca local (otimizador).** Um programa que testa muitas tabelas possíveis, mudando um pouco de cada vez e guardando as que melhoram uma nota. Foi usado para escolher a chave sem a mão humana.

**Cadeia de Markov.** Um modo de gerar sequências em que cada símbolo é sorteado conforme o símbolo anterior. Serve para fabricar texto com a "cara" de um texto real, sem significado nenhum.

**Cético.** Na Fase 18, o agente que recebeu só as tabelas e a conclusão provisória, sem o raciocínio, com a tarefa de achar erros e explicações alternativas.

**Chave.** A tabela que diz qual letra ou sílaba cada símbolo representa. Aqui, uma chave só vale se as suas regras forem fixadas antes da leitura.

**Chave nula.** Uma chave treinada pelo mesmo método, mas sobre o texto já embaralhado. Mostra quanto "acerto" o método produz sozinho, sem haver mensagem.

**Cifra.** Um método de esconder uma mensagem trocando letras ou pedaços de texto por outros símbolos, segundo regras.

**Cifra encadeada.** Cifra em que a escolha da grafia de um pedaço depende do pedaço anterior. Não foi testada; é candidata para a Fase 19.

**Cifra homofônica.** Cifra em que uma mesma letra pode ser escrita de vários jeitos, para confundir quem conta letras.

**Cifra Naibbe.** Cifra proposta por Michael Greshko em 2025. Parte o texto em pedaços de uma ou duas letras e escolhe, para cada pedaço, uma de seis tabelas sorteadas com cartas de baralho. O autor mostrou que ela produz texto parecido com o do Voynich.

**Cifra verbosa.** Cifra em que cada letra ou sílaba vira um grupo de vários símbolos, deixando o texto cifrado mais longo que o original.

**Código palavra a palavra (nomenclátor).** Sistema em que cada palavra inteira é trocada por outra, segundo uma lista. Mantém o vocabulário e o agrupamento do texto original.

**Controle (embaralhado).** O mesmo texto com as palavras em ordem aleatória. Se uma chave "lê" o texto embaralhado tão bem quanto o original, ela não está lendo nada.

**Controle positivo.** Um caso em que a resposta certa é conhecida: por exemplo, latim cifrado de propósito com uma chave escolhida por nós. Serve para provar que o método encontraria o sinal, se ele existisse.

**Coordenador.** O agente que divide o trabalho, distribui as tarefas aos auxiliares, junta os resultados e toma as decisões, seguindo critérios escritos antes.

**Cosseno (semelhança de cosseno).** Número entre 0 e 1 que mede quanto duas listas de palavras se parecem. 1 é idêntico, 0 é nada em comum.

**Critério registrado antes (pré-registro).** Escrever, antes de rodar um teste, o que contará como resultado a favor e contra. Impede que qualquer resultado seja lido depois como confirmação.

**Currier A e B (dialetos).** Duas variedades de escrita do Voynich, identificadas por Prescott Currier nos anos 1970. Diferem na frequência de certas combinações de glifos e coincidem com escribas diferentes.

**Decifrar × traduzir.** Decifrar é descobrir o sistema (a chave). Traduzir é passar o resultado para outra língua. Aqui não se chegou nem à primeira etapa.

**Deriva lexical.** Mudança lenta, de página em página, nas palavras preferidas pelo escriba. Um gerador com deriva reproduz o agrupamento por trechos sem precisar de significado.

**Dialeto.** Ver *Currier A e B*.

**Dirichlet (α).** Um jeito de sortear proporções aleatórias. Na Fase 18, os pesos das tabelas da cifra Naibbe foram sorteados assim, página a página; um α menor quer dizer que os pesos mudam mais de uma página para outra.

**Entropia (h1, h2).** Medida de quão imprevisível é a próxima letra. h1 olha a letra sozinha; h2 olha a letra sabendo a anterior. O Voynich tem h2 muito baixa: suas letras são previsíveis demais para uma língua comum.

**Escriba (mão).** Cada pessoa que escreveu o manuscrito. Estudos de paleografia identificam cinco mãos diferentes.

**EVA.** Sigla de European Voynich Alphabet. Um padrão que troca cada símbolo do Voynich por letras comuns (`q`, `o`, `k`, `ch`…), para que o texto possa ser digitado e analisado. As letras EVA não têm valor de som.

**F1 (ao recolocar o espaço).** Nota de 0 a 1 que mede quanto um programa acerta ao recolocar os espaços num texto do qual eles foram tirados. Mostra quão previsível é o lugar do espaço.

**Fólio.** Uma folha do manuscrito. "f2r" quer dizer folha 2, frente (*recto*); "f2v", folha 2, verso.

**Gallows (glifos-forca).** Os glifos altos do Voynich, com "pernas" (`k`, `t`, `p`, `f` em EVA). Os parágrafos costumam começar com um deles.

**Gerador sem conteúdo.** Programa que fabrica texto seguindo regras, sem mensagem nenhuma. Serve de "falsificador": o que ele imita não prova que existe significado.

**Glifo.** Cada símbolo da escrita do Voynich.

**Gramática de casas.** Um molde de seis posições (prefixo, gallows, bancada, série de `e`, vogal, final) em que cabem 75,8% das palavras do Voynich.

**Hapax.** Palavra que aparece uma única vez no texto. A proporção de hapax é uma das marcas do vocabulário de uma língua.

**Informação mútua.** Mede quanto saber um símbolo ajuda a adivinhar outro. Aqui, foi usada para comparar a ligação entre o fim de uma palavra e o começo da seguinte com a ligação entre o começo e o fim da mesma palavra.

**IVTFF.** O formato de arquivo das transcrições do Voynich. Cada linha começa com um "endereço" entre `< >` que diz o fólio, a linha e o tipo de trecho.

**Junção.** A fronteira entre duas palavras vizinhas. No Voynich, a junção carrega mais informação do que o interior da palavra, o que é o contrário de uma língua comum.

**Lei de Zipf.** Regularidade das línguas: a palavra mais comum aparece cerca de duas vezes mais que a segunda, três vezes mais que a terceira, e assim por diante. A "inclinação de Zipf" mede o quanto um texto segue essa regra.

**Léxico.** Lista de palavras que existem de verdade numa língua. Aqui, 48.224 formas latinas tiradas de 1,26 milhão de palavras de textos antigos.

**Ligadura.** Dois ou mais glifos unidos num traço só. Contam como uma unidade.

**Mediana.** O valor do meio quando os resultados são postos em ordem. É menos sensível a um resultado estranho do que a média.

**Modelo de trigramas.** Um modelo que sabe com que frequência cada sequência de três letras aparece numa língua. Serve para dar nota a quanto um texto "parece" latim.

**Nulo próprio.** O resultado de um texto depois de embaralhado várias vezes. Comparar cada texto com o seu próprio nulo evita réguas injustas.

**p-valor.** A chance de o acaso produzir um resultado tão forte quanto o observado. Quanto menor, menos provável que seja acaso.

**Permutação (teste de).** Embaralhar os dados muitas vezes para ver com que frequência o acaso produz um resultado tão forte quanto o observado.

**Poder (de um teste).** A chance de um teste detectar um efeito que existe de verdade. Um resultado negativo só informa algo se o teste tinha poder.

**PYTHONHASHSEED.** Uma configuração do Python. Fixá-la em 0 garante que os sorteios internos saiam sempre iguais, para que os números possam ser reproduzidos.

**Qui-quadrado.** Teste estatístico que verifica se proporções diferem mais do que o acaso explicaria.

**Razão tipo/ocorrência (TTR).** Número de palavras diferentes dividido pelo total de palavras. Mede a riqueza do vocabulário, mas depende do tamanho do texto: textos maiores dão valores menores.

**Recuperação R.** Na Fase 18, quanto do agrupamento por página um texto mostra acima dos seus próprios embaralhamentos, em proporção ao que o manuscrito mostra. O manuscrito vale 1; um texto embaralhado vale cerca de 0.

**Régua (variação interna).** Faixa de valores que o próprio manuscrito mostra quando se mede pedaços diferentes dele. Um texto "parece o manuscrito" se cai dentro dessa faixa.

**Repetição imediata.** Quando a mesma palavra aparece duas vezes seguidas (`chol chol`). No Voynich isso é muito mais comum do que em latim.

**Rótulo.** Palavra curta escrita junto a uma figura, como uma legenda.

**Seções.** As partes do manuscrito, nomeadas pelas figuras: herbal (plantas), biológica (banhos), farmacêutica (frascos e raízes), zodíaco, astronômica, cosmológica e receitas (parágrafos curtos marcados por estrelas).

**Semente (aleatória).** Número que inicia os sorteios de um programa. A mesma semente dá sempre os mesmos sorteios, o que permite repetir um experimento.

**SHA-256.** Uma "impressão digital" de um arquivo. Publicar a impressão digital da chave congelada prova que ela não foi alterada depois.

**Silabário.** Sistema de escrita em que cada símbolo, ou grupo de símbolos, representa uma sílaba.

**Subamostra.** Um pedaço do texto, sorteado, usado para ver quanto uma medida varia dentro do próprio texto.

**Teste da ordem.** O teste central das Fases 5, 8 e 9: comparar quanto uma chave "lê" o texto na ordem real e com as palavras embaralhadas. Uma cifra real dá diferença grande; o ruído dá diferença perto de zero.

**Teste de Mantel.** Teste que mede se duas tabelas de semelhança se correspondem. Aqui: se páginas com desenhos parecidos têm texto parecido.

**Teste exato de Fisher.** Teste para tabelas pequenas de contagem. Aqui: se uma palavra aparece mais nas páginas com certo traço do desenho.

**tf-idf.** Um peso dado a cada palavra de uma página: alto para palavras frequentes ali e raras no resto do livro.

**Transliteração.** A transcrição do manuscrito para letras comuns, símbolo por símbolo, sem tentar dizer o que significam. Aqui foram usadas duas: ZL3b e RF1b.

**Validação cruzada (dentro × fora da amostra).** Ajustar um modelo numa parte dos dados e testá-lo em outra parte que ele nunca viu. Evita que o modelo pareça bom só porque decorou os dados.

**Vírgula (espaço incerto).** Nas transcrições, a vírgula marca um lugar em que não se sabe se há espaço. Todas as contagens foram feitas das duas formas.

**z (escore z).** Quantos "desvios típicos" um resultado está longe da média do acaso. Acima de 2, em módulo, costuma indicar que não é acaso.
