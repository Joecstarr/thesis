<!-- prettier-ignore-start -->
(sec-CWPTT-def)=
#### Canonical Weighted Planar Tangle Trees (CWPTT)
<!-- prettier-ignore-end -->

Observe that the weighted planar tangle trees we've seen are badly non-unique
representatives for arborescent tangles. The first step to finding a unique
preferred representative is to put some additional conditions on a weighted
planar tree $\Gamma$. The following conditions pair down the equivalence class
of an arborescent tangle to a more manageable level.

`````{prf:definition} Canonical Weighted Planar Tangle TreesBonahon and Seibenmann Section 12.8.2 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-def-abcanon

A Weighted Planar Tree is called a **Canonical Weighted Planar
Tangle Tree (CWPTT)** if it satisfies the following conditions:


-   **Weight Condition** At each vertex of $\Gamma$, at most one weight is
    non-zero.
-   **Stick Condition** On any stick the weights are non-zero except for end
    vertices that have a bond free in $\Gamma_0$ and for the case $\Gamma_0$ is
    {prf:ref}`wpt-construc-fig-stick_cond-1` or
    {prf:ref}`wpt-construc-fig-stick_cond-2`. The non-zero weights along any
    stick are of alternating sign. No end vertex of a stick has weight $\pm 1$
    unless it has a bond free in $\Gamma_0$, or
    {prf:ref}`wpt-construc-fig-stick_cond-3`.
-   One of:

    -   **Positivity Condition** There are no sticks in $\Gamma_0$ of the form
        {prf:ref}`wpt-construc-fig-positivity_cond`.
    -   **Negativity Condition** There are no sticks in $\Gamma_0$ of the form
        {prf:ref}`wpt-construc-fig-negativity_cond`.
````{prf:observation}
:label: wpt-construc-fig-stick_cond

```{figure} ./media/bands/conditions/stick/0.svg
:label: wpt-construc-fig-stick_cond-1
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/stick/00.svg
:label: wpt-construc-fig-stick_cond-2
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/stick/pm1.svg
:label: wpt-construc-fig-stick_cond-3
:width: 100px
$\ a$
```

````

````{prf:observation}
:label: wpt-construc-fig-positivity_cond

```{figure} ./media/bands/conditions/positivity/am2.svg
:label: wpt-construc-fig-positivity_cond-1
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/positivity/am2a.svg
:label: wpt-construc-fig-positivity_cond-2
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/positivity/m2.svg
:label: wpt-construc-fig-positivity_cond-3
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/positivity/m1.svg
:label: wpt-construc-fig-positivity_cond-4
:width: 100px
$\ a$
```

````

````{prf:observation}
:label:wpt-construc-fig-negativity_cond

```{figure} ./media/bands/conditions/negativity/a2.svg
:label: wpt-construc-fig-negativity_cond-1
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/negativity/a2a.svg
:label: wpt-construc-fig-negativity_cond-2
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/negativity/2.svg
:label: wpt-construc-fig-negativity_cond-3
:width: 100px
$\ a$
```

```{figure} ./media/bands/conditions/negativity/1.svg
:label: wpt-construc-fig-negativity_cond-4
:width: 100px
$\ a$
```

````

`````

Bonahon and Seibenmann show in {prf:ref}`wpt-equi-lemma-exist` that these
conditions are sufficient to distinguish every arborescent tangle. In fact,
every weighted planar tangle tree can be turned into a CWPTT by a series of
moves in an extended calculus on weighted planar trees given by Bonahon and
Seibenmann [@bonahonNewGeometricSplittings2016]. We call this process
**canonization** of a weighted planar tangle tree.

```{prf:corollary} Existance of CWPTT, Bonahon and Seibenmann Corollary 12.20 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-lemma-exist

Every arborescent tangle is obtained by pairwise connected sum operations from
arborescent tangles associated to positively (or negatively)
canonical weighted planar trees (with labels in $V_4$ at free bonds).
```

We should note some consequences of the positivity and negativity condition.
First, a positive CWPTT ($\LP +\RP$-CWPTT) can be transformed by a sequence of
moves in the extended calculus of weighted planar trees into a negative CWPTT
$\LP -\RP$-CWPTT). Similarly, a ($\LP -\RP$-CWPTT) can be transformed into a
positive CWPTT. Second, we note that a CWPTT can be neutral in positivity or
negativity, this happens when the tree lacks any of the described subtrees. In
our later discussion of generation algorithms, we will refer to these trees as
**neutral** trees.

Bonahon and Seibenmann additionally give a classification of arborescent tangles
via moves on CWPTT, seen in {prf:ref}`wpt-equi-thm-classi`.

```{prf:theorem} Classification Theorem for Canonical Weighted Planar Tangle Trees, Bonahon and Seibenmann theorem 12.21 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-thm-classi
Consider two positive (or negative) CWPTT
$\Gamma^{\,}$ and $\Gamma^\prime$, with free bonds labelled by
elements of $V_4$. Plumbing according to $\Gamma$ and $\Gamma^\prime$
gives isomorphic arborescent tangles if and only if $\Gamma$ and
$\Gamma^\prime$ can be deduced from each other by a sequence of moves
($F_1$), ($F_2$), ($F_3^\prime$).
```

Further, Bonahon and Seibenmann describe an algorithm for producing these
sequences of moves. The algorithm will be useful in the following sections,
enabling us to pass between any two trees $\Gamma$ and $\Gamma^\prime$ in the
class of representatives for an arborescent tangle $\T$.

```{prf:theorem} Bonahon and Seibenmann theorem 12.19 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-cor-algo
There exists an effective algorithm which, for any weighted planar tree $\Gamma$
with free bonds labelled by elements of $V_4$, alters $\Gamma$ by a sequence of
moves of the calculus of arborescent tangles to produce a collection of
positively (or negatively) canonical weighted planar trees.
```

Finally, we define the **Arborescent Crossing Number** of the tangle diagram
described by a CWPTT as follows.

```{prf:definition} Arborescent Crossing Number
:label: apn-def-2

We call the crossing number of the tangle diagram described by a tree the
**Arborescent Crossing Number (ACN)** which is given by:
$$\text{ACN}=\sum |\text{weights in the tree}|$$
```
