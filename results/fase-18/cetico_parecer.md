# Parecer do Cético: Fase 18 (Naibbe original sobre textos latinos)

Escopo: li só os 9 arquivos de `cetico_entrada/`. Refiz as contas em Python:
- as medianas entre sementes;
- a conferência célula a célula entre tabelas e JSON;
- a reconstrução das réguas a partir das seções e dos extremos das subamostras;
- as bandeiras da verificação de sanidade.

Depois apliquei a regra registrada, sem mudança, a tudo o que os JSON contêm: os textos claros, cada semente da Naibbe, cada seção e mão do manuscrito, cada semente do modelo de regras e cada embaralhamento.

## 0. Conferência de contas: nada errado

- Todas as células de `tabela_cifrador`, `tabela_comparador` e `tabela_controle` batem com os JSON no arredondamento exibido. Não achei nenhuma divergência.
- As medianas entre sementes estão corretas: Naibbe s1–s3, regras s13–s15, embaralhados s7–s8.
- As réguas de A e de B se reconstroem exatamente como [mín, máx] de {seções com 3.000+ fichas} ∪ {mín e máx das subamostras}. As fontes declaradas ("mín vem de / máx vem de") também estão corretas.
- As bandeiras "~0? / ~original? / cai nas duas?" da sanidade se reproduzem.
- A tabela da conclusão (valores e "fora da régua") bate, inclusive a parte das referências.

**Não há erro de transcrição nem de aritmética.** Os problemas estão no desenho do teste e na inferência.

---

## Objeções

### Objeção 1. A regra registrada reprova o próprio latim sem cifra, e reprovaria qualquer código palavra a palavra. Ela não tem poder para discriminar.

**Tipo:** métrica que não discrimina / comparação injusta.

**Evidência:**
- **P2 dos textos claros (tabela_cifrador, seção ii).** Apliquei a regra registrada, sem mudança. Os 5 latinos falham em P2:

  | Texto claro | Métrica fora da régua |
  |---|---|
  | plinio16 | agrup_200 = +0,040 (abaixo de 0,0759); viz_200 = +0,022 (abaixo de 0,0325) |
  | apicius | agrup_200 = +0,189 (acima de 0,1066); bloco8_200 = +0,106 |
  | isidoro17 | bloco8_200 = +0,087 |
  | hyginus | bloco8_200 = +0,116 |
  | cesar | bloco8_200 = +0,059 |

  A régua de bloco8_200 é [−0,0093; +0,0512]. Dante e europarl também falham. **Nenhum dos 7 textos claros passa as três métricas de P2 ao mesmo tempo.** Os dois únicos que passam em bloco8_200 (plinio 0,020 e dante 0,007) são exatamente os que falham em agrup_200 e em viz_200.
- **P1 dos textos claros.** Os 5 latinos também falham. O hapax de isidoro (74,3%) e o de plinio (72,9%) ficam acima de 71,69%. Os de apicius (60,2%), hyginus (65,1%) e cesar (66,1%) ficam abaixo de 66,86%. Pela regra, o latim sem cifra recebe **"CONTRA"**.
- **Invariância.** TTR, hapax, zipf, agrup, bloco8, viz e chave_frac não mudam sob qualquer substituição bijetiva de palavras: dependem só de quais fichas são do mesmo tipo e de onde estão. Logo, a coluna "claro" é **exatamente** o que um código ou nomenclátor palavra a palavra produziria com esses textos. A regra registrada teria dado CONTRA para essa cifra também.
- **Largura da janela.** A janela de agrup_200 tem 0,031 de largura. Os latinos claros vão de 0,040 a 0,189, uma amplitude cerca de 5 vezes maior.

**Consequência:** para estes textos, P(CONTRA | cifra) ≈ P(CONTRA | não cifra) ≈ 1. A razão de verossimilhança da saída da regra é ≈ 1, e "decisão pela regra registrada" não é evidência. A conclusão sobre a Naibbe pode estar certa, mas não por causa da regra.

**Gravidade:** **DERRUBA** a justificativa formal ("pela regra registrada") e, com ela, o efeito automático nas estimativas. Não derruba o fato substantivo sobre a Naibbe (ver Veredito).

