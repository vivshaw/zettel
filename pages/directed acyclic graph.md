---
tags: graph, math, data structures
alias: DAG
---

- we can do a **topological sort** on a DAG, which means, put the nodes in a linear order where for every edge $(u,v)$, $u$ comes before $v$
	- we can use a [[depth-first search]] to do this. simply add each node to the front of a linked list as it is finished.