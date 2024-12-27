---
tags: ml, mlops, error analysis
---

- a framework for a final performance audit before deployment from [[Andrew Ng]]:
	- brainstorm the ways the system might go wrong
		- performance on particular subsets?
		- how common are particular errors?
		- performance on rare classes
	- establish metrics to assess performance for these specific issues on slices of your dataset
	- get buy-in from business & product
- this can be automated, and there are tools for it- for example, [[Tensorflow]] has [[TFMA]]