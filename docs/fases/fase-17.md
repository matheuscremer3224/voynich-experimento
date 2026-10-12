# Fase 17 – Onde concordo e onde discordo do que foi feito em 2026

[← Fase 16](fase-16.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 18 →](fase-18.md)

> **Em uma frase:** Uma leitura crítica, com os dados do projeto, de um resumo sobre tentativas recentes com IA.

**A pergunta.** O que os nossos números permitem dizer sobre as afirmações feitas em 2026?

**O que foi feito.** O agente comparou quatro afirmações de um resumo trazido pelo usuário com os seus próprios resultados.

**O que deu.** Concordou com os fatos (vocabulário com cara de língua, agrupamento por seções, escribas), mas discordou de conclusões: Zipf e agrupamento não provam significado, a 'fôrma' rígida das palavras não é um paradoxo, e o problema não é a falta de uma Pedra de Roseta, mas sim de controles positivos.

**Por que importa.** Mostra como discordar com base em testes, não em opinião.

- **Código:** nenhum (fase de texto e interpretação)
- **Saídas:** nenhuma (fase sem saídas de código)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 17 – Onde eu concordo e onde discordo do que foi feito em 2026

Sobre o resumo trazido pelo usuário, com o que os meus dados permitem dizer:

- **"Obedece à Lei de Zipf e se agrupa por seções como um livro real".** Concordo com o fato e discordo da conclusão. Meus números confirmam um vocabulário de língua natural (razão tipo/ocorrência 0,205 contra 0,226 no latim; 70% de formas únicas contra 67%) e um agrupamento por página igual ao do latim (+0,109 contra +0,113). Mas um gerador sem conteúdo de seis regras reproduz a distribuição de frequências e as diferenças entre seções (Fase 10), e a deriva lexical lenta reproduz o agrupamento por trechos (Fase 15). Zipf e agrupamento não provam significado. Além disso, o jeito como o Voynich se agrupa (trechos longos, poucas palavras próprias de cada página) é diferente do de um texto real (Fase 13).
- **"Paradoxo da baixa entropia: 97% das palavras seguem uma fôrma".** O número depende da gramática usada; a minha, de seis casas, cobre 75,8% das ocorrências. E não vejo paradoxo. A baixa entropia e a fôrma rígida são exatamente o que se obtém quando o espaço corta pedaços de aparência silábica de um fluxo contínuo: o espaço voynichiano tem a previsibilidade de um corte silábico, F1 de 0,90 (Fase 8). Um gerador com essas regras dá h2 de 2,15 contra 2,14 do manuscrito.
- **"Cinco calígrafos".** É compatível com o que medi. As mãos coincidem com os dialetos A e B, e cada mão muda a proporção de `k`/`t` conforme a seção (Fase 8). Até onde sei, a identificação dos cinco escribas vem da paleografia de Lisa Fagin Davis (2020). Não verifiquei a atribuição à visão computacional.
- **"A IA esbarra na falta de uma Pedra de Roseta".** Aqui discordo com mais força. Para saber se há uma língua codificada, não é preciso Pedra de Roseta; é preciso controle positivo. Os meus mostram que o método enxergaria uma cifra silábica de tabela fixa em seis línguas (+33 a +54 pontos no teste da ordem). Mostram também que enxergaria uma palavra de cor usada com regularidade nas páginas com aquela cor (86–90% de detecção). Quando o sinal não aparece num teste com poder, a ausência é informação. O problema não é falta de dado de treino: no nível da palavra, o texto não se comporta como língua codificada.

### Veredito (Fases 1 a 17)

**Resultados que ficam, com confiança alta:**
- nenhuma substituição silábica de tabela fixa, em seis línguas, com tabela única ou por dialeto, lê o texto;
- o espaço é um corte de aparência silábica num fluxo contínuo, com uma regra de emenda entre as palavras;
- `-m` é uma abreviatura de margem, no lugar de `-iin`, `-l` e `-r`;
- as palavras são unidades estáveis, com vocabulário de tamanho natural, que derivam devagar ao longo do códice.

**Minha melhor explicação, com confiança de cerca de 70%:** o texto foi produzido por regras, e não por uma língua. Pedaços de aparência silábica, convenções de linha e de parágrafo, e um repertório de palavras que muda ao longo da cópia, distribuído entre escribas com hábitos próprios. É um livro ilustrado de herbário, banhos e astrologia médica, com aparência de saber cifrado.

**O que segue em aberto, com cerca de 30%:** uma notação com significado cuja correspondência não é uma tabela fixa e que, ainda assim, mantém palavras estáveis. Nem a minha versão de cifra com sorteio nem uma tabela fixa explicam isso. A versão bem calibrada da cifra Naibbe é o melhor candidato a testar.

### Resumo (Fases 1 a 17)

**Hipótese:** o silabário homofônico sobre o latim foi refutado, junto com as variantes em seis línguas e por dialeto. A explicação mais econômica é um texto gerado por regras de aparência silábica, com repertório que deriva, sem conteúdo linguístico recuperável.

**Melhor frase traduzida:** f2r.2 → *et eis cis*, sem valor de prova.

**Teste:** nenhuma chave passou no teste da ordem (≤ +1,7 ponto contra +33 a +54 nos controles). Não há acoplamento texto–imagem, e o teste tinha poder para isso. Os rótulos não se comportam como nomes. Um gerador de seis regras com deriva lexical reproduz a superfície e o agrupamento por trechos.

**Confiança:** chave < 1%, tradução < 1%, texto gerado por regras ≈ 70%, livro de herbário/banhos/astrologia pelas figuras ≈ 35%, texto contendo essa informação ≈ 10–15%.

**Ponto mais fraco:** a cifra Naibbe bem calibrada não foi testada. Se ela produzir palavras estáveis, vocabulário natural e agrupamento por trechos a partir de latim ou italiano reais, a balança volta para o conteúdo, e o caminho passa a ser decifrá-la por sorteio de tabelas, não por tabela fixa.

---

[← Fase 16](fase-16.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 18 →](fase-18.md)
