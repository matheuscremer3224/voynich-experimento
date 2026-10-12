# Parecer do Cético, 2ª rodada (Fase 18b)

Li só `cetico_entrada2/` (e a pasta da 1ª rodada). Refiz em Python: R e "passa" do T2, os z do T5(i), os D por rodada do T6, as medianas da tabela final e a régua do T3 contra cada referência. As contas batem, salvo o que está listado em (b).

## (a) As objeções foram resolvidas?
1. **Sim.** T1 confirma que a regra v1 não tem poder (0 de 5). T2 passou nos três testes de poder: código palavra a palavra com R de 0,40 a 1,95; VB embaralhado com 0,01. Ressalvas em (b) 2 e (b) 7.
2. **Sim.** "Regras" não sobe. Casas2 tem R 0,03, igual à Naibbe; a variante com deriva (α = 10) tem R de 0,37 a 0,42. P2 só pede deriva.
3. **Em parte.** No mesmo tamanho, o hapax confirma a falha: 60,3% a 63,0% contra 69,0% em VB e régua [68,0; 70,3]. Minha previsão para o TTR estava errada: deu 0,317, acima da régua, e não dentro. Mas a régua de TTR do T3 repete o vício da v1 (ver (b) 1).
4. **Sim.** bloco8_200 saiu da decisão, viz_200 passou a ser só informativo e P2 foi renomeado. Reconheço que meu subteste de blocos de 200 fichas estava mal posto: o resultado não muda por construção (0,0966 = 0,0966).
5. **Em parte.** A deriva está resolvida: P2 não separa cifra de regras. Mas a "não permutabilidade" vem de um critério meu (\|z\| < 2) que mede significância, não tamanho do efeito (ver (b) 5).
6. **Sim, no essencial.** D_fora / D_dentro = 0,330 / 0,240 = 1,38. Fora da amostra, o modelo de regras fica 3,5 a 4 vezes mais perto do manuscrito que a Naibbe, mesmo com tamanho casado. Restam duas ressalvas: só há 4 rodadas, e uma delas dá 2,26 (alvo 1, s14: 0,193 → 0,436); e a Naibbe não teve orçamento de reajuste.
7. **Não**, o teste ficou inconclusivo. Está neutralizado, porque o efeito registrado era 0. Aceito que o viés de "blocos por grupo" também enfraquece a evidência que usei (as razões bloco8/agrup).
8. **Sim.** Sem Apício, 4 de 4 falham. A assimetria continua, mas agora há teste de poder.

## (b) Erros novos nos testes corretivos
1. **A régua de TTR do T3 reprova o próprio VB contíguo.** Ela vem de subamostras de páginas espalhadas: [0,261; 0,294]. Ficam fora o VB contíguo (0,234), o VB embaralhado (0,233), casas2 (0,237) e regras‑deriva (0,215 a 0,226); o VA (0,296) fica acima. É o mesmo vício da v1, que o coordenador já declarou fatal.
   - O "0,317 contra 0,234" usa uma única janela de VB. A seção BxS sozinha, com 10.851 fichas, tem TTR 0,283 (tabela_comparador ii).
   - A margem mínima é então de cerca de 0,025 (apicius, 0,308), não de 0,083. A régua certa seria a distribuição de todas as janelas contíguas de VB com 10.974 fichas.
2. **O T2 não tem teto.** "Passa" quer dizer "tem agrupamento", não "agrupa como VB".
   - Memória ρ = 0,9 (TTR 0,08; hapax 41% a 43%; R 2,8 a 3,1) e α = 1 (R 1,7 a 2,2) "passam".
   - α = 10 recupera só 37% a 42% (agrup_200 de 0,035 a 0,041, abaixo de 0,076).
   - O que sustenta "P2 só exige deriva" é a continuidade: R de 0,06 a 0,08 com α = 100, 0,41 com α = 10, 1,7 a 2,2 com α = 1. Falta uma rodada com α entre 3 e 5 que mostre agrup, viz e bloco8 no nível de VB ao mesmo tempo.
3. **α = 1 não decifra 100%:** 0,99994 (isidoro), 0,99974 (plinio), 0,99977 (cesar). Isso viola o critério ("tem de continuar 100%") e contradiz o "decifração de 100%" das respostas. Cosmético.
4. **"Hapax de 41% a 53%"** nas variantes está errado: o mínimo é 40,0% (memória 0,5, hyginus, 0,4004). Cosmético.
5. **T5(i): o critério de permutabilidade (\|z\| < 2, proposto por mim) é sensível demais.** Com cerca de 30 mil fichas, ele detecta efeitos irrelevantes.
   - A razão de 0,024 a 0,040 (z +4,4 a +6,4) equivale a cerca de 1% da distância entre o embaralhado e VB (2,47).
   - A repetição imediata, de 0,11% a 0,17% contra 0,36% a 0,38% no nulo próprio, vai no sentido **oposto** ao de VB (0,91% contra 0,49%).
   - Nenhum dos dois desvios aproxima a Naibbe do manuscrito.
6. **T6: D_Naibbe (1,37 a 1,50) não foi medido nas mesmas condições.** Ele usa as saídas inteiras (24 a 35 mil fichas) contra VB inteiro, enquanto D_regras usa metades de mesmo tamanho.
   - Com o tamanho casado do T3, recalculei D_Naibbe = 1,14 a 1,23; o termo do hapax cai de 3,7–4,3 para 1,2–1,8.
   - O veredito não muda. Mas o ruído entre sementes da mesma metade (D_dentro de 0,19 a 0,30) é do tamanho do efeito: "sem inflação" é uma estimativa pontual, não uma demonstração.
7. **Os limiares do T2 foram fixados com os resultados já conhecidos** (o R mínimo do código, cerca de 0,40, já estava visível na v1). O coordenador declarou isso. O "CONTRA v2" é uma releitura dos números da v1, não evidência nova. A evidência nova desta rodada está no T3, no T5(ii) e no T6.

## (c) Proporcionalidade
- **Itens 1, 2 e 5 da conclusão:** proporcionais.
- **Item 3:** tirar o TTR da lista do que separa "sem depender de régua", ou dar a margem honesta (≥ 0,025, e dependente da janela). Razão e repetição imediata ficam; são robustas. Acrescentar que, no mesmo tamanho, regras‑deriva também falha em P1: hapax de 62,2% a 63,5%, abaixo de 68,0%, em 3 de 3 sementes. É também o maior termo de D no T6 (0,97 a 1,40). Pela regra v2 aplicada aos dois lados, regras‑deriva fica INCONCLUSIVO (passa no T2, falha no T3), e não aprovado. Isso deve ficar registrado como problema aberto do modelo de regras.
- **Item 4, estimativas:**
  - **Texto gerado por regras ≈ 70% (sem mudança):** proporcional.
  - **Conteúdo −1:** aceitável; está dentro do ruído, e 0 também seria defensável.
  - **Chave, tradução e livro pelas figuras (sem mudança):** corretos.
  - **"A Naibbe original gerou o manuscrito": 2–5% é desproporcional; deveria ser ≤ 1%.** A regra registrada foi seguida, mas o critério que a alimenta (meu) premia desvios triviais ou contrários ao manuscrito (ver (b) 5). Além disso, a Naibbe falha em P2 (R ≈ 0), na junção, na repetição, no hapax casado e no TTR, e as variantes com deriva também falham na junção (0,02 a 0,15) e no hapax (40% a 53%).
