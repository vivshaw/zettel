---
tags: math, sorting, algorithms, compsci
---

- a sorting algorithm that works by iterating through the list, and inserting each element into its correct position in the sorted portion of the array.
	- one way to do this: move through the array right-to-left for each element you sort, check if it's in the correct position relative tot he element to the left. if it is, swap them, and continue left-to-right until it's in the correct position.
- best-case complexity is $O(n)$, worst-case is $O(n^2)$, average case is $O(n^2)$