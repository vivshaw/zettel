---
tags: math, data structure
---

- one way to represent a graph is with **adjacency lists**: for each node, there's a list containing the other vertices it connects to.
	- this tends to be better for sparse graphs, and uses less memory
	- finding each edge takes $\Theta(V + E)$ time
- another way is an **adjacency matrix**: each node is a row and column in a matrix, and the values indicate whether there is an edge from the row to the column
	- this tends to be better for dense graphs, and when you need to identify if two nodes have an edge as rapidly as possible, but uses more memory
	-