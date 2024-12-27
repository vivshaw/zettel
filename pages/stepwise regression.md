---
tags: stats, regression
---

- the process of building a regression model through a multi-step procedure. this is especially common in [[data mining]]
- 3 commons paths:
	- **forward** - start with a null model, fit $p$ separate simple linear regressions, then add whichever variable has the lowest RSS. then repeat until we're happy.
	- **backward** - start with every variable, then drop the least significant variable. repeat until we're happy (e.g., all variables are significant).
	- **mixed** - do the forward method. then, remove all variables with large p-values.
- ⚠️ be **extremely careful** about using this. it possibly the most common form of [[p-hacking]]! if you build the model and test it on the same data, you are plunging head-first into the [[multiple comparisons problem]]. if you must, try something like a [[test-train split]], or apply a correction factor