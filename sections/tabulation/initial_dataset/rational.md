### Rational Tangles

We will see in this section that, what are called **rational tangles**, have a
deeply combinatorial nature, making them among the simplest classes of tangle.
This simplicity leads to the rational tangles, and their knot closures, being
some of the most commonly studied objects in knot theory.

#### Construction

In our development of the modified tangle calculus (@subsec-tangle_operations)
we described a way to glue tangles together, allowing us to take simple objects
and build complex objects. That approach forms the basis for our construction of
the rational tangles.

We start, with an intuitive description of the construction. Imagine a $0$
tangle, with a crank attached to the right (east) side of the tangle
(@fig-rat_tang-crank). If we take the crank and turn it clockwise a half turn,
we introduce a positive twist. Notice that we can turn the crank $n$ half turns
to make an integral $n$ tangle.

```{figure} ../../media/fig-rat_tang-crank.svg
:label: fig-rat_tang-crank
The first set of cranks taking a basic $0$ tangle to an integral $3$ tangle.
```

From here, take the crank and move it to the bottom (south) side of the tangle.
We again add $n$ half clockwise turns, this time building a vertical integral
tangle. Alternating, between right and bottom sets of half turns, as seen in
@fig-rat_tang-crank_many, builds a rational tangle. We call the list of counts
of right and bottom twists the **twist vector** (@rational-def-twistvector) for
the rational tangle.

```{figure} ../../media/fig-rat_tang-crank_many.svg
:label: fig-rat_tang-crank_many
The set of cranks that build a rational tangle, we will see this tangle is
called $\LB1\ 2\ 3\RB$.
```

Formalizing this concept requires the machinery we developed in
@subsec-tangle_operations namely the $\vee$ and $+$ operations, as well as the
integral tangles from @subsec-integral_tangle. For convinence, we denote a
horizontal integral tangle with $a$ crossings as $t_a$, similarly, a vertical
integral tangle with $a$ crossings as $t_a^\prime$.

```{prf:definition} Rational Tangle [@goldmanRationalTangles1997]
:label: rational-def-rational

To build a **rational tangle** start with a horizontal tangle $t_{a_0}$. Add by
$\vee$ a vertical tangle $t_{b_0}^{\prime}$ on the bottom, then add by $+$ a
horizontal tangle $t_{a_1}$ on the right, then add by $\vee$ a
$t_{b_1}^{\prime}$ on the bottom, and so on, stopping after a finite number of
such steps.
```

```{note}
We can reformulate @rational-def-rational, by
starting with a $\pm 1$ tangle. This equates to starting with a vertical
$t_{b_0\pm 1}^\prime$ tangle. We then alternate horizontal vertical with $+$
and $\vee$ as in the original construction. In this thesis, we assume that we
always start with the horizontal tangle.

```

Our intuitive construction from the beginning of this section must align with
@rational-def-rational. We can see the alignment with the cranking corresponding
to horizontal and vertical integral tangles, and alternating right and bottom
corresponding to alternating $+$ and $v$.

##### Correspondence With Rational Numbers

We are now ready to address our first two essential questions. This will be done
by describing a notation for rational tangles. Next, demonstrating a
correspondence between the rational tangles and the rational numbers. Finally,
we show that the correspondence distinguishes rational tangles.

To answer the first of the essential questions, we formalize the twist vector
notational strategy we saw in our intuitive fomulation of for rational tangles.

````{prf:definition} Twist Vector [@conwayEnumerationKnotsLinks1970;@goldmanRationalTangles1997]
:label: rational-def-twistvector
The list of integers of the sets of tangles $t_{a_i}$ and $t_{b_j}^\prime$
from @rational-def-rational ordered as @rational-def-math-tv is called a
**twist vector**. Note, if $\LS t_{b_j}^\prime\RS_j^n$ then $t_{a_i}$
may have $n$ or $n+1$ entries.

```{math}
:label: rational-def-math-tv
\LB a_0\ b_0\ a_1\ b_1\ \cdots\ a_n\ b_n\ a_{n+1}\RB
```
````

We are now ready to answer the second of the essential questions. The critical
observation to answer the questions is due to Conway's use
[@conwayEnumerationKnotsLinks1970] of the entries of a twist vector as the
entries for a continued fraction (@rational-def-frac). Since the twist vector is
finite length, this continued fraction corresponds to a rational number
[@rockettContinuedFractions1998].

