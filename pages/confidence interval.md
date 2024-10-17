tags:: stats, data

- a **confidence interval** for a given [[estimate]] is a range within which we'd expect to see the real population parameter, given a certain confidence level
	- the [[type-1 error]] for the interval, is in fact the same as the confidence level!
- for the [[mean]], can be calculated like so:
	- if the population standard deviation is known, or the sample size is >= 30, `mu_ci = X_bar +/- z * (sigma / sqrt(n))`, where `z` is the [[z-score]] of the given confidence interval. this is a [[z-test]].
	- if the population standard deviation is *unknown* or the sample is small, we use mu_ci = X_bar +/- t * (sigma / sqrt(n)), where `t` is the [[t-score]] of the given confidence interval. this is a [[t-test]].
- for [[variance]], the [[Central Limit Theorem]] doesn't hold, so we need to use a [[chi-square test]]
- for a [[proportion]], we'll use a [[binomial test]]
- for a [[Poisson distribution]] rate, we use a [[Poisson test]]
- in [[R]], the `confint()` function may be of interest