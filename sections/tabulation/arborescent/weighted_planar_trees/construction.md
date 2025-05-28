<!-- prettier-ignore-start -->

<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
(construction_of_arbor)=
#### Construction of Arborescent Knots from Weighted Planar Trees
<!-- prettier-ignore-end -->

This section begins with an introduction to a construction of arborescent knots
and tangles in the smooth setting. This is followed by the development of a
combinatorial representation for arborescent knots and tangles. We will
introduce partial solutions and progressively modify them until they fit the
needs of arborescent knots and tangles. We then describe a collection of
operations on the combinatorial structure that lets us systematically modify the
structure. The section finishes with an overview of the classification of
arborescent knots and tangles given by Bonahon and Seibenmann
[@bonahonNewGeometricSplittings2016].

##### Bands and Plumbing Squares

Our first step in describing a notation for the arborescent knots
[@bonahonNewGeometricSplittings2016] is describing a plumbing operation on
bands. A band with a plumbing square is a band $S^1\times\LB 0,1\RB$, along with
an oriented square on the band such that two of the sides of the square
intersect the boundary of the band. Two examples of bands with plumbing squares
can be seen in {prf:ref}`wpt-construc-fig-band_sum`.

````{prf:observation}
:label:wpt-construc-fig-band_sum

```{figure} ./media/bands/bnd_sum_1.svg
:label: wpt-construc-fig-band_sum-1
:width: 500px

@@@ TODO
```

```{figure} ./media/bands/bnd_sum_2.svg
:label: wpt-construc-fig-band_sum-2
:width: 500px

@@@ TODO
```

````

##### Plumbing bands

We now glue the bands seen {prf:ref}`wpt-construc-fig-band_sum` together with an
operation called plumbing. Consider the orientation given in the green band's
plumbing square. We will call the red arrow $x$ and the orange arrow $y$,
similarly for the blue band $x^\prime$ and $y^\prime$.

We plumb the bands together along their plumbing squares, with the requirement
that the orientation labels are mapped $x\to y^\prime$ and $y\to x^\prime$.
Finally, we forget the boundaries of the plumbing squares, leaving only the
joined boundaries of the bands. The result of plumbing as well as a local
picture for plumbing can be seen in {prf:ref}`wpt-construc-fig-band_sum_opo`.

````{prf:observation}
:label:wpt-construc-fig-band_sum_opo

```{figure} ./media/bands/bnd_sum_sum.svg
:label: wpt-construc-fig-band_sum_opo-1
:width: 500px
Plumbed bands
```

```{figure} ./media/bands/bnd_sum_patch.svg
:label: wpt-construc-fig-band_sum_opo-2
:width: 500px
Plumbed bands
```
````

To turn our band construction into a knot, before plumbing we add a series of
half-twists into our bands with plumbing squares, seen in
{prf:ref}`wpt-construc-fig-6` and {prf:ref}`wpt-construc-fig-25`. When forming
the half twists, we have two options for direction relative to the band, we call
one positive and one negative. A positive twist, on a band drawn with boundary
parallel to the x-axis, results in the "closer" boundary component having a
positive slope, negative is defined likewise. We note that the twists appear in
unique regions of the band, determined by their position relative to the
plumbing squares.

````{prf:observation}
```{figure} ./media/bands/arbor_band_with_twist.svg
:label: wpt-construc-fig-6
:width: 500px
Band with two negative half twists<br/> and three plumbing squares.
```

```{figure} ./media/bands/arbor_band_with_twist_2.svg
:label: wpt-construc-fig-25
:width: 500px

Band with three positive half twists <br/>and one plumbing square.
```

<!--   -->````

Combining these half twisted bands together with plumbing yields objects similar
to those seen in {prf:ref}`wpt-construc-fig-10`. Finally, turning
{prf:ref}`wpt-construc-fig-10` into a knot is as simple as forgetting the two
cell leaving only the boundary, seen in {prf:ref}`wpt-construc-fig-24`.

````{prf:observation}
```{figure}./media/bands/arbor_bands.svg
:label: wpt-construc-fig-10
:width: 500px
Bands plumbed
```

