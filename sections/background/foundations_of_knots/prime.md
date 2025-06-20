<!-- prettier-ignore-start -->
(subsec-prime_knot)=
### Prime Knots
<!-- prettier-ignore-end -->

With the goal of enumerating objects, we should be clear on what types of object
should be enumerated and which should be left uncounted. We now describe the
class of knot that tabulators are interested in, the **prime knots**. The first
step is to define an operation on knots, called the **connect sum**. Given two
knots $J$ and $K$, the connect sum of $J$ and $ K$, written $J\#K$, is produced
by first excising an arc from both $J$ and $K$, and then glueing endpoints of
$J$ to endpoints of $K$ (@fig-prime_knot-connect_sum).

```{figure} ../../media/fig-prime_knot-connect_sum.svg
:label: fig-prime_knot-connect_sum
An example of the connect sum of two trefoil knots.
```

With the connect sum operation defined, we are now prepared to give the
definitions for prime and composite knots.

```{prf:definition} Prime and Composite Knots [@jablanLinKnotKnotTheory2007]
A knot is called **prime** if, in every decomposition into a connected sum, one
of the factors is unknotted. Otherwise, the knot is called **composite**.
```
