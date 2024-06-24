tags:: stats, statistical tests
alias:: ADM(n-1) procedure

- a test for [[dispersion]] that can be used when the data is non-normal. it uses the [[median absolute deviation]], and a [[t-test]] for two samples or [[ANOVA]] for more.
	- it's can be used in an `n-1` flavor, in which we drop the median value itself. it provides no additional information about the dispersion, since its dispersion is 0 (if an odd number of observations) or equal to the other co-median value (if even).
- to do this in [[R]] for two samples:
	- classify the grouping variable as a factor
	- calculate the [[median absolute deviation]]
	- then, use `t.test.twosample.independent.fx()`