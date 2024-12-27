---
tags: stats
---

- compare a [[linear model]] to this *additive model*
	- $E(Y_i | X_i) = \Beta_0 + r_1(X_{i1}) ... r_p(X_{ip})$
		- such that each $r_j$ is an arbitrary univariate function
- we can now generalize this additive model, much like we would with a [[generalized linear models]]. we'll have a random component (the distribution), a systematic component (the additive model), and a link function
	- we can estimate the $r$s non-parametrically!