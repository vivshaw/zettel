---
tags: stats, data
---

- a distribution for [[continuous data]].
- good for representing physical processes that have a restraint, like the distance of a hole from a reference edge.
- generally, we only need the [[mean]] and the origin (minimum value) to work with this.
- when the minimum value is zero, the mean and the [[standard deviation]] are equal!
- in [[R]], we can use the `pexp` function. (this requires the *rate*, which is `1 / mu`.) for one with an origin that isn't 0, use `pexp.low` from [[lolcat]] instead.
- testing for exponentiality:
	- with n <= 100, use the [[Shapiro-Wilk test]]
	- with n > 100, use the [[Epps and Pulley test]]
	- in [[R]], test with [[lolcat]]'s `shapiro.wilk.exponentiality.test()` or `shapetest.exp.epps.pulley.1986()`.