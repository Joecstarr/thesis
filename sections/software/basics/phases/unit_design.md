<!-- prettier-ignore-start -->
(sec-product-unit-design)=
### Unit Design
<!-- prettier-ignore-end -->

As we proceed down the left side of the V model, we narrow our focus,
progressively becoming less abstract and more concrete in our representation of
our software. The software design gives us a description of what units we will
need, but does not give an actionable description of those units. A unit
description gives that actionable description, a language agnostic but directly
implementable (programmable) description for what a unit contains and how a unit
works.

A description for a unit contains the data members (variables) and the
functional members a unit contains. Each of these items is described in two
ways, first a plain English description, and second included diagrammatically in
a class diagram [@UnifiedModelingLanguage2017] for the unit. The plain English
description for each member describes what that member is intended to be or do.
In the case of functional memember, along with an English description, a
diagrammatic definition as a state machine[@UnifiedModelingLanguage2017] should
also be given.

As with the the special language/mood used when designing requirements
(@subsec-requirements), documentation at the unit level and below have a
particular frugal and direct style. When this style is first encountered it can
be jarring, and the writing appear shockingly poor. However, just as the use of the
indicative mood in requirements encourages precision, the style of documentation
at this level serves a purpose. Documentation at this level is not intended to
tell a story or describe a problem, but to directly define a computational unit
one layer of abstraction above code. Simple direct language here encourages the
clear communication of expectations and intents that translate to code.
Complicated ideas, at this level, are easier to express (and consume) when
presented diagrammatically. Our English descriptions serve simply to supplement
the diagrams.

```{note}
Writing long, elaborate explanations at the unit level should prompt you to
engage in analysis of your design. The need for explanations like this
often indicates you are missing something at the software design level, look for
missing abstraction or a place to divide and conquer.
```

#### Diagrams

##### Class Diagram

$\,$

A class diagram [@UnifiedModelingLanguage2017], containing a collection of
blocks and their relationships, similar to a block diagram. However, in a class
diagram, the blocks are functional subunits of a unit. Each block contains a set
of data members followed by a set of functional members. In an object aware
language, such as Python or Java, a block might directly correspond to a class
in the language sense. In an imperative language, such as C, the blocks may
correspond to one or more `.c` or `.h` files.

Each member of the class is decorated to indicate public or private visibility,
meaning, visibility to the world outside the unit. A $+$ is used to indicate
public visibility, meaning the member can be seen and used by other classes, and
a $-$ to indicate private visibility, meaning the member can only be seen from
inside the class. When referencing other units in the system, the external units
are truncated to an empty class (the `Card` class in @se-cd-fig-agg). One or
more optional decorators can be added to a class to further contextualize the
class. The decorators that we allow in a class diagram are:

1. Enumeration: Indicating the class is an enumeration.
1. Interface: Indicating the class is an interface. This is usually used to
   simplify the diagram when common collections of data/functions need to be
   repeated.
1. External: Indicating the class is defined outside the current unit.

The relationships between classes are described by arrows between those classes.
Each type of arrow used in a class diagram defines a slightly different type of
relationship. The arrows that we will allow in a class diagram are the
aggregation (@se-cd-fig-agg) and the realization (@se-cd-fig-real). The
aggregation connection describes the relationship when one class uses
(aggregates) the connected class. In @se-ex-class, a class diagram for a Go Fish
player, we see the `Player` class using (aggregating) the `Hand` class. In
@se-cd-fig-real we see the realization connection, which describes the
relationship when a class implements an interface. An example can be seen in
@se-ex-class with the `Hand` and `Book`[^book] classes realizing the
`CardCollection` interface. Both the `Hand` and `Book` classes are collections
of multiple cards and will need common data, such as a function to print all
cards in the collection. This common (expected) data is modeled as an interface
that can be reused without needing to be rewritten.

```{note}
In some object-oriented languages, this relationship may be defined by an
inheritance or inheritance. However, in languages that are not object oriented
such as C, we instead define this common set of data as an abstract interface
for design purposes that we must implement in each component that realizes the
interface.
```

```{include} ./diagrams/class.md

```

##### State Machine

A state machine [@UnifiedModelingLanguage2017] diagram describes the collection
of states and transitions that a function can move between. When defining a
state machine, we start with two special states. The first special state is the
start state, indicated by a filled in circle, and the second special state is
the end state, indicated by a filled in circle surrounded by a ring. Other
states are recorded by a box with text describing the state. Decision points are
documented with a diamond, with each path of the condition decorated with text.

```{include} ./diagrams/state-machine.md

```

[^book]:
    A book is the matched sets of cards that are counted at the end of Go Fish
    to determine the winner.
