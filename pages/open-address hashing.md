---
tags: compsci, hash table, data structures
---

- a different solution to hash collisions compared to chaining.
	- in short: if the slot is occupied, put it in an alternate location. the sequence of locations to look at is called the **probing sequence**. it needs to eventually contain every position in the table.
	- a simple version of this might be, if location `i` is taken, just move it on ahead to `i+1`, and if that's taken, `i+2`, etc. etc. this is called **linear probing**. (you could also use a different step)
	- **quadratic probing** is another option
- deletion becomes a problem. when we delete something, it might be part of a probe sequence! then the sequence would stop prematurely.
	- we fix this by using a sort of soft-deletion. delete the content, but flag the cell as `DELETED`. search will treat it like it's still occupied. but insertion will treat it as empty, and reuse it.
- open addressing properties:
	- needs rehashing
	- utilizes space better
	- can have clustering problems
	- [[cache locality]], which can improve performance
- CPython uses open-address hashing!