<!-- prettier-ignore-start -->
(sec-history-of-tabulation)=
## History of Knot Tabulation
<!-- prettier-ignore-end -->

Mathematical interest in knots was brought to the forefront of mathematics and
physics during the 1860s by Lord Kelvin. A central area of research in physics
during the 1860s was the investigation of the fundamental building blocks of
matter: the atoms. Lord Kelvin hypothesized that atoms were knotted vortices in
the aether [@thomsonVortexAtoms1867], with this hypothesis, a natural next step
is the creation of a table of the elements which, by hypothesis, was a table of
knots.

### Knot Tabulation by Hand

With Lord Kelvin's vortex hypothesis as the driving force for knot tabulation,
the first knot table was produced, via hand computation, by P.G. Tait. Tait's
first table, completed in the 1860s, contained prime knots (described in
@subsec-prime_knot) up to seven crossings [@taitFirstSevenOrders1884], a table
of the first seven knots can be seen in @fig-hist-7table

```{figure} ../../media/knots_to_7.svg
:label: fig-hist-7table
A table of the first seven prime knots. [@schareinInteractiveTopologicalDrawing1998]
```

With a table of seven crossing knots complete, Tait's work in knot tabulation
continued, alongside Kirkman and Little [@taitTenfoldKnottiness1885;
@kirkmanEnumerationDescriptionConstruction1885; @littleKnotsCensusOrder1885],
for the next 25 years. The trio ultimately constructed a complete list of prime
knots up to ten crossings (250+1 knots). When the knot theoretic machinery
available at the time is considered, the completion of these tables with such
high accuracy was a Herculean task. The tables contained a single error, two
equivalent (described in @subsec-knot_equivalence) ten crossing knots
(@fig-hist-perko), identified in 1974 by Perko, an amateur mathematician
[@perkoClassificationKnots1974].

```{figure} ../../media/perko_pair.svg
:label: fig-hist-perko
The Perko pair, a pair of equivalent ten crossing knots appearing as an
error in early knot tables
[@schareinInteractiveTopologicalDrawing1998;@perkoClassificationKnots1974].
```

After the completion of the ten crossing tables, efforts in knot tabulation
stagnated, with few concerted efforts and little progress being made in
expanding the tables. The next researcher to take up the tabulation torch was
Conway in the 1960s [@conwayEnumerationKnotsLinks1970]. Conway, in "a few hours"
[@conwayEnumerationKnotsLinks1970], tabulated knots to eleven crossings, with
only four omissions[@caudron1982classification]. Conway's work continued by hand
computation, but employed a novel approach to tabulation. He described
decompositions of knots into building blocks, which he called
tangles[@conwayEnumerationKnotsLinks1970]. Conway paired this with a calculus to
glue the blocks together. Under Conway's tangle calculus, the combinatorial work
of knot tabulation became a game of building from simple to complex. Inspired by
Conway's strategies, a second effort to enumerate eleven crossing knots was
carried out by Caudron [@caudron1982classification], verifying Conway's findings
and rectifying the four omissions. Caudron's confirmation of the eleven crossing
tables marked the final chapter in the hand computation era of knot tabulation.

### Knot Tabulation by Computer

With advancements in manufacturing in the early 1980s, electronic computers
became closer to commodity products, this allowed for researchers of diverse
backgrounds and interests to take their crack at time-consuming computational
tasks. One of these computational tasks was the construction of knot tables. The
first to construct a knot table by computer were Dowker and Thistlethwaite in
1983 [@dowkerClassificationKnotProjections1983], who produced a table of all
prime knots to thirteen crossings. The pair implemented a novel two pass
approach that has served as an outline for all major efforts that have followed.
The process begins with a first pass to enumerate all possible knot diagrams
(described in @subsec-knot_def). This is followed by a second pass where
"sufficient invariants to distinguish them (knots) from each other"
[@dowkerClassificationKnotProjections1983] are computed. This effectively
assigns knots to equivalence classes (bins [^bins]), hence finding and removing
all duplicate entries from the list (deduping [^dedupe]).

The next table produced by computer, knots up to sixteen crossing, was given by
Hoste, Thistlethwaite, and Weeks [@hosteFirst1701936Knots1998] in 1998. Their
process deviates only slightly from the earlier approach of Dowker and
Thistlethwaite, by leaning on heuristics[^heuristics] to limit the duplicates
found in their first pass. This preprocessing in the first pass allowed Hoste,
Thistlethwaite, and Weeks to compute their table in one to two weeks of wall
time[^wall-time].

The most recent computational effort was carried out by Burton in 2020
[@burtonNext350Million2020], finding knots to nineteen crossings. Burton's
program followed closely to the two pass processes, with further heuristic work
to preprocess in the first pass and heavily relying on the hyperbolic volume
invariant for the second pass. The computation of the nineteen crossing table
required months of wall time on a cluster[^cluster], serving as an important
signpost for the time requirement problems of knot tabulation.

### Tangle Tabulation

Conway's tangle construction allowed him to quickly and effectively tabulate
knots by hand. These building blocks of knots are interesting mathematical
objects in their own right, however tabulation efforts for tangles have been
sparse. The importance of the creation of a large table of tangles has been
called:

> "The Most Important Missing Infrastructure Project in Knot Theory" - Bar-Natan
> [@bar-natanMostImportantMissing]

As it stands, tables of tangles have been generated by hand up to seven
crossings by Kanenobu, Saito, and Satoh [@kanenobuTanglesSevenCrossings2003a].
Computer driven efforts have been undertaken by several members of the
University of Iowa Applied Topology (UIAT) group namely Conolly
[@connollyClassificationTabulation2string2021], Bryhtan
[@bryhtanTabulating2stringTangles2024], and this thesis. Separately, a table of
algebraic tangles has been produced by Gren, Sulkowska, and,
Gabrovšek[@gren2025classificationalgebraictangles].

[^wall-time]:
    The real effective time of a clock on a wall, this is different from CPU
    time which is a relative measure of time.

[^cluster]:
    An aggregation of many computers, each with many computational cores. We'll
    see later in this thesis that tabulation is massively parallelizable.

[^bins]:
    In software development, the mathematical concept of an equivalence class is
    often called a "bin".

[^dedupe]:
    Short for deduplicating, meaning the removal of duplicate entries from the
    list.

[^heuristics]:
    When discussing algorithms, a heuristic describes a special case that, when
    seen, short circuits the algorithm, reducing unnecessary work.
