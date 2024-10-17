tags:: stats, Poisson, regression

- a regression used to model counts.
	- $P(y=k) = \dfrac{e^{-\lambda} \cdot \lambda^k}{K!}$
	- $\lambda(x_1, ..., x_p) = e^{\beta_0 + \beta_1 \cdot x_1 + ... + \beta_p \cdot x_p}$
- we want to maximize:
	- $l(\beta_0, ..., \beta_p) = \Pi^n_{i=i} {\dfrac{e^{-\lambda(x_i)} \cdot \lambda(x_i)^{y_i}}{y_i!}}$
- in [[R]], we can do a [[GLM]] like so: `model.pois = glm(y ~ x.1 + x.2, data = Data, family = poisson)`
	- or, we can use [[tidymodels]]' `poisson_reg()` with the `glm` engine