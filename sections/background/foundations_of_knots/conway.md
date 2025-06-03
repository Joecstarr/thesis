#### Conway Notation

In @sec-history-of-tabulation, we saw that Conway claimed to have enumerated
knots up to 11 crossings in "a few hours". Conway accomplished this by breaking
knots into building blocks he called tangles. This section gives an outline of
the tools he used to achieve those "a few hours" of amazing efficiency.

<!-- prettier-ignore-start -->
(subsubsec-deftangles)=
##### Definition of a Tangle
<!-- prettier-ignore-end -->

Our first step in unlocking Conway's tabulation secrets is the definition of a
tangle. We will give Conway's original definition followed by a description of
what this looks like for a three three dimensional embedding for a knot.

```{prf:definition} Tangle [@conwayEnumerationKnotsLinks1970]
We define a **tangle** as a portion of a knot diagram from which there emerge just 4
arcs pointing in the compass directions $NW,\ NE,\ SW,\ \text{and }SE$.
```

This can be thought of as drawing a circle around, or slamming a cookie cutter
onto, a knot diagram. Then cutting off the parts of the knot laying outside the
circle/cookie cutter, this process is seen in @fig-knot2tangle.

```{figure} ./media/tangle_maker.svg
:label: fig-knot2tangle
@@@ TODO: Add content description
```

These circular boundaries that split knots at four points are called Conway
circles, and we call the points $NW,\ NE,\ SW,\ \text{and }SE$ boundary points.
Formally, we can consider a Conway circle to be a Jordan curve meeting the knot
diagram in exactly four points [@bonahonNewGeometricSplittings2016]. In general,
we prefer our Conway circles to be circles in the colloquial sense. Luckily, the
circle and Jordan curve constructions are equivalent, this can be seen by a
straightforward isotopy of one into the other. We move our attention to the
three dimensional analog for a Conway circle, the Conway sphere. A Conway
sphere, similar to the Conway circle, is a $S^2$ that encapsulates a portion of
a knot so that the knot intersects the sphere in exactly four points. Here we
see the first example of our preference for ambient space to be $S^3$ as opposed
to $\R^3$. When a knot in $S^3$ is split by a Conway sphere, the ambient $S^3$
is decomposed into two $B^3$, each with a portion of the knot.

<!-- prettier-ignore-start -->
(subsubsec-basic_tangles)=
##### Basic Tangles
<!-- prettier-ignore-end -->

Often, when thinking about a new construction, we focus on what is the simplest
object that can be created with the construction. For the case of drawing Conway
circles to build tangles, the simplest tangles are the tangle with no crossings
as the tangle with a single crossing. The $+1$ and $0$ tangles can be seen in
@fig-basic_tangles.

````{prf:observation}
:label: fig-basic_tangles


```{figure} ./media/0.svg
:label: prelim-fig-basic_0
:width: 500px
A tangle with no crossings, called the $0$ tangle.
```

```{figure} ./media/1.svg
:label: prelim-fig-basic_1
:width: 500px
A tangle with a single crossings, called the $1$ tangle.
```
````

<!-- prettier-ignore-start -->
(subsubsec-tangle_flips)=
##### Rotation and Mirroring of Tangles
<!-- prettier-ignore-end -->

Consider a generic tangle, as seen in @fig-generic_tangle, where ambient
orientation of data in the interior of the Conway circle is indicated by a
broken $T$.

```{figure} ./media/generic_tangles/generic_tangle.svg
:label: fig-generic_tangle
@@@ TODO: Add content description
```

We can manipulate this tangle by the set of rotations, clockwise or
anti-clockwise. Each rotation in turn gives an arrangement of the interior data.
We can also manipulate the tangle by the set of flips, one around the core
x-axis and one around the y-axis. Each flip gives an arrangement of the interior
data. Pairing flips with rotations gives the table seen in @fig-tangle_flips.

```{figure} ./media/fig-tangle_flips.svg
:label: fig-tangle_flips
@@@ TODO: Add content description
```

When we apply this set of flips and rotations to the basic tangles seen in
@subsubsec-basic_tangles we two additional basic tangles seen in
@fig-basic_tangles_extra.

````{prf:observation}
:label: fig-basic_tangles_extra


```{figure} ./media/inf.svg
:label: prelim-fig-basic_nc-inf
:width: 500px
A tangle with no crossings, called the $\infty$ tangle.
```

```{figure} ./media/m1.svg
:label: prelim-fig-basic_c-m1
:width: 500px
A tangle with a single crossings, called the $m1$ tangle.
```
````

<!-- prettier-ignore-start -->
(subsubsec-conway_calc)=
##### Operations on Tangles
<!-- prettier-ignore-end -->

In addition to the rotations and flips, Conway introduced a calculus on tangles
[@conwayEnumerationKnotsLinks1970]. This calculus allowed Conway to build the
simple basic tangles into iteratively more complex tangles.

<!-- prettier-ignore-start -->
(subsubsec-conway_minus)=
##### Minus Tangle
<!-- prettier-ignore-end -->

For a generic tangle $T$, we call the tangle generated from a clockwise rotation
and flip around the y-axis the negative of $T$ notated $-T$. Equivalently, this
can be thought of as rotating the tangle around the $NW$ and $SE$ axis, as
indicated in @fig-opo-minus.

```{figure} ./media/fig-opo-minus.svg
:label: fig-opo-minus
@@@ TODO: Add content description
```

