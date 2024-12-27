---
tags: stats, ANOVA
alias: Fisher ANOVA
---

- an ANOVA version that is one-way and assumes equal variance between the groups.
	- see also [[Welch's ANOVA]] for cases with _unequal_ variance
- assumptions:
	- the data is at least [[interval data]]
	- each treatment population is [[normally distributed]]
	- the treatment populations have equal [[variance]]
	- both individuals and groups are independent
- to perform:
	- we calculate the within-subgroup variance as: $\hat{\sigma}^2 = \frac{\sum{s^2_j}}{J}$, aka **mean square within** ($MS_W$)
	- and the between-subgroup variance as: $\hat{\sigma}^2 = ns\frac{2}{X}$, aka **mean square between** ($MS_B$)
	- then we calculate an F-score as: $F = \frac{MS_B}{MS_W}$
- in [[R]], we can use `aov()`.
	- ⚠️ we need to make sure the grouping variable is a factor, though!
	- we can then summarize with `summary()`
	- we can use `anova_stats()` from `sjstats` on a linear model to get the [[importance]]