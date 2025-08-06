---
tags: compsci, data structure
---

- a Bloom filter is a compact and fast [[set]] data structure, based on hashing
	- it is approximate by nature. you can be sure an element *doesn't* belong to the set (no false negatives), but you can't be sure that an element *does* (false positives)
	- represented as a bit string
- choose a set of random hash functions $h_1 ... h_k$.
	- to **insert** an element, hash it with every one of those hash functions and set all the resulting bits
	- to **check membership** of an element, hash it with every hash function and check if each bit is set