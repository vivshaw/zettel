---
tags: stats, spc, measurement systems analysis
---

- we would hope that:
	- the variability from the measurement system erro isn't a significant portion of the process specs, _or_ of the [[natural tolerance]]
- we can think of the measurement error, $\sigma_E$, as decomposing into [[repeatability]] error and [[reproducibility]] error:
	- $\sigma_E = \sqrt{\sigma^2_{Rpt} + \sigma^2_{Rpd}}$
- having calculated the measurement error,  we might then calculate:
	- a **P/T ratio**, showing us what portion of the spec tolerances the measurement error takes up:
		- $\dfrac{6\sigma_E}{USL - LSL}$
		- we'd hope this is less than 30%, ideally less than 10%
	- a **%GRR**, comparing the measurement error to the total variation:
		- $\dfrac{\sigma_E}{\sigma}$
		- we'd hope this is less than 9% of the total variance ideally less than 1%
	- or, a $GRR^2$ summing **equipment variance** (repeatability) and **appraiser variance** (reproducibility)
	- or, the number of distinguishable categories within the spec tolerance, as a measure of resolution
- we can determine the sources of variance using a [[two-way random effects ANOVA]]
- in [[R]], we can use [[lolcat]]'s `msa.continuous.repeatability.reproducibility()`
	- we might like to inspect the `ev.full` component! as well as `ev.reduced`