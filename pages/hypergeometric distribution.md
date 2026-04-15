---
tags: stats, math, distributions
---

- for a [[discrete]] [[random variable]]. useful for sampling without replacement from a finite population and counting the number of successes
	- notated $X \sim HGeom(w, b, n)$
	- parameters $w$ success objects, $b$ failure objects, $n$ number of draws
- formulae:
	- [[expectation]]: $\dfrac{nw}{w+b}$
	- [[PMF]]: $P(X = x) = \dfrac{\binom{w}{x} \binom{b}{n-x}}{\binom{w+b}{n}}$