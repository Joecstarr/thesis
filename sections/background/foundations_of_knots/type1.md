###### Kauffman Bracket: Type I

With the writhe we're ready to approach the bracket polynomial applied to the
type I move. We augment the type I move with the addition of multiplication by a
$-A^{-3w\LP K\RP}$ term obtaining the following theorem.

We first compute our writhes

````{prf:theorem}
:label: thm-typei
```{math}
    \begin{aligned}
        -A^{-3w\LP
            \img{media/kauf_bkt/type1/1b}\RP}\bkt{media/kauf_bkt/type1/1b}
            & = \bkt{media/kauf_bkt/type1/3}\\
        -A^{-3w\LP
            \img{media/kauf_bkt/type1/1}\RP}\bkt{media/kauf_bkt/type1/1}
            & = \bkt{media/kauf_bkt/type1/3}\\
    \end{aligned}
```
````

````{prf:proof}

We first compute our writhes
```{math}
    \begin{aligned}
            -w\LP \img{media/kauf_bkt/type1/1b}\RP=-1\\
            -w\LP \img{media/kauf_bkt/type1/1}\RP=1\\
    \end{aligned}
```
now computing each flavor of type I move in turn
```{math}
\begin{aligned}
        -A^{-3w\LP
    \img{media/kauf_bkt/type1/1b}\RP}\bkt{media/kauf_bkt/type1/1b}
    & =
    \LP-A^{3}\RP\LP-A^{-3}\bkt{media/kauf_bkt/type1/3}\RP \\
        & =
    \LP-A^{3}\RP\LP-A^{-3}\bkt{media/kauf_bkt/type1/3} \RP\\
        & = \bkt{media/kauf_bkt/type1/3} \\
\end{aligned}
```
```{math}
\begin{aligned}
        -A^{-3w\LP
    \img{media/kauf_bkt/type1/1}\RP}\bkt{media/kauf_bkt/type1/1}
    & =
    \LP-A^{-3}\RP\LP-A^{3}\bkt{media/kauf_bkt/type1/3}\RP\\
        & =
    \LP-A^{-3}\RP\LP-A^{3}\bkt{media/kauf_bkt/type1/3} \RP\\
        & = \bkt{media/kauf_bkt/type1/3} \\
\end{aligned}
```
the desired sets of equality.
````
