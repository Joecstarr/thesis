The second stage of software product development is the software engineering
process. Just as in the product management section (@sec-product-management), we
are approaching the software engineering process from an undergraduate training
perspective. However, unlike our discussion of general product management, we
assume some prior knowledge of software practices. With this in mind, we will
focus on engineering processes needed for our tangle tabulation, omitting
discussion of programming practice itself.

Before development can begin, we must define the steps we will take and any
quality gates[^gate] that need to be satisfied before moving between those
steps. We call this collection of steps and transitions a **software life
cycle**. There are several popular patterns defining a software life cycle. The
most common in intustry are agile models such as extreme programming
[@beckExtremeProgrammingExplained2012] and scrum [@nonakaNewNewProduct1986].
Less common by historically relevent are linear models such as the
waterfall[@beningtonProductionLargeComputer1983] or the V
model[@forsbergRelationshipSystemEngineering1991].

`````{prf:observation}
```{figure} ../../media/software/extreme_programming.svg
The extreme programing agile life cycle[@donwellsExtremeProgrammingsvg2010].
```
```{figure} ../../media/software/scrum_process.svg
The scrum agile life cycle [@lakeworksScrumProjectManagement2008].
```
````{figure} ../../media/software/waterfall_process.drawio.svg
The water process model. Note that the model allows no back tracking.
````
````{figure} ../../media/software/v_process.drawio.svg
The v process model.
````
Life cycle diagrams of two agile and two linear process models.
`````

Agile process models allow tight feedback loops which ensures the product meets
the needs of stakeholders, this reduction of risk makes agile methods popular in
industry. In a research context, by the time product software is being written,
requirements and expectations for the software are necessarily fully understood
and well-defined. Consequently, and contrary to industry trends, linear models
are the most appropriate for research contexts. While researchers are expected
to define well-considered requirements, as amateur software engineers, it is
rare that the design and programming techniques are mature enough to support the
strict progression of a waterfall process. As such, a V model where downstream
phases feedback into previous phases is ideal. We will, however, make a single
change by disallowing changes in requirements caused by down stream phases
(@se-fig-modifiedv).

```{figure} ../../media/software/v_mod_process.svg
:label: se-fig-modifiedv
The feature v process model.
```

Research problems like those found in tabulation have clear delineations between
problem statements. For example, in the tabulation of tangles we have seen in
the previous chapters, each problem has two parts:

1. The combinatorial notational strategy
2. The generation algorithm

The modified V model (@se-fig-modifiedv) is easily parallelized as in
@se-fig-modifiedmultiv. The parallelizability allows for this process to be
scaled for use by any size of research team. Allowing the process to be utilized
by individual researchers at primarily undergraduate institutions or large
REU[^reu] projects.

```{figure} ../../media/software/v_multi_process.svg
:label: se-fig-modifiedmultiv
The feature v process model.
```

In the remainder of the section, we will describe each phase of the modified v
model. In each subsection, we will describe what activities should be carried
out as well as an overview of what, if any, diagrams we should expect to be
created in each phase. The diagrams we will discuss are non-standard
simplifications of standard UML [@UnifiedModelingLanguage2017] diagrams. Through
all the subsections, we will use the game of "go fish" as an example. Since the
rules of "go fish" are highly non-standard, we will use the rules defined by
Parlett [@parlettPenguinBookCard2009] as a common base.

### Requirements

Requirements define the conditions and behaviors that are expected out of a
system. Writing specific and non-ambiguous requirements is a surprisingly
difficult task, for example, when writing a set of requirements for "go fish" we
may define a requirement such as @se-fig-bad_req.

```{prf:example}  AS requirement for a fishing action
:label: se-fig-bad_req
At the beginning of the active player's turn that player shall request a
card from any other player.
```

```{note}
Observe the indicative mood used in @se-fig-bad_req. The indicative mood, such
as the use of "shall" helps the designer reduce ambiguity.
```

On its face, @se-fig-bad_req seems to be a perfectly good requirement phrasing
the "fishing" phase of a turn. However, if you put yourself in the shoes of a
person who has never player "go fish" you might be confused by how to ask for a
card. Can the active player as for a $10$ or should they ask specifically for a
$10\heartsuit$? Fixing this ambiguity in @se-fig-bad_req can by done as in
@se-fig-bad_req_fixed.

