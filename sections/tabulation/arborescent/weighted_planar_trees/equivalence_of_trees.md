<!-- prettier-ignore-start -->
(sec-CWPTT-def)=
#### Canonical Weighted Planar Tangle Trees (CWPTT)
<!-- prettier-ignore-end -->

Observe that the weighted planar tangle trees we've seen are badly non-unique
representatives for arborescent tangles. The first step to finding a unique
preferred representative is to put some additional conditions on a weighted
planar tree, $\Gamma$. The following conditions pare down the equivalence class
of an arborescent tangle to a more manageable level.

`````{prf:definition} Bonahon and Seibenmann Section 12.8.2 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-def-abcanon

A weighted planar tree is called a **canonical weighted planar
tangle tree (CWPTT)** if it has a single free bond with a label from
$V_4$ and satisfies the following conditions:


-   **Weight Condition** At each vertex of $\Gamma$, at most one weight is
    non-zero.
-   **Stick Conditions**

    1. On any stick the weights of the vertices are non-zero except for end vertices that have a bond free in $\Gamma$ and for the case $\Gamma$ is @wpt-construc-fig-stick_cond-1 or @wpt-construc-fig-stick_cond-2.
    2. The non-zero weights along any stick are of alternating sign.
    3. No end vertex of a stick has weight $\pm 1$ unless it has a bond free in $\Gamma$.

    ````{figure}
    :label: wpt-construc-fig-stick_cond

    ```{figure} ../../media/bands/conditions/stick/0.svg
    :label: wpt-construc-fig-stick_cond-1
    :width: 100px
    The zero tangle.
    ```

    ```{figure} ../../media/bands/conditions/stick/00.svg
    :label: wpt-construc-fig-stick_cond-2
    :width: 100px
    The infinity tangle.
    ```

    ````
-   One of:

    -   **Positivity Condition** Except for those with a free bond, there are no sticks in $\Gamma$ of the forms
        @wpt-construc-fig-positivity_cond-1 or @wpt-construc-fig-positivity_cond-2.

        ````{figure}
        :label: wpt-construc-fig-positivity_cond

        ```{figure} ../../media/bands/conditions/positivity/am2.svg
        :label: wpt-construc-fig-positivity_cond-1
        :width: 100px
        The $-2$ integral tangle.
        ```

        ```{figure} ../../media/bands/conditions/positivity/am2a.svg
        :label: wpt-construc-fig-positivity_cond-2
        :width: 100px
        A fully open stick with $-2$ crossings.
        ```

        ````
    -   **Negativity Condition** Except for those with a free bond, there are no sticks in $\Gamma$ of the forms
         @wpt-construc-fig-negativity_cond-1 or @wpt-construc-fig-negativity_cond-2.

        ````{figure}
        :label:wpt-construc-fig-negativity_cond

        ```{figure} ../../media/bands/conditions/negativity/a2.svg
        :label: wpt-construc-fig-negativity_cond-1
        :width: 100px
        The $2$ integral tangle.
        ```

        ```{figure} ../../media/bands/conditions/negativity/a2a.svg
        :label: wpt-construc-fig-negativity_cond-2
        :width: 100px
        A fully open stick with $2$ crossings.
        ```

        ````

`````

```{figure} ../../media/bands/watt_montesinos.svg
:label: wpt-fig-construc-canon-
A canonical tree for Montesinos tangle, a smaller class of
tangle described by [@bonahonNewGeometricSplittings2016]
```

```{convention}
The positivity and negativity conditions are a consequence of the behavior of
two crossing tangles seen in @minimal-fig-nonmin. Enforcing one of the
conditions forces us globally choose a convention for moves as in
@minimal-fig-nonmin. We will adopt the $\LP+\RP$ as our prefered form.
```

Bonahon and Seibenmann show in @wpt-equi-lemma-exist that these conditions are
sufficient to realize every arborescent tangle. In fact, every weighted planar
tangle tree can be turned into a CWPTT by a series of moves in an extended
calculus on weighted planar trees [@bonahonNewGeometricSplittings2016]. We call
this process **canonization** of a weighted planar tangle tree.

