<!-- prettier-ignore-start -->
(sec-future_work-tabulation)=
## Tabulation as Undergraduate Research
<!-- prettier-ignore-end -->

### A Research Experience Program for Undergraduates

The accessibility of knot theory was discussed in @sec-intro-intuit_knot_theory.
This section elaborates on how that accessibility can be leveraged to engage
undergraduates in research. Throughout this thesis, we have investigated and
observed the depth and complexity of tabulation. We have seen how easily
portions of complex tabulation problems can be "peeled off" and decomposed as
self-contained problems. Additionally, we discussed product management training
(@sec-product-management) and developed a software enginering life cycle
(@sec-life-cycle) for use in organizing undergraduate research. These self
contained problems combined with our processes, produce a research experience
program ideal for undergraduates. The research experience program can be
enhanced by sequencing problems with a gradual release of responsibility model
as described by Fisher and Frey [@fisherBetterLearningStructured2013].

We now outline a multi-semester program for training of undergraduates,
beginning when those students have only lower division (college algebra level)
maturity. To begin, we engage in directed reading with low level accessible
texts such as this thesis or The Knot Book: An Elementary Introduction to the
Mathematical Theory of Knots by Adams [@adamsKnotBookElementary2004]. When the
student has gained a basic understanding of knots, a structured play problem
(potentially non-original work) can be introduced. Fitting the need here are
problems such as: the sculpting and 3D printing of stick knots[^stick] in a
program such as Blender or OpenSCAD @sec-proj-sticks, the creation of knot
mosaics @sec-proj-mosaic, or quilting Celtic knots @sec-proj-quilt. The goal of
such an activity is to build wonder and cultivate confidence in the students
investigation skills.

As the student matures, their investigation skills improve, and their
knowledgebase deepens, they can be presented with more complex reading and novel
research problems. Depending on the student's interest, we present additional
but more advanced readings such as LinKnot [@jablanLinKnotKnotTheory2007] or
accessible research papers such as Burton [@burtonNext350Million2020]. We should
encourage freedom in these readings, allowing students to select sections and
formulate questions of their own. At this level, problems should still be well
structured having a clear path from start to finish but requiring the filling in
of gaps with original work. We should consider problems such as the translation
of notations as in @sec-proj-notations, or the computation of a well understood
invariant, as in @sec-projs-invariants.

The program culminates with a mature undergraduate researcher ready to tackle
complex problems. At this point we expect the student to have mature reading and
reasoning skills, but perhaps lack skills such as literature review. Support for
reading at this stage should be focused on assisting students in finding answers
rather than answers being provided. Students may be prepared to formulate a
research question of their own and this should be encouraged; however presenting
students with ideas to build on or select from is beneficial. An ideal problem
here should fit student's interests and have a clear goal but perhaps no clear
starting point, for example the random tangle sampling seen in @sec-proj-rand.

### Infrastructure of a Tabulation Program

One key issue that must be addressed in a tabulation research program is
computational needs. Computing on knots and tangles is not necessarily a
computationally challenging task. Many problems are simple to describe
computationally and have efficient implementations. The primary challenge for
tabulation research stems from the raw scale of the dataset, as both the knot
and tangle datasets grow exponentially. This exponential growth of the data
gives us two primary areas of concern, time to compute and space to store. Even
if a problem has a nice constant time or linear time solution, doing a
computation on every knot or tangle in our dataset turns the problem into an
exponential one, a computational "death by a thousand cuts".

Generally when research questions run up against computational time constraints,
solutions take one of two forms, vertical scaling or horizontal scaling. We will
explain the two by analogy. Imagine we are trying to move a large boulder with a
bulldozer that is just not powerful enough for the job. We can trade in our
bulldozer for a bigger more powerful bulldozer that will push the rock without a
problem, this would be vertical scaling. Alternatively, we can blow up the
boulder and trade in our bulldozer for multiple smaller bulldozers, each able to
simultaneously move bits of the boulder, this would be horizontal scaling. In
our tabulation case, we could feasibly use either solution. If we vertically
scale, we could complete each computation faster. This makes sense for some
computations where each computation is slow such as hyperbolic volume. For other
computations, like the grafting seen in @sec-rlitt-generation, each computation
requires such little computational effort we would quickly run up against data
retrieval bottlenecks. In cases like this, distributing the effort horizontally
means, with some infrastructure effort, on aggregate we have less idle time in
the system. Another key feature of horizontal scaling in our case is the common
availability of clusters, at primarily undergraduate institutions. These
primarily undergraduate institutions often have no access to the large super
computers available at large institutions.

