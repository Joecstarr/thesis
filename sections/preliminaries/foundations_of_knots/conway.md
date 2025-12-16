<!-- prettier-ignore-start -->
(sec-conway)=
#### Conway Notation
<!-- prettier-ignore-end -->

In @sec-history-of-tabulation, we saw that Conway claimed to have enumerated knots up to 11
crossings in "a few hours". Conway accomplished this by breaking knots into building blocks he
called tangles. This section gives an outline of the tools he developed and used to achieve those
"few hours" of amazing efficiency.

<!-- prettier-ignore-start -->
(subsubsec-deftangles)=
##### Definition of a Tangle
<!-- prettier-ignore-end -->

Our first step in unlocking Conway's tabulation secrets is the definition of a tangle. We will give
Conway's original definition followed by a description of what this looks like for a three
dimensional embedding for a knot.

```{prf:definition} Conway, Page 330 [@conwayEnumerationKnotsLinks1970]
We define a **tangle** as a portion of a knot diagram from which there emerge just 4
arcs pointing in the compass directions $NW, \ NE, \ SW, \ \text{and }SE$.
```

These boundaries that split knots at four points are called **Conway circles**, and we call the
points $NW,\ NE,\ SW,\ \text{and }SE$ **boundary points**. Formally, we can consider a Conway circle
to be a Jordan curve [^Jordancurve] meeting the knot diagram in exactly four points
[@bonahonNewGeometricSplittings2016]. In general, we prefer our Conway circles to actually be
circles in the colloquial sense. Luckily, the circle and Jordan curve constructions are equivalent.
This can be seen by a straightforward isotopy of one into the other, @fig-jordan_isotopy.

```{figure} ../../media/conway_circ_isotopy.svg
:label: fig-jordan_isotopy
An isotopy turning Jordan curves into circles.
```

We move our attention to the three dimensional analog for a Conway circle, the **Conway sphere**. A
Conway sphere, similar to the Conway circle, is an $S^2$ that encapsulates a portion of a knot so
that the knot intersects the sphere in exactly four points. Here we see the first example of our
preference for ambient space to be $S^3$ as opposed to $\R^3$. When a knot in $S^3$ is split by a
Conway sphere, the ambient $S^3$ is decomposed into two $B^3$, each with a portion of the knot.
Meaning, a single Conway sphere splits a knot into a pair of tangles.

<!-- prettier-ignore-start -->
(subsubsec-basic_tangles)=
##### Basic Tangles
<!-- prettier-ignore-end -->

Often, when thinking about a new construction, we focus on the simplest object that can be created
with the construction. In the case of drawing Conway circles to build tangles, the simplest tangles
are a tangle with no crossings (the 0 tangle @prelim-fig-basic_0) and a tangle with a single
crossing (the $+1$ tangle @prelim-fig-basic_1).

````{figure}
:label: fig-basic_tangles


```{figure} ../../media/0.svg
:label: prelim-fig-basic_0

A tangle with no crossings, called the 0 tangle.
```

```{figure} ../../media/1.svg
:label: prelim-fig-basic_1

A tangle with a single crossing, called the 1 tangle.
```
Two basic tangles.
````

<!-- prettier-ignore-start -->
(subsubsec-tangle_flips)=
##### Rotation and Mirroring of Tangles
<!-- prettier-ignore-end -->

Consider a **generic tangle**, as seen in @fig-generic_tangle, where orientation (the position of
the NW point) of data in the interior of the Conway circle is indicated by a broken $T$.

```{figure} ../../media/generic_tangles/generic_tangle.svg
:label: fig-generic_tangle
A generic tangle with a broken T.
```

We can manipulate this tangle by the set of rotations, clockwise or anti-clockwise. Each rotation in
turn gives a new arrangement of the interior data. We can also manipulate the tangle by the set of
flips, one around the core x-axis and one around the y-axis. Each flip gives an arrangement of the
interior data. Pairing flips with rotations gives the table seen in @fig-tangle_flips.

```{figure} ../../media/fig-tangle_flips.svg
:label: fig-tangle_flips
A table with all unique rotations and flips for a generic tangle.
From top to bottom in the first column:$\ \bullet$ No Flip$\ \bullet$
Flip around the north south axis.
From left to right in each row:$\ \bullet$ No rotation$\ \bullet$
rotation quarter turn clockwise$\ \bullet$ rotation half turn clockwise
$\ \bullet$ rotation three quarter turn clockwise$\ \bullet$ rotation
quarter turn clockwise
```

When we apply this set of flips and rotations to the basic tangles seen in @subsubsec-basic_tangles,
we obtain the two additional basic tangles seen in @fig-basic_tangles_extra.

````{figure}
:label: fig-basic_tangles_extra


