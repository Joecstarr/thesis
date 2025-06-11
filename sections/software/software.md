---
title: Software and its Engineering
---

We now shift from the mathematical world to the world of computers and software.
We start with a brief overview of product management and software engineering.
The overview includes the definitions of concepts and terms needed for modeling
of a software process to be paired with the knot theory software toolbox. With
the design goal of use in professional and undergraduate research projects.
Next, we summarize what features we should look for in knot theory software and
give an architectural design against those features for a general Knot Theory
Software Toolbox. Finally, using this architecture, we present documentation for
how the tabulation theory of @ch-tabulation is translated to software.

```{include} ./basics.md

```

<!-- prettier-ignore-start -->
(sec-surveyoftools)=
# Survey of Knot Theory Software Tools
<!-- prettier-ignore-end -->

In this section, we explore what the strength and weaknesses of some tools
currently in use in the computational knot theoretic space.

## KnotPlot

KnotPlot[@schareinInteractiveTopologicalDrawing1998] is a closed source[^closed]
knot computation tool primarily used for diagramming knots. Knotplot was
developed as a portion of Robert Scharein's PhD thesis
[@schareinInteractiveTopologicalDrawing1998], he is the primary maintainer. The
primary interface for KnotPlot is by interacting with a GUI. This makes the
onboarding process for non-technical users straightforward and the learning
curve shallow. KnotPlot has recently added a programmatic interface allowing
general scripting in the programming language Lua. This scripting interface
allows for custom diagramming and input output components. These custom scripts
are limited however by the hooks into KnotPlot. It is not always clear what
calls to make into KnotPlot to accomplish your goals. Additionally, since the
scripting interface is compiled into KnotPlot and isn't a language widely used
in research, the environment becomes a walled garden that can be difficult to
build into a tool chain.

## Mathematica Libraries

