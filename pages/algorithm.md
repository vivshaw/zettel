---
tags: compsci, math
alias: algorithms
---

- an **algorithm** is a [[computational procedure]]. stated differently, it's a step-by-step recipe for solving a given problem.
	- it takes a set of **inputs**, processes them via [[deterministic]] steps, and returns **outputs**
- algorithms have been around for ages. their early history:
	- Ancient Indian mathematicians created the place value system and arithmetic rules.
	- Greek mathematicians gave us the Euclidean algorithm and Sieve of Eratosthenes
	- Chinese mathematicians develop procedures for abacus computation
	- the word "algorithm" comes from [[al-Khwarizmi]]'s name!
- in the past, algorithms have often been seen as an afterthought to the more important [[theorem]] it's used to demonstrate. that's different nowadays! we rely on computers, and computers need to calculate. to do that efficiently, we had to start studying algorithms as a first-class science
	- [[Turing]] in the 1930s came up with the [[Turing machine]], the abstract model of computation that we still use today. This mathematically formalized what a computation is
	- [[Knuth]] and his Art of Computer Programming are probably the second-biggest influence on the modern study of algorithms
- we can measure an algorithm's efficiency with [[computational complexity]]
- a correct algorithm will always halt, and always give the correct output
	- but algorithms can be useful even if they are incorrect, if the error rate is controllable!
- an algorithm typically operates on a particular [[data structure]]