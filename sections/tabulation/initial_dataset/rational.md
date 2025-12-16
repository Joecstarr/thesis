<!-- prettier-ignore-start -->
(sec-rational)=
## Rational Tangles
<!-- prettier-ignore-end -->

We will see in this section that **rational tangles**, originally described by Conway
[@conwayEnumerationKnotsLinks1970], have a deeply combinatorial nature, making them among the
simplest classes of tangle. This simplicity leads to the rational tangles, and their knot closures,
being some of the most commonly studied objects in knot theory.

### Construction

In our development of the modified tangle calculus (@subsec-tangle_operations) we described a way to
glue tangles together, allowing us to take simple objects and build complex objects. That approach
forms the basis for our construction of the rational tangles.

We start, with an intuitive description of the construction. Imagine a zero tangle
(@prelim-fig-basic_0), now attach to that tangle a crank on the right (east) side
(@fig-rat_tang-crank). We allow, for a moment, the fixed points of the tangle to move. If we crank a
half turn clockwise or anti-clockwise, we introduce a twist, if we turn the crank $n$ half turns we
make an integral $n$ tangle(@subsec-integral_tangle).

```{figure} ../../media/fig-rat_tang-crank.svg
:label: fig-rat_tang-crank
A set of three turns, changing a basic $0$ tangle into an integral $3$ tangle.
```

When we have completed $n$ turns we take the crank and move it to the bottom (south) side of the
tangle. We turn the crank to add $n$ half turns, this time building a vertical integral tangle.
Continuing this, alternating between right and bottom sets of half turns, as seen in
@fig-rat_tang-crank_many, a **rational tangle**. For a rational tangle $T$, the list of counts for
right and bottom twists is the **twist vector** (@rational-def-twistvector) of the rational tangle.

```{figure} ../../media/fig-rat_tang-crank_many.svg
:label: fig-rat_tang-crank_many
The set of alternating turns building a rational tangle $\LB3\ 2\ 1\RB$.
```

Formalizing this intuitive construction requires the $\vee$ and $+$ operations
(@subsec-tangle_operations), as well as the integral tangles (@subsec-integral_tangle). This
formalization was originally stated by Conway [@conwayEnumerationKnotsLinks1970] but was ultimately
proved by Burde and Zieschang, we will give a later construction by Kauffman and Goldman
[@goldmanRationalTangles1997]. For convenience, we denote a horizontal integral tangle with $a\in\Z$
crossings as $t_a$, similarly, a vertical integral tangle with $b\in \Z$ crossings as $t_b^\prime$.

```{prf:definition}Kauffman and Goldman, Page 310 [@goldmanRationalTangles1997;@conwayEnumerationKnotsLinks1970]
:label: rational-def-rational

To build a **rational tangle**, take one of the following constructions:
1. Start with a horizontal tangle $t_{a_0}$. Add by $\vee$ a vertical tangle
   $t_{b_0}^{\prime}$ on the bottom, then add by $+$ a horizontal tangle
   $t_{a_1}$ on the right, then add by $\vee$ a $t_{b_1}^{\prime}$ on the
   bottom, and so on, stopping after a finite number of such steps at a
   horizontal tangle $t_{a_n}$.
1. Start with a vertical tangle $t_{b_0}^\prime$. Add by $+$ a horizontal
   tangle $t_{a_0}$ on the right, then add by $\vee$ a vertical tangle
   $t_{b_1}^\prime$ on the bottom, then add by $+$ a $t_{a_1}$ on the right, and
   so on, stopping after a finite number of such steps at a
   horizontal tangle $t_{a_n}$.
```

```{note}

In the first case the twist vector has an odd number of entries and in the
second the twist vector has an even number of entries.
```

To see the alignment between @rational-def-rational and our intuitive construction, view the turning
of the crank as corresponding to horizontal and vertical integral tangles, and the alternating of
right and bottom as corresponding to alternating $+$ and $\vee$.

#### Correspondence With Extended Rational Numbers

Now we formally address our first two essential questions by:

