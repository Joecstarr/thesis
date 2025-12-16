<!-- prettier-ignore-start -->
(calculus_on_trees)=
#### Calculus of Weighted Planar Trees
<!-- prettier-ignore-end -->

This subsection develops a set of moves, $F^\prime_3,\ F_2,\ F_1$, and $R^\pm$, on the weighted
planar trees described in @wpt-construc-sec-wptt. We will restrict our discussion to a subset of the
calculus of weighted planar trees. A full description of the calculus can be found in Bonahon and
Siebenmann [@bonahonNewGeometricSplittings2016]. The $F^\prime_3,\ F_2,\ F_1,\text{ and}\ R_\pm$
moves allow us to systematically modify, without changing the topology, a weighted planar tree and
form the basis for the classification of the arborescent knots.

##### The $F^\prime_3$ Move

The first move, and as we will see, the most important in distinguishing tangles, is the
$F_3^\prime$ move. In this move we consider the local picture of a vertex. In the local view,
isolate a single bond (half-edge corresponding to a plumbing square of a band), then move a weight
across that bond. The impact of this movement of a weight propagates to the descendants of the
subtree attached to the bond (plumbing square) but leaves unchanged all other weights and bonds
(including their attached subtrees) in the local view of the object vertex.

````{prf:definition} Bonahon and Siebenmann, Section 12.7.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-f3p_move

 The **$F_3^\prime$ move** on a weighted arborescent tree moves
  a weight $W$ as in
  @wpt-moves-fig-f3p_move-indef and, if $W$ is odd,
  reverses the cyclic order of
  weights and bonds at all vertices of the subtree attached to the
  purple bond (half-edge) lying at odd distance
  (count of edges between two vertices) from the vertex shown. Also, when $W$ is
  odd, apply $\xi$ ($X$-axis rotation
  @wpt-construc-fig-k4g) to all free bonds
  in the subtree attached to the purple bond (half-edge) that are
  attached to a vertex at even distance from the
  vertex shown, and $\eta$ ($Y$-axis rotation
  @wpt-construc-fig-k4g-y) to those
  at odd distance. The rotations are relative to the local orientations of the
  plumbing squares on the bands corresponding to vertices at odd distance from
  the vertex carrying weight $W$.


```{figure} ../../media/bands/moves/f3/f3p_def.svg
:label: wpt-moves-fig-f3p_move-indef

An $F_3^\prime$ move on a subtree. The purple bond indicates the subtree
impacted by the move. The blue portion of the local view indicates all other bonds and weights
of the vertex.
```
````

The $F_3^\prime$ move is a derivative of the more general $F_3$ move described in Bonahon and
Siebenmann [@bonahonNewGeometricSplittings2016].

````{prf:definition} Bonahon and Siebenmann, Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-f3_move


The **$F_3$ move** replaces the left side of
  @wpt-moves-fig-f3_move-indef with the right side, where
  the cyclic order of bonds and weights is reversed at all vertices
  in the subtree attached to the purple bond (half-edge) of the
  vertex shown and at odd distances from this vertex. Also, apply
  $\xi$ ($X$-axis rotation) to all free bonds in the subtree attached
  to the purple bond (half-edge) that are attached to a vertex at
  even distance from the vertex shown,
  and $\eta$ ($Y$-axis rotation) to those at odd distance. The rotations are
  relative to the orientation of the  plumbing square (Conway sphere) of the the
  band the weight is moving across, per
  @wpt-construc-fig-band_orientation.


```{figure} ../../media/bands/moves/f3/f3_def.svg
:label: wpt-moves-fig-f3_move-indef
An $F_3$ move on a subtree. The purple bond indicates the subtree
impacted by the move. The blue portion of the local view indicates all other bonds and weights
of the vertex.
```

````

```{note}
$F_3^\prime$ is equivalent, in @wpt-moves-fig-f3_move-indef, to
$X=0$, then executing $F_3$ $W$ times, decreasing $\abs{W}$ with each iteration.
```

We will now consider some examples of the $F_3^\prime$ move. While we explore these examples, we
view $F_3^\prime$ from the perspective of an object vertex (object band). The object vertex may have
one or more children that we will act on with $F^\prime_3$. When we translate $F_3$ and $F_3^\prime$
into practice we are free to operate on children as well as the parent of a vertex (band).

###### $F_3^\prime$ on bands

