---
tags: stats
alias: PCA
---

- a method of [[dimensionality (data)]] reduction, visualizing [[high dimensional]] data, or feature extraction
- imagine your data $X$ is an $n \times m$ matrix- n samples of m measurements.
	- we'll take an [[eigendecomposition]] of our [[covariance]] matrix, $X^TX$, which is $m \times m$, into a set of eigenvectors $W$ ($m \times m$) and eigenvalues $\lambda$
	- the columns of $W$ are called the **loadings**. they are ordered by the amount of [[variance]] in our data they explain
	- we can calculate $T = XW$, getting another $n \times m$ matrix, that we call our **scores**. but this didn't actually shrink our data at all! it just transformed how we view it.
	- how we *shrink* it is, we'll pick the first $r$ columns of $W$. since $W$ is ordered, we just can just take what we want and truncate the rest. Then, $T = XW_r$, an $n \times r$ matrix
- we can also think of it in terms of [[singular value decomposition]]
	- $X = U \Sigma V^*$, where $U$ is an $m \times m$ unitary matrix, $\Sigma$ is an $m \times n$ diagonal matrix, $V$ is an $n \times n$ unitary matrix, and $V^*$ is the  conjugate transpose of $V$
	- the diagonal values of $\Sigma$ are the square roots of the eigenvalues of $X^*X$. this isn't the same as the eigendecomposition, but it's similar.
	- here we say our scores $T = XV$, equivalently $T = U \Sigma V^*V$. since $V^*V$ is an [[identity matrix]], that's the same as $T = U \Sigma$
	- then, we truncate to $Tr$ by taking the first $r$ columns of $U$, and the first $r \times r$ square block from $\Sigma$
	- unlike eigendecomposition, we can use this approach when the data we're operating on isn't square.
- the components we get will be:
	- linear combinations of the original features
	- uncorrelated with each other
	- orthogonal axes
- we can pick $r$ with a [[scree plot]]
- before doing PCA, we should ensure our data is normalized to have zero mean and unit variance
- this is in some ways similar to [[compression]]!