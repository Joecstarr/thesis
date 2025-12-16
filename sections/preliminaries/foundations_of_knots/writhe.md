###### Writhe

Before we can develop the concept of the **writhe** of a knot, we need to define an **orientation**
for a knot. Imagine the strands of a knot to be a roller coaster, it's clear that the rollercoster
car has two choices for direction. One direction we intuitively call forward and its oposite
backward. Just like most rollercosters, each component of a knot is a circle we can choose to
traverse in one of two directions. On a knot we call this choice of forward, an orientation, see
(@fig-writhe-orientation).

```{figure} ../../media/orientation/5_1.svg
:label: fig-writhe-orientation
An orientation applied to the knot $5_1$. Following the strand in the direction
of the arrow, you'll find that you arrive where you started.
```

We now zoom in on our oriented diagram, and focus on each crossing. Since the whole diagram is
oriented, each strand in the local crossing has an induced orientation, indicated by arrow heads on
the strands. We arrange the crossing, by rotating, so that the over strand arrowhead points up,
notice then that there are two possibilities for the under strand; pointing west or pointing east.
We call the crossing with a west pointing under strand a positive (+) crossing
(@fig-inv-or-positive), while an east pointing under strand is called a negative (-) crossing
(@fig-inv-or-negative).

```{figure} ../../media/crossing_+.svg
:label: fig-inv-or-positive
A positive crossing.
```

```{figure} ../../media/crossing_-.svg
:label: fig-inv-or-negative
A negative crossing.
```

```{note}
A hint for determining the orientation of a crossing in practice is a right-hand
rule. After the knot has been oriented, imagine your right hand with your
fingers extended and palm towards you. Align your hand with the over strand so
that your thumb points with the arrowhead. Now if your fingers are pointing with the
arrowhead of the under strand, the crossing is positive, if your fingers are
opposite the arrowhead of the under strand, the crossing is negative.
```

Given an oriented knot, we can now classify each crossing as either positive or negative, providing
us with enough information to define the writhe of a knot.

````{prf:definition}
:label: def-writhe
The writhe, $w\LP K\RP$, of an oriented knot $ K$ is defined to be:
```{math}
\begin{aligned}
w\LP K\RP&=\LP\text{count of positive crossings in } K\RP\\
&-\LP\text{count of negative crossings in } K\RP
\end{aligned}
```
````

The writhe is fairly simple to calculate, we will now carry out an example calculation for knot
$5_1$.

We start by taking the oriented version of knot $5_1$ seen in @fig-writhe-orientation and modifying
the diagram with local pictures for each crossings seen in @fig-writhe-local.

```{figure} ../../media/orientation/fig-writhe-local.svg
:label: fig-writhe-local
An oriented five crossing knot, each local picture around a vertex is magnified
to show local crossing signs.
```

Classifying each crossing as positive or negative, we can count finding $5$ positive and $0$
negative crossing giving

```{math}
w\LP\img{media/kauf_bkt/orientation/5_1}\RP=5+0=5
```
