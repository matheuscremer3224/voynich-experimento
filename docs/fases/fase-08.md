# Fase 8 – Os experimentos que ficaram em aberto

[← Fase 7](fase-07.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 9 →](fase-09.md)

> **Em uma frase:** Onde o espaço cai, uma última chance para os silabários, e duas regras postas à prova.

**A pergunta.** O espaço do Voynich parece com que tipo de corte? E se as sílabas atravessarem as palavras?

**O que foi feito.** O agente tirou os espaços do texto e mediu quanto dá para recolocá-los só pelo contexto, comparando com o mesmo latim cortado de vários jeitos. Testou uma variante da hipótese em que as sílabas formam um fluxo contínuo (S′), com controles positivos em latim e italiano. Testou também se `k` e `t` são mesmo grafias da mesma letra, e o comportamento do `-m` no fim da linha.

**O que deu.** O espaço do Voynich se parece com a divisão em sílabas de um texto corrido, com uma regra de emenda entre os pedaços. A variante S′ também falhou, em latim, italiano e alemão (diferença de 0,7 a 1,1 ponto, contra 36 a 54 nos controles). A regra `k` = `t` caiu: a proporção muda com o assunto. O `-m` se confirmou como abreviatura de margem.

**Por que importa.** Separou o que é fato do sistema de escrita (espaço, emenda, `-m`) do que dependia da chave, que caiu.

- **Código:** [`espaco.py`](../../src/espaco.py), [`segmentacao.py`](../../src/segmentacao.py), [`unidade.py`](../../src/unidade.py), [`sprime.py`](../../src/sprime.py), [`controle_positivo2.py`](../../src/controle_positivo2.py), [`controle_positivo_it.py`](../../src/controle_positivo_it.py), [`lingua.py`](../../src/lingua.py), [`testes_r1_m.py`](../../src/testes_r1_m.py), [`diffs.py`](../../src/diffs.py)
- **Saídas:** [`results/fase-08/`](../../results/fase-08/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 8 – Continuação: os experimentos que ficaram em aberto

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

### Resumo atualizado

**Hipótese:** a família silábica (S e S′) caiu para latim, italiano e alemão. O que fica é estrutural: o espaço é um corte silábico num fluxo sem fronteiras de palavra, com uma regra de emenda entre os pedaços e uma abreviatura de fim de linha (`-m` no lugar de `-iin`, `-l` e `-r`).

**Melhor frase traduzida:** continua sendo f2r.2 → *et eis cis*, e continua sem valor de prova.

**Teste:** com a segmentação contínua, +0,7 ponto em latim, +1,1 em italiano e +0,8 em alemão, contra +36 a +54 nos controles positivos; a chave nula, treinada em texto embaralhado, dá +1,4.

**Confiança:** chave ≈ 1%, tradução < 1%, espaço como corte silábico ≈ 50%, `-m` como abreviatura ≈ 70%, interpretação geral do livro ≈ 40%.

**Ponto mais fraco:** só testei tabelas fixas e três línguas. Uma tabela que mude por seção, ou uma língua que não testei, ainda escapam.

---

[← Fase 7](fase-07.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 9 →](fase-09.md)
