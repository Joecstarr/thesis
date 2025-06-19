<!-- prettier-ignore-start -->
(sec-intro-applications)=
## Brief Discussion on Applications
<!-- prettier-ignore-end -->

As we saw in the intuitive overview, mathematical knots can be easily
constructed as physical objects. It should be no surprise then that mathematical
knots and tangles appear in the hard sciences, particularly in the realms of
physics, chemistry, and biology. In this section we will discuss one of the most
commonly discussed applications of knot theory.

### Tangles in DNA

One of the fundamental features that identifies life as life is the ability to
self-replicate. In order to self-replicate, life must have a mechanism to pass
information to successive generations. Consider first the most basic self
replicating component of life, called a cell. The information of a cell is
stored as double-stranded DNA (dsDNA)[@watsonMolecularStructureNucleic1953], a
polymer consisting of two strands constructed from a sugar-phosphate connected
to one of the monomers:

1. Adenine (A) [@watsonMolecularStructureNucleic1953]
1. Guanine (G) [@watsonMolecularStructureNucleic1953]
1. Cytosine (C) [@watsonMolecularStructureNucleic1953]
1. Thymine (T) [@watsonMolecularStructureNucleic1953]

The two strands of dsDNA connect to each other to form the "double-helix" where
the monomers bind to each other with guanine (G) binding to cytosine (C), and
adenine (A) binding to thymine (T) [@watsonMolecularStructureNucleic1953]
(@fig-intro-dna_chemical_structure). When replicating, the cell will duplicate
the dsDNA by splitting the dsDNA into two single strands with the enzyme
DNA-helicase. Once the DNA is split, two new complimentary single stands are
constructed to be paired with each of the original single strands.

```{figure} ../../media/dont_proc/DNA_chemical_structure.svg
:label:fig-intro-dna_chemical_structure
@@@ TODO: Add content description [@priceballDNAChemicalStructure2007]
```

The dsDNA of a cell needs to be physically stored inside the cell. The volume
within a cell is limited, so organizing the dsDNA so that all of it fits
requires several complex cellular mechanisms. We will now describe one of those
mechanisms. First, the issue the mechanism solves, every once in a while, the
dsDNA in a cell may become locally knotted. When this local knotting happens and
the cell attempts to replicate, the DNA-helicase will begin splitting the dsDNA,
but when the DNA-helicase reaches the knotted portion it will become stuck and
the replication will be unable to continue [@albertsMolecularBiologyCell2022].
If this local knotting is allowed to happen unchecked, every cell would
eventually be unable to replicate and would ultimately die. Famously, life finds
a way, for this knotting problem, a solution is: the enzyme called type II
topoisomerase[@albertsMolecularBiologyCell2022]. The enzyme attempts to solve
this local knotting by splitting the dsDNA at a crossing, then moving the
(depending on perspective) top double strand to be the bottom double strand.
This action can be seen in @fig-intro-topo.

```{figure} ../../media/topo3.svg
:label: fig-intro-topo
Type II topoisomerase doing a crossing exchange. From top left to bottom
right: 1) A crossing of two dsDNA strands. 2) The enzyme grabs the under strand.
3) The enzyme splits the under strand. 4) The enzyme passes the over strand
through the gap. 5) The crossing with the strands exchanged.
```

In mammals (and many other animal groups), dsDNA takes the form of long strings,
which can only form everyday knots. However, it was discovered that in some
bacteria the dsDNA is a closed loop, allowing it to form a mathematical knot
(@fig-intro-circ_dna_fig) [@dulbeccoEVIDENCERINGSTRUCTURE1963]
[@weilCYCLICHELIXCYCLIC1963] [@vinogradTwistedCircularForm1965].

````{prf:observation}
:label: fig-intro-circ_dna_fig


```{figure} ../../media/dna_circle.svg
:label: fig-intro-dna_circle
A schematic diagram of circular dsDNA.
```

```{figure} ../../media/sem_knot.png
:label: fig-intro-sem_knot-png
A scanning electron microscope image of knotted dsDNA [@arsuagaDNAKnotSeen2013].
```
````

From here one may ask, "If the dsDNA is knotted and type II topoisomerase makes
a change, what kind new knot does this make?", this question was addressed first
by Ernst and Sumners in the 1990s [@ernstCalculusRationalTangles1990]
[@ernstTANGLEEQUATIONS1996]. Their approach considers the dsDNA to be bounded by
two "areas", the first area is created by drawing a circle around the crossing
that type II topoisomerase is working on (right side of
@fig-intro-tangle_equation_start) and the second by drawing a circle around the
remainder (left side of @fig-intro-tangle_equation_start). From here, the
crossing change from type II topoisomerase can be modeled by changing the tangle
bound in the area on the right (@fig-intro-tangle_calc),
[@darcy3DVisualizationSoftware2008]. After the change, there may be many
crossings that type II topoisomerase could "choose" to work on next. A program
like TopoICE-X [@darcy3DVisualizationSoftware2008] built into KnotPlot
[@schareinInteractiveTopologicalDrawing1998] can help visualize the results of
making these choices as seen in @fig-intro-pathway-png.

````{prf:observation}
:label: fig-intro-tangle_calc


```{figure} ../../media/tangle_equation_start.svg
:label: fig-intro-tangle_equation_start
A knot diagram showing two areas containing knot data. The right side contains
the crossing that type II topoisomerase will work on.
```

```{figure} ../../media/tangle_equation_result.svg
:label: fig-intro-tangle_equation_result
A knot diagram showing two areas containing knot data. The right side contains
the crossing that type II topoisomerase has worked on.
```

```{figure} ../../media/pathway.png
:label: fig-intro-pathway-png
Output of TopoICE-X [@darcy3DVisualizationSoftware2008] built into KnotPlot.
```
````
