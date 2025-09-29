---
tags: stats
---

- **analysis of variance** is a test of differences in [[mean]]s for more than two groups. it allows us to test hypotheses with > 2 levels. it works by comparing variation _between_ groups, to variation _within_ groups
	- we use this over running multiple [[t-test]]s because running multiple tests inflates [[type-1 error]]!
- assumptions:
	- the data is at least [[interval data]]
	- each treatment population is [[normally distributed]]
	- the treatment populations have equal [[variance]]
	- both individuals and groups are independent
- ANOVA is robust to the normality assumption for large $n$ (e.g., 10-15), and equal variances if group sizes are equal
- in [[python]], we can use [[pingouin]]'s `anova(data=foo, dv="depedent var", between="anova categories")`