---
tags: systems engineering
---

- a process for resolving conflicts between competing design goals or parameters. everything in engineering is a trade-off, and a trade study is how we resolve those trade-offs.
- we do this in a step by step, data-driven process:
	- determine objectives
	- establish alternatives
	- establish criteria
	- weight criteria
		- you should weight them to create a score out of 1.0, or out of 100, for ease of interpretation.
	- convert values to scores
		- normalize your criteria to 0-10 scales, with 10 as your preferred value
		- if you're dealing with something qualitative, you can using polling to convert it to a quantity
	- evaluate weighted scores
	- perform sensitivity analysis
		- we want to estimate how sensitive the final ratings are to small changes in the inputs
	- if there's sufficient info to decide, select an alternative! otherwise, iterate the process.
- don't treat cost as a trade-off! do your trade study on only the quantifiable technical characteristics. then, treat cost as an independent variable.
	- if you *must* factor it in, consider using the sensitivity analysis step to see how changing cost changes the outcome.