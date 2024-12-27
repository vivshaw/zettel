tags:: stats, regression, non-parametric regression

- a class of techniques for non-parametric estimation of functions
	- the [[kernel]] must satisfy $\int^{\infty}_{-\infty} k(x)dx = 1$
	- the bandwidth $h$ represents the influence of external points, relative to the middle of the kernel
	- we weight points based on their distance. we'll place the kernel at each data point $X_i$, and slide it along. then we'll measure the estimated $y$ for each value, to the kernel's result for each value
	- you can use many types of kernel- [[uniform]], [[Gaussian]], etc.