**Teste:**
- **(a) Prova de que a regra não tem poder.** Rodar a regra registrada, sem alteração, sobre um código bijetivo de cada texto latino: cada tipo latino vira o tipo do VMS‑B de mesmo posto de frequência. Previsão: P1 e P2 idênticos à coluna "claro", 0 de 5 passam, CONTRA. Se isso se confirmar, a regra precisa ser substituída.
- **(b) Critério substituto, contra o nulo próprio de cada texto.** Fazer 20 embaralhamentos globais da própria saída. Considerar "P2 presente" se agrup_200 ficar acima do percentil 95 desse nulo **e** recuperar pelo menos 25% da distância entre o VB embaralhado e o VB (−0,0022 → +0,0966).
  - Previsão: a Naibbe recupera de −0,4% a +4,8% e falha. O código palavra a palavra recupera de 42% a 194% e passa.
  - Se der isso, a frase "a Naibbe não reproduz P2" fica justificada. Se os dois falharem, a métrica não serve.

### Objeção 2. O modelo de regras é reprovado pela mesma régua, e o modelo de regras sem deriva tem P2 idêntico ao da Naibbe. P2 separa "com deriva" de "sem deriva", não "regras" de "cifra".

**Tipo:** comparação injusta / explicação alternativa.

**Evidência:**
- **Regras‑deriva B reprova na régua de B** (tabela_controle i e ii):
  - em P1: TTR 0,191 < 0,2264 e hapax 61% < 66,86%;
  - em P2: agrup_200 +0,060 < 0,0759 e viz_200 +0,118 > 0,1160.
- **A reprovação vale semente a semente** (JSON): agrup_200 = 0,0596 / 0,0571 / 0,0641 e hapax = 0,607 / 0,610 / 0,601. São 3 reprovações em 3 sementes. A própria conclusão registra isso na linha "regras-deriva mediana B: falha | falha".
- **Regras‑casas2 B (s13) tem P2 no patamar da Naibbe:** agrup_200 = +0,002, viz_200 = +0,001, bloco8_200 = +0,002. Para comparar: Naibbe agrup_200 de −0,003 a +0,003 e viz_200 de +0,001 a +0,005; VB embaralhado agrup_200 −0,002.
- **Fração recuperada da distância entre o VB embaralhado e o VB, em agrup_200:**

  | Gerador | Fração recuperada |
  |---|---|
  | regras‑deriva | 63% |
  | regras‑casas2 | 4% |
  | Naibbe | −0,4% a 4,8% |

O que produz P2 é a **deriva lexical**. Esse mecanismo foi dado ao modelo de regras e não à cifra. Sem deriva, o modelo de regras falha em P2 exatamente como a Naibbe.

**Consequência:** subir "texto gerado por regras" de 70% para 75–80% é incoerente. O teste usado para isso também reprova o próprio modelo de regras, e nele as regras sem deriva empatam com a Naibbe. O máximo que os números sustentam é "deriva > sem deriva".

**Gravidade:** **DERRUBA** o efeito declarado em "texto gerado por regras".

**Teste:** aplicar a regra registrada, idêntica, a regras‑deriva e a regras‑casas2, com 5 ou mais sementes cada, e reportar o resultado ao lado da Naibbe.
- Se regras‑deriva falhar em 3 ou mais de 5 sementes (hoje falha em 3 de 3), a estimativa de "regras" não pode subir com base nesta fase.
- Para que possa subir, falta uma comparação quantitativa pré‑registrada, por exemplo a distância normalizada pela largura da régua, somada em P1+P2+P3. Nela, regras‑deriva teria de vencer também a Naibbe **com deriva** (Objeção 5).

### Objeção 3. Em P1, o TTR aqui mede o tamanho da amostra: o próprio dialeto B é reprovado pela sua régua.

**Tipo:** comparação injusta (tamanho de amostra).

**Evidência:**
- **Tamanhos diferentes.** A régua de B foi montada com peças de 3.473 fichas (BxH), 6.251 (BxB), 10.851 (BxS) e 8.911 a 11.666 (subamostras; JSON `subamostras.B.n`). As saídas da Naibbe têm de 22.959 a 61.484 fichas (tabela_cifrador i, "fichas de texto").
- **O próprio B reprova.** O dialeto B inteiro (23.128 fichas) tem TTR 0,210 < 0,2264 e falha em P1 na própria régua (tabela de referências da conclusão; tabela_comparador i). O manuscrito inteiro (0,205) também falha.
- **No mesmo tamanho, a Naibbe tem TTR igual ou maior que B:**

  | Texto | Fichas | TTR |
  |---|---|---|
  | apicius‑Naibbe | 24.186 | 0,217 |
  | dante‑Naibbe | 22.959 | 0,224 |
  | Voynich B | 23.128 | 0,210 |

