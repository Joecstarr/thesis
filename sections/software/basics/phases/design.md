<!-- prettier-ignore-start -->
(subsec-softearedesign)=
### Software Design
<!-- prettier-ignore-end -->

After expectations of a system are set in the requirements phase, we can
decompose the problem into a software design. Pressman and Maxim
[@pressmanSoftwareEngineeringPractitioners2015a] outline eight principles
(@se-def-8core) that guide this process. This problem decomposition tells us how
to break the software into discrete pieces of functionality called **units**.
Depending on the team, their needs, and the technologies they are using, a unit
can be sized anywhere from a single function to a collection of files.

```{prf:definition}Paraphrasing Pressman and Maxim, Section 7.2.2 [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-8core
1. Divide and conquer: You should break a hard problem into smaller solvable
   problems where possible.
1. Understand the use of abstraction: Solving your problem is good, solving a
   more general version of your problem is better. Write software that hits the
   "sweet spot" of abstraction. Software that is not too general that it's hard
   to use for your specifc needs, and not to specialized that you can't use it
   again for a similar problem.
1. Strive for consistency: It's easier to use/build intuition when choices are
   consistent. When you open a textbook, why is it easy to find the index?
   Because they are consistently in the same location.
1. Focus on the transfer of information: Software, at its most basic, is about
   manipulating data. Knowing where that data moves and how it's consumed
   is key to understanding and contextualizing a problem.
1. Build software that exhibits effective modularity: When decomposing a problem
   as in (1), the smaller problems should have low coupling (see @se-def-coup) and
   high cohesion (see @se-def-coh).
1. Look for patterns: Look for ways common design patterns (see @se-def-designpat) can
   be used to solve the problem.
1. When possible, represent the problem and its solution from a number of
   different perspectives: It's often the case that the first solution (obvious
   solution) is not the best/ideal solution. Approaching a problem from many
   perspectives helps identify alternative solutions.
1. Remember that someone will maintain the software: "Be kind to future you."
   Spend an hour now to save days later.
```

```{prf:definition} Paraphrasing Pressman and Maxim, Section 14.2.4 [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-coup
**Coupling** is a qualitative measure of the degree to which units are
connected to one another. As units become more interdependent, coupling
increases.
```

```{prf:definition} Paraphrasing Pressman and Maxim, Section 14.2.3 [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-coh
Within the context of unit-level design for systems, **cohesion** implies that a
unit encapsulates only attributes and operations that are closely
related to one another and to the unit itself.
```

```{prf:definition} Paraphrasing Pressman and Maxim, Page 349[@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-designpat
A **design pattern** is an abstraction that prescribes a design solution to a
specific, well-bounded design problem. A design pattern saves you from
"reinventing the wheel," or worse, inventing a "new wheel" that is slightly out
of round, too small for its intended use, and too narrow for the ground it will
roll over.

As an example we give a common design pattern the **Iterator Pattern**[@gammaDesignPatternsElements1995]:

**Intent**

Provide a way to access the elements of an aggregate object sequentially without
exposing its underlying representation.

**Motivation**

An aggregate object such as a list should give you a way to access its elements
without exposing its internal structure. Moreover, you might want to traverse
the list in different ways, depending on what you want to accomplish. But you
probably don't want to bloat the List interface with operations for different
traversals, even if you could anticipate the ones you will need. You might also
need to have more than one traversal pending on the same list.

The Iterator pattern lets you do all this. The key idea in this pattern is to
take the responsibility for access and traversal out of the list object and put
it into an iterator object. The Iterator class defines an interface for
accessing the list's elements. An iterator object is responsible for keeping
track of the current element; that is, it knows which elements have been
traversed already.

**Applicability**

Use the Iterator pattern:

-   to access an aggregate object's contents without exposing its internal
    representation.
-   to support multiple traversals of aggregate objects.
-   to provide a uniform interface for traversing different aggregate structures
    (that is, to support polymorphic iteration).

```

#### Diagrams

##### Block Diagram

To diagrammatically represent a software design, we utilize a modified block
diagram. A block diagram gives a high-level description of the discrete units of
a software design and how those units relate to each other. The units are given
by blocks containing a descriptive title. Units that satisfy similar use cases
and may be abstractable to a common design are grouped together in container
blocks (`User Interface` in @se-ex-block). Connections between blocks are
recorded with decorated arrows, the decorations indicate the multiplicity of the
relationship between components, such as `1` for a one-to-one, `1..*` for a 1 to
many, or `*..1` for a many to 1 mapping.

```{include} ./diagrams/block.md

```

##### Sequence Diagram

When the software design must account for communication between units, a
sequence diagram may be used. A sequence diagram records the actions and data
transfers that actors (units) take during a use case. A sequence diagram encodes
time on the vertical axis, with actors as vertical lanes. Interactions between
actors over time are indicated by annotated arrows between lanes. Arrow
annotations are a description of the interaction taking place. Conditional
sequences are indicated by boxes delimiting the possible sequences of the
interaction (`is negative` and `is positive` subsequences in @se-ex-seq).

```{include} ./diagrams/sequence.md

```
