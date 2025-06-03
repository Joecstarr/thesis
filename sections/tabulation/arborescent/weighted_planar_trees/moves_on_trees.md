<!-- prettier-ignore-start -->
(calculus_on_trees)=
#### Calculus of Weighted Planar Trees
<!-- prettier-ignore-end -->

This section develops a set of moves, $F^\prime_3,\ F_2,\ F_1$ and $R^\pm$ on
the weighted planar trees described in {prf:ref}`wpt-construc-sec-wptt`. We will
restrict our discussion to a subset of the calculus of weighted planar trees, a
full description of the calculus can be found in Bonahon and Seibenmann
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
{prf:ref}`wpt-moves-fig-f3p_move-indef` and, if $w$ is odd,
reverse the cyclic order of weights and bonds at all vertices of the purple
subtree lying at odd distance (count of edges between two vertices) from the vertex shown. Also, apply
$\xi$ ($z$-axis rotation @wpt-construc-fig-k4g) to all free bonds in the purple subtree that are attached to a vertex at
even distance from the vertex shown, and $\eta$ ($y$-axis rotation) to those at odd distance.

```{figure} ../../media/bands/moves/f3/f3_def.svg
:label: wpt-moves-fig-f3p_move-indef
:width: 500px
An $F_3^\prime$ move on a subtree
```

````

The $F_3^\prime$ move is a derivative of the more general $F_3$ move described
in Bonahon and Seibenmann [@bonahonNewGeometricSplittings2016]. The general
$F_3$ move is identical to the $F_3^\prime$ except $w$ can be split, that is, if
$w=3$ we can choose to move a single crossing.

###### $F_3^\prime$ on bands

Before we examine more deeply $F_3^\prime$ move on weighted planar trees, we
will focus on understanding $F_3^\prime$ move on the band model. The
$F_3^\prime$ move shifts a (or some) crossings across a plumbing square by
moving a half turn across a plumbing square. When this is carried out, for an
odd number of crossings, the child band is inverted so it lies inside the parent
band. The inversion reverses the cyclic order of the child, as described in
{prf:ref}`wpt-moves-def-f3p_move`. Applying $F_3^\prime$ to an even number of
crossings is equivalent to applying the move to two sets of an odd number of
crossings. When the first set of odd crossings is applied, the child band is
inverted the second set inverts the child again, leaving it where it began.

The translation of crossings across child bands models the traditional **flype**
move, of "Tait Flyping Conjecture" {cite:p}`taitKnotsIIIII1900` fame. To see the
correspondence of $F_3^\prime$ and flype we need to view the plumbed child band
as a tangle $T$. We can then carry out $F_3^\prime$ over this tangle. Tracking
the parts of this operation, we can see the correspondence in
{prf:ref}`uc-c-f3-e-flype_and_bnd`.

```{figure} ../../media/bands/moves/f3/bnd_f3.svg
:label: uc-c-f3-e-flype_and_bnd
:width: 500px
Flype and $F_3^\prime$
```

We expand to examples where the child band has descendants, as in
{prf:ref}`uc-c-f3-e-cor`. Observe that when the $F_3^\prime$ is applied in this
case, the child band and every band even distance from it (odd distance from the
parent) are inverted.

```{figure} ../../media/bands/moves/f3/cyclic_order_odd.svg
:label: uc-c-f3-e-cor
:width: 500px
Cyclic order reversal
```

###### $F_3^\prime$ Examples

Consider the weighted planar tree in {prf:ref}`wpt-moves-fig-example_f3-even`
and {prf:ref}`wpt-moves-fig-example_f3-odd`, the two trees agree in all but a
weight of a single vertex, what we will call our object vertex which is marked
in orange. The weight of this object vertex has been changed from $\ \m 2$ in
{prf:ref}`wpt-moves-fig-example_f3-even` to $\ \m 3$ in
{prf:ref}`wpt-moves-fig-example_f3-odd`.