```{figure} ../../media/inf.svg
:label: prelim-fig-basic_nc-inf

A tangle with no crossings, called the $\infty$ tangle.
```

```{figure} ../../media/m1.svg
:label: prelim-fig-basic_c-m1

A tangle with a single crossing, called the $ \m 1$ tangle.
```
Two additional basic tangles.
````

<!-- prettier-ignore-start -->
(subsubsec-conway_calc)=
##### Operations on Tangles
<!-- prettier-ignore-end -->

In addition to the rotations and flips, Conway introduced a calculus on tangles
[@conwayEnumerationKnotsLinks1970]. This calculus allowed Conway to build the simple basic tangles
into iteratively more complex tangles.

<!-- prettier-ignore-start -->
(subsubsec-conway_minus)=
##### Minus Tangle
<!-- prettier-ignore-end -->

For a generic tangle $T$, we call the tangle generated from a clockwise rotation and flip around the
y-axis the negative of $T$, notated $-T$. Equivalently, this can be thought of as rotating the
tangle around the $NW$ and $SE$ axis (@fig-opo-minus).

```{figure} ../../media/fig-opo-minus.svg
:label: fig-opo-minus
Rotating a tangle around the $NW$ $SE$ diagonal, yielding the negative of the
tangle.
```

```{note}
Observe that the minus of the $+1$ tangle (@prelim-fig-basic_1) is the $ \m 1$
tangle (@prelim-fig-basic_c-m1).
```

<!-- prettier-ignore-start -->
(subsubsec-opo-plus)=
##### Tangle Addition
<!-- prettier-ignore-end -->

For a pair of generic tangles, $A$ and $B$, we construct their sum $A+B$ by first aligning $A$ and
$B$ horizontally. We then connect the $NE$ and $SE$ of $A$ to the $NW$ and $SW$ of $B$, as seen in
@fig-opo-plus.

```{figure} ../../media/fig-opo-plus.svg
:label: fig-opo-plus
The sum of two generic tangles.
```

The class of tangles built by successive addition of the $\pm 1$ basic tangles are called the
**integral tangles**.

##### Tangle Multiplication

For a pair of generic tangles, $A$ and $B$, we construct their product, $A*B$ (or $A\ B$) by first
aligning $A$ and $B$ horizontally. We then take $-A$ and sum the two resulting tangles, equivalent
to $-A+B$, as seen in @fig-opo-times.

```{figure} ../../media/fig-opo-times.svg
:label: fig-opo-times
The product of two generic tangles
```

````{note}
Notice that
```{math}
A*0=-A+0=-A
```
````

##### Tangle Ramification

For a pair of generic tangles, $A$ and $B$, we construct their ramification $A,B$ by first aligning
$A$ and $B$ horizontally. We then take $-A$ and $-B$ and sum the resulting tangles. This makes
ramification equivalent to $-A-B$ or $A0+B0$, as seen in @fig-opo-ramification.

```{figure} ../../media/fig-opo-ramification.svg
:label: fig-opo-ramification
The ramification of two generic tangles.
```

<!-- prettier-ignore-start -->
(subsubsec-opo-precedence)=
##### Indicating Precedence
<!-- prettier-ignore-end -->

With a set of operations comes the desire to chain multiple operations together. The precedence for
operations on tangles is indicated by parentheses in the obvious way (@fig-opo-prec).

```{figure} ../../media/fig-opo-prec.svg
:label: fig-opo-prec
Multiple operations chained together with precedence indicated by parentheses.
```

<!-- prettier-ignore-start -->
(subsubsec-opo-flype)=
##### The Flype
<!-- prettier-ignore-end -->

When working in this calculus of tangles, a common situation you find yourself in is one where the
$1$ (or $\m 1$) tangle is added to a tangle. In this situation, we can move the $1$ crossing from
one side of $T$ to the other by a **flype**. To complete a flype, we grab the top (north) and bottom
(south) of the tangle and rotate (opposite the handedness of the crossing) as in @fig-opo-flype.

```{figure} ../../media/reidemeister_move/flype.svg
:label: fig-opo-flype
A $(+)$-flype on the top and a $(-)$-flype on the bottom. Note that the generic
tangle is flipped around the $x$-axis during the flype.
```

##### Closures

Since Conway's interest was in knots, he naturally needed ways to close up a tangle to form a knot.
In this section, we will introduce two ways that this can be accomplished. The first closure method
is the simple tangle closure, where points on a tangle are connected. The second closure method is
the insertion of multiple tangles into a graph.

###### Simple Tangle Closures