The planning and design of infrastructure leads us to address the second
challenge, space to store data. We will touch on two points: first the actual
storage of the data, and second, accessing and adding to the dataset. As we have
discussed, knot and tangle data grows exponentially, as expected, the space
needed to store that data also grows exponentially. As a benchmark, we use
arborescent tangles and the space required to store them in their linearized
form (@sec-arborescent-linear).


| Tree Crossing Number | Projected Total Number of Tangles up to TCN | Projected Total Size of Notations up to TCN |
| :------------------: | :-----------------------------------------: | :-----------------------------------------: |
| 20                   | 20,178,846,455.0426                         | 744.93 GB                                   |
| 21                   | 77,404,113,447.2751                         | 3.02 TB                                     |
| 22                   | 296,920,571,662.606                         | 12.24 TB                                    |
| 23                   | 1,138,987,289,416.26                        | 49.59 TB                                    |
| 24                   | 4,369,161,597,793.56                        | 200.98 TB                                   |
| 25                   | 16,760,135,017,593                          | 814.55 TB                                   |
| 26                   | 64,292,004,387,526.9                        | 3.30 PB                                     |
| 27                   | 246,624,621,285,968                         | 13.38 PB                                    |
| 28                   | 946,053,943,972,148                         | 54.23 PB                                    |
| 29                   | 3,629,070,212,865,634                       | 219.77 PB                                   |

As we can see, the space required for storing tangles quickly becomes
large. For perspective, a basic storage solution holds at least two copies of
the data, meaning to store arborescent tangles up to 21 crossings, we need
$3\times4\text{TB}=12\text{TB}$ of disk space (using 4TB as it's a common disk
size). More robust would be a solution that allows for two drive failures such
as RAIDZ2, in this case, we require $\LP2+3\RP\times4\text{TB}=20\text{TB}$. At
approximately $\$15$ per TB, putting us at around $\$200$ for the basic solution
and $\$300$ for the robust solution. It's important to remember this is the
required space and cost to store only a sequential list of notations for tangles
as in @math-listoftangles making retrieval of a specific tangle difficult.

```{note}
:label: math-listoftangles
$\iota\LP\LP\LB 2\RB \LB \m 3\RB \RP1\RP\iota\LP\LP\LB 2\RB \LB 2\RB \m 1\RP1\RP\iota\LP\LP\LB 2\RB \LB 2\RB 1\RP1\RP\cdots$
```

To expand the list, we require infrastructure that allows for random access, the
ability to search the data, and the ability to add additional data. This will
require that the data be stored in a database system. Unfortunately, a database
does come with a downside, it increases the storage requirements for the data
with mandatory overhead. With an effective data model and some consideration of
what should be stored and what should be computed on demand, we can mitigate
some of this overhead. However, even at low crossing number $\leq 12$, we will
quickly run into storage issues as we complete undergraduate computation
problems.

We will now discuss the selection and design of a database for a table of
tangles. Our data will be used by undergraduates, so an ideal database system is
one with a data model that has a shallow learning curve. Additionally, our data
is largely non-relational, meaning we don't need a database system geared to
relational data. These two items make a noSQL database system ideal. Just as we
had options for vertical scaling and horizontal scaling for carrying out the
computations we have the same two options for serving our database. However, in
the service case our choice is significantly more clear. Based on the size of
our data if we select vertical scaling our cost for a server will be in the
$\$10k-\$20k$ (not including storage cost) range and we may still end up with
bottlenecks. Therefore, for our needs, horizontal scaling is ideal. In this case
we can use a few low-cost cloud servers to store portions of the data, with a
coordinator balancing load across the system. If we encounter a bottleneck,
instead of buying a whole new expensive server, we simply add another low-cost
server to our system. This horizontal scaling concept is called sharding, a
feature of MongoDB an ideal choice for our needs.

```{include} ./selection_projects.md

```

[^stick]: A stick knot is a knot made of straight lines of a unit length.