```{prf:example}  An updated requirement for a fishing action
:label: se-fig-bad_req_fixed
At the beginning of the active player's turn that player shall request a
card, by rank and suit, from any other player.
```

In a research context, the phrasing of a requirement as in @se-fig-bad_req_fixed
is often redundant. Most pieces of software in a rigorous mathematical context
will inherently have theorems and definitions that unambiguously define what the
software should do. This means we must change how we think about requirements in
the research setting. Instead of requirements of the style of
@se-fig-bad_req_fixed we phrase requirements as **use cases**.

```{prf:definition} A use case [@pressmanSoftwareEngineeringPractitioners2015a]
A **use case** tells a stylized story about how an end user (playing one of a number
of possible roles) interacts with the system under a specific set of
circumstances. The story may be narrative text, an outline of tasks or
interactions, a template-based description, or a diagrammatic representation.
```

In this context, we may rephrase @se-fig-bad_req_fixed as a use case, such as
@se-fig-use_case.

```{prf:example} A usecase for a fishing action
:label: se-fig-use_case
A player asks another player for a specific card (rank and suit).
```

A use case is phrased for behavior in a research context should appear as a
close to lay retelling of the rigorous theoretical requirements.

#### Use Case Diagram

One popular way to phrase and visualize use cases is a use case diagram
[@UnifiedModelingLanguage2017]. In a use case diagram, you show the connections
between actors (Player and Dealer in @se-ex-usecase) and use cases (oval cells
in @se-ex-usecase). When an actor is connected to a use case, we interpret that
connection as the user being able to initiate that use case. In @se-ex-usecase
we have one more type of connection, the "include" connection. When a use case
is connected to another use case with an "include" connection, we interpret the
child (further from the actor by graph distance) as being a separate behavior
started by the parent use case. This "include" relationship is useful for
generalizing behavior, we see this as the "matching" use case is included in
both the "fishing" and "drawing" use cases.

````{prf:example} A use case diagram for go fish
:label: se-ex-usecase
```{mermaid-p}

flowchart LR

    player["Player fa:fa-user"]
    dealer["Dealer fa:fa-user"]
    P1([Fishes for a card])
    P2([Matches four cards<br> into a 'book'.])
    P3([Draw a card from the deck])
    D1([Shuffle the deck])
    player --> P1
    player --> P3
    dealer --> D1
    P1 -. include .-> P2
    P3 -. include .-> P2

```
````

### Software Design

After expectations of a system are set in the requirements phase, we can
decompose the problem into a software design, Pressman
[@pressmanSoftwareEngineeringPractitioners2015a] outlines eight principles
(@se-def-8core) that guide this process. This decomposition, tells us how to
break the software into discrete pieces of functionality called **units**.
Depending on the team and their needs, a unit can be sized anywhere between a
single function and a collection of files.

```{prf:definition} Eight Core Principles to Fundamental Softare Engineering [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-8core
1. Divide and conquer: You should break a hard problem into smaller solvable
   problems where possible.
1. Understand the use of abstraction: Solving your problem is good, solving a
   more general version of your problem is better. Write software that hits the
   "sweet spot" of generality, not too general that it's hard, not to
   specialized that you can't use it again.
1. Strive for consistency: It's easier to use/build intuition when choices are
   consistent. When you open a textbook, why is it easy to find the index?
   Because they are consistently in the same location.
1. Focus on the transfer of information: Software, at its most basic, is about
   manipulating data. Understanding where that data moves and how it's consumed
   is key to understanding a problem.
1. Build software that exhibits effective modularity: When decomposing a problem
   as in (1), the smaller problems should have low coupling @se-def-coup and
   high cohesion @se-def-coh.
1. Look for patterns: Look for ways common design patterns @se-def-designpat can
   be used to solve the problem.
1. When possible, represent the problem and its solution from a number of
   different perspectives: It's often the case that the first solution (obvious
   solution) is not the best/ideal solution. Approaching a problem from many
   perspectives helps identify alternative solutions.
1. Remember that someone will maintain the software: Be kind to future you.
   Spend an hour now to save days later.
```

```{prf:definition} Coupling [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-coup
**Coupling** is a qualitative measure of the degree to which units are
connected to one another. As units become more interdependent, coupling
increases.
```

