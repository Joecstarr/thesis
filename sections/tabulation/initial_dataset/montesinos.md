<!-- prettier-ignore-start -->
(sec-monttang)=
### Montesinos Tangles
<!-- prettier-ignore-end -->

In this section, we will use the rational tangles to build a yet more complex
class of tangles, the Montesinos tangles. This building up process demonstrates
one of the core strategies for tangle tabulation.

#### Construction

With the rational tangles in hand, we wish to utilize that data to enumerate
additional tangles. One way we have seen to build simple objects into complex
objects is to combine two tangles with the $+$ or $\vee$ operation. To keep
complexity under control, we start with combining tangles with repeated $+$ sum.
When all summands, $R_i$ in equation @mont-math-def, are rational or integral,
we call the result of the sum a **Montesinos Tangle**
[@ernstTANGLEEQUATIONS1996;@bonahonNewGeometricSplittings2016].

```{math}
:label: mont-math-def

R_0+R_1+\cdots+R_n

```

```{note}
Under this characterization of the Montesinos tangles, every rational and
integral tangle is also a Montesinos tangle with a single summand.
```

##### Unique Representative

Next, we develop a classification of Montesinos tangles, allowing us to tell two
Montesinos tangles apart. For each rational or integral summand $R_i$ in a
Montesinos tangle, we have four possibilities:

1. $R_i$'s canonical twist vector is positive and ends in $0$
2. $R_i$'s canonical twist vector is positive and does not end in $0$
3. $R_i$'s canonical twist vector is negative and ends in $0$
4. $R_i$'s canonical twist vector is negative and does not end in $0$

Observe that in the second and fourth cases, $R_i$ terminates in a horizontal
integral tangle. In these cases, the tangle can be simplified by using the flype
(@subsubsec-opo-flype) to move the horizontal crossings to be the right most
summand, seen in @mont-ex-flypesimple. When this process is carried out for each
summand of the type in cases two and four, the resulting summands all fall into
cases one and three.

```{figure} ../../media/fig-mont.svg
:label: mont-ex-flypesimple
A Montesinos tangle $\LB1\ 2\ 2\RB+\LB \m1\ \m2\ 0\RB+\LB \m3\ \m2\ \m1\RB+\LB 1\ 2\ 0\RB+\LB1\ 2\ 2\RB$
simplifying to $\LB 1\ 2\ 0\RB+\LB \m 1\ \m 2\ 0\RB+\LB \m3\ \m 2\ 0\RB+\LB1\ 2\ 2\RB+\LB1\ 2\ 0\RB+\LB 3\RB$
```

We will now pare down to a single possibility, case one. Consider a summand
$R_i$ in case three, meaning $\m 1 <F\LP R_i\RP<0$ except for $R_n$, which may
be integral. @rational-thm-conways tells us that if we can find an alternative,
potentially non-canonical, twist vector that fits our needs, we are free to
exchange without impacting topology. What we would like is an odd length twist
vector, where every entry is positive, except for the rightmost, which is a
negative value, see @mont-ex-equ-replace.

```{figure}../../media/3_2_-1.svg
:label: mont-ex-equ-replace
On the left rational tangle $\LB \m1\ \m2\ \m1\ \m1\ 0\RB$ and on the right
$\LB 3\ 2\ \m1\RB$. These tangles have fractions
$F\LP\LB \m1\ \m2\ \m1\ \m1\ 0\RB\RP=\frac{\m4}{7}$ and
$F\LP\LB 3\ 2\ \m1\RB\RP=\frac{\m4}{7}$ showing the tangles to be isotopic.
```

This ensures that the fraction is still negative but will allow us to flype the
terminal horizontal integral tangle to the right. Rockett and Sz\"usz give a
lemma that establishes the existence of such a twist vector for each rational
number.

```{prf:lemma} Rockett and Sz"usz Page 3 [@rockettContinuedFractions1998]
:label: mont-lem-other_cfrac
Every extended rational number has a continued fraction with positive integer entries
except for the first (rightmost twist vector entry) which is an integer.
```

We have now shown that each case (2,3,4) can be transformed into the first case,
and we can define a canonical form for Montesinos tangles.

````{prf:theorem}Bonahon and Seibenmann Theorem 11.7 [@bonahonNewGeometricSplittings2016]

Every non-rational Montesinos tangle $T$ admits a canonical diagram satisfying
the following construction:
```{math}
T \cong R_0+\cdots+R_m+\frac{k}{1}
```
where each $R_i \cong \frac{p_i}{q_i}$ is a rational subtangle in canonical form with
fraction satisfying $0<\frac{p_i}{q_i}<1$, and $\frac{k}{1}$ is a horizontal
integer subtangle.
````

#### Computational Methods

##### Notation

Before we can generate Montesinos tangles, we need to define an efficient
notation for computation and storage. Similar to what we saw in the rational
tangle case, the theoretical notation for Montesinos tangles is sufficient for
computation. However, with eyes on future computational work, we will generalize
our notation to increase reusability and the efficiency of storage.

Montesinos tangles are simple forms of the algebraic tangles (@def-algebraic),
so we will build a notational strategy for general algebraic tangles. The
theoretical notation for algebraic tangles is outlined in
@subsec-tangle_operations and seen in @mont-ex-tree. We can simplify the
notation, without losing fidelity, by substituting the integral tangle summands
for rational tangle twist vectors. Additionally, we can improve the storage
overhead by storing the tree as a string in Polish notation
[@lukasiewiczElementyLogikiMatematycznej1929]. Storing in Polish notation allows
us to drop all the parentheses from our notation, saving two bytes in each
instance.

````{prf:example}
:label: mont-ex-tree
```{image}../../media/mont.svg
```

Algebraically:

