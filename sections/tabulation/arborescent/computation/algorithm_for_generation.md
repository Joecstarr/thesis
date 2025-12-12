<!-- prettier-ignore-start -->
(sec-rlitt-generation)=
#### Generation of Right Leaning Identity Weighted Planar Tangle Trees
<!-- prettier-ignore-end -->

##### Generation of Rooted Plane Tree

Just as rooted plane trees serve as the scaffolding we built WPTT on, a rooted plane tree algorithm
will serve as the backbone for our RLITT generation algorithm. We will now give a brief description
of the generation algorithm for rooted plane trees given by Nakano
[@nakanoEfficientGenerationPlane2002]. We begin by defining the **rightmost path** of a rooted plane
tree $\Gamma$.

```{prf:definition} Nakano Section 2 [@nakanoEfficientGenerationPlane2002]

Let $v_0$ be the root and $v_i$ be the highest indexed leaf (vertex of valence
$\leq 1$) of a rooted plane tree $\Gamma$. The unique path
$\LP v_0,\,\cdots,\,v_i \RP$, in the standard graph theoretic sense, is called
the **rightmost path** of $\Gamma$.
```

Next, we define a grafting operation on rooted plane trees $\Gamma$ and $\Gamma^\prime$.

```{prf:definition}
:label: rli-gen-def-grafting_op

Let $\mathcal{T}^{p}_{n}$ be the set of rooted plane trees on $n$ vertices,
$\Gamma_r\in \mathcal{T}^{p}_{n}$ , and $\Gamma_s\in \mathcal{T}^{p}_{m}$.
Define the **grafting operation** as follows.

$$
\begin{aligned}
\star_i:\mathcal{T}^{rp}_{n}\times\mathcal{T}^{rp}_{m}&\to\mathcal{T}^{rp}_{n+m}\\
\Gamma_r\times\Gamma_s&\mapsto\Gamma_r\star_i\Gamma_s
\end{aligned}
$$

At the vertex $v_i$ of $\Gamma_r$, introduce an edge to the root of $\Gamma_s$.
Now, adjust the indexing of a vertex $s_k$ of $\Gamma_s$ as $v_{n+k}$, placing
$\Gamma_s$ as the rightmost child of $v_i$. This results in a rooted plane tree
$\Gamma\in \mathcal{T}^{rp}_{n+m}$.

When grafting at the root $v_0$ we omit the index label in the grafting
operation, that is, $\star_0$ is written simply as $\star$. We call $\Gamma_r$ the
**rootstock** and $\Gamma_s$ the **scion**.
```

````{prf:example}
:label:  rli-gen-fig-scion_grafting
```{figure} ../../media/bands/arbor_graph_grafting.svg
:width: 500px
```
Grafting a scion $\Gamma_s$ to a rootstock $\Gamma_r$ with $\Gamma_r\star_3\Gamma_s$
````

Now we are prepared to give the algorithm to generate all rooted plane trees of a given size that
are created from $\Gamma$ by a sequence of $\star_\ast$ operations on the rightmost path of
$\Gamma$.

```{algorithm} Find all rooted plane trees of a given size created from $\Gamma$ [@nakanoEfficientGenerationPlane2002]
:label: find-all-related-trees

**Input**

-   A tree $\Gamma\in \mathcal{T}^{rp}_{i}$, $i<n$
-   A target size $n\in T$

**Output**

-   All collections of trees $\Gamma\in \mathcal{T}^{rp}_{n}$ created from $\Gamma$

**Routine**

1. Set $P$ to the rightmost path of $\Gamma$
2. Set $\Gamma_1$ as the single vertex rooted plane tree
3. If the number of vertices of $\Gamma$ is $n$ exit the algorithm
4. For each vertex $v_i$ in $P$
    1. Graft $\Gamma_1$ onto $\Gamma$ as $\Gamma\star_i \Gamma_1=\Gamma^\prime$
    2. Start a new instance of [](#find-all-related-trees) with
       $\Gamma=\Gamma^\prime$ and size=size
```

This algorithm can be extended to an algorithm that finds all rooted plane trees up to a given size
as follows.

