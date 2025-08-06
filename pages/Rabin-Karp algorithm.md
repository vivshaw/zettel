---
tags: algorithms
---

- an algorithm for [[string matching]] using [[hash function]]s. it uses a rolling hash function over a window.
	- first, hash the target string $s$
	- next, hash a chunk of the text $t$ equal in length to $s$
	- now let's slide the window through the text:
		- do their hashes match? if so, could be a collision, so iterate through them and check that the strings actually match, and return the index if so
		- otherwise, move forward one position in $t$
- a cleverly-chosen hash function can do a sliding window while still being $O(1)$. for example, $Hash(s) = s_1 a^{k-1} + s_2 a^{k-2} + ... + s_k a^0$, for some constant $a$.
	- you can add and remove characters through addition and subtraction, and you can left-shift by multiplying by $a$
- this has [[time complexity]] of $O(n + m)$ expected time, but $O(nm)$ in the worst case
- you can use a similar technique to find a common substring of length $m$. simply hash all substrings of length $m$ and compare them. you can do this in $O(n_1 + n_2)$ time.