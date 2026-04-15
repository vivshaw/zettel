---
tags: math, stats, distributions
---

- a distribution for a [[discrete]] [[random variable]]. suppose we're flipping a coin until we get our first heads, and we want to know how many tails we get along the way?
	- notated $X \sim Geom(p)$
	- one parameter, $p$ probability of success
- it is [[memoryless]]
- formulae:
	- [[expectation]]: $\dfrac{1}{p}$
	- [[variance]]: $\dfrac{1-p}{p^2}$
	- [[PMF]]: $P(X = x) = (1 - p)^{x - 1}(p)$ (including first success), or $P(X = x) = (1 - p)^x(p)$ (excluding)