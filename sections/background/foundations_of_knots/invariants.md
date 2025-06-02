### Knot Invariants

Our next topic of interest is that of a knot invariant. In general an invariant
for an object is a datum which is computed deterministically for the object and
remains unchanged under a concept of equivalence. In the knot case we will take
the concept of equality given in @subsec-knot_equivalence. As discussed in
@sec-history-of-tabulation invariants play an important role in tabulation and
will continue to be key players in through the remainder of this thesis. The
remainder of this section will be devoted to the construction of one of the most
historically useful knot invariants the Jones polynomial.

#### Jones Polynomial

The Jones polynomial was published by Vaughan Jones in 1985
[@jonesPolynomialInvariantKnots1985], discovered during his work on Von Neumann
algebras. A more combinatorial approach to the construction given here uses the
Kauffman bracket [@kauffmanStateModelsJones1987].

```{prf:definition} Jones Polynomial [@jonesPolynomialInvariantKnots1985; @lickorishIntroductionKnotTheory1997]
:label: def-jones
The Jones Polynomial $V\LP \mathscr{K}\RP$ of an oriented knot $\mathscr{K}$ is
the Laurent polynomial with integer coefficients in $t^{1/2}$. Defined by

$$
V\LP \mathscr{K}\RP=\LP\LP-A\RP^{\ \m 3w(K)}\LA K\RA\RP \_{t^{1/2}=A^{\ \m 2}}
$$

where $K$ is any oriented diagram for $\mathscr{K}$.
```

```{include} kauf_bkt.md

```

Having gained each equality needed for an invariant of knots we finish the
section with the following theorem.

```{prf:theorem}
The Jones polynomial ( @def-jones) is an invariant of oriented knots.

```

```{prf:proof}

Combining @thm-typeii_bkt, @thm-typeiii_bkt, and @thm-typei, substituting $A$ for
$ t$ we obtain the result.
```
