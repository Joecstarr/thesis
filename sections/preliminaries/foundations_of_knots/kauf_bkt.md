<!-- prettier-ignore-start -->
(subsec-kauff)=
##### Kauffman Bracket
<!-- prettier-ignore-end -->

The Kauffman bracket is a function that takes knot diagrams as input and outputs
a Laurent polynomial[^lp] (@kb-def-kaufb).

```{prf:definition} Kauffman Definition 2.1[@kauffmanStateModelsJones1987;@lickorishIntroductionKnotTheory1997]
:label: kb-def-kaufb
The **Kauffman bracket** of an unoriented knot $K$, $\LA K\RA$, is the Laurent
polynomial with integer coefficients in $A$ given by the following relations:

1. $\LA\img{media/kauf_bkt/unknot} \RA=1$
2. $\LA K \sqcup \img{media/kauf_bkt/unknot} \RA=\LP-A^2-A^{\m2}\RP \LA K \RA$
3. $\LA \img{media/kauf_bkt/crossing/crossing_un} \RA=A\LA \img{media/kauf_bkt/type2/6a} \RA+A^{\ \m 1}\LA \img{media/kauf_bkt/type2/6b} \RA$

```

Since the number one and the unknot serve important roles for polynomials and
knots respectively, the first criterion is intuitive to select, when inventing a
knot polynomial invariant. For now, we focus our discussion on the third
criterion. The action we see in three is called **smoothing a crossing** and is
difficult to see. We will now present an intuitive model (originally by Jones
[@jonesJonesPolynomialDummies2014]) for what happens in the smoothing process.

Consider a crossing as a tangle, imagine that the over strand of the crossing is
the slot of a giant flathead screw, and attach a marker on either end of the
slot. Taking a screwdriver, we may turn the screw clockwise or anti-clockwise.
When the screw is turned, the markers (arrows in @fig-jp-screw-model) trace out
two arcs on the page. We create two new tangles by placing arcs inside each
tangle and connecting the endpoints joined by the marker trace. We can see, by
inspection, that the resulting pictures match the components of the third
condition of @kb-def-kaufb.

```{figure} ../../media/fig-jp-screw-model_iso.svg
:label: fig-jp-screw-model
A diagram depicting the screwdriver model of crossing smoothing. On top, we have
the original, pre smoothed crossing. On the bottom left, we have an anti-clockwise
smoothing. The result connects the top point to the left point and the bottom point
to the right point. On the bottom right we have a clockwise smoothing. The
result connects the top point to the right point and the bottom point
to the left point.
```

We will now move to proving that $\LA\,\RA$ is invariant under Reidemeister
moves. That is, when we start with two equivalent (by Reidemeister move) local
knot diagrams, the brackets of the two diagrams are equivalent. First, we prove
that $\LA\,\RA$ is invariant under the type II move. For a moment, we will write
the third condition of @kb-def-kaufb as
$\LA \img{media/kauf_bkt/crossing/crossing_un} \RA=A\LA \img{media/kauf_bkt/type2/6a} \RA+B\LA \img{media/kauf_bkt/type2/6b} \RA$
and the second as
$\LA K \sqcup \img{media/kauf_bkt/unknot} \RA=\LP-A^2-A^{\m2}\RP \LA K \RA$.

````{prf:theorem}
:label: thm-typeii_bkt
The equality of equation @thm-kb-math-t2 holds.
```{math}
:label: thm-kb-math-t2
\LA \img{media/kauf_bkt/type2/1}\RA=\LA \img{media/kauf_bkt/type2/6b} \RA
```
````

````{prf:proof}
We begin by smoothing the crossing on the right side of the diagram, we then smooth
the other crossing, this process yields the following chain of equalities,
combining like terms where appropriate.