- **Extrapolação.** Ajustei log TTR × log N nas 18 saídas da Naibbe (6 textos, sem europarl, 3 sementes): inclinação −0,39, r = −0,98. O TTR previsto a 11.564 fichas é ≈ 0,29, dentro da régua. O ajuste é grosseiro, porque mistura texto com tamanho; serve só para a ordem de grandeza.
- **O mesmo vício em outros limites.** BxH (3.473 fichas, cerca de 17 páginas de 200) define **9 dos 22 limites** da régua de B: os máximos de TTR, hapax, zipf e h2, e os mínimos de agrup_200, compr, razao, F1esp e rep. Dois efeitos disso:
  - a Naibbe só "passa" em zipf (−0,88 a −0,90) porque o máximo −0,8432 vem de BxH. Sem BxH a faixa seria [−1,086; −1,001], e ela falharia;
  - o h2 da Naibbe (2,113 a 2,131) "falha" por 0,01 a 0,03 bit contra um máximo, 2,1030, que também vem de BxH.

**Consequência:** o "TTR fora" em 5 de 5 textos não informa nada. P1 se sustenta só pelo hapax (47,7% a 50,6% contra a faixa de 66,86% a 71,69%). Esse desvio é real no mesmo tamanho: apicius‑Naibbe 50,6% e dante‑Naibbe 49,0%, contra 68,4% em B. Mas regras‑deriva também falha no hapax (60,7%).

**Gravidade:** **ENFRAQUECE**. P1 passa a depender de uma única métrica, e o TTR deve sair da decisão.

**Teste:**
- Cortar cada saída da Naibbe em janelas contíguas com o mesmo número de fichas de cada componente da régua (3.473, 6.251, 10.851 e o tamanho de cada subamostra) e comparar cada janela com o componente do mesmo tamanho.
- Truncar cada saída em 23.128 fichas e comparar com B inteiro.

Previsão: o TTR entra na faixa em 3 ou mais textos. O hapax fica fora da faixa: pela extrapolação, cerca de 0,56 com 11,5 mil fichas e cerca de 0,65 com 3,5 mil. Se o hapax de 3 ou mais textos entrar em [0,6686; 0,7169] com tamanhos casados, a afirmação "a Naibbe falha em P1" cai.

### Objeção 4. Duas das três métricas de P2 têm problema de sanidade, uma delas não discrimina nada, e o protocolo registrado não foi seguido.

**Tipo:** métrica que não discrimina.

**Evidência:**
- **bloco8_200 não separa o manuscrito do embaralhado.**
  - A régua de B é [−0,0093; +0,0512]. O B embaralhado entre páginas dá +0,003 (tabela_controle i, "VB global") e fica **dentro** da régua.
  - As próprias seções de B dão ≈ 0 ou negativo: BxH −0,007, BxB −0,002 (tabela_comparador ii). A Naibbe (−0,005 a +0,009) também cai dentro.
  - A métrica passou na sanidade só porque o teste foi "cair a 10% ou menos do original" (0,003 / 0,034 = 0,08), e não "o embaralhado fica fora da régua".
- **viz_200 falhou na sanidade registrada, sem retirada nem registro.**
  - O critério registrado diz que o agrupamento "deve cair a ~0"; a implementação usa |mediana| ≤ 10% do original.
  - Em VA ele falhou: 0,0082 / 0,0718 = 0,114, marcado "não" (tabela_controle iii, linha "VA global viz_200").
  - Os critérios mandam: "Se não separarem, a métrica não serve e é retirada antes da decisão, com registro." Não houve retirada nem registro, e a conclusão usa viz_200 como métrica "fora da régua" em todas as linhas.
