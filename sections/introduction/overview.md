<!-- prettier-ignore-start -->
(sec-intro-overview)=
## Overview of this Thesis
<!-- prettier-ignore-end -->

As discussed in the previous section, the goal of this thesis is to address, in
part, the three questions "How do I systematically construct knots?", "How do I
tell two knots I make apart?", and "How do I generate new knots?" Particularly,
we will address a restricted version of these questions, for objects that can be
thought of as the building blocks of knots, the tangles introduced by Conway
[@conwayEnumerationKnotsLinks1970]. Through the middle of this thesis, we will
describe several strategies that have been employed to answer even further
restricted versions of these questions:

-   "How do I systematically construct rational tangles?", "How do I tell two
    rational tangles I make apart?", and "How do I generate new rational
    tangles?"
-   "How do I systematically construct Montesinos tangles?" and "How do I tell
    two Montesinos tangles I make apart?", and "How do I generate new Montesinos
    tangles?"
-   "How do I systematically construct algebraic/arborescent tangles?" and "How
    do I tell two algebraic/arborescent tangles I make apart?", and "How do I
    generate new algebraic/arborescent tangles?"

While we could answer these questions with pen and paper brute force, beyond a
reasonable "crossing number" (@subsec-knot_def), as small as 6 or 7, the time
and effort needed makes pen and paper untenable. To achieve our goal in a
reasonable time, we will follow a similar framework to that of Hoste,
Thistlethwaite, Weeks, and Burton [@hosteFirst1701936Knots1998]
[@hosteEnumerationClassificationKnots2005] [@burtonNext350Million2020].
Utilizing computer methods to generate a tangle table of algebraic/arborescent
tangles to twelve crossings. To effectively utilize computers for this
tabulation work requires the design and implementation of a knot theory specific
software toolbox.

### Chapter Summary

We will now summarize each of the chapters of this thesis. Organizationally,
this thesis is partitioned into five chapters, with each chapter further divided
into sections, and subsections.

#### Chapter 1: Introduction

The introduction gives an intuitive description of the basics of knot theory,
and a discussion of an application for knots and tangles. Then finishes with
this description of the content of this thesis.

#### Chapter 2: Preliminaries

This chapter gives the preliminaries in knot theory needed for the rest of the
thesis. Included are the historical background of tabulation in knot theory and
a grounding in knot and tangle theory. We will see definitions for knots and
tangles, as well as some notations and invariants for those knots and tangles.

#### Chapter 3: Tabulation

This chapter describes the theoretical methodology for the tabulation of
tangles. It is divided into two sections, the first contains the method used for
tabulation of two well-understood classes of tangles: the rational and
Montesinos tangles. The second describes the methodology for the tabulation of
the more general type of tangle the arborescent (algebraic) tangles. For each
class of tangle we tabulated, a definition and classification is given, followed
by a theoretical generation strategy.

#### Chapter 4: Software and its Engineering

This chapter addresses the computational and engineering aspects of software for
mathematics research. The chapter begins with an overview of product management
and software engineering practices. In our discussion of software engineering we
develop a process designed for use by professional and undergraduate researchers
in computational knot theory. With our process, we create a product design for a
general purpose "knot theory software toolbox". The chapter concludes with the
software design (unit description) for the tools developed to realize the
solutions in the tabulation section.

#### Chapter 5: Future Directions

The final chapter of this thesis gives an overview of future work to be done in
the tangle tabulation domain. This takes two forms, first the direct next steps
for tangle tabulation at the professional research level. Second, we outline a
collection of topics and research directions at various levels appropriate for
undergraduate researchers.