1. Describing a notation for rational tangles.
2. Demonstrating a correspondence between the rational tangles and the extended rational numbers.
3. Showing that the correspondence distinguishes (tells apart) rational tangles.

The answer to our first essential question, "How do I systematically construct rational tangles?",
is seen by formalizing the twist vector notational strategy we saw in our intuitive formulation for
rational tangles. This allows us to systematically write down a rational tangle by a list of
integers.

````{prf:definition}Conway Page 332[@conwayEnumerationKnotsLinks1970;@goldmanRationalTangles1997]
:label: rational-def-twistvector
The list of integers of the sets of tangles $t_{a_i}$ and $t_{b_j}^\prime$
from @rational-def-rational ordered as @rational-def-math-tv or
  @rational-def-math-tv2 is called a
**twist vector**.

```{math}
:label: rational-def-math-tv
    \LB a_0\ b_0\ a_1\ b_1\ \cdots\ a_n\RB
```
```{math}
:label: rational-def-math-tv2
    \LB b_0\ a_0\ b_1\ \cdots\ a_n\RB
```

````

We are now ready to answer the second of the essential questions, "How do I tell two rational
tangles I make apart?" The critical observation to answer the questions is due to Conway's use
[@conwayEnumerationKnotsLinks1970] of the entries of a twist vector as the entries for a continued
fraction (@rational-def-frac). Since the twist vector is of finite length, this continued fraction
corresponds to an extended rational number [@rockettContinuedFractions1998], $\Q\cup\LS\infty\RS$.

````{prf:definition}Conway, Page 332[@conwayEnumerationKnotsLinks1970]
:label: rational-def-frac
For a rational tangle $T$ we call @rational-math-frac the **fraction of a
rational tangle** and denote it $F\LP T\RP$.
```{math}
:label: rational-math-frac
    \frac{p}{q} = a_{n} + \cfrac{1}{b_n + \cfrac{1}{a_n + \cfrac{1}{b_{n-1} +
    \cfrac{1}{a_{n-1} + \cfrac{1}{\ddots\,+\cfrac{1}{a_0}}}}}}
```
````

```{note}
  The correspondance with the extended rational numbers means that
  $F\LP\LB1\ \m 1\ 0\RB\RP=\frac{1}{0}$ corresponds to the basic $\infty$ tangle
(@prelim-fig-basic_nc-inf).
```

Kauffman and Goldman [@goldmanRationalTangles1997] prove (@rational-thm-conways) that this
correspondence distinguishes, tells apart, rational tangles. Meaning, given two rational tangles, if
their fractions are the same the tangles are isotopic, and if the fractions are different, the
tangles are not isotopic. This answers the second of our essential questions.

```{prf:theorem} Conway's Theorem, Kauffman and Goldman page 315[@conwayEnumerationKnotsLinks1970;@burdeKnots2013;@goldmanRationalTangles1997]
:label: rational-thm-conways
Let $T_1$ and $T_2$ be rational tangles. $F\LP T_1\RP=F\LP T_2\RP$ if and only
if $T_1$ is ambient isotopic to $T_2$.
```

Observe, @rational-thm-conways does not discount the possibility of two non-equivalent twist
vectors, those differing in at least one entry, representing the same rational tangle.
@rational-ex-tvssamebutdiff demonstrates that the possibility is true. In fact, for each rational
tangle, the set of twist vectors representing it is infinite.

````{prf:example}
:label: rational-ex-tvssamebutdiff
```{math}
\begin{aligned}
F\LP\LB 1\ 7\ 0\ 1\RB \RP &= \frac{9}{1}\\\\
F\LP\LB \m 3\ 1\ \ \m 1\ \m 1\ \m 1\ 1\ 9\RB \RP &= \frac{9}{1}\\\\
F\LP\LB 1\ \m1\ 1\ \m1\ 7\ 0\ 3\RB \RP &= \frac{9}{1}\\\\
F\LP\LB 1\ \m1\ \m1\ 1\ \m1\ 1\ \m1\ 1\ \m1\ 9\RB \RP &= \frac{9}{1}\\\\
F\LP\LB 1\ 8\RB \RP &= \frac{9}{1}\\\\
F\LP\LB 9\RB \RP &= \frac{9}{1}\\\\
\end{aligned}
```
````