- **agrup_200 mistura página com ordem local.**
  - Embaralhar as palavras **dentro** de cada página preserva exatamente o vocabulário de cada página, e mesmo assim já tira B da régua: VB página = +0,072 (s7 0,073; s8 0,070) < 0,0759. A razão mediana/original é 0,74, marcada "~original? não".
  - Ou seja, cerca de 25% do sinal de agrup_200 vem da ordem das palavras dentro da página (repetição em linhas próximas), e não do "agrupamento por trechos de páginas".
  - A conclusão lista "VB página mediana: P2 falha" sem comentar que isso contradiz o nome da propriedade.

**Consequência:** a decisão sobre a Naibbe não muda, porque agrup_200 sozinho a reprova em 5 de 5. Mas a fase declarou um protocolo de sanidade e não o cumpriu, e uma das métricas que decidem é cega.

**Gravidade:** **COSMÉTICA** para o veredito; **ENFRAQUECE** a credibilidade do protocolo.

**Teste:**
- Registrar a sanidade completa, com duas exigências: (i) o embaralhado global fica a no máximo 10% do original em V, VA e VB; (ii) o valor do embaralhado global fica **fora** da régua.
- Retirar bloco8_200, que falha em (ii). Decidir explicitamente sobre viz_200, que falha em (i) no VA, e registrar a decisão. Refazer a decisão só com agrup_200. Previsão: CONTRA mantido, 5 de 5.
- À parte: embaralhar dentro de blocos de 200 fichas, e não dentro de páginas, para medir quanto de agrup_200 é sub‑página. Se a queda for de novo de cerca de 25%, renomear P2 como "agrupamento por página + repetição local".

### Objeção 5. Uma única causa, que vem do desenho da cifra, explica P1, P2 e P3 de uma vez. A fase conta três falhas onde há uma, e trata como "só contexto" a evidência mais limpa.

**Tipo:** explicação alternativa.

**Evidência:**
- **Uma palavra, muitas grafias** (tabela_cifrador iii). Cada palavra latina frequente aparece com **15 a 19 grafias** diferentes (estab_grafias), e estab_frac vai de 0,063 a 0,094. Atenção: essas métricas não estão definidas em `definicoes_metricas.md`. Pelo nome, estab_frac seria a fração de ocorrências com a grafia mais comum. O padrão é o que se espera da escolha aleatória e independente de homófono ou tabela a cada ocorrência.
- **A mesma independência produz tudo de uma vez:**
  - hapax baixo, porque o vocabulário é feito de fragmentos recombinados;
  - P2 ≈ 0: agrup_200 de −0,003 a +0,003 e viz_200 de +0,001 a +0,005, iguais aos do VB embaralhado (−0,002 e −0,006);
  - P3 entre palavras no nível do texto embaralhado:

    | Métrica | Naibbe | VB embaralhado | VB |
    |---|---|---|---|
    | razão | 0,028 a 0,044 | 0,02 | 2,47 |
    | F1esp | 0,92 a 0,93 | 0,917 | 0,906 |
    | rep | 0,11% a 0,22% | 0,49% | 0,91% |

    Na razão, a Naibbe recupera só de 0,5% a 1,2% da distância entre o embaralhado e o VB. No rep, fica abaixo até do VB embaralhado.
- **Leitura:** em tudo o que acontece entre palavras, a Naibbe se comporta como o manuscrito com as palavras permutadas. P1 (hapax), P2 e P3 (razão) não são três evidências independentes.
- **Era previsível sem rodar nada.** Uma cifra que trabalha abaixo do nível da palavra e escolhe homófonos sem memória não consegue criar agrupamento por página nem dependência na junção entre palavras.

**Consequência:**
- A conclusão está certa, mas por motivo incompleto. O achado robusto é "a Naibbe gera fichas permutáveis". Ele aparece em razão e rep sem depender da largura de régua nenhuma, e a fase o rebaixou a "contexto".
- Como era previsível pelo desenho, o resultado traz pouca informação nova sobre a hipótese de cifra em geral. Só confirma que esta família de cifra não serve.

**Gravidade:** **ENFRAQUECE** o alcance da conclusão, não o fato.

