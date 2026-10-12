# Fase 12 – Os rótulos da farmácia nomeiam as plantas?

[← Fase 11](fase-11.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 13 →](fase-13.md)

> **Em uma frase:** Os rótulos dos frascos e raízes não coincidem com as primeiras palavras das páginas de plantas.

**A pergunta.** Se os rótulos da seção farmacêutica forem nomes de plantas, eles reaparecem no começo das páginas do herbário?

**O que foi feito.** O agente comparou 235 rótulos farmacêuticos e 659 rótulos de outras seções com as 128 primeiras palavras das páginas de plantas, com três critérios fixados antes.

**O que deu.** Nenhum rótulo farmacêutico é igual a uma palavra de abertura do herbário. No critério mais frouxo, eles coincidem até menos que os rótulos de outras seções.

**Por que importa.** Mais um teste de 'conteúdo' que deu negativo.

- **Código:** [`farma_herbal.py`](../../src/farma_herbal.py)
- **Saídas:** [`results/fase-12/`](../../results/fase-12/)

Termos técnicos estão explicados no [glossário](../glossario.md).

---

## Texto técnico (trecho do relatório completo)

### Fase 12 – Os rótulos farmacêuticos nomeiam as plantas do herbário?

Nos herbários da época, a página costuma abrir com o nome da planta. Se os rótulos da seção farmacêutica (desenhos de raízes, folhas e frascos) forem nomes de plantas, deveriam coincidir com as primeiras palavras das páginas herbais. Deveriam coincidir mais do que os rótulos de outras seções, que têm a mesma morfologia de rótulo mas outro assunto.

Comparei 235 rótulos farmacêuticos e 659 rótulos de zodíaco, astronomia e cosmologia com as 128 palavras de cabeça herbais. Usei três critérios fixados antes:
- **exato:** farmacêutica 0,0%, outros rótulos 0,2%;
- **grafias fundidas:** 0,0% contra 0,5%;
- **"miolo"** (sem o primeiro e o último pedaço, para descontar um ornamento inicial e a terminação): 3,7% contra 5,6% (P = 0,87).

Nenhum rótulo farmacêutico é igual a uma palavra de cabeça herbal, e no critério mais frouxo eles coincidem menos que os outros rótulos. Não há sinal de que os rótulos farmacêuticos nomeiem as plantas do herbário, ao menos na posição em que um herbário poria o nome.

---

[← Fase 11](fase-11.md) · [Diário](../../DIARIO.md) · [README](../../README.md) · [Fase 13 →](fase-13.md)
