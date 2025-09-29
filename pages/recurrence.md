---
tags: math, algorithms
---

- a **recurrence** is an equation that describes a function, using that function.
	- a recurrence contains several cases. a **recursive** case calls the function again. a **base** case doesn't.
- a recurrence is **algorithmic** if, over some threshold:
	- for all $n < N_0$, $T(n) = \Theta(1)$
	- for all $n >= N_0$, every recursion eventually terminates in a base case