```{prf:definition} Cohesion [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-coh
Within the context of unit-level design for systems, **cohesion** implies that a
unit encapsulates only attributes and operations that are closely
related to one another and to the unit itself.
```

````{prf:definition} Design Pattern [@pressmanSoftwareEngineeringPractitioners2015a]
:label: se-def-designpat
A **design pattern** is an abstraction that prescribes a design solution to a
specific, well-bounded design problem. A design pattern saves you from
"reinventing the wheel," or worse, inventing a "new wheel" that is slightly out
of round, too small for its intended use, and too narrow for the ground it will
roll over.

```{prf:example} **Iterator Patern** [@gammaDesignPatternsElements1995]


**Intent**

Provide a way to access the elements of an aggregate objectsequentially without
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
````

#### Diagrams

##### Block Diagram

To diagrammatically represent a system design, we will utilize a modified block
diagram. This modified block diagram gives a high-level description of the
discrete units of a system design and how those units relate to each other. The
units are indicated as blocks containing a descriptive title. Units that satisfy
similar use cases and may be abstractable are grouped together in container
blocks. Connections between blocks are indicated with decorated arrows, the
decorations should indicate the relationship between components. Examples of
decorators may show multiplicity relationship, such as `1` for one-to-one
mapping, `1..*` for 1 to many, or `*..1` for many to 1.

````{prf:example} A block diagram for go fish
:label: se-ex-block
```{mermaid-p}

flowchart LR
    subgraph User Interface
        ui-hd["Hand Display"]
        ui-dd["Deck Display"]
        ui-ps["Player Score"]
    end

    subgraph Game Objects
        go-h["Hand"]
        go-d["Deck"]
    end

    gs["Game State"]

     go-h --->|*..1| gs
     go-d --->|1| gs
     gs --->|1| ui-hd
     gs --->|1| ui-dd
     gs --->|1..*| ui-ps

```
````

##### Sequence Diagram

When the system design must account for communication between units, a system
design may benefit from a sequence diagram. A sequence diagram records the
actions and data transfers that actors take during a use case. The diagram
encodes time on the vertical axis, actors as vertical lanes, and interactions as
arrows between lanes. Arrows are labeled with a description of the interaction
taking place. Conditional sequences are indicated by boxes around and splitting
the sequence of interactions.

````{prf:example} A sequence diagram for go fish turn
:label: se-ex-seq
```{mermaid-p}

sequenceDiagram
    participant o as Player 1
    participant t as Player 2
    participant d as Deck

    o ->> t: Asks for a card
    alt is negative
    t ->> o: Responds in the negative
    o ->> d: Requests a card
    d ->> o: Distributes a card
    else is positive
    t ->> o: Responds in the postive
    t ->> o: Distributes a card
    end

```
````

### Unit Design

As we proceed down the v model, we narrow our focus, progressively becoming less
abstract and more concrete in our representation of our system. The system
design gives us a description of what units we will need, but does not give an
actionable description of those units. A unit description gives that actionable
description, giving non-language specific but directly implementable
(programmable) descriptions for how a unit works.

A unit description should contain what data members (variables) and functions a
unit contains. This containment is described in two ways, first a plain English
description and second diagrammatically in a class diagram
[@UnifiedModelingLanguage2017]. A unit description should also describe what
that data or function is intended to do, this is again described in plain
English. In the case of function descriptions, a diagrammatic definition as a
state machine[@UnifiedModelingLanguage2017] should also be given.

#### Diagrams

##### Class Diagram

A class diagram [@UnifiedModelingLanguage2017], similar to a block diagram,
contains a collection of blocks and their relationships. In the case of a class
diagram, the blocks are functional subunits of a unit. Each block contains a set
of data members followed by a set of functions, type annotations are optional.
In an object aware language, such as Python or Java, a block might correspond to
a class in the language sense. In an imperative language, such as C, the blocks
may correspond to a `.c` or `.h` file. The members of the class are decorated
with $+$ to indicate public visibility, meaning the member can be seen and used
by other units. The members of the class are decorated with $-$ to indicate
private visibility, meaning the member can only be seen from inside the class.
When referencing other units in the system, the external units are truncated to
an empty block.

````{prf:example} A class diagram for a go fish player.
:label: se-ex-class

```{mermaid-p}
classDiagram
    Player <|-- Hand
    Player <|-- Book
    class Player{
        +Hand hand
        +List[Book] books
        +get_score()
        +go_fishing()
        +check_card_in_hand()
        -count_books()
        -make_books()
    }
    class Hand{
    }
    class Book{
    }