**Teste:**
- **(i) Nulo próprio.** Embaralhar globalmente as fichas de cada saída da Naibbe (mesmas sementes, 20 repetições) e recalcular agrup_200, viz_200, razão, rep e F1esp. Se os valores originais ficarem a menos de 2 desvios‑padrão desse nulo em todas as métricas, a Naibbe é permutável, e a fase deve reportar **uma** falha estrutural, não três.
- **(ii) Naibbe com deriva.** A decifração continua 100% em ambas as variantes:
  - escolher a tabela por uma cadeia de Markov que repete a tabela ou o homófono da última ocorrência do mesmo fragmento com probabilidade ρ ∈ {0; 0,5; 0,8; 0,9; 0,95};
  - ou sortear, por página, as probabilidades de tabela de uma Dirichlet(α·p_autor), com α ∈ {1; 10; 100}.

  Se algum valor de ρ ou α puser agrup_200 em [0,076; 0,107] e viz_200 dentro da faixa, P2 não separa cifra de regras (as duas só precisam de deriva), e o efeito nas estimativas deve ser zero. Se nenhum conseguir isso sem piorar ainda mais o hapax ou a razão, a falha é estrutural da família Naibbe, e só dela.

### Objeção 6. A comparação é assimétrica: o modelo de regras é avaliado em parte dentro da amostra; a Naibbe, fora dela.

**Tipo:** comparação injusta.

**Evidência:**
- **Mesmo esqueleto do manuscrito.** O modelo de regras tem 227, 114 e 83 páginas, idênticas a V, VA e VB (campo `paginas` de cada entrada em `dados_controle.json`).
- **Dependência da transcrição.** O campo `contorno` do mesmo JSON registra que o gerador `deriva_lexical` importa `copia3_grade.py`, que "lê 'ZL.txt'" (a transcrição do manuscrito) no momento da importação.
- **Acertos de superfície quase exatos:**

  | Métrica | Regras‑deriva B | VB |
  |---|---|---|
  | razão | 2,473 (mediana; sementes 2,39 / 2,52 / 2,47) | 2,473 |
  | h2 | 2,04 | 2,02 |
  | compr | 4,56 | 4,61 |
  | F1esp | 0,90 | 0,91 |

- **A Naibbe está em condição oposta.** Foi rodada "sem recalibrar", com tabelas que o autor ajustou para outras propriedades, sobre textos com estrutura de parágrafos de texto corrido (de 5 a 464 parágrafos por texto).

**Consequência:** "regras perto, Naibbe longe" mistura ajuste dentro da amostra com previsão fora da amostra. Isso não muda a falha da Naibbe, mas impede usar a proximidade do modelo de regras como prova a favor das regras.

**Gravidade:** **ENFRAQUECE** o lado comparativo da conclusão e o efeito em "regras".

**Teste:** validação cruzada para os dois modelos.
- Derivar e calibrar o modelo de regras com só metade das páginas de B (ou só com A) e medi‑lo na outra metade.
- Dar à Naibbe o mesmo orçamento de ajuste: re‑estimar tabelas e probabilidades na mesma metade, incluindo a deriva.
- Comparar as distâncias fora da amostra. Se a vantagem do modelo de regras em P1 e P3 cair pela metade ou mais, a comparação atual está inflada.

### Objeção 7. Os textos testados não têm a estrutura de conteúdo do manuscrito, e o padrão de P2 do manuscrito é compatível com "uma entrada por página".

**Tipo:** comparação injusta (estrutura) / explicação alternativa.

**Evidência:**
- **No manuscrito, o agrupamento é local à página:** agrup_200 alto (B 0,097) e bloco8_200 baixo (B 0,034; BxH −0,007; BxB −0,002). A razão bloco8_200 / agrup_200 é 0,35 em B e 0,31 em A.
- **Nos latinos claros, o agrupamento é de longo alcance.** A mesma razão vai de 0,51 a 1,11: plinio 0,51, apicius 0,56, cesar 0,59, isidoro 1,02, hyginus 1,11. Europarl dá 1,20.
- **Dante é a exceção** (0,12): texto natural organizado em unidades curtas também pode ter perfil local.
- **Por que isso importa.** O perfil "forte por página, fraco em blocos de 8 páginas" é o que se espera de um herbário com uma planta por página, isto é, de texto **com** conteúdo atrelado às figuras. Os textos escolhidos são prosa contínua, repaginada em blocos de 200 fichas sem relação com unidades temáticas.

**Consequência:** a fase não testou o cenário de conteúdo que pesa na estimativa "o texto contém a informação das figuras". Para a Naibbe isso é irrelevante, porque ela zera tudo. Mas o efeito proposto nessa estimativa não pode se apoiar nesta fase.

