---
tags: stats
---

- a measure of how much the variance increases from adding a predictor into a larger model. commonly used to assess [[multicollinearity]].
- $VIF(\hat{\beta_i}) = \dfrac{Var(\hat{\beta_i})\ full\ model}{Var(\hat{\beta_i})\ simple\ model}$
- or, $VIF(\hat{\beta_i}) = \dfrac{1}{1 - R^2_{X_i/X_{-i}}}$
	- where $R^2_{X_i/X_{-i}}$ is the [[coefficient of determination]] from regressing $x_i$ against all the other predictors.
- VIF is ideally 1, which is what you'll get if there's no collinearity at all.
	- if VIF is large, it implies that predictor is collinear with one or more of the others