The translation of crossings across child bands models the traditional **flype** move of "Tait
Flyping Conjecture" [@taitKnotsIIIII1900] fame. To see the correspondence between $F_3^\prime$ and
flype we need to view the plumbed child (or parent) band as a tangle, $T$. We can then carry out
$F_3^\prime$ over this tangle. Tracking the parts of this operation, we can see the correspondence
in @uc-c-f3-e-flype_and_bnd.

```{figure} ../../media/bands/moves/f3/bnd_f3.svg
:label: uc-c-f3-e-flype_and_bnd

Flype and $F_3^\prime$, with orientation of the Conway sphere given by @wpt-construc-sec-wptt
```

When this is carried out, for an odd number of crossings, the child band is inverted so it lies
inside the parent band (@uc-c-f3-e-flype_bnd). The inversion reverses the cyclic order of the child,
as described in @wpt-moves-def-f3p_move.

```{figure} ../../media/bands/moves/f3/bnd_only_f3.svg
:label: uc-c-f3-e-flype_bnd

The odd $F_3^\prime$ case on a band model realization of the given portion of a tree, with local
$X$-axis in blue and $Y$-axis in red given relative to the purple band. Yielding a $\xi$ ($X$-axis
rotation) to all bands plumbed to the purple band or plumbed at even distance (counting plumbing
squares) from the orange band, and $\eta$ ($Y$-axis rotation) to the purple band and those plumbed
at odd distance from the orange band. Note that the orientations of the plumbing squares must agree
before and after $F_3^\prime$. Following the orientations with the left hand
(Figure~\ref{wpt-construc-fig-band_orientation}) rule shows the orientation of the purple band
reverses in $X$ and $Z$ in the second image due to the rotation in $Y$ (we are no longer looking
through the band in the second image).
```

Applying $F_3^\prime$ to an even number of crossings is equivalent to applying the move on two sets
of an odd number of crossings. When the first set of odd crossings is applied, the child band is
inverted; the second set inverts the child again, leaving it where it began
(@wpt-moves-fig-example_f3-even-2).

```{figure} ../../media/bands/moves/f3/bnd_only_f3_even_2.svg
:label: wpt-moves-fig-example_f3-even-2

 The even case of the $F_3^\prime$
    with the purple band and any descendants of the purple band
  remaining unchanged.
```

We expand to an example where the child band has descendants, as in @uc-c-f3-e-cor. Observe that
when the $F_3^\prime$ is applied in this case, the child band and every band even distance from it
(odd distance from the parent) are inverted.

```{figure} ../../media/bands/moves/f3/bands_odd_change.svg
:label: uc-c-f3-e-cor


$F_3^\prime$ when applied to a band (gray) with a child (orange) and grandchild (light blue). We
read the bands following the local orientation of the plumbing squares. Before the move is applied,
the child (orange) band is traversed as; the blue band, a green star, a green circle, and back to
the parent. After $F_3^\prime$ it is traversed as; a green circle, a green star, the blue band, and
back to the parent. The blue band is traversed as; yellow star, yellow circle, and back to orange
band.

```

###### $F_3^\prime$ Examples

Consider the weighted planar tree in @wpt-moves-fig-example_f3-even-1 and
@wpt-moves-fig-example_f3-odd_1, the left trees in each agree in all but a weight of a single
vertex, what we will call our object vertex which is marked in orange. The weight of this object
vertex has been changed from $-2$ in @wpt-moves-fig-example_f3-even-1 to $-3$ in
@wpt-moves-fig-example_f3-odd_1.

We will first walk through @wpt-moves-fig-example_f3-even-1. In this example, our object weight is
even, applying $F_3^\prime$ to the tree, the impacted subtree (purple subtree in
@wpt-moves-fig-f3p_move-indef) is unchanged except for free bonds, which are altered as described in
@wpt-moves-def-f3p_move.

```{figure} ../../media/bands/moves/f3/watt_rooted_even.svg
:label: wpt-moves-fig-example_f3-even-1


$F_3^\prime$ on a weighted planar tree with even weight. The weight of the object weight is even, so
the impacted subtree is unchanged.

```

In @wpt-moves-fig-example_f3-odd_1, the object weight is odd, applying $F_3^\prime$ the cyclic order
of vertices of the impacted subtree at an odd distance are reversed. Additionally, all free bonds in
the impacted subtree are altered as described in @wpt-moves-def-f3p_move.

