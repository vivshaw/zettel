---
tags: data structures, heap, tree (DS)
---

- a treap is a randomized [[binary search tree]], where each node has both a **key** and a **priority**. the binary search tree property holds of the keys, and each node's priority is smaller than its children.
	- if the keys and priorities are distinct, then the structure is completely determined by these values!
- to insert an element, first use standard BST insertion, then rotate nodes up until the heap property is restored.
- to delete, rotate the node down until it is a leaf, then remove it.
- constructing a treap is equivalent to randomized [[quicksort]]