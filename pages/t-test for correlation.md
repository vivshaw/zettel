tags:: stats, [[relationship (stats)]]

- a [[one-sample test]] as to whether two random variables have a correlation significantly different from 0. uses the [[Pearson product-moment coefficient of correlation]], along with a [[t-test]].
	- if you need to test whether the correlation differs from a _non-zero_ value, use [[Fisher's z-test for correlation]]
	- ⚠️ the t-test has degrees of freedom $n - 2$, because there are _two_ variables!
- assumptions:
	- the pairs are independent
	- the populations are normally distributed
- this assesses _only_ a linear relationship!
- in [[R]], we can use [[lolcat]]'s `cor.pearson.r.onesample()`