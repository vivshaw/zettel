---
tags: stats
alias: sample
---

- a **sample** is a representative portion of a [[population (statistics)]], used to reach conclusions about that population.
- a good sample needs to be both:
	- **random**- every possible sample of size `n` has an equal chance of being selected
	- **representative**
- types of sampling:
	- non-random/non-probability/judgment: specimens are selected deliberately
	- random: all specimens have a probability of being in the sample
		- simple: each sample of size n has an equal chance of being selected
		- systematic: specimens are selected at some interval
			- in python, determine an interval, then use `.iloc[::interval]`
		- stratified: specimens are divided into homogenous strata, then random proportionate subsamples are taken from each stratum
			- in [[python]], you can use [[pandas]] `.sample()` on a `groupby` to do this. use `frac` to perform a proportional stratified sample, or `n` for an equal counts stratified sample
		- cluster: specimens are divided into groups that are homogenous between each other, but heterogenous within. then, we pick one or more random clusters.
- sampling can be done with or without replacement- returning the item to the population after the sample
- in [[R]], you can use the `sample()` function