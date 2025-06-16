<!-- prettier-ignore-start -->
(sec-history-of-tabulation)=
## History of Knot Tabulation
<!-- prettier-ignore-end -->

Mathematical interest in knots was brought into the forefront of mathematics and
physics during the 1860s by Lord Kelvin. A central area of research in physics
during the 1860s was the investigation of the fundamental building blocks of
matter: the atoms. At this time Lord Kelvin hypothesized that atoms were knotted
vortices in the aether [@thomsonVortexAtoms1867]. Given this hypothesis, a
natural next step is the creation of a table of the elements which, by
hypothesis, was a table of knots.

### Knot Tabulation Hand

With Lord Kelvin's vortex hypothesis as the driving interest in knots, the first
knot table was produced, via hand computation, by P.G. Tait. Tait's first table,
completed in the 1860's, contained prime knots (described in @subsec-prime_knot)
up to seven crossings [@taitFirstSevenOrders1884], a table of the first seven
knots can be seen in @fig-hist-7table

```{figure} ../../media/knots_to_7.svg
:label: fig-hist-7table
@@@ TODO: Add content description [@schareinInteractiveTopologicalDrawing1998]
```

With a table of seven crossing knots complete Tait's work in knot tabulation
didn't stop. Tait continued to work, alongside Kirkman and Little
[@taitTenfoldKnottiness1885;@kirkmanEnumerationDescriptionConstruction1885;
@littleKnotsCensusOrder1885], on tabulation of knots for the next 25 years. The
trio ultimately published a complete list of prime knots up to ten crossings
(250+1 knots). When the knot theoretic machinery available at the time is
considered, we see the completion of these tables were a herculean task. The
tables contained a single error, two equivalent ten crossing knots, identified
in 1974 by Perko an amateur mathematician [@perkoClassificationKnots1974] (the
pair can be seen in @fig-hist-perko) .

```{figure} ../../media/perko_pair.svg
:label: fig-hist-perko
@@@ TODO: Add content description [@schareinInteractiveTopologicalDrawing1998]
```

After Tait, Kirkman, and Little's completion of the ten crossing table efforts
in knot tabulation stagnated, with few concerted efforts and little progress
being made in expanding the tables. The next researcher to take up the
tabulation torch was Conway in the 1960's [@conwayEnumerationKnotsLinks1970] who
in "a few hours" tabulated knots to eleven crossings, with only four
omissions[@caudron1982classification]. Still working by hand computation, Conway
employed a novel approach to tabulation. He described decompositions for knots
into building blocks which he called tangles. Under Conway's tangle calculus the
combinatorial work of knot tabulation became a game of building from simple to
complex. Inspired by Conway's strategies, a second effort to enumerate eleven
crossing knots was carried out by Caudron [@caudron1982classification] verifying
Conway's findings and rectifying the four omissions. Caudron's confirmation of
the eleven crossing tables marked the final chapter in the hand computation era
of knot tabulation.

### By Computer

With advancements in manufacturing in the early 1980s electronic computers
became closer to commodity products, allowing for more and diverse users to take
their crack at time consuming computational tasks. One of these computational
tasks is the construction of knot tables. The first to construct a knot table by
computer was Dowker and Thistlethwaite
[@dowkerClassificationKnotProjections1983] in 1983 who produced a table of all
prime knots to thirteen crossing. The pair implemented a novel two pass approach
that has served as an outline for all major efforts that have followed. The
process begins with a first pass to enumerate all possible knot projections.
This is followed by a second pass where "sufficient invariants to distinguish
them (knots) from each other" [@dowkerClassificationKnotProjections1983] are
computed. This effectively assigns knots to equivalence classes ("bins" in
software parlance) hence finding and removing all duplicate entries from the
list ("deduping" in software parlance). The next computer table, knots up to
sixteen crossing, was given by Hoste, Thistlethwaite, and Weeks
[@hosteFirst1701936Knots1998] in 1998. Their process deviates only slightly from
the earlier Dowker and Thistlethwaite approach, leaning on a heuristic approach
to limit the duplicates found in their first pass. This preprocessing in the
first pass allowed Hoste, Thistlethwaite, and Weeks to compute their table in
1-2 weeks of wall time[^wall-time].The most recent computational effort was
carried out by Burton in [@burtonNext350Million2020] in 2020, finding knots to
nineteen crossings. Burton's program followed closely to the two pass processes,
with further heuristic work to preprocess in the first pass and heavily relying
on the hyperbolic volume invariant for the second pass. The computation of the
nineteen crossing table required months of wall time on a cluster[^cluster],
serving as an important signpost for the time complexity problems of knot
tabulation.

[^wall-time]:
    The real effective time of a clock on a wall, this is different from CPU
    time which is a relative measure of time.

[^cluster]:
    An aggregation of many computers each with many computational cores. We'll
    see later in this thesis that tabulation is massively parallelizable.
