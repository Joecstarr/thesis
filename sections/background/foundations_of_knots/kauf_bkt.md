##### Kauffman Bracket

The Kauffman bracket is a function that takes knot diagrams as inputs and
outputs a polynomial with integer coefficients.

The Kauffman bracket of an unoriented knot $K$, $\LA K\RA$, is the Laurent
polynomial with integer coefficients in $A$ given by the following:

$\LA\img{media/kauf_bkt/unknot} \RA=1$

$\LA K \sqcup \img{media/kauf_bkt/unknot} \RA=\LP-A^2-A^2\RP \LA K \RA$

$\LA \img{media/kauf_bkt/crossing/crossing_un} \RA=A\LA \img{media/kauf_bkt/type2/6a} \RA+A^{-1}\LA \img{media/kauf_bkt/type2/6b} \RA$
[@kauffmanStateModelsJones1987] [@lickorishIntroductionKnotTheory1997]

We focus our discussion from here on the third criteria in the definition of the
kauffman bracket. The action in criteria three is called the smoothing of a
crossing and is perhaps not straight forward to see. We will now present an
intuitive model (originally by jones [@jonesJonesPolynomialDummies2014]) for
what happens in the smoothing process. Consider an unoriented crossing, imagine
that the over strand of the crossing is the drive (the slot) of a giant flathead
screw. Imagine also attaching to the screw a marker on either end of the drive,
the full model is shown in @fig-jp-screw-model.

```{figure} ./media/fig-jp-screw-model_iso.svg
:label: fig-jp-screw-model
@@@ TODO: Add content description
```


We can take a screw driver and turn the screw clockwise or anti-clockwise. When
the screw is turned, the markers traces out two arcs on the page. The arcs for a
clockwise turn can be seen in @fig-jp-screw-model and anti-clockwise in
@fig-jp-screw-model. Looking again at criteria three we notice that the
crossing, when smoothed, match those seen in @fig-jp-screw.

We will now move to proving that $\LA\,\RA$ is invariant under, Reidemeister II
and III moves. First we prove the type II move.

$$\LA \img{media/kauf_bkt/type2/1}\RA=\LA \img{media/kauf_bkt/type2/6b} \RA$$

We begin by smoothing the crossing on the left of the diagram, we then smooth
the other crossing this process yields the following chian of equalities.

Now, utilizing the fact $\LA\,\RA$ is invariant for type II we will prove the
same for type III.

$$\LA \img{media/kauf_bkt/type3/1}\RA=\LA \img{media/kauf_bkt/type3/6} \RA$$

We begin by smoothing the crossing on the center of each the diagram in the
equality, yielding @eq-kbkt-t3-1, enlarged in @fig-inv-t3-c we execute a type II
move to obtain @fig-inv-t3-ct2 the clockwise smoothing from @eq-kbkt-t3-2,
enlarged in @fig-inv-t3-ct2.

```{figure} ./media/kauf_bkt/type3/2b

@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/type3/3b

@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/type3/2a

@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/type3/3a

@@@ TODO: Add content description
```

Finally, following a process similar to the clockwise case on the anti-clockwise
smoothing @eq-kbkt-t3-1, enlarged in @fig-inv-t3-cc we execute two type II moves
to obtain @fig-inv-t3-cct2 the anti-clockwise smoothing from @eq-kbkt-t3-2,
enlarged in @fig-inv-t3-cct2. Since the type II move is invariant for bracket
polynomial, shown in @thm-typeII_bkt, this chain of equalities shows the desired
result.

Now for the final, and least straight, Reidemeister move we compute
$$\bkt{media/kauf_bkt/type1/1b} \bkt{media/kauf_bkt/type1/1}$$

```{include} writhe.md

```

###### Kauffman Bracket: Type I

With the writhe we're ready to approach the bracket polynomial applied to the
type I move. We augment the type I move with the addition of multiplication by a
$-A^{-3w\LP K\RP}$ term obtaining the following theorem.

We first compute our writhes
