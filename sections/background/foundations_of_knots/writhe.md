###### Writhe

Before we can develop the concept of writhe of a knot we need to define the an
orientation for a knot. Imagine the strands of a knot to be a roller coaster in
three dimensional space. It's clear that the roller coster car has two choices
of "forward" for the car to point on the track. We call a choice of forward an
orientation for the track. Similarly for knots, each strand of a knot is a
circle we can choose to traverse in one of two directions. A choice of direction
on a strand of a knots, seen in @fig-writhe-orientation is a choice of
orientation for that knot. $5_1$. Following the strand in the direction of the
arrow you'll find that you arrive where you started.

```{figure} ./media/kauf_bkt/orientation/5_1.svg
:label: fig-writhe-orientation
An orientation applied to the knot $5_1$. Following the strand in the direction
of the arrow you'll find that you arrive where you started.
```


We now zoom in on our oriented diagram to focus on a crossing. Since the whole
diagram is oriented, each strand in the local crossing has an induced
orientation, indicated by arrow heads on the strands. We can arrange the
crossing so that the over strand arrowhead points north, notice then that there
are two possible arrangements, orientations, for the under strand; pointing west
or pointing east. In this a arrangement a west pointing under strand is called a
positive (+) crossing, while an east pointing under strand is called a negative
(-) crossing, seen in @fig-writhe-oriented_crossing.

````{prf:observation}
:label: fig-writhe-oriented_crossing




```{figure} ./media/kauf_bkt/crossing/crossing_+.svg
:label: fig-inv-or-positive
@@@ TODO: Add content description
```

```{figure} ./media/kauf_bkt/crossing/crossing_-.svg
:label: fig-inv-or-negative

@@@ TODO: Add content description
```

````

A hint for determining the orientation of a crossing in practice is a right hand
rule. After the knot has been oriented, imagine your right hand with your
fingers extended and palm towards you, aligned with the over strand so that your
thumb points with the arrowhead. Now if your fingers are pointing with the
arrowhead of the understand the orientation is positive if your fingers are
opposite the arrowhead of the under strand the orientation is negative.

Given an oriented knot we can now classify each crossing as either a positive or
negative, giving us enough information to define the writhe of a knot.

The writhe, $w\LP K\RP$, of an oriented knot $ K$ is defined to be:
$$w\LP K\RP=\LP\text{count of positive crossings in } K\RP-\LP\text{count of negative crossings in } K\RP$$

The writhe is fairly simple to calculate and we will now carry out an example
calculation for knot $5_1$.

We start by taking the oriented version of knot $5_1$ seen in
@fig-writhe-orientation and modifying the diagram with local pictures for
crossings seen in @fig-writhe-local

```{figure} ./media/missing.svg
:label: fig-writhe-local
@@@ TODO: Add content description
```

then classifying each crossing as positive or negative we can count finding $5$
positive and $0$ negative crossing giving

$$
w\LP\img{images/kauf_bkt/orientation/5_1}\RP=5+0=5
$$