````{prf:definition} The fraction of a rational tangle [@goldmanRationalTangles1997]
:label: rational-def-frac
For a rational tangle $T$ we call @rational-math-frac the **fraction of a
rational tangle** and denote it $F\LP T\RP$.
```{math}
:label: rational-math-frac
\frac{p}{q} = a_{n+1} + \cfrac{1}{b_n + \cfrac{1}{a_n + \cfrac{1}{b_{n-1} +
\cfrac{1}{a_{n-1} + \ddots\,}}}}
```
````

```{note}
The fraction $\frac{1}{0}$ corresponds to the basic $\infty$ tangle.
```

Kauffman and Goldman prove [@goldmanRationalTangles1997] that this
correspondence distinguishes rational tangles, answering the second of our
essential questions.

```{prf:theorem} Conway's Theorem [@goldmanRationalTangles1997]
:label: rational-thm-conways
Let $T_1$ and $T_2$ be rational tangles. If $F\LP T_1\RP=F\LP T_2\RP$, then
$T_1$ is ambient isotopic to $T_2$.
```

Observe, @rational-thm-conways does not discount the possibility of two
non-equivalent twist vectors representing the same rational tangle,
@rational-ex-tvssamebutdiff demonstrates that the possibility is true. In fact,
for each rational tangle, the set of twist vectors representing it is infinite.

````{prf:example}
:label: rational-ex-tvssamebutdiff
```{math}
\begin{aligned}
F\LP\LB 1\ 7\ 0\ 1\RB \RP &= \frac{9}{1}\\
F\LP\LB \ \m 3\ 1\ \ \m 1\ \m 1\ \m 11\RB \RP &= \frac{9}{1}\\
F\LP\LB 1\ 1\ \ \m 1\ \m 7\ \m 7\RB \RP &= \frac{9}{1}\\
F\LP\LB \ \m 1\ 1\ \m 1\ \m 1\ \m 1\ \m 1\ \m 1\ 1\ 9\RB \RP &= \frac{9}{1}\\
F\LP\LB 1\ 8\RB \RP &= \frac{9}{1}\\
F\LP\LB 9\RB \RP &= \frac{9}{1}\\
\end{aligned}
```
````

To effectively answer our third essential question, we will need to determine a
unique representative for each rational tangle. We will then develop a method
for effectively enumerating those unique representatives.

#### Canonical Twist Vectors

Identifying a unique representative will stem from properties of finite
continued fractions. We start by defining a specific subclass of finite
continued fractions with integer coefficients, the **regular continued
fractions**. We frame the definition in the context of twist vectors.

```{prf:definition} Regular Continued Fractions [@kauffmanClassificationRationalKnots2002; @rockettContinuedFractions1998]
A continued fraction with integer coefficients $c_i$ is called a **regular
continued fraction** if $0 \geq c_i$ for every coefficient or $c_i \geq 0$ for
every coefficient.
```

Conveniently, each rational number corresponds to exactly two regular continued
fractions [@rockettContinuedFractions1998, pg. 3]. The first is a twist vector
with leftmost element greater than or equal to $2$, and the second with leftmost
element equal to $1$ (@rational-math-twotv). Observe, one of these twist vectors
has an even number of entries and one has an odd number of entries.

```{math}
:label: rational-math-twotv
\begin{aligned}
F\LP\LB 9\RB \RP &=  F\LP\LB 1\ 8\RB \RP = \frac{9}{1}\\
F\LP\LB 9\ 0\RB \RP &=  F\LP\LB 1\ 8\ 0\RB \RP = \frac{1}{9}\\
F\LP\LB \m 9\RB \RP &=  F\LP\LB \m 1\ \m 8\RB \RP = \frac{\m 9}{1}\\
F\LP\LB \m 9\ 0\RB \RP &=  F\LP\LB \m 1\ \m 8\ 0\RB \RP = \frac{1}{\m 9}\\
\end{aligned}
```

```{note}
The fraction $\frac{1}{0}$ corresponds to the $\LB 0\ 0\RB$ twist vector.
```

To identify a unique representative for a rational number and hence rational
tangle, we will select, for convenience in our construction in @sec-monttang,
the odd length twist vector as our unique representative.

```{prf:definition} Canonical Twist Vector [@kauffmanClassificationRationalKnots2002]
:label: rational-def-canonrat

A twist vector that contains coefficients of a regular continued fraction and
is of odd length is called a **canonical twist vector**.
```

#### Computational Methods

Armed with a unique representative for a rational tangle, we can construct our
answer to the third essential question.

##### Notation

We start by describing how we will digitally store a rational tangle. In the
rational tangle case the theoretical encoding strategy, twist vectors, happens
to be well suited for computational storage. A twist vector can be
computationally stored identically to it's written form, a list of space
separated integers delimited by a pair of square braces, $\LB\ \RB$. As we will
see in @sec-arborescent this is not always the case.

