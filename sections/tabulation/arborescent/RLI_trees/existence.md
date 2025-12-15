#### Existence of Right Leaning CWPTT

We start our construction of RLITT by defining what conditions make a CWPTT a
right leaning CWPTT.

```{prf:definition}
:label: rli-const-def-rl

A CWPTT is called **right leaning** if all weights are in the highest indexed
reigon (as in @indexing-rpt) of each vertex. Additionally, any ring subtrees
that are children of a vertex are the highest indexed children of that vertex.
```

Our next step is to show that every arborescent tangle has a right leaning
representative.

```{prf:theorem}
:label: rli-const-thm-rl_exists
Every arborescent tangle has a right leaning CWPTT representative.
```

```{prf:proof}
Let $\Gamma$ be a CWPTT representative for a tangle $T$. If every weight
$w_i$ of $\Gamma$ is in the highest indexed reigon of $\Gamma_{w_i}$, we
are done. Otherwise, we will follow a similar algorithm to that outlined by
Bonahon and Siebenmann [@bonahonNewGeometricSplittings2016] for distinguishing
CWPTT. Let $w_i$ be the weight for the lowest indexed vertex $v_i$ not in its
highest indexed reigon of $\Gamma_{v_i}$. With move $F_3^\prime$ shift $w_i$ so
that it lies in the highest indexed reigon. Further, choose to shift $w_i$
anti-clockwise, this ensures that $v_j$ with $j<i$ are unchanged when $w_i$ is
even. We repeat this process for any $v_k$ with $i<k$ where the weight $w_k$ not
in the highest indexed reigon. Since $\Gamma$ has finite vertices, the
algorithm terminates with a $\Gamma$ transformed into a right leaning tree
completing the proof.
```

#### Existence of Identity CWPTT

Our second step in the construction of RLITT is to define what conditions make a
CWPTT an identity CWPTT.

```{prf:definition}
:label: rli-const-def-identity
A CWPTT is called an **identity tree** if its free bond is marked by
$\iota\in V_4$.
```

Again, we must show that every arborescent tangle has an identity
representative.

```{prf:theorem}
:label: rli-const-thm-ident_exists
Every arborescent tangle has an identity CWPTT representative.
```

```{prf:proof}
Let $\Gamma$ be a CWPTT representative for a tangle $T$. If the label
$\alpha$ for the free bond of $\Gamma$ is $\iota$ we are done. Otherwise,
we fall into one of three cases:

-   $\alpha=\zeta$: In the case $\alpha$ is $\zeta$ we apply move $F_1$. This
    modifies $\alpha$ by $\zeta$ yielding $\alpha\zeta=\zeta\zeta=\iota$.
-   $\alpha=\eta$: In the case $\alpha$ is $\eta$ we apply move $F_{2e}$. This
    modifies $\alpha$ by $\eta$ yielding $\alpha\eta=\eta\eta=\iota$.
-   $\alpha=\xi$: In the case $\alpha$ is $\xi$ we apply move $F_{2o}$. This
    modifies $\alpha$ by $\xi$ yielding $\alpha\xi=\xi\xi=\iota$.

This transforms $\Gamma$ into an identity tree completing the proof.
```

#### Existence of Right Leaning Identity CWPTT (RLITT)

What we have shown is that every arborescent tangle has at least one right
leaning CWPTT and at least one identity CWPTT representative. Combining these
two ideas, we will show that every arborescent tangle has at least one CWPTT
that is right leaning and identity, we call such a CWPTT a RLITT.

```{prf:definition}
:label: rli-const-def-rlident
A CWPTT is called a **right leaning identity tangle tree (RLITT)** if it's a
right leaning and identity tree.
```

```{prf:theorem}
:label: rli-const-thm-rightident_exists
Every CWPTT has a right leaning identity representative.
```

```{prf:proof}
Let $\Gamma$ be an identity CWPTT representative for a tangle $T$.
Applying the algorithm described in the proof of
@rli-const-thm-rl_exists transforms $\Gamma$ into a right leaning
tree. Our requirement that $F_3^\prime$ be anti-clockwise ensures that the
resulting tree retains label $\iota$. This shows that $\Gamma$ can be
represented as a right leaning identity CWPTT.
```
