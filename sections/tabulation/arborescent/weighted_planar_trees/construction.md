<!-- prettier-ignore-start -->

<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
(construction_of_arbor)=
#### Construction of Arborescent Knots from Weighted Planar Trees
<!-- prettier-ignore-end -->

This subsection begins with an introduction to Bonahon and Siebenmann's
[@bonahonNewGeometricSplittings2016] construction of arborescent knots and tangles in the smooth
setting. This is followed by the development of a combinatorial representation for arborescent knots
and tangles [@bonahonNewGeometricSplittings2016]. We deviate slightly from Bonahon and Siebenmann's
introduction but ultimately arrive at the same structure. In our introduction we develop partial
solutions, then progressively modify those partial solutions until they fit our needs. Next, we
describe Bonahon and Siebenmann's [@bonahonNewGeometricSplittings2016] operations on the
combinatorial structure, which allow us to systematically modify the structure, without changing the
topology. This subsection finishes with the classification of arborescent knots and tangles given by
Bonahon and Siebenmann [@bonahonNewGeometricSplittings2016] as well as our extension from a global
to local viewpoint.

##### Bands and Plumbing Squares

Our first step in describing a notation for the arborescent knots
[@bonahonNewGeometricSplittings2016] is describing a plumbing operation on bands. A band with a
plumbing square is a band $S^1\times\LB 0,1\RB$, along with an oriented square on the band such that
two of the sides of the square intersect the boundary of the band. Two examples of bands with
plumbing squares can be seen in @wpt-construc-fig-band_sum.

````{figure}
:label:wpt-construc-fig-band_sum

```{figure} ../../media/bands/bnd_sum_1.svg
:label: wpt-construc-fig-band_sum-1


A band with a plumbing square facing the viewer.
```

```{figure} ../../media/bands/bnd_sum_2.svg
:label: wpt-construc-fig-band_sum-2


A band with the plumping square facing away from the viewer. We are looking through the band.
```
Plumbing squares of bands.
````

##### Plumbing bands

We now glue the bands seen in @wpt-construc-fig-band_sum together with an operation called
**plumbing**. Consider the orientation given in the green band's plumbing square. We will call the
blue arrow $X$ and the thicker red arrow $Y$; similarly for the blue band with $X^\prime$ and
$Y^\prime$. We **plumb** the bands together along their plumbing squares, with the requirement that
the orientation labels are mapped $X\to Y^\prime$ and $Y\to X^\prime$. Finally, we forget the
boundaries of the plumbing squares, leaving only the joined boundaries of the bands. The result of
plumbing as well as a local picture for plumbing can be seen in @wpt-construc-fig-band_sum_opo.

````{figure}
:label:wpt-construc-fig-band_sum_opo

```{figure} ../../media/bands/bnd_sum_sum.svg
:label: wpt-construc-fig-band_sum_opo-1

Plumbed bands
```

```{figure} ../../media/bands/bnd_sum_patch.svg
:label: wpt-construc-fig-band_sum_opo-2

Plumbed bands
```
Two bands plumbed.
````

Our plumbing band construction can be turned into a knot, by adding a series of half-twists to our
plumbing bands (@wpt-construc-fig-6 and @wpt-construc-fig-25). When forming the half twists, we have
two options for direction relative to the band, we call one positive (left handed twists) and one
negative (right handed twists). We note that the twists appear in unique regions of the band,
determined by their position relative to the plumbing squares.

````{figure}
:label:wpt-construc-fig-111
```{figure} ../../media/bands/arbor_band_with_twist.svg
:label: wpt-construc-fig-6

Band with two negative half twists<br/> and three plumbing squares.
```

```{figure} ../../media/bands/arbor_band_with_twist_2.svg
:label: wpt-construc-fig-25

Band with three positive half twists and one plumbing square.
```
Plumbing bands with twists.
````

Successive plumbing yields collections of bands like those seen in @wpt-construc-fig-10. Finally,
turning @wpt-construc-fig-10 into a knot is as simple as removing the interior of the band, leaving
only the boundary, per @wpt-construc-fig-24.

````{figure}
:label:wpt-construc-fig-112
```{figure} ../../media/bands/arbor_bands.svg
:label: wpt-construc-fig-10

Bands plumbed
```

```{figure} ../../media/bands/arbor_bound.svg
:label: wpt-construc-fig-24

An arborescent knot
```
A set of plumbed bands in
    @wpt-construc-fig-10
  and arborescent knot in @wpt-construc-fig-24
````

