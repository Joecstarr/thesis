# Foundations of Tangles

Having now an understanding of the concept of tangles and their usefulness as a
building block for knots we will switch gears slightly to consider a tangle as a
first class object. This section will give the foundations of the theory of
tangles needed for the remainder of this thesis.

# Tangle Equivalence

As we saw for knots in @subsec-knot_equivalence to tell two tangles apart we
need to also be able to say what we mean when we say tangles are the same. Our
development for the concept of equality of tangles follows closely to that of
knots. From @subsubsec-deftangles we have definitions for tangles in the context
of knot diagrams and three dimensional embeddings of knots. This tells us that
the concepts fo equality developed in @subsec-knot_equivalence namely ambient
isotopy and Reidemeister moves applies also in the tangle case with two key
differences. The first difference in tangles when compared to knots is that we
restrict ambient isotopy, and Reidemeister moves, from pushing a strand through
the Conway sphere, or Conway circle in the diagram case. This leads us to the
second difference when handling the tangle case, being how we handle the
boundary points. There are two constructions for how to handle equality; first
fixing the boundary points on the Conway sphere and second allowing the boundary
points to move on the Conway sphere.

# Non-moveable Boundary Points

The non-moveable case is the more straight forward of the two boundary inclusive
concepts of equality for tangles. When the boundary points are fixed we have
essentially the same concept of equality for knots. We need only care for the
ambient isotopy, Reidemister move, equivalence of the interior of the Conway
sphere. In the fixed boundary world we have four distinct basic tangles
$1,\ -1,\ 0,\ \text{and } \infty$ seen in @fig-four_basics. With a little play
it's easy to convince yourself that these are all distinct when the boundary is
fixed. In @fig-tangl_eq-fixed we find two tangle, each with two crossings but
not equivalent by Reidemeister moves.

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

# Moveable Boundary Points

Our second case for handling the boundary of a tangle is allowing the boundary
points to move freely on the Conway sphere. The ability to move the boundary
points gives us a scenario where for a generic tangle $T$, $T$ is equivalent to
each of its rotations and flips found in @subsubsec-tangle_flips. In addition to
the rotation and flip equivalence a moveable boundary allows us to unwind
integral components of a tangle which are connected to boundary inline with the
integral twists. This unwinding can be seen in @fig-tangl_eq-unwinding.

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

For this thesis we will assume tangles have a fixed boundary unless explicitly
mentioned.

# Modified Tangle Operations

In @subsubsec-conway_calc we saw Conway's calculus of tangles. While this
construction is powerful and flexible it's rather unintuitive when starting and
cumbersome when combined with computer methods. In this section we will describe
a slightly modified, but equivalent, version of the calculus. This version of
tangle arithmetic was first constructed by Kauffman and Goldman in 1997
@goldmanRationalTangles1997. Instead of Conway's three operations on the two
basic tangles $1$ and $0$ we need only two operations but all four basic tangles
seen in @fig-four_basics. The first operation in this arithmetic is exactly
Conway's horizontal sum, $+$. The second operation is the vertical sum, $
\vee$
, sometimes written $*$ as in Kauffman and Goldman
@goldmanRationalTangles1997. The for generic tangle $A$ and $B$, $A\vee B$ is
build analogously to the $+$ but stacking $A$ vertically on top of $B$ instead
of horizontally. The operations can be seen in @fig-newopo

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

```{figure} ./images/missing.svg

@@@ TODO: Add content description
```

These two operations give a natural arithmetic structure to the combinations of
tangles. We'll see in later sections how this structure is easily encoded on a
computer as a data structure.

# Integral Tangles

We finish the chapter with a description of a class of tangles we first
encountered in @subsubsec-opo-plus. The integral tangles are the simplest class
of tangle that are built from the basic operations on basic tangles. We start by
defining the $ \pm$ horizontal integral tangles.

A tangle built from the successive sum of $n$ $+1$ tangles is called a
horizontal $n$ tangle. Similarly, a sum of $-1$ tangles is a horizontal $ -n$
tangle.

It is convenient to notate the horizontal integral tangles simply by their
corresponding integer $\pm n$. A similar construction can be defined for the
$\vee$ operation, yielding the $ \pm$ vertical integral tangles.

A tangle built from the successive vertical sum of $n$ $ +1$ tangles is called a
vertical $n$ tangle. Similarly, a vertical sum of $-1$ tangles is a vertical
$-n$ tangle.

We adopt a similar notational convention for the vertical integral tangles,
however as to not overload our notations we will instead notate the vertical
tangles by $\pm\frac{1}{n}$.
