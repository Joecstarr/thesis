<!-- prettier-ignore-start -->
(sec-intro-intuit_knot_theory)=
## An Intuitive Grounding in Knot Theory
<!-- prettier-ignore-end -->

A knot, when used in everyday life, is a tool whether the "bunny ear" knot
holding on your shoe, a decorative monkey's fist on your keychain, or a climbing
hitch securing yourself to a rock wall. When thinking of these tool knots, we
should note one critical attribute of all these everyday knots: they're made of
a single string with open ends, as seen in @fig-intro-everyday_knot. Notice with
this construction, no matter how "knotted" the string, we can always pull on
loops to remove the knot, leaving us with only an unknotted string.

```{figure} ../../media/everyday_knot.svg
:label: fig-intro-everyday_knot
:alt: testing this thing
@@@ TODO: Add content description
```

This leaves us with a somewhat unsatisfying construction, exactly one object.
How might we add some spice to our construction? What if we turn the string into
a circle by gluing the ends as in @fig-intro-everyday_knot_closed.

````{prf:observation}
:label: fig-intro-closed_knots


```{figure} ../../media/everyday_knot_closed.svg
:label: fig-intro-everyday_knot_closed
@@@ TODO: Add content description
```

```{figure} ../../media/circle.svg
:label: fig-intro-circle
@@@ TODO: Add content description
```
````

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

```{figure} ../../media/torus.svg
:label: fig-intro-torus
@@@ TODO: Add content description
```

In fact, this twisting gives us a whole infinite family of odd crossing torus
knots, a sampling of which can be seen in @fig-intro-torus_knots.

````{prf:observation}
:label: fig-intro-torus_knots


```{figure} ../../media/torus_3.svg
:label: fig-intro-torus_3
@@@ TODO: Add content description
```

```{figure} ../../media/torus_5.svg
:label: fig-intro-torus_5

@@@ TODO: Add content description
```

```{figure} ../../media/torus_7.svg
:label: fig-intro-torus_7

@@@ TODO: Add content description
```
````

These closed knots are what are called "mathematical knots" and our
experimentation may conjure some questions, perhaps the three most obvious
questions being "How do I systematically construct knots?", "How do I tell two
knots I make apart?", and "How many knots can I write down?". Attempting to
answer these questions, even just in part or with restrictions, is the bread and
butter of knot theory and the focus of the rest of this thesis. Some great texts
for continued reading on knot theory in order of accessibility are: The Knot
Book: An Elementary Introduction to the Mathematical Theory of Knots by Adams
[@adamsKnotBookElementary2004], LinKnot: Knot Theory by Computer by Sazdanovic
[@jablanLinKnotKnotTheory2007], Knots and Links by Rolfsen
[@rolfsenKnotsLinks2003], and An Introduction to Knot Theory by Lickerish
[@lickorishIntroductionKnotTheory1997]. The remainder of this thesis quickly
exchanges the idea of a knot for that of a tangle, introduced by Conway
[@conwayEnumerationKnotsLinks1970]. To build a tangle from a knot, we take what
we've developed and follow the recipe (as seen in @fig-intro-tangle_maker):

```{figure} ../../media/tangle_maker.svg
:label: fig-intro-tangle_maker
@@@ TODO: Add content description
```

As we'll see in the following section, mathematical knots and tangles have
various real-world applications.
