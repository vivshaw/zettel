---
tags: stats, math
alias: density function, PDF (stats)
---

- the function for a [[continuous]] [[random variable]] that, for any value in the [[sample space]], gives you the relative likelihood that a random sample is equal to that value... _kinda_
	- except... it doesn't really return a probability, it returns a **density**, because continuous values can be infinitely subdivided. so really it tells you something more like "how likely is the value to be *close* to x". you can compare relative densities, but they don't tell you much in absolute likelihood
	- so, perhaps a more accurate way: "the thing you integrate to get the [[CDF]]"
	- for example, for the [[normal distribution]], this is the famous bell curve
- a valid PDF:
	- is positive,
	- when integrated over the support of the random variable, sums to 1