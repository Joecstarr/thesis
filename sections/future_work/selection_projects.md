### Selection of Undergraduate Projects

The accessibility of knot theory and tangles was discussed in the in
introduction (Chapter @pt-introduction) this elaborates on how that
accessibility can be leveraged to engage Undergraduates in research. Throughout
this thesis we've investigated and observed the depth of tangle tabulation.
We've also seen, even through the structure of this thesis itself, how easily
portions of tangle tabulation can be "peeled off" and decomposed as a singular
self-contained project.

#### Compute HOMFLYPT polynomial from algebraic tangle
trees

One of the most important advancements in knot theory was the discovery of knot
polynomials as a class of knot invariants. Perhaps the most powerful of these
polynomials is the HOMFLYPT polynomial @freydNewPolynomialInvariant1985 $$ P(L)
= \frac{-(\ell+\ell^{-1})}{m} P(L_1)P(L_2) $$ \ noindent constructed from the
skein relations ( @fig-future_work-Skein_HOMFLY ) conveniently the data needed
to apply the skein relations is exactly the data encoded by the algebraic tangle
tree, with the natural tangle orientations. @skein_rel

```{figure} ./images/Skein_HOMFLY.svg

@@@ TODO: Add content description
```

In this project an undergraduate researcher will conceive the theory and design
the software for computing the HOMFLYPT (and Jones as special case of HOMFLYPT)
polynomial. The hand computation of the HOMFLYPT, for reasonably sized knots,
requires only college algebra maturity and should be easily accomplishable by
most undergraduates. However, the algorithmic computation of HOMFLYPT offers a
range of great opportunities for original heuristic optimizations.

#### Compute Diagram for Algebraic Tangle Trees

Perhaps the aspect of knot theory that makes it among the most accessible higher
math domains is the ability for anyone to draw pictures of the knots and play. A
continuing theme of this thesis is that computations/operations are easy by had,
with the qualifier, "up to reasonable crossing number". This carries through
with the drawing of the diagrams. The primary drawing tool in knot theory is
KnotPlot @schareinInteractiveTopologicalDrawing. However, KnotPlot has no
interface for drawing knots in "arbitrary" notations. This project will remedy
that, with the description of a LUA interface for placing beads into KnotPlot
and a further layer for algebraic tangle trees to be drawn from a call to The
Tanglenomicon website API.

#### Notation Description for Extended Gauss Notation

There are many ways to encode the data of a knot, each with its own advantages
and disadvantages. Throughout this thesis the primary target notation was the
algebraic tangle tree @TODO. In the context of tangle tabulation and tangle
arithmetic this is a natural choice as it preserves the important algebraic
substructure for the tangles, while in section
@sec-future_work-continued_tabulation we saw that the Conway notation for
polygonal tangles is preferred. Another commonly used notational strategy is the
extended Gauss notation @knotinfo_gauss. In the extended Gauss notation a knot
is encoded as a string of integers. The integers are assigned to crossings by
starting at a point and walking along the strand until we come to a crossing. If
the crossing has a label we list that label if not we increment our count. We
also encode if we entered the crossing as the over/under strand by a +/-
attached to the listed integer, a Gauss notation of the trefoil knot:
$$
1,-2,3,-1,2,-3 $$ The extended Gauss notation additionally encodes the data
for handedness of the crossing. In this project an undergraduate researcher will
describe a computational data structure for extended Gauss notation. They will
then develop the software implementing extended Gauss notation within The
Tanglenomicon core library structure. Finally, as a stretch goal they will
develop a translation interface for taking algebraic tangle trees and converting
them into extended Gauss notation.

#### Notation description for planar diagram (PD) notation

There are many ways to encode the data of a knot, each with its own advantages
and disadvantages. Throughout this thesis the primary target notation was the
algebraic tangle tree @TODO. In the context of tangle tabulation and tangle
arithmetic this is a natural choice as it preserves the important algebraic
substructure for the tangles, while in section
@sec-future_work-continued_tabulation we saw that the Conway notation for
polygonal tangles is preferred. Another commonly used notational strategy is the
planar diagram (PD) notation @knotinfo_pd. A knot encoded in PD nation is a list
of lists of integers each with 4 integers. To encode a diagram as in PD we start
by enumerating the strands between crossings. Now starting with strand labeled 1
and walk around the knot until you reach a crossing, now imagine that crossing
as a +/- 1 tangle with the incoming strand as the SE point. List the integers
associated with the strands as $\LS \text{SE, NE, NW, SW}\RS$. Continue in this
way until all crossings are exhausted, an example of the trefoil knot encoded as
PD notation is: $$ \LS\LS 1,5,2,4 \RS,\LS 2,5,3,6\RS,\LS 3,1,4,6\RS\RS $$ In
this project an undergraduate researcher will describe a computational data
structure for PD notation. They will then develop the software implementing PD
notation within The Tanglenomicon core library structure. Finally, as a stretch
goal they will develop a translation interface for taking algebraic tangle trees
and converting them into PD notation.

#### Notation description for DT notation

There are many ways to encode the data of a knot, each with its own advantages
and disadvantages. Throughout this thesis the primary target notation was the
algebraic tangle tree @TODO. In the context of tangle tabulation and tangle
arithmetic this is a natural choice as it preserves the important algebraic
substructure for the tangles, while in section @TODO we saw that the Conway
notation for polygonal tangles is preferred. Another commonly used notational
strategy is the Dowker-Thistlethwaite (DT) notation @knotinfo_dt. A knot encoded
in DT notation is list of even integers. To encode a knot in DT notation we need
to first start on the string between two crossing and start a walk along the
string. At each crossing we reach we label, starting at 1 that crossing with an
integer then increment. We repeat this process until each crossing has two
labels (one even and one odd). Now ordering the crossings their odd label and
listing will give the DT notation of the knot diagram, an example of the trefoil
knot is: $$ 4,6,2 $$ In this project an undergraduate researcher will describe a
computational data structure for DT notation. They will then develop the
software implementing DT notation within The Tanglenomicon core library
structure. Finally, as a stretch goal they will develop a translation interface
for taking algebraic tangle trees and converting them into DT notation.

#### Notation description for ??? notation

As seen in the previous three sections each of the various knot notational
structures offer an opportunity for an undergraduate research project. The
general project outline can be described as follows. In this project an
undergraduate researcher will describe a computational data structure for ???
notation. They will then develop the software implementing ??? notation within
The Tanglenomicon core library structure. Finally, as a stretch goal they will
develop a translation interface for taking algebraic tangle trees and converting
them into ??? notation.

#### Random tangle retrieval

In the introduction chapter @sec-intro-applications applications of knots to the
hard sciences were discussed. When working in the hard sciences being able to
sample with an understood distribution from a collection is important. Similarly
to the above notational projects, describing and implementing random sampling
methodologies is a class of extremely useful tabulation projects. A project
outline for random tangle sampling can be described as follows. In this project
an undergraduate researcher will describe and implement a computational method
for sampling from a collection of tangles. The distribution of the sampling
method will classified. Finally, the researcher will implement the sampling
strategy for use with the Tanglenomicon.
