---
tags: stats
alias: bootstrap (stats)
---

- **bootstrapping** is sampling from the data we observed, to estimate a distribution. we repeatedly sample the data we observed to construct a sampling distribution. usually, we sample with replacement.
	- for example, we might repeatedly sample our data, fit our model, and get our predictors. then, look at the sampling distribution of the mean of those predictors, and use it to estimate the true mean.
	- you can also think of kinda like the reverse of sampling from a population. with sampling, we go from the pop to a smaller sample we use as an estimate. with bootstrapping, we treat the pop _as_ a sample, to estimate a broader population
	- this tends to be better for estimating the population [[standard deviation]] than it is for the [[mean]]
- typically, we'd also provide confidence intervals for the predictors
- we can do this in [[R]] with the `boot` package:
	- ```R
	  # Here, we bootstrap an estimate of the median
	  bootstrap.median <- function(x, n){ median(x[i])}
	  boostrap <- boot(data, boot.median, R = 10000)
	  boot.ci(bootstrap, type = "perc")
	  ```