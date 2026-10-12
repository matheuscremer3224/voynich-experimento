# Fase 13 – De onde vem o agrupamento por páginas?

[← Fase 12](fase-12.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 14 →](fase-14.md)

> **Em uma frase:** O agrupamento é de vocabulário, não de grafia, e se estende por trechos de várias páginas.

**A pergunta.** O agrupamento por páginas é só mudança de hábito de grafia? É de cada página ou de trechos longos?

**O que foi feito.** O agente fundiu as grafias variantes e recalculou; depois juntou páginas vizinhas em blocos de 2, 4 e 8 e comparou com o latim.

**O que deu.** Fundir as grafias quase não muda o agrupamento. E ele resiste em blocos de 8 páginas, enquanto no latim cai quando os blocos misturam assuntos.

**Por que importa.** O quadro passou a ser o de um vocabulário que muda devagar ao longo do livro, não o de um vocabulário próprio de cada planta.

- **Código:** [`agrupamento_grafia.py`](../../src/agrupamento_grafia.py)
- **Saídas:** [`results/fase-13/`](../../results/fase-13/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 13 – De onde vem o agrupamento por páginas?

O agrupamento por páginas era o único indício a favor de conteúdo que tinha sobrado da Fase 10. Duas perguntas sobre ele:

**É vocabulário ou só ortografia?** Se fosse mudança de hábitos de grafia (`k`/`t`, `ch`/`sh`, séries de `e`), fundir as variantes o derrubaria. Não derruba: o índice vai de +0,109 para +0,108 e, numa fusão mais forte (`o` = `a` e finais equivalentes), para +0,103. O agrupamento é de vocabulário.

**É de página ou de trecho longo?** Juntei páginas vizinhas em blocos e recalculei:

| Blocos de | Voynich | Latim de Isidoro |
|---|---|---|
| 1 página | +0,109 | +0,113 |
| 2 páginas | +0,107 | +0,114 |
| 4 páginas | +0,091 | +0,096 |
| 8 páginas | +0,088 | +0,060 |

No latim, o agrupamento cai quando os blocos passam a misturar assuntos. No Voynich, ele resiste em trechos de oito páginas. Junto com a escassez de palavras presas a uma página (Fase 10), o quadro é de um vocabulário que muda devagar ao longo do códice, não de um vocabulário próprio de cada planta ou de cada receita.

---

[← Fase 12](fase-12.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 14 →](fase-14.md)
