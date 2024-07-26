tags:: spc, stats

- a set of constants that can be used to estimate the standard deviations for variables we wish to measure on [[control chart]]s. the are empirical estimates based on the [[sample size]].
- we can use these to calculate:
	- $SD(X) = \dfrac{\bar{R}}{d_2}$
	- $SD(X) = \dfrac{\bar{MR}}{d_2}$ (sample size will be $2$)
	- $SD(X) = \dfrac{\bar{S}}{c_4}$
	- $SD(\bar{X}) = \dfrac{\bar{R}}{d_2 \sqrt{n}}$
	- $SD(R) = \dfrac{d_3R}{d_2}$
- in [[R]], we can use [[lolcat]]'s `spc.constant.calculation` to calculate these values.