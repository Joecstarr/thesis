<!-- prettier-ignore-start -->
(sec-arborescent-linear)=
#### An Encoding Strategy for Arborescent Knots and Tangles
<!-- prettier-ignore-end -->

The various flavors of weighted planar trees we have seen thus far are a useful tool for
manipulation of arborescent tangles by humans or machines. Unfortunately, the tree structure is
quite difficult to store directly in a computer database. We will rectify this by introducing a
linearization strategy for weighted planar trees. This linearization strategy is designed to encode
not only CWPTT but arbitrary weighted planar tangle trees. If a weighted planar tangle tree has more
than one free bond we list the label as a subtree. We will omit this from our algorithm description
as we are primarily concerned with RLITT.

```{note}
The strategy outlined here is designed for linearizing tangles. A small
modification must be made for use with knots. That being, in the knot case,
ignore the $0^{\text{th}}$ weight position for the root.
```

We will descend the tree following the indexing of the total order (@indexing-rpt). As we descend
the tree, we annotate the linearization with two sets of delimiters. Each delimiter communicates
extra information about the type of subtree it is delimiting, the two sets of delimiters are as
follows:

- $\LB\ \RB$: Corresponds to a half-open proper stick and is interpreted as a twist vector for a
  rational tangle @kauffmanClassificationRationalKnots2002.
- $\LP\ \RP$: Corresponds to a vertex not on a half-open stick.

We will now walk through an example of the linearization algorithm. Let $\Gamma$ be a weighted
planar tangle tree seen in @wpt-rli-fig-23. As we walk the tree, the vertex currently being
linearized will be called the **object vertex**.

##### Tangle Linearization Example

We begin by adding the $V_4$ label for our tangle to the linearization. We then start the following
algorithm with the root as the object vertex.

For the object vertex, we add a '$\LP\ \right.$' delimiter to our linearization. Adding to our
linearization the weights and children of the object vertex in an anti-clockwise order. When a child
bond is encountered, we descend to that child. When we descend, we have two cases to consider, the
child is a half-open proper stick or otherwise.

##### Case 1: The Child Is The Root Of A Half-Open And Proper Stick

When the child is the root of a is proper and half-open (contains a leaf vertex), we append that
stick as the twist vector (@rational-def-twistvector) for the corresponding rational tangle. Let the
stick consist of the vertices, $v_i\cdots v_{i+k}$, and weights, $w_i\cdots w_{i+k}$. We delimit the
stick with $\LB\ \RB$, with each weight separated by a space, and the leaf weight as the left most
entry of the twist vector. Further, every other entry is multiplied by $-1$, forcing the sign of all
entries to match, as in @linear-math-tv.

```{math}
:label: linear-math-tv
\LB w_{i+k}\ \m w_{i+k-1}\cdots\ \m w_{i-1}\ w_{i}\RB
```

##### Case 2: The Child Is Essential, On A Open Stick, Or On A Non-Proper Stick

In this case, we restart the algorithm from the beginning with the current vertex as the object
vertex.

When we have exhausted the children for the object vertex, we close our linearization for that
vertex with the delimiter '$\LN\ \RP$'. We then return to the parent linearization, repeating until
all vertices have been exhausted. An example of a tree encoded with this strategy can be seen in
@wpt-rli-fig-23.

```{figure} ../../media/bands/watt_walk_tangle.svg
:label: wpt-rli-fig-23

Encoded tree subtrees are indicated by color.
```
