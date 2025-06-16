<!-- prettier-ignore-start -->
(sec-intro-overview)=
## Overview of this thesis
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
reasonable crossing number, as small as 9, the time and effort needed makes pen
and paper untenable. To achieve our goal in reasonable time we will follow a
similar framework to Hoste, Thistlethwaite, Weeks, and recently Burton
[@hosteFirst1701936Knots1998] [@hosteEnumerationClassificationKnots2005]
[@burtonNext350Million2020] utilizing computer methods to generate a tangle
table of algebraic tangles to twelve crossings. To effectively utilize computers
for this tabulation work requires the design and implementation of several
pieces of software. This tabulation framework, described in the later parts, is
constructed with the accessible nature of knot theory in mind. We keep this
accessibility in mind to enable future work with undergraduate researchers.

### Chapter Summary

In this section, we describe the order and give a short summary of each part of
this thesis. Organizationally, this thesis is broken into five parts. Each part
is further broken down into chapters, sections, and subsections.

#### Introduction

The introduction gives an intuitive description of the basics of knot theory,
and a sampling of applications for tangles. The finishes with a description of
the content of this thesis.

#### Background

This chapter gives historical and rigorous groundings in the knot theory needed
for the rest of the thesis. This includes definitions for knots and tangles, as
well as a sampling of notations and invariants for knots and tangles.

#### Tabulation

This chapter describes the methodology for the tabulation of tangles. The
chapter is broken down into two chapters, the first contains the methodology
used for tabulation of historically well-understood tangles, while the second
describes the methodology for the tabulation of the more general algebraic
(arborescent) tangles. For each class of tangle addressed, the definition and
classification is given, followed by the theoretical and computational
generation strategy.

#### Architecture Of A Knot Theory Software Toolbox

This chapter describes the software created for the tabulation. The chapter
begins with an overview of the system design for a general purpose "knot theory
software toolbox". The design given in this chapter are intended to be used in
this work as well as generically for research projects, including undergraduate
research projects. The chapter concludes with a description of the presentation
layer for the tangle table, a web interface similar to KnotInfo
[@livingstonKnotInfoTableKnot2025].

#### Future Work and Undergraduate Research

The final chapter of this thesis gives an overview of future work to be done on
tangle tabulation. The chapter has a particular emphasis on outlining project
plans for undergraduate research in tangle tabulation.
