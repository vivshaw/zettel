---
tags: math, algorithms
---

- a method for solving [[recurrence]]s with this form: $T(n) = aT(n/b) + f(n)$ where $a > 0$ and $b > 1$
	- that is to say, for [[divide-and-conquer]] algorithms on a problem of size $n$, dividing it into $a$ subproblems, of size $n/b$
	- $f(n)$ is the **driving function**, covering the cost of dividing and combining the subproblems
- the method works by comparing the driving function to a **watershed function**, $n^{\operatorname{log_b} a}$
	- if there's a constant $\epsilon > 0$ such that $f(n) = \Theta(n^{\operatorname{log_b} a - \epsilon} )$, then $T(n) = \Theta(n^{\operatorname{log_b} a})$
		- said differently, "if the watershed function grows asymptotically faster". specifically, polynomially faster
	- if there's a constant $k \geq 0$ such that $f(n) = \Theta(n^{\operatorname{log_b} a} \lg^k n)$, then $T(n) = \Theta(n^{\operatorname{log_b} a} \lg^{k+1} n)$
		- said differently, "if they grow at about the same rate"
	- if there's a constant $\epsilon > 0$ such that $f(n) = \Omega(n^{\operatorname{log_b} a + \epsilon})$, **and** $f(n)$ satisfies the **regularity condition** $af(n/b) \leq cf(n)$ for some constant $c > 1$, then $T(n) = \Theta(f(n))$
		- said differently, "if the driving function grows asymptotically faster". specifically, polynomially faster
- you can't always apply this method! for example, there are gaps between each of the cases, in which one function is growing faster, but not _polynomially_ faster.