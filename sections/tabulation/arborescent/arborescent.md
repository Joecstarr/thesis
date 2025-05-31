## Arborescent Tangles

<!-- prettier-ignore-start -->
(prelim-arbor_def)=
#### Definition of Arborescent
<!-- prettier-ignore-end -->

The primary goal of our program is the enumeration of the algebraic tangles,
however the Conway construction algebraic tangles lack a direct classification,
making the combinatorics of the Conway style algebraic tangles intractable.
Instead, we will leverage a slightly different, but equivalent, construction
given by Bonahon and Seibenmann [@bonahonNewGeometricSplittings2016] the
**arborescent tangles**. The correspondence will become clear when we introduce
the combinatorial construction for arborescent tangles in
[](#construction_of_arbor). In our discussion of arborescent knots and tangles,
we will use the concept of a **knot pair** defined in
{prf:ref}`prelim-def-arborescent_knot_pair`. To define an arborescent tangle, we
will start by defining an arborescent knot as
{prf:ref}`prelim-def-arborescent_knot`.

```{prf:definition} A knot pair, Bonahon and Seibenmann Chapter 2 [@bonahonNewGeometricSplittings2016]
:label: prelim-def-arborescent_knot_pair
A knot pair is a pair $(M, K)$ where $M$ is an oriented connected compact 3
manifold with (possibly empty) boundary, and where $K$ is a proper 1-dimensional
submanifold of $M$.
```

```{prf:definition} Arborescent Knots, Bonahon and Seibenmann Chapter 3 [@bonahonNewGeometricSplittings2016]
:label: prelim-def-arborescent_knot
A knot $(S^3, K)$ is **arborescent** if there exists a finite collection
$F_1,\dots,F_n$ of disjoint Conway spheres such that, if $N$ is the closure of
any component of $S^3 − ⋃_{i=1}F_i$ , then the pair $(N, K \cap N )$ takes the
simple form of {prf:ref}`fig-arborescent_part` after suitable isotopic
deformation in $S^3$.
```

```{figure} ./media/arborescent_knot.svg
:label: fig-arborescent_part
:width: 500px

A collection of Conway spheres (circles) forming what we call an
**arborescent knot vignette**.
```

Observe that arborescent knots are characterized by a collection of Conway
spheres (circles), these Conway spheres are filled in with knot data which form
tangles. This observation gives us a natural way to define arborescent tangles.

```{prf:definition} Arborescent Tangles, Bonahon and Seibenmann Chapter 3 [@bonahonNewGeometricSplittings2016]
Define an **arborescent tangle** as one whose underlying knot pair $(M, K)$ is
arborescent in the sense defined in {prf:ref}`prelim-def-arborescent_knot`
namely $M$ is connected, embeds in $S^3$ and if $(M, K)$ can be split up along a
family of disjoint Conway spheres into pairs that are hollow
(not filled with knot data).
```

```{include} weighted_planar_trees/weighted_planar_trees.md

```

```{include} RLI_trees/RLI_trees.md

```

```{include} computation/computation.md

```