```{figure} ./media/bands/arbor_bound.svg
:label: wpt-construc-fig-24
:width: 500px
An arborescent knot
```

````

It is important to note that we must restrict plumbing from creating "cycles" in
the bands. That is a chain of plumbing beginning and ending with the same band,
as seen in {prf:ref}`wpt-construc-fig-cycle`.

```{figure} ./media/bands/band_cycle.svg
:label: wpt-construc-fig-cycle
:width: 500px
An collection of bands plumbed in such a way that the last band is plumbed to
the first band forming a cycle.
```

We now establish some language for describing the relative positions of bands.
This language will be reused when we transition to the combinatorial setting,
and is widely used in graph theoretic settings.

```{prf:definition} Relationships of Bands
:label: wpt-construc-def-relationships_of_bands
Given a band $B$ with plumbing squares, we call the set $C$ of bands
plumbed to $B$ the **children** of $B$. Additionally, for $c\in C$ we call $B$
the **parent** of $c$ and the collection of $C-\LS c \RS$ the
**siblings of $C$**.
```

We claim the plumbing band construction is in correspondence with the definition
of arborescent seen in {prf:ref}`prelim-def-arborescent_knot`. To see this, we
take each plumbing band and encapsulate it in an $S^2$ so that the corners of
the plumbing squares lay on the $S^2$. Then taking an orthogonal projection
gives us a vignette seen in {prf:ref}`fig-arborescent_part`.

##### Weighted Planar Trees

The band construction we have seen for arborescent knots, as it stands, is
completely unsuited for machine computation. In this section, we lay out a line
of reasoning leading to a combinatorial encoding strategy for arborescent knots
and tangles. The line of reasoning starts by presenting the required data about
arborescent knots and tangle that any combinatorial representation must encode.
We will then propose partial solutions, each progressively closer to a full
encoding. As we will see, the encoding strategy ultimately takes the form of a
modified rooted plane tree, a specialized flavor of graph theoretic tree.

Inventing a combinatorial encoding strategy means we first have to identify the
essential information that is needed to construct band plumbings. The two
essential pieces of information that must be encoded by any combinatorial
strategy for notating plumbing of bands are the following.

1.  The parent child relationship of bands
2.  The relative positions of children (plumbing squares) and twists on a band

Explicit details expanding on why these two pieces of information are essential
can be found in Bonahon and Seibenmann [@bonahonNewGeometricSplittings2016]. We
will see in future sections some ways in which these data are essential, albeit
in specialized cases.

The first of these pieces of essential data we will work on is the parent child
relationships of bands. Perhaps the most commonly computationally utilized
structure that encodes relational data is an abstract graph. We imagine how an
abstract graph might be used for encoding the relationship of bands. One
solution is to map bands to vertices and plumbing relationships to edges. In the
discussion of the band construction, we restricted plumbing from forming cycles
({prf:ref}`wpt-construc-fig-cycle`). A result of this restriction is that any
abstract graph must also have no cycles, meaning all the graphs we will work
with, abstract or otherwise, are actually trees. We will call the data of a
vertex and a collection of **bonds** (half-edges) associated to plumbing squares
the **local picture around a vertex**.

We have partially completed our goal of encoding the essential information of
band plumbing in a combinatorial object. Unfortunately, an abstract tree doesn't
encode all the essential data we require. Particularly, our second piece of
information, the positions of children and weights, is not easily seen in an
abstract tree. To solve this problem, we will instead use a modified version of
an abstract tree, a **rooted plane tree** for our encoding.

```{prf:definition} Rooted Plane Tree
:label: wpt-construc-def-rooted_plane_tree

A **rooted plane tree** is an abstract tree imbued with a strict total order,
indexed by the integers, on the vertices. We call the least vertex the **root**
of the tree.
```

