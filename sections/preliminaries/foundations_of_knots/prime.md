<!-- prettier-ignore-start -->
(subsec-prime_knot)=
### Prime Knots
<!-- prettier-ignore-end -->

With the goal of enumerating objects, we should be clear on what types of objects should be
enumerated and which should be left uncounted. We now describe the class of knot that tabulators are
interested in, the **prime knots**. The first step is to define an operation on knots called the
**connect sum**.

````{prf:definition}
For knots $J$ and $K$, the **connect sum** $J\#K$ is produced by:

1. Excising an arc from both $J$ and $K$
2. Gluing endpoints of $J$ to endpoints of $K$

```{figure} ../../media/fig-prime_knot-connect_sum.svg
:label: fig-prime_knot-connect_sum
An example of the connect sum of two trefoil knots.
```
````

With the connect sum operation defined, we are now prepared to give the definitions for prime and
composite knots.

```{prf:definition}
A knot is called **prime** if, in every decomposition into a connected sum, one
of the factors is unknotted. Otherwise, the knot is called **composite**.
```
