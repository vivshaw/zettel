---
tags: db, data structure, compsci, tree (DS)
---

- commonly used by [[relational DB]]s
- keeps key-value pairs in a balanced tree sorted by key, but maps them to fixed-size *blocks* or *pages*
- pages have unique addresses, allowing them to reference each other on-disk
- one page is the root of the b-tree, contains a set of keys, and refs in between them. each ref points to a child, responsible for the range of keys in between the keys around 'em.
- the **branching factor** is how many children each page has
- a B-tree with `n` keys has a depth of `O(log n)`
- if a DB crashes while doing a write that's split across multiple pages, it could corrupt!
	- commonly, we use a [[write-ahead log]]
	- some DBs use copy-on-write instead, so that old pages can't be corrupted