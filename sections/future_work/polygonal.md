### Polygonal Tangles

In our discussion of minimalization, we discussed the polygonal tangles which we
previously defined in @subsubsec-opo-insert. The second topic for future
research is the expansion of the tangle tables to include all polygonal tangles
up to a target crossing number. Expanding tangle tables to include the polygonal
tangles is useful as at high crossing numbers, the polygonal tangles dominate
the arborescent tangles. Unfortunately, for the polygonal case, we lack a
general classification result. Meaning, as it stands, we have no mechanism to
directly generate unique representatives for a polygonal tangle as we have done
with the classes of tangle in this thesis. The development of a general
classification for polygonal tangles is difficult, at least as difficult as a
general classification of knots. With this in mind, we will discuss two possible
directions for tackling the polygonal knot case.

#### Ad Hoc Classification of Constellations

In @subsubsec-opo-insert, we discussed constellations
[@connollyClassificationTabulation2string2021] used for generation of polygonal
tangles via insertion. Since the crossing number of a polygonal tangle is
bounded below by the vertex count of its constellation, the number of
constellations represented at reasonable crossing numbers is small.
Additionally, the difference between crossing number and vertex count is low,
many of the inserted tangles will have low crossing number, bounding possible
complexity. In his thesis work, Connolly
[@connollyClassificationTabulation2string2021] enumerates the ten smallest
constellations, those with ten or fewer vertices. With such a small set to work
with, and relative complexity being low, developing an ad hoc classification
results for each constellation may be a fruitful approach to expanding to
polygonal tangles. For example, consider the constellation seen in
@fig-6starstar_nonminimal, we can enumerate the possible crossing numbers for
tangles to be inserted. We do that for $n$ up to 7 is in @sec-fw-adhoc-tab-to7,
where we see that up to 7 crossing this constellation only admits rational
insertion, at 8 we get our first Montesinos. Completing an analysis of these
patterns may reveal patterns that allow a classification of this $6^{**}$
constellation. Even partial results in this arena may yield more efficient
heuristics when utilizing the methodology in @subsubsec-fw-brute.

```{table}
:label: sec-fw-adhoc-tab-to7

| Crossing Number |                                              Possible Crossing numbers                                               |
| :-------------: | :------------------------------------------------------------------------------------------------------------------: |
|        5        |                                                     $*.1.1.1.1.1$                                                      |
|        6        |                       $$\begin{aligned}*.2.1.1.1.1,*.1.2.1.1.1\\\ast.1.1.2.1.1,*.1.1.1.2.1,\\\ast.1.1.1.1.2\end{aligned}$$                       |
|        7        | $$\begin{aligned}*.1.1.1.2.2,*.1.1.2.1.2\\\ast.1.1.2.2.1,*.1.2.1.1.2,\\\ast.1.2.1.2.1,*.1.2.2.1.1,\\ast.2.1.1.1.2,*.2.1.1.2.1,\\\ast.2.1.2.1.1,*.2.2.1.1.1,\\\ast.3.1.1.1.1,*.1.3.1.1.1,\\\ast.1.1.3.1.1,*.1.1.1.3.1,\\\ast.1.1.1.1.3\end{aligned}$$ |
```

<!-- prettier-ignore-start -->
(subsubsec-fw-brute)=
#### Brute Force Tabulation
<!-- prettier-ignore-end -->

Without a full or partial classification of the polygonal tangles, we must take
an alternative approach to what we have seen in this thesis. That alternative is
the brute force, two pass enumeration strategy used in previous knot tabulation
efforts
[@dowkerClassificationKnotProjections1983;@hosteFirst1701936Knots1998;@burtonNext350Million2020]
and outlined in @sec-history-of-tabulation. The key difficulty in this
methodology, a selection of invariants that combine to uniquely identify
tangles. This difficulty is due to the fast growth rate for the count of tangles
of a given crossing number. This growth rate, means any invariant that is
selected must have an efficient computation strategy. If, for example, as Burton
did [@burtonNext350Million2020], we select hyperbolic volume. Utilizing this we
may be able to distinguish a large portion of tangles, however computation for
crossing numbers as low as 10 will be intractable due to the per tangle time to
compute the volume. This says nothing to the raw storage needed to hold the
computed and partial data. A seemingly better choice are Invariants with
polynomial time computation, such as those introduced by van der Veen and
Bar-Natan (to be published [@vanderveenKnotInvariantsFinite]). While weaker than
hyperbolic volume, these invariants are stronger than the polynomial invariants,
and faster than both to compute. Statistics for polynomial invariants can be
found in Maguire's thesis work (Section 5.4
[@maguireKhovanovHomologyLegendrian]).
