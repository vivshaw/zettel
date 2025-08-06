---
tags: math, graph, algorithms
---

- an algorithm for finding [[minimum spanning tree]]s.
- start by creating $v$ trees, one for each vertex in $G$
- then iterate over the edges, in increasing order of weight
	- for the edge $u, v$, if $u$ and $v$ are in the same tree, we can't add it cause we'd make a cycle
	- otherwise, add it and merge the trees