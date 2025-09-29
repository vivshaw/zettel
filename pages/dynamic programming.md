---
tags: algorithms
---

- like [[divide-and-conquer]], solves problems by combining solutions to subproblems. but unlike D&C, the subproblems can overlap. in these situations, D&C would do too much "rework", but with dynamic programming, we can [[memoize]] to save time
	- most often, this applies to [[optimization]] problems
- what needs to be true for this to work?
	- **optimal substructure**: an optimal solution contains optimal solutions to subproblems
	- those subproblems must overlap