---
tags: hash tables, compsci, data structures
---

- an alternative to chaining or [[open-address hashing]] for dealing with collisions.
- use two tables, with two hash functions, $h_1$ and $h_2$
- insertion:
	- try to insert $k$ into the first table at $h_1(k)$.
	- if it's occupied, display the existing key $l$, and try to insert it into the second table at $h_2(l)$
	- if _that's_ occupied, again displace the current occupant and attempt to hash and place in the other table. repeat this until you find a slot.
	- the the chain cycles or becomes too long, rehash the whole table.
- benefits:
	- lookup involves checking only two positions, $h_1(k)$ and $h_2(k)$
	- deletion is simple, just remove the key
	- expected [[time complexity]] of $O(1)$ for all operations