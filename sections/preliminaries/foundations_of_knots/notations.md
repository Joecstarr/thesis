### Knot Notations

The final topic to cover in our treatment of foundations for knot theory is
notational strategies for knots. In @subsec-knot_def, we came across our first
notational strategy for knots, the knot diagrams. While diagrams are a great
human-readable way to note a knot, when the tasks of enumeration and computation
(by hand) are considered, knot diagrams quickly show deficiencies. These
deficiencies become intractable when a computer is brought into the picture. As
a remedy for this issue, knot theorists have invented several combinatorial
notations for knots. Perhaps the most historically important knot notation for
use in tabulation by computer is the Dowker-Thistlethwaite (DT) notation
(@sec-proj-note_dt) developed by its namesakes specifically for use in
computational tabulation. Each notational strategy used in knot theory has
strengths and weaknesses. For example, using DT notation for computation of the
Jones polynomial @def-jones may be more cumbersome than using the Planar Diagram
(PD) notation (@sec-proj-note_pd) for the same task, as PD directly encodes
crossings while DT encodes a walk on a strand. The remainder of this section
will be the development of the Conway notation, which lays the foundation for
the work in this thesis.

```{include} conway.md

```
