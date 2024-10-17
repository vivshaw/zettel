tags:: stats, classification
alias:: LDA

- a [[generative model]] that tries to find some linear combination of features to separate the problem space into classes. a special case of the [[Bayes classifier]].
	- it can also be used for dimensionality reduction
- for $K$ classes, assume:
	- $f_k(x)$ is [[normal]]
	- all variances $\sigma_1 ... \sigma_k$ are equal
- then, for a single predictor:
	- $f_k(x) = \dfrac{1}{\sqrt{2\pi} \cdot \sigma_k} - exp(-\dfrac{1}{2\sigma_k^2} \cdot (x-\mu_k)^2)$
	- $P_k(x) = \dfrac{\pi_k \cdot \dfrac{1}{\sqrt{2\pi} \cdot \sigma} - exp(-\dfrac{1}{2\sigma^2} \cdot (x-\mu_k)^2)}{\sum^K_{l=1}{\pi_l \cdot \dfrac{1}{\sqrt{2\pi} \cdot \sigma} - exp(-\dfrac{1}{2\sigma^2} \cdot (x-\mu_l)^2)}}$
	- what we want to maximize, reachable by taking the log of the top chunk then doing some algebra:
		- $\delta_k(X) = x \cdot \dfrac{\mu_k}{\sigma^2} - \dfrac{\mu_k^2}{2\sigma^2} + log(\pi_k)$
		- we can plug in some data-driven estimates, using the same fundamental [[statistics]] we'd use anywhere else:
			- $\hat{\mu}_k = \dfrac{1}{n_k} \cdot \sum_{i:y_i = k}{X_i}$ - this is just the sample [[mean]] for the class $\bar{x}$, calculated as normal!
			- $\hat{\sigma}^2 = \dfrac{1}{n - K} \cdot \sum^K_{k=1} \sum_{i:y_i=k}{(X_i - \hat{\mu}_k)}$ - again, this is the sample [[variance]] $s^2$
			- $\hat{\pi}_k = \dfrac{n_k}{n}$ - this is just a [[proportion]]
- extended to multiple predictors $p$, we can translate the same functions to work with vectors and matrices:
	- $X = (x_1, ..., x_p)$
	- $X \sim N(\mu, \Sigma)$ (X is a multivariate [[normal]])
		- the vector length of $\mu$ is $p$, and $\Sigma$ is the [[covariance]] of X, a $p \times p$ matrix (which is basically our $\sigma$ from the univariate case)
	- now we'll work vectorized:
		- $f(x) = \dfrac{1}{(2\pi)^{P/2} \cdot |\Sigma|^{1/2}} - exp(-\dfrac{1}{2} \cdot (X-\mu)^T \cdot \Sigma^{-1} \cdot (X-\mu))$
		- $\delta_k(x) = X^T \cdot \Sigma^{-1} \cdot \mu_k -\dfrac{1}{2} \cdot \mu_k^T \cdot \Sigma^{-1} \cdot \mu_k + log(\Pi_k)$
- in [[R]], we can do this with `lda()` from the [[MASS]] package, then `predict()` to make predictions
	- or, we can use [[tidymodels]]' `discrim_linear()` with MASS as an engine