---
tags: math, algorithms, compsci, sorting
---

- an example of a [[divide-and-conquer]] algorithm
- effectively, we take our array, and recursively divide it in half until all subarrays have only one or two elements. we then sort those directly if needed. then, we recursively merge the sorted subarrays back together.
	- we can do the merge efficiently by creating a `temp` array, then using two pointers `i` and `j` to iterate over both subarrays simultaneously, copying in the smallest element. then we can copy `temp` back into that space in the array
- has a [[time complexity]] of $\Theta(n \log n)$