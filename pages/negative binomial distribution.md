---
tags: math, stats, distributions
---

- a distribution for a [[discrete]] [[random variable]]. if we are doing an unlimited number of [[Bernoulli distribution]] trials, how many failures should we expect before we get $r$ successes?
	- notated $X \sim NBin(r, p)$
	- paramters $r$ for target number of successes, $p$ for probability of success
	- related to the [[binomial distribution]] because it's basically just $r$ repeats of a binomial. related to the [[geometric distribution]] similarly to how binomial relates to Bernoulli- generalizing from 1 success to many
- formulae:
	- [[expectation]] : $\dfrac{r(1-p)}{p}$
	- [[variance]]: $\dfrac{r(1-p)}{p^2}$
	- [[PMF]]: $P(X = x) = \binom{x + r - 1}{r -1} p^r (1-p)^x$