$\LB1\ 2\ 0\RB+\LP\LB2\ 1\ 0\RB+\LB2\ 2\ 0\RB\RP$

In polish notation:

$+\LB1\ 2\ 0\RB+\LB2\ 1\ 0\RB\LB2\ 2\ 0\RB$

As an algebraic tangle tree:
   ```{mermaid}
   flowchart TD
   id0("$$+$$")-->id1("[1 2 0]")
   id0-->id2
   id2("$$+$$")-->id3("[2 1 0]")
   id2-->id4("[2 2 0]")
   ```
````

##### Generation

In this section, we will design an algorithm that allows us to efficiently
generate new Montesinos tangles up to a given crossing number. As we saw, the
construction of a Montesinos tangle is based on the repeated summation of
rational tangles. Consequently, our generation strategy will utilize our table
of rational tangles.

To start, we need a mechanism that allows us to select all possible combinations
of rational tangles with crossing numbers that sum to our target. For a
Montesinos tangle $T$, the set of rational components $\LS R_i\RS_i^n$ combined
with the integral component $k$ corresponds to an ordered list of crossing
numbers as in equation @mont-math-orderedlist.

```{math}
:label: mont-math-orderedlist
CN\LP R_0\RP,\ \cdots,\ CN\LP R_n\RP,\  CN\LP k\RP
```

We call a list of the form seen in @mont-math-orderedlist a **stencil** for a
Montesinos tangle. By construction, every canonical Montesinos tangle relates to
precisely one stencil. Observe, that $2\leq CN\LP R_i\RP$ since $\frac{1}{2}$ is
the lowest crossing number rational tangle with fraction in the unit interval.

Generation for all Montesinos tangles of a given crossing number at this point
can be broken down into two steps:

1. Generate all stencils
2. Fill in the stencils with all rational tangles whose fraction is in the unit
   interval (plus an integral tangle in the rightmost position).

For the first step, we require a mechanism for breaking an integer into all
possible combinations where the parts sum to the integer. Luckily, we have
already seen how to do this, in the context of a twist vector. We follow the
same counting algorithm outlined in @find-rat-tang-of-n however, we modify the
algorithm to keep both the even and odd outputs, but filter out stencils with
entries less than two.

```{prf:example}
:label: ex-mont-stencils

The set of all possible stencils for crossing number 5:
|                 |               |              |              |
| --------------- | ------------- | ------------ | ------------ |
| $1\ 1\ 1\ 1\ 1$ | $2\ 1\ 1\ 1 $ | $1\ 2\ 1\ 1$ | $1\ 1\ 2\ 1$ |
| $1\ 1\ 1\ 2 $   | $3\ 1\ 1 $    | $1\ 3\ 1 $   | $1\ 1\ 3 $   |
| $2\ 2\ 1 $      | $2\ 1\ 2 $    | $1\ 2\ 2 $   | $3\ 2 $      |
| $2\ 3 $         | $4\ 1 $       | $1\ 4 $      | $5 $         |

$\!\,$The set of stencils for crossing number 5:

|        |        |
| ------ | ------ |
| $3\ 2$ | $2\ 3$ |
```

For the second step, we insert unit interval rational tangles (and an integral
tangle when the stencil has length greater than two) from our existing list,
creating all combinations of input tangles given by the stencil.

```{prf:example}
:label: ex-mont-stencil_insert
:align: center

The set of rational tangles of crossing numbers two and three:

| Two         | Three        |
| ----------- | ------------ |
| $[1\ 1\ 0]$ | $[2\ 1\ 0] $ |
| $[2] $      | $[1\ 2\ 0] $ |
|             | $[3] $       |

$\!\,$The set of stencils for crossing number five, with rational tangles inserted :

| $3\ 2$                 | $2\ 3$               |
| ---------------------- | ---------------------- |
| $+[2\ 1\ 0][1\ 1\ 0] $ | $+[1\ 1\ 0][2\ 1\ 0] $ |
| $+[1\ 2\ 0][1\ 1\ 0] $ | $+[1\ 1\ 0][1\ 2\ 0] $ |
```

We conclude the section with a set of algorithms that describe this method for
computationally generating all Montesinos tangles up to a given crossing number.

```{prf:algorithm} Find all stencils of crossing number $n$
:label: find-mont-sten

**Input**

-   A crossing number

**Output**

-   All collection $S$ stencils

**Routine**

1. Generate $O$ the stencil of all $1$s for $n$
1. for $i=0$ to $2^{n-1}$
   1. Transform $i$ into binary form
   2. Exchange as in @rational-math-1plus digits of $i$ with spaces where $i$
      is $O$ and with $+$ where $i$ is $1$
   3. Apply operations to the $1$s vector and store the resulting vector as $O_r$
   4. Continue to the next iteration if $O_r$ has entries less than 2
   5. Add $O_r$ to $S$
```

```{prf:algorithm} Find all Montesinos tangles of crossing number $n$
:label: find-mont-tang-of-n
**Input**

-   All rational tangles of crossing number up to $n$

**Output**

-   All collection $T$ of Montesinos tangles

**Routine**

1. Execute @find-mont-sten for $n$
1. for each composition $c$ in in $C$
    1. Retrieve lists $L=\LS L_i\RS_i^n$ of rational tangles for each stencil
       entry $c_i$.
    1. Add to the $L_n$ list the integral tangle $c_n$
    1. While there is a list in $L$ that is not exhausted.
        1. Construct and store a Montesinos tangle from list entries.
```

```{prf:algorithm} Find all Montesinos tangles up to crossing number $n$
:label: find-mont-tang-to-n

**Input**

-   A crossing number
-   All rational tangles up to $n$

**Output**

-   All collection $T$ of twist vectors

**Routine**

1. for $i=4$ to $n$
    1. Execute @find-mont-tang-of-n with $i$
```
