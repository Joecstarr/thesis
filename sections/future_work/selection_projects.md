<!-- prettier-ignore-start -->
(sec-selection_projects)=
### Selection of Undergraduate Projects
<!-- prettier-ignore-end -->

In this section we will provide a curated collection of undergraduate research problem statements.
We will also give a brief outline for each, contextualizing the problem and describing what phase of
the research experience program the problem may be appropriate for:

1. **Lower Division Student:** A lower division student is a student with little to no research or
   abstract math experience. A student at this level should be expected to have completed a college
   algebra course and started a calculus sequence. For students with a computational background we
   should expect the student to have started an introduction to programming course.
2. **Intermediate Student:** An intermediate student is a student who has some exposure to abstract
   math. This could take the form of solving a lower division problem. These students should be well
   into a calculus sequence, having completed calculus II (advanced integration) or calculus III
   (vector calculus). For students with a computational background we should expect the student to
   have completed an introduction to programming sequence and started a course on algorithms and
   data structures.
3. **Upper Division Student:** An upper division student is a student who can be expected to work
   semi-independently. They have solved one or more intermediate student problems, have completed
   the standard calculus sequence, and have begun abstract math courses. For students with a
   computational background we should expect the student to have completed a discrete methods
   course, ideally covering computational complexity theory.

The remainder of the section gives statements for problems appropriate for undergraduate research.
The problems in the list fall into five types: visualizations (@sec-proj-visual), invariants
(@sec-projs-invariants), notations (@sec-proj-notations), generation (@sec-proj-gen), and
potpourri[^pot] (@sec-proj-pot).

<!-- prettier-ignore-start -->
(sec-proj-visual)=
#### Visualization
<!-- prettier-ignore-end -->

Visualization and spatial reasoning are critically important for work in knot theory. Problems of
the visualization type develop specific visualizations or general visualization tools for knots and
tangles.

<!-- prettier-ignore-start -->
(sec-proj-mosaic)=
##### Create Knot Mosaics: Lower Division Student
<!-- prettier-ignore-end -->

###### Problem Statement

Create a knot mosaic that has a particular property.

###### Brief

Knot mosaics are a simple method for creating knots from a collection of tiles. Creating mosaics
with a particular property, a specific writhe, for example, is a fun and engaging activity where
abstraction of a concept can be explored. Modifying the tile set can add additional complexity to
the task.

<!-- prettier-ignore-start -->
(sec-proj-sticks)=
##### Create Stick Knots: Lower Division Student
<!-- prettier-ignore-end -->

###### Problem Statement

Create stick knots with desired properties.

###### Brief

Stick knots are knots built from a collection of unit sticks. Creating a physical model by hand or
with computer design and 3D printing develops spatial reasoning skills needed for work in higher
knot theory.

<!-- prettier-ignore-start -->
(sec-proj-quilt)=
##### Creating Celtic Knots: Lower Division Student
<!-- prettier-ignore-end -->

###### Problem Statement

Create Celtic knots with desired properties.

###### Brief

Celtic knots are common artistic knots. Exploring the creation of a unique rule set for creating
Celtic knots is an opportunity to develop a unique understanding of the diagrammatic nuances of knot
theory.

<!-- prettier-ignore-start -->
(sec-proj-diagram_att)=
##### Compute Diagram for General Notations: Intermediate Student
<!-- prettier-ignore-end -->

###### Problem Statement

Create an interface for plotting knots in an arbitrary notation in KnotPlot.

###### Brief

An aspect of knot theory that makes it among the most accessible higher math domains is the ability
for anyone to draw pictures of knots. A continuing theme of this thesis is that
computations/operations are easy by hand, with the qualifier "up to reasonable crossing number".
This carries through with the drawing of the diagrams. A common drawing tool in knot theory is
KnotPlot [@schareinInteractiveTopologicalDrawing1998], unfortunately KnotPlot has no interface for
drawing knots in "arbitrary" notations. The tool however, does have a Lua scripting interface in
which an arbitrary notation decoder can be designed.

##### Create VR Band Plumbing Visualizer: Upper Division Student

###### Problem Statement

Create a 3D VR visualizer for the band plumbing construction for arborescent knots.

###### Brief

The plumbing construction for arborescent knots and tangles is easiest visualized in 3D. The ideal
for visualizing these objects is in VR, as this reduces the need for spatial reasoning. While the
theory exists for creating the objects, the linear algebra required makes this an upper division
problem.

<!-- prettier-ignore-start -->
(sec-projs-invariants)=
#### Invariants
<!-- prettier-ignore-end -->

One way to build conjecture is by the analysis of patterns in data, these conjectures often lead to
the development of new theory. Problems in this section create the collections of data that can be
used for developing those conjectures and theories.

<!-- prettier-ignore-start -->
(sec-proj-homflypt)=
##### Compute Polynomial From A Tangle Notation: Intermediate Student or Upper Division Student
<!-- prettier-ignore-end -->

###### Problem Statement

Develop the theory needed for efficiently computing polynomials of tangles

###### Brief

One of the most important advancements in knot theory was the discovery of knot polynomials as a
class of knot invariants. As an example, one of the most powerful of these polynomials is the
HOMFLYPT polynomial [@freydNewPolynomialInvariant1985] constructed from the skein relations equation
@fig-future_work-skein_homfly.

```{math}
\begin{aligned}
    P\LP\text{unknot}\RP&=1\\
    \ell P\left(L_{+}\right)+\ell^{-1} P\left(L_{-}\right)+m
    P\left(L_0\right)&=0\\
  \end{aligned}
```

