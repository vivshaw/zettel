---
tags: algorithms
---

- an algorithm that at each step, makes the choice that seems best at that time. this isn't always the most efficient strategy! but for some problems, it is.
	- to contrast with [[dynamic programming]], dynamic solutions can go bottom-up and depend on results from subproblems, but greedy algorithms must be top-down and depend only on past state
- when's it the right choice?
	- the **greedy-choice** property: you can assemble a globally optimal solution, out of locally greedy choices
	- **optimal substructure**:  an optimal solution contains inside optimal solutions to subproblems. (also needed for [[dynamic programming]])
- applications:
	- [[Huffman codes]]