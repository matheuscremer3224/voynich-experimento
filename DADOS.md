# Onde baixar os dados

[← README](README.md) · [Como rodar o código](src/README.md)

Este repositório **não inclui** as transcrições do manuscrito, o PDF com as imagens nem a cifra Naibbe (só três páginas de exemplo, em baixa resolução, para o README). Eles pertencem aos seus autores e devem ser baixados das fontes abaixo. Também não inclui os textos de comparação (latim, italiano, alemão etc.), que são grandes e têm licenças próprias.

Depois de baixar, a organização esperada é esta:

```text
voynich-experimento/
├── src/
│   ├── ZL.txt                ← cópia de ZL3b-n.txt
│   └── RF.txt                ← cópia de RF1b-er.txt
└── dados_externos/
    ├── latin_library/        ← textos latinos (pastas isidore/, apicius/, ...)
    ├── europarl_raw/         ← pastas italian/ e german/
    ├── ud/                   ← UD_Catalan-AnCora/, UD_Old_French-SRCMF/, UD_Occitan-TTB/
    └── naibbe-cipher/        ← clone do repositório da cifra Naibbe
```

Para usar outras pastas, defina as variáveis de ambiente `LATIN_LIBRARY`, `EUROPARL`, `UD_TREEBANKS` e `NAIBBE_REPO` (veja [`src/config.py`](src/config.py)).

---

## 1. Transcrições do manuscrito (obrigatórias)

São as fontes de todas as contagens. Estão no formato IVTFF, com o alfabeto EVA.

| Arquivo | O que é | Onde baixar |
|---|---|---|
| `ZL3b-n.txt` | Transcrição Zandbergen–Landini, versão 3b, de 13/05/2025, em EVA estendido. Fonte principal | Página de transcrições do site de René Zandbergen: [voynich.nu/transcr.html](https://www.voynich.nu/transcr.html) |
| `RF1b-er.txt` | Transcrição de referência RF1b, em EVA básico. Usada para conferência | Mesma página |

Copie os dois para `src/ZL.txt` e `src/RF.txt`. O formato está descrito em [IVTFF_format.pdf](https://www.voynich.nu/software/ivtt/IVTFF_format.pdf), no mesmo site.

## 2. Imagens do manuscrito (só para a Fase 11)

- **Original:** Beinecke Rare Book & Manuscript Library, Yale University, *Cipher Manuscript*, MS 408. [Página do manuscrito na Beinecke](https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript), com acesso ao acervo digital.
- **Cópia completa:** [archive.org/details/voynich_MS_408](https://archive.org/details/voynich_MS_408).

Três páginas (f2r, f71r e f78r) estão em [`docs/imagens/`](docs/imagens/), em baixa resolução, só para ilustrar o README. O PDF completo não vem no repositório.

O experimento usou um PDF com as imagens dos fólios. O script da Fase 11 (`src/imagem_texto.py`) espera as páginas extraídas como `src/pdfimg/p001.jpg`, `p002.jpg` etc. (por exemplo, com `pdftoppm -jpeg -r 100 voynich.pdf src/pdfimg/p`). A correspondência entre fólio e página do PDF está em `src/zl_paginas.json`; no PDF usado, a página do PDF era a página ZL + 2 até o fólio 66. Com outro PDF, confira essa correspondência antes. As medidas de cor já extraídas estão em `src/imagem_features.json`, então os outros scripts da Fase 11 rodam sem as imagens.

## 3. Cifra Naibbe (só para a Fase 18)

- **Código e tabelas:** [github.com/greshko/naibbe-cipher](https://github.com/greshko/naibbe-cipher). Usamos `naibbe_v2.py`, `decrypt_naibbe.py` e `references/naibbe_tables.csv`, sem nenhuma alteração.
  ```bash
  git clone https://github.com/greshko/naibbe-cipher dados_externos/naibbe-cipher
  ```
- **Artigo (cite se usar):** Greshko, Michael A. (2025). "The Naibbe cipher: a substitution cipher that encrypts Latin and Italian as Voynich Manuscript-like ciphertext". *Cryptologia*. [doi:10.1080/01611194.2025.2566408](https://doi.org/10.1080/01611194.2025.2566408).
- **Dados suplementares do autor:** [doi:10.5281/zenodo.16415087](https://doi.org/10.5281/zenodo.16415087).
- **Licença:** MIT modificada, que exige manter o aviso de copyright e citar o artigo.

Dois dos textos cifrados na Fase 18 vêm desse mesmo repositório: Plínio, *História Natural* XVI (`input/examples/nathist_book16.txt`), e Dante, *Divina Comédia* (`input/examples/divina_commedia.txt`).

## 4. Textos de comparação

| Uso | Corpus | Onde baixar | Pasta esperada |
|---|---|---|---|
| Latim: léxico, modelo de trigramas, controles positivos, Fase 18 | Latin Library, cópia do projeto CLTK | [github.com/cltk/lat_text_latin_library](https://github.com/cltk/lat_text_latin_library) | `dados_externos/latin_library/` |
| Italiano e alemão (Fase 8); italiano moderno (Fase 18) | Europarl, distribuição do NLTK | [europarl_raw.zip](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/europarl_raw.zip) | `dados_externos/europarl_raw/` |
| Catalão, francês antigo, occitano (Fase 9) | Treebanks Universal Dependencies | [UD_Catalan-AnCora](https://github.com/UniversalDependencies/UD_Catalan-AnCora), [UD_Old_French-SRCMF](https://github.com/UniversalDependencies/UD_Old_French-SRCMF), [UD_Occitan-TTB](https://github.com/UniversalDependencies/UD_Occitan-TTB) | `dados_externos/ud/` |

Arquivos da Latin Library usados: `isidore/` (todos os livros; em especial 4, 12, 16 e 17), `apicius/` (1 a 5), `columella/`, `bible/`, `aquinas/`, `hyginus/` (1 a 4), `caesar/` (`gall1.txt` e `gall2.txt`) e os textos de Guilherme de Conches (`wmconchesdogma.txt`, `wmconchesphil.txt`).

O léxico latino já processado vem pronto em `src/lexicon_latim.json`. Por isso, as Fases 3 a 5 rodam sem baixar a Latin Library. Os modelos de italiano, alemão, catalão, francês antigo e occitano (`modelo_*.json`) não vêm no repositório: `src/lingua.py` os recria na primeira execução, a partir dos corpora acima.

Cada corpus tem a sua licença; consulte as páginas de origem antes de redistribuir qualquer parte deles.
