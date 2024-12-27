---
tags: stats
alias: KNN
---

- for optimal performance, it's important that the predictors be normalized, so they all have the same influence.
- can be used for either classification or regression:
	- classification:
		- given our data, for each point $X$, we choose the $K$ nearest points. the most common class among them is the value we assign to $X$
	- regression:
		- for each point $X$, we choose the $K$ nearest points. the average of their $Y$-values is the value we assign to $X$
- choosing $K$:
	- smaller $K$ leads to more [[variance]]
	- larger $K$ leads to more [[bias]]
- in [[R]], we can do KNN with [[class (R library)]]'s `knn()` function. it works in one step, like so: `knn.preds <- knn(train.X, test.X, train.Direction, k=3)`
	- ⚠️ you need to remove the target labels from the datasets!
	- or, with [[tidymodels]]' `nearest_neighbor()`