**Gravidade:** **ENFRAQUECE** o efeito sobre "conteúdo".

**Teste:** paginar textos organizados por entradas (herbários latinos medievais como Pseudo‑Apuleio, Macer Floridus ou Circa instans, ou o próprio Isidoro XVII com uma planta por página) e medir P2 em claro e cifrado com a Naibbe.
- Previsão: em claro, perfil de agrup alto e bloco8 baixo, como no manuscrito; cifrado, P2 ≈ 0.
- Se o texto claro reproduzir o perfil, fica mostrado que P2 é compatível com conteúdo e que só a Naibbe o destrói. A conclusão sobre a Naibbe se mantém, e a inferência para "conteúdo" e para "regras" cai.

### Objeção 8. A regra é assimétrica e foi escrita depois de uma exposição prévia ao caso.

**Tipo:** comparação injusta (procedimento).

**Evidência:**
- **Assimetria.** CONTRA exige falhar em **uma** propriedade (P2) em 3 textos. A FAVOR exige passar em **duas** (P1 e P2) em 3 textos.
- **Exposição prévia.** O teste de fumaça com Apício, semente 1, aconteceu antes do registro. Nessa semente, agrup_200 = +0,0010 e viz_200 = +0,0049 (JSON). Se alguma saída foi olhada, o P2 nulo estava visível.

**Consequência:** somada à Objeção 1, a regra fazia de CONTRA o resultado esperado sob qualquer hipótese. Isso não muda o fato sobre a Naibbe (sem Apício, 4 de 4 falham em P2), mas reduz o peso que a decisão pode ter.

**Gravidade:** **COSMÉTICA**.

**Teste:**
- Refazer a decisão excluindo Apício. Previsão: 4 de 4 falham em P2, CONTRA mantido.
- Nas próximas fases, registrar antes de rodar uma regra simétrica e uma "previsão de base": o que a regra diria do texto claro e de um código bijetivo.

---

## Observações menores (não pesam no veredito)

- **Rótulos artificiais.** Nos 7 textos, n_palavras_claro − fichas de texto = n_paragrafos, exatamente. Exemplos: isidoro 9.036 − 8.721 = 315; europarl 16.536 − 16.531 = 5. Ou seja, uma palavra por parágrafo virou "rótulo".
  - Por isso, eco e concentração dos textos latinos são artefatos: isidoro claro tem concentração 1,000, e europarl claro tem eco de 100% com só 5 rótulos.
  - Não entram na decisão, mas não devem ser citados.
- **Subamostras com P2 menor que B inteiro.** As subamostras de metade das páginas dão P2 sistematicamente menor que B inteiro:

  | Métrica | Mediana das subamostras | B inteiro |
  |---|---|---|
  | agrup_200 | 0,0865 | 0,097 |
  | viz_200 | 0,083 | 0,108 |
  | bloco8_200 | 0,020 | 0,034 |

  Ou isso é efeito de tamanho, ou as subamostras quebram a vizinhança entre páginas. Nos dois casos, os limites inferiores de P2 ficam mais baixos, o que favorece o texto testado. Convém verificar se `mc.subamostras` sorteia páginas contíguas.
- **Métricas sem definição.** estab_frac, estab_grafias e estab_n aparecem na tabela_cifrador (iii), mas não estão definidas em `definicoes_metricas.md`.

---

## Veredito do Cético

**A conclusão sobrevive com ressalvas, e em parte está certa pelos motivos errados.**

### O que sobrevive
- **Entre palavras, a Naibbe é indistinguível do manuscrito embaralhado.** Com as tabelas e os parâmetros do autor, ela recupera, da distância entre o B embaralhado e o B:
  - de −0,4% a +4,8% em agrup_200;
  - de 6% a 9% em viz_200;
  - de 0,5% a 1,2% na razão.
- **O hapax é cerca de 18 pontos menor que o de B no mesmo tamanho:** apicius‑Naibbe 50,6% e dante‑Naibbe 49,0%, contra 68,4%.
- **O resultado se repete** nas 3 sementes e nos 7 textos.
- **É robusto ao viés de tamanho de P2, que até favorece a Naibbe.** Os números sugerem que agrup_200 cresce com o número de páginas: B inteiro 0,097 contra 0,0865 nas meias‑amostras; A inteiro 0,085 contra 0,065. As saídas da Naibbe têm de 115 a 307 páginas de 200 fichas, contra 17 a 58 nos componentes da régua.

