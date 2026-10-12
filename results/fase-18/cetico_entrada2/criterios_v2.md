# Fase 18b – Critérios registrados DEPOIS do parecer do Cético e ANTES de rodar os testes corretivos

Registrado pelo coordenador em 11/10/2026, depois de ler cetico_parecer.md e antes de executar qualquer teste abaixo.
O critério v1 (criterios.md) não foi editado. A decisão v1 continua sendo reportada tal como saiu: CONTRA.
O Cético mostrou que a régua v1 também reprova o latim sem cifra, o próprio dialeto B (no TTR) e o modelo de regras.
Por isso, o efeito v1 nas estimativas fica suspenso até o teste T1. Estes critérios são posteriores ao primeiro
resultado e motivados pelas objeções: valem como correção declarada, não como pré-registro original.

## Testes (o que será rodado, com previsão escrita antes)

T1 – Poder da regra v1 (Obj. 1a). Código palavra a palavra para cada texto latino: cada tipo latino vira o tipo de VB
     de mesmo posto de frequência. A regra v1 é aplicada sem mudança.
     Previsão: CONTRA (0 de 5 passam em P1+P2).
     Se a previsão se confirmar, a regra v1 é declarada sem poder e o efeito v1 não é aplicado.

T2 – Novo critério de P2 contra o nulo de cada corpus (Obj. 1b e 4).
     Nulo de X: 20 embaralhamentos globais de X (mc.embaralhar, nível global, sementes 100–119).
     X tem P2 se as duas condições valem:
       (a) agrup_200(X) > percentil 95 do nulo de X;
       (b) recuperação R = [agrup_200(X) − média do nulo de X] ÷ [agrup_200(VB) − média do nulo de VB] ≥ 0,25.
     bloco8_200 sai da decisão: o B embaralhado cai dentro da régua.
     viz_200 é reportado, mas não decide: na sanidade, falhou no dialeto A (0,114 > 0,10).
     Teste de poder do próprio T2, exigido antes de usá-lo:
       (i) VB passa;
       (ii) o código palavra a palavra de T1 passa em 3 ou mais de 5 textos;
       (iii) VB embaralhado globalmente (semente 7) falha.
     Se qualquer um falhar, T2 não serve e P2 fica INCONCLUSIVO.

T3 – P1 com tamanho casado (Obj. 3).
     TTR e hapax medidos nas primeiras N fichas de cada saída da Naibbe, com N = mediana do número de fichas das 10
     subamostras de B (sementes da Naibbe 1–3, mediana).
     Régua casada = [mín, máx] de TTR e hapax nas 10 subamostras de B, sem as seções.
     Passa se TTR e hapax caem dentro dela. zipf é reportado, mas não decide: só passa por causa de BxH.

Decisão v2 sobre a Naibbe original (textos latinos):
  - CONTRA: 3 ou mais de 5 falham em T2.
  - A FAVOR: 3 ou mais de 5 passam em T2 e em T3.
  - INCONCLUSIVO: qualquer outro caso.
  - Também é reportado o resultado sem Apício, exposto no teste de fumaça (Obj. 8).

T4 – Sanidade completa (Obj. 4).
     O embaralhado global tem de cair fora da régua (só reportado, porque bloco8_200 já sai).
     Também se mede quanto de agrup_200 em VB vem de dentro dos blocos de 200: embaralha-se dentro de cada bloco de
     200 fichas (sementes 7 e 8).

T5 – Nulo próprio e Naibbe com deriva (Obj. 5).
     (i) Para cada texto latino cifrado (semente 1): z de agrup_200, viz_200, razao, rep e F1esp contra 20
         embaralhamentos globais da própria saída.
         Se |z| < 2 nas cinco métricas em 3 ou mais textos, a falha da Naibbe é contada como UMA só (fichas
         permutáveis), e não como três.
     (ii) VARIANTES da Naibbe, que não são a cifra original. Tabelas e glifos idênticos; só muda o sorteio da tabela.
         Dirichlet: pesos de tabela sorteados por página, ~ Dirichlet(α · pesos do autor), α ∈ {1, 10, 100}.
         Memória: com probabilidade ρ ∈ {0,5; 0,9}, repete a(s) tabela(s) da última ocorrência do mesmo
         unigrama/bigrama do texto claro.
         A verificação de ambiguidade do autor é mantida. A decifração por decrypt_naibbe.py tem de continuar 100%.
         Se alguma variante passar em T2 em 3 ou mais de 5 textos latinos, P2 NÃO separa "cifra" de "regras": as duas
         precisam só de deriva. Nesse caso a estimativa "regras" não sobe por esta fase.

T6 – Validação cruzada do modelo de regras (Obj. 6).
     As páginas de B são divididas ao meio, alternando por ordem de fólio. O SlotModel é treinado com A + metade 1 de B.
     A deriva lexical gera texto sobre o leiaute da metade 2; o resultado é comparado com a metade 2 real (fora da
     amostra). Depois, ao contrário: treina-se com A + metade 2 e gera-se a metade 1.
     Referência: o modelo treinado com tudo, medido nas mesmas metades (dentro da amostra).
     Distância D = média, nas métricas de P1 e P3 (TTR, hapax, zipf, h2, compr, razao, F1esp, rep), de
     |gerado − real| ÷ largura da régua de B.
     Se D_fora ≥ 2 · D_dentro, o ajuste dentro da amostra inflava a proximidade: "regras" −5.
     O leiaute (comprimento das linhas, rótulos) continua vindo das páginas de destino; isso será declarado.

T7 – Texto organizado por entradas (Obj. 7).
     Isidoro XVII e Apício (um parágrafo numerado = uma entrada) são paginados por entrada: parágrafos inteiros,
     página fechada ao atingir 60 palavras. Mede-se, em claro e cifrado (Naibbe, semente 1), o agrup e o bloco8 em
     páginas naturais e a razão bloco8/agrup. Essa razão é comparada com a de VB em páginas naturais.
     O perfil é "local como o manuscrito" se, ao mesmo tempo:
       - bloco8/agrup ≤ 0,5;
       - agrup ≥ 0,075.

## Efeito nas estimativas (declarado antes de rodar)

Valores atuais: chave <1%; tradução <1%; texto gerado por regras ≈70%; livro de herbário/banhos/astrologia pelas
figuras ≈35%; o texto contém a informação das figuras 10–15%.

- Chave e tradução: não mudam em nenhum cenário, porque nenhuma chave foi testada.
- Livro pelas figuras: não muda, porque nenhum teste toca as figuras.
- Nova linha, "a Naibbe original (cifra de fragmentos de 1–2 letras com homófono sem memória) gerou o manuscrito":
  ≤1% se a decisão v2 for CONTRA e T5(i) indicar fichas permutáveis; 2–5% se for CONTRA sem permutabilidade;
  sem número se for INCONCLUSIVO.
- Texto gerado por regras (soma dos três termos, partindo de 70):
  - +2 se a decisão v2 for CONTRA e nenhuma variante de T5(ii) passar em T2;
  - 0 se alguma variante passar;
  - −5 se T6 indicar inflação (D_fora ≥ 2 · D_dentro).
- Conteúdo (partindo de 10–15):
  - −1 se a decisão v2 for CONTRA, porque uma das propostas de cifra mais elaboradas falhou;
  - +2 se T7 mostrar perfil local em pelo menos 1 dos 2 textos em claro e a Naibbe o destruir;
  - 0 se T7 não mostrar perfil local.