The first closure method is the simple tangle closure. For a generic tangle $T$, we have two options
for how to simply close up the tangle. One option is to connect a strand from $NW$ to $NE$ and a
strand from $SW$ to $SE$ (@fig-closure-num), called the numerator closure. The alternative is the
denominator closure, formed by connecting a strand from $NW$ to $SW$ and a strand from $NE$ to $SE$
(@fig-closure-den). In both cases, we introduce no additional crossings.

````{figure}
:label: fig-closure-prec

```{figure} ../../media/fig-closure-num.svg
:label: fig-closure-num
The numerator closure of a tangle.
```

```{figure} ../../media/fig-closure-den.svg
:label: fig-closure-den
The denominator closure of a tangle.
```
The two simple closures of a tangle.
````

<!-- prettier-ignore-start -->
(subsubsec-opo-insert)=
###### Tangle insertions
<!-- prettier-ignore-end -->

With the calculus of tangles and simple closures, Conway was able to enumerate a substantial number
of knots, but not all. We should notice a common theme with the calculus, when starting with basic
tangles every operation forms a bigon[^bigon]. We can collapse bigons in the knot shadow by deleting
edges and merging the two vertices of a bigon. For a knot formed by only the operations and simple
closures, if we iteratively collapse all bigons we obtain a four-valent planar graph [^fourval] with
one vertex, per @fig-bigon_collapse. The class of knots who have a presentation where bigons can be
collapsed to a single vertex with two self edges are called the **algebraic knots**.

```{figure} ../../media/fig-bigon_collapse.svg
:label: fig-bigon_collapse
The collapsing of the bigons in a knot
shadow from left to right: $\ \bullet$ A trefoil knot. $\ \bullet$ A
knot shadow for a trefoil knot with a
bigon highlighted. $\ \bullet$ The previously highlighted bigon
collapsed, and a new
bigon highlighted. $\ \bullet$ A graph with no bigons.

```

To obtain a knot that has non-bigon connections between inputs, we will first identify a four-valent
planar graph that has non-bigon connections between vertices. The class of graph that is most useful
here are the polygon graphs. For example, the $6^{**}$ graph (or octahedron) can be seen in
@fig-6starstar. Within the $6^{**}$ graph, we notice triangular regions between vertices.

```{figure} ../../media/fig-6starstar.svg
:label: fig-6starstar
A four valent planar graph with six vertices and triangular regions between
vertices. When the graph is placed on the surface of an $S^2$ we get the
octahedron.
```

The simplest thing we can do from here is consider the graph as a knot shadow, and for each vertex,
choose an over and under strand. While that method would give us a knot, it is limiting. Less
limiting is a process of tangle insertion. In this process we consider each vertex a boundary of a
Conway circle in which we can place a tangle generated with the Conway calculus. When we insert the
tangle into the Conway circle (vertex in the graph), the $NW,\,NE,\,SW,\,\text{and }SE$ points of
the tangle are connected to marked points of the Conway circle (the four edges of the vertex). An
example of a tangle insertion into $6^{**}$ can be seen in @fig-6starstar_insurtion.

```{figure} ../../media/fig-6starstar_insurtion.svg
:label: fig-6starstar_insurtion

Tangles inserted into the $6^{**}$
tangle, with Conway notation $$6^{**}\ast.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1.1\ 2\ 2\ 3\ 1$$
The $\ast$ labeled vertex defines the four boundary points of the
resulting tangle.
```

When each vertex has a tangle inserted, the result is a knot. When $n$ vertices are left empty, the
result is a tangle with $n$ boundary Conway circles. If $n$ is $1$, we have a tangle in the sense
we've been discussing. To reduce ambiguity, we mark in the graph with a $\ast$ in that empty vertex.
On each polygon graph, we select a canonical ordering of the vertices, per @fig-6starstar_ordered.
When notating the tangle insertions, we list the subtangles we wish to insert in graph canonical
order, each separated by a period and an empty vertex indicated with $\ast$. Following the
terminology outlined by Conolly [@connollyClassificationTabulation2string2021], we call these
singularly marked polygonal graphs **constellations**. We call the tangle diagrams generated by this
approach the **polygonal diagrams**. If a tangle has no algebraic representative we call it a
**polygonal tangle**.

```{figure} ../../media/fig-6starstar_orderd.svg
:label: fig-6starstar_ordered

The $6^{\ast\ast}$ graph with an order applied.
```

```{note}
Observe that insertion into the one vertex graph is equivalent to the simple
tangle closures.
```

[^Jordancurve]:
    A Jordan curve is a simple closed curve. This can be thought of as a curve drawn on a piece of
    paper that has: 1) No end points. 2) No self intersections.

[^bigon]:
    A bigon is a polygon with two sides. In the same way that an octagon has eight sides or a trigon
    (triangle) has three.

[^fourval]:
    A graph is said to be four valent if each vertex has four edge ends connected to it. In
    @fig-bigon_collapse, the result is four valent.
