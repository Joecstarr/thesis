<!-- prettier-ignore-start -->
(calculus_on_trees)=
#### Calculus of Weighted Planar Trees
<!-- prettier-ignore-end -->

This section develops a set of moves, $F^\prime_3,\ F_2,\ F_1$ and $R^\pm$ on
the weighted planar trees described in @wpt-construc-sec-wptt. We will restrict
our discussion to a subset of the calculus of weighted planar trees. A full
description of the calculus can be found in Bonahon and Seibenmann
[@bonahonNewGeometricSplittings2016]. The
$F^\prime_3,\ F_2,\ F_1,\text{ and}\ R_\pm$ moves allow us to systematically
modify, without changing the topology, a weighted planar tree and form the basis
for the classification of the arborescent knots.

##### The $F^\prime_3$ Move

The first, and as we will see, most important, move we will define is the
$F_3^\prime$ move.

````{prf:definition} The $F^\prime_3$ move, Bonahon and Seibenmann Section 12.7.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-f3p_move

The $F_3^\prime$ move on a weighted arborescent tree moves a weight $w$ as in
@wpt-moves-fig-f3p_move-indef and, if $w$ is odd,
reverse the cyclic order of weights and bonds at all vertices of the purple
subtree lying at odd distance (count of edges between two vertices) from the vertex shown. Also, apply
$\xi$ ($z$-axis rotation @wpt-construc-fig-k4g) to all free bonds in the purple subtree that are attached to a vertex at
even distance from the vertex shown, and $\eta$ ($y$-axis rotation) to those at odd distance.

```{figure} ../../media/bands/moves/f3/f3p_def.svg
:label: wpt-moves-fig-f3p_move-indef
:width: 500px
An $F_3^\prime$ move on a subtree
```

````

The $F_3^\prime$ move is a derivative of the more general $F_3$ move described
in Bonahon and Seibenmann [@bonahonNewGeometricSplittings2016].

````{prf:definition} The $F_3$ move, Bonahon and Seibenmann Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-f3_move

Replace the left side of @wpt-moves-fig-f3_move-indef with the right side, where
the cyclic order of bonds and weights is reversed at all vertices in the purple
subtree of the vertex shown, and at odd distance from this vertex. Also, apply
$\xi$ ($z$-axis rotation) to all free bonds in the purple
subtree that are attached to a vertex at even distance from the vertex shown,
and $\eta$ ($y$-axis rotation) to those at odd distance.

```{figure} ../../media/bands/moves/f3/f3_def.svg
:label: wpt-moves-fig-f3_move-indef
:width: 500px
An $F_3$ move on a subtree. Note $F_3^\prime$ is equivalent to the case of
$X=0$ and $F_3$ carried out $W$ times.
```

````

###### $F_3^\prime$ on bands

Before we examine more deeply $F_3^\prime$ move on weighted planar trees, we
will focus on understanding $F_3^\prime$ move on the band model. The
$F_3^\prime$ move shifts a (or some) crossings across a plumbing square by
moving a half turn across a plumbing square. The translation of crossings across
child bands models the traditional **flype** move, of "Tait Flyping Conjecture"
{cite:p}`taitKnotsIIIII1900` fame. To see the correspondence between
$F_3^\prime$ and flype we need to view the plumbed child band as a tangle $T$.
We can then carry out $F_3^\prime$ over this tangle. Tracking the parts of this
operation, we can see the correspondence in @uc-c-f3-e-flype_and_bnd.

```{figure} ../../media/bands/moves/f3/bnd_f3.svg
:label: uc-c-f3-e-flype_and_bnd
:width: 500px
Flype and $F_3^\prime$
```

When this is carried out, for an odd number of crossings, the child band is
inverted so it lies inside the parent band (@uc-c-f3-e-flype_bnd). The inversion
reverses the cyclic order of the child, as described in @wpt-moves-def-f3p_move.

```{figure} ../../media/bands/moves/f3/bnd_only_f3.svg
:label: uc-c-f3-e-flype_bnd
:width: 500px
$F_3^\prime$ on the band model realization of the orange vertex and impacted
subtree.
```

Applying $F_3^\prime$ to an even number of crossings is equivalent to applying
the move on two sets of an odd number of crossings. When the first set of odd
crossings is applied, the child band is inverted the second set inverts the
child again, leaving it where it began (@wpt-moves-fig-example_f3-even-2).

```{figure} ../../media/bands/moves/f3/bnd_only_f3_even_2.svg
:label: wpt-moves-fig-example_f3-even-2
:width: 500px
 $F_3^\prime$ on the band model realization of the orange vertex. Note
 any children of the purple bands remain unchanged except for free bonds.
```

We expand to an example where the child band has descendants, as in
@uc-c-f3-e-cor. Observe that when the $F_3^\prime$ is applied in this case, the
child band and every band even distance from it (odd distance from the parent)
is inverted.

```{figure} ../../media/bands/moves/f3/cyclic_order_odd.svg
:label: uc-c-f3-e-cor
:width: 500px
Cyclic order reversal
```

###### $F_3^\prime$ Examples

