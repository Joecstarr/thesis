@_default:
    just --list


# Set up development environment
bootstrap:
    uv venv
    uv pip install -r requirements.txt

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
    ruff format --check resources

do-ruff:
    ruff format plugins
    ruff format resources

normalize-media:
    uv run ./resources/imgproc/svg_colors.py

# Build all the things.
init:
    myst clean --all -y
    myst init --write-toc

build: bootstrap
    myst build ./main.md
    cp -r resources/coloremoji/coloremoji _build/exports/main_tex
    cp resources/coloremoji/coloremoji.sty _build/exports/main_tex
    uv run ./resources/postprocess/subfigure.py

html: bootstrap
    myst build ./main.md --html


live:
    myst start

latex-main_0:
    cd ./_build/exports/main_tex && \
    latexmk -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -lualatex main_0.tex

latex-main_1:
    cd ./_build/exports/main_tex && \
    latexmk -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -lualatex main_1.tex

latex: latex-main_0 latex-main_1
    echo built!