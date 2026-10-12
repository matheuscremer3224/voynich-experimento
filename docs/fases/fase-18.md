# Fase 18 – A cifra Naibbe original, com agentes em paralelo

[← Fase 17](fase-17.md) · [Diário](../../DIARIO.md) · [README](../../README.md)

> **Em uma frase:** A cifra testada exatamente como o autor publicou não gera um texto como o do manuscrito, e um agente Cético pegou falhas no desenho do teste.

**A pergunta.** A cifra Naibbe, com o código e as tabelas do autor, transforma latim real num texto com palavras estáveis, vocabulário natural e agrupamento por trechos?

**O que foi feito.** O trabalho foi dividido entre agentes. Um coordenador escreveu um código único de medidas e registrou por escrito, antes de rodar, o que contaria a favor e contra. Três agentes trabalharam ao mesmo tempo: o Cifrador cifrou cinco textos latinos e dois italianos com a Naibbe; o Comparador mediu o manuscrito por dialeto e seção e montou a 'régua'; o Controle mediu o modelo de regras e o texto embaralhado. Depois, um agente Cético recebeu só as tabelas e a conclusão, e tentou derrubá-la. Houve duas rodadas de críticas e correções.

**O que deu.** A cifra funciona (decifra 100%), mas o texto que ela produz não tem palavras estáveis (cada palavra latina sai com 15 a 19 grafias), tem vocabulário fora do padrão e agrupamento zero. O Cético não achou erro de conta, mas mostrou que a régua escrita antes reprovaria até o latim sem cifra: a conclusão automática foi suspensa e refeita com critérios melhores. Ele também mostrou que uma variante da cifra com 'deriva' recupera o agrupamento, então essa medida não separa cifra de regras. O que separa é a ligação entre palavras vizinhas, que nenhuma variante da Naibbe reproduz.

**Por que importa.** As estimativas quase não mudaram: o efeito que o critério antigo previa não foi aplicado, porque o critério não tinha poder. Uma linha nova entrou: 'a Naibbe original gerou o manuscrito', até 1%.