To effectively answer our third essential question, "How do I generate rational tangles?", we will
need to determine a unique twist vector representative for each rational tangle. A unique
representative allows us to simply and efficiently write down each tangle without risk of duplicates
showing up on our list.

### Canonical Twist Vectors

Identifying a unique representative will stem from properties of finite continued fractions. We
start by defining a specific subclass of finite continued fractions with integer coefficients, the
**regular continued fractions**. We frame the definition in the context of twist vectors.

```{prf:definition}Kauffman and Goldman, page 318[@kauffmanClassificationRationalKnots2002; @rockettContinuedFractions1998]
A continued fraction with integer coefficients $c_i$ is called a **regular
continued fraction** if $c_i< 0$ for every coefficient or $0< c_i$ for
every coefficient except the last which may be $0$.
```

Conveniently, each extended rational number corresponds to exactly two regular continued fractions
[@rockettContinuedFractions1998]. The first is a twist vector with the leftmost element greater than
or equal to $2$, and the second with leftmost element equal to $1$, per @rational-math-twotv.
Observe, one of these twist vectors has an even number of entries, and one has an odd number of
entries.

```{math}
:label: rational-math-twotv
\begin{aligned}
    F\LP\LB 9\RB \RP &= \frac{9}{1}= 8+\frac{1}{1} = F\LP\LB 1\ 8\RB \RP \\
    F\LP\LB 9\ 0\RB \RP &= 0+\frac{1}{9}=0+\frac{1}{8+\frac{1}{1}}=
    F\LP\LB 1\ 8\ 0\RB \RP \\
\end{aligned}
```

```{note}
  The fraction $\frac{1}{0}$ corresponds to the $\LB 0\ 0\RB$ twist vector.
```

To identify a unique representative for a rational number and hence rational tangle, we will select,
for convenience, the odd length twist vector as our unique representative.

```{prf:definition}Kauffman and Lambropoulou, Page 13 [@kauffmanClassificationRationalKnots2002]
:label: rational-def-canonrat

A twist vector is called a **canonical twist vector** if it contains
coefficients of a regular continued fraction and is of odd length or is
$\LB0\ 0\RB$.
```

### Computational Methods

Armed with a unique representative for a rational tangle, we can construct our computational answer
to the third essential question.

#### Notation

We start by describing how we will digitally store a rational tangle. In the rational tangle case,
the theoretical encoding strategy of twist vectors happens to be well suited for computational
storage. A twist vector can be computationally stored identically to its written form, a list of
space separated integers delimited by a pair of square braces, $\LB\ \RB$. As we will see in
@sec-arborescent this direct translation of theoretical notation to computational notation is not
always the case.

#### Generation

A common tactic in the knot tabulation space is to pare down the number of items that must be
tabulated by leveraging symmetries of the objects being tabulated. For example, the $\LB 3\RB$ and
$\LB \m 3\RB$ tangles are related to each other by a minus operation (@subsubsec-conway_minus).
Meaning, if we tabulate $\LB 3\RB$, we can recover $\LB \m 3\RB$ with multiplication by $\m 1$. This
fact holds for all rational tangles as demonstrated by @rationa-lema-pmtv. Allowing us to focus our
efforts on the rational tangle with twist vectors containing only positive entries.

```{prf:lemma}Kauffman and Lambropoulou, Page 19[@kauffmanClassificationRationalKnots2002]
:label: rationa-lema-pmtv
For a tangle $T$ with negative $-T$ (@subsubsec-conway_minus), if
$F\LP T\RP=\frac{p}{q}$ then $F\LP \m T\RP=\m\frac{ p}{q}$.
```