```{prf:corollary} Existance of CWPTT, Bonahon and Seibenmann Corollary 12.20 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-lemma-exist

Every arborescent tangle is obtained by plumbing operations from
arborescent tangles associated to positively (or negatively)
canonical weighted planar trees (with labels in $V_4$ at free bonds).
```

We note some consequences of the positivity and negativity condition. First, a
positive CWPTT ($\LP +\RP$-CWPTT) can be transformed by a sequence of moves in
the extended calculus of weighted planar trees into a negative CWPTT
($\LP -\RP$-CWPTT). Similarly, a negative CWPTT can be transformed into a
positive CWPTT. Second, we note that a CWPTT can be both positive and negative,
we will refer to these trees as **neutral** trees.

Bonahon and Seibenmann give a classification of arborescent tangles via moves on
CWPTT.

```{prf:theorem} Classification Theorem for Canonical Weighted Planar Tangle Trees, Bonahon and Seibenmann theorem 12.21 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-thm-classi
Consider two positive (or negative) CWPTT
$\Gamma^{\,}$ and $\Gamma^\prime$, with free bonds labeled by
elements of $V_4$. Plumbing according to $\Gamma$ and $\Gamma^\prime$
gives isomorphic arborescent tangles if and only if $\Gamma$ and
$\Gamma^\prime$ can be deduced from each other by a sequence of moves
($F_1$), ($F_2$), ($F_3^\prime$), and the modified ring moves $\LP\pm R\RP$.
```

Further, Bonahon and Seibenmann describe an algorithm for producing these
sequences of moves. This algorithm will be useful to us in
@sec-rlitt-generation.

```{prf:theorem} Bonahon and Seibenmann theorem 12.19 [@bonahonNewGeometricSplittings2016]
:label: wpt-equi-cor-algo
There exists an effective algorithm which, for any weighted planar tree $\Gamma$
with free bonds labeled by elements of $V_4$, alters $\Gamma$ by a sequence of
moves of the calculus of arborescent tangles to produce a collection of
positively (or negatively) canonical weighted planar trees.
```

##### Canonical Vertex

The conditions for a weighted planar tree to be a CWPTT are phrased for the
global context of a weighted planar tangle tree. We now contextualize those
conditions for a local view, a single vertex of the tree.

```{prf:definition}
:label: vertex-canon-def
A vertex $v_i$ of a weighted planar tangle tree $\Gamma$ with a single free
bond labeled from $V_4$ is said to be **$\LP+\RP$-canonical** if $v_i$ has at
most one non-zero weight $w_i$, and $i$ is zero (the root) with no conditions or
$i$ is not zero with the following conditions satisfied:

1.   If the valence of $v_i$ is $1$ and all of:
        -   $w_i\neq 0$ unless $i=1$ and $w_0=0$ (the weight of the root)
        -   $w_i\neq \pm 1$
        -   If the valence of $v_{i-1}$ (the parent) is $2$ then
            $\text{sign}\LP w_i\RP\neq\text{sign}\LP w_{i-1}\RP$ unless $i=1$ and
            $w_0=0$
        -   If the valence of $v_{i-1}$ (the parent) is greater than $2$ then
            $w_i\neq -2$
2.   If the valence of $v_i$ is $2$ and all of:
        -   $w_i\neq 0$
        -   If valence of the parent or valence of the child is greater than $2$ (is
            essential) then $w_i\neq \pm1$
        -   If valence of the parent and valence of the child is greater than $2$
            (both are essential) then $w_i\neq \m2$
        -   If valence of the parent is $2$ then
            $\text{sign}\LP w_i\RP\neq\text{sign}\LP w_{i-1}\RP$ (the parent)
        -   If valence of the child is $2$ then
            $\text{sign}\LP w_i\RP\neq\text{sign}\LP w_{i+1}\RP$ (the child)
```

From this definition, we now show that these conditions are identical to those
in the global context of @wpt-equi-def-abcanon.

```{prf:theorem}
:label: vertex-and-cannon
$\Gamma$ is a $\LP+\RP$-CWPTT if and only if all the vertices of $\Gamma$ are
$\LP+\RP$-canonical.
```

