---
tags: math, algorithms, recurrence
---

- a general method for solving recurrences, in which you guess the recurrence using symbolic constants, then use induction to demonstrate it works and calculate the constants
	- there isn't a general method to make good guesses, though! you have to pick it up from similar algorithms, or get lucky.
	- sometimes you can use a **recursion tree** to generate a good guess- a tree where each node is the cost of some subproblem, that you can then recursively sum up by level