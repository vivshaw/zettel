---
tags: algorthms, robotics, path planning
alias: rapidly-expanding random tree
---

- a probabilistic algorithm that constructs a tree of random configurations to find paths from a start to a target configuration.
- the result of the RRT algorithm is a graph. you'll still need a [[path planning]] graph algorithm like [[Dijkstra's algorithm]] if what you want is the shortest path
- steps:
	- in a configuration space $C$,
	- create a graph $G$ with only the starting node
	- initialize a counter $k$
	- choose a maximum depth $K$
	- choose an incremental distance $\Delta q$
	- while the current node is not the target configuration, and $k$ is less than $K$:
		- choose a new random configuration $q_{rand}$
		- pick the nearest vertex in $G$ to $q_{rand}$, call it $q_{near}$
		- compute a new configuration $q_{new}$ by moving $\Delta q$ from $q_{near}$ toward $q_{rand}$
		- choose whichever is closer of $q_{rand}$ and $q_{new}$. if the edge between it and $q_{near}$ is collision-free, add it to $G$
- to make it more likely to reach the goal quickly, you can sample the goal as $q_{rand}$ some % of the time.