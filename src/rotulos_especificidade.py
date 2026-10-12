"""Fase 10b – Os rótulos que reaparecem no texto da própria página são palavras CARACTERÍSTICAS daquela página
(como o nome de uma coisa desenhada) ou palavras quaisquer da página (como numa cópia mecânica)?
Concentração de uma palavra w numa página p: c_p(w) / c_total(w) (fração das ocorrências de w que caem em p).
Compara rótulos ecoados com fichas sorteadas do texto da mesma página (mesmo critério de tamanho: 3+ unidades)."""
import random, statistics as st, sys
from collections import Counter, defaultdict
from ivtff import parse, units

def analyze(pages_text, pages_labels, name, reps=200, out=print, seed=3):
    """pages_text: {pagina: [palavras do texto]}, pages_labels: {pagina: [palavras de rótulo]}"""
    rng = random.Random(seed)
    G = Counter(w for ws in pages_text.values() for w in ws)
    conc_lab = []; freq_lab = []; echo = 0; nlab = 0
    pools = {}
    for p, labs in pages_labels.items():
        T = Counter(pages_text.get(p, []))
        pool = [w for w in pages_text.get(p, []) if len(units(w)) >= 3]
        if not pool: continue
        pools[p] = (T, pool)
        for w in labs:
            if len(units(w)) < 3: continue
            nlab += 1
            if T[w] > 0:
                echo += 1; conc_lab.append(T[w] / G[w]); freq_lab.append(G[w])
    # fichas aleatórias do texto das mesmas páginas, uma por rótulo ecoado, na mesma proporção por página
    per_page = Counter()
    for p, labs in pages_labels.items():
        if p in pools:
            T, _ = pools[p]
            per_page[p] = sum(1 for w in labs if len(units(w)) >= 3 and T[w] > 0)
    sims_c = []; sims_f = []
    for _ in range(reps):
        cs = []; fs = []
        for p, k in per_page.items():
            T, pool = pools[p]
            for w in rng.sample(pool, min(k, len(pool))):
                cs.append(T[w] / G[w]); fs.append(G[w])
        sims_c.append(st.median(cs)); sims_f.append(st.median(fs))
    mc = st.median(conc_lab) if conc_lab else float("nan"); mf = st.median(freq_lab) if freq_lab else float("nan")
    p_c = sum(x >= mc for x in sims_c) / reps
    out(f"{name:44s} rótulos(3+) {nlab:4d}  ecoados {echo:3d} ({100*echo/max(nlab,1):.0f}%)  "
        f"concentração mediana {mc:.3f} vs fichas da página {st.mean(sims_c):.3f}  (P={p_c:.3f})  "
        f"frequência global mediana {mf:.0f} vs {st.mean(sims_f):.0f}")
    return {"nlab": nlab, "echo": echo, "conc": mc, "conc_null": st.mean(sims_c), "p": p_c, "freq": mf, "freq_null": st.mean(sims_f)}

def voynich_pages(path="ZL.txt", sections=None):
    L, pv = parse(path)
    text = defaultdict(list); labs = defaultdict(list)
    for l in L:
        if sections and pv[l.folio].get("I") not in sections: continue
        ws = [w for w in l.split if "?" not in w]
        (labs if l.ltype[0] == "L" else text)[l.folio].extend(ws)
    return text, labs

if __name__ == "__main__":
    for secs, name in [(None, "Voynich, todas as seções"), ({"B"}, "Voynich, biológica"), ({"C"}, "Voynich, cosmológica"),
                       ({"P"}, "Voynich, farmacêutica"), ({"Z"}, "Voynich, zodíaco"), ({"A"}, "Voynich, astronômica")]:
        t, l = voynich_pages(sections=secs)
        analyze(t, l, name)

def lift_test(pages_text, pages_labels, name, reps=200, out=print, seed=4):
    """Versão pareada por frequência: 'lift' = ocorrências na página / esperado se a palavra se espalhasse ao acaso.
    Cada rótulo ecoado é comparado com fichas da mesma página cuja frequência global é parecida (±50%)."""
    rng = random.Random(seed)
    G = Counter(w for ws in pages_text.values() for w in ws); N = sum(G.values())
    lab_lift = []; null_lifts = [[] for _ in range(reps)]
    for p, labs in pages_labels.items():
        Tl = pages_text.get(p, []); T = Counter(Tl); n = len(Tl)
        if not n: continue
        for w in labs:
            if len(units(w)) < 3 or T[w] == 0: continue
            lab_lift.append(T[w] / (G[w] * n / N))
            cands = [v for v in T if v != w and len(units(v)) >= 3 and G[w] / 1.5 <= G[v] <= G[w] * 1.5]
            if not cands:
                for r in null_lifts: r.append(float("nan"))
                continue
            weights = [T[v] for v in cands]
            for r in null_lifts:
                v = rng.choices(cands, weights)[0]; r.append(T[v] / (G[v] * n / N))
    ok = [i for i in range(len(lab_lift)) if null_lifts[0][i] == null_lifts[0][i]]
    ml = st.median([lab_lift[i] for i in ok]) if ok else float("nan")
    meds = [st.median([r[i] for i in ok]) for r in null_lifts] if ok else [float("nan")]
    p = sum(x >= ml for x in meds) / len(meds)
    out(f"{name:44s} ecoados pareados {len(ok):3d}  lift mediano dos rótulos {ml:5.2f}  vs fichas de frequência parecida {st.mean(meds):5.2f}  (P={p:.3f})")
    return ml, st.mean(meds), p

if __name__ == "__main__":
    print("\nVersão pareada por frequência global:")
    for secs, name in [(None, "Voynich, todas as seções"), ({"B"}, "Voynich, biológica"), ({"C"}, "Voynich, cosmológica"),
                       ({"P"}, "Voynich, farmacêutica"), ({"Z"}, "Voynich, zodíaco")]:
        t, l = voynich_pages(sections=secs)
        lift_test(t, l, name)
