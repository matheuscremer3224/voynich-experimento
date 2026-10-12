"""Fase 5 – teste da chave congelada num trecho não usado, contra controles."""
import json, random, statistics as st, sys
from ivtff import parse, units
from chave import decode_word, segment, status
import lexicon

LEX = lexicon.load()
KEY = json.load(open("chave_final.json"))["tabela"]
rng = random.Random(2026)

def lines_of(path, folio, lt="P", comma="split"):
    L, _ = parse(path)
    return [(l.split if comma == "split" else l.join) for l in L if l.folio == folio and l.ltype[0] == lt]

def measure(lines):
    tot = lida = inc = multi = 0
    for ws in lines:
        dec = [decode_word(w, KEY) for w in ws]
        for j, i, f in segment(dec, LEX):
            n = i - j; tot += n
            s = status(f, LEX)
            if s == "lida": lida += n
            elif s == "incerta": inc += n
            if f and n > 1: multi += n
    return {"n": tot, "valida": (lida + inc) / tot, "lida": lida / tot, "incerta": inc / tot, "multi": multi / tot}

def word_shuffle(lines):
    flat = [w for ws in lines for w in ws]; rng.shuffle(flat); out = []; k = 0
    for ws in lines:
        out.append(flat[k:k + len(ws)]); k += len(ws)
    return out

def glyph_shuffle(lines):
    out = []
    for ws in lines:
        nw = []
        for w in ws:
            u = units(w); rng.shuffle(u); nw.append("".join(u))
        out.append(nw)
    return out

def summarize(name, lines, reps=200):
    real = measure(lines)
    ws = [measure(word_shuffle(lines)) for _ in range(reps)]
    gs = [measure(glyph_shuffle(lines)) for _ in range(reps)]
    def ms(xs, k):
        v = [x[k] for x in xs]; return st.mean(v), st.pstdev(v)
    p_ws = sum(x["valida"] >= real["valida"] for x in ws) / reps
    p_gs = sum(x["valida"] >= real["valida"] for x in gs) / reps
    print(f"\n{name}: {real['n']} palavras")
    print(f"  texto real           válidas {real['valida']:.1%} (lidas {real['lida']:.1%}, incertas {real['incerta']:.1%}); em grupos multipalavra {real['multi']:.1%}")
    m, s = ms(ws, "valida"); mm, sm = ms(ws, "multi")
    print(f"  ordem embaralhada    válidas {m:.1%} ± {s:.1%}; multipalavra {mm:.1%} ± {sm:.1%}; P(controle ≥ real) = {p_ws:.2f}")
    m2, s2 = ms(gs, "valida"); mm2, _ = ms(gs, "multi")
    print(f"  glifos embaralhados  válidas {m2:.1%} ± {s2:.1%}; multipalavra {mm2:.1%}; P(controle ≥ real) = {p_gs:.2f}")
    return {"real": real, "ws": (m, s, mm, sm, p_ws), "gs": (m2, s2, mm2, p_gs)}

if __name__ == "__main__":
    res = {}
    for path in ("ZL.txt", "RF.txt"):
        for folio in ("f4r", "f78r"):
            res[f"{path}:{folio}"] = summarize(f"{path} {folio}", lines_of(path, folio))
    for folio in ("f4r", "f78r"):
        res[f"ZL-join:{folio}"] = summarize(f"ZL.txt {folio} (vírgula = junção)", lines_of("ZL.txt", folio, comma="join"))
    # todo o texto fora do treino que não foi usado na Fase 4
    L, _ = parse("ZL.txt")
    json.dump(res, open("fase5_resultados.json", "w"), indent=1, default=str)
