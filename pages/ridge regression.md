tags:: stats, regression, regularization
alias:: Tikhonov regularization

- a form of regression that's useful when there is [[multicollinearity]] . it deals with it by regularizing with the [[L2 norm]]- all parameter estimates are limited to within the L2 norm.
- to minimize:
- construct a new function, and minimize it: $F(\beta_0, \beta1, \lambda) = \sum_{i=1}^n{(y_i - \sum_{j=1}^p{x_{ij} \Beta_j})^2} + \lambda(\sum_{j=1}^p{\beta_j^2})$
	- the first half is the [[SSE]], and is the same as [[ordinary least squares]]. we call the second half the **constraint**.
	- equivalently, we minimize $\underset{\beta}{\mathrm{argmin}}|| y - X B ||_2^2 + \lambda|| B ||_2^2$
	- we end up with a closed-form solution $\hat{\beta}_{Ridge} = (X^TX + \lambda \mathbf{I})^{-1}X^TY$
	- you can think of $\lambda$ as a penalty factor- the larger it is, the smaller $\beta$ must be. if lambda is 0, we just get OLS. $\operatornamewithlimits{argmin}_0$
- in [[R]], we can use the [[glmnet]] package to perform ridge regression. you might do that like so:
	- ```R
	  ridge_spec <- linear_reg(mixture = 0, penalty = 0) %>%
	    set_mode("regression") %>%
	    set_engine("glmnet")
	  ```
	- we can update the `penalty` at prediction time like:
		- ```R
		  predict(ridge.fit, new_data = Data, penalty = 500)
		  ```
	- or you might call the package raw, setting the `alpha` parameter to 0:
		- ```R
		  glmnet(as.matrix(data), labels, alpha = 0, family = "gaussian", lambda = 0.3) 
		  ```
	- we can also use `cv.glmnet()` to automatically do [[cross-validation]]