```{math}
\begin{aligned}
 \bkt{media/kauf_bkt/type2/1}
&=A\bkt{media/kauf_bkt/type2/2a}+\LP
  B\RP\bkt{media/kauf_bkt/type2/2b}\\
&=A \LP
    A\bkt{media/kauf_bkt/type2/3a}+\LP
    B\RP\bkt{media/kauf_bkt/type2/4}\RP
 +\LP B\RP\LP A\bkt{media/kauf_bkt/type2/6b}+\LP
    B\RP\bkt{media/kauf_bkt/type2/6a}\RP\\
&=\LP A^2+ABC+B^2\RP\bkt{media/kauf_bkt/type2/6a}
 +\LP AB\RP\bkt{media/kauf_bkt/type2/6b}\\
\end{aligned}
```
To ensure that the bracket polynomial is an invariant we need
to select $A, \ B, \ C$ so that $A^2+ABC+B^2=0$ and $AB=1$. The conditions are satisfied by
$A=A$, $B=A^{\m 1}$, and $C=\LP-A^2-A^{\m2}\RP$ (justifying the second criteria
of @kb-def-kaufb). We then compute from the beginning @sec-kb-math-t2ftb,
showing the desired result.

```{math}
:label: sec-kb-math-t2ftb
\begin{aligned}
 \bkt{media/kauf_bkt/type2/1}
&=A\bkt{media/kauf_bkt/type2/2a}+\LP
B\RP\bkt{media/kauf_bkt/type2/2b}\\
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
````

Now, utilizing the fact that $\LA\,\RA$ is invariant for type II, we will prove
the same for type III.

````{prf:theorem}
:label: thm-typeiii_bkt
The equality of equation @thm-kb-math-t3 holds.
```{math}
:label: thm-kb-math-t3
\LA \img{media/kauf_bkt/type3/1}\RA=\LA \img{media/kauf_bkt/type3/6} \RA
```
````

````{prf:proof}
We begin by smoothing the crossing at the center of each diagram in the
equality, yielding

```{math}
:label: eq-kbkt-t3-1
\bkt{media/kauf_bkt/type3/1} =A\bkt{media/kauf_bkt/type3/2b}+A^{\ \m 1}\bkt{media/kauf_bkt/type3/2a}
```

```{math}
:label: eq-kbkt-t3-2
\bkt{media/kauf_bkt/type3/6} =A\bkt{media/kauf_bkt/type3/3b}+A^{\ \m 1}\bkt{media/kauf_bkt/type3/3a}
```
Now, on the clockwise smoothing equation @eq-kbkt-t3-1, we execute a type II
move and obtain @fig-inv-t3-c.

```{figure} ../../media/kauf_bkt/type3/2b_color.svg
:label: fig-inv-t3-c
On the left is a clockwise smoothing of the type 3 move type crossing
@fig-knot_def-r3. On the right is an application of the type II move on the
under strand.
```
Similarly, the anti-clockwise smoothing from equation @eq-kbkt-t3-2 we execute a type II
move to obtain @fig-inv-t3-cc.

```{figure} ../../media/kauf_bkt/type3/2a_color.svg
:label: fig-inv-t3-cc
On the left is an anti-clockwise smoothing of the type 3 move type crossing
@fig-knot_def-r3. On the right is an application of the type II move on the
under strand.
```

Since the type II move is invariant for the bracket polynomial (@thm-typeii_bkt)
the chain of equalities in equation @eq-kbkt-t3-final shows the desired result.

```{math}
:label: eq-kbkt-t3-final
\begin{aligned}
\bkt{media/kauf_bkt/type3/1} &=A\bkt{media/kauf_bkt/type3/2b}+A^{\ \m 1}\bkt{media/kauf_bkt/type3/2a}\\
&=A\bkt{media/kauf_bkt/type3/3b}+A^{\ \m 1}\bkt{media/kauf_bkt/type3/3a}&&\text{(by type II move)} \\
&=\bkt{media/kauf_bkt/type3/6}
\end{aligned}
```

````

Now for the final Reidemeister move, the type I move, we compute two chains of
equality, @sec-kb-math-t11 and @sec-kb-math-t12.

```{math}
:label: sec-kb-math-t11
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

```{math}
:label: sec-kb-math-t12
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

Observe, with @sec-kb-math-t11 and @sec-kb-math-t12, that the bracket polynomial
as it stands is not invariant under Reidemeister moves. We must augment the
bracket polynomial to find the invariance we would like.

```{include} writhe.md

```

```{include} type1.md

```