```{algorithm} Efficient generation of rooted plane trees [@nakanoEfficientGenerationPlane2002]
:label: find-efficient-trees

**Input**

-   A target number of vertices of a tree $n\in \Z$

**Output**

-   All trees $\Gamma\in \mathcal{T}^{rp}_{n}$

**Routine**

1. Set $\Gamma_1$ as the single vertex rooted plane tree
2. Execute [](#find-all-related-trees) with $\Gamma=\Gamma_1$ and $n=n$
```

##### Modification for RLITT

The algorithm described above serves as the inspiration for the algorithm we will build now for the
enumeration of the arborescent tangles. Building this algorithm begins with modifying the grafting
$\star_i$ operation to operate on weighted planar tangle trees as follows.

```{prf:definition}
:label: rli-gen-def-grafting_op-wpt

The **grafting operation** $\star_i$ for weighted planar tangle trees, we require
that the free bond of the scion be grafted to $v_i$. We also specify that the
scion be grafted so that the rightmost weight of $v_i$ remains to the right of
the scion after grafting; this can be seen in
@rli-gen-fig-scion_grafting_wth_weight.
```

````{figure}
:label:rli-gen-fig-scion_grafting_wth_weight

```{figure} ../../media/bands/awptt_graph_pregraft.svg
:label:  rli-gen-fig-scion_grafting_wth_weight_1
:width: 500px

A rootstock $\Gamma_r=\iota\LP \LP2\LP2\LB3\RB2\LB -3\RB3\RP \LB3\RB4\RP 4\RP$ in grey and scion $\Gamma_s=\iota\LB 10\ 9 \RB$ in orange. Each vertex is
labeled with its index in the order on $\Gamma$.
```

```{figure} ../../media/bands/awptt_graph_grafted.svg
:label:  rli-gen-fig-scion_grafting_wth_weight_2
:width: 500px

Grafting at $v_2$ yields $\Gamma_r\star_2\Gamma_s=\iota\LP \LP2\LP2\LB3\RB2\LB -3\RB\LB 10\ 9 \RB 3\RP \LB3\RB4\RP 4\RP$
```
````

Just as we have adjusted the grafting operator, we must adjust the Nakano algorithm so it is aware
of the extra data in an RLITT. The initial reaction to this problem may be to simply annotate the
scion of the grafting operation with the weights necessary to reach a target TCN. Unfortunately,
this method quickly runs into issues generating even just the Montesinos tangles, a smaller class of
tangle described by [@bonahonNewGeometricSplittings2016]. We must make a slightly more radical
change to the Nakano algorithm, that being, grafting an entire RLITT to only the root $v_0$ of the
rootstock. We will now show that a list of integral tangles (single vertex RLITT
@wpt-construc-sec-integral) combined with grafting at the root generates all $\LP+\RP$-RLITT. To
start, we will prove that each $\LP+\RP$-RLITT is integral or the result of grafting weighted planar
tangle trees at the root.

```{prf:theorem}
:label: rli-gen-const-thm-acnm1toacn

Every $\Gamma$ $\LP+\RP$-RLITT of TCN $n$ is one of two forms:

1. $\Gamma$ is a single vertex with weight $\pm n$.
2. $\Gamma$ is the result of grafting at the root of some rootstock $\Gamma_r$
   and $\LP+\RP$-RLITT scion $\Gamma_s$ where:
    1. In $\Gamma_r$, $v_0$ is valence two, and $v_1$ is canonical
       except for violating the stick condition by
       $\text{Sign}\LP v_0\RP=\text{Sign}\LP v_1\RP$. Each vertex in
       $\LS v_i\RS_{i=2}^n$ of $\Gamma_r$ is $\LP +\RP$-canonical.
    1. $\Gamma_r$ is $\LP+\RP$-RLITT
```

