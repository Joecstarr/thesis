### Rational Tangles

We will see in this section that the rational tangles have a deeply
combinatorial nature, which makes them among the simplest classes of tangle to
describe. This simplicity leads to the rational tangles, and their knot
closures, being some of the most commonly studied objects in knot theory.

#### Construction

In our development of the modified tangle calculus in @subsec-tangle_operations
we described a way to glue tangles together, allowing us to build complex
objects. That approach forms the basis for our construction of the rational
tangles. We start, with an intuitive description of the construction. Start with
a $0$ tangle, imagine now, a crank is attached to the right (east) side of the
tangle, seen in @fig-rat_tang-crank. If we take the crank and crank it clockwise
a half turn we introduce a positive twist, it is important to notice that we can
crank $n$ half turns to make an integral $n$ tangle.

```{figure} ./media/fig-rat_tang-crank.svg
:label: fig-rat_tang-crank
The first set of cranks taking a basic $0$ tangle to a integral $3$ tangle.
```

From here, take the crank and move it to the bottom (south) side of the tangle.
We again add $n$ half clockwise turns, this time building a vertical integral
tangle. Alternating, right and bottom sets of half turns, as seen in
@fig-rat_tang-crank_many, builds a rational tangle. We call the list of counts
of right and bottom twists the Twist Vector for the rational tangle.

```{figure} ./media/fig-rat_tang-crank_many.svg
:label: fig-rat_tang-crank_many
The set of cranks that build a rational tangle, we will see this tangle is
called $\LB1\ 2\ 3\RB$.
```

Formalizing this concept requires the machinery we developed in
@subsec-tangle_operations namely the $\vee$ and $+$ operations, as well as the
integral tangles from @subsec-integral_tangle. We denote a horizontal integral
tangle with $a$ crossings as $t_a$. Similarly, we denote a vertical integral
tangle with $a$ crossings as $t_a^\prime$

```{prf:definition} Rational Tangle [@goldmanRationalTangles1997]
:label: rational-def-rational

To build a **rational tangle** start with a horizontal tangle $t_{a_0}$. Add by
$\vee$ a vertical tangle $t_{b_0}^{\prime}$ on the bottom, then add by $+$ a
horizontal tangle $t_{a_1}$ on the right, then add by $\vee$ a
$t_{b_1}^{\prime}$ on the bottom, and so on, stopping after a finite number of
such steps.
```

```{note}
We can reformulate @rational-def-rational, in an as we will see equivalent, by
starting with a $\pm 1$ tangle. This equates to starting with a vertical
$t_{b_0\pm 1}^\prime$ tangle. We then alternate horizontal vertical with $+$
and $\vee$ as in the original construction. In this thesis, we assume that we
always start with the horizontal tangle.

```

Our intuitive construction from the beginning of this section should align with
@rational-def-rational. We can see the alignment with the cranking corresponding
to horizontal and vertical integral tangles, and alternating right and bottom
corresponding to alternating $+$ and $v$.

##### Correspondence With Rational Numbers

We are now ready to address our first two essential questions. This will be done
by describing a notation for rational tangles. Next, demonstrating a
correspondence between the rational tangles and the rational numbers, and
showing that the correspondence distinguishes rational tangles.

To answer the first of the essential questions, we will develop a convenient
notational strategy for rational tangles. In @rational-def-rational, we saw a
construction for rational tangles that is built on sets of integral tangles
$t_{a_i}$ and $t_{b_j}^\prime$. We know the tangles alternate between horizontal
and vertical. This fact allows us to instead encode the same information in a
single list of integers, we call this list of integers a **twist vector**.

````{prf:definition} Twist Vector [@conwayEnumerationKnotsLinks1970]
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
entries for a continued fraction as @rational-math-frac. Since the twist vector
is finite length, this continued fraction corresponds to a rational number.