<!-- prettier-ignore-start -->
(subsubsec-opo-plus)=
##### Tangle Addition
<!-- prettier-ignore-end -->

For a pair of generic tangles, $A$ and $B$, we construct their sum $A+B$ by
first aligning $A$ and $B$ horizontally. We then connect in order the $NE$ and
$SE$ of $A$ to the $NW$ and $SW$ of $B$. This can be seen in @fig-opo-plus

```{figure} ./media/fig-opo-plus.svg
:label: fig-opo-plus
@@@ TODO: Add content description
```

The class of tangles built by successive addition of the $\pm 1$ basic tangles
are called the integral tangles.

##### Tangle Multiplication

For a pair of generic tangles, $A$ and $B$, we construct their product $A*B$, or
$A\ B$ by first aligning $A$ and $B$ horizontally. We then take $-A$ and connect
in order the $NE$ and $SE$ of $-A$ to the $NW$ and $SW$ of $B$. This
multiplication is equivalent to $-A+B$. This operation can be seen in
@fig-opo-times.

```{figure} ./media/fig-opo-times.svg
:label: fig-opo-times
@@@ TODO: Add content description
```

```{note}
Notice that $$A*0=-A+0=-A$$
```

##### Tangle Ramification

For a pair of generic tangles, $A$ and $B$, we construct their ramification
$A,B$ by first aligning $A$ and $B$ horizontally. We then take $-A$ and $-B$ and
connect in order the $NE$ and $SE$ of $-A$ to the $NW$ and $SW$ of $-B$. This
ramification is equivalent to $-A-B$ or $A0+B0$. This operation can be seen in
@fig-opo-ramification.

```{figure} ./media/fig-opo-ramification.svg
:label: fig-opo-ramification
@@@ TODO: Add content description
```

<!-- prettier-ignore-start -->
(subsubsec-opo-precedence)=
##### Indicating Precedence
<!-- prettier-ignore-end -->

With a set of operations comes the desire to chain multiple operations together.
The precedence for operations on tangles is indicated by parentheses in the
obvious way. An example can be seen in @fig-opo-prec.

```{figure} ./media/fig-opo-prec.svg
:label: fig-opo-prec
@@@ TODO: Add content description
```

<!-- prettier-ignore-start -->
(subsubsec-opo-flype)=
##### The Flype
<!-- prettier-ignore-end -->

When working in this calculus of tangles, a common situation you may find
yourself is one where the $1$ (or $\ \m 1$) tangle is added to a tangle $T$. In
this situation, we can move the $1$ crossing from one side of $T$ to the other
by a flype. To complete a flype we grab the top (north) and bottom (south) of
$T$ and rotate (according to the sign of the $\pm 1$) around the horizontal axis
of $
T$. An example of a flype is given in @fig-opo-flype.

```{figure} ./media/reidemeister_move/flype.svg
:label: fig-opo-flype
@@@ TODO: Add content description
```

##### Closures

For a generic tangle $T$, we have two options for how to close up the tangle.
The first is by connecting a strand from $NW$ to $NE$ and a strand from $SW$ to
$SE$, seen in @fig-closure-num, called the numerator closure. The second is the
denominator closure formed by connecting a strand from $NW$ to $SW$ and a strand
from $NE$ to $SE$, seen in @fig-closure-den.

````{prf:observation}
:label: fig-closure-prec

```{figure} ./media/fig-closure-num.svg
:label: fig-closure-num
@@@ TODO: Add content description
```

```{figure} ./media/fig-closure-den.svg
:label: fig-closure-den
@@@ TODO: Add content description
```

````

<!-- prettier-ignore-start -->
(subsubsec-opo-insert)=
##### Tangle insertions
<!-- prettier-ignore-end -->

With the calculus of tangles, Conway was able to enumerate a substantial number
of knots, but not all. We should notice a common theme with the calculus, every
operation forms a bigon in the knot shadow. Then systematically remove bigons in
the knot shadow, deleting edges and merging vertices, for a knot formed by only
these operations we obtain a four-valent graph with one vertex. The process of
bigon collapse can be seen in @fig-bigon_collapse. The class of knots who have a
presentation where bigons can be collapsed to a single vertex is called
**algebraic**.

```{figure} ./media/fig-bigon_collapse.svg
:label: fig-bigon_collapse
@@@ TODO: Add content description
```

To obtain a knot that has non-bigon connections between tangles, we will first
identify a four-valent graph that has non-bigon connections between vertices.
The class of graph that is most useful here are the polygons, the $6^{**}$ graph
or hexagon can be seen in @fig-6starstar.

```{figure} ./media/fig-6starstar.svg
:label: fig-6starstar
@@@ TODO: Add content description
```

The simplest thing we can do from here is consider the graph as a knot shadow
and for each vertex choose an over and under strand. While that method would
give us a knot, it is limiting. A less limiting option is the process of tangle
insertion. In this process we first generate a tangle with the calculus, we then
replace the vertex in the graph with that generated tangle, connecting the
$NW,\,NE,\,SW,\,\text{and }SE $ points to the four edges of the vertex. An example of a tangle insertion into $ 6^{**}$
can be seen in @fig-6starstar_insurtion.

```{figure} ./media/fig-6starstar_insurtion.svg
:label: fig-6starstar_insurtion
$6^*\ *.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1$
```

When noting the tangle insertion we list first the graph to be inserted into,
each graph has a canonical ordering of vertices for purposes of insertion. Next
we list the subtangles we wish to insert, each separated by a period.