````{prf:observation}
:label:wpt-moves-fig-example_f3-even

```{figure} ../../media/bands/moves/f3/watt_rooted_even.svg
:label: wpt-moves-fig-example_f3-even-1
:width: 500px
$F_3$ on a weighted planar tree with even weight.
```

```{figure} ../../media/bands/moves/f3/bnd_only_f3_even.svg
:label: wpt-moves-fig-example_f3-even-2
:width: 500px
 $F_3^\prime$ on the band model realization of the orange vertex. Note how
 any children of the purple bands remain unchanged.
```

````

We will first walk through {prf:ref}`wpt-moves-fig-example_f3-even`. In this
example, our object weight is even, applying $F_3^\prime$ to the tree the
impacted subtree (purple subtree in {prf:ref}`wpt-moves-fig-f3p_move-indef`) is
unchanged except for free bonds.

In {prf:ref}`wpt-moves-fig-example_f3-odd`, the object weight is odd, applying
$F_3^\prime$ the cyclic order of vertices, of the impacted subtree at an odd
distance are reversed.

````{prf:observation}
:label:wpt-moves-fig-example_f3-odd

```{figure} ../../media/bands/moves/f3/watt_rooted_odd.svg
:label: wpt-moves-fig-example_f3-odd_1
:width: 500px
$F_3^\prime$ on a weighted planar tree with odd weight clockwise. Note the
changes in the relative positions of subtrees after the application of
$F_3^\prime$.
```

```{figure} ../../media/bands/moves/f3/bnd_only_f3.svg
:label: uc-c-f3-e-flype_bnd
:width: 500px
$F_3^\prime$ on the band model realization of the orange vertex and impacted
subtree.
```

````

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
be seen in {prf:ref}`wpt-moves-fig-example_f2`.

````{prf:observation}
```{figure} ../../media/bands/moves/f2/f2_local.svg
:label: wpt-moves-fig-example_f2_cycle
:width: 500px
$F_3$ moving a weight in a complete cycle
```

```{figure} ../../media/bands/moves/f2/watt_rooted.svg
:label: wpt-moves-fig-example_f2
:width: 500px
$F_2$ on a weighted planar tree. Note the changes in the relative positions of
subtrees after the application of $F_2$.
```
````

Observe that $F_2$ effectively partitions a tree into two equivalence classes of
vertices, those even and odd distance from the root, we write $F_2$ on the even
class as $F_{2e}$ and odd as $F_{2o}$.

##### The $F_1$ Move

The third of the $F$ moves is the $F_1$ move, which is a repeated application of
the $F_2$ move.

```{prf:definition} The $F_1$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: uc-c-f1-d-f1_t

The $F_1$ move on a weighted arborescent tangle tree reverses the cyclic order
of bonds and weights at every vertex of the graph and applies $\zeta$ ($x$-axis
rotation) to every free bond.
```

To realize $F_1$ as a collection of $F_2$ moves, we apply both $F_{2e}$ and
$F_{2o}$ to the tree. Observe that the combination of $F_{2e}$ and $F_{2o}$
modifies free bonds by $\xi\eta=\zeta$.

##### The $R^\pm$ moves

The $R$ move or ring move is the final move we will describe on weighted planar
tangle trees and deals with the ring subtrees of a tree.

````{prf:definition} The $R^+$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-rp

Replace the left image with the right, leaving both the blue
and purple subtrees unchanged.

```{image} ../../media/bands/moves/R/p/def.svg
```

````

````{prf:definition} The $R^-$ move for weighted planar tangle trees, Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-rm

Replace the left image with the right, leaving both the blue
and purple subtrees unchanged.

```{image} ../../media/bands/moves/R/n/def.svg
```

````

The result of a ring move on a tangle can be seen in @wpt-moves-fig-example-r.

````{prf:observation}
:label: wpt-moves-fig-example-r

```{image} ../../media/bands/moves/R/example_ring.svg
```

$R^-$ on on a tangle representation of a tree.

````
