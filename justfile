@_default:
    just --list

# Set up development environment
bootstrap:
    uv venv
    uv pip install -r requirements.txt
    mkdir -p _build

# This will only work for how I (@joecstarr) have zotero set up.
bib:
    zotero &
    curl "http://127.0.0.1:23119/better-bibtex/export/collection?/1/DNKTAVKK.biblatex" > ./biblio.bib

check-prettier:
    prettier README.md --check
    prettier main.md --check
    prettier "sections/**/*.md" --check

do-prettier:
    prettier -w README.md
    prettier -w main.md
    prettier -w "sections/**/*.md"

check-ruff:
    ruff format --check plugins

do-ruff:
    ruff format plugins

normalize-media:
    uv run ./resources/imgproc/svg_colors.py

# Build all the things.
init:
    myst clean --all -y
    myst init --write-toc
    mkdir -p _build/exports

build: bootstrap
    rip _build/exports
    mkdir -p _build/exports
    myst build -a
    cp -r resources/coloremoji/coloremoji _build/exports/myst_tex
    mkdir -p _build/exports/myst_tex/media/kauf_bkt && cp -r media/kauf_bkt _build/exports/myst_tex/media
    find ./_build/exports/myst_tex/media/ -iname "*.svg" -exec sh -c 'svg2pdf "$1" "${1%.*}.pdf" ' sh {} \;
    cp resources/coloremoji/coloremoji.sty _build/exports/myst_tex
    uv run ./resources/postprocess/nsf.py

html: bootstrap
    myst build --html

proc-svg-ws:
    uv run ./resources/imgproc/proc_svg_text.py .


proc-svg-size:
    uv run ./resources/imgproc/proc_svg_size.py .

proc-svg-mini:
    find../../media/ -iname "*.svg" -exec sh -c 'svgo -i "$1" -o "$1" ' sh {} \;

live:
    myst start

latex-main_0:
    cd ./_build/exports/myst_tex && \
    tectonic myst_0.tex --keep-logs --keep-intermediates

latex-main_1:
    cd ./_build/exports/myst_tex && \
    tectonic myst_1.tex --keep-logs --keep-intermediates

latex-main_2:
    cd ./_build/exports/myst_tex && \
    tectonic myst_2.tex --keep-logs --keep-intermediates

latex: latex-main_0 latex-main_1 latex-main_2
    echo built!
