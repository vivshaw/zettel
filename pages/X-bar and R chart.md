---
tags: spc, dataviz, stats
alias: mean and range chart
---

- a continuous [[control chart]] for small samples ($<8$).
- it consists of two charts: one of the [[mean]], and another of the [[range]].
	- for the range, the upper and lower control limits are $UCL_R = D_4\bar{R}$ and $LCL_R = D_3\bar{R}$
		- where $D_4 = 1 + 3 \dfrac{d_3}{d_2}$ and $D_3 = 1 - 3 \dfrac{d_3}{d_2}$
	- for the mean, the upper and lower control limits are $UCL_{\bar{X}} = \bar{\bar{X}} + A_2\bar{R}$ and $UCL_{\bar{X}} = \bar{\bar{X}} - A_2\bar{R}$
		- where $A_2 = \dfrac{3}{d_2\sqrt{n}}$
	- (see the [[control chart constants]] for where these values come from)
- in [[R]], we can use [[lolcat]]'s `spc.chart.variables.mean.and.meanrange()`
- if you see the values...
	- hugging the midline, that's a sign that there's drastically more within-sample variation than between-sample variation. that might happen in a [[setup dominant]] process.
	- avoiding the midline, that's a sign that there's drastically less within-sample variation than between-sample variation. that might happen in a [[machine dominant]] process.