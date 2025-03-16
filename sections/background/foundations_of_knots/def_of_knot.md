# Definition of a Knot

Our first effort in formalization is the construction of a definition for knots.

A proper knot is a smooth embedding of a circle $ S^1$ into Euclidean
3-dimensional space $\R^3$ (or the 3-dimensional sphere
$S^3$).@jablanLinKnotKnotTheory2007

After some consideration we can see this definition aligns with our intuitive
description of a knot given in @sec-intro-intuit_knot_theory. We note that this
definition gives two choices for ambient space, for this thesis we will prefer
$S^3$ as an ambient space, the preference will become clear in later sections. A
natural extension of this concept is the allowance for more then a single $S^1$
component to be embedded into the ambient space and allowing this gives the
following definition.

A $c$ component link is a smooth embedding of $ c$ disjoint copies of a circle
$S^1$ into $\R^3$ (or $S^3$), where the embeddings of circles $S_i^1$ are its
components ($i = 1, 2,... , c$). @jablanLinKnotKnotTheory2007

For convenience, and brevity, we will adopt the following convention. The term
knot will refer to the collection of all proper knots as well as all $c$
component links. When we find need to exclude the $c$ component links from
consideration we will use the term proper knot.

Playing with this three dimensional construction for knots it will become
quickly apparent that three dimensional knots are unwieldy to work with. In an
effort to simplify our work we will now build a two dimensionally encoded model
for knots. We start by taking a knot $K$ as above, we select an $S^2$ such that
$K$ lays fully in the interior. Now, for any plane that lays tangent to $S^2$ we
can take an orthogonal projection of the knot onto the plane. We further require
that the projection have no more then two points on strands that are colinear.
We call this projection a knot shadow, an example can be seen in
@fig-knot_def-shadow, and is commonly interpreted as a planar graph.

```{figure} ./images/missing.svg

```

```{figure} ./images/missing.svg

```

In our knot shadow we notice some points where strands overlap, call them
vertices as in a graph. When we look at these points in out three dimensional
model, those vertices are where strands are colinear in the projection. Taking
only the shadow of a knot loses some intuitively important data being the
relative distance of colinear points, our crossings. To recover this data, we
split the edges of the shadow, corelating to the strand closer to the plane so
that it appears to travel under the edge corelating to the strand further from
the plane. We call the split edge the under strand while the other edge is
called the over strand,. The result of this can be seen in
@fig-knot_def-shadow_knot. These augmented knot shadows are called knot diagrams
and will serve as our primary schematic model for knots throughout this thesis.
We finish with naming a knot with particular significance as we move forward,
the knot with no crossings in its diagram is called the unknot.
