---
tags: algorithms, compsci
---

- the function $h$ that maps a key $k$ to its hash $H(k)$
- we'd love it to have certain ideal properties:
	- we'd ideally like our hash functions to be **independent uniform hash functions**. this means that the output $h(k)$ for a given $k$ is independently and uniformly selected from $U$, but deterministically
	- this isn't really possible in reality, but it's the ideal we'll compare all hash functions to
- a **collision** occurs when two keys hash to the same value
- we might work with families of hash functions. - in a **universal hash function family**, the chance of any two functions colliding for a given key is $1/m$ , where $m$ is the size of the universe $U$
	- you might want this so that you can do randomized hashing by picking one from the family at random