<!-- prettier-ignore-start -->
(sec-intro-overview)=
## Overview of This Thesis
<!-- prettier-ignore-end -->

As discussed in the previous section, the goal of this thesis is to address, in
part, the three questions "How do I systematically construct knots?", "How do I
tell two knots I make apart?", and "How many knots can I write down?" .
Particularly, we will address a restricted version of these questions, for
objects that can be thought of as the building blocks of knots, the tangles
introduced by Conway [@conwayEnumerationKnotsLinks1970]. Through the middle of
this thesis, we will describe several strategies that have been employed to
answer even further restricted versions of these questions:

-   "How do I systematically construct rational tangles?", "How do I tell two
    rational tangles I make apart?", and "How many rational tangles can I write
    down?"
-   "How do I systematically construct Montesinos tangles?" and "How do I tell
    two Montesinos tangles I make apart?", and "How many Montesinos tangles can
    I write down?"
-   "How do I systematically construct algebraic/arborescent tangles?" and "How
    do I tell two algebraic/arborescent tangles I make apart?", and "How many
    algebraic/arborescent tangles can I write down?"

While we could answer these questions with pen and paper brute force, beyond
reasonable crossing number, as small as 9 or 10, the time and effort needed
makes pen and paper untenable. To achieve our goal in reasonable time, we will
follow a similar framework to that of Hoste, Thistlethwaite, Weeks, and Burton
[@hosteFirst1701936Knots1998] [@hosteEnumerationClassificationKnots2005]
[@burtonNext350Million2020]. Utilizing computer methods to generate a tangle
table of algebraic/arborescent tangles to twelve crossings. To effectively
utilize computers for this tabulation work requires the design and
implementation of a framework and several pieces of software. This tabulation
framework, described in the later chapters, is constructed with the accessible
nature of knot theory in mind to enable future work with undergraduate
researchers.

### Chapter Summary

For the remainder of this section, we describe the order and give a short
summary of each chapter of this thesis. Organizationally, this thesis is broken
into five chapters. Each chapter is further broken down into sections, and
subsections.

#### Introduction

The introduction gives an intuitive description of the basics of knot theory,
and a discussion of an application for knots and tangles. Then finishes with
this description of the content of this thesis.

#### Background

This chapter gives the preliminaries needed for the rest of the thesis. This
includes the historical background of tabulation in knot theory and a rigorous
grounding in knot and tangle theory. We will see definitions for knots and
tangles, as well some notations and invariants for knots and tangles.

#### Tabulation

This chapter describes the theoretical methodology for the tabulation of
tangles. The chapter is broken down into two chapters, the first contains the
methodology used for tabulation of historically well-understood classes of
tangles. The second describes the methodology for the tabulation of the more
general algebraic (arborescent) tangles. For each class of tangle addressed, a
definition and classification is given, then followed by the theoretical and
computational generation strategy.

#### Architecture Of A Knot Theory Software Toolbox

This chapter describes the software and process that was created for
computational knot theory. The chapter begins with an overview of product
management and software engineering. We then give a design for a general purpose
"knot theory software toolbox", intended to be used in this work as well as
generically for research projects, including undergraduate research projects.
The chapter concludes with the software design (unit description) for the tools
developed to realize the solutions in the tabulation section. These software
design descriptions are phrased to fit the process outlined by the "knot theory
software toolbox".

#### Future Directions and Undergraduate Research

The final chapter of this thesis gives an overview of future work to be done on
tangle tabulation. This takes two forms, first the direct next steps in tangle
tabulation at the professional research level. The second form is on outlining
future project topics for undergraduate researchers at various levels.
