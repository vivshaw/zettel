---
tags: stats, statistical tests
alias: repeated measures t-test, matched pairs t-test
---

- a [[mean]] test for [[dependent samples]], using a [[t-test]]. operates on pairs of scores.
	- you can use this either with paired samples or repeated samples.
	- generally, you want 30 samples for each pair
- assumptions:
	- the *pairs* of scores are independent of each other
	- the populations are normally distributed, *as are the difference scores*
- calculated as: $t = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n} + \frac{s_2^2}{n} - 2r\frac{s_1}{\sqrt{n}}\frac{s_2}{\sqrt{n}}}} = \frac{\bar{D}}{\frac{S_d}{\sqrt{n}}}$
	- where $n$ is the sample size of the pairs of scores
- in [[R]], we can use [[lolcat]]'s `t.test.twosample.dependent()`
	- there is a `.dbar()` version, for when you only have the differences
- in [[python]], we can use [[scipy]]'s `stats.ttest_rel()` or [[pingouin]]'s `ttest()`