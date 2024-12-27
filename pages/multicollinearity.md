---
tags: stats
---

- multicollinearity is when predictors in a regression model are correlated. it generally reduces the quality of a model, leading to high p-values and large standard error
- we can assess multicollinearity using a [[variable inflation factor]]
- however, it is wrong to exclude variables based on collinearity! dropping variables post-hoc to improve the model fit is [[p-hacking]]! you should decide what to include and exclude in advance based on what parameters are sensible.