```{prf:proof}
Let $\Gamma$ be a $\LP +\RP$-RLITT, we have three cases based on the valence of
$v_0\in \Gamma$.

Valence of $v_0$ is:

1. **One:** $\Gamma$ is integral (@wpt-construc-sec-integral), we fall into
   the first condition.
2. **Two:** $\Gamma$ is a stick at the root, we let $\Gamma_r=\iota\LB w_0\RB$
   and $\Gamma_s=\iota\LP\alpha w_1\RP$, where $\alpha$ is the remaining
   vertices, weights, and bonds of $\Gamma$. $\Gamma_r$ is integral, and as such
   is $\LP+\RP$-RLITT. Now to show that $\Gamma_s$ is $\LP+\RP$-RLITT. Since
   $\Gamma$ is $\LP+\RP$-RLITT, each $v_i$ in $\Gamma$ is canonical. Each vertex
   in $\Gamma_s$ is also in $\Gamma$, so $\Gamma_s$ has only canonical vertices
   and by @vertex-and-cannon is $\LP+\RP$-canonical. Finally, since locations of
   weights are unchanged and grafting requires the scion to have identity label
   $\Gamma_s$ is $\LP+\RP$-RLITT.
3. **Three:** The root of $\Gamma$ has two children, we let $\Gamma_s$ be the tree
   with the right child of $v_0$ as a root and
   $\Gamma_r=\iota\LP \alpha w_0\RP$, where $\alpha$ is the remaining vertices,
   weights, and bonds of $\Gamma$. Showing $\Gamma_s$ is $\LP+\RP$-RLITT follows
   identically as it did in the first form.

    We now show $\Gamma_r$ is $\LP+\RP$-RLITT. First, given that $\Gamma$ is
    $\LP+\RP$-RLITT, each $v_i$ in $\Gamma$ is canonical, consequently each
    vertex that is unchanged in $\Gamma_r$ ($\LS v_i\RS_{i=2}^n$) is canonical.
    The vertices that differ in $\Gamma_r$ are $v_0$ and $v_1$, $v_0$ remains
    the root of $\Gamma_r$ so is canonical. Showing the canonicity of $v_1$
    depends on the the valence of $v_1$. When the valence is 0 or is greater
    than 2, $\Gamma_r$ is $\LP+\RP$-RLITT by the same argument as $\Gamma_s$.
    When $v_1$ is valence 1 or $2$, $\Gamma_r$ begins with a stick, and $v_1$
    continues to satisfy the weight, positivity, and the $\pm 1$ and $0$ portion
    of the stick condition. For the sign condition, when the signs agree, we are
    in form 2.1 of this theorem, and when they disagree, we are in form 2.2.

4. **Greater than Three:** The final case is when the valence of $v_0$ is greater
   than three. We let $\Gamma_s$ be the tree with the right child of $v_0$ as a
   root and $\Gamma_r=\iota\LP \alpha w_0\RP$, where $\alpha$ is the remaining
   vertices, weights, and bonds of $\Gamma$. Both $\Gamma_r$ and $\Gamma_s$
   follow the same argument used for $\Gamma_s$ of the valence 1 case.
```

An identical theorem can be phrased for the $\LP-\RP$-RLITT case. With this result, we can start our
construction of a grafting algorithm for arborescent tangles.

```{algorithm} Find weighted planar trees by grafting RLITT scions to the root of RLITT rootstocks
:label: find-grafted-trees

**Input**

-   A collection of of RLITT scions $T_s$
-   A collection of RLITT rootstocks $T_r$

**Output**

-   A collection of weighted planar trees

**Routine**

1. for each combination of $\Gamma_r\in T_r$ and $\Gamma_s \in T_s$
    1. Compute $\Gamma_r\star \Gamma_s$
```

Executing the algorithm with $\Gamma_r=\LS \iota\LB 1\RB\RS$ as the rootstock and
$\Gamma_s=\LS \iota\LB 2\ 0\RB\RS$ produces the tangle $\iota\LB 2\ 0\ 1\RB$. Unfortunately, this
resultant tangle violates the stick condition and hence is not canonical. The remainder of this
subsection will refine the grafting algorithm to satisfy each of the RLITT conditions.

###### Weight Condition

The simplest condition to verify is the weight condition. By construction, grafting the rootstock
and scion introduces no additional weights at the grafting vertex. Meaning, the weight condition is
satisfied with no adjustment to the algorithm.

