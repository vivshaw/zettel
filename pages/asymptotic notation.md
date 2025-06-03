---
tags: math, compsci
alias: big-O notation
---

- a notation that describes the growth rate of a function as its input asymptotically tends to infinity. it can also be used to measure the [[computational complexity]] of an algorithm.
	- $O$ is an *upper bound*. "the function grows no faster than this".
		- formally, $f(n) \in O(g(n)$ means there exists a constant $k > 0$ and a constant $a$ such that the inequality $0 <= f(x) <= k g(x)$ holds for all $x > a$.
		- $o$ is this, except not asymptotically tight. that means it's a stronger bound! like "grows strictly slower than this" or, $O : o ::\ \leq\ :\ =$
			- formally, for _every_ constant $k > 0$ there's a constant $a$ such that the inequality $0 <= f(x) <= k g(x)$ holds for all $x > a$.
	- $\Omega$ is a *lower bound*. "the function grows at least this fast"
		- $\omega$ is this, except not asymptotically tight. like "grows strictly faster than this"
	- $\Theta$ is a *tight bound*. "the function grows exactly this fast"
		- this implies both $O$ and $\Omega$
	- sometimes we might assess these complexities separately for a best-case or worst-case input
- with this notation, we ignore constant factors, and we ignore lower-order terms. so, for example, $O(3n^2 + n)$ becomes $O(n^2)$
	- logs of different bases are also equivalent up to a common factor
- effectively, we are comparing more complex functions to simpler ones we know well, to get a better sense of how they grow