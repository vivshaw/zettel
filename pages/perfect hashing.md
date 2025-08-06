---
tags: hash tables, data structures, algorithms
---

- **perfect hashing:** suppose you already know the keys you're gonna insert. can you create a [[hash table]] where zero collisions are possible? yes!
	- create two levels of hash tables.
	- the first has $n$ slots, using hash function $h_1$
	- the second level, for each slot $j$ with collisions, create a hash table with size $n_j^2$ to store those colliding keys in. use a different hash function for each of these, and if there are any collisions, try again with a different hash function.
- these tables are immutable. you can't add to them after creation.