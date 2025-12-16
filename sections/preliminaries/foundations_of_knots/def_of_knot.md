<!-- prettier-ignore-start -->
(subsec-knot_def)=
### Definition of a Knot
<!-- prettier-ignore-end -->

As with anything, we must start with a definition, here we give one for a **proper knot**.

```{prf:definition}Jablan and Sazdanović Definition 1.17 [@jablanLinKnotKnotTheory2007]
:label: def-knot
A **proper knot** is a smooth embedding of a circle $ S^1$ into Euclidean
3-dimensional space $\R^3$ (or the 3-dimensional sphere
$S^3$).
```

With some consideration, we can see this definition aligns with our intuitive description of a knot
given in @sec-intro-intuit_knot_theory. We note that this definition gives two choices for ambient
space, for this thesis we will prefer $S^3$ as an ambient space, the preference will become clear in
later sections. A natural extension of the concept of a knot is to allow for more than a single
$S^1$ component to be embedded into the ambient space. This allowance gives us the concept of a
**$c$ component link**.

```{prf:definition} Jablan and Sazdanović Definition 1.17 [@jablanLinKnotKnotTheory2007]
:label: def-link
A **$c$ component link** is a smooth embedding of $ c$ disjoint copies of a circle
  $S^1$ into $\R^3$ (or $S^3$), where the embeddings of circles $S_i^1$ are its
  components ($i = 1, 2,\dots, c$).
```

```{convention}
  For convenience, and brevity, in the remainder of this thesis we
  will adopt the
  following convention. The term **knot** refers to the collection of
  all proper knots and
  all $c$ component links. If we find the need to exclude the $c$
  component links
  from consideration, we will use the term proper knot.
```

Playing with this three-dimensional construction for knots, it will quickly become apparent that
three-dimensional knots are unwieldy to work with. To simplify our work, we will now build a
two-dimensionally encoded model for knots, a **knot diagram**. We start by taking a knot
$K\subset S^3$. We then select an $S^2$ such that $K$ lies fully in the interior. Now, for any plane
that lies tangent to $S^2$, we take an orthogonal projection of the knot onto the plane. We require
that the projection have no **degenerate crossings**, intersections of the knot projection where
more than two points are collinear or where the crossing is not transverse. We call this projection
a **knot shadow**, an example can be seen in @fig-knot_def-shadow. A knot shadow is interpreted as a
planar graph[^planargraph], with points where strands overlap (are collinear in the projection) as
vertices, and edges of the shadow as the strands between the overlaps.

```{figure} ../../media/knot_shadow.svg
:label: fig-knot_def-shadow
A schematic diagram demonstrating a knot (orange) and its
    shadow (grey).
    Imagine a light shining from above the knot onto a piece of paper. The knot
  shadow is the shadow cast on the paper.

```

Taking only the shadow of a knot we lose some data that is intuitively important, the crossings of a
knot (the relative distance of collinear points). To recover this data in a diagram, we split the
edges of the shadow where the strand closer to the projection plane appears to travel under the edge
corresponding to the strand further from the plane. We call the edge that is split the **under
strand**, and the non-split strand the **over strand**. These augmented knot shadows are called knot
diagrams and will serve as our primary schematic model for knots throughout this thesis. We call the
count of crossings in a knot diagram the **crossing number** of the knot diagram.

We finish with naming a knot with particular significance, the knot with no crossings in its diagram
is called the **unknot**.

[^planargraph]:
    A graph in the mathematical sense, a set of vertices combined with a set of relationships
    between those vertices called edges. A planar graph is a graph that when drawn in the plane has
    no overlapping edges.
