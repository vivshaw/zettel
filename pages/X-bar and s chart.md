tags:: spc, dataviz, stats
alias:: mean and standard deviation chart

- a continuous [[control chart]] for large samples ($>=8$). it is less influenced by extreme values than the [[X-bar and R chart]].
- it consists of two charts: one of the [[mean]], and another of the [[standard deviation]].
	- for the standard deviation, the upper and lower control limits are $UCL_S = B_4\bar{S}$ and $LCL_S = B_3\bar{S}$
	- for the mean, the upper and lower control limits are $UCL_{\bar{X}} = \bar{\bar{X}} + A_3\bar{R}$ and $UCL_{\bar{X}} = \bar{\bar{X}} - A_3\bar{R}$
	- (see the [[control chart constants]] for where these values come from)
- in [[R]], we can use [[lolcat]]'s `spc.chart.variables.mean.and.meanstandarddeviation()`