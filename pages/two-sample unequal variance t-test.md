---
tags: stats, statistical tests
alias: Welch's test
---

- a [[mean]] test for two samples, when we don't know the population variance, but believe it to be unequal. it is a type of [[t-test]].
- assumptions:
	- the samples are randomly selected from independent populations
	- the populations are normally distributed
	- the [[variance]] of the two populations is unequal
	- that variance is unknown
- calculated as $t_{df} = \dfrac{\bar{X}_1-\bar{X}_2}{\sqrt{\dfrac{s^2_1}{n_1}+\dfrac{s^2_2}{n_2}}}$, where
	- the degrees of freedom are weighted: $df^* = \dfrac{[\dfrac{s^2_1}{n_1}+\dfrac{s^2_2}{n_2}]^2}{[\dfrac{(\dfrac{s^2_1}{n1})^2}{n_1 - 1}+\dfrac{(\dfrac{s^2_2}{n2})^2}{n_2 - 1}]}$
		- this is also known as Satterthwaite's Formula
- in [[R]], we can use `t.test.twosample.independent()` from [[lolcat]], as we would with the [[two-sample equal variance t-test]]
- in [[python]], we can use [[scipy]]'s `stats.ttest_ind()`, or [[pingouin]]'s `ttest()`