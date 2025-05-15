## An Intuitive Grounding in Knot Theory

A knot, when used in everyday life, is a tool whether the "bunny ear" knot
holding on your shoe, a decorative monkey's fist on your keychain, or a climbing
hitch securing yourself to a rock wall. When thinking of these tool knots, we
should note one critical attribute of all these everyday knots: they're made of
a single string with open ends, as seen in @fig-intro-everyday_knot. Notice with
this construction, no matter how "knotted" the string, we can always pull on
loops to remove the knot, leaving us with only an unknotted string.

```{figure} ./images/everyday_knot.svg
:label: fig-intro-everyday_knot
```

This leaves us with a somewhat unsatisfying construction, exactly one object.
How might we add some spice to our construction? What if we turn the string into
a circle by gluing the ends as in @fig-intro-everyday_knot_closed.

<!-- @@@-subfigure-start-@@@ -->

```{figure} ./images/everyday_knot_closed.svg
:label: fig-intro-everyday_knot_closed
```

```{figure} ./images/circle.svg
:label: fig-intro-circle
```

<!-- @@@label:fig-intro-closed_knots  -->
<!-- @@@-subfigure-end-@@@ -->

Now when we try to wiggle the string around, stretching and pulling on it to try
to remove the knot, we end up tugging all the way around the circle.
Constructing a physical model of @fig-intro-everyday_knot_closed and exploring
it should convince you that the knot can't be removed. We are already in a
better place when compared to an everyday knot, as we can record at least two,
those listed in @fig-intro-closed_knots. Continuing to experiment with your
physical model, you may discover that twisting the ends of the string around
each other (figure @fig-intro-torus) then gluing the ends gives you knots that
can't be maneuvered to look the same as @fig-intro-everyday_knot_closed or
@fig-intro-circle.

```{figure} ./images/torus.svg
:label: fig-intro-torus
```

In fact, this twisting gives us a whole infinite family of odd crossing torus
knots, a sampling of which can be seen in @fig-intro-torus_knots.

<!-- @@@-subfigure-start-@@@ -->

```{figure} ./images/torus_3.svg
:label: fig-intro-torus_3
```

```{figure} ./images/torus_5.svg
:label: fig-intro-torus_5

```

```{figure} ./images/torus_7.svg
:label: fig-intro-torus_7

```

<!-- @@@label:fig-intro-closed_knots  -->
<!-- @@@-subfigure-end-@@@ -->

These closed knots are what are called "mathematical knots" and our
experimentation may conjure some questions, perhaps the two most obvious
questions being "What knots can I make?" and "How do I tell two knots I make
apart?". Attempting to answer these two questions, even just in part or with
restrictions, is the bread and butter of knot theory and the focus of the rest
of this thesis. Some great texts for continued reading on knot theory in order
of accessibility are: The Knot Book: An Elementary Introduction to the
Mathematical Theory of Knots by Adams @adamsKnotBookElementary2004, LinKnot:
Knot Theory by Computer by Sazdanovic @jablanLinKnotKnotTheory2007, Knots and
Links by Rolfsen @rolfsenKnotsLinks2003, and An Introduction to Knot Theory by
Lickerish @lickorishIntroductionKnotTheory1997. The remainder of this thesis
quickly exchanges the idea of a knot for that of a tangle, introduced by Conway
@conwayEnumerationKnotsLinks1970. To build a tangle from a knot, we take what
we've developed and follow the recipe (as seen in @fig-intro-tangle_maker):

```{figure} ./images/tangle_maker.svg
:label: fig-intro-tangle_maker
```

As we'll see in the following section, mathematical knots and tangles have
various real-world applications.
