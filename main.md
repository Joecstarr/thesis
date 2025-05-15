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
math:
    # Note the 'single quotes'
    '\N': '\mathbb{N}'
    '\Z': '\mathbb{Z}'
    '\Q': '\mathbb{Q}'
    '\R': '\mathbb{R}'
    '\T': '\mathscr{T}'
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
    '\bkt': '\LA \img{ #1}\RA'
    '\mvspc': '\hspace{.125cm}'
    '\mvtwt': '\frac{\mvspc}{\mvspc}\frac{\mvspc}{\mvspc}'
    '\mvtht': '\frac{\mvspc}{\mvspc}\frac{\mvspc}{\mvspc}\frac{\mvspc}{\mvspc}'
---

<!-- prettier-ignore-start -->

<!-- prettier-ignore-end -->


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

<!-- @@@-subfigure-start-@@@ -->

<!-- ```{figure} ./media/bands/bnd_sum_1.svg.svg
:label: UC-N-APN-E-4
:align: center
@@@ TODO
```

```{figure} ./media/bands/bnd_sum_2.svg.svg
:label: UC-N-APN-E-4
:align: center
@@@ TODO
``` -->

<!-- @@@-subfigure-end-@@@ -->
