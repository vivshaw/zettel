---
tags: stats, data, tables
alias: cross-tabulation, cross-tabulated
---

- a format for data in which we compare variables by placing each on their own axis.
	- in spreadsheets, these are often created with [[pivot tables]]
- e.g.:
	- |  | Foo 1 | Foo 2 |
	  | --- | --- | --- |
	  | Bar 1 | 5 | 6 |
	  | Bar 2 | 2 | 0 |
- in [[R]], we can use `xtabs()`, or [[lolcat]]'s `transform.individual.format.to.xt()`, or `table()`