###### Identity Condition

The next RLITT condition to address is the identity condition. We note that the $\star_i$ operation
does not modify the $V_4$ label of the rootstock. This observation means if the rootstock is
identity, the grafted tree will also be identity.

<!-- prettier-ignore-start -->
(rli-gen-sec-stick-con)=
###### Stick Condition
<!-- prettier-ignore-end -->

To start with the stick condition we will prove that if grafting produces a non-canonical tree the
non-canonical vertex must be adjacent to the root.

```{prf:theorem}
:label: only-the-root-matters
For $\Gamma_r$ a $\LP+\RP-$RLITT and $\Gamma_s$ a $\LP+\RP-$RLITT scion,
the result of $\Gamma=\Gamma_r\star\Gamma_s$ is canonical, if all
$v_i$ at distance $1$ or less from the root are canonical.
```

```{prf:proof}
We need to show that each vertex $v_i$ at a distance greater than one from the
root of $\Gamma=\Gamma_r\star\Gamma_s$ is canonical. The vertex $v_i$ is also a
vertex of either $\Gamma_r$ or $\Gamma_s$. If the vertex is in $\Gamma_r$ then
$v_i$ has a parent in $\Gamma_r$ and if the valence of $v_i$ is 2 or more
$v_i$ also has children in $\Gamma_r$. The parent and children in $\Gamma$ are
the same as the parent and children in $\Gamma_r$. Since $\Gamma_r$ is RLITT
$v_i$ is canonical in $\Gamma_r$ and since it shares a parent and children in
$\Gamma$ it is also canonical in $\Gamma$. Similarly, for $v_i$ in the scion,
showing canonicity of grafting is dependent only on the canonicity of the
vertices at a distance up to one from the root.
```

The $\LP-\RP$-RLITT case is shown identically, covering the majority of possibilities. However, we
need to take special care when grafting a non-negative to a non-positive tree (or the reverse).
Before we address that case we define a restricted class of scions that, after grafting, satisfy the
nonzero portion of the stick condition.

```{prf:definition}
A $\LP+\RP-$RLITT (respectively $\LP+\RP-$RLITT) $\Gamma$ with root weight $w_0$
is called a **good scion** when either:

1. $w_0\neq0$
2. $w_0=0$ and the valence of $v_0$ is greater than $2$ (essential)
```

```{prf:theorem}
:label: positive-and-negative-dont-mix
For $\Gamma_r$ a non-negative $\LP+\RP-$RLITT, and $\Gamma_s$ a good
non-positive $\LP-\RP-$RLITT scion, the result of
$\Gamma=\Gamma_r\star\Gamma_s$ is non-canonical.
```

```{prf:proof}
$\Gamma_r$ is a non-neutral $\LP+\RP-$RLITT, so it has a non-root vertex $v_{i}$,
which is a stick of the form @wpt-construc-fig-positivity_cond-1 or
@wpt-construc-fig-positivity_cond-2. Similarly, $\Gamma_s$ is a non-neutral
$\LP+\RP-$RLITT, so it has a non-root vertex $v_{j}$, which is a stick of the
form @wpt-construc-fig-negativity_cond-1 or @wpt-construc-fig-negativity_cond-2.
Since, $v_i$ and $v_j$ are not at the root, they remain sticks of the form
@wpt-construc-fig-positivity_cond-1, @wpt-construc-fig-positivity_cond-2,
@wpt-construc-fig-negativity_cond-1, or @wpt-construc-fig-negativity_cond-2
after grafting. Making $\Gamma$ neither $\LP+\RP-$RLITT nor $\LP-\RP-$RLITT, as
we desired.
```

```{algorithm} Find weighted planar trees by grafting RLITT good scions to the root of RLITT rootstocks
:label: find-grafted-good-trees


**Input**

-   A collection of RLITT good scions $T_s$
-   A collection of RLITT rootstocks $T_r$

**Output**

-   A collection of weighted planar trees (still not guaranteed to be RLITT)

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma_r \in T_r$
    1. Compute $\Gamma = \Gamma_r\star \Gamma_s$
    1. for each vertex $v_i$ at distance 1 from the root of $\Gamma$
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the stick condition
    1. Report $\Gamma$

```

