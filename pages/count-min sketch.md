---
tags: data structures, algorithms
---

- a probabilistic data structure for counting the frequency of events in streamed data. similar to a [[Bloom filter]].
- we create a 2-dimensional array of $n$ counters with $m$ slots each.
	- to count a word, hash it for each counter, then add 1 to the appropriate slot for each counter.
	- to retrieve the approximate count, hash it for each counter, then take the minimum of that slot across each counter.
		- you may wish to consider if the returned value is below the acceptable discrepancy, and return $0$. any value under this threshold, statistically, is just noise
- the error rate is... I'm not quite sure how this works. can be calculated with a Markov inequality? you end up with $\dfrac{n}{\delta m}$, where $\delta$ is your acceptable discrepancy in the count.
	- the count-min sketch can never _under_estimate the frequencies of items, only overestimate.
	- the minimum estimate can only be an overestimate if _every_ counter is an overestimate
- why would you use this over a [[hash table]] that stores exact counts? well, imagine you're storing data  that has _trillions_ of events to count. it might be impossible to allocate enough memory to make a hash table work! but a count-min sketch _can_.
	- furthermore, you can tune your desired accuracy and memory use! want more accuracy? give it more memory. want more memory efficiency? sure, if you can accept lower accuracy.