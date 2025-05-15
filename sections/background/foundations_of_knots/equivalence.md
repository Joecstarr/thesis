# Knot Equivalence

Armed with the formal definition of a knot we can make our first progress in
answering the overarching question "How do I tell two knots I make apart? from
@sec-intro-intuit_knot_theory. To tell two knots apart we need to also be able
to discuss the concept of equivalence of knots, that concept is given by ambient
isotopy and equal knots are said to be ambient isotopic, formally stated in
@def-ambient_isotopic.

Two knots $J$ and $K$ are said to be ambient isotopic if there exists an ambient
isotopy, that is a diffeomorphism of the ambient space, taking $J$ to
$K$.@jablanLinKnotKnotTheory2007

When working with the a three dimensional model of a knot writing down explicit
ambient isotopies is, in general, quite difficult. As we did in @subsec-knot_def
we can simplify the concept of equality by moving ambient isotopy to an
equivalence of knot diagrams. Taking the orthogonal projection model for knot
diagrams given in @subsec-knot_def ambient isotopy is modeled as three
Reidemeister moves@TODO on diagrams. Meaning, two knots are ambient isotopic if
and only if they're equal under a chain of Reidemeister moves. The first
Reidemeister move we will define is the Type I move. To carry out the Type I
move, seen in @fig-knot_def-R1, start by taking a portion of a diagram with no
crossings. Now add a half twist, when adding the twist we have two choices;
twist into or out of the plane the diagram lays in. In either we can freely
remove the new crossing by twisting in the opposite direction.

```{figure} ./images/reidemeister_move/R1.svg

@@@ TODO: Add content description
```

The next Reidemeister move is the Type II move, seen in @fig-knot_def-R2. When
we carry out the type II move we need two strands, each with no crossings. We
then pull one strand on top of the other, inducing two crossing in our diagram.
Similarly to the type I move, the type II move can be freely undone by pulling
the strands apart.

```{figure} ./images/reidemeister_move/R2.svg

@@@ TODO: Add content description
```

The final Reidemeister move is the Type III move. In the type III move we take
three strands, two that form a crossing and a third that lays in one of three
possible positions; above the over strand, between the over and under strands,
or below the under strand. We can now execute the type III move by taking the
third strand and passing it across the crossing in the other two strands. As
with type I and type II, we're free to reverse the type III move.

```{figure} ./images/reidemeister_move/R3.svg

@@@ TODO: Add content description
```
