tags:: stats, data, machine learning

- a binary tree of decision nodes that recursively splits a data set until it's left with leaf nodes of only a single class.
- useful for classification in cases that are not linearly separable
- a common technique to improve the accuracy and reduce variance is [[bagging]]
- in [[R]], we can use the `rpart` library:
	- ```R
	  tree <- rpart(Label ~ ., data)
	  ```
	- or, the `tree` library, which provides options like `cv.tree()` with built-in [[cross-validation]]