It is important to note that, for creating arborescent knots, we must restrict plumbing from
creating "cycles" of bands. That is a chain of plumbing beginning and ending with the same band, as
seen in @wpt-construc-fig-cycle. If we allow cycles in the bands, we may create a polygonal tangle,
defined in @subsubsec-opo-insert. These polygonal tangles contain portions that do not satisfy
@intro-def-arbor-tangle, so are not arborescent presentations.

```{figure} ../../media/bands/band_cycle.svg
:label: wpt-construc-fig-cycle

A collection of bands plumbed in such a way that the last band is plumbed to
the first band in a cycle.
```

We now establish some language for describing the relative positions of bands. This language will be
reused when we transition to the combinatorial setting, and is widely used in graph theoretic
settings.

```{prf:definition}
:label: wpt-construc-def-relationships_of_bands
Given a band $B$ with plumbing squares, we call the set $C$ of bands
plumbed to $B$ the **children** of $B$. Additionally, for $c\in C$ we call $B$
the **parent** of $c$ and the collection of $C-\LS c \RS$ the
**siblings of $C$**.
```

We claim the plumbing band construction is in correspondence with the definition of arborescent seen
in @prelim-def-arborescent_knot. To see this, we take each plumbing band and encapsulate it in a
$S^2$ so that the corners of the plumbing squares lie on the $S^2$, giving us the vignette seen in
@fig-arborescent_band.

##### Weighted Planar Trees

The band construction we have developed for arborescent knots, as it stands, is completely unsuited
for machine computation. In this subsection, we lay out a line of reasoning leading to a
combinatorial encoding strategy [@bonahonNewGeometricSplittings2016] for the plumbing band
construction of arborescent knots and tangles. The line of reasoning starts by presenting the
required data of arborescent knots and tangles that any combinatorial representation must encode. We
then propose partial solutions, each progressively closer to the full encoding described by Bonahon
and Siebenmann [@bonahonNewGeometricSplittings2016]. As we will see, the encoding strategy
ultimately takes the form of a modified rooted plane tree, a specialized flavor of graph theoretic
tree.

Inventing a combinatorial encoding strategy means we first have to identify the essential
information that is needed to construct arborescent knots and tangles from band plumbings. The two
essential pieces of information that must be encoded by any combinatorial strategy for notating
plumbing of bands are the following:

1.  The parent child relationship between bands
2.  The twists on bands, and their positions relative to the band's children (plumbing squares)

Explicit details expanding on why these two pieces of information are essential can be found in
Bonahon and Siebenmann [@bonahonNewGeometricSplittings2016]. We will see in the following
subsections ways in which these data are essential, albeit in specialized cases.

Consider the first piece of essential information our combinatorial strategy must encode, the parent
child relationships between bands. Perhaps the most commonly computationally utilized structure that
encodes relational data is an abstract graph. We imagine how an abstract graph might be used for
encoding the relationship of bands. One solution is to map bands to vertices and plumbing
relationships to edges. In the discussion of the band construction, we restricted plumbing from
forming cycles (@wpt-construc-fig-cycle). A result of this restriction is that any abstract graph
must also have no cycles, meaning all the graphs we will work with, abstract or otherwise, are
actually trees. We will call the data of a vertex and a collection of **bonds** (half-edges)
associated with plumbing squares the **local picture around a vertex**.

We have partially completed our goal of encoding the essential information of band plumbing in a
combinatorial object. Unfortunately, an abstract tree doesn't encode all the essential data.
Particularly, our second piece of information, the positions of children and weights, is not easily
seen in an abstract tree. To solve this problem, we will instead use a modified version of an
abstract tree, a **rooted plane tree**, for our encoding.

```{prf:definition}
:label: wpt-construc-def-rooted_plane_tree

A **rooted plane tree** is an abstract tree imbued with a strict total order,
indexed by the non-negative integers, on the vertices. We call the least
vertex the **root** of the tree.
```

In a rooted plane tree $\Gamma$, at each vertex $v$, the children of $v$ have an ordering inherited
from the total order of $\Gamma$, we call this ordering of the children the **cyclic order** of the
children. The cyclic order gives us two natural ways to draw $v$ and its children in the plane. We
may choose to draw the children anti-clockwise in one of increasing or decreasing order of index.
The realization of these two options can be seen in @wpt-construc-fig-order_tree. A universal choice
of increasing or decreasing yields a unique realization of a rooted plane tree in the plane.

````{figure}
:label:wpt-construc-fig-order_tree

```{figure} ../../media/bands/arbor_graph_split_local_inc.svg
:label: wpt-construc-fig-order_1

The local picture of a vertex with child labels increasing in anti-clockwise order.
```

