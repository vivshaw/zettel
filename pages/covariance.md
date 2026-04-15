---
tags: stats
---

- a measure of the joint variability of two random variables
- calculated as: $\operatorname{cov}(X, Y) = \operatorname{E}\big[(X - \operatorname{E}[X])(Y - \operatorname{E}[Y])\big]$
	- or equivalently, $Cov[X,Y] = E[XY] + E[X] E[Y]$
	- $Cov[X, Y] = Cov[Y, X]$
- the magnitude of covariance is arbitrary, which makes it challenging to get a good sense of how strongly the variables move together. thus, [[correlation]], which is easier to interpret
- relation to [[variance]]:
	- $Cov[X, X] = Var[X]$
	- we can use it to sum variances! $Var[X + Y] = Cov[X + Y, X + Y] = Var[X] + Var[Y] + 2 Cov[X, Y]$
- relation to [[independence]]: if two vars are independent, they must have covariance 0, but not necessarily vice-versa! for example, if $X$ is the integers and $Y$ is their squares, they'll have zero covariance, but they're clearly dependent!