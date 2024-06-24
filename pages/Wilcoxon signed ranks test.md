tags:: stats, [[statistical tests]]

	- a test for use with ordinal data. it works by ranking the scores in their absolute magnitude, then applying a sign based on whether they're above or below the hypothesized median. we then compare the sum of the positive ranks to the sum of the negative ranks.
	- assumptions:
		- the specimens are independent
		- the measurement scale is at least ordinal, and the underlying property is continuous
		- the probability of values falling on the median is low
		- the distributions is symmetrical around the median
- in [[R]], we can use [[lolcat]]'s `median.test.onesample.wilcoxon()`