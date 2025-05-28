#### Generation of Right Leaning Identity Weighted Planar Tangle Trees

We are now prepared for the enumeration of the arborescent tangles. This section
will show the development of an algorithm that uniquely generates each
arborescent tangle. We will follow a similar guided development we saw in our
introduction of CWPTT in [](#construction_of_arbor).

##### Generation of Rooted Plane Tree

We will now give a brief description of a generation algorithm for rooted plane
trees given by Nakano [@nakanoEfficientGenerationPlane2002]. To give the
description, we will require some preliminary conventions and definitions. Let
$\Gamma$ be a rooted plane tree, $r$ be the root of $\Gamma$, and $v_i\neq r$ be
a vertex, with parent $p$. Further assume $v_i$ has order $i$, $p$ has order $j$
and the children $c_1,\,\cdots,\,c_n$ of $v$ have order $k_1,\,\cdots,\,k_n$. We
adopt the convention that the order on a rooted plane tree must satisfy the
following:

1.  $r$ has order $0$
2.  $j<i<k_1<\cdots k_n$

```{figure} ./media/bands/arbor_graph_with_order.svg
:label: wpt-construc-fig-order_unique
:width: 500px
A rooted plane tree $\Gamma$ with vertices labeled in the order of $\Gamma$.
```

With this convention, we define the **rightmost path** of a rooted plane tree
$\Gamma$.

```{prf:definition} Rightmost path of a rooted plane tree [@nakanoEfficientGenerationPlane2002]

Let $v_0$ be the root and $v_i$ be the highest indexed leaf (vertex of valence
$\leq 1$) of a rooted plane tree $\Gamma$. The unique path
$\LP v_0,\,\cdots,\,v_i \RP$, in the standard graph theoretic sense, is called
the **rightmost path** of $\Gamma$.
```

Next, we define a grafting operation on rooted plane trees $\Gamma$ and
$\Gamma^\prime$.

```{prf:definition} Grafting operation on rooted plane tree
:label: rli-gen-def-grafting_op

Let $\mathcal{T}^{rp}_{n}$ be the set of rooted plane trees on $n$ vertices,
$\Gamma_r\in \mathcal{T}^{rp}_{n}$ called the rootstock,
$\Gamma_s\in \mathcal{T}^{rp}_{m}$ called the scion, and $v_i$ the
$i^{\text{th}}$ vertex of $\Gamma_r$. Define the grafting operation as follows.

$$
\begin{aligned}
\star_i:\mathcal{T}^{rp}_{n}\times\mathcal{T}^{rp}_{m}&\to\mathcal{T}^{rp}_{n+m}\\
\Gamma_r\times\Gamma_s&\mapsto\Gamma
\end{aligned}
$$

Starting from the vertex $v_i$ of $\Gamma_r$, introduce an edge to the root of
$\Gamma_s$. Now, adjust the indexing of a vertex $w_k$ of $\Gamma_s$ as
$v_{n+k}$ This results in a rooted plane tree
$\Gamma\in \mathcal{T}^{rp}_{n+m}$.

When grafting at the root $v_0$ we omit the index label in the grafting
operation, that is $\star$ is written simply as $\star$.

```

````{prf:example}
:label:  rli-gen-fig-scion_grafting
```{figure} ./media/bands/arbor_graph_grafting.svg
:width: 500px
```
Grafting a scion $\Gamma_s$ to $\Gamma_r$ from {prf:ref}`wpt-construc-fig-order_unique` with $\Gamma_r\star_3\Gamma_s$
````

Now we are prepared to give the algorithm to generate all rooted plane trees of
a given size that are related to $\Gamma$ by a sequence of $\star_i$ on the
rightmost path of $\Gamma$.

```{prf:remark} Find all rooted plane trees of a given size related to $\Gamma$ [@nakanoEfficientGenerationPlane2002]
:label: find-all-related-trees

**Input**

-   A tree $\Gamma\in \mathcal{T}^{rp}_{n}$
-   A target size $n\in T$

**Output**

-   All collections of trees $\Gamma\in \mathcal{T}^{rp}_{n}$

**Routine**

1. Set $P$ to the rightmost path of $\Gamma$
2. Set $\Gamma_1$ as the single vertex rooted plane tree
3. If the number of vertices of $\Gamma$ is $n$ exit the algorithm
4. For each vertex $v_i$ in $P$
    1. Graft $\Gamma_1$ onto $\Gamma$ as $\Gamma\star_i \Gamma_1=\Gamma^\prime$
    2. Start a new instance of [](#find-all-related-trees) with
       $\Gamma=\Gamma^\prime$ and size=size

```

This algorithm can be extended to an algorithm that finds all rooted plane trees
up to a given size as follows.

```{prf:remark} Efficent generation of rooted plane trees [@nakanoEfficientGenerationPlane2002]
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

The algorithm described above serves as the inspiration for the algorithm we
will build here for the enumeration of the arborescent tangles. Building this
algorithm begins with modifying the grafting $\star_i$ operation to operate on
weighted planar tangle trees as follows.

```{prf:definition} Grafting operation on weighted planar tangle trees
:label: rli-gen-def-grafting_op-wpt


To adapt the grafting operation $\star_i$ defined in
{prf:ref}`rli-gen-def-grafting_op` for weighted planar tagle trees we require
that the free bond of the scion be grafted to $v_i$. We also specify that the
scion be grafted so that the rightmost weight of $v_i$ remain to the right of the
scion after grafting this can be seen in {prf:ref}`rli-gen-fig-scion_grafting_wth_weight`.
```

````{prf:observation}
:label:rli-gen-fig-scion_grafting_wth_weight

```{figure} ./media/bands/awptt_graph_pregraft.svg
:label:  rli-gen-fig-scion_grafting_wth_weight_1
:width: 500px

A rootstock $\Gamma_r=\iota\LP \LP2\LP2\LB3\RB2\LB -3\RB3\RP \LB3\RB4\RP 4\RP$ in grey and scion $\Gamma_s=\iota\LB 10\ 9 \RB$ in orange. Each vertex is
labeled with its index in the order on $\Gamma$.
```

```{figure} ./media/bands/awptt_graph_grafted.svg
:label:  rli-gen-fig-scion_grafting_wth_weight_2
:width: 500px

Grafting at $v_2$ yields $\Gamma_r\star_2\Gamma_s=\iota\LP \LP2\LP2\LB3\RB2\LB -3\RB \LP\LB 10\ 9 \RB \RP3\RP \LB3\RB4\RP 4\RP$
```
````

Just as we have adjusted the grafting operator, we must adjust the Nakano
algorithm so it is aware of the extra data in a RLITT. The initial reaction to
this problem may be to simply annotate the scion of the grafting operation with
the weights necessary to reach a target ACN. Unfortunately, this method quickly
runs into issues generating even just the Montesinos tangles, a smaller class
described in [@bonahonNewGeometricSplittings2016]. We must make a slightly more
radical change to the Nakano algorithm, that being, grafting an entire RLITT to
only the root $v_0$ of the rootstock. This modified version of the algorithm can
be seen in {prf:ref}`find-grafted-trees`.

```{prf:remark} Find weighted planar trees by grafting RLITT scions to the root of RLITT rootstocks
:label: find-grafted-trees

**Input**

-   A collection of of RLITT scions $T_s$
-   A collection of RLITT rootstocks $T_r$

**Output**

-   All collection of weighted planar trees

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma \in T_r$
    1. Compute $\Gamma_r\star \Gamma_s$
```

This modified algorithm serves as the backbone in our generation, but a quick
example with $\Gamma_r=\LS \iota\LB 1\RB\RS$ as the rootstock input and
$\Gamma_s=\LS \iota\LB 2\ 0\RB\RS$ as the scion input. When executed, the
algorithm will produce the tangle $\iota\LB 2\ 0\ 1\RB$, this output violates
the stick condition and hence is not a CWPTT. This can be rectified with
additional refinements to address each of the RLITT conditions.

###### Weight Condition

The simplest condition to verify is the weight condition. We select the
rootstock and scion to both satisfy the weight condition. Grafting the rootstock
and scion introduces no additional weights at the crafting vertex. Meaning, the
weight condition is satisfied with no additional adjustment.

###### Identity Condition

The next RLITT condition to address is the identity condition. We note that the
$\star_i$ operation does not modify the $V_4$ label of the rootstock. This
observation means if the rootstock is identity, the grafted tree will also be
identity.

###### Right Leaning Condition

Satisfying the right leaning condition is a consequence of the modified
$\star_i$ operation. Our definition of the $\star_i$ operation grafts the scion
in such a way that weights at $v_i$ are always right of the scion. This means
the grafted tree is right leaning again with no additional adjustment.

<!-- prettier-ignore-start -->
(rli-gen-sec-stick-con)=
###### Stick Condition
<!-- prettier-ignore-end -->

To tackle the stick condition, we first must ensure that the root of $\Gamma_s$
is essential, or the weight is not equal to zero or one, we call these **good
scions**. We need to ensure that grafting respects the alternating sign of
sticks, this requirement induces four possible cases to consider:

1.  $v_i$ of $\Gamma_r$ has valence $>2$ and $v_0$ of $\Gamma_s$ has valence
    $>2$
1.  $v_i$ of $\Gamma_r$ has valence $>2$ and $v_0$ of $\Gamma_s$ has valence
    $<2$
1.  $v_i$ of $\Gamma_r$ has valence $<2$ and $v_0$ of $\Gamma_s$ has valence
    $>2$
1.  $v_i$ of $\Gamma_r$ has valence $<2$ and $v_0$ of $\Gamma_s$ has valence
    $<2$

In the first case, both $v_0$ of $\Gamma_r$ and $v_0$ of $\Gamma_s$ are
essential, meaning grafting does not introduce or modify a stick. The second
case grafts a stick to an essential vertex, introducing a stick. Since
$\Gamma_s$ satisfies the alternating portion of the stick condition, the grafted
tree will also satisfy the alternating portion of the stick condition. In the
third case, an essential vertex is grafted to a stick, this modification doesn't
impact the alternating portion of the stick condition. The final case, is
grafting a stick onto a stick. For this grafting to respect the alternating
portion of the stick condition, the end vertex $v_i$ of $\Gamma_r$ must disagree
in sign with the root of $\Gamma_s$.

These considerations give us the following modified algorithm to generate trees
that satisfy the stick condition.

```{prf:remark} Find weighted planar trees by grafting RLITT good scions to the root of RLITT rootstocks
:label: find-grafted-good-trees


**Input**

-   A collection of RLITT good scions $T_s$
-   A collection of RLITT rootstocks $T_r$

**Output**

-   All collection of weighted planar trees

**Routine**

1. for each combination of $\Gamma_s\in T_s$ and $\Gamma_r \in T_r$
    1. Set $r$ to the root of $\Gamma_s$
    3. Continue to next iteration of the loop if $v_0\in \Gamma_r$ is the end vertex of
        a stick and $\text{sign}\LP v_0\RP= \text{sign}\LP r\RP$
    4. Compute $\Gamma_r\star \Gamma_s$
```

###### Positivity/Negativity Condition

The final condition of an RLITT we need to address is the positivity/negativity
condition. As we established in [](#sec-CWPTT-def) that a $\LP+\RP$-RLITT can be
transformed into a $\LP-\RP$-RLITT. We then established in
[](#rli-const-thm-ident_exists) that a $\LP+\RP$-RLITT is a unique
representative for a tangle. The requirement that we generate neutral tangles
such as $\iota\LB-3\ -2\RB$ means we cannot simply discount the $\LP-\RP$-RLITT
during the generation phase. To satisfy the conditions in the generation phase,
we require that when the rootstock is determined explicitly positive or
negative, the scion agree or be neutral. Meaning, if the rootstock is
$\LP+\RP$-RLITT then the scion must be $\LP+\RP$-RLITT or neutral, similarly for
$\LP-\RP$-RLITT. This gives us the three algorithms seen below.

```{prf:remark} Find weighted planar trees by grafting $\LP +\RP$-RLITT good scions to rightmost path of $\LP +\RP$-RLITT rootstocks
:label: find-grafted-good-ptrees

**Input**

-   A collection of $\LP+\RP$-RLITT or neutral good scions $T_s$
-   a collection of $\LP+\RP$-RLITT rootstocks $T_r$

**Output**

-   All collection of weighted planar trees

**Routine**

1. Execute [](#find-grafted-good-trees) with $T_s$ and $T_r$ as input
```

```{prf:remark} Find weighted planar trees by grafting $\LP -\RP$-RLITT good scions to rightmost path of $\LP -\RP$-RLITT rootstocks
:label: find-grafted-good-mtrees

**Input**

-   A collection of $\LP-\RP$-RLITT or neutral good scions $T_s$
-   a collection of $\LP-\RP$-RLITT rootstocks $T_r$

**Output**

-   All collection of weighted planar trees

**Routine**

1. Execute [](#find-grafted-good-trees) with $T_s$ and $T_r$ as input
```

```{prf:remark} Find weighted planar trees by grafting RLITT good scions to rightmost path of neutral RLITT rootstocks
:label: find-grafted-good-ntrees

**Input**

-   A collection of good scions $T_s$
-   a collection of neutral rootstocks $T_r$

**Output**

-   All collection of weighted planar trees

**Routine**

1. Execute [](#find-grafted-good-trees) with $T_s$ and $T_r$ as input
```

##### Full Generation Algorithm

The algorithm we have developed so far generates new RLITT from two restricted
collections of trees. Unfortunately, it doesn't yet tell us how to select the
collections that guarantee the generation of all arborescent tangles up to a
target ACN are represented. The final step in the generation scheme is
describing how to build these collections. With computer enumeration in mind, we
would like for our strategy to be easily split into jobs that can be run in
parallel.

We observe that when grafting $\Gamma_r\star_i\Gamma_s=\Gamma$, the ACN of
$\Gamma_r$ is $r$ and the ACN of $\Gamma_s$ is $s$ sum so that the ACN of
$\Gamma$ is $r+s$. This observation is the key underpinning of the strategy we
use to define discrete generation jobs. For a target ACN we have the integer
pairs seen in [equation (%s)](#rli-gen-eq-buckets) that sum to ACN. Each of
these pairs defines two classes, determined by ACN, of RLITT that can be
grafted.

```{math}
:label: rli-gen-eq-buckets
\begin{aligned}
(0&,\text{ACN})\\
( 1&,\text{ACN}-1)\\
&\vdots\\
(\text{ACN}-1&,1)\\
(\text{ACN}&,0)
\end{aligned}
```

The next question we should ask is if we can simplify the list at all. First, as
we saw in the discussion of the stick condition [](#rli-gen-sec-stick-con), we
need our scions to be good. This means we cannot have $1$ or $0$ in the second
position of the pair, excluding $(\text{ACN}-1,1)$ and $(\text{ACN},0)$ from the
list. Second, the pair $(0,\text{ACN})$ will be excluded from our list, since
the zero crossing tangle $\iota[0\ 0]$ can't serve as rootstock, grafting any
scion would violate the stick condition. We will recover tangles with root
weight $0$ with a post-processing step.

The following is the recursive algorithm used to take us from the set of RLITT
with $\text{ACN}-1$ to the set of RLITT of the target ACN.

```{prf:remark} Find RLITT of given ACN from all RLITT of ACN-1
:label: find-rlitt-from-acnm1toacn


**Input**

-   A target ACN
-   All RILTT up to ACN-1

**Output**

-   A set $T$ of all RLITT of ACN

**Routine**

1. Set $i=1$
1. Set $N=\text{ACN}-1$
1. Set $T$ to the set $\LS \iota[\text{ACN}], \iota[0\ \text{ACN}]\RS$
1. For each pair $(i,N-i)$
    1. Set $T_{s+}$ to be the set of $+$-RLITT good scions with ACN
       equal to $\text{N}-i$
    1. Set $T_{s-}$ to be the set of $-$-RLITT good scions with ACN
       equal to $\text{N}-i$
    1. Set $T_{sn}$ to be the set of neutral RLITT good scions with ACN
       equal to $\text{N}-i$
    1. Set $T_{r+}$ to be the set of $+$-RLITT ACN equal to $i$
    1. Set $T_{r-}$ to be the set of $-$-RLITT ACN equal to $i$
    1. Set $T_{rn}$ to be the set of neutral RLITT ACN equal to $i$
    1. Execute [](#find-grafted-good-mtrees) with input $T_{r-}$ and $T_{s-}$
    1. Execute [](#find-grafted-good-mtrees) with input $T_{r-}$ and $T_{sn}$
    1. Execute [](#find-grafted-good-ptrees) with input $T_{r+}$ and $T_{s+}$
    1. Execute [](#find-grafted-good-ptrees) with input $T_{r+}$ and $T_{sn}$
    1. Execute [](#find-grafted-good-ntrees) with input $T_{rn}$ and $T_{s-}$
    1. Execute [](#find-grafted-good-ntrees) with input $T_{rn}$ and $T_{s+}$
    1. Execute [](#find-grafted-good-ntrees) with input $T_{rn}$ and $T_{sn}$
    1. Add the results to $T$
1. For every RLITT $\Gamma$ in $T$
    1. Continue to the next iteration of the loop if root of $\Gamma$ is valance
       two with weight zero
    1. Compute $\iota[0]\star\Gamma$ and add to T
```

```{prf:remark} Find RLITT up to a given ACN
:label: find-rlitt-up-to-acn


**Input**

-   A target ACN

**Output**

-   A set $T$ of all RLITT up to ACN

**Routine**

1. Set $T$ to be the set $\LS \iota[0],\ \iota[0\ 0],\ \iota[1],\ \iota[-1],\ \iota[2],\ \iota[-2],\,\ \iota[2\ 0],\ \iota[-2\ 0]\RS$
2. for i from 3 to ACN
    1. Execute [](#find-rlitt-from-acnm1toacn) with input ACN $i$ and RLITT set
       $T$.
    1. Add the results to $T$
```

It is important to note that the output of [](#find-rlitt-up-to-acn) includes
duplicates in the form of $\LP+\RP$-RLITT and $\LP-\RP$-RLITT pairs. To
deduplicate our list so it contains only topologically unique objects, we select
from the list the collection of $\LP+\RP$-RLITT and neutral RLITT.

The algorithms we have introduced are, currently, only intuitively convincing.
We will rectify this by a proof for the claims of the algorithms.

```{prf:theorem}
:label: rli-gen-const-thm-acnm1toacn

Every $\Gamma$ RLITT of ACN $n$ is one of two forms:

1. $\Gamma$ is a single vertex with weight $n$.
2. $\Gamma$ is the result of grafting at the root of some rootstock $\Gamma_i$
   with ACN $i$ and a good scion $\Gamma_j$ with ACN $j$ with the conditions
   $0\leq i<n$ and $0<j<n$.
```

```{prf:proof}

Let $\Gamma$ be a RLITT of ACN $n$. We branch into cases based on the
number of vertices in $\Gamma$. First, when $\Gamma$ has a single vertex, which
clearly falls into form $1$. Next, assume that $\Gamma$ has $1<k<n$ vertices.

We will show that $\Gamma$ is decomposable into two trees that satisfy the
conditions in form $2$. From here we again branch into cases, based on the
valence of the root of $\Gamma$. Since the number of vertices of $\Gamma$ is
greater than $1$, the least valence of the root vertex is two. In this case, we
assign $\Gamma_i$ as the root vertex alone and $\Gamma_j$ as the remaining
subtree, with ACN $i$ and $j$ respectively. $\Gamma$ is RLITT, the
root vertex has weight greater than or eqaul to $0$. Consequently, $\Gamma_i$
has ACN $0\leq i<n$. Further, since $\Gamma$ is RLITT it satisfies the
stick condition, making $\Gamma_j$ a good scion with $0<j<n$.

The final case is when the root of $\Gamma$ has valence greater than two. In
this case, we let $\Gamma_j$ be the subtree on the rightmost path of $\Gamma$
excluding the root. We then let $\Gamma_i$ be the remaining subtree. Our
assumption of valence means $\Gamma_i$ has at least two vertices, so by the
stick condition $0\leq i<n$. Similarly, by stick condition $\Gamma_j$ is a good
scion with $0<j<n$ completing the proof.
```
