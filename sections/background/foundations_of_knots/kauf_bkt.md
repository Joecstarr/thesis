##### Kauffman Bracket

The Kauffman bracket is a function that takes a knot diagrams as input and
outputs a polynomial with integer coefficients.

```{prf:definition} Kauffman Bracket [@kauffmanStateModelsJones1987] [@lickorishIntroductionKnotTheory1997]
The **Kauffman bracket** of an unoriented knot $K$, $\LA K\RA$, is the Laurent
polynomial with integer coefficients in $A$ given by the following:

1. $\LA\img{media/kauf_bkt/unknot} \RA=1$
2. $\LA K \sqcup \img{media/kauf_bkt/unknot} \RA=\LP-A^2-A^2\RP \LA K \RA$
3. $\LA \img{media/kauf_bkt/crossing/crossing_un} \RA=A\LA \img{media/kauf_bkt/type2/6a} \RA+A^{\ \m 1}\LA \img{media/kauf_bkt/type2/6b} \RA$

```

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
crossing, when smoothed, match those seen in @fig-jp-screw-model.

We will now move to proving that $\LA\,\RA$ is invariant under, Reidemeister II
and III moves. First we prove the type II move.

```{prf:theorem}
:label: thm-typeii_bkt
$$\LA \img{media/kauf_bkt/type2/1}\RA=\LA \img{media/kauf_bkt/type2/6b} \RA$$
```

````{prf:proof}
We begin by smoothing the crossing on the left of the diagram, we then smooth
the other crossing this process yields the following chian of equalities.

```{math}
\begin{aligned}
 \bkt{media/kauf_bkt/type2/1}
&=A\bkt{media/kauf_bkt/type2/2a}+\LP
A^{\ \m 1}\RP\bkt{media/kauf_bkt/type2/2b}\\
 &=A \LP
A\bkt{media/kauf_bkt/type2/3a}+\LP
A^{\ \m 1}\RP\bkt{media/kauf_bkt/type2/4}\RP+\LP
A^{\ \m 1}\RP\LP A\bkt{media/kauf_bkt/type2/6b}+\LP
A^{\ \m 1}\RP\bkt{media/kauf_bkt/type2/6a}\RP\\
 &= \LP
A^2+A^{\ \m 2}\RP\bkt{media/kauf_bkt/type2/6a}+\bkt{media/kauf_bkt/type2/4}+\bkt{media/kauf_bkt/type2/6b}\\
 &= \LP
A^2+A^{\ \m 2}\RP\bkt{media/kauf_bkt/type2/6a}+\LP-A^{2}-A^{\ \m 2}\RP\bkt{media/kauf_bkt/type2/6a}+\bkt{media/kauf_bkt/type2/6b}\\
 &=\bkt{media/kauf_bkt/type2/6b}\\
\end{aligned}
```
showing the desired result.
````

Now, utilizing the fact $\LA\,\RA$ is invariant for type II we will prove the
same for type III.

```{prf:theorem}
:label: thm-typeiii_bkt
$$\LA \img{media/kauf_bkt/type3/1}\RA=\LA \img{media/kauf_bkt/type3/6} \RA$$
```

$$\LA \img{media/kauf_bkt/type3/1}\RA=\LA \img{media/kauf_bkt/type3/6} \RA$$

`````{prf:proof}
We begin by smoothing the crossing on the center of each the diagram in the
equality, yielding



```{math}
:label: eq-kbkt-t3-1
\bkt{media/kauf_bkt/type3/1} =A\bkt{media/kauf_bkt/type3/2b}+A^{\ \m 1}\bkt{media/kauf_bkt/type3/2a}
```

```{math}
:label: eq-kbkt-t3-2
\bkt{media/kauf_bkt/type3/6} =A\bkt{media/kauf_bkt/type3/3b}+A^{\ \m 1}\bkt{media/kauf_bkt/type3/3a}
```
Now on the clockwise smoothing @eq-kbkt-t3-1,
enlarged in @fig-inv-t3-c we execute a type II
move to obtain @fig-inv-t3-ct2 the clockwise
smoothing from @eq-kbkt-t3-2, enlarged in @fig-inv-t3-ct2
.

````{prf:observation}
```{figure} ./media/kauf_bkt/type3/2b
:label: fig-inv-t3-c
:width:100px
@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/type3/3b
:label: fig-inv-t3-ct2
:width:100px
@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/type3/2a
:label: fig-inv-t3-cc
:width:100px
@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/type3/3a
:label: fig-inv-t3-cct2
:width:100px
@@@ TODO: Add content description
```
````

Finally, following a process similar to the clockwise case on the anti-clockwise
smoothing @eq-kbkt-t3-1, enlarged in @fig-inv-t3-cc we execute two type II moves
to obtain @fig-inv-t3-cct2 the anti-clockwise smoothing from @eq-kbkt-t3-2,
enlarged in @fig-inv-t3-cct2. Since the type II move is invariant for bracket
polynomial, shown in @thm-typeii_bkt, this chain of equalities shows the desired
result.

`````

Now for the final, and least straight, Reidemeister move we compute

```{math}
\begin{aligned}
 \bkt{media/kauf_bkt/type1/1b} & =
A\bkt{media/kauf_bkt/type1/2a}+A^{\ \m 1}\bkt{media/kauf_bkt/type1/2b}\\
& = A\bkt{media/kauf_bkt/type1/3}+A^{\ \m 1}\LP
-A^2-A^{\ \m 2}\RP\bkt{media/kauf_bkt/type1/3}\\
& = \LP A+
-A^-A^{\ \m 3}\RP\bkt{media/kauf_bkt/type1/3}\\
& = -A^{\ \m 3}\bkt{media/kauf_bkt/type1/3}\\
\end{aligned}
```

and for the second flavor of type I move $\bkt{media/kauf_bkt/type1/1}$

```{math}
\begin{aligned}
 \bkt{media/kauf_bkt/type1/1} & =
A\bkt{media/kauf_bkt/type1/2b}+A^{\ \m 1}\bkt{media/kauf_bkt/type1/2a}\\
 & = A\LP
-A^2-A^{\ \m 2}\RP\bkt{media/kauf_bkt/type1/3}+A^{\ \m 1}\bkt{media/kauf_bkt/type1/3}\\
& = \LP
-A^3-A^{\ \m 1}+A^{\ \m 1}\RP\bkt{media/kauf_bkt/type1/3}\\
& = -A^{3}\bkt{media/kauf_bkt/type1/3}\\
\end{aligned}
```

```{include} writhe.md

```

```{include} type1.md

```
