<!-- prettier-ignore-start -->
(sec-arborescent-linear)=
#### An Encoding Strategy for Arborescent Knots and Tangles
<!-- prettier-ignore-end -->

The various flavors of weighted planar trees we have seen thus far are a useful
tool for manipulation of arborescent tangles by human or machine. Unfortunately,
where storage is concerned, the tree structure is quite difficult to store
directly in a computer database. We will rectify this by introducing a
linearization strategy for weighted planar trees.

The strategy outlined here is designed for linearizing tangles. A small
modification must be made for use with knots. That being, in the knot case,
ignore the $n^{\text{th}}$ weight position for the root. We will descend the
tree in a depth-first order. Annotating the linearization with two sets of
delimiters that indicate the change in depth in the tree. Each delimiter also
communicates some extra information about the subtree it is delimiting. The two
sets of delimiters are as follows:

-   $\LB\ \RB$: Corresponds to a half open stick and is interpreted as a twist
    vector for a rational tangle. Note that, to align with the traditional
    notation, the twist vector is written in depth first post order.
-   $\LP\ \RP$: Corresponds to a vertex not on a half open stick.

We will now walk through an example of the linearization algorithm. Let $\Gamma$
be a weighted planar tangle tree seen in @wpt-rli-fig-23. We assume
that all sticks of $\Gamma$ be proper stick. As we walk the tree, the vertex
currently being linearized will be called the **object vertex**. Beginning with
the root as an object vertex, we descend the tree in a depth-first order.

##### Tangle Linearization Example

We begin by adding the $V_4$ label for our tangle to the linearization. Now with
the root as the object vertex, we add $\LP\ \right.$ to our linearization. When we
encounter a child bond, we descend to the child. When we descend, we have two
cases to consider, the child is essential or non-essential.

##### Case 1: The Child is Essential

If the child is essential, we restart the algorithm from the beginning with the
essential vertex as the object vertex.

##### Case 2: The Child is Non-essential

When the child vertex is non-essential we are descending a stick of $\Gamma$
which can take two forms, open and half-open.

###### Case 2a: The Stick is Open

We delimit the levels of the stick by the delimiters $\LP\ \RP$ with weights
placed in the right most sections. Since the stick is open, the bottom of the
stick is an essential vertex. We restart the algorithm from the beginning with
the essential vertex as the object vertex. This can be seen in
@wpt-rli-fig-23 in the right subtree of the root.

###### Case 2a: The Stick is Half-open

When the stick is half-open (i.e. contains a leaf vertex), we append that stick
as the twist vector for the corresponding rational tangle. We delimit the stick
with $\LB\ \RB$ with all weights positive and separated by spaces where the leaf
is the right most entry. Six single vertex sticks can be seen in
@wpt-rli-fig-23 as leaf vertices.

When we have exhausted the children for the object vertex, we close our
linearization for that vertex with $\LN\ \RP$ closing the $\LP\ \right.$ for the
vertex. We return to the parent linearization, repeating until all vertices have
been exhausted. An example of a tree encoded with this strategy can be seen in
@wpt-rli-fig-23.

```{figure} ../../media/bands/watt_walk_tangle.svg
:label: wpt-rli-fig-23
:width: 500px
Encoded tree subtrees are indicated by color.
```
