---
tags: math, stats
---

- when we are working with multiple samples, that we presume to have the same variance, we can achieve a higher-precision estimate of the variance by pooling the variance from all samples together.
- calculated as $s_p^2 = \frac{(n_1-1)s_1^2+(n_2-1)s_2^2 + \cdots + (n_k - 1)s_k^2}{(n_1 - 1) + (n_2 - 1) + \cdots +(n_k - 1)}$
- in [[R]], we can use `weighted.mean()`, like so:
	- ```R
	  pooled.variance <- weighted.mean(x = c(var_1, var_2), w = c(n_1, n_2))
	  ```