```
````

##### State Machine

A state machine [@UnifiedModelingLanguage2017] diagram describes the collection
of states and transitions that a function or system can move between. Each state
machine has two special states. The first special state is the start state,
indicated by a filled in circle. The second special state is the end state,
indicated by a filled in circle surrounded by a ring. Other states are indicated
by a box with text describing the state. Decision points are indicated with a
diamond with conditional transitions decorated with text.

````{prf:example} A state machine diagram for go fish turn
:label: se-ex-sm
```{mermaid-p}

stateDiagram-v2
    select: Select player to ask for a card
    fish: Ask player for a card
    match: Group hand into books
    rc: Receive a card
    dac: Draw card from deck
    state has_card <<choice>>

    [*] --> select
    select --> fish
    fish --> has_card
    has_card --> dac: Target player does not have card
    has_card --> rc: Target player has card
    dac --> match
    rc --> match
    match --> [*]

```
````

### Implementation

Once the unit design is complete, we are ready to implement (program) the unit.
There are no special activities in the implementation phase outside of
programming effort. It is important to strictly follow the unit and system
design in this phase. If deficiencies in design are found, the V model allows
for that feedback to be pushed up to earlier phases and addressed.

### Unit Testing

With implementation complete, we move to the right side of the V, which consists
of verification activities. The first verification activity is the isolated
verification of each unit, called **unit testing**. In this phase, we design and
carry out tests of the software we have implemented. When designing tests, it is
important to draw expectations from the unit design directly, instead of
designing tests against the actual implemented code. Testing the code against
the design ensures that we are not drawing the target around the arrow. Tests,
particularly unit tests can, and should, be separated into two classes of test.
The first class is the "happy path", these tests validate that "good"
well-formed input generates expected output, see @se-ex-happyut. The second
class is the "unhappy path", these tests validate that "bad" or malformed input
is handled as expected, see @se-ex-unhappyut. Each public, accessible to
external units, interface of a unit should have at least one unit test.

Through all the phases of the verification arm of the V model, we will utilize
test cards to define a set of requirements that a test will be implemented
against. Each test card has four fields with content as follows:

-   **Test Name**: The unique name for the test. This name is used in test
    reports to identify what has failed.

-   **Description**: The description of what the test is validating and how that
    validation works. This section may include text and diagrams.

-   **Inputs**: A set of inputs to feed the unit.

-   **Outputs**: The outputs that are expected when the inputs are fed to the
    unit.

```{prf:example} A happy path test card for a player turn in go fish
:label: se-ex-happyut
**Test Name**: Request a card, reponse is positive

**Description**: Active player requests a card from a target player. The target
player has the requested card and produces it.

**Inputs**:

-   A valid requested card
-   A valid target player with requested card in hand

**Outputs**:

-   Active player puts replied card in hand

```

```{prf:example} A unhappy path test card for a player turn in go fish
:label: se-ex-unhappyut
**Test Name**: Illegally request a card

**Description**: Active player requests a card that is not in their hand.

**Inputs**:

-   An invalid requested card

**Outputs**:

-   Active player is notified the request failed

```

### Integration Testing

It is very rare for a system to have a single unit or a collection of units that
are completely uncoupled. We defined the coupling in the system during the
system design phase, we call the process of sticking these coupled units
together, **integration**. We verified during the unit tests that implemented
units work individually as we expect, in integration testing we determine
whether implemented units work together as expected.

### Acceptance Testing

When we have completed unit and integration testing, we have verified that the
system doesn't unexpectedly break and satisfies written requirements (use
cases). However, we have not yet verified that the system satisfies what
stakeholders wanted. In our go fish example, this phase may include a
presentation to a customer. This is the point where a customer may find that our
interpretations of @se-fig-bad_req disagree, and we update to
@se-fig-bad_req_fixed.

[^gate]:
    A collection of quality goals that need to be satisfied to call a step
    "complete".

[^reu]:
    Research Experiences for Undergraduates, a program funded by the National
    Science Foundation (NSF).

[^ds]:
    A data structure describes how the data is represented and stored while
    being worked on by the computer.