**A Naibbe original não é um mecanismo suficiente para o manuscrito. Isso pode ser afirmado.**

### O que não sobrevive: a justificativa
- A regra registrada reprova o latim sem cifra (5 de 5 em P1 e em P2) e, por invariância, qualquer código palavra a palavra.
- O dialeto B inteiro reprova na própria régua (TTR).
- O embaralhamento dentro da página reprova em P2.
- O modelo de regras reprova em P1 e em P2, em todas as sementes.

Uma régua que reprova tudo, inclusive a própria referência, não é evidência. A conclusão é verdadeira porque a Naibbe zera as propriedades entre palavras. Isso se vê sem régua nenhuma e era previsível pelo desenho da cifra; não depende de a regra ter dado CONTRA.

### Efeito nas estimativas: **exagerado**

| Estimativa | Proposto pelo coordenador | Proporcional aos dados |
|---|---|---|
| Texto gerado por regras | 70% → 75–80% | +0 a +2 pontos |
| O texto contém a informação das figuras | 10–15% → ≈ 10% | 0 a −2 pontos |
| Chave, tradução, leitura pelas figuras | sem mudança | sem mudança (adequado) |

- **"Texto gerado por regras":** a subida é injustificada. O modelo de regras falha na mesma régua, e o modelo de regras sem deriva (casas2) empata com a Naibbe em P2. O que P2 separa é haver ou não deriva, um mecanismo que também pode ser dado a uma cifra. Mais do que 2 pontos só depois de rodar a Naibbe com deriva (Objeção 5) e a validação cruzada (Objeção 6).
- **"Conteúdo":** o efeito é levemente exagerado. A fase testou uma família de cifra (abaixo do nível da palavra, homófonos sem memória), não o conteúdo em geral, e não testou texto paginado por entradas (Objeção 7).
- **A estimativa que os dados realmente movem não está na tabela:** "a Naibbe, ou uma cifra abaixo do nível da palavra com escolha de homófono sem memória, gerou o manuscrito". Essa fica praticamente excluída.

### O que o coordenador NÃO pode afirmar com base nisto
1. **Que "a hipótese de cifra" perdeu força em geral.** Perdeu só a família Naibbe. Um código palavra a palavra preservaria P1 e P2 do texto claro, e não foi testado contra uma régua capaz de aprová‑lo.
2. **Que o resultado favorece "texto gerado por regras".** O modelo de regras também reprova (hapax 0,60–0,61; agrup_200 0,057–0,064 nas 3 sementes), e parte da sua proximidade em P3 vem de ajuste dentro da amostra.
3. **Que "a regra registrada decidiu CONTRA" tem peso de evidência.** Ela daria CONTRA para o latim sem cifra.
4. **Que a Naibbe falha em P1 "por TTR e hapax".** O TTR reprova o próprio B; resta só o hapax.
5. **Que P2 mede agrupamento "por trechos de páginas" puro.** Cerca de 25% é ordem local dentro da página, e bloco8_200 não separa o manuscrito do embaralhado.
6. **Que texto natural não tem o padrão de P2 do manuscrito.** Não foi testado texto com uma entrada por página.
7. **Que P3 é mero contexto.** Razão, rep e F1esp no nível do embaralhado são a prova mais limpa contra a Naibbe. A conclusão deveria se apoiar nelas, reformulada como "a Naibbe gera fichas permutáveis".

### Redação que eu aceitaria
"A Naibbe com os parâmetros do autor, aplicada a 5 textos latinos e 2 italianos, gera texto cujas propriedades entre palavras (agrupamento por página, semelhança entre páginas vizinhas, dependência na junção) são indistinguíveis das do manuscrito embaralhado. Seu vocabulário tem cerca de 50% de hapax, contra cerca de 68% em B no mesmo tamanho. Ela não é um mecanismo suficiente para o manuscrito. A régua registrada não discrimina (reprova o latim sem cifra e o próprio B) e não deve ser usada para mover estimativas; o efeito se limita à família Naibbe."
