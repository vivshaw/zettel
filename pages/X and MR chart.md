---
tags: spc, dataviz, stats
alias: individual and moving range chart
---

- a continuous [[control chart]] for individual units. you might use it when measures are very expensive, or extremely homogenous, or don't fall into logical subgroups.
	- some disadvantages: it's less sensitive to shifts in the mean, it's less obvious when you're using the wrong distribution, and [[autocorrelation]] can mess 'em up
	- also, standard [[Nelson rules]] for runs and trends don't apply
- it consists of two charts: one of the individual observations, and another of the [[moving range]].
	- for the range, the upper and lower control limits are $UCL_{MR} = D_4\bar{MR}$ and $LCL_{MR} = D_3\bar{MR}$
	- for the mean, the upper and lower control limits are $UCL_{X} = \bar{X} + \dfrac{AE_2\bar{MR}}{3}$ and $LCL_{X} = \bar{X} - \dfrac{AE_2\bar{MR}}{3}$
		- or if it's stable and normally distributed, $\bar{X} +/- A(s)$
	- for the median, the upper and lower control limits are $\bar{X} +/- \dfrac{A\tilde{MR}}{\tilde{d}_2}$
		- (you might prefer the median if the process is not stable)
	- (see the [[control chart constants]] for where these values come from)
- in [[R]], we can use `spc.chart.variables.individual.and.movingrange.normal.simple()`
- we can use this chart for non-normal data as well!
	- one would be to transform it to a normal distribution, such as [[log-normal]] or [[Box-Cox]]
	- another would be to use another model that _does_ fit, e.g. an [[exponential distribution]]
	- or, to fit a distribution post-hoc, such as a [[Johnson distribution]]