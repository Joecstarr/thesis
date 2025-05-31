<!-- prettier-ignore-start -->
(subsec-prime_knot)=
### Prime Knots
<!-- prettier-ignore-end -->

When enumerating objects it's important to be clear on what types of object
should be enumerated and which should be left uncounted. In this section we
describe the class of knot that is of particular interest to tabulators, the
prime knots. The first step is to define the connect sum operation on knots.
Given two knots $J$ and $K$, the connect sum of $J$ and $ K$, written $J\#K$, is
given by first excising an arc from both $J$ and $K$, and then glueing endpoints
of $J$ to endpoints in $ K$. We can see an example of the connect sum of a
trefoil and figure 8 knot in @fig-prime_knot-connect_sum

```{figure} ./media/fig-prime_knot-connect_sum.svg
:label: fig-prime_knot-connect_sum
@@@ TODO: Add content description
```

With the connect sum operation we are now prepared to give the key definition
for the section.

```{prf:definition} Prime and Composite Knots [@jablanLinKnotKnotTheory2007]
A knot is called **prime** if in every decomposition into a connected sum, one of
the factors is unknotted. Otherwise, the knot is called **composite**.
```
