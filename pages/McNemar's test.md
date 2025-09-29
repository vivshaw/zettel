---
tags: stats, statistical tests
---

- a test for [[proportion]]s in [[dependent samples]].
	- operates on a 2x2 [[contingency table]], and uses a [[chi-square test]] only using the changed values
	- the table is constructed based on the value of a pair across the two samples, like:
		- | | Pair1_0 | Pair1_1 |
		  | --- | --- | --- |
		  | Pair2_0 | A | B |
		  | Pair2_1 | C | D |
		- we take only cells B and C to test on.
- assumptions:
	- each pair of observations is independent
	- each cell represents one joint event
- calculated as: $\chi^2 = {(b-c)^2 \over b+c}$
- in [[R]], we can use [[lolcat]]'s `proportion.test.mcnemar.simple()` on the contingency table results
- in [[python]], we can use [[pingouin]]'s `chi2_mcnemar()`