---
tags: math
alias: L1 norm, L2 norm, Euclidean norm
---

- a **vector norm** is a function on a vector space to the non-negative reals, that behaves in particular ways like the [[distance]] from the origin.
- some common norms:
	- **L0 "norm":** $||x||_0 = \sum_{r=1}^n{|x_r|^0}$ where $0^0 = 0$ - the number of non-zero entries in the vector
		- ⚠️ not a real norm!
	- **L1 norm:** $||x||_1 = \sum_{r=1}^n{|x_r|}$ - the sum of the absolute values of the vector
		- also known as the Taxicab norm, and the derived distance is the [[Manhattan distance]]
	- **L2 norm:** $||x||_2 = \sqrt{\sum_{r=1}^n{|x_r|^2}}$ - the square root of the sum of the squares of the values
		- often (but not exclusively) called the Euclidean norm, and the derived distance is the Euclidean distance
	- **L-infinity norm:** $||x||_{infty}=max_i|x_r|$ - the value of the largest element in the vector