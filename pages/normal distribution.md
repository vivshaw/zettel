---
tags: stats, data, distributions
alias: normal, normally distributed, normality, Gaussian
---

- a distribution for [[continuous data]], and one of the most common.
	- notated $X \sim N(\mu, \sigma)$
	- parameters $\mu$ the [[mean]], and $\sigma$ the [[standard deviation]]
- characteristics:
	- symmetric around $\mu$
	- all measures of central tendency are equal ([[mean]], [[median]], and [[mode]])
	- [[skewness]] and [[kurtosis]] are 0
	- the tails extend to infinity, but never hit 0
- formulae:
	- [[PDF]]: $f(x) = \dfrac{1}{\sigma \sqrt{2\pi}} e^{-(x-\mu)^2 / 2\sigma^2}$ for $-\infty \leq x \leq \infty$
	- [[expectation]]: $E(X) = \mu$
	- [[variance]]: $Var(X) = \sigma^2$
- when $\mu$ is $0$ and $\sigma$ is $1$, we have a **standard normal**, which is often easier to work with:
	- $f(x) = \dfrac{1}{\sqrt(2\pi)} e^{-x^2/2}$ for $-\infty \leq x \leq \infty$
	- you can convert! $\dfrac{X - \mu}{\sigma} \sim N(0, 1)$
	- [[CDF]]: $\Phi(z) = P(Z \leq z) =  \dfrac{1}{\sqrt{2\pi}} \int^z_{-\infty} e^{-x^2/2} dx$
- you can determine how far any given value is from the mean using a [[z-score]]
- we can test for normality:
	- when n < 25, we can use the [[Anderson-Darling test]] or [[Shapiro-Wilk test]]
	- when n >= 25, we can use the [[moment tests]]
- in [[R]], you can use `pnorm` to get the tail probability.