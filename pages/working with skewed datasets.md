---
tags: ml, mlops, stats, error analysis
alias: skewed datasets
---

- a **skewed dataset** is one where the grand majority fall into one category. for example, a dataset of an extremely rare medical condition, where 99% of examples are healthy tissue
- with a dataset like this, [[accuracy]] isn't very useful, because you can get 99% far with just `print(False)`!
- you should instead use a [[confusion matrix]], and look at the [[recall]] and [[precision]]! the recall will be extremely low if your algorithm is in the `print(False)` case
	- you can use an [[F1 score]] to factor in both recall and precision