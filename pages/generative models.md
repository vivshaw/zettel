---
tags: stats
alias: generative model
---

- [[classification]] models in which, rather than estimating the probability $P(Y=K | X = x)$, we instead estimate $P(X = x | Y = K)$, then flip the model with [[Bayes' theorem]].
	- said differently, models on the [[joint probability distribution]] of the predictor X and target Y.
	- said differently again, models that try to estimate how the data was generated.
	- contrast with [[discriminative models]]
- for the $k$th class, $f_k(x) = P(X | Y = k)$
- then, $P(X = x | Y = K) = \dfrac{\pi_k f_k(x)}{\sum^K_{l=1}{\pi_l f_l(x)}}$ (our [[posterior]]), for each of the $K$ classes, and we pick the largest. hey look- that's [[Bayes classifier]]!
	- ($\pi_k$ being our [[prior]]- our estimate of the probability that a random observation belongs to class $k$)
- examples:
	- [[Naive Bayes]]
	- [[linear discriminant analysis]]
	- [[quadratic discriminant analysis]]