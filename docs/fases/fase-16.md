# Fase 16 – E se for uma cifra com escolhas ao acaso?

[← Fase 15](fase-15.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 17 →](fase-17.md)

> **Em uma frase:** Uma objeção séria, testada com uma versão simplificada da cifra Naibbe.

**A pergunta.** Uma cifra que sorteia a grafia a cada vez (como a Naibbe, de 2025) enganaria os testes de significado?

**O que foi feito.** Com a pesquisa de 2026 trazida pelo usuário, o agente cifrou latim com duas versões próprias e simplificadas de cifras com sorteio e rodou os mesmos testes.

**O que deu.** A objeção procede em parte: essas cifras apagam os sinais de rótulo e de palavras-chave, como no Voynich. Mas também apagam o agrupamento por páginas e desfiguram o vocabulário, o que não acontece no Voynich.

**Por que importa.** Deixou pendente o teste com a cifra verdadeira, do autor, feito na Fase 18.

- **Código:** [`naibbe_calibracao.py`](../../src/naibbe_calibracao.py)
- **Saídas:** [`results/fase-16/`](../../results/fase-16/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 16 – E se for uma cifra com escolhas ao acaso?

O usuário trouxe a pesquisa de 2026 e a cifra "Naibbe" de Greshko. Ela gera texto com cara de Voynich a partir de latim ou italiano, partindo as palavras em pedaços e sorteando tabelas com dados ou cartas. Isso levanta uma objeção séria aos meus testes de significado: numa cifra assim, o mesmo nome sairia com grafias diferentes a cada vez, e os testes das Fases 10 a 13 dariam negativo mesmo com conteúdo.

Fiz uma calibração com uma versão minha, simplificada, não a dele. Cifrei o Isidoro de dois jeitos e rodei os mesmos testes:

| | Rótulo ecoado: concentração (fichas) | Agrupamento por página | Palavras-chave de página (acaso) | Razão tipo/ocorrência |
|---|---|---|---|---|
| Latim sem cifra | 0,667 (0,200) | +0,112 | 50 (4,1) | 0,326 |
| Homofônica por letra, palavra inteira, 3 tabelas sorteadas | 1,000 (0,830), quase sem ecos | +0,004 | 1 (1,8) | 0,760 |
| Estilo Naibbe: pedaços de 1–2 letras, 3 tabelas sorteadas | 0,001 (0,003) | +0,019 | 5 (2,3) | 0,006 |
| Voynich | 0,031 (0,076) | +0,109 | 20 (5,8) | 0,205 |

A objeção procede para os testes de rótulo e de palavras-chave: as duas cifras apagam esses sinais, como acontece no Voynich. Mas elas também apagam o agrupamento por página e desfiguram o vocabulário. Uma multiplica as formas (razão tipo/ocorrência 0,76); a outra as reduz a quase nada (0,006).

O Voynich tem vocabulário de tamanho natural e agrupamento de texto real. Suas palavras se comportam como unidades lexicais estáveis, que voltam com a mesma grafia e se concentram em trechos. Não se comportam como pedaços cifrados com sorteio. Uma cifra do tipo Naibbe, para explicar o manuscrito, precisaria reproduzir também essas duas propriedades, e a minha versão simplificada não reproduz. A de Greshko pode ser mais bem calibrada; esse é o teste a fazer com ela.

---

[← Fase 15](fase-15.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 17 →](fase-17.md)
