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


A minimal presentation of a arborescent tangle in both its orthogonal projection
as well as its weighted planar tree.
```

```{figure} ../../media/bands/non-minimal.svg
:label: minimal-fig-nonmin_non


A non-minimal presentation of the same arborescent tangle as
@minimal-fig-nonmin_min in both its orthogonal projection as well as its CWPTT.
```
Minimal and non-minimal trees.
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

````{prf:definition} Bonahon and Siebenmann, Section 12.3 [@bonahonNewGeometricSplittings2016]
:label: minimal-def-arithmetic
When carrying out the following **arithmetic moves** the relative positions of weights are
critical to the invariance of the underlying knot pair.
- (0.1) The **0.1 move** replaces the left side with the right side of @minimal-fig-move01.
    ```{figure} ../../media/bands/moves/0/1/def.svg
    :label: minimal-fig-move01
    

    Move 0.1 on a weighted planar tree.
    ```
- (0.2) The **0.2 move** replaces the left side with the right side of @minimal-fig-move02. Additionally, the cyclic order of all descendants in the purple subtree is reversed and $\zeta$ ($Z$-axis rotation @wpt-construc-fig-k4g-z). The vertices $a$ and $b$ need not be valence two, either or both may have a valence greater than two.
    ```{figure} ../../media/bands/moves/0/2/def.svg
    :label: minimal-fig-move02
    

    Move 0.2 on a weighted planar tree.
    ```
- (1.1) The **1.1 move** replaces the left side with the right side of @minimal-fig-move11.
    ```{figure} ../../media/bands/moves/1/1/def.svg
    :label: minimal-fig-move11
    

    Move 1.1 on a weighted planar tree.
    ```
- (1.2) The **1.2 move** replaces the left side with the right side of @minimal-fig-move12. The vertices $a$ and $b$ need not be valence two, either or both may have a valence greater than two.
    ```{figure} ../../media/bands/moves/1/2/def.svg
    :label: minimal-fig-move12
    

    Move 1.2 on a weighted planar tree.
    ```
- (2.1) Replace the left side with the right side of @minimal-fig-move21
    ```{figure} ../../media/bands/moves/2/1/def.svg
    :label: minimal-fig-move21
    

    Move 2.1 on a weighted planar tree.
    ```
- (2.2) Replace the left side with the right side of @minimal-fig-move22. The vertices $a$ and $b$ need not be valence two, either or both may have a valence greater than two.
    ```{figure} ../../media/bands/moves/2/2/def.svg
    :label: minimal-fig-move22
    

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

```{prf:proof}Let $\Gamma$ be a minimal TCN arborescent representative
of its equivalence
class. Starting with the weight condition
(W) maximally apply $F_3$ consolidating the weights of each vertex.
$F_3$ may need to be reapplied after application of arithmetic moves
and does not impact TCN.

Next we handle the stick condition starting with condition S.0 concerning
sticks having non-zero weights. Maximally apply
to $\Gamma$ moves 0.1, and 0.2; this removes zero weights of
sticks. In the general canonization process S.A, the alternating
stick condition, is handled by application
of move 1.2. However, on a pair of vertices violating condition
S.A, move 1.2
decreases the TCN. This means by minimality of $\Gamma$, condition
S.A must already be
satisfied. Finally to obtain condition S.1, we apply moves 1.1 and
1.2, where move 1.2 may increase crossing number by 1.

The last condition to enforce is P, the positvity condition, which is
done by modifying $\Gamma$ by application of moves 2.1
and 2.2. Similarly to our S.1 case, $\Gamma$ is minimal, 2.1,
and 2.2 cannot decrease TCN. However, 2.1 and 2.2 may increase TCN
by 1 and 2 respectively.
```


We note that
@minimal-thm-minimal indicates that
any opportunities to decrease TCN in a CWPTT are found on the end
vertices of sticks adjacent to
an essential vertex. Particularly, at least one weight
used in the execution of 1.2, 2.1, and 2.2 must be carried by an essential
vertex. Reversing the sequence of moves in
@minimal-thm-minimal tells us that a
minimal tree can be constructed from a CWPTT by application of TCN
decreasing moves 1.2,
2.1, and 2.2. It is important to note that this does not guarantee that
every set of applications of the 1.2, 2.1, and 2.2 moves to a CWPTT
minimizes the TCN, only the existence of a path to a minimal tree.


##### Bounding complexity


We now introduce a bound on complexity between a CWPTT and a minimal
representation of that tree.  We build the bound by identifying the
maximum number of subtrees of a CWPTT which admit
a 1.2, 2.1, or 2.2 move. We begin by identifying the smallest TCN of a
subtree that admits each move. These minimal subtrees follow directly from
Definition~\ref{minimal-def-arithmetic} and our essential vertex
requirement. The smallest, by TCN, canonical subtree admitting move 1.2 is
7, as in @minimal-fig-minimize_move12.
For move 2.1 the smallest TCN for a canonical subtree is 5, as in
@minimal-fig-minimize_move21, and for 2.2 the smallest TCN is
10, as in @minimal-fig-minimize_move22. Combining these
smallest TCN subtrees with the how each move decreases TCN gives the
bound in @bound-arbor-cwptt, where $\Gamma_m$ is a
minimal representative for the
tangle class of $\Gamma$.

```{math}
:label: bound-arbor-cwptt
\begin{aligned}
\text{TCN}\LP\Gamma\RP-\text{TCN}\LP\Gamma_m\RP&\leq
1\cdot\left\lfloor\frac{\text{TCN}\LP\Gamma\RP}{7}\right\rfloor+1\cdot\left\lfloor\frac{\text{TCN}\LP\Gamma\RP}{5}\right\rfloor+2\cdot\left\lfloor\frac{\text{TCN}\LP\Gamma\RP}{10}\right\rfloor\\
&\leq
\frac{\text{TCN}\LP\Gamma\RP}{7}+\frac{\text{TCN}\LP\Gamma\RP}{5}+2\cdot\frac{\text{TCN}\LP\Gamma\RP}{10}\\
&=\frac{\text{TCN}\LP\Gamma\RP\cdot 19}{35}\\
\end{aligned}
```

````{figure}
```{figure} ../../media/bands/moves/1/2/minimal.svg
:label: minimal-fig-minimize_move12
Admits move 1.2
```
```{figure} ../../media/bands/moves/2/1/minimal.svg
:label: minimal-fig-minimize_move21
Admits move 2.1
```
```{figure} ../../media/bands/moves/2/2/minimal.svg
:label: minimal-fig-minimize_move22
Admits move 2.2
```
Examples of
canoncial subtrees of a $\LP+\RP$-CWPTT which admit the given moves.
Note: These are subtrees admiting the moves, but not the only subtrees admiting
the moves.
````
