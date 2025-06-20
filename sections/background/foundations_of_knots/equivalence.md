<!-- prettier-ignore-start -->
(subsec-knot_equivalence)=
### Knot Equivalence
<!-- prettier-ignore-end -->

Armed with the formal definition of a knot, we can make our first progress in
answering the overarching question from @sec-intro-intuit_knot_theory.

> How do I tell two knots I make apart?

To tell two knots apart we need to also be able to discuss the concept of
sameness, that is, what is equivalence in knots. Our concept of equivalence is
given by **ambient isotopy** and equal knots are said to be **ambient isotopic**
(@def-ambient_isotopic).

```{prf:definition} Ambient Isotopic [@jablanLinKnotKnotTheory2007]
:label: def-ambient_isotopic
Two knots $J$ and $K$ are said to be **ambient isotopic** if there exists an ambient
isotopy, that is a diffeomorphism of the ambient space, taking $J$ to $K$.
```

When working with the three-dimensional model of a knot, writing down explicit
ambient isotopies is, in general, quite difficult. As we did in
@subsec-knot_def, we can simplify the concept of equality by moving ambient
isotopy to an equivalence of knot diagrams. Taking the orthogonal projection
model for knot diagrams given in @subsec-knot_def, ambient isotopy is modeled as
three Reidemeister moves on diagrams
[@reidemeisterElementareBegruendungKnotentheorie1927]. Meaning, two knots are
ambient isotopic if and only if their diagrams are equal under a chain of
Reidemeister moves.

The first Reidemeister move we will define is the Type I move
[@reidemeisterElementareBegruendungKnotentheorie1927]. To carry out the Type I
move (@fig-knot_def-r1), start by taking a portion of a diagram with no
crossings, then add a half twist. When adding the twist, we have two choices;
twist into or out of the plane the diagram lays in. In either, we can freely
remove the new crossing by twisting in the opposite direction.

```{figure} ../../media/reidemeister_move/R1.svg
:label: fig-knot_def-r1
Executing the two flavors of type I move on a knot diagram. On the left, we have
a twist into the plane, also called a positive or left-handed twist. On the right,
we have a twist into the plane, also called a negative or right-handed twist.
```

The next Reidemeister move is the Type II
move[@reidemeisterElementareBegruendungKnotentheorie1927], seen in
@fig-knot_def-r2. When we carry out the type II move, we need two strands, each
with no crossings. We then pull one strand on top of the other, inducing two new
crossing in our diagram. Similarly to the type I move, the type II move can be
freely undone by pulling the strands apart.

```{figure} ../../media/reidemeister_move/R2.svg
:label: fig-knot_def-r2
Executing the two type II moves with a pair of stands. In the top image, the
bottom strand is pulled over the upper. In the bottom image, the bottom strand
is puled under the top strand.
```

The final Reidemeister move is the Type III
move[@reidemeisterElementareBegruendungKnotentheorie1927]. In the type III move
we take three strands, two that form a crossing and a third that lays in one of
three possible positions:

1. above the over strand
2. between the over and under strands
3. below the under strand

We now execute the type III by taking the third strand (not part of the center
crossing) and passing it across the center crossing. As with type I and type II,
we're free to reverse the type III move.

```{figure} ../../media/reidemeister_move/R3.svg
:label: fig-knot_def-r3
Executing the three type III moves with a set of three stands. In the images top
to bottom, the third strand is: • on top of the crossing strands • between
the crossing strands • under the crossing strands.
```

We should note here that with a concept of equivlance comes equivlance classes
of knot diagrams. Of particular interest in the tabulation of knots, are the
knot diagrams which have minimal crossing number. That is, knot diagrams where
crossing number cannot be decreasesd by reidemeister moves.
