<!-- prettier-ignore-start -->
(sec-arborescent)=
# Arborescent Tangles
<!-- prettier-ignore-end -->

This section describes the methodology we use to answer the final of the essential questions
detailed in @sec-intro-overview.

> "How do I systematically construct algebraic/arborescent tangles?", "How do I tell two
> algebraic/arborescent tangles I make apart?", and "How many algebraic/arborescent tangles can I
> create?"

In this thesis so far we have worked with the algebraic tangles (@def-algebraic) constructed with
Conway's tangle arithmetic (@subsubsec-conway_calc).

In this section we will leverage a slightly different, but equivalent, construction given by Bonahon
and Siebenmann [@bonahonNewGeometricSplittings2016] the **arborescent tangles**. The one-to-one
correspondence between the classes will become clear as we introduce the construction for
arborescent tangles.

This section starts with an overview of Bonahon and Siebenmann's
[@bonahonNewGeometricSplittings2016] definition of arborescent knots and tangles
(@prelim-arbor_def). We then give their smooth and combinatorial constructions of arborescent knots
and tangles (@subsec-wptt). Next, we give original work extending Bonahon and Siebenmann's canonical
construction to a local view (@sec-CWPTT-def). This local view is leveraged to define a unique
representative for each class of arborescent tangles (@subsec-rlitt). Finally, we will describe an
original algorithm and notation that directly enumerates those unique representatives
(@subsec-computation).

<!-- prettier-ignore-start -->
(prelim-arbor_def)=
## Definition of Arborescent
<!-- prettier-ignore-end -->

We now give a high-level description of the manifold theory underpinning the theory of arborescent
knots and tangles. A full treatment of the manifold theory can be found in Bonahon and Siebenmann
[@bonahonNewGeometricSplittings2016]. Our first concept is that of a **knot pair**, which serves as
the underlying structure for all the smooth objects in this subsection.

```{prf:definition} Bonahon and Siebenmann, Page 15 [@bonahonNewGeometricSplittings2016]
:label: prelim-def-arborescent_knot_pair
A **knot pair** is a pair $(M, K)$ where $M$ is an oriented connected compact 3
manifold with (possibly empty) boundary, and where $K$ is a proper 1-dimensional
submanifold of $M$.
```

````{prf:definition} Bonahon and Siebenmann, Page vi [@bonahonNewGeometricSplittings2016]
:label: prelim-def-arborescent_knot
A knot $(S^3, K)$ is **arborescent** if there exists a finite collection
$F_1,\dots,F_n$ of disjoint Conway spheres such that, if $N$ is the closure (in the sense of a closure of a set) of
any component of $S^3 − \cup_{i=1}F_i$ , then the pair $(N, K \cap N )$ takes the
simple form of @fig-arborescent_part after suitable isotopic
deformation in $S^3$.

```{figure}../../media/arborescent_knot.svg
:label: fig-arborescent_part
:width: 70%

A collection of Conway circles forming what we call an
**arborescent vignette**.
```
````

````{figure}
:label: fig-arborescent_vignette_99
```{figure}../../media/arborescent_band.svg
:label: fig-arborescent_band

The arborescent vignette from @fig-arborescent_part seen with Conway spheres.
```

```{figure}../../media/vin_1.svg
:label: fig-arborescent_vignette_1

The arborescent vignette showing a $1$ crossing tangle to be arborescent.
```
Arborescent vignettes.
````

```{note}
The $F_i$ in @prelim-def-arborescent_knot are disjoint but may sit inside
each other. This means we may have arborescent vignettes containing arborescent
vignettes, but the closure of each individual component looks like
@fig-arborescent_part.
```

Observe that arborescent knots are characterized by a collection of Conway spheres (circles).
Choosing to not fill one, or more, of these Conway spheres yields a tangle.

```{prf:definition}Bonahon and Siebenmann, Page 144 [@bonahonNewGeometricSplittings2016]
:label: intro-def-arbor-tangle
Define an **arborescent tangle** as one whose underlying knot pair $(M, K)$ (@prelim-def-arborescent_knot_pair) is
arborescent in the sense defined in @prelim-def-arborescent_knot.
```

We see from the above the first portion of the correspondence between the algebraic and arborescent
tangles. Each algebraic tangle can be naturally decomposed into a collection of nested arborescent
knot vignettes given by its operations $+$ and $\vee$.

```{include} weighted_planar_trees/weighted_planar_trees.md

```

```{include} RLI_trees/RLI_trees.md

```

```{include} computation/computation.md

```
