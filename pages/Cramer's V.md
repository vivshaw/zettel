---
tags: stats, [[relationship (stats)]]
---

- a measure of [[association]] for rectangular nominal data. it's based on the [[chi-square test]].
	- calculated as $\phi = \sqrt{\dfrac{\chi^2}{n(m-1)}}$
- in [[R]], we can use `cor.cramer.v()` on [[cross-tabulated]] data