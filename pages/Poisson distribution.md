---
tags: stats, math, distributions
---

- a distribution for a [[discrete]] [[random variable]]. commonly used for [[ordinal data]] or [[absolute data]]. for example, the number of occurrences of a rare event within some interval, or the number of defects per item.
	- consider the **Poisson Paradigm** for approximation: if the probability of events to occur is relatively small, and the number of observations is relatively large, then we can estimate as a Poisson even if the chances aren't identical. it's OK if they're [[weakly dependent]]
	- notated $X \sim Pois(\lambda)$
	- one parameter, $\lambda$ the rate of occurrence
- formulae:
	- [[expectation]]: $\lambda$
	- [[variance]]: $\lambda$
	- [[support]]: the positive integers
	- [[PMF]]: $P(X = x) = \dfrac{e^{-\lambda} \lambda^x}{x!}$
- related to [[binomial distribution]]! as $n \rightarrow \infty$ and $p \rightarrow 0$, the binomial approaches a Poisson
- in [[R]], can use `dpois()` for exact probabilities, or `ppois()` for tails. (decrease the count by one for upper tail!). we can test if a distribution is Poisson using [[lolcat]]'s `poisson.dist.test()`. we can generate random Poisson data with `rpois()`.
	- ```
	  #generate 5 random draws from X, where X ~ Pois(3.2)
	  rpois(5, 3.2)
	  
	  # PMF, find P(X = 5), where X ~ Pois(3.2)
	  dpois(5, 3.2)
	  
	  # CDF, find P(X <= 6), where X ~ Pois(3.2)
	  ppois(6, 3.2)
	  ```