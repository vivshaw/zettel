---
tags: data structures, algorithms
---

- what is a heap?
	- an array of numbers, called the keys
		- with some special properties
	- often some other data, the payload
- what can we do to a heap?
	- **heapify** - given an ordinary array, turn it into a heap
	- **insert**
	- **delete**
	- **minimum-element** - find the smallest key in the heap
- there are both min-heaps and max-heaps
	- min-heap property: every node with children is smaller than its children
- each element $i$ may have a left child $2i$ and a right child $2i + 1$
	- in this way, it's also a [[binary tree]]!