##### Generation

A common tactic in the knot tabulation space is to pair down the number of items
that must be tabulated by leveraging symmetries of the objects being tabulated.
For example, the $\LB 3\RB$ and $\LB \m 3\RB$ tangles are related to each other
by a minus operation (@subsubsec-conway_minus). This fact holds for all rational
tangles (@rationa-lema-pmtv). Telling us that if we generate the rational
tangles with all positive twist vectors, we can then turn those into rational
tangles with all negative twist vectors by multiplying each coefficient by
$\m 1$. Allowing us to focus our efforts on the rational tangle with all
positive twist vectors.

```{prf:lemma}[@kauffmanClassificationRationalKnots2002, pg. 19]
:label: rationa-lema-pmtv
If $F\LP T\RP=\frac{p}{q}$ then $F\LP \m T\RP=\m\frac{ p}{q}$.
```

Consider, for a given crossing number $n$, what is the most "obvious" twist
vector? A viable candidate for most "obvious" is a twist vector of the form seen
in @rational-math-1s.

```{math}
:label: rational-math-1s
\LB 1\ 1\ 1\ \cdots\ 1\RB
```

The 1's twist vector (@rational-math-1s) is an ideal starting point for
developing a generation strategy. The 1's twist vector distributes the data of a
rational tangle as broadly as possible. Next, we consider how we might transform
the 1's twsit vector into a twist vector with a two crossing integral
components. We can do this by exchanging the space between the first and second
$1$ with an arithmetic $+$.

```{math}
:label: rational-math-1plus
\begin{aligned}
&\LB 1\square 1\ 1\ \cdots\ 1\RB\\
&\LB 1+1\ 1\ \cdots\ 1\RB\\
&\LB 2\ 1\ \cdots\ 1\RB\\
\end{aligned}
```

This process tells us that we can utilize the exchange of whitespace of a twist
vector for $+$ to generate new twist vectors. To complete our generation, we
must generate every combination of exchanges.

The 1's twist vector with crossing number $n$ has $n$ $1$s and $n-1$ spaces. In
each space position, we have the option between a space and $+$, to enumerate
all $2^{n-1}$ combinations we can simply count, in binary, from $1$ to $2^{n-1}$
as in @rational-ex-counting.

````{prf:example} Combinations of exchanges for $n=4$ and their twist vector
:label:rational-ex-counting
```{math}
:label: rational-ex-math-counting
\begin{aligned}
000\to \square \square \square\to &\LB2\ 1\ 1\ 1\RB \\
001\to \square \square +\to &\LB1\ 1\ 2\RB \\
010\to \square + \square\to &\LB1\ 2\ 1\RB \\
011\to \square + +\to &\LB1\ 3\RB \\
100\to + \square \square\to &\LB2\ 1\ 1\RB \\
101\to + \square +\to &\LB2\ 2\RB \\
110\to + + \square\to &\LB3\ 1\RB \\
111\to + + +\to &\LB4\RB \\
\end{aligned}
```
````

Our final refinement in this process it to transform this collection into
canonical twist vectors. Half of the twist vectors, those of odd length,
generated in this process are already canonical. To canonize the even length
twist vectors, we append $0$ to the right most position of each list, turning
the even vector into an odd canonical vector.

```{note}
Appending $0$ to the even twist vectors makes each of the fractions for these
twist vectors sit in the unit interval.
```

We conclude the section with a set of algorithms that describe a method for
computationally generating all rational tangles up to a given crossing number.

```{prf:remark} Find all rational tangles of crossing number $n$
:label: find-rat-tang-of-n

**Input**

-   A crossing number

**Output**

-   All collection $T$ of twist vectors

**Routine**

1. Generate $o$ the 1's twist vector @rational-math-1s for $n$
1. for $i=0$ to $2^{n-1}$
   1. Transform $i$ into binary form
   2. Exchange as in @rational-math-1plus spaces of $o$ with $+$ where $i$'s binary form is $1$ store as $o_e$
   3. If $o_e$ is odd length, store $o_e$ in $T$
   4. Else, append $0$ to $o_e$ and store
```

```{prf:remark} Find all rational tangles up to crossing number $n$
:label: find-rat-tang-to-n

**Input**

-   A crossing number

**Output**

-   All collection $T$ of twist vectors

**Routine**

1. Store the twist vectors $\LB 0\RB,\LB 0\ 0\RB,\LB 1\RB$
1. for $i=2$ to $n$
    1. Execute @find-rat-tang-of-n with $i$
```
