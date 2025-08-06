---
tags: graph, math, algorithms
---

- a maximal strongly connected component of a graph is a maximal subset where for every pair of vertices $u$ and $v$, both $u$ is reachable from $v$ and $v$ is reachable from $u$
- we can calculate this by first doing a DFS on the graph G noting the finish time of each node, then doing a DFS on its transform $G^T$ considering the elements in order of decreasing finish time. each tree in the depth-first forest will then be an SCC