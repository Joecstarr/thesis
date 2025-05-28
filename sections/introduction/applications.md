## Brief Discussion on Applications

As we saw in the intuitive overview, mathematical knots can be easily
constructed as physical objects. It should be no surprise then that mathematical
knots and tangles appear in the hard sciences, particularly in the realms of
physics and biology, this section will discuss some of these applications.

### Solar Flares

The sun is a ball of "burning" gas 150 million kilometers away, this burning gas
generates tremendous heat and a massive magnetic field. You may remember from an
earth science course that the earth has layers, and as you move further from the
center, the layers become cooler. The sun also has layers, similarly to the
layers of the earth, the core of the sun is the hottest and as you move outward
the layers become cooler. However, unlike the earth, as you move to the
atmosphere the temperature increases as you move outward. With the hottest layer
of the solar atmosphere, called the corona, being the outermost
[@carrollIntroductionModernAstrophysics2014]. One model for why the corona is so
hot, is the braiding of solar flares (magnetic field lines)
[@cirtainEnergyReleaseSolar2013],bergerEnergycrossingNumberRelations1993. When
energy builds in this magnetic field and released, a solar flare, an arc of
burning gas, is formed. When these arcs form, they will sometimes "dance" around
each other, becoming a braid. While at first glance this structure may not look
like a tangle, in fact, physically it's not a tangle.

```{figure} ./media/Sun-corona-magnetic-braids.jpg
:label: fig-intro-solar_lines
@@@ TODO: Add content description
```

To see the tangle, we need to change our perspective slightly; we move the end
points of the flares so that they lay on the edge of one giant circle and
"delete" the rest of the sun we are left with a $n-\text{string tangle}$ similar
to @fig-intro-solar_tangle In general when talking about the knot theory of
solar flares we instead consider what is known as a braid, where two circles are
drawn around the two sets of bases of the flares, seen in

````{prf:observation}
:label: fig-intro-solar


```{figure} ./media/solar_tangle.svg
:label: fig-intro-solar_tangle
@@@ TODO: Add content description
```

```{figure} ./media/solar_braid.svg
:label: fig-intro-solar_braid
@@@ TODO: Add content description
```
````

@fig-intro-solar_braid. An accessible introduction to the theory of braids can
be found in Birman's "Braids: A survey" [@birman2005braids]. For further reading
on the braid theory of solar flares reference `@@@missing`.

### Tangles in DNA

One of the fundamental features that identifies life as life is the ability to
self-replicate. In order to self-replicate, life must have a mechanism to pass
information to successive generations. Consider first the most basic self
replicating component of life, called a cell. The information of a cell is
stored as double-stranded DNA (dsDNA), a polymer consisting of two strands a
sugar-phosphate connected to one of the monomers: adenine (A), guanine (G),
cytosine (C), and thymine (T) [@watsonMolecularStructureNucleic1953]. The two
strands of dsDNA connect to each other to form the "double-helix" where the
monomer guanine (G) binding to cytosine (C), and adenine (A) binding to thymine
(T) [@watsonMolecularStructureNucleic1953] as seen in
@fig-intro-DNA_chemical_structure. When replicating, the cell will duplicate the
dsDNA by splitting the dsDNA with an enzyme DNA-helicase into two single
strands, then will build two new strands from each strand of the original dsDNA.
The dsDNA of a cell needs to be physically stored in the cell. The volume in a
cell which can contain the dsDNA is small, so to fit all the dsDNA into the cell
it must remain organized. Every once in a while, the dsDNA will become locally
knotted. If this type of knotting happens to dsDNA and the cell attempts to
replicate, the DNA-helicase will start to split the dsDNA, but when the
DNA-helicase reaches the knot it will become stuck and the DNA helicase, as well
as the replication, would be unable to continue
[@albertsMolecularBiologyCell2022]. If this was allowed to happen, every cell
would eventually be unable to replicate and would ultimately die. Famously, life
finds a way, for the knotting problem. A solution is an enzyme, called type II
topoisomerase, that tries to ensure there are no knots on the
dsDNA[@albertsMolecularBiologyCell2022]. Type II topoisomerase accomplishes this
by splitting the dsDNA at a crossing and moving the (depending on perspective)
top double strand to be the bottom double strand. This action can be seen in
@fig-intro-topo.

````{prf:observation}
:label: fig-intro-dna


```{figure} ./media/dont_proc/DNA_chemical_structure.svg
:label:fig-intro-DNA_chemical_structure
@@@ TODO: Add content description
```

```{figure} ./media/dont_proc/topo.svg
:label: fig-intro-topo
@@@ TODO: Add content description
```
````

While in mammals, dsDNA takes the form of long strings, which can only form
everyday knots, however it was discovered that in some bacteria the dsDNA is a
closed loop, making it a mathematical knot (@fig-intro-circ_dna_fig)
[@dulbeccoEVIDENCERINGSTRUCTURE1963] [@weilCYCLICHELIXCYCLIC1963]
[@vinogradTwistedCircularForm1965].

````{prf:observation}
:label: fig-intro-circ_dna_fig


```{figure} ./media/dna_circle.svg
:label: fig-intro-dna_circle
@@@ TODO: Add content description
```

```{figure} ./media/sem_knot.png
:label: fig-intro-sem_knot-png
@@@ TODO: Add content description
```
````

From here one may ask, "If the dsDNA is knotted and type II topoisomerase makes
a change, what kind new knot does this make?", this question was addressed first
by Ernst and Sumners in the 1990s [@ernstCalculusRationalTangles1990]
[@ernstTANGLEEQUATIONS1996]. Their approach was to consider the dsDNA split in two
"areas", the first area is created by drawing a circle around the crossing that
type II topoisomerase is working on and the second by drawing a circle around
the remainder, as seen in @fig-intro-tangle_equation_start. From here, the
crossing change from type II topoisomerase can be modeled by changing the tangle
bound in the area on the right (@fig-intro-tangle_calc),
[@darcy3DVisualizationSoftware2008] built into KnotPlot
@schareinInteractiveTopologicalDrawing

````{prf:observation}
:label: fig-intro-tangle_calc


```{figure} ./media/tangle_equation_start.svg
:label: fig-intro-tangle_equation_start
@@@ TODO: Add content description
```

```{figure} ./media/tangle_equation_result.svg
:label: fig-intro-tangle_equation_result
@@@ TODO: Add content description
```

```{figure} ./media/pathway.png
:label: fig-intro-pathway-png
@@@ TODO: Add content description
```
````

@fig-intro-tangle_equation_result. As you can see after the change there, may be
many crossings that type II topoisomerase could "choose" to work on next. A
program like TopoICE-X [@darcy3DVisualizationSoftware2008] built into KnotPlot
@schareinInteractiveTopologicalDrawing can help visualize the results of making
these choices as seen in @fig-intro-pathway-png.