We now begin our development of a generation strategy for twist canonical twist vectors of rational
tangles. The method seen here utilizes a common combinatorial method for defining compositions of
integers, the same is used for rational tangle counting by Bryhtan
[@bryhtanTabulating2stringTangles2024]. Consider, for a given crossing number $n$, what is the most
"obvious" twist vector? A viable candidate for most "obvious" is a twist vector, of the form seen in
@rational-math-1s, dropping the trailing $0$ where needed.

```{math}
:label: rational-math-1s
\LB 1\ 1\ 1\ \cdots\ 1\RB
```

The 1's twist vector @rational-math-1s is an ideal starting point for developing a generation
strategy, as it distributes the data of a rational tangle as broadly as possible. Next, we consider
how we might transform the 1's twist vector into a twist vector with a two crossing integral
components. We can do this by exchanging the space between the first and second $1$ with a numeric
$+$.

```{math}
:label: rational-math-1plus
\begin{aligned}
&\LB 1\square 1\ 1\ \cdots\ 1\RB\\\\
&\LB 1+1\ 1\ \cdots\ 1\RB\\\\
&\LB 2\ 1\ \cdots\ 1\RB\\\\
\end{aligned}
```

This process tells us that we can utilize the exchange of whitespace of a twist vector for $+$ to
generate new twist vectors. To complete our generation, we must generate every combination of
exchanges.

The 1's twist vector with crossing number $n$ has $n$ $1$s and $n-1$ spaces. In each space position,
we have the option between a space and $+$. To enumerate all $2^{n-1}$ combinations, we can simply
count, in binary, from $1$ to $2^{n-1}$, as in @rational-ex-counting.

````{prf:example} Combinations of exchanges for $n=4$ and their twist vector
:label:rational-ex-counting
```{math}
:label: rational-ex-math-counting
\begin{aligned}
000\to \square \square \square\to &\LB1\ 1\ 1\ 1\RB \\\\
001\to \square \square +\to &\LB1\ 1\ 2\RB \\\\
010\to \square + \square\to &\LB1\ 2\ 1\RB \\\\
011\to \square + +\to &\LB1\ 3\RB \\\\
100\to + \square \square\to &\LB2\ 1\ 1\RB \\\\
101\to + \square +\to &\LB2\ 2\RB \\\\
110\to + + \square\to &\LB3\ 1\RB \\\\
111\to + + +\to &\LB4\RB \\\\
\end{aligned}
```
````

Our final refinement in this process it to transform this collection into canonical twist vectors.
Half of the twist vectors, those of odd length, generated in this process are already canonical. To
canonize the even length twist vectors, we append $0$ to the right most position of each list,
turning the even vectors into an odd canonical vectors.

```{note}
Appending $0$ to the even twist vectors makes each of the fractions for these
twist vectors sit in the unit interval, $\LB 0,1\RP$.
```

We conclude the section with a set of algorithms that describe a method for computationally
generating all rational tangles up to a given crossing number.

```{prf:algorithm} Find all rational tangles of crossing number $n$
:label: find-rat-tang-of-n

**Input**

-   A crossing number $n$

**Output**

-   All collection $T$ of twist vectors

**Routine**

1. Generate $O$ the 1's twist vector as in @rational-math-1s for $n$
1. for $i=0$ to $2^{n-1}$
   1. Transform $i$ into its binary representation
   2. Exchange as in @rational-math-1plus digits of $i$ with spaces where $i$
      is $O$ and with $+$ where $i$ is $1$
   3. Apply operations to the $1$s vector and store the resulting vector as $O_r$
   4. If $O_r$ is odd length, store $O_r$ in $T$
   5. Else, append $0$ to $O_r$ and store
```

```{prf:algorithm} Find all rational tangles up to crossing number $n$
:label: find-rat-tang-to-n

**Input**

-   A crossing number $n$

**Output**

-   All collection $T$ of twist vectors

**Routine**

1. Store the twist vectors $\LB 0\RB,\LB 0\ 0\RB,\LB 1\RB$
1. for $i=2$ to $n$
    1. Execute @find-rat-tang-of-n with $i$
```
