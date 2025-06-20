## Foundations of Tangles

With the concept of tangles and their usefulness as a building block for knots,
we will switch gears slightly to consider a tangle as our main object of
interest. This section will give the foundations of the theory of tangles needed
for the remainder of this thesis.

### Tangle Equivalence

As we saw for knots in @subsec-knot_equivalence, if we want to tell two tangles
apart, we first need to be able to say when tangles are the same. Our
development of the concept of equality of tangles follows closely to that of
knots. From @subsubsec-deftangles, we have definitions for tangles in the
context of knot diagrams and three-dimensional embeddings of knots. This tells
us that the concepts of equality developed in @subsec-knot_equivalence, namely
ambient isotopy and Reidemeister moves, will apply in the tangle case with two
key differences.

The first difference in tangles when compared to knots is that we restrict
ambient isotopy, and Reidemeister moves, from pushing a strand through the
Conway sphere, or Conway circle. The second difference, is the handling of the
boundary points. There are two conventions for how to handle equality with the
boundary points; first fixing the boundary points on the Conway sphere and
second allowing the boundary points to move on the Conway sphere.

#### Non-moveable Boundary Points

The non-moveable case is the more straightforward of the two boundary concepts
of equality for tangles. When the boundary points are fixed, we have essentially
the same concept of equality for knots, ambient isotopy and Reidemister moves in
the interior of the Conway sphere/circle. In the fixed boundary world, we have
four distinct basic tangles $1,\ \ \m 1,\ 0,\ \text{and } \infty$ seen in
@fig-basic_tangles and @fig-basic_tangles_extra. With a little play, it's easy
to convince yourself that these are all distinct when the boundary is fixed. In
@fig-tangl_eq-fixed we find two tangles, each with two crossings but not
equivalent by Reidemeister moves.

````{prf:observation}
:label: fig-tangl_eq-fixed



```{figure} ../../media/fig-tang_eq-fixed-2.svg
:label: fig-tang_eq-fixed-2
A horizontal integral tangle with two crossings.
```

```{figure} ../../media/fig-tang_eq-fixed-v2.svg
:label: fig-tang_eq-fixed-v2
A vertical integral tangle with two crossings.
```

````

#### Moveable Boundary Points

Our second case for handling the boundary of a tangle is allowing the boundary
points to move freely on the Conway sphere. The ability to move the boundary
points gives us a scenario where for a generic tangle $T$, $T$ is equivalent to
each of its rotations and flips (@subsubsec-tangle_flips). In addition to the
rotation and flip equivalence, a moveable boundary allows us to unwind integral
components of a tangle (@fig-tangl_eq-unwinding).

```{figure} ../../media/fig-tangl_eq-unwinding.svg
:label: fig-tangl_eq-unwinding
The progressive unwinding of integral tangles, leaving a basic $0$ tangle.
```

```{note}
In the moveable boundary case, there is only one basic tangle, the $0$ tangle.
```

For this thesis, we will assume tangles have a fixed boundary unless explicitly
mentioned.

<!-- prettier-ignore-start -->
(subsec-tangle_operations)=
### Modified Tangle Operations
<!-- prettier-ignore-end -->

In @subsubsec-conway_calc we saw Conway's calculus of tangles. While this
construction is powerful and flexible, it's rather unintuitive and cumbersome
when combined with computer methods. In this section, we will describe a
slightly modified, but equivalent, version of the calculus. This version of
tangle arithmetic is due to Kauffman and Goldman [@goldmanRationalTangles1997].

Instead of Conway's three operations on the two basic tangles $1$ and $0$, this
arithmetic needs only two operations but all four basic tangles
(@fig-basic_tangles and @fig-basic_tangles_extra). The first operation in this
arithmetic is exactly Conway's horizontal sum, $+$ (@fig-opo-plus). The second
operation is the vertical sum, $\vee$, sometimes written
$*$[@goldmanRationalTangles1997]. For generic tangle $A$ and $B$, $A\vee B$ is
built analogously to the $+$ but stacking $A$ vertically on top of $B$ instead
of horizontally (@fig-opo-vee).

```{figure} ../../media/fig-opo-vee.svg
:label: fig-opo-vee
The vertical sum of two generic tangles.
```

These two operations combined with parentheses as in @subsubsec-opo-precedence
give a natural arithmetic structure to the combinations of tangles. We'll see in
later sections how this structure is easily encoded on a computer as a data
structure. We conclude the section by redefining the Algebraic Tangles.

```{prf:definition} Algebraic Tangle [@conwayEnumerationKnotsLinks1970]
:label: def-algbraic
Any tangle that can be produced by the two binary operations $+$ and $\vee$ on
the four basic tangles is called an **algebraic tangle**.

```

<!-- prettier-ignore-start -->
(subsec-integral_tangle)=
### Integral Tangles
<!-- prettier-ignore-end -->

We finish the chapter with a description of a class of tangles we first
encountered in @subsubsec-opo-plus. The integral tangles are the simplest class
of tangle that are built from the basic operations on basic tangles. We start by
defining the $ \pm$ horizontal integral tangles.

```{prf:definition}
A tangle built from the successive sum of $n$ $+1$ tangles is called a
horizontal integral $n$ tangle. Similarly, a sum of $\ \m 1$ tangles is a
horizontal integral $ -n$ tangle.
```

It is convenient to notate the horizontal integral tangles simply by their
corresponding integer $\pm n$. A similar construction can be defined for the
$\vee$ operation, yielding the $ \pm$ vertical integral tangles.

```{prf:definition}
A tangle built from the successive vertical sum of $n$ $+1$ tangles is called a
vertical integral $n$ tangle. Similarly, a vertical sum of $\ \m 1$ tangles is a
vertical integral $-n$ tangle.
```

We adopt a similar notational convention for the vertical integral tangles,
however as to not overload our notations, we will instead notate the vertical
tangles by $\pm\frac{1}{n}$.
