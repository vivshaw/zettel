tags:: stats, regression

- commonly used for modeling binary classifiers / [[qualitative data]] . we use a logistic curve, and call everything above the midpoint a 1, and everything below the midpoint a 0.
- simple logistic regression for a binary classifier looks like:
	- $P(x) = \dfrac{e^{\beta_0 + \beta_1x}}{1 + e^{\beta_0 + \beta_1x}}$
	- as a corollary, the [[odds]] ($\dfrac{p(x)}{1- p(x)}$) equal $e^{\beta_0 + \beta_1x}$
	- we might also want a [[logit]], the log odds, which equals $\beta_0 + \beta_1x$
- multiple logistic regression for a binary classifier looks like:
	- $P(x) = \dfrac{e^{\beta_0 + \sum^p_{i=1}{\beta_ixi}}}{1 + e^{\beta_0 + \sum^p_{i=1}{\beta_ixi}}}$
- multinomial response (used with multiple classes) looks like:
	- $P(Y=K|X=x) = \dfrac{e^{\beta_{K0} + \beta_{K1}x}}{1 + \sum^{K-1}_{l=1}{e^{\beta_{l0} + \beta_{l1}x}}}$, for a given class of the $K$ classes
	- in essence, comparing the likelihood of each other class, to the likelihood of the baseline class
	- in practice, we might use [[softmax]], in which we do $P(Y=K|X=x) = \dfrac{e^{\beta_{K0} + \beta_{K1}x}}{\sum^{K}_{l=1}{e^{\beta_{l0} + \beta_{l1}x}}}$ for all classes. in essence, we eliminate the baseline class.
- in [[R]], we can use a [[GLM]] with `family = "binomial"` [[tidymodels]]' `logistic_reg()`