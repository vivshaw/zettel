tags:: stats, data, distributions

- a dkistribution used for a discrete random variable with two outcomes
- based on the [[Bernoulli process]]
- the binomial formula: `P(r in n trials) = (n! / (r! * (n-r)!) * p^r * (1-p)^(n-r)`
- in [[R]], you can use `dbinom` to calculate one value, or `table.dist.binom` for a table. or, you can use `pbinom` to calculate upper or lower tail probabilities. (go down one count for upper tail!)