tags:: stats, distribution
alias:: log-normal

- a distribution which, if you take its natural log, is [[normally distributed]].
	- can be useful for data which is positively skewed, but mesokurtic.
	- a log-normal distribution has only positive values. if your dataset has negative values, and you wish to apply a log transformation, you may need to add a constant before transforming! 2x the minimum value is a good default.
- in [[R]], we can simply take the `log()` of the data, and use `exp()` to transform it back!