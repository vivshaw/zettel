tags:: stats, regression
alias:: GLM

- an approach that unifies multiple different regression models- [[linear regression]], [[logistic regression]], [[Poisson regression]]...
	- we generalize linear regression, by applying a [[link function]] that transforms the result. we pick a link function based on the distribution of the data we wish to estimate.
	- in a sense, there's a random component (distribution of the target, a member of the [[exponential family]]), a systematic component (the linear relation with the predictors), and the link function
	- this is the core of why linear, logistic, and Poisson regression are very mathematically similar!
- for example:
	- [[linear regression]] : continuous data in a [[normal distribution]] : [[linear]] linking function
	- [[logistic regression]] : discrete binary classification data in a [[Bernoulli distribution]] or [[binomial distribution]] : [[logit]] linking function
	- [[Poisson regression]] : discrete numerical data (counts) in a [[Poisson distribution]] : [[log]] linking function
- conceptually, to find the link function, you can think: *how could I solve for a linear function of the predictors and* $\beta$*s on one side? what would then be on the other side?*
- let:
	- $X \in \mathbb{R}^p$ (X is a vector of real number predictors)
	- we assume $g(E(Y | X) = \beta^T \cdot X$ for some function $g$ and some $\beta \in \mathbb{R}^p$
	- for linear regression:
		- $y \in \mathbb{R}$ (y, the target, is real)
		- we assume $E(Y | X) = \beta^T \cdot X$
			- so $g(x) = x$, that is to say, $g$ is the [[identity (math)]]
	- for logistic classification:
		- $y \in \{0, 1\}$
		- we assume $log(\dfrac{P(y=1 | X)}{1 - P(y=1 | X)}) = \beta^T \cdot X$ for some $\beta \in \mathbb{R}$
			- so $g(x) = \operatorname{logit}(x)$, the [[logit]]
- in [[R]], we can use the `glm()` function together with a `family = ` parameter to use a GLM however we'd like. we can then use `predict(glm.fit, type = "response")` to predict.
	- but we'll get probabilities as our output, so we'll need to transform into class labels, like `ifelse(glm.pred > 0.5, T, F)`
	- we can also use it with [[tidymodels]]- just set `"glm"` as the engine!