<!-- prettier-ignore-start -->
(sec-intro-intuit_knot_theory)=
## An Intuitive Grounding in Knot Theory
<!-- prettier-ignore-end -->

A knot, when used in everyday life, is a tool whether the "bunny ear" knot
holding on your shoe, a decorative monkey's fist on your keychain, or a climbing
hitch securing yourself to a rock wall. When thinking of these tool knots, we
should note one critical attribute of these everyday knots, they're made of a
single string with open ends (@fig-intro-everyday_knot). Notice with this
construction, no matter how "knotted" the string, we can always pull on loops to
remove the knot, leaving us with only an unknotted string.

```{figure} ../../media/everyday_knot.svg
:label: fig-intro-everyday_knot
:alt: testing this thing
An everyday knot with open ends.
```

This leaves us with a somewhat unsatisfying construction, exactly one object.
How might we add some spice to our construction? What if we turn the string into
a circle by gluing the ends as in @fig-intro-everyday_knot_closed. When we try
to wiggle the closed up string around, stretching and pulling on it to try to
remove the knot, we end up tugging all the way around the circle. We call these
closed up knots **mathematical knots**.

```{figure} ../../media/everyday_knot_closed.svg
:label: fig-intro-everyday_knot_closed
Closing the ends of the everyday knot in @fig-intro-everyday_knot to form a
mathematical knot.
```

```{figure} ../../media/circle.svg
:label: fig-intro-circle
A representation of a simple loop made from glueing the ends of a rope together.
```

Constructing a physical model of @fig-intro-everyday_knot_closed and exploring
with it should convince you that the knot can't be removed. With this, when
compared to an everyday knot, we are already in a better place. Continuing to
experiment with your physical model, twisting the ends of the string around each
other in different ways (@fig-intro-torus). You may discover that then gluing
the ends yields knots that can't be maneuvered to look the same as
@fig-intro-everyday_knot_closed or @fig-intro-circle.

```{figure} ../../media/torus_physical.svg
:label: fig-intro-torus
A representation of twisting the ends of a rope around itself before gluing.
```

In fact, this twisting gives us a whole infinite family of odd crossing torus
knots, a sampling of which can be seen in @fig-intro-torus_knots.

```{figure} ../../media/torus.svg
:label: fig-intro-torus_knots
Three knots built from the operation seen in @fig-intro-torus. From left
to right, a three, five, and seven crossing torus knots.
```

Our experimentation with the physical model may conjure some questions, three
important questions we may ask are;

1. "How do I systematically construct knots?"
1. "How do I tell two knots I make apart?"
1. "How many knots can I write down?".

Attempting to answer these questions, even just in part or with restrictions, is
the bread and butter of knot theory and the focus of the rest of this thesis.
Some great texts for continued reading on knot theory in order of accessibility
are: The Knot Book: An Elementary Introduction to the Mathematical Theory of
Knots by Adams [@adamsKnotBookElementary2004], LinKnot: Knot Theory by Computer
by Sazdanovic [@jablanLinKnotKnotTheory2007], Knots and Links by Rolfsen
[@rolfsenKnotsLinks2003], and An Introduction to Knot Theory by Lickerish
[@lickorishIntroductionKnotTheory1997]. The remainder of this thesis quickly
exchanges the idea of a knot for that of a tangle, introduced by Conway
[@conwayEnumerationKnotsLinks1970]. A tangle can be thought of as drawing a
circle around, or slamming a cookie cutter onto, a knot diagram. Then cutting
off the parts of the knot laying outside the circle/cookie cutter, this process
is seen in @fig-intro-tangle_maker.

```{figure} ../../media/tangle_maker.svg
:label: fig-intro-tangle_maker
The creation of a tangle from a knot by cutting a section out of the knot but
fixing four points.
```

As we'll see in the following section, mathematical knots and tangles have
various real-world applications.