```{figure} ../../media/bands/moves/f3/watt_rooted_odd.svg
:label: wpt-moves-fig-example_f3-odd_1

$F_3^\prime$ on a
    weighted planar tree with odd weight clockwise. Note the
    changes in the relative positions of subtrees after the application of
  $F_3^\prime$.

```

##### The $F_2$ Move

Our second move, $F_2$, is a special application of the general $F_3$ move.

```{prf:definition} Bonahon and Siebenmann, Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: uc-c-f2-d-f2_t


The **$F_2$ move** on a weighted arborescent tangle tree reverses the cyclic order of bonds and
weights at one vertex on the tree and at every vertex at even distance from it; also apply $\eta$
($Y$-axis rotation) to every free bond of a vertex at even (or zero) distance, and apply $\xi$
($X$-axis rotation) to every free bond at odd distance. The rotations are relative to the
orientation of the plumbing square (Conway sphere) of the band being acted on, per
@wpt-construc-sec-wptt.
```

$F_2$ is equivalent to applying $F_3$ to a vertex by moving a $\pm 1$ weight around a full cycle of
the children (and parent), as in @wpt-moves-fig-example_f2_cycle. If the vertex has no weights, the
zero weight is split into $+1$ and $-1$, one of which completes the cycle. The $+1$ and $-1$ then
cancel, returning the vertex to zero weight. The result of carrying out $F_2$ on a weighted planar
tree can be seen in @wpt-moves-fig-example_f2.

````{figure}
```{figure} ../../media/bands/moves/f2/f2_local.svg
:label: wpt-moves-fig-example_f2_cycle

$F_3$ moving a weight in a complete cycle
```

```{figure} ../../media/bands/moves/f2/watt_rooted.svg
:label: wpt-moves-fig-example_f2

$F_2$ on a weighted planar tree. Observe the changes to the entire tree, as
opposed to the changes of $F_3^\prime$ which impact only a subtree.
```
$F_2$ on a WPT
````

Observe that vertices can be partitioned into two equivalence classes. Those changed by $F_2$
applied at an even distance from the root, and those changed by $F_2$ applied at an odd distance
from the root. We write $F_2$ on the even class as $F_{2e}$ and odd as $F_{2o}$.

##### The $F_1$ Move

The third of the $F$ moves is the $F_1$ move, which is a repeated application of the $F_2$ move.

```{prf:definition} Bonahon and Siebenmann, Section 12.7.1 [@bonahonNewGeometricSplittings2016]
:label: uc-c-f1-d-f1_t


The **$F_1$ move** on a weighted arborescent tangle tree reverses the cyclic order of bonds and
weights at every vertex of the graph and applies $\zeta$ ($z$-axis rotation) to every free bond. The
rotations are relative to the orientation of the plumbing square (Conway sphere) of the band being
acted on, per @wpt-construc-sec-wptt.

```

To realize $F_1$ as $F_2$ moves, we successively apply $F_{2e}$ and then $F_{2o}$ to the tree.
Observe that the combination of $F_{2e}$ and $F_{2o}$ modifies the free bonds by $\xi\eta=\zeta$.

##### The $R^\pm$ moves

The $R$ move, or ring move is the final move we will describe on weighted planar tangle trees and
deals with the ring subtrees of a tree. The result of a ring move on a tangle can be seen in
@wpt-moves-fig-example-r.

```{figure} ../../media/bands/moves/R/example_ring.svg
:label: wpt-moves-fig-example-r

$R^-$ on on a tangle representation of a tree.

```

````{prf:definition} Bonahon and Siebenmann, Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-rm

The **$R^-$** replaces the left of @rmove-n-pic with the right, leaving the rest of the tree unchanged.

```{figure} ../../media/bands/moves/R/n/def.svg
:label: rmove-n-pic
A $\LP-\RP$-ring subtree moving around a vertex. Equivalent to @wpt-moves-fig-example-r.
```

````

```{note}
In @wpt-moves-fig-example-r the ring moves from the right to the left of the
tangle. This corresponds to the ring subtree in @wpt-moves-def-rm moving from
top to bottom of the orange portion of the tree.
```

````{prf:definition} Bonahon and Siebenmann, Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: wpt-moves-def-rp

The **$R^+$** replaces the left of @rmove-n-pic with the right, leaving the rest of the tree unchanged.

```{figure} ../../media/bands/moves/R/p/def.svg
:label: rmove-p-pic
A $\LP+\RP$-ring subtree moving around a vertex.
```

````
