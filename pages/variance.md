---
tags: stats, data
---

- a measure of [[dispersion]] of a [[random variable]]
- the average squared distance a value falls from the mean. effectively, the square of the [[standard deviation]]
- calculated $Var(X) = \sum_i (x_i - E(X))^2 P(X = x_i)$
	- equivalently, $Var(X) = E(X^2) - E(X)^2$
	- to sum, $Var[X + Y] = Cov[X + Y, X + Y] = Var[X] + Var[Y] + 2 Cov[X, Y]$ (see [[covariance]] )
	- variance is _not_ a linear operator. $Var(3X)$ = $9 Var(X)$
- symbols:
	- $\sigma^2$ for a population, $s^2$ for a sample