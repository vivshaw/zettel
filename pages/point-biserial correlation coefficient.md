---
tags: stats, [[relationship (stats)]]
---

- $\rho_{pbi}$, a measure of [[correlation]] between a continuous variable and a two-outcome nominal variable.
- assumptions:
	- the pairs are independent
	- one variable is continuous, the other is dichotomous
	- the continuous variable is [[normally distributed]]
	- the items within each level of the dichotomous variable are independent
- in [[R]], we can use `cor()` for this. it will automatically choose this method when we provide this sort of data. we can use `cor.test()` to test if the correlation is different from 0. [[lolcat]]'s `cor.point.biserial()` will also do this.