<!-- (Mathematica https://katlas.org/wiki/Printable_Manual) -->

KnotTheory [@bar-natanKnotTheory] and LinKnot [@jablanLinKnotKnotTheory2007] are
collections of knot theory operations and datasets that can be used with the
Wolfram Mathematica system. Both KnotTheory and LinKnot are open source[^open]
and available for download. Mathematica is a natural environment for mathematics
research, the language syntax is similar to written theoretical mathematics.
This appearance lowers the difficulty of learning to use the tooling. The
interfaces defined by both KnotTheory and LinKnot are natural in the Mathematica
context, further shallowing the learning curve for use. Additionally, both
collections are well documented in the "knot atlas" and text "LinKnot" for
KnotTheory [@bar-natanKnotTheory] and LinKnot [@jablanLinKnotKnotTheory2007]
respectively. Unfortunately, neither collection is published under version
control and neither collection appears to be under active development or
maintenance, with last published versions from $2016$ and $2011$. Without
visible versioning, tracing bugs becomes difficult. Compounding this difficulty,
neither collection has published test suites, making program correctness
something that must be considered when using the collections.

<!-- prettier-ignore-start -->
(sec-surveyoftools-snap)=
## SnapPea/SnapPy
<!-- prettier-ignore-end -->

SnapPy [@SnapPy] is a python wrapper for SnapPea, a collection of C libraries.
Both SnapPy and SnapPea are open source and published in the same GitHub
repository, including test suites. SnapPy's python bindings allow researchers to
leverage the massive python ecosystem, allowing for wide and varied usage, from
GUI tools to draw knots to webapps to do knot computations. Decoupling the core
logic from the interface layer allows for fast execution of the SnapPea C code,
but simple supportable python bindings for users finding a happy medium between
speed and ease of use. The SnapPea layer, however, is designed on an ad hoc
basis, meaning if a developer wants to reuse the C layer they must reverse
engineer the structures they wish to reuse.

# Architecture of A Knot Theory Software Toolbox

We will now detail the documentation generated during an abbreviated process
model described in @sec-life-cycle, we will carry out only the left side of the
V and in gross detail.

## Requirements

In @sec-surveyoftools we discussed prior art in the knot computation space, we
can use that analysis to define the goals of our Software Toolbox. First, we
would like our system to be easy to use. As we saw, easy to use can encompass
various possibilities. We can capture all of these possibilities by decoupling
the theoretical functionality from the user interfaces, and instead we will
implement specific interfaces for specific users.

```{requirement} User Interface Goals
The system shall not couple functionality to user interface.

```

This design goal allows the interface to be a Jupyter notebook during
undergraduate knot theory class, a Mathematica library for research, or a tool
run on a university cluster for high-performance needs. With any possible target
environment, the system must not be coupled to a particular platform (windows,
linux, etc.), informing our second requirement.

```{requirement} Portability Goals
The system shall be platform (OS, language, toolchain, I/O[^io]) agnostic.
```

The tools we saw in @sec-surveyoftools are all what we may call monolithic.
Meaning, from a development perspective, if the tool is to be used as a
component in a new system the whole tool must be included. In general, it is
preferable to include only the functionality a system actually needs. For
example, consider a system is being built to teach a seminar on constructing the
Jones polynomial. That system will need to include a Jones polynomial component.
Pulling in a hyperbolic volume component serves no purpose, needlessly
increasing the complexity of the system. These extensibility goals inform a
encapsulation design goal.

```{requirement} Encapsulation Goals
System use cases shall be encapsulated into feature components.
```

Encapsulating each feature allows for the system components to be used by
developers to build projects. However, as we saw in our discussion of SnapPy
(@sec-surveyoftools-snap), encapsulation itself does not remove all difficulty
in reuse. We can further lower the difficulty of reuse by increasing commonality
between components without coupling the components. This is accomplished by
ensuring that every system component adheres to a set of common design patterns.

```{requirement} Pattern Goals
System use cases shall adhere to a set of design patterns.
```

Finally, we can further reduce the overhead of reuse we enforce a common
development process on system components.

```{requirement} Documentation Goals
System use cases shall be documented and planned as outlined by the modified V
model (@sec-life-cycle).
```

## System Design

With a set of requirements for our design, we can now describe a system design.
Each requirement can be partitioned into one of two classes of requirement,
functional or non-functional. Where, a functional requirement can impact the
implementation of code and a non-functional requirement cannot. We start by
addressing a system design for the non-functional requirements:

-   User Interface Goals
-   Portability Goals
-   Documentation Goals

The user interface goal is satisfied by simply excluding any user interface
design from the system. The portability goal tells us that we need to pick a
technology stack that is supported on the maximal number of platforms. The clear
choice is to implement the system in the C language. The C language is widely
used, and a C compiler exists to target just about any platform. The following
is a selection of C compilers and tool chains and their targets:

-   Cython[@behnel2011cython]: "Cython is a Python compiler that makes writing C
    extensions for Python as easy as Python itself. Cython is based on Pyrex,
    but supports more cutting edge functionality and optimizations." - Cython
    Documentation
-   GNU[@GCCGNUCompiler2025]: A C compiler that can has around 200 targets
    including
    -   x86_64
    -   ARM
    -   Motorola 68000
    -   PowerPC
-   Emscripten[@zakaiEmscriptenLLVMtoJavaScriptCompiler2011]: Compiles C to
    WebAssembly[@WebAssemblyCoreSpecification2] allowing for C code to be used
    in web systems.
-   Embedded compilers: Various compilers for esoteric embedded systems.[^emb]

Selecting C for an implementation language has some consequences. The main
consequence is caused by the low-level[^high-level] nature of C. As a low-level
language, C has no built-in garbage collection mechinism, that is, memory can be
allocated but is not unallocated automatically. To mitigate this risk in C
development we disallow memory allocation in our components. Any memory
allocation must happen in the user interface layer then buffers with known size
are to be passed to the components.

To address the two remaining functional requirements, Encapsulation Goals and
Pattern Goals, we define a collection of generic components called interfaces
that cover common use cases as well as a block diagram demonstrating the
relationship between the interfaces. To give our interfaces an appropriate
scope, that is, an appropriate encapsulation of a component, we must identify
common use cases for a knot theory system. Our common use cases are as follows:

-   Runner: The runner use case serves as the stand-in for user interfaces.
    Since we are decoupling the interface from the functionality, there is no
    further design consideration for the runner use case.
-   Runnable Use Cases: Runnable use cases serve as the functionality that is
    called by an external runner.
    -   Computation: The computation use case is a runnable that operates in a
        one call, one return flow. Example: Compute Jones Polynomial and Compute
        Writhe.
    -   Generator: The generation use case is a runnable that operates in a one
        call, multiple return flow. Example: Generate rational tangles, Generate
        Montesinos tangles, and Generate arborescent tangles.
-   Data Wranglers: Data Wrangler use cases serve as a non-user facing layer
    used by runnables to handle data.
    -   Notation: The notation use cases define data structures used to
        represent knot data. Additionally, the use case describes the
        translation between string representations and data structures. Example:
        Conway notation, Algebraic tangle tree notation, and Weighted planer
        tree notation.
    -   Storage: The storage use case serves the need for components to read and
        write from external systems. Examples: the command line or a database.

````{figure}
```{mermaid-p}
flowchart LR
    Runner
    subgraph "Runnables"
        Generator
        Computation
    end
    subgraph "Data Wranglers"
        Notation
        Storage
    end
    Runner -->|1..*| Generator
    Runner -->|1..*| Computation
    Runner -->|1..*| Notation
    Generator -->|1..*| Notation
    Computation -->|1..*| Notation
    Generator -->|1| Storage
    Computation -->|1| Storage
```
A block diagram of the architecture of a knot theory software toolbox
````

```{include} ./documentation/interfaces/interfaces.md

```

# Unit Design for Tangle Tabulation

```{include} ./documentation/core_libraries.md

```

[^closed]:
    Closed source software is a software product with no published source code.

[^open]:
    Open-source software is a software product with publicly published source
    code.

[^io]: Input and Output
[^emb]:
    An embedded system is a small, usually low power, computer (microcontroller)
    that is built into a product. For example, the power seat of your car is an
    embedded system.

[^high-level]:
    A low-level language such as C or Rust compiles to machine code that runs
    directly on the hardware. A high-level language is one that abstracts
    functionality away from hardware.
