---
tags: stats, statistical tests
---

- a statistical test for [[mean absolute deviation]], which uses a [[t-test]] for two samples, or the [[ANOVA]] for more than two
- assumes that the data is [[normal]]
- to do this in [[R]] for two samples:
	- classify the grouping variable as a factor
	- calculate the [[mean absolute deviation]]
	- then, use `t.test.twosample.independent.fx()`