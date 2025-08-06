---
tags: compsci, algorithms, sorting, math
---

- a sorting algorithm that uses a [[heap]].
	- we start by heapifying the array into a max-heap.
	- we then extract the maximum element and place it at the end of the array
	- then, bubble down to restore the heap
	- repeat until the array is sorted
- this can be done in-place with no extra space needed. simply decrease the heap size each time you extract an element
- [[time complexity]]: heapify is $\Theta(n)$, and bubble down is $n$ deletions each taking $\Theta(\log n)$ for the bubble down. so total complexity $\Theta(n \log n)$
- this combines some good aspects of other sorts. like [[mergesort]], it is $O(n \log n)$. like [[insertion sort]], it is in-place