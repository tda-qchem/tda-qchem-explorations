

A list of molecular descriptors represented by a scalar field $f(\vec{r})$ defined
on the molecular domain ${\cal M} \subset \mathbb{R}^3$, $f: \vec{r} \in {\cal M} \rightarrow \mathbb{R}$:

* electron density (ED), $\rho(\vec{r})$

* reduced density gradient (RDG),  $s(\vec{r})$:

$$
s(\vec{r}) = \frac{1}{2(3\pi^2)^{1/3}}\frac{|\nabla\rho(\vec{r})|}{\rho(\vec{r})^{4/3}}
\label{eq:redgrad}
$$

* the sign of the Laplacian of the ED (L2(ED)), $sign(\lambda_2)\rho(\vec{r})$

* molecular electrostatic potential (MESP), $V(\vec{r})$:

$$
  V(\vec{r}) = \sum_{A}^{N} \frac{Z_A}{|\vec{r} - \vec{R}_A|} 
             - \int \frac{\rho(\vec{r}\ ')}{|\vec{r} - \vec{r}\ '|} d^3 \vec{r}\ '
  \label{eq:mesp}
$$

* bare nuclear potential (BNP), $V_{nuc}(\vec{r})$:

$$
  V_{nuc}(\vec{r}) = \sum_{A}^{N} \frac{Z_A}{|\vec{r} - \vec{R}_A|} 
  \label{eq:bnp}
$$


A list of molecular descriptors represented by a second-order tensor field $t(\vec{r})$ defined
on the molecular domain ${\cal M} \subset \mathbb{R}^3$, $t: \vec{r} \in {\cal M} \rightarrow \mathbb{R}^3 \times \mathbb{R}^3$:

* magnetically-induced current density (MICD), $j^B$:



