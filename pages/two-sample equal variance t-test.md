---
tags: stats, statistical tests
---

- a [[mean]] test for two samples, when we don't know the population variance, but believe it to be equal. it is a type of [[t-test]].
- assumptions:
	- the samples are randomly selected from independent populations
	- the populations are normally distributed
	- the [[variance]] of the two populations is equal, but...
	- that variance is unknown
- calculated as $t_{df} = \dfrac{\bar{X}_1-\bar{X}_2}{\sqrt{s^2_p}(\dfrac{1}{n_1}+\dfrac{1}{n_2})}$, where
	- $s^2_p$ is the [[pooled variance]]
	- the degrees of freedom $df = n_1 + n_2 - 2$
- in [[R]], we can use `t.test.twosample.independent()` from [[lolcat]].
	- if our data is in [[independent format]], we will either need to
		- subset it with the grouping variable (like `Data$Foo[Data$Group==1]`), so we can pass `g1` and `g2`, OR
		- convert the grouping variable into a factor with `as.factor()`, so we can use function notation and pass `fx = Foo ~ Group`