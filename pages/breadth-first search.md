---
tags: math, graphs, algorithms
---

- steps:
	- create a queue to store nodes
	- add the starting node to the queue
	- create a set to track visited nodes
	- while there are nodes in the queue:
		- dequeue the next node
		- for each adjacent node to the dequeued node, if it's not in the set of visited nodes, add it to both the queue and the visited set
- this can be transformed to find the shortest path with only a small change:
	- create a dictionary to track each node's parent. store those parents when we visit
	- if the dequeued node is the target node, recursively return its parents
	- **this only works on graphs with unweighted edges**. for weighted edges, you need something like [[Dijkstra's algorithm]]