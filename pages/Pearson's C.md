tags:: stats, [[relationship (stats)]]

- a measure of [[association]] for square nominal data, larger than 2x2. it's based on the [[chi-square distribution]].
	- calculated as $\phi = \sqrt{\dfrac{\chi^2}{\chi^2 + n}}$
- in [[R]], we can use `cor.pearson.c()` on [[cross-tabulated]] data