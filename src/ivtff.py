"""Parser IVTFF para as transliterações ZL3b (EVA estendido) e RF1b (EVA básico).

Limpeza aplicada:
  * linhas '#' e comentários inline <!...> descartados (metadados);
  * variáveis de página ($Q $P $F $B $I $L $H $C $X) herdadas por cada linha;
  * <%> <$> (início/fim de parágrafo) removidos; <-> e <~> (interrupção por figura) = separador de palavra;
  * [a:b] (leituras alternativas do ZL) -> primeira opção;
  * {..} (ligadura) e @NNN; (caractere raro) = uma unidade;
  * '.' separa palavras; ',' (espaço incerto) gera duas versões: 'split' (é espaço) e 'join' (não é);
  * '?' = glifo ilegível; palavras com '?' ficam marcadas e saem das contagens lexicais.
"""
import re
from collections import namedtuple

Line = namedtuple("Line", "folio line pos ltype vars split join raw")

LOCUS = re.compile(r"^<(f\d+[rv]\d*|fRos)\.(\d+[a-z]?),([@+*=&~\-])([A-Z][a-z0-9]?)>\s*(.*)$")
PAGE = re.compile(r"^<(f\d+[rv]\d*|fRos)>\s*<!\s*(.*?)>")

# unidade glífica: ligadura, raro, bancada com gallows, ch/sh, letra (+ apóstrofo opcional)
UNIT = re.compile(r"\{[^}]*\}|@\d+;|c[ktpf]h|ch|sh|[a-zA-Z?]'?")


def _first_alt(m):
    return m.group(1).split(":")[0]


def clean_text(t):
    t = re.sub(r"<![^>]*>", "", t)          # comentários inline
    t = t.replace("<%>", "").replace("<$>", "")
    t = re.sub(r"<[-~]>", ".", t)            # quebra por figura
    t = re.sub(r"<[^>]*>", "", t)            # qualquer outra marcação
    # alternativas [a:b] (podem conter {} e @;)
    t = re.sub(r"\[([^\]]*)\]", _first_alt, t)
    t = re.sub(r"\.+", ".", t).strip(".")
    return t


def words_of(t, comma="split"):
    if comma == "split":
        t = t.replace(",", ".")
    else:
        t = t.replace(",", "")
    return [w for w in t.split(".") if w]


def units(word):
    return UNIT.findall(word)


def parse(path):
    pagevars = {}
    cur = {}
    out = []
    for raw in open(path, encoding="latin-1"):
        raw = raw.rstrip("\n\r")
        if not raw or raw.startswith("#"):
            continue
        m = PAGE.match(raw)
        if m:
            folio, v = m.groups()
            cur = dict(re.findall(r"\$(\w)=(\S+)", v))
            cur["folio"] = folio
            pagevars[folio] = cur
            continue
        m = LOCUS.match(raw)
        if not m:
            continue
        folio, ln, pos, lt, text = m.groups()
        vars_ = pagevars.get(folio, cur)
        t = clean_text(text)
        out.append(Line(folio, ln, pos, lt, vars_, words_of(t, "split"), words_of(t, "join"), text))
    return out, pagevars


def ltype_class(lt):
    return {"P": "paragrafo", "L": "rotulo", "C": "circulo", "R": "radial"}[lt[0]]


if __name__ == "__main__":
    for p in ("ZL.txt", "RF.txt"):
        lines, pv = parse(p)
        ns = sum(len(l.split) for l in lines)
        nj = sum(len(l.join) for l in lines)
        print(p, "linhas", len(lines), "páginas", len(pv), "palavras(split)", ns, "palavras(join)", nj)
