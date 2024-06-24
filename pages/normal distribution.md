tags:: stats, data, distributions
alias:: normal, normally distributed, normality

- a distribution for [[continuous data]], and one of the most common
- characteristics:
	- all measures of central tendency are equal ([[mean]], [[median]], and [[mode]])
	- skewness and kurtosis are 0
	- the tails extend to infinity, but never hit 0
- you can determine how far any given value is from the mean using a [[z-score]]
- we can test for normality:
	- when n < 25, we can use the [[Anderson-Darling test]] or [[Shapiro-Wilk test]]
	- when n >= 25, we can use the [[moment tests]]
- in [[R]], you can use `pnorm` to get the tail probability.