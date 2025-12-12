
In @sec-surveyoftools we discussed prior art in the knot computation space, in
this section we utilize that analysis to design a software architecture for a
general knot theory software toolbox. To complete this design, we will execute
the first two phases of the modified V model we developed in @sec-life-cycle.

## Requirements

In this section we carry out the requirements phase of the modified V model. We
will create a set of requirements and use cases that model the expectations we
have for a general knot theory software toolbox. First, we would like our system
to be easy to use. As we saw, easy to use can encompass various possibilities.
We can capture all of these possibilities by decoupling the theoretical
functionality from the user interfaces, and instead we will implement specific
interfaces for specific users.

```{requirement} User Interface Goals
The system shall not couple functionality to user interface.

```

This design goal allows the interface to be a Jupyter notebook during
undergraduate knot theory class, a Mathematica library for research, or a tool
run on a university cluster for high-performance needs. With any possible target
environment as a goal, the system must not be coupled to a particular platform
(Windows, Linux, etc.), informing our second requirement.

```{requirement} Portability Goals
The system shall be platform (OS, language, toolchain, I/O[^io]) agnostic.
```

The tools we saw in @sec-surveyoftools are all what we may call monolithic,
meaning, from a development perspective, if the tool is to be used as a part in
a new system, the whole tool must be included. In general, it is preferable to
include only the functionality a system actually requires. For example, consider
a system is being built to teach a seminar on constructing the Jones polynomial.
That system will need to include a Jones polynomial component. Needing to pull
in at the same time a hyperbolic volume component that serves no purpose,
needlessly increasing the complexity of the system. These extensibility goals
inform an encapsulation design goal.

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

We now develop a collection of use cases that address the high-level behaviors
expected by the general knot theory software toolbox.

```{use-case} Use the software
A user interacts with the system.
```

```{use-case} Data is manipulated
Data in the system is manipulated into somthing different.
```

```{use-case} Data is created
New data in the system is created.
```

```{use-case} Data is written
Data is written down for future use.
```

````{figure}
```{mermaid}

flowchart LR

    player["User fa:fa-user"]
    P1([Use the software])
    P2([Data is manipulated])
    P3([Data is created])
    P4([Data is written])
    player --> P1
    P1 -. include .-> P2
    P1 -. include .-> P3
    P2 -. include .-> P4
    P3 -. include .-> P4

```
A use case diagram for the listed use cases.
````

<!-- prettier-ignore-start -->
(sec-system_design)=
## Software Design
<!-- prettier-ignore-end -->

With a set of requirements for our design, we can now describe a software
design. Each requirement can be partitioned into one of two classes of
requirements, functional or non-functional. Where, a functional requirement can
impact the implementation of code and a non-functional requirement cannot. We
start by addressing a software design for the non-functional requirements:

-   User Interface Goals
-   Portability Goals
-   Documentation Goals

The user interface goal is satisfied by simply excluding any user interface
design from the software. The portability goal tells us that we need to pick a
technology stack that is supported on the maximal number of platforms. The clear
choice is to implement the software in the C language. The C language is widely
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

Selecting C for an implementation language has some risks, primarily caused by
the low-level[^high-level] nature of C. As a low-level language, C has no
built-in garbage collection mechanism, that is, memory can be allocated but is
not unallocated automatically. To mitigate this risk in C development we
disallow memory allocation in our components. Any memory allocation must happen
in the user interface layer, and then buffers with known sizes are passed to the
components.

To address the two remaining functional requirements, encapsulation goals and
pattern goals, we define a collection of generic component interfaces that cover
common use cases we described in the previous section. We also model these
interfaces as a block diagram demonstrating the relationship between the
interfaces.

-   Runner: The runner interface serves as the stand-in for user interfaces.
    Since we are decoupling the interface from the functionality, there is no
    further design consideration for the runner interface.
-   Runnables: Runnables serve as the functionality that is called by a runner.
    -   Computation: The computation interface is a runnable that operates in a
        one call, one return program flow (one thing in one thing out). Example:
        Compute Jones Polynomial and Compute Writhe.
    -   Generator: The generation interface is a runnable that operates in a one
        call, multiple return flow (one thing in many things out). Example:
        generate rational tangles, generate Montesinos tangles, and generate
        arborescent tangles.
-   Data Wranglers: Data wranglers serve as a non-user facing layer used by
    runnables to handle data.
    -   Notation: The notation interface defines data structures used to
        represent knot data. Additionally, the interface describes the
        translation between string representations and data structures. Example:
        Conway notation, algebraic tangle tree notation, and weighted planar
        tangle tree notation.
    -   Storage: The storage interface serves the need for components to read
        and write from external systems. Examples: the command line or a
        database.

````{figure}
```{mermaid}
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

[^io]: Input and Output
[^emb]:
    An embedded system is a small, usually low power, computer (microcontroller)
    that is built into a product. For example, the power seat of your car is an
    embedded system.

[^high-level]:
    A low-level language such as C or Rust compiles to machine code that runs
    directly on the hardware. A high-level language is one that abstracts
    functionality away from hardware.
