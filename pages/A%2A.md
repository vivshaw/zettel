---
tags: path planning, compsci
---

- a variation on [[Dijkstra's algorithm]] to increase its efficiency on large graphs. Dijkstra's needs to traverse the whole graph. A* adds a heuristic to instead guess the most likely paths, and try those first
- effectively, the only difference is:
	- we choose some heuristic to apply to each node
	- when we put that node in the priority queue, we calculate the priority as the distance _plus_ the heuristic