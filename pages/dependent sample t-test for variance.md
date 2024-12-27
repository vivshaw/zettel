---
tags: stats, statistical tests
---

- a [[variance]] test for [[dependent samples]], using a [[t-test]]
- assumptions:
	- the pairs of samples are independent
	- the sample data are dependent
	- the underlying populations are [[normally distributed]]
- calculated as: $t = \frac{s_1^2 - s_2^2}{2s_1s_2\sqrt{\frac{1 - r^2}{n -2}}}$, where $r$ is the [[correlation]]
- in [[R]], we can use [[lolcat]]'s `variance.test.twosample.dependent()`