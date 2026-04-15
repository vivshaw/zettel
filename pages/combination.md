---
tags: math
---

- an unordered subset of $k$ objects taken from a set of $n$ objects
- aka **bionomial coefficient**
- contrast with [[permutation]]
- notated $C_{k,n}$ or $\binom{n}{k}$, calculated as $\dfrac{n!}{k! (n-k)!}$
	- $\binom{n}{k} = \binom{n}{n - k}$
- we can compare likelihood like so. suppose you've a group of 10 fruits, 4 oranges and 6 apples. you want to choose 3 fruits. what's the chance that at least 1 apple and 1 orange are chosen? that's $P(1A \& 2O) + P(2A \& 1O)$, which is $\dfrac{\binom{6}{1}\binom{4}{2}}{\binom{10}{3}} + \dfrac{\binom{6}{2}\binom{4}{1}}{\binom{10}{3}}$
- useful for the [[binomial distribution]]!