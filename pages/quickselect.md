---
tags: algorithms
---

- problem: given an a array, find the $K$th smallest element. can we do it faster than sorting the array and choosing the $K$th element? we can, using a technique similar to [[quicksort]]!
- start by choosing a random element $j$ and partition.
	- if $j$ is the $k$th element, we found it! return it.
	- otherwise, determine whether $j$ is less than or greater than $k$, and recur only on the appropriate partition.
	- not every partition will be helpful. only ones in the middle values will. this has probability $1/2$
- even though the worst case is still $\Theta(n^2)$, the expected time complexity is actually $\Theta(n)$!