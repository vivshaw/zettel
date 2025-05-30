---
tags: robotics, engineering
---

- a naive method to map a space would be to use a grid. divide the spaces into discrete cells, and mark each cell occupied that you detect a point in.
	- but this is memory-intensive, and slow to access. an $n \times n$  grid containing $m$ points requires $n^2$ bytes to store, and $n^2$ operations to access all occupied grid squares (need to check every square)
	- but it's quick to check a single point- O(1)
	- if we are mapping using data from a beam sensor, like a [[LIDAR]], we not only have data about which cells are occupied, but about which cell _aren't_ occupied (any of those that would have interrupted the beam). we can use something like [[Bresenham's line algorithm]] to select all the cells on a line between our sensor and the detected point.
- a more advanced method would be a **point-region quadtree**. this partitions a 2D space into regions by recursively dividing it into equal quadrants until each quadrant contains at most one point.
	- for example, in #python: https://scipython.com/blog/quadtrees-2-implementation-in-python/
	- an $n \times n$ quadtree containing $m$ points requires ~$m$ bytes to store, and $m$ operations to access all occupied grid squares
	- but it requires up to the depth of the tree to check a specific point
- we might also wish to construct a **topological map**, one that represents the space in a graph structure.
	- this might be useful, for example, if we want to do [[trajectory following]]
- it is possible to convert from a grid to a graph! treat each unoccupied cell as a node, and its 4-neighborhood (or 8-neighborhood if you want diagonals) as its graph connections.
	- the New York subway map is a great example of a topological map
	- it's not guaranteed that you can do the reverse, though! consider a subway map where certain trains skip past certain stations.
- we might choose to map probabilistically. this reduces the chances of seeing a phantom obstacle where one doesn't exist due to noise or other flukes. for example, we might choose to increment the probability of an obstacle in a grid cell by 1% for each hit.
- how can we navigate this map, though? we can use **configuration space**:
	- for a circular robot, we can grow each obstacle by the radius of the robot, then shrink the robot's representation to a single point.
	- for a rectangular robot, we can [[convolve]] with a rectangular [[kernel]].