Consider the weighted planar tree in @wpt-moves-fig-example_f3-even-1 and
@wpt-moves-fig-example_f3-odd_1, the left trees in each agree in all but a
weight of a single vertex, what we will call our object vertex which is marked
in orange. The weight of this object vertex has been changed from $-2$ in
@wpt-moves-fig-example_f3-even-1 to $-3$ in @wpt-moves-fig-example_f3-odd_1.

We will first walk through @wpt-moves-fig-example_f3-even-1. In this example,
our object weight is even, applying $F_3^\prime$ to the tree the impacted
subtree (purple subtree in @wpt-moves-fig-f3p_move-indef) is unchanged except
for free bonds which are altered as described in @wpt-moves-def-f3p_move.

```{figure} ../../media/bands/moves/f3/watt_rooted_even.svg
:label: wpt-moves-fig-example_f3-even-1
:width: 500px
$F_3^\prime$ on a weighted planar tree with even weight. The weight of the
object weight is even, so the impacted subtree is unchaged, except for labels of
free bonds.
```

In @wpt-moves-fig-example_f3-odd_1, the object weight is odd, applying
$F_3^\prime$ the cyclic order of vertices, of the impacted subtree at an odd
distance are reversed. Additionally, all free bonds in the impacted subtree are
altered as described in @wpt-moves-def-f3p_move.

```{figure} ../../media/bands/moves/f3/watt_rooted_odd.svg
:label: wpt-moves-fig-example_f3-odd_1
:width: 500px
$F_3^\prime$ on a weighted planar tree with odd weight clockwise. Note the
changes in the relative positions of subtrees after the application of
$F_3^\prime$.
```

##### The $F_2$ Move

Our second move, $F_2$, is a special application of the general $F_3$ move.

```{prf:definition} The $F_2$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: uc-c-f2-d-f2_t

The $F_2$ move on a weighted arborescent tangle tree reverses the cyclic order
at one vertex on the tree and at every vertex at even distance from it; also
apply $\eta$ ($y$-axis rotation) to every free bond of a vertex at even (or zero) distance, and
apply $\xi$ ($z$-axis rotation) to every free bond at odd distance.

```

$F_2$ is equivalent to applying $F_3$ to a vertex by moving a single weight
around a full cycle of the children, as in @wpt-moves-fig-example_f2_cycle. If
the vertex has no weights, the zero weight is split into a $+1$ and $-1$, one of
which completes the cycle. The $+1$ and $-1$ then cancel, returning the vertex
to zero weight. The result of carrying out $F_2$ on a weighted planar tree can
be seen in @wpt-moves-fig-example_f2.

````{prf:observation}
```{figure} ../../media/bands/moves/f2/f2_local.svg
:label: wpt-moves-fig-example_f2_cycle
:width: 500px
$F_3$ moving a weight in a complete cycle
```

```{figure} ../../media/bands/moves/f2/watt_rooted.svg
:label: wpt-moves-fig-example_f2
:width: 500px
$F_2$ on a weighted planar tree. Observe the changes to the entire tree, as
opposed to the changes of $F_3^\prime$ which impact only a subtree.
```
````


Observe that $F_2$ effectively partitions the vertices of a tree into two
equivalence classes of vertices, those and even distance from the root and those
an odd distance from the root. We write $F_2$ on the even class as $F_{2e}$ and
odd as $F_{2o}$.

##### The $F_1$ Move

The third of the $F$ moves is the $F_1$ move, which is a repeated application of
the $F_2$ move.

```{prf:definition} The $F_1$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: uc-c-f1-d-f1_t

The $F_1$ move on a weighted arborescent tangle tree reverses the cyclic order
of bonds and weights at every vertex of the graph and applies $\zeta$ ($x$-axis
rotation) to every free bond.
```

To realize $F_1$ as $F_2$ moves, we successivly apply $F_{2e}$ then $F_{2o}$ to
the tree. Observe that the combination of $F_{2e}$ and $F_{2o}$ modifies the
free bonds by $\xi\eta=\zeta$.

##### The $R^\pm$ moves

The $R$ move or ring move is the final move we will describe on weighted planar
tangle trees and deals with the ring subtrees of a tree. The result of a ring
move on a tangle can be seen in @wpt-moves-fig-example-r.

```{figure}../../media/bands/moves/R/example_ring.svg
:label: wpt-moves-fig-example-r

$R^-$ on on a tangle representation of a tree.

```

````{prf:definition} The $R^+$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-rp

Replace the left of @rmove-n-pic with the right, leaving both the blue
and purple subtrees unchanged.

```{figure} ../../media/bands/moves/R/p/def.svg
:label: rmove-p-pic
A $+$-ring subtree moving around a vertex. Equivlent to @wpt-moves-fig-example-r.
```

````

````{prf:definition} The $R^-$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-rm

Replace the left of @rmove-n-pic with the right, leaving both the blue
and purple subtrees unchanged.

```{figure} ../../media/bands/moves/R/n/def.svg
:label: rmove-n-pic
A $-$-ring subtree moving around a vertex. Equivlent to @wpt-moves-fig-example-r.
```

````
