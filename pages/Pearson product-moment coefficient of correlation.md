tags:: stats, [[relationship (stats)]]

- a measure of [[correlation]] invented by [[Karl Pearson]]. used with continuous random variables, and linear relations.
- calculated as:
	- for a population, $\rho_{X,Y}= \frac{\operatorname{cov}(X,Y)}{\sigma_X \sigma_Y}$
		- where $\operatorname{cov}$ is the [[covariance]]
	- for a sample, $r_{xy} =\frac{\sum ^n _{i=1}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum ^n _{i=1}(x_i - \bar{x})^2} \sqrt{\sum ^n _{i=1}(y_i - \bar{y})^2}}$
- in [[R]], this can be calculated with `cor()`