---
tags: stats, data, distributions
---

- a discrete distribution for [[ordinal data]] or [[absolute data]] . for example, the number of occurrences of an event within some interval, or the number of defects per item.
- calculated as: `P(X) = (lambda^X / X!) * e^-lambda`
	- where `lambda` is the mean number of occurrences per unit
- in
	- [[R]], can use `dpois()` for exact probabilities, [[lolcat]]'s `table.dist.poisson()` for a table, or `ppois()` for tails. (decrease the count by one for upper tail!). we can test if a distribution is Poisson using [[lolcat]]'s `poisson.dist.test()`. we can generate random Poisson data with `rpois()`.
- you can find the area between two possibilities by subtracting tail probabilities.