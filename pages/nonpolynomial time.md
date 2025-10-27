---
tags: math, algorithms, [[computational complexity]] 
alias: NP, NP-complete
---

- a class of problems that _cannot_ be decided in [[polynomial time]]
- there are two subclasses to think of here:
	- **NP** problems can't be _solved_ in P, but _can_ be verified in P time. so if someone else handed you a solution, you could prove it was right.
	- **NP complete** (or **NPC**) can't be solved _or_ verified in P time
- formally, NP is about _decision_ problems. but you can often reduce an optimization to a related decision problem. so if we can prove a known NP problem reduces to our problem, we know our problem is also NP
- there are some odd pairs of problems that seem very similar, but one's polynomial and the other's NP:
	- shortest (P) vs. longest path (NP)
	- Euler tour (cycle that covers each edge, P) vs. Hamiltonian cycle (cycle that covers each vertex. NP)
	- 2-CNF (P) vs 3-CNF (NP)