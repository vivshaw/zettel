---
tags: stats, [[relationship (stats)]]
---

- a measure of [[correlation]] for use with ordinal data. we use it by converting scores to ranks (giving ties the average rank), then calculating the [[Pearson product-moment coefficient of correlation]] on the ranks.
- in [[R]], we can use `cor()` just as we would for other correlations, but we specify `method = "spearman"`. we can use [[lolcat]]'s `cor.spearman.rank()` to test if the result is different from 0.
	- we can calculate ranks with R's built-in `rank()`!