- **Código:** [`fase18/metricas_comuns.py`](../../src/fase18/metricas_comuns.py), [`fase18/cifrador_rodar.py`](../../src/fase18/cifrador_rodar.py), [`fase18/comparador_rodar.py`](../../src/fase18/comparador_rodar.py), [`fase18/controle_rodar.py`](../../src/fase18/controle_rodar.py), [`fase18/coordenador_decisao.py`](../../src/fase18/coordenador_decisao.py), [`fase18/coordenador_testes.py`](../../src/fase18/coordenador_testes.py), [`fase18/coordenador_extras.py`](../../src/fase18/coordenador_extras.py), [`fase18/coordenador_tabela_final.py`](../../src/fase18/coordenador_tabela_final.py)
- **Saídas:** [`results/fase-18/`](../../results/fase-18/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

> Nos caminhos citados abaixo, `fase18/` corresponde a [`src/fase18/`](../../src/fase18/) (código) e a [`results/fase-18/`](../../results/fase-18/) (tabelas, critérios registrados, pareceres do Cético).

### Fase 18 – A cifra Naibbe original, sobre latim real

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

#### Resultado

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

#### Decisão registrada e o parecer do Cético

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

#### Estimativas de confiança

| | Antes | Agora | Mudança | Por quê |
|---|---|---|---|---|
| Chave correta | < 1% | < 1% | 0 | Nenhuma chave para o manuscrito foi testada. A Naibbe tem chave conhecida, mas não gera texto como o do manuscrito. |
| Tradução válida | < 1% | < 1% | 0 | Mesmo motivo. |
| Texto gerado por regras | ≈ 70% | ≈ 70% | 0 | A regra registrada pedia 75–80%, mas não tinha poder. O agrupamento por trechos também é alcançado por uma cifra com deriva e não favorece as regras. A validação cruzada não achou inflação, e o meu modelo também falha no hapax casado. Nada novo a favor, nada novo contra. |
| Livro de herbário, banhos e astrologia pelas figuras | ≈ 35% | ≈ 35% | 0 | Nenhum teste tocou as figuras. |
| O texto contém a informação das figuras | 10–15% | 9–14% | −1 | Caiu uma das propostas de cifra mais elaboradas. Um código palavra a palavra e uma cifra encadeada não foram testados, e o código passa no critério de agrupamento. |
| *Nova:* a Naibbe original gerou o manuscrito | – | ≤ 1% | – | Falha no agrupamento (R ≈ 0), na junção (0,03 contra 2,47), na repetição e no vocabulário no mesmo tamanho. As variantes com deriva consertam o agrupamento, mas não a junção nem o hapax. |

#### Hipótese registrada, não testada (sugestão do usuário)

As figuras podem ter sido feitas para despistar: alguém por volta de 1400 escondendo informação da Igreja e usando as imagens para enganar os leitores. Fica registrada, sem adesão. Um fato dos nossos dados é compatível com ela: em B, os rótulos reaparecem no texto da própria página em 19% dos casos, e em 20% com o texto embaralhado entre as páginas, ou seja, ao acaso. O mesmo fato é compatível com texto gerado por regras, e por enquanto não separa as duas. Ela só teria força se o texto mostrasse conteúdo de língua desacoplado das figuras, coisa que nenhum teste com poder mostrou até aqui.

### Veredito final (Fases 1 a 18)

**Resultados que ficam, com confiança alta:**
- nenhuma substituição silábica de tabela fixa, em seis línguas, lê o texto;
- o espaço é um corte de aparência silábica com regra de emenda: no dialeto B, a dependência na junção entre palavras é 2,5 vezes a de dentro da palavra;
- `-m` é abreviatura de margem;
- as palavras são unidades estáveis, com vocabulário de tamanho natural;
- a cifra Naibbe original, com as tabelas do autor, não gera texto como o do manuscrito: zera o agrupamento, apaga a dependência na junção e espalha cada palavra por 15 a 19 grafias.

**Minha melhor explicação, com cerca de 70%:** texto gerado por regras, com repertório que deriva ao longo da cópia. O ponto fraco dele é real: o vocabulário tem menos formas únicas que o do manuscrito no mesmo tamanho.

**O que segue em aberto:** uma notação com significado que mantenha palavras estáveis *e* a dependência na junção. A Naibbe não serve. Um código palavra a palavra ou uma cifra encadeada, em que a tabela de cada palavra depende do fim da anterior, ainda não foram testados com uma régua capaz de aprová-los.

### Resumo final

**Hipótese:** o silabário homofônico de tabela fixa foi refutado. A cifra Naibbe original, testada sobre latim real com as tabelas do autor, também não explica o manuscrito. A explicação mais econômica continua sendo um texto gerado por regras com repertório que deriva.

**Melhor frase traduzida:** f2r.2 → *et eis cis*, sem valor de prova.

**Teste:** nenhuma chave passou no teste da ordem. A Naibbe cifra e decifra latim perfeitamente, mas fica a −0,01 do agrupamento do manuscrito (escala em que B = 1) e a 0,03 contra 2,47 na junção entre palavras. Uma variante com deriva recupera o agrupamento, mas não a junção.

**Confiança:** chave < 1%; tradução < 1%; texto gerado por regras ≈ 70%; livro de herbário/banhos/astrologia pelas figuras ≈ 35%; texto contendo essa informação ≈ 9–14%; a Naibbe original como mecanismo ≤ 1%.

**Ponto mais fraco:** o agrupamento por trechos não decide nada; só exige deriva. A decisão passa a depender da junção entre palavras e da forma do vocabulário, e nesta última o meu próprio modelo também falha.

---

[← Fase 17](fase-17.md) · [Diário](../../DIARIO.md) · [README](../../README.md)
