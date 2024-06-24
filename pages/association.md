tags:: stats, data, [[relationship (stats)]]

- a measure of [[relationship (stats)]] between two variables, used when both variables are nominal.
- we might use these variations on the [[chi-square distribution]] to calculate it:
	- [[Pearson's phi]] when we have a 2x2 grid
	- [[Pearson's C]] when we have a square matrix larger than 2x2
	- [[Cramer's V]] when we have a rectangular matrix
- in [[R]], we'll want to get our data into a [[contingency table]] format rather than [[frequency format]] or [[individual format]].