```{figure} ../../media/bands/arbor_graph_split_local_dec.svg
:label: wpt-construc-fig-order_2

The local picture of a vertex with child labels decreasing in anti-clockwise order.
```
$\,$

````

<!-- prettier-ignore-start -->
(indexing-rpt)=
###### Indexing the total order of a tree
<!-- prettier-ignore-end -->

We will now describe an **ideal indexing** for a rooted plane tree.

```{prf:definition}
Let $\Gamma$ be a rooted plane tree $r$, be the root of $\Gamma$. Additionally,
let $v_i\neq r$ be a vertex with parent $v_p$ and children
$v_{c_1},\,\cdots,\,v_{c_n}$. We call the indexing of a rooted plane **ideal** if
it satisfies the following:

-   $r$ is index $0$
-   $p<i<c_1<\cdots< c_n$
```

```{note}
Two commonly seen orderings of a tree are the breadth and depth
  first orderings, both orderings
  are ideal orderings. For our purposes we will prefer the depth first ordering.
```

````{figure}
:label:wpt-construc-fig-order

```{figure} ../../media/bands/rpt_order.svg
:label: wpt-construc-fig-rptorder_1

A rooted plane tree with ideal indexing. The index of each vertex is seen inside the vertex.
```

```{figure} ../../media/bands/rpt_order_ni.svg
:label: wpt-construc-fig-rptorder_2

A rooted plane tree with indexing that is not ideal. The index of is each vertex seen inside the vertex.
```
Indexing strategies of a rooted plane tree.
````

```{convention}
For the remainder of this thesis we will adopt some conventions for
  rooted plane
  trees (and their derivatives the weighted planar tangle trees, CWPTT, and
  RLITT). When realizing a tree in the plane we select the universal
  anti-clockwise increasing
  order and assume that the tree has depth first indexing.

```

The final data we need to record is the position and count of half twists relative to plumbing
squares. We observed earlier that the half twists on a band must lie in a unique region determined
by position relative to plumbing squares on a band. This relationship can be recreated for a rooted
plane tree by annotating the local view of a vertex with an integer placed in the regions between
bonds. The relationship between a plumbing band and a weighted vertex in a rooted plane tree can be
seen in @wpt-construc-fig-7. The weights placed in regions between bonds inherit a cyclic order from
the cyclic order of the bonds. Each weight falls in the region between two bonds. We assign to each
weight (including zero weights) the lower of the two indices. This aligns with assigning to the
weight the index that appears before it in the anti-clockwise planar realization of the cyclic
order, per @wpt-construc-fig-weights-with-index.

````{figure}
:label:wpt-construc-fig-order_weights

```{figure} ../../media/bands/arbor_graph_split_local_with_band.svg
:label: wpt-construc-fig-7

The local view of a vertex with the weights two, zero, and zero.
```

```{figure} ../../media/bands/arbor_graph_split_local_1.svg
:label: wpt-construc-fig-weights-with-index

The local view of a vertex with weight. Notice the index of the weights come
from the bond "before" it in the planar realized cyclic order.
```
Local view of a vertex with weights.
````

We can see a full example of a tree with its associated plumbed construction in
@wpt-construc-fig-27. We call this fully realized combinatorial recipe for an arborescent knot a
**weighted planar tree**.

```{prf:definition} Bonahon and Siebenmann, Page 143[@bonahonNewGeometricSplittings2016]
A rooted plane tree $\Gamma$ augmented with weights is called a
**weighted planar tree**.
```

````{figure}
:label: wpt-construc-fig-114
```{figure} ../../media/bands/arbor_graph.svg
:label: wpt-construc-fig-27

The tree describing the plumbing of bands. Each vertex represents the band illustrated near it.
```

```{figure} ../../media/bands/arbor_bands.svg
:label: wpt-construc-fig-28

The realization by plumbing bands of the tree in @wpt-construc-fig-27
```
Realization of plumbing of a tree.

````

<!-- prettier-ignore-start -->
(wpt-construc-sec-wptt)=
##### Weighted Planar Tangle Trees
<!-- prettier-ignore-end -->

Our construction to this point has been concerned with the notation for knots and links. We now give
a modification of this notation for tangles. A weighted planar tree, as in @wpt-construc-fig-29, can
be modified to represent a tangle by allowing a **free bond** (half-edge), to be attached to a
vertex, that is, to allow bands to have a non-plumbed plumbing square. We realize the non-plumbed
square, as a Conway circle for a two string tangle as in @wpt-construc-fig-tangle_trad. To
consistently orient the Conway sphere's interior, we align the north boundary points of the Conway
sphere with the top (up in the band orientation) boundary component, and place the NW corner first
(following the orientation of the boundary), per @wpt-construc-fig-band_orientation. Plumbing two
bands then corresponds to the action of gluing a pair of tangles together on their Conway spheres so
that boundary points align.

