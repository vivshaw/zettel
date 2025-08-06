---
tags: compsci, math, graph
---

- an algorithm to find the shortest path through a weighted graph.
- steps:
	- consider the starting node at distance 0, and all other nodes at distance infinity
	- create a heap sorted by distance to track univisited node. add the starting node to it
	- create a set to store visited nodes
	- create a dictionary to store parents of nodes
	- while there are unvisited nodes:
		- pop the top one off the heap, store it in the visited set
		- for each neighbor, if it isn't in the visited set, update the distance, note the parent in the parent dictionary, and push it onto the heap
		- repeat until you reach the target