```{prf:proof}

The forward implication follows directly from the definition of canonicity of a
tree. We take special consideration for the $0$ (@wpt-construc-fig-stick_cond-1)
and $\infty$ (@wpt-construc-fig-stick_cond-2) tangles. The zero tangle has a
single vertex, the root. The root of a CWPTT is always a $\LP+\RP$-canonical
vertex, satisfying the forward implication for the $0$ tangle. The $\infty$
tangle, again, has root which is a $\LP+\RP$-canonical vertex. We verify the
only non-root vertex, $v_1$, is a $\LP+\RP$-canonical vertex. The valence of
$v_1$ is $1$, so falls in the first condition we check each part in turn:

-   The weight $w_1$ is $0$ but $i=1$ and $w_0=0$, satisfying the part.
-   The weight $w_1$ is $0\neq \pm1$, satisfying the part.
-   The weight $i=1$ and $w_0=0$, satisfying the part.
-   The valence of the parent is 2, satisfying the part.

This shows $v_1$ to be the a $\LP+\RP$-canonical vertex. Other trees, follow a
similar process.

To show the reverse implication, we check the canonicity conditions, for each
condition we find a contradiction to the assumption that $\Gamma$ is not a CWPTT
but has only $\LP+\RP$-canonical vertices.

-   **Weight Condition:** We assume that there is a vertex that violates the
    weight condition. That is, there exists a $v_i\in \Gamma$ with
    $w_{i_0}\neq 0$ and $w_{i_1}\neq 0$, contradicting our assumption that
    $\Gamma$ has only canonical vertices.
-   Stick Condition:
    -   **No non-root vertex of a stick has zero weight:** We assume that there
        is a vertex $v_i$ that violates the stick condition by being a vertex
        that is not the root but has weight zero. Since $v_i$ is on a stick,
        $v_i$ has valence one or two. In either case, $v_i$ is not a canonical
        vertex, contradicting our assumption that $\Gamma$ has only canonical
        vertices.
    -   **No end vertex of a stick has weight $\pm 1$:** We assume that there is
        a vertex $v_i$ that violates the stick condition by being an end vertex
        of a stick with weight $\pm 1$ that is not the root. Since $v_i$ is the
        end of a stick, $v_i$ has valence one or two and has a parent, child, or
        both with valence greater than $2$ (essential). In both the valence 1
        and valence 2 cases, $v_i$ is then not a canonical vertex, contradicting
        our assumption that $\Gamma$ has only canonical vertices.
    -   **The non-zero weights on a stick alternate in sign:** We assume that
        there are a pair of vertices $v_i$ and $v_{i+1}$ on a stick that
        violates the stick condition with
        $\text{sign}\LP w_i\RP\neq\text{sign}\LP w_{i+1}\RP$. Our assumption
        makes $v_i$ have valence 2 ($v_{i+1}$ may be valence 1 or 2), $v_i$ is
        then not a canonical vertex, contradicting our assumption that $\Gamma$
        has only canonical vertices.
-   Positivity Condition:
    -   **No stick is @wpt-construc-fig-positivity_cond-1:** We assume that
        there is a vertex $v_i$ that is the single vertex of the stick
        @wpt-construc-fig-positivity_cond-1. Since $v_i$ is valence one and is
        the only vertex of the stick, it has a parent of valence $2$. Since
        $w_i$ is $-2$, $v_i$ is then not a canonical vertex, contradicting our
        assumption that $\Gamma$ has only canonical vertices.
    -   **No stick is @wpt-construc-fig-positivity_cond-2:** We assume that
        there is a vertex $v_i$ that is the single vertex of the stick
        @wpt-construc-fig-positivity_cond-2. The valence of $v_i$ is two and is
        the only vertex of the stick; consequently, it has a parent and child of
        valence greater than $2$. Since $w_i$ is $-2$, $v_i$ is then not a
        canonical vertex, contradicting our assumption that $\Gamma$ has only
        canonical vertices.

The definition and proof for $\LP-\RP$-canonical vertices are identical.
Similarly to the canonical tree case, we define a third positivity class for a
vertex, the **neutral vertex**, a vertex that is both $\LP-\RP$-canonical and
$\LP+\RP$-canonical.

```
