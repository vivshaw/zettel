---
tags: stats, data, statistical tests
---

- a test of normality that works well for small datasets, but may be inaccurate for larger ones. it is more sensitive to departures from normality.
- in [[R]], you can use `shapiro.wilk.normality.test()`, or `summary.continuous()` from `lolcat`
	- for exponentiality, you can use `shapiro.wilk.exponentiality.test()`