Observe that in a rooted plane tree for each vertex $v$, the children of $v$
have an order inherited from the total order, we call this order the **cyclic
order** of the children. The cyclic order gives us two natural ways to draw in
the plane the local picture for $v$. We may choose to list the children
anticlockwise in either increasing or decreasing order, based on the index of
the child vertex. The realization of these two options can be seen in
{prf:ref}`wpt-construc-fig-order`. A universal choice of increasing or
decreasing yields a unique realization of a rooted plane tree into the plane. We
will shortly see that for our full combinatorial encoding, the increasing and
decreasing embeddings are topologically equivalent.

````{prf:observation}
:label:wpt-construc-fig-order

```{figure}./media/bands/arbor_graph_split_local_inc.svg
:label: wpt-construc-fig-order_1
:width: 500px
The local picture of a vertex with child labels increasing.
```

```{figure}./media/bands/arbor_graph_split_local_dec.svg
:label: wpt-construc-fig-order_2
:width: 500px
The local picture of a vertex with child labels decreasing.
```

````

The final data we need to record is the position and count of half twists
relative to plumbing squares. We observed earlier that the half twists on a band
must lie in a unique region determined by position relative to plumbing squares
on a band. This relationship can be recreated for a rooted plane tree by
annotating the local view of a vertex with an integer placed in the spaces
between bonds. The relationship between a plumbing band and a weighted vertex in
a rooted plane tree can be seen in {prf:ref}`wpt-construc-fig-7`.

```{figure} ./media/bands/arbor_graph_split_local_with_band.svg
:label: wpt-construc-fig-7
:width: 500px
The local view of a vertex with weight
```

We can see a full example of a tree with its associated plumbed construction in
{prf:ref}`wpt-construc-fig-27`. We call this fully realized combinatorial recipe
a **weighted planar tree**.

````{prf:observation}
```{figure} ./media/bands/arbor_graph.svg
:label: wpt-construc-fig-27
:width: 500px
@@@ TODO
```

```{figure} ./media/bands/arbor_bands.svg
:label: wpt-construc-fig-28
:width: 500px
@@@ TODO
```

````

<!-- prettier-ignore-start -->
(wpt-construc-sec-wptt)=
##### Weighted Planar Tangle Trees
<!-- prettier-ignore-end -->

Our construction to this point has been concerned with the notation for knots,
we now give a modification of this notation for tangles. A tree, as in
{prf:ref}`wpt-construc-fig-9`, can be modified to represent a tangle by allowing
a **"free" bond** to be attached to a vertex, that is, to allow bands to have a
non-plumbed plumbing square. We can realize the non-plumbed square, as a Conway
circle for a two string tangle.

````{prf:observation}
```{figure} ./media/bands/arbor_tangle.svg
:label: wpt-construc-fig-29
:width: 500px
@@@ TODO
```

```{figure} ./media/bands/example_tangle.svg
:label: wpt-construc-fig-tangle_trad
:width: 500px
@@@ TODO
```

````

In the next section, we will introduce a collection of moves on weighted planar
tangle trees. These moves can be realized as moves on plumbed bands. We will see
that keeping track of the orientation of the boundary sphere is important when
determining tangle equivalence. This prompts us to assign rotation information
to the free bonds. This information takes the form of labels from the members of
$V_4$ of the Klein four-group $\iota,\xi,\zeta,\eta$. Each of these labels
corresponds to a rotation of the Conway sphere around an axis in $\R^3$, as seen
in {prf:ref}`wpt-construc-fig-k4g`. A tree may have many free bonds, with each
free bond representing a unique boundary Conway sphere. For our efforts in
enumerating two string tangles, we restrict our focus to trees that have a
single free bond. In tangle trees with a single free bond, we designate the
vertex with the free bond as the root of the weighted planar tangle tree.

````{prf:observation}
:label: wpt-construc-fig-k4g

```{figure} ./media/iota.svg
:label: wpt-construc-fig-k4g-i
:width: 500px
$\iota$ for no rotation
```

```{figure} ./media/zeta.svg
:label: wpt-construc-fig-k4g-x
:width: 500px
$\zeta$ rotates around the $x$-axis
```

```{figure} ./media/eta.svg
:label: wpt-construc-fig-k4g-y
:width: 500px
$\eta$ rotates around the $y$-axis
```

