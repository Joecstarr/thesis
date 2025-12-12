<!-- prettier-ignore-start -->
(sec-minimalization)=
#### Minimalization of CWPTT
<!-- prettier-ignore-end -->

##### CWPTT are Not Minimal

A common measure for the complexity of knots and their relatives is the
**minimal crossing number**. That being the least number of crossings needed to
realize the object in a diagram, we call that diagram the **minimal diagram**.
It is natural to ask if our CWPTT are minimal representatives among either all
representations or arborescent representations. A quick analysis of the process
of canonization demonstrates that CWPTT are unfortunately far from minimal even
among arborescent representatives. An example of canonizing a tangle, making
that tangle non-minimal, is seen in @minimal-fig-nonmin_min.

````{figure}
:label:minimal-fig-nonmin

```{figure} ../../media/bands/non-minimal_minimalized.svg
:label: minimal-fig-nonmin_min
:width: 500px

A minimal presentation of a arborescent tangle in both its orthogonal projection
as well as its weighted planar tree.
```

```{figure} ../../media/bands/non-minimal.svg
:label: minimal-fig-nonmin_non
:width: 500px

A non-minimal presentation of the same arborescent tangle as
@minimal-fig-nonmin_min in both its orthogonal projection as well as its CWPTT.
```

````

##### Canonization Can Increase Complexity

As we have seen, a CWPTT often does not realize a minimal crossing
representative for an arborescent tangle. Since minimal crossing number is such
a common measure for complexity, we should understand how canonization impacts
the crossing number complexity of a CWPTT. We will accomplish this by
identifying a (non-unique) minimal arborescent representative for each tangle.
That is, a weighted planar tangle tree with minimal TCN among all weighted
planar tangle trees in its equivalence class. To begin we expand our
understanding of the moves in the calculus of arborescent tangles to those that
alter weights arithmetically. These moves are related to the arithmetic
operations on continued fractions [@bonahonNewGeometricSplittings2016].

````{prf:definition} Bonahon and Seibenmann Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: minimal-def-arithmetic
When carrying out the following **arithmetic moves** the relative positions of weights are
critical to the invariance of the underlying knot pair.
- (0.1) The **0.1 move** replaces the left side with the right side of @minimal-fig-move01.
    ```{figure} ../../media/bands/moves/0/1/def.svg
    :label: minimal-fig-move01
    :width: 500px

    Move 0.1 on a weighted planar tree.
    ```
- (0.2) The **0.2 move** replaces the left side with the right side of @minimal-fig-move02. Additionally, the cyclic order of all descendants in the purple subtree is reversed and $\zeta$ ($Z$-axis rotation @wpt-construc-fig-k4g-z). The vertices $a$ and $b$ need not be valence two, either or both may have a valence greater than two.
    ```{figure} ../../media/bands/moves/0/2/def.svg
    :label: minimal-fig-move02
    :width: 500px

    Move 0.2 on a weighted planar tree.
    ```
- (1.1) The **1.1 move** replaces the left side with the right side of @minimal-fig-move11.
    ```{figure} ../../media/bands/moves/1/1/def.svg
    :label: minimal-fig-move11
    :width: 500px

    Move 1.1 on a weighted planar tree.
    ```
- (1.2) The **1.2 move** replaces the left side with the right side of @minimal-fig-move12. The vertices $a$ and $b$ need not be valence two, either or both may have a valence greater than two.
    ```{figure} ../../media/bands/moves/1/2/def.svg
    :label: minimal-fig-move12
    :width: 500px

    Move 1.2 on a weighted planar tree.
    ```
- (2.1) Replace the left side with the right side of @minimal-fig-move21
    ```{figure} ../../media/bands/moves/2/1/def.svg
    :label: minimal-fig-move21
    :width: 500px

    Move 2.1 on a weighted planar tree.
    ```
- (2.2) Replace the left side with the right side of @minimal-fig-move22. The vertices $a$ and $b$ need not be valence two, either or both may have a valence greater than two.
    ```{figure} ../../media/bands/moves/2/2/def.svg
    :label: minimal-fig-move22
    :width: 500px

    Move 2.2 on a weighted planar tree.
    ```
````

```{note}
The 2.1 and 2.2 moves are what allow us to pass between the $\LP+\RP$ and
$\LP-\RP$ canonical classes of trees.
```

From here we will show that canonization of minimal trees increases TCN
complexity in a controlled manner.

```{prf:theorem}
:label: minimal-thm-minimal
A minimal tree canonizes to $\LP+\RP$-CWPTT, with only the moves (1.2), (2.1),
and (2.2) increasing TCN.
```

```{prf:proof}
Let $\Gamma$ be a minimal TCN arborescent representative of its equivalence
class. Starting with the weight condition (W) and the second portion of the
stick condition (S.2) concerning sticks having non-zero weights. Maximally apply
to $\Gamma$ moves $F_3$, (0.1), and (0.2). This removes zero weights and
consolidates weights of each vertex, $\Gamma$ now satisfies the conditions (S.2)
and (W) while remaining minimal. We consider condition (S.1), the alternating
condition. In the general canonization process (S.1) is handled by application
of move (1.2). However, on a pair of vertices violating (S.1) move (1.2)
decreases the TCN. This means by minimality of $\Gamma$ (S.1) must already be
satisfied. We are left now with conditions (S.3) and (P). Canonization of
$\Gamma$ to satisfy these conditions involves application of moves (1.2), (2.1),
and (2.2). Similarly to our (S.1) case, $\Gamma$ is minimal, so (1.2), (2.1),
and (2.2) cannot decrease TCN. However, (1.2), (2.1), and (2.2) may increase TCN
by 1, 1, and 2 respectively.
```

Working in the contrapositive, @minimal-thm-minimal tells us that a minimal tree
can be constructed from a CWPTT by application of TCN decreasing moves (1.2),
(2.1), and (2.2). It is important to note that this does not guarantee that
every set of applications of the (1.2), (2.1), and (2.2) moves to a CWPTT
minimizes the TCN, only the existence of a path to a minimal tree.

##### Bounding complexity

We now introduce a bound on complexity between a CWPTT and a minimal
representation of that tree. We note that @minimal-thm-minimal indicates that
any opportunities to decrease TCN in a CWPTT are found on the boundary between
an essential vertex and a stick of the tree. Particularly, at least one weight
used in the execution of (1.2), (2.1), and (2.2) must be carried by an essential
vertex.

```{prf:lemma}
:label: minimal-lemma-weights
The sum of the weights of all essential vertices of a CWPTT is at
most $\text{TCN}-4$.
```

```{prf:proof}
The weight of an essential vertex of a CWPTT is maximized when consolidated on
at a single vertex. By definition, each essential vertex has at least two
children. In a CWPTT the least value that can be carried by a leaf vertex is
$2$. Combining these gives us the desired bound.
```

```{prf:theorem}
For a CWPTT $\Gamma$, the difference in TCN between $\Gamma$ and the minimal tree $\Gamma_m$ is bounded as:
$$\text{TCN}\LP\Gamma\RP-\text{TCN}\LP\Gamma_m\RP\leq\sum\abs{\text{weights of essential vertices of }\Gamma}\leq \text{TCN}-4$$
```
