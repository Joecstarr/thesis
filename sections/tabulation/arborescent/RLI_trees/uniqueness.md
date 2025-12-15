#### Uniqueness of Right Leaning Identity CWPTT

Our final step at identifying a preferred representative CWPTT of an arborescent
tangle is to show that a $\LP +\RP$-RLITT is unique in the set of CWPTT
representing an arborescent tangle. We will utilize the key proposition from
Bonahon and Siebenmann [@bonahonNewGeometricSplittings2016] a consequence of
@wpt-equi-thm-classi and @wpt-equi-cor-algo.

```{prf:proposition} Bonahon and Siebenmann proposition 12.2 [@bonahonNewGeometricSplittings2016]
:label: rli-const-prop-not_iso
Let $\Gamma$ and $\Gamma^\prime$ be $\LP +\RP$-CWPTT tangle trees with isomorphic
underlying abstract trees. Further, let $\varphi$ be a sequence of moves of the
calculus of arborescent tangles. Assume that there is an $i > 0$ such that
$\varphi$ respects the cyclic orders of weight and bonds at each vertex $v_j$
with $j < i$, and that the labels of the free bond $\alpha$ in
$\Gamma$ and of $\varphi\LP \alpha\RP$ in $\Gamma^\prime$ are identical. Assume
moreover that one of:

1. $\varphi$ reverses the cyclic order of bonds at $v_i$
2. $\varphi$ does not respect the label in $V_4$ of some free bond of a
   vertex $v_j$ with $1 \leq j < i$.

Then $\varphi$ is not a sequence of moves of the calculus of arborescent tangles
taking $\Gamma^\prime$ to $\Gamma$.

```

```{prf:theorem}
:label: rli-const-thm-RLITT_unique
The $\LP +\RP$-RLITT representative is unique in the class of CWPTT.
```

```{prf:proof}
Let $\Gamma$ and $\Gamma^\prime$ be two $\LP +\RP$-RLITT representatives for an arborescent
tangle $T$. Assume for the sake of contradiction that
$\Gamma\neq \Gamma^\prime$, meaning $T$ has two distinct $\LP +\RP$-RLITT. The
classification result in @wpt-equi-thm-classi and algorithm given
by @wpt-equi-cor-algo we produce a sequence of moves in the
calculus of arborescent tangles that takes $\Gamma^\prime$ to $\Gamma$. Let
$\varphi$ be such a sequence. By construction the labels in $V_4$ of $\Gamma$
and $\Gamma^\prime$ agree. Now, since $\Gamma\neq \Gamma^\prime$ there must be a
first, in the total order, vertex $v_i$ where $\Gamma$ and $\Gamma^\prime$
disagree. As $\LP +\RP$-RLITT the location of weights for $v_i$ in $\Gamma$ and
$\Gamma^\prime$ must appear in the same reigon. This requires that the
disagreement at $v_i$ must be in cyclic order of its children. We find ourselves
in the first case of @rli-const-prop-not_iso, making $\varphi$ not a
sequence of moves of the calculus of arborescent tangles taking $\Gamma^\prime$
to $\Gamma$.
```
