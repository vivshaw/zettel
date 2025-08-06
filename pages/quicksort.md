---
tags: algorithms, sorting
---

- a [[divide-and-conquer]] sorting algorithm. developed by [[Hoare]]. good for sorting in place!
- steps of the algorithm:
	- **divide.** we partition the array- we create a point for which everything to the left is $\leq$ to the pivot, and everything to the right is $\geq$
		- how can we do this? one way is **Lomuto partitioning** to choose the last element as the pivot, then iterate through the array and build up a "low" and "high" half. whenever an element is higher than the pivot, leave it where it is. it's in the high half. whenever an element is lower than the pivot, swap it with the first element of the high half. it's now the last element of the low half. once you've reached the end, swap the pivot with the first element of the high half. now the pivot is in its final place!
		- another alternative is **Hoare partitioning**. here, we choose the first element as pivot, then start with an index on each end. we iterate inward until we find an inversion, swap those indices, then repeat until partitioned.
		- this step has runtime $O(n)$
	- **conquer.** we recursively quicksort the left and right halves.
	  id:: 68543d31-1701-4a34-9761-e3e89dcc3384
	- **combined** except, no need to combine once we're done- all sorting happens in-place!
- we can improve performance by randomizing. a simple way to do that would be to pick a _random_ element as the pivot, instead of the last one, then swap that element with the last one.
- you can also improve performance by picking better pivots. one way might be to pick _three_ random pivots, then choose the median among them.
- [[time complexity]]:
	- worst case is $\Theta(n^2)$, which occurs if the partitioning always chooses the lowest or highest element, so the recursive call never splits up the array
	- best case is $\Theta(n \log n)$, if we always choose the median element, so each half of the partition is almost balanced in size
	- average case is in fact still $\Theta(n \log n)$! for randomly distributed data, we'll likely get a mix of good and bad partitions, but it averages out to only a constant factor worse than the best case.
- advantages of quicksort:
	- memory-efficient due to in-place sorting
	- good cache locality
	- easy to randomize