```{figure} ../../media/bands/bnd_with_orientation.svg
:label: wpt-construc-fig-band_orientation

The orientation of a
Conway sphere given by a plumbing square on a band of an
arborescent tangle. The orientation of the underlying plumbing
square is shown.
This aligns with a left hand rule with $Y$ the thumb, $X$ the
index finger, and
$Z$ middle finger, with $Z$ pointing away from the center of the band,
out of the page in this case.
```

A tree may have many free bonds, with each free bond representing a unique boundary Conway sphere.
Each boundary component serves as a location where a tangle can be inserted to form a knot or link.
For our efforts in enumerating two string tangles, we restrict our focus to trees that have a single
free bond. In tangle trees with a single free bond, we designate the vertex with the free bond as
the root of the tree.

````{figure}
:label:  wpt-construc-fig-115


```{figure} ../../media/bands/arbor_tangle.svg
:label: wpt-construc-fig-29

The plumbing realization of an arborescent tangle.
```

```{figure} ../../media/bands/example_tangle.svg
:label: wpt-construc-fig-tangle_trad


With an isotopy of the tangle and inversion of the Conway circle given by the
non-plumbed square we have the realization of @wpt-construc-fig-29 as a
traditional orthogonally projected tangle.
```
Plumbing bands as a tangle.
````

We will see that keeping track of the location of the fixed points of the boundary sphere is
important when determining tangle equivalence. This is due to the need to maintain the rational
number (@rational-def-frac) associated with the "rational tangle" subtangles of a tree, prompting us
to assign rotation information to the free bonds. This information takes the form of labels from the
members of $V_4$ of the Klein four-group $\iota,\xi,\zeta,\eta$. Each of these labels corresponds to
a rotation of the Conway sphere around an axis in $\R^3$, as seen in @wpt-construc-fig-v_4rotations
and @wpt-construc-fig-k4g. Full details for the manifold theory underpinning these markings are
found in Bonahon and Siebenmann [@bonahonNewGeometricSplittings2016]. We call such a labeled tree a
**weighted planar tangle tree**.

````{figure}
:label: wpt-construc-fig-v_4rotations

```{figure} ../../media/v4_rotations_i.svg
:label: wpt-construc-fig-k4g-rotationsi

The identity rotation (no rotation)
```

```{figure} ../../media/v4_rotations.svg
:label: wpt-construc-fig-k4g-rotations

The effect of the $V_4$ rotations on each of the
```
The identity rotation (no rotation), and the effect of the $V_4$ rotations on each of the
````

```{prf:definition}Bonahon and Siebenmann Page 165 [@bonahonNewGeometricSplittings2016]
A weighted planar tree $\Gamma$ with free bonds labeled in $V_4$ is called a
** weighted planar tangle tree (WPTT)**.
```

````{figure}
:label: wpt-construc-fig-k4g

```{figure} ../../media/iota.svg
:label: wpt-construc-fig-k4g-i

$\iota$ for no rotation
```
```{figure} ../../media/zeta.svg
:label: wpt-construc-fig-k4g-x

$\xi$ rotates around the $X$-axis
```

```{figure} ../../media/eta.svg
:label: wpt-construc-fig-k4g-y

$\eta$ rotates around the $Y$-axis
```

```{figure} ../../media/xi.svg
:label: wpt-construc-fig-k4g-z

$\zeta$ rotates around the $Z$-axis
```
Roations of a tangle.

````

<!-- prettier-ignore-start -->
(wpt-construc-sec-subtrees)=
#### Anatomy of a tree
<!-- prettier-ignore-end -->

In this subsection, we will describe several portions of weighted planar trees: the ring subtree,
essential vertex, and the sticks of a tree.

<!-- prettier-ignore-start -->
(wpt-construc-sec-rings)=
##### Ring subtree
<!-- prettier-ignore-end -->

We will now describe the ring subtrees of a weighted planar tree, which locally appear as
@wpt-construc-fig-17.

```{figure} ../../media/bands/arbor_graph_ring.svg
:label: wpt-construc-fig-17


Positive and negative ring subtrees
```

Now, resolving the plumbing for the positive subtree, we arrive at bands as in @wpt-construc-fig-12.

```{figure} ../../media/bands/arbor_ring.svg
:label: wpt-construc-fig-12

Plumbed ring bands
```

