---
title: "The Tanglenomicon: Tabulation of two string tangles"
authors:
    - name: Joe Starr
date: 2024-01-16
exports:
    - format: tex
      template: ./templates/arxiv
      logo: false
    - format: tex
      template: ./templates/editing
      logo: false
abstract: >
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
math:
    # Note the 'single quotes'
    '\N': '\mathbb{N}'
    '\Z': '\mathbb{Z}'
    '\Q': '\mathbb{Q}'
    '\R': '\mathbb{R}'
    '\T': '\mathscr{T}'
    '\M': '\mathscr{M}'
    '\LN': '\left.'
    '\RN': '\right.'
    '\LP': '\left('
    '\RP': '\right)'
    '\LS': '\left\lbrace'
    '\RS': '\right\rbrace'
    '\LA': '\left\langle'
    '\RA': '\right\rangle'
    '\LB': '\left['
    '\RB': '\right]'
    '\MM': '\ \middle|\ '
    '\abs': '\left\vert#1\right\vert'
    '\msr': 'm\left(#1\right)'
    '\inv': " #1^{-1}"
    '\img': '\text{ place holder }'
    '\bkt': '\LA \img{ #1}\RA'
    '\mvspc': '\hspace{.125cm}'
    '\mvtwt': '\frac{\mvspc}{\mvspc}\frac{\mvspc}{\mvspc}'
    '\mvtht': '\frac{\mvspc}{\mvspc}\frac{\mvspc}{\mvspc}\frac{\mvspc}{\mvspc}'
---

<!-- Include frontmatter -->

```{include} sections/frontmatter/frontmatter.md

```

<!-- Include chapters -->

```{include} sections/introduction/introduction.md

```

```{include} sections/background/background.md

```

```{include} sections/tabulation/tabulation.md

```

```{include} sections/software/software.md

```

```{include} sections/future_work/future_work.md

```
