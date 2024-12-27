---
tags: stats, Bayes, classification
---

- a classifier that uses [[Bayes' theorem]]. it assigns the class prediction to the class with the highest conditional probability, like so:
	- $p_k(x) = \dfrac{\pi_k \cdot f_k(x)}{\sum_{l=1}^k{\pi_l \cdot f_l(x)}}$
		- where $\pi_k$ is the [[prior]] estimate that the item belongs to class $k$, and $f_k(x)$ is the [[density function]] for class $k$, or likelihood
	- stated differently, $C^\text{Bayes}(x) = \underset{r \in \{1,2,\dots, K\}}{\operatorname{argmax}} \operatorname{P}(Y=r \mid X=x)$
- this classifier has the lowest theoretical misclassification rate.
- but to use this in practice, we need to know $f_k(x)$! in reality, we usually don't.
	- so, the Bayes classifier becomes the seed for a whole class of [[generative model]]s that plug in different functions for $f_k(x)$. [[linear discriminant analysis]], [[quadratic discriminant analysis]], and [[Naive Bayes]] all do this! (with different assumptions.)