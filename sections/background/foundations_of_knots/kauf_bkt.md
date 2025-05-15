# Kauffman Bracket

The Kauffman bracket is a function that takes knot diagrams as inputs and
outputs a polynomial with integer coefficients.

The Kauffman bracket of an unoriented knot $K$, $\LA K\RA$, is the Laurent
polynomial with integer coefficients in $A$ given by the following:

$\LA\img{images/kauf_bkt/unknot} \RA=1$

$\LA K \sqcup \img{images/kauf_bkt/unknot} \RA=\LP-A^2-A^2\RP \LA K \RA$

$\LA \img{images/kauf_bkt/crossing/crossing_un} \RA=A\LA \img{images/kauf_bkt/type2/6a} \RA+A^{-1}\LA \img{images/kauf_bkt/type2/6b} \RA$
@kauffmanStateModelsJones1987 lickorishIntroductionKnotTheory1997

We focus our discussion from here on the third criteria in the definition of the
kauffman bracket. The action in criteria three is called the smoothing of a
crossing and is perhaps not straight forward to see. We will now present an
intuitive model (originally by jones @jonesJonesPolynomialDummies2014) for what
happens in the smoothing process. Consider an unoriented crossing, imagine that
the over strand of the crossing is the drive (the slot) of a giant flathead
screw. Imagine also attaching to the screw a marker on either end of the drive,
the full model is shown in @fig-JP-screw-model.

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

We can take a screw driver and turn the screw clockwise or anti-clockwise. When
the screw is turned, the markers traces out two arcs on the page. The arcs for a
clockwise turn can be seen in @fig-JP-screw-traceC and anti-clockwise in
@fig-JP-screw-traceCC. Looking again at criteria three we notice that the
crossing, when smoothed, match those seen in @fig-JP-screw.

We will now move to proving that $\LA\,\RA$ is invariant under, Reidemeister II
and III moves. First we prove the type II move.

$$\LA \img{images/kauf_bkt/type2/1}\RA=\LA \img{images/kauf_bkt/type2/6b} \RA$$

We begin by smoothing the crossing on the left of the diagram, we then smooth
the other crossing this process yields the following chian of equalities.

Now, utilizing the fact $\LA\,\RA$ is invariant for type II we will prove the
same for type III.

$$\LA \img{images/kauf_bkt/type3/1}\RA=\LA \img{images/kauf_bkt/type3/6} \RA$$

We begin by smoothing the crossing on the center of each the diagram in the
equality, yielding @eq-kbkt-t3-1, enlarged in @fig-inv-t3-c we execute a type II
move to obtain @fig-inv-t3-ct2 the clockwise smoothing from @eq-kbkt-t3-2,
enlarged in @fig-inv-t3-ct2.

```{figure} ./images/kauf_bkt/type3/2b.svg

@@@ TODO: Add content description
```

```{figure} ./images/kauf_bkt/type3/3b.svg

@@@ TODO: Add content description
```

```{figure} ./images/kauf_bkt/type3/2a.svg

@@@ TODO: Add content description
```

```{figure} ./images/kauf_bkt/type3/3a.svg

@@@ TODO: Add content description
```

Finally, following a process similar to the clockwise case on the anti-clockwise
smoothing @eq-kbkt-t3-1, enlarged in @fig-inv-t3-cc we execute two type II moves
to obtain @fig-inv-t3-cct2 the anti-clockwise smoothing from @eq-kbkt-t3-2,
enlarged in @fig-inv-t3-cct2. Since the type II move is invariant for bracket
polynomial, shown in @thm-typeII_bkt, this chain of equalities shows the desired
result.

Now for the final, and least straight, Reidemeister move we compute
$
\bkt{images/kauf_bkt/type1/1b}$ $ \bkt{images/kauf_bkt/type1/1}$

```{include} writhe.md

@@@ TODO: Add content description
```

```{include} type_i.md

@@@ TODO: Add content description
```
