"""Onde ficam os dados externos (que não vêm no repositório; veja DADOS.md).

Por padrão, tudo fica em dados_externos/, na raiz do repositório:
    dados_externos/latin_library/   textos latinos (cópia CLTK da Latin Library)
    dados_externos/europarl_raw/    Europarl (NLTK data): italian/, german/
    dados_externos/ud/              treebanks Universal Dependencies (catalão, francês antigo, occitano)
    dados_externos/naibbe-cipher/   clone do repositório da cifra Naibbe (Greshko)
Para usar outras pastas, defina as variáveis de ambiente de mesmo nome (ex.: LATIN_LIBRARY=/caminho/).
As transliterações ZL.txt e RF.txt ficam aqui mesmo, em src/ (os scripts as abrem pelo nome)."""
import os

SRC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(SRC)
DADOS = os.environ.get("VOYNICH_DADOS", os.path.join(RAIZ, "dados_externos"))

def _pasta(var, padrao):
    return os.path.join(os.environ.get(var, os.path.join(DADOS, padrao)), "")

LATIN_LIBRARY = _pasta("LATIN_LIBRARY", "latin_library")
EUROPARL = _pasta("EUROPARL", "europarl_raw")
UD_TREEBANKS = _pasta("UD_TREEBANKS", "ud")
NAIBBE_REPO = os.environ.get("NAIBBE_REPO", os.path.join(DADOS, "naibbe-cipher"))
SAIDA_FASE18 = os.path.join(RAIZ, "results", "fase-18")
