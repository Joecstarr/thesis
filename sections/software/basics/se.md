<!-- prettier-ignore-start -->
(sec-life-cycle)=
## Software Engineering and Life Cycle
<!-- prettier-ignore-end -->

The second stage of software product development is the software engineering
process. Just as in the product management section (@sec-product-management), we
are approaching the software engineering process from an undergraduate training
perspective. However, unlike our discussion of general product management, we
assume some prior knowledge of software practices. We assume familiarity with
programming, types of programming languages, and the basic structure of a
program. If the reader feels unprepared, they may find it useful to complete one
of the many free asynchronous online courses offered by major
universities[^online] and browse a standard intoduction to computation text such
as "Introduction to the theory of computation" by
Sipser[@sipserIntroductionTheoryComputation2013]. With this in mind, we will
focus on engineering processes needed for our tangle tabulation use case,
omitting discussion of the practice of programming itself.

We will first define what steps we will take as part of our model process and
any quality gates[^gate] to be satisfied before moving between those steps. We
call this collection of steps and transitions a **software life cycle**. Rather
than reinventing the wheel, we will build on top of an existing life cycle
model. There are several existing models available to us, the most common
processes used in industry are agile models such as extreme programming
[@beckExtremeProgrammingExplained2012] (@fig-extreme-model) and scrum
[@nonakaNewNewProduct1986] (@fig-scrum-model). Less common in industry but
historically relevant are linear models such as the
waterfall[@beningtonProductionLargeComputer1983] (@fig-waterfall-model) or the V
model[@forsbergRelationshipSystemEngineering1991] (@fig-v-model).

`````{figure}
```{figure} ../../media/software/extreme_programming.svg
:label: fig-extreme-model
The extreme programing agile life cycle[@donwellsExtremeProgrammingsvg2010].
```
```{figure} ../../media/software/scrum_process.svg
:label: fig-scrum-model
The scrum agile life cycle [@lakeworksScrumProjectManagement2008].
```
````{figure} ../../media/software/waterfall_process.drawio.svg
:label: fig-waterfall-model
The waterfall process model. Note that the model allows no back tracking.
````
````{figure} ../../media/software/v_process.drawio.svg
:label: fig-v-model
The V process model.
````
Life cycle diagrams of two agile and two linear process models.
`````

Agile processes have become ubiquitous in industry as they allow for tight
feedback loops which ensures the product meets the needs of stakeholders,
reducing the risk of misunderstandings. In a research context, by the time
product software is being written, requirements and expectations for the
software are necessarily fully understood and well-defined. Consequently, and
contrary to industry trends, linear models are the most appropriate for research
contexts. While researchers can be expected to define well-considered
requirements, as amateur software engineers, it is rare that the design and
programming techniques are mature enough to support the strict progression of a
waterfall process. As such, a V model where downstream phases feedback into
previous phases is ideal. For our model process, however, we will make a single
change, disallowing feedback caused by down stream phases to change
requirements, as seen in @se-fig-modifiedv.

```{figure} ../../media/software/v_mod_process.svg
:label: se-fig-modifiedv
The feature V process model.
```

Often software products are developed by teams of engineers. In these team
environments, it is important that the software process be easily parallelizable.
Our modified V model can be parallelized as in @se-fig-modifiedmultiv. Allowing
the process to be utilized by individual researchers at primarily undergraduate
institutions or large REU[^reu] projects.

```{figure} ../../media/software/v_multi_process.svg
:label: se-fig-modifiedmultiv
The feature V process model.
```

The remainder of this section describes each phase of our modified V model. In
each subsection, we will describe the activities that should be carried out
during that phase, as well as an overview of what, if any, diagrams we should
expect to be created. The diagrams we will discuss for each phase are
simplifications of standard UML [@UnifiedModelingLanguage2017] diagrams.
Throughout the phases, we will use an implementation of the game of "Go Fish" as
an example software product.

```{note}
Since the rules of "Go Fish" are highly non-standard, we will use the
rules defined by Parlett [@parlettPenguinBookCard2009, page 397] as a common base.
```

```{include} ./phases/requirements.md

```

```{include} ./phases/design.md

```

```{include} ./phases/unit_design.md

```

```{include} ./phases/implementation.md

```

```{include} ./phases/validation.md

```

[^gate]:
    A collection of quality goals that need to be satisfied to call a step
    "complete".

[^reu]:
    Research Experiences for Undergraduates, a program funded by the National
    Science Foundation (NSF).

[^online]:
    At the time of writing "Python for Everybody" by the University of Michigan
    is a great choice.
