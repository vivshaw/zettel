---
tags: stats, [[statistical tests]]
---

- any time you do a two-sample test, you must test (in this order!) for:
	- [[normality]] (which verifies our assumptions about the variance)
	- [[variance]] (which verifies our assumptions about the means)
	- [[mean]]
- when we have [[independent samples]]...
	- and we're testing for means...
		- if we don't know the variance...
			- and we presume the variances are *equal*, we'll use the [[two-sample equal variance t-test]]
			- and we presume the variances are *unequal*, we'll use the [[two-sample unequal variance t-test]]
	- and we're testing for [[dispersion]] ...
		- use the [[two-sample F test]] for [[variance]]
		- OR, the [[Levene test]] for [[mean absolute deviation]]
		- OR, the [[Brown-Forsythe test]] when the data is not normal