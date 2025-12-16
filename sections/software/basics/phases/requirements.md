<!-- prettier-ignore-start -->
(subsec-requirements)=
### Requirements
<!-- prettier-ignore-end -->

Requirements define the conditions and behaviors that are expected out of a system. Writing specific
and non-ambiguous requirements is a surprisingly difficult task, for example, when writing a set of
requirements for "Go Fish" we may define a requirement such as @se-fig-bad_req.

````{prf:example} A requirement for a fishing action
:label: se-fig-bad_req

```{requirement} Player goes fishing
At the beginning of the active player's turn that player shall request a
card from any other player.

```
````

```{note}
Observe the indicative mood used in @se-fig-bad_req. The indicative mood, as in
the use of "shall," helps the designer reduce ambiguity by sharpening precision.
```

On its face, @se-fig-bad_req seems to be a perfectly good requirement phrasing the "fishing" phase
of a turn. However, if you put yourself in the shoes of a person who has never played "Go Fish," you
might be confused by how to ask for a card. Can the active player ask for a $10$, or should they ask
specifically for a $10\heartsuit$? Fixing this ambiguity in @se-fig-bad_req can by done by making
the requirement more precises @se-fig-bad_req_fixed.

````{prf:example} An updated requirement for a fishing action
:label: se-fig-bad_req_fixed
```{requirement} Player goes fishing
At the beginning of the active player's turn that player shall request a
card, by rank and suit, from any other player.
```
````

In a research context, the phrasing of a requirement, as in @se-fig-bad_req_fixed is often
redundant. Most pieces of software in a rigorous mathematical context will have backing from
theorems and definitions that unambiguously define what the software should do. This means we must
change how we think about requirements in the research setting. Instead of requirements of the style
of @se-fig-bad_req_fixed we phrase requirements as **use cases**.

```{prf:definition} Paraphrasing Pressman and Maxim, Page 149 [@pressmanSoftwareEngineeringPractitioners2015a]
A **use case** tells a stylized story about how an end user (playing one of a number
of possible roles) interacts with the system under a specific set of
circumstances. The story may be narrative text, an outline of tasks or
interactions, a template-based description, or a diagrammatic representation.
```

In this context, we may rephrase @se-fig-bad_req_fixed as a use case, such as @se-fig-use_case.

````{prf:example} A usecase for a fishing action
:label: se-fig-use_case
```{use-case} Player goes fishing
A player asks another player for a specific card (rank and suit).
```
````

#### Use Case Diagram

One popular way to phrase and visualize a collection of use cases is a use case diagram
[@UnifiedModelingLanguage2017]. A use case diagram shows the connections between actors (Player and
Dealer in @se-ex-usecase) and use cases (oval cells in @se-ex-usecase). When an actor is connected
to a use case, we interpret that connection as the user being able to initiate (kicking off the
story the use case tells) that use case. In @se-ex-usecase we have a connection between use cases,
the "include" connection, this connection models a use case initiating another use case. The
"include" relationship is useful for generalizing behavior, in @se-ex-usecase we see the `matching`
use case included in both the `fishing` and `drawing` use cases.

```{include} ./diagrams/use-case.md

```
