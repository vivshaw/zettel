---
tags: stats, classification
---

- a [[generative model]] that further relaxes the assumptions made by [[linear discriminant analysis]] and [[quadratic discriminant analysis]]. a special case of the [[Bayes classifier]].
	- Naive Bayes assumes _nothing_ about the distribution, while both of those assume $f_k(x)$ is normal.
	- we _do_ assume that all the predictors are completely [[independent]]
- we get:
	- $f_k(x) = f_{k_1} (x_1) \cdot f_{k_2} (x_2) \cdot ... \cdot f_{k_p} (x_p)$
	- $P_k(x) = \dfrac{\pi_k \cdot f_{k_1} (x_1) \cdot ... \cdot f_{k_p} (x_p)}{\sum_{l=1}^K{\pi_l \cdot f_{l_1} (x_1) \cdot ... \cdot f_{l_p} (x_p)}}$
- in [[R]], we can do this with [[e1071]]'s `naiveBayes()` function
	- we can use `type = raw` if we want the raw probabilities, rather than the class prediction
	- or, we can use [[tidymodels]]' `naive_Bayes()` with the `klaR` engine