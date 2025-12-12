Having now established a model process for developing software we can start our
efforts in developing a design for a general knot theory software toolbox. To
begin, we explore a collection of tools currently in use in the computational
knot theory space. Considering the strengths and shortcomings of these tools
helps inform the requirements and possible use cases for our general knot theory
software toolbox.

## KnotPlot

KnotPlot[@schareinInteractiveTopologicalDrawing1998] is a closed source[^closed]
knot computation tool primarily and widely used for diagramming knots, this
includes several diagrams in this thesis. Knotplot was developed as a portion of
Dr. Robert Scharein's PhD thesis [@schareinInteractiveTopologicalDrawing1998],
he is also the primary maintainer. The primary interface for KnotPlot is by
interacting with a GUI[^GUI]. This makes the onboarding process for
non-technical users, including undergraduate researchers, straightforward and
the learning curve shallow. Knotplot includes many export options and
specialized research computational tools, some undocumented. While support is
readily available from Dr. Scharein this can make power use of KnotPlot
difficult. KnotPlot has recently added a programmatic interface allowing general
scripting in the programming language Lua. This scripting interface allows for
custom diagramming and custom components. These custom scripts are limited
however by the hooks available in KnotPlot. It is not always clear what calls to
make into KnotPlot to accomplish your goals. Additionally, since the Lua
interface is compiled into KnotPlot and isn't a language widely used in
research, finding supported external libraries can be difficult. KnotPlot is an
unparalleled knot diagramming tool, but the environment becomes a walled garden
that can be difficult to build into a tool chain.

## Mathematica Libraries

<!-- (Mathematica https://katlas.org/wiki/Printable_Manual) -->

KnotTheory [@bar-natanKnotTheory] and LinKnot [@jablanLinKnotKnotTheory2007] are
collections of knot theory tools and datasets that are used with the Wolfram
Mathematica system. Both KnotTheory and LinKnot are open source[^open] and
available for download. Mathematica is a natural environment for mathematics
research, as the language syntax is similar to written theoretical mathematics.
This similarity of appearance lowers the learning curve for use of the tooling.
Mathematica is also commonly used in undergraduate calculus sequences, making
the onboarding of undergraduate researchers straight forward. The interfaces
defined by both KnotTheory and LinKnot are natural in the Mathematica context,
further shallowing the learning curve for those already familiar with
Mathematica. Additionally, both collections are well documented by the website
"knot atlas" [@bar-natanKnotTheory] and the textbook "LinKnot"
[@jablanLinKnotKnotTheory2007] for KnotTheory and LinKnot, respectively.
Unfortunately, neither collection is under active development or maintenance,
with the last published versions from $2016$ for KnotTheory and $2011$ for
LinKnot. Additionally, neither collection is released under version control, has
a bug log, or has a published test suite. Missing the traceability implicit in
these artifacts makes program correctness something that must be considered when
using the collections.

<!-- prettier-ignore-start -->
(sec-surveyoftools-snap)=
## SnapPy/SnapPea
<!-- prettier-ignore-end -->

SnapPy [@SnapPy] is a Python wrapper for SnapPea, which is a collection of C
libraries. SnapPy and SnapPea are open source and published in the same GitHub
repository which includes bug reporting and test suites. SnapPy's Python
bindings allow researchers to leverage the massive Python ecosystem, allowing
for wide and varied usage. SnapPy can be utilized in anything from a simple
command line tool, to a GUI tool to draw knots, to a webapp doing knot
computations. This allows SnapPy to be tailored to the needs of individual
researchers, allowing for simple subsets of functionality to be presented to
undergraduate researchers. Each of these uses benefits from the decoupling of
SnapPy and the core logic in SnapPea, allowing for fast execution of the SnapPea
C code, but simple supportable Python bindings. The SnapPea layer, however, is
designed on an ad hoc basis, meaning each file/unit stands alone with little
structural overlap. If a developer wants to reuse the SnapPea C layer directly,
they must reverse engineer the structures they wish to reuse.

[^closed]:
    Closed source software is a software product with no published source code.

[^open]:
    Open-source software is a software product with publicly published source
    code.

[^GUI]:
    A graphical user interface, such as a Windows or the screen on a copy
    machine.
