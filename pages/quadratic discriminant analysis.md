---
tags: stats
---

- a [[generative model]] similar to [[linear discriminant analysis]], but with relaxed assumptions. a special case of the [[Bayes classifier]].
	- specifically, it removes the assumption of equal variance. QDA assumes that each class has its own [[covariance]] matrix $\Sigma$. the rest is just like LDA!
	- generally, QDA is more flexible than LDA, but has higher variance.
		- QDA estimates a quadratic boundary between classes.
	- QDA also needs to estimate more parameters ($\frac{K \cdot p \cdot (p+1)}{2}$ as opposed to $K \cdot p$)
- we end up with this:
	- $\delta_k(x) = -\dfrac{1}{2} \cdot X^T \cdot \Sigma^{-1}_k \cdot x + x^T \cdot \Sigma^{-1}_k \cdot \mu_k - \dfrac{1}{2} \cdot \mu_k^T \cdot \Sigma^{-1}_k \cdot \mu_k + log(\pi_k)$
- we can use [[tidymodels]]'s `discrim_quad()` with [[MASS]] as an engine