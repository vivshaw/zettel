---
tags: stats, data, distributions
alias: uniform
---

- a distribution for a [[continuous]] [[random variable]] where every possible value has equal probability
	- formulae:
		- [[PDF]]: $f(x) = \begin{cases} \frac{1}{b-a} \text{ if } a \leq x \leq b \\ 0 \text{ else} \\ \end{cases}$
		- [[CDF]]: $P(X \leq x) = \dfrac{x-a}{b-a}$
		- [[expectation]]: $E(X) = \dfrac{b - a}{2}$
		- second [[moment]]: $E(X^2) = \dfrac{b^2 + ab + a^2}{3}$
		- [[variance]]: $Var(X) = \dfrac{(b-a)^2}{12}$
- **universality of the uniform**: if you want to create a distribution with CDF $Foo$, you can simply let $X = Foo^{-1}(U(X))$
	- similarly, for any random variable $X$ with CDF $Bar$, $Bar(X)$ follows a standard uniform distribution $Unif(0, 1)$