Conveniently, the data needed to apply the skein relations is precisely the data encoded by RLITT,
relative crossing data.

```{figure} ../../media/Skein_HOMFLY.svg
:label: fig-future_work-skein_homfly
The skein
    relation for the HOMFLYPT polynomial.  (Public domain, via
    Wikimedia Commons [@pbroks13SkeinHOMFLYPublic2008])

```

Depending on the polynomial selected, the problem is appropriate for intermediate students or upper
division students. When the polynomial has a developed tangle theory, the solution will have a well
defined start and end point and is appropriate for intermediate students. Otherwise, the full tangle
theory must be developed. This requires experience with the development of original abstract theory,
making the problem appropriate for upper division students.

##### Compute Finite Type Invariant From A Tangle Notation: Intermediate Student or Upper Division Student

###### Problem Statement

Develop the theory needed for efficiently computing a finite type invariant of tangles

###### Brief

Similar to the computation of polynomial invariants the computation of finite type invariants
expands our table with data useful for binning future tangles and knots. Depending on the invariant
selected, the problem is appropriate for intermediate or upper division students. When the invariant
has a developed tangle theory the solution will have a well defined start and end point and be
appropriate for intermediate students. Otherwise, the full tangle theory must be developed. This
requires experience with the development of original abstract theory, making the problem appropriate
for upper division students.

<!-- prettier-ignore-start -->
(sec-proj-notations)=
#### Notations
<!-- prettier-ignore-end -->

There are many ways to encode the data of a knot, each with advantages and disadvantages. Throughout
this thesis, the primary target notation was the RLITT @subsec-rlitt. This subsection discusses
several useful notations where a computational tool translating from and to RLITT is desired. Since
the source and destination notation in each problem are well understood each is appropriate for
intermediate students.

<!-- prettier-ignore-start -->
(sec-proj-note_gauss)=
##### Notation Description for Extended Gauss Notation: Intermediate Student
<!-- prettier-ignore-end -->

###### Problem Statement

Develop the theory translating RLITT to extended Gauss notation. Additionally, develop the software
needed for storing and translating per theory.

% prettier-ignore-start (sec-proj-note_pd)=

##### Notation Description for Planar Diagram (PD) Notation: Intermediate Student

% prettier-ignore-end

###### Problem Statement

Develop the theory for translating RLITT to PD notation. Additionally, develop the software required
for storing and translating per theory.

% prettier-ignore-start (sec-proj-note_dt)=

##### Notation Description for DT Notation: Intermediate Student

% prettier-ignore-end

###### Problem Statement

Develop the theory for translating RLITT to DT notation. Additionally, develop the software needed
for storing and translating per theory.

<!-- prettier-ignore-start -->
(sec-proj-gen)=
#### Generation
<!-- prettier-ignore-end -->

% prettier-ignore-end

This section expands the census of tangles to more abstract classes. These expanded lists increase
accessibility of complex objects allowing for the creation of new theory.

##### Create a table of virtual tangles: Upper Division Student

###### Problem Statement

Create the theory needed to construct a table of virtual tangles.

###### Brief

Virtual knots, developed by Kauffman [@kauffmanVirtualKnotTheory1999], are an extension of the knot
concept where a knot shadow need not be planar. Some work has been done on classifying the virtual
tangles by Mellor and Nevin [@mellorVirtualRationalTangles2020]. The full tangle theory must be
developed to solve this problem. This requires experience with the development of original abstract
theory, making the problem appropriate for upper division students

##### Create a table of $n$ string tangles: Upper Division Student

###### Problem Statement

Create the theory needed to construct a table of $n$ string tangles.

###### Brief

The tangles we have worked with in this thesis are the two string tangles, those with four fixed
points on the Conway circle. A natural extension to this concept is the $n$ string tangle. Recently,
Kwon [@kwonClassificationRational3tangles2025], the 3 strings rational tangles, have been
classified. For the remaining cases, the full tangle theory must be developed to solve the problem,
this requires experience with the development of original abstract theory, making the problem
appropriate for upper division students

<!-- prettier-ignore-start -->
(sec-proj-pot)=
#### Potpourri
<!-- prettier-ignore-end -->

Problems in this section are those that do not fit into other classes of problems.

<!-- prettier-ignore-start -->
(sec-proj-rand)=
##### Random Tangle Sampling: Upper Division Student
<!-- prettier-ignore-end -->

###### Problem Statement

Create the theory and software to select from a collection or generate a tangle at random with an
understood distribution.

###### Brief

In the introduction chapter @sec-intro-applications, applications of knots to the hard sciences were
discussed. When working in the hard sciences, being able to sample with an understood distribution
from a collection is important. Similarly to the previous notational projects, describing and
implementing random sampling methodologies is a class of extremely useful tabulation projects. The
full tangle theory must be developed to solve this problem. This requires experience with the
development of original abstract theory, making the problem appropriate for upper division students

##### Develop a tangle analogue for petal knots: Upper Division Student

###### Problem Statement

Create the theory needed for a well defined tangle analogue of the petal
knots[@adamsKnotProjectionsSingle2015].

###### Brief

Petal knots, first developed by Adams [@adamsKnotProjectionsSingle2015], are knots in which all
crossings are collinear in the orthogonal projection, an "ubercrossing". Converting these objects to
a braid is straightforward, however less obvious is converting to a two string tangle. Identifying a
tangle analogue for the petal knots may allow for computation of a whole new family of tangle data.
The full tangle theory must be developed to solve this problem. This requires experience with the
development of original abstract theory, making the problem appropriate for upper division students

[^pot]: Definition: A miscellaneous collection
