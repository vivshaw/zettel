tags:: stats

- [[ordinary least squares]] assumes that the errors of the model are independent and identically distributed. what can we do if they aren't? for example, what if the data is [[heteroscedastic]]?
- **generalized least squares** instead assumes the error terms have a non-diagonal covariance matrix $\Omega$.
	- we factor in the covariance by multiplying the dependent and independent variables by a "whitening matrix" - the inverse of the square root of $\Omega$
		- in [[R]], we can do this like:
			- ```R
			  P <- chol(Sigma)  # square root of the covariance matrix, aka Cholesky decomposition
			  P_inv <- solve(t(P))
			  
			  PX <- P_inv %*% X
			  Py <- P_inv %*% y 
			  
			  lm(Py ~ PX -1)
			  ```
			- or, use the `gls()` function from the [[nlme]] package
				- ```R
				  glmod <- gls(y ~ x.1 + x.2, correlation = corAR1(form = ~ time), data = data)
				  ```
	- then we do good ol' OLS on the transformed model, then we reverse the transformation
	- in practice, we won't know $\Omega$, we'll have to estimate it from the data
- Medium article: https://towardsdatascience.com/generalized-least-squares-gls-mathematical-derivations-intuition-2b7466832c2c