<!-- prettier-ignore-start -->
(rli-gen-sec-pm-con)=
###### Positivity/Negativity Condition
<!-- prettier-ignore-end -->

Our approach to the positivity and negativity condition follows our approach to the stick condition.
We will leverage @only-the-root-matters to add a check for positivity and negativity in our
algorithm.

```{algorithm} Find weighted planar trees by grafting $\LP+\RP$-RLITT good scions to the root of $\LP+\RP$-RLITT rootstocks
:label: find-grafted-good-trees-p


**Input**

-   A collection of $\LP+\RP$-RLITT good scions $T_s$
-   A collection of $\LP+\RP$-RLITT rootstocks $T_r$

**Output**

-   A collection of weighted planar trees (still not guaranteed to be RLITT)

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma_r \in T_r$
    1. Compute $\Gamma = \Gamma_r\star \Gamma_s$
    1. for each vertex $v_i$ at distance 1 from the root of $\Gamma$
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the stick condition
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the positivity condition
    1. Report $\Gamma$
```

```{algorithm} Find weighted planar trees by grafting $\LP-\RP$-RLITT good scions to the root of $\LP-\RP$-RLITT rootstocks
:label: find-grafted-good-trees-n


**Input**

-   A collection of $\LP-\RP$-RLITT good scions $T_s$
-   A collection of $\LP-\RP$-RLITT rootstocks $T_r$

**Output**

-   A collection of weighted planar trees (still not guaranteed to be RLITT)

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma_r \in T_r$
    1. Compute $\Gamma = \Gamma_r\star \Gamma_s$
    1. for each vertex $v_i$ at distance 1 from the root of $\Gamma$
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the stick condition
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the negativity condition
    1. Report $\Gamma$
```

###### Right Leaning Condition

Satisfying the right leaning condition is a consequence of the modified $\star_i$ operation. Our
definition of the $\star_i$ operation grafts the scion in such a way that weights at $v_i$ are
always right of the scion. To fully satisfy the right leaning condition, we need to ensure that any
stick subtrees of are in the right most postions. This is accomplished with a slight modification of
our grafting algorithms.

```{algorithm} Find weighted planar trees by grafting $\LP+\RP$-RLITT good scions to the root of $\LP+\RP$-RLITT rootstocks
:label: find-grafted-good-trees-p-r


**Input**

-   A collection of $\LP+\RP$-RLITT good scions $T_s$
-   A collection of $\LP+\RP$-RLITT rootstocks $T_r$

**Output**

-   A collection of RLITT

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma_r \in T_r$
    1. Compute $\Gamma = \Gamma_r\star \Gamma_s$
    1. Shift ring subtrees of the root of $\Gamma$ to the right
    1. for each vertex $v_i$ at distance 1 from the root of $\Gamma$
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the stick condition
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the positivity condition
    1. Report $\Gamma$
```

```{algorithm} Find weighted planar trees by grafting $\LP-\RP$-RLITT good scions to the root of $\LP-\RP$-RLITT rootstocks
:label: find-grafted-good-trees-n-r


**Input**

-   A collection of $\LP-\RP$-RLITT good scions $T_s$
-   A collection of $\LP-\RP$-RLITT rootstocks $T_r$

**Output**

-   A collection of RLITT

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma_r \in T_r$
    1. Compute $\Gamma = \Gamma_r\star \Gamma_s$
    1. Shift ring subtrees of the root of $\Gamma$ to the right
    1. for each vertex $v_i$ at distance 1 from the root of $\Gamma$
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the stick condition
        1. Continue to the next iteration of the outer loop if $v_i$ fails to satisfy the negativity condition
    1. Report $\Gamma$
```

##### Full Generation Algorithm

The algorithm we have developed so far generates new RLITT from two restricted collections of trees.
Unfortunately, it doesn't yet tell us how to select the collections that guarantee the generation of
all arborescent tangles up to a target TCN are represented. The final step in the generation scheme
is describing how to build these collections. With computer enumeration in mind, we would like for
our strategy to be easily split into jobs that can be run in parallel.

