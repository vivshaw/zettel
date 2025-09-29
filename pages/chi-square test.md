---
tags: stats, statistical tests
---

- a test for that uses the [[chi-square distribution]]
	- you can think of it as a generalization of [[proportions]] to >2 groups, much like you can think of [[ANOVA]] as a generalization of [[t-test]]s to >2 groups
- assumptions:
	- the population is normally distributed
	- the specimens are independent
- calculated as $\chi^2=\sum{\dfrac{(O_i-E_i)^2}{E_i}}$, where $O_i$ is the observed value, and $E_i$ is the expected value
- in [[R]], you can use `chisq.test()` for this.
- in [[python]], you can use [[pingouin]]'s `chi2_independence()`
- commonly used for testing [[variance]] or [[independence]]
- most commonly, a right-tailed test