````{prf:definition} The fraction of a rational tangle [@goldmanRationalTangles1997]
For a rational tangle $T$ we call @rational-math-frac the **fraction of a
rational tangle** and denote it $F\LP T\RP$.
```{math}
:label: rational-math-frac
\frac{p}{q} = a_{n+1} + \cfrac{1}{b_n + \cfrac{1}{a_n + \cfrac{1}{b_{n-1} +
\cfrac{1}{a\_{n-1} + \ddots\,}}}}
```
````

Kauffman and Goldman prove [@goldmanRationalTangles1997] that this
correspondence distinguishes rational tangles, answering our essential question.

```{prf:theorem} Conway's Theorem [@goldmanRationalTangles1997]
:label: rational-thm-conways
Let $T_1$ and $T_2$ be rational tangles. If $F\LP T_1\RP=F\LP T_2\RP$, then
$T_1$ is ambient isotopic to $T_2$.
```

Now, we will answer our third essential question, the answer takes the form of a
method for efficiently writing down twist vectors. @rational-thm-conways details
a method for determining if two rational tangles are equivalent. However,
@rational-thm-conways does not discount the possibility of two non-equivalent
twist vectors representing the same rational tangle, @rational-ex-tvssamebutdiff
demonstrates that the possibility is true. In fact, for each rational tangle,
the set of twist vectors representing it is infinite.

````{prf:example}
:label: rational-ex-tvssamebutdiff
```{math}
\begin{aligned}
F\LP\LB 1\ 7\ 0\ 1\RB \RP &= \frac{9}{1}\\
F\LP\LB -3\ 1\ -1\ -11\RB \RP &= \frac{9}{1}\\
F\LP\LB 1\ 1\ -1\ -7\RB \RP &= \frac{9}{1}\\
F\LP\LB -1\ 1\ -1\ 1\ -1\ 1\ 9\RB \RP &= \frac{9}{1}\\
F\LP\LB 1\ 8\RB \RP &= \frac{9}{1}\\
F\LP\LB 9\RB \RP &= \frac{9}{1}\\
\end{aligned}
```
````

To effectively enumerate the rational tangles, we will need to determine a
unique representative for each rational tangle. We will then develop a method
for effectively enumerating those unique representatives.

#### Canonical Twist Vectors

Identifying a unique representative will stem from properties of finite
continued fractions. We start by defining a specific subclass of finite
continued fractions with integer coefficients, the **regular continued
fractions**. We frame the definition in the context of twist vectors.

```{prf:definition} Regular Continued Fractions [@rockettContinuedFractions1998]
A continued fraction with integer coefficients is called a **regular continued
fraction** if the initial term (rightmost twist vector entry) is an integer and
all remaining terms are positive integers.
```

Conveniently, each rational number corresponds to exactly two regular continued
fractions [@rockettContinuedFractions1998, pg. 3]. The first is a twist vector
with leftmost element greater than or equal to $2$, and the second with leftmost
element equal to $1$, seen in @rational-math-twotv. Observe that one of these
twist vectors has an even number of entries and one has an odd number of
entries.

```{math}
:label: rational-math-twotv
\begin{aligned}
F\LP\LB 9\RB \RP &=  F\LP\LB 1\ 8\RB \RP = \frac{9}{1}\\
F\LP\LB 9 0\RB \RP &=  F\LP\LB 1\ 8\ 0\RB \RP = \frac{1}{9}\\
\end{aligned}
```

To identify a unique representative for a rational number and hence rational
tangle, we will select, for convenience in @sec-monttang, the odd length twist
vector as our unique representative.

```{prf:definition} Canonical Twist Vector [@goldmanRationalTangles1997]
:label: rational-def-canonrat

A twist vector that contains coefficients of a regular continued fraction and
is of odd length is called a **canonical twist vector**.
```

#### Computational Methods

Armed with a unique representative for a rational tangle, we can complete our
answer to the essential question. This is by describing:

1. A method to computationally generate rational tangles.
2. A strategy for storing rational tangles.

##### Notation

We start by describing how we will digitally store a rational tangle. We will
take the

In this case the theoretical encoding strategy happens to be well suited for
computational storage. As we will see in @sec-monttang and @sec-arborescent this
is frequently not the case.

##### Generation
