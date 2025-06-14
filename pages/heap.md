---
tags: data structures, algorithms
---

- a **heap** is a special type of [[binary tree]], stored in an array. each node has a number, called the key. and potentially some other data, called the payload.
	- each node $i$ might have:
		- a left child $2i$
		- a right child $2i + 1$
		- a parent at $\lfloor{i / 2}\rfloor$
	- the tree must follow one of these special properties
		- min-heap property: every node with children is $\leq$ than its children
		- max-heap property: every note with children is $\geq$ than its children
- what primitives do we need to have in place to implement a heap?
	- **bubble up**: use this to restore heap correctness when one key is smaller than its parent. if the element's smaller than its parent, swap them, then call bubble-up recursively on the parent. if we've reached element 1, break early.
		- time complexity is $\Theta(log\ n)$
	- **bubble down**: use this to restore heap correctness when one key is larger than its parent. if the node is larger than its parent, swap it with its smallest child, then recursively call bubble-down on the child
		- [[time complexity]] is $\Theta(log\ n)$
- operations:
	- **insert**: to insert an element, we append it ($\Theta(1)$), then bubble up ($\Theta(log\ n)$).
	- **delete**: to delete an element $j$, swap the last element into $j$'s position, then adjust the range to n-1, then fix what's broken. if the element in the $j$th position is larger than its parent, bubble up. otherwise, bubble down.
	- **finding the minimum/maximum element**: return the first element. if min heap, that's the smallest. if a max heap, that gets us the largest. there's no shortcut to find the other.
	- **heapify** - given an ordinary array, turn it into a heap
		- from the midpoint of the array down to 1, recursively do bubble down. time complexity is $\Theta(n)$