We observe that when grafting $\Gamma_r\star_i\Gamma_s=\Gamma$, the TCN $r$ of $\Gamma_r$ and the
TCN $s$ of $\Gamma_s$, sum to the TCN of $\Gamma$. This observation is the key underpinning of the
strategy we use to define discrete generation jobs. For a target TCN we have the integer pairs seen
in [equation (%s)](#rli-gen-eq-buckets) that sum to the target TCN. Each of these pairs defines two
classes, determined by TCN, of RLITT that can be grafted.

```{math}
:label: rli-gen-eq-buckets
\begin{aligned}
(0&,\text{TCN})\\
( 1&,\text{TCN}-1)\\
&\vdots\\
(\text{TCN}-1&,1)\\
(\text{TCN}&,0)
\end{aligned}
```

The next question we should ask is if we can simplify the list at all. First, as we saw in the
discussion of the stick condition [](#rli-gen-sec-stick-con), we need our scions to be good. This
means we cannot have $1$ or $0$ in the second position of the pair, excluding $(\text{TCN}-1,1)$ and
$(\text{TCN},0)$ from the list. Second, the pair $(0,\text{TCN})$ will be excluded from our list,
since the zero-crossing tangle $\iota[0\ 0]$ can't serve as rootstock; grafting any scion would
violate the stick condition. We will recover tangles with root weight $0$ with a post-processing
step.

The following is the recursive algorithm used to take us from the set of RLITT with $\text{TCN}-1$
to the set of RLITT of the target TCN.

```{algorithm} Find RLITT of given TCN from all RLITT of TCN-1
:label: find-rlitt-from-acnm1toacn


**Input**

-   A target TCN
-   All RILTT up to TCN-1

**Output**

-   A set $T$ of all RLITT of TCN

**Routine**

1. Set $i=1$
1. Set $N=\text{TCN}-1$
1. Set $T$ to the set $\LS \iota[\text{TCN}], \iota[0\ \text{TCN}]\RS$
1. For each pair $(i,N-i)$
    1. Set $T_{s+}$ to be the set of $+$-RLITT good scions with TCN
       equal to $\text{N}-i$
    1. Set $T_{s-}$ to be the set of $(-)$-RLITT good scions with TCN
       equal to $\text{N}-i$
    1. Set $T_{r+}$ to be the set of $(+)$-RLITT TCN equal to $i$
    1. Set $T_{r-}$ to be the set of $(-)$-RLITT TCN equal to $i$
    1. Execute [](#find-grafted-good-trees-n-r) with input $T_{r-}$ and $T_{s-}$
    1. Add the results to $T$
    1. Execute [](#find-grafted-good-trees-p-r) with input $T_{r+}$ and $T_{s+}$
    1. Add the results to $T$
1. For every RLITT $\Gamma$ in $T$
    1. Continue to the next iteration of the loop if root of $\Gamma$ is valence two with weight zero
    1. Compute $\iota[0]\star\Gamma$ and add to T
```

```{algorithm} Find RLITT up to a given TCN
:label: find-rlitt-up-to-acn


**Input**

-   A target TCN

**Output**

-   A set $T$ of all RLITT up to TCN

**Routine**

1. Set $T$ to be the set $\LS \iota[0],\ \iota[0\ 0],\ \iota[1],\ \iota[-1],\ \iota[2],\ \iota[-2],\,\ \iota[2\ 0],\ \iota[-2\ 0]\RS$
2. for i from 3 to TCN
    1. Execute [](#find-rlitt-from-acnm1toacn) with input TCN $i$ and RLITT set
       $T$.
    1. Add the results to $T$
```

It is important to note that the output of [](#find-rlitt-up-to-acn) includes duplicates in the form
of $\LP+\RP$-RLITT and $\LP-\RP$-RLITT pairs. To deduplicate our list so it contains only
topologically unique objects, we select from the list the collection of $\LP+\RP$-RLITT.
