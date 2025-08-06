---
tags: stats, math
---

- a set of [[distributions]] with a particular form, that happens to makes them useful in statistics
- $y$ is a random variable from the exponential family if:
	- $f(y, \theta, \phi) = \exp{\dfrac{y \cdot \theta - b(\theta)}{a(\phi)}} + c(y, \phi)$
		- $\theta$ is called the *canonical parameter*
		- $\phi$ is called the *dispersion parameter*
- members of this family include:
	- the [[Gaussian]]
	- the [[binomial distribution]] and [[Bernoulli distribution]]
	- the [[Poisson distribution]]
	- the [[exponential distribution]]
- for the Gaussian:
	- $\theta = \mu$ and $b(\theta) = \dfrac{\theta^2}{2}$
	- $\phi = \sigma$ and $a(\phi) = \sigma^2$
	- $c(y, \phi) = - \dfrac{y^2}{2 \cdot \sigma^2} - \log \sigma - \log \sqrt{2 \cdot \pi}$