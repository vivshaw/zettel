---
tags: stats
---

- when we know the population [[standard deviation]], we can find our minimum sample size...
	- for directional hypotheses, with `n = (z_alpha + z_beta)^2 * sigma^2 - delta^2`, where `delta` is the effect size
	- for non-directional hypotheses, with `n = (z_alpha/2 + z_beta)^2 * sigma^2 - delta^2`
	- in [[R]], we can use `lolcat`'s `sample.size.mean.z.onesample()`
- when we don't, we can do the same with the T distribution, but we have to do it iteratively (since the degrees of freedom depend on the sample size!)
	- in [[R]], we can use `lolcat`'s `sample.size.mean.t.onesample()`
- in [[R]], for [[variance]] we can use `lolcat`'s `sample.size.variance.onesample()`.
	- if we are testing a non-directional hypothesis, we should take the estimate for both the higher and lower variance, and use whichever sample size is larger.
- in [[R]], for proportions we can use `lolcat`'s `sample.size.proportion.test.onesample.exact()`.
	- as with variance, we'll need to run it twice and choose the larger if the hypothesis is nondirectional