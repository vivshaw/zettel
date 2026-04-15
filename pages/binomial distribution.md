---
tags: stats, math, distributions
---

- a distribution used for a [[discrete]] [[random variable]] with two outcomes
	- based on a repeated [[Bernoulli process]]. you can think of the [[Bernoulli distribution]] as a binomial with only one trial
	- said differently: "we perform n independent trials, each with only two outcomes (usually we think of these two outcomes as success or failure) and with a probability of success p that stays constant from trial to trial." ([source](https://bookdown.org/probability/beta/conditional-probability.html#conditional-probability-1))
- we notate that a variable has this distribution with: $X \sim Bin(n,p)$
	- two parameters, $n$ number of trials, and $p$ probability of success
- formulas:
	- the [[expectation]] is: $E(X) = np$
	- the [[variance]] is: $Var(X) = np(1-p)$
	- the [[support]] is the integers $0 ... n$ inclusive
	- $P(X=k) = \binom{n}{k} p^k (1−p)^{n−k}$ is the [[probability mass function]] (chance of $k$ in $n$ trials)
	- $P(X≥k) = \sum^n_{i=k}​\binom{n}{i} p^i (1−p)^{n−i}$ is the [[CDF]] (chance of $k$ or more in $n$ trials)
	- uses [[combination]]!
- in [[R]], you can use `dbinom` to calculate one value, or `table.dist.binom` for a table. or, you can use `pbinom` to calculate upper or lower tail probabilities. (go down one count for upper tail!)
	- ```R
	  #generate 5 random draws from X, where X ~ Bin(30, 1/4)
	  rbinom(5, 30, 1/4)
	  
	  # PMF, find P(X = 3), where X ~ Bin(10, 1/2)
	  dbinom(3, 10, 1/2)
	  
	  # CDF, find P(X <= 6), where X ~ Bin(15, 1/3)
	  pbinom(6, 15, 1/3)
	  
	  #find the value of x such that P(X <= x) = .9, where X ~ Bin(50, 1/5)
	  qbinom(.9, 50, 1/5)
	  ```