Notice that the boundary of these plumbed bands has three components, as seen in
@wpt-construc-fig-13.

```{figure} ../../media/bands/arbor_ring_no_bnd.svg
:label: wpt-construc-fig-13

Ring boundary
```

With an isotopy of the tangle and inversion of the Conway circle given by the non-plumbed square, we
can arrange our plumbed bands into the standard tangle projection seen in @wpt-construc-fig-14. This
tangle projection tells us that the subtree in @wpt-construc-fig-12 is, depending on location of
$\text{NW}$, either the zero or infinity tangle with a ring.

```{figure} ../../media/bands/arbor_ring_tangle.svg
:label: wpt-construc-fig-14

Ring Tangle
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-essential_verts)=
##### Essential Vertex
<!-- prettier-ignore-end -->

We now classify each vertex into one of two classes, the essential vertices and the non-essential
vertices.

```{prf:definition} Bonahon and Siebenmann, Page 159[@bonahonNewGeometricSplittings2016]
:label: apn-def-2
We define an **essential vertex** as any vertex with valence (count of the number of bonds) greater than $3$.
```

```{prf:definition} Bonahon and Siebenmann, Page 159[@bonahonNewGeometricSplittings2016]
:label: apn-def-3

A vertex is called non-essential if it has valence (count of the
number of bonds) $0,1,2$.
```

As an example, consider the vertices seen in @wpt-construc-fig-18.

```{figure} ../../media/bands/arbor_ring_essential.svg
:label: wpt-construc-fig-18

A weighted planar tree annotated with essential vertices in orange and
non-essential in blue
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-sticks)=
##### Sticks of a Tree
<!-- prettier-ignore-end -->

The final part of the anatomy of a tree we will consider is the **sticks** of a tree.

```{prf:definition} Bonahon and Siebenmann, Page 159[@bonahonNewGeometricSplittings2016]
:label: wpt-construc-def-sticks_of_a_tree
Let $\Gamma$ be a weighted planar tree and $\LS b_i\RS$ be the set of essential
vertices of $\Gamma$ including their bonds (half-edges). We call the
$\Gamma_s=\Gamma\setminus \LS b_i\RS$ the **sticks** of $\Gamma$ and every
connected component of $\Gamma_s$ a **stick**.
```

As an example, consider the tree seen in @wpt-construc-fig-18, the sticks of which can be seen in
@wpt-construc-fig-19.

```{figure} ../../media/bands/arbor_ring_noessential.svg
:label: wpt-construc-fig-19

Sticks of the tree from @wpt-construc-fig-18, six half-open sticks and one open
stick.
```

By construction, a stick subtree of $\Gamma$ may have 0, 1, or 2 free bonds (seen in
@wpt-construc-fig-sticks). We call a stick with 0 free bonds closed, 1 free bond half-open, and 2
free bonds open. Additionally, we call a stick where each vertex has a single weight a **proper
stick**, and we call a vertex on the end of a stick an **end vertex**.

```{figure} ../../media/bands/sticks_open.svg
:label: wpt-construc-fig-sticks

From top to bottom, a closed, half-open, and an open stick. Each end vertex
is colored in red.
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-integral)=
###### Integral Tangles
<!-- prettier-ignore-end -->

When a weighted planar tangle tree is a half-open stick containing a single vertex with a single
weight $w_0$ we call it an **integral tangle tree**.

```{figure} ../../media/watt_integral.svg
:label: wpt-construc-fig-integral
A stick realized as a integral tangle.
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-rational)=
###### Rational Tangles
<!-- prettier-ignore-end -->

Bonahon and Siebenmann [@bonahonNewGeometricSplittings2016] give a correspondence between stick
tangle trees (stick with a single free bond) and Conway's rational tangles
[@conwayEnumerationKnotsLinks1970]. An example of the correspondence can be seen in
@wpt-construc-fig-rat.

```{figure} ../../media/watt_rational.svg
:label: wpt-construc-fig-rat
A stick tangle tree realized as a rational tangle.
```

<!-- prettier-ignore-start -->
(wpt-construc-sec-TCN)=
###### Tree Crossing Number
<!-- prettier-ignore-end -->

Finally, we define the **Tree Crossing Number (TCN)** of a weighted planar tangle tree. This
corresponds to the crossing number of the tangle diagram given by the weighted planar tangle tree.

````{prf:definition}
:label: apn-def-TCN

For weighted planar tangle tree $\Gamma$, with weights $\LS w_i\RS$. We call
```{math}
:enumerated: false
\text{TCN}=\sum |w_i|
```
the **Tree Crossing Number (TCN)**.
````
