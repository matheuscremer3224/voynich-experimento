# Instruções comuns aos agentes da Fase 18

Contexto mínimo: estamos testando se a cifra Naibbe (Greshko 2025), com as tabelas originais, gera a partir de latim
real um texto parecido com o Manuscrito Voynich em três propriedades: palavras estáveis, vocabulário natural e
agrupamento lexical por trechos de páginas. Há três papéis rodando em paralelo (Cifrador, Comparador, Controle) e um
Cético depois.

Regras:
1. Use SOMENTE o módulo /home/claude/voynich/fase18/metricas_comuns.py para medir (leia o docstring no topo). Não
   reimplemente métricas e não edite esse módulo, o repositório da Naibbe nem os arquivos em /home/claude/voynich.
2. Rode Python com a variável PYTHONHASHSEED=0, por exemplo:
   `cd /home/claude/voynich/fase18 && PYTHONHASHSEED=0 python3 seu_script.py`
3. Escreva seus scripts e saídas só dentro de /home/claude/voynich/fase18/, com o prefixo do seu papel
   (cifrador_*, comparador_*, controle_*).
4. A máquina tem 2 núcleos e outros agentes rodam ao mesmo tempo: rode as coisas em sequência, sem paralelizar.
5. Saída obrigatória: um JSON (<papel>_resultados.json) e uma tabela Markdown (<papel>_tabela.md) feita com
   mc.tabela_md(...), mais as tabelas extras que o seu papel pedir. Na mensagem final, informe os caminhos, cole a
   tabela principal e descreva em até 10 linhas o que observou, sem interpretar além dos números. Reporte também
   qualquer erro, aviso ou comportamento estranho.
6. Os critérios de decisão estão em /home/claude/voynich/fase18/criterios.md. Não os altere.
