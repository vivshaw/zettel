tags:: stats, statistical tests

- a [[two-sample test]] for [[variance]].
- assumptions:
	- we have [[independent samples]]
	- the populations are [[normally distributed]]
	- calculated as: $F_{(n_1-1, n_2-1, df)} = \dfrac{s^2_1}{s^2_2}$, which is a ratio of the variances
- in [[R]], we can use [[lolcat]]'s `variance.test.twosample.independent()`