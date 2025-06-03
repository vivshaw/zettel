---
tags: hashing, data structures, algorithms
---

- a data structure that maps keys to values using a [[hash function]]
- what happens when the hash function has a key collision for two values?
	- we deal with this by having each slot store a _list_ of key/value pairs.
- what can we do with a hash table?
	- **insert:** hash the key, append to the list
	- **find:** hash the key, search the list
		- this has worst-case [[time complexity]] of $O(n)$ if all keys collide, but is more commonly $O(n / m)$ (or $O(load\ factor)$)
	- **delete:** hash the key, search the list, delete
		- same as find
- the **load factor** of a hash table is the # of elements / the capacity of the table
	- commonly, when the load factor exceeds 1/2, you might **rehash** into a table twice the size, which is $O(n)$