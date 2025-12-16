### Polygonal Tangles

We now discuss the expansion of the tangle tables to include all polygonal tangles up to a target
crossing number. Expanding tangle tables to include the polygonal tangles is useful as at high
crossing numbers, the polygonal tangles dominate the arborescent tangles. Unfortunately, for the
polygonal case, we lack a general classification result. Meaning, as it stands, we have no
theoretical mechanism for direct generation of unique representatives for a polygonal tangle as we
have done with the classes of tangle in this thesis. The development of a general classification for
polygonal tangles is difficult, at least as difficult as a general classification of knots. With
this in mind, we will discuss two possible directions for expanding the polygonal tangles.

#### Ad Hoc Classification of Constellations

In @subsubsec-opo-insert, we discussed constellations [@connollyClassificationTabulation2string2021]
used for generation of polygonal tangles via insertion. The crossing number of a polygonal tangle is
bounded below by the vertex count of its constellation. So the number of constellations represented
at reasonable crossing numbers is small. Additionally, when the difference between crossing number
and vertex count is low, many of the inserted tangles will have low crossing numbers, again bounding
complexity. In his thesis work, Connolly [@connollyClassificationTabulation2string2021] enumerates
the ten smallest constellations, those with ten or fewer vertices.

```{note}
It's worth noting that expanding the table of constellations for a polygon graph is computationally
hard, shown NP-Complete by Cook[@cookComplexityTheoremprovingProcedures1971].
```

With low vertex count polygons, and at low crossing number, developing an ad hoc classification
result for each constellation may be a fruitful approach. For example, consider the constellation
seen in @fig-6starstar_const, we can enumerate the possible crossing numbers and locations for
tangles to be inserted, @sec-fw-adhoc-tab-to7.

```{figure} ../../media/fig-6starstar_const.svg
:label: fig-6starstar_const
The unique constellation for $6^{\ast\ast}$
```

We see that up to 7 crossings this constellation only admits rational insertions, at 8 crossings we
see our first Montesinos. Completing an analysis of the possibilities for insertion may reveal
patterns that allow a classification of this $6^{**}$ constellation. Even partial results in this
arena may yield more efficient heuristics when utilizing the methodology in @subsubsec-fw-brute.

```{table} Possible insertions of $6^{\ast\ast}$ by crossing number.
:label: sec-fw-adhoc-tab-to7
| Crossing Number |                                              Possible Crossing numbers for insertion                                              |
| :-------------: | :------------------------------------------------------------------------------------------------------------------: |
|        5        |                                                     $\ast.1.1.1.1.1$                                                      |
|        6        |                       $$\begin{aligned}\ast.2.1.1.1.1,\ast.1.2.1.1.1\\\ast.1.1.2.1.1,\ast.1.1.1.2.1,\\\ast.1.1.1.1.2\end{aligned}$$                       |
|        7        | $$\begin{aligned}\ast.1.1.1.2.2,*.1.1.2.1.2\\\ast.1.1.2.2.1,*.1.2.1.1.2,\\\ast.1.2.1.2.1,*.1.2.2.1.1,\\\ast.2.1.1.1.2,*.2.1.1.2.1,\\\ast.2.1.2.1.1,*.2.2.1.1.1,\\\ast.3.1.1.1.1,*.1.3.1.1.1,\\\ast.1.1.3.1.1,*.1.1.1.3.1,\\\ast.1.1.1.1.3\end{aligned}$$ |
```

<!-- prettier-ignore-start -->
(subsubsec-fw-brute)=
#### Brute Force Tabulation
<!-- prettier-ignore-end -->

Without a full or partial classification of the polygonal tangles, we must take an alternative
approach to what we have seen in this thesis. That alternative is the brute force, two pass
enumeration strategy used in previous knot tabulation efforts
[@dowkerClassificationKnotProjections1983; @hosteFirst1701936Knots1998; @burtonNext350Million2020]
and outlined in @sec-history-of-tabulation. The key difficulty in this methodology is the selection
of invariants that combine to uniquely identify tangles. This difficulty is due to the fast growth
rate for the count of tangles of a given crossing number. This growth rate means any invariant that
is selected must have an efficient computation strategy. If, for example, as Burton did
[@burtonNext350Million2020], we select hyperbolic volume, we may be able to distinguish a large
portion of tangles, however computation for crossing numbers as low as 10 will be intractable due to
the per tangle time to compute the volume. This says nothing about the raw storage needed to hold
the computed and partial data. A seemingly better choice are invariants (@subsec-invariant) which
have polynomial time computations, such as those introduced by van der Veen and Bar-Natan (to be
published [@vanderveenKnotInvariantsFinite]). While weaker than hyperbolic volume, these invariants
are stronger than the polynomial invariants, and faster than both to compute. Statistics for
polynomial invariants can be found in Maguire's thesis work [@maguireKhovanovHomologyLegendrian].
