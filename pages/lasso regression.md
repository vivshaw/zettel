---
tags: stats, regression, regularization
---

- similar to [[ridge regression]], except regularizes with the [[L1 norm]] instead of the [[L2 norm]]. useful when there is [[multicollinearity]].
	- LASSO = Least Absolute Shrinkage and Selection Operator
- we minimize $\underset{\beta}{\mathrm{argmin}}|| y - X B ||_2^2 + \lambda|| B ||_2$, where the first have is the [[SSE]] just like [[OLS]]
	- unlike with ridge, there isn't a simple closed-form solution!
- in comparison to [[ridge regression]], lasso more often takes a parameter all the way to zero.
- we can do this in [[R]] with `glmnet()` from the `glmnet` package, setting the `alpha` parameter to 1:
	- ```R
	  glmnet(as.matrix(data), labels, alpha = 1, family = "gaussian", lambda = 0.3) 
	  ```