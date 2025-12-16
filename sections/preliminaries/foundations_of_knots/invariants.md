<!-- prettier-ignore-start -->
(subsec-invariant)=
### Knot Invariants
<!-- prettier-ignore-end -->

Our next topic of interest is that of a knot invariant. In general, an invariant for an object is a
datum that is computed deterministically for the object and remains unchanged within an equivalence
class. In the knot case, we will take the concept of equality to be that given in
@subsec-knot_equivalence. As discussed in @sec-history-of-tabulation, invariants play an important
role in computer tabulation. We will now describe a simple invariant we first introduced in
@subsec-knot_equivalence.

#### Minimal Crossing Number

We saw at the end of @subsec-knot_equivalence the definition of the minimal crossing number for a
knot. That being the minimal number of crossings needed to represent the knot as a diagram. Somewhat
intuitively, this number is an invariant for a knot. If a knot has minimal crossing number $4$, we
will never be able to represent it with three crossings, so it has to be different from the trefoil
knot (a knot with three crossings). However, we can see from the table of the first seven knots
(seen in @fig-hist-7table) that having equivalent crossing number does not give us equivalent knots.