```{figure} ./media/xi.svg
:label: wpt-construc-fig-k4g-z
:width: 500px
$\xi$ rotates around the $z$-axis
```

````

##### Anatomy of a tree

In this section, we will describe several special subtrees of weighted planar
trees.

<!-- prettier-ignore-start -->
(wpt-construc-sec-rings)=
###### Rings
<!-- prettier-ignore-end -->

We will now describe special subtrees of a weighted planar tree, locally
appearing as {prf:ref}`wpt-construc-fig-17`.

```{figure} ./media/bands/arbor_graph_ring.svg
:label: wpt-construc-fig-17
:width: 500px

Positive and negative ring subtree
```

Now, resolving the plumbing for the positive subtree, we arrive at bands as in
{prf:ref}`wpt-construc-fig-12`.

```{figure} ./media/bands/arbor_ring.svg
:label: wpt-construc-fig-12
:width: 500px
Plumbed ring bands
```

Notice that the boundary of these plumbed bands has three components, as seen in
{prf:ref}`wpt-construc-fig-13`.

```{figure}./media/bands/arbor_ring_no_bnd.svg
:label: wpt-construc-fig-13
:width: 500px
Ring boundary
```

With an obvious flype and inversion of the Conway circle given by the
non-plumbed square, we can arrange our plumbed bands into the standard tangle
projection seen in {prf:ref}`wpt-construc-fig-14`. This tangle projection tells
us that the subtree in {prf:ref}`wpt-construc-fig-12` is either the zero or
infinity tangle with a ring.

```{figure}./media/bands/arbor_ring_tangle.svg
:label: wpt-construc-fig-14
:width: 500px
Ring Tangle
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-essential_verts)=
###### Essential vertices
<!-- prettier-ignore-end -->

Shifting away from special subtrees for a moment, we again consider a local
picture of a vertex. During computation on weighted planar trees we can
partition vertices into two classes, essential vertices and non-essential
vertices.

```{prf:definition} Essential vertex
:label: apn-def-2
We define an **essential vertex** as any vertex with valence
greater than $3$ or ring number greater than $1$.
```

```{prf:definition} Non-essential vertex
:label: apn-def-3

A vertex is called non-essential if it has valence $0,1,2$ and no rings.
```

We see in {prf:ref}`wpt-construc-fig-18` essential vertices in orange and
non-essential in red.

```{figure} ./media/bands/arbor_ring_essential.svg
:label: wpt-construc-fig-18
:width: 500px
Abbreviated
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-sticks)=
###### Sticks
<!-- prettier-ignore-end -->

The final important class in the anatomy of a tree is the sticks of a tree.

```{prf:definition} Sticks of a weighted planar tree
:label: wpt-construc-def-sticks_of_a_tree
Let $\Gamma$ be a weighted planar tree and $\LS e_i\RS$ be the set of essential
vertices of $\Gamma$ including their bonds (half-edges). We call the collection subtrees
$\Gamma_s=\Gamma\setminus \LS e_i\RS$ the **sticks** of $\Gamma$ and every
connected component of $\Gamma_s$ a **stick**.
```

As an example, consider the tree seen in {prf:ref}`wpt-construc-fig-18`, the
sticks of which can be seen in {prf:ref}`wpt-construc-fig-19`.

```{figure} ./media/bands/arbor_ring_noessential.svg
:label: wpt-construc-fig-19
:width: 500px
Sticks of a tree
```

By construction, a stick subtree of $\Gamma$ may have 0,1, or 2 free bonds, we
call a stick with; 0 free bonds closed, 1 free bond half-open, and 2 free bonds
open. We call a stick where each vertex has a single weight a **proper stick**.
Bonahon and Seibenmann [@bonahonNewGeometricSplittings2016] give a
correspondence between stick subtrees and Conway's rational tangles
[@conwayEnumerationKnotsLinks1970]. An example of the corresponcance can be seen
in {prf:ref}`wpt-construc-fig-rat`.

```{figure} ./media/watt_rational.svg
:label: wpt-construc-fig-rat
:width: 500px
A stick realized as a rational tangle.
```
