### Minimalization of Arborescent Tangles

As we discussed in @sec-minimalization the fact that RLITT are often none
minimal arborescent representatives of a tangle. In fact, minimal arborescent
representations may not be minimal tangle representations. Conway gives an
example [@conwayEnumerationKnotsLinks1970] where an arborescent (algebraic) knot
is transformed into a minimal polygonal tangle (@subsubsec-opo-insert). In
@fig-6starstar_nonminimal we rephrase Conway's example for tangles.

```{figure}../../media/fig-6starstar_nonminimal.svg
:label: fig-6starstar_nonminimal
An arborescent tangle being turned into a polygonal tangle via a sequence of
Reidemister moves.
```

This leads to two items that must be addressed to ensure the list of tangles
contains the all important minimal diagrams.

#### Identification of Minimal Arborescent Tangle Representations

The first item, and most straightforward to address, is the identification of a
minimal arborescent representative of a given RLITT $\Gamma$. Meaning,
identifying the weighted planar tree related to $\Gamma$ whose ACN is minimal.
We saw in @sec-minimalization the ways canonization can increase complexity in a
weighted planar tangle tree. To take $\Gamma$ to its minimal form, we will need
to develop the theory for and an implementation of an efficient algorithm to
systematically de-canonize $\Gamma$.

#### Identification of Minimal Representations for Arborescent Tangles

Second, and seemingly significantly more challenging, is the identification of
the minimal representative of a given arborescent tangle. That is, the
identifying the minimal representative, arborescent or otherwise as in
@fig-6starstar_nonminimal. This task requires the development of a
classification of the subtrees of a weighted planar tree that correspond to
moves of the type seen in @fig-6starstar_nonminimal. The complexity of this task
is compounded by the fact the family of planar graphs allowing these types of
moves is infinite (easily shown via an induction). Further, the moves that
enable arborescent tangles that are minimally polygonal are not limited to the
moves on the marked $6^{**}$ (@fig-6starstar_nonminimal). We can see a second
class in @fig-other_nonminimal, realizing the arborescent form is left to the
reader.

```{figure}../../media/fig-other_nonminimal.svg
:label: fig-other_nonminimal
A polygonal
```
