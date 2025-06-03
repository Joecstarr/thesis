<!-- prettier-ignore-start -->

<!-- prettier-ignore-end -->

#### Minimalization of CWPTT

##### CWPTT Are Not Minimal

A common measure for complexity of knots and their relatives is the **minimal
crossing number**. That being the least number of crossings needed to realize
the object in a diagram, we call that diagram the **minimal diagram**. It is
natural to ask if our CWPTT are minimal representatives among arborescent
representations. A quick analysis of the process of canonization demonstrates
that they are unfortunately far from minimal. An example of canonizing a tangle,
making the tangle non-minimal is seen in @minimal-fig-nonmin_min.

````{prf:observation}
:label:minimal-fig-nonmin

```{figure} ../../media/bands/non-minimal_minimalized.svg
:label: minimal-fig-nonmin_min
:width: 500px

A minimal presentation of a arborescent tangle in both its orthogonal projection
as well as its CWPTT.
```

```{figure} ../../media/bands/non-minimal.svg
:label: minimal-fig-nonmin_non
:width: 500px

A non-minimal presentation of the same arborescent tangle as
@minimal-fig-nonmin_min in both its orthogonal projection as well as its CWPTT.
```

````

##### Canonization Increases Complexity

In the previous section we saw that a CWPTT often does not realize a minimal
crossing representative for a tangle. Since minimal crossing number is such a
common measure for complexity, we should understand how non-minimal the process
of canonization can make a CWPTT. We will accomplish this by first identifying
which conditions of a CWPTT can potentially increase crossing number. The weight
condition ensures that each vertex has a single weight, consolidating all the
crossings into a single integral tangle. Meaning, enforcing the weight condition
on a weighted planar tree can only decrease crossing number. The stick condition
has three parts, the first two parts have no impact on the crossing number of
the tree. However, the third part can increase crossing number via the 1.2 move
, which increases crossing number by $1$.

````{prf:definition} The 1.2 move, Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: minimal-def-11and12

Replace the left side with the right side of @minimal-fig-move12



```{figure} ../../media/bands/moves/1/2/def.svg
:label: minimal-fig-move12
:width: 500px

Move 1.2 on a weighted planar tree.
```

````

The final condition to check is the positivity/negativity condition. We will
limit our analysis to the positivity condition, the negativity condition follows
identically. The positivity condition calls out four specific subtrees that must
not be present to satisfy the condition. Two of the trees can't be simplified
the @wpt-construc-fig-positivity_cond-3 and @wpt-construc-fig-positivity_cond-4.
The remaining two subtrees, @wpt-construc-fig-positivity_cond-1 and
@wpt-construc-fig-positivity_cond-2, can be transformed, via the 2.1 and 2.2
moves respectively. We can see from the definitions of the moves that the 2.1
move increases the crossing number by $1$ and the 2.2 move increases by $2$.

````{prf:definition} The 2.1 and 2.2 move, Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: minimal-def-21and22

1. Move 2.1: replace the left side with the right side of @minimal-fig-move11
2. Move 2.2: replace the left side with the right side of @minimal-fig-move12

```{figure} ../../media/bands/moves/2/1/def.svg
:label: minimal-fig-move11
:width: 500px

Move 2.1 on a weighted planar tree.
```
```{figure} ../../media/bands/moves/2/2/def.svg
:label: minimal-fig-move22
:width: 500px

Move 2.2 on a weighted planar tree.
```

````

##### Bounding Complexity

We are now prepared to give a bound for the complexity of the canonization of a
weighted planar tree. Given a weighted planar tree $\Gamma$ and vertices
$V=\LS v_i\RS_i^n$, additionally let $\Gamma_c$ be the canonization of $\Gamma$.
In the worst case, each vertex in $\Gamma$ increases the crossing number by $2$
with a $2.2$ move. We can then bound the crossing number of $\Gamma$ as in
@minimal-eq-upper-bound.

```{math}
:label: minimal-eq-upper-bound
\text{ACN}\LP \Gamma\RP \leq \text{ACN}\LP \Gamma_c\RP\leq 2\cdot\abs{V}+\text{ACN}\LP\Gamma\RP
```
