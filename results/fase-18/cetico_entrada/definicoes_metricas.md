# Definições das métricas (do código comum)

```
Estrutura de 'página': {"folio": str, "I": seção, "L": dialeto, "lines": [(tipo, [palavras], inicio_de_paragrafo)]},
tipo "P" = texto corrido, "L" = rótulo. Todas as métricas são calculadas só sobre linhas "P" (os rótulos entram apenas
nas métricas de eco).

DEFINIÇÕES (as mesmas das Fases 1–17):
  h2           entropia condicional (bits) de letra dado a letra anterior, espaço contando como símbolo
  compr, dp    média e desvio do comprimento das palavras em unidades glíficas (ch, sh, cth, ckh, cph, cfh = 1)
  TTR          tipos / ocorrências; hapax = fração dos tipos com 1 ocorrência
  zipf         inclinação de log(freq) × log(posto) nas 1.000 formas mais frequentes
  razao        MI(última letra de w_n ; 1ª unidade de w_n+1) ÷ MI(1ª unidade ; última letra da mesma palavra, 3+ unid.),
               ambas descontado o valor com pares embaralhados
  F1esp        F1 ao recolocar os espaços a partir de ±2 unidades de contexto (treino nas linhas pares, teste nas ímpares)
  rep, quase   palavras vizinhas idênticas; vizinhas que diferem em uma unidade
  agrup        índice de agrupamento por página: média, nas palavras com 10+ ocorrências na seção, de
               (páginas esperadas ao acaso − páginas observadas) / esperadas
  bloco8       o mesmo índice com blocos de 8 páginas vizinhas
  chave_frac   fração das palavras com 5+ ocorrências na seção que têm metade ou mais das ocorrências numa só página
  viz          cosseno médio entre páginas vizinhas menos o cosseno entre páginas a 5+ de distância
  *_200        as quatro métricas de página acima, recalculadas depois de repaginar tudo em páginas de 200 fichas
               (corrige diferenças de tamanho de página entre corpora)
  eco, eco_acaso, conc_rot, conc_nulo   rótulos (3+ unidades): reaparecem no texto da própria página / de outra;
               concentração (fração das ocorrências que cai na página) dos ecoados × de fichas quaisquer da página
```
