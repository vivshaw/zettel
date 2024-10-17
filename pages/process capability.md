tags:: spc

- a measure of how well we can meet the design spec.
	- we can only analyze this for processes that are in a state of [[statistical control]].
- can be measured via **process indices**:
	- $C_p$ is the number of "full curves" that could fit within the spec limits, regardless of centering.
		- calculated using only [[dispersion]], as: $\dfrac{USL - LSL}{NT}$, where $NT$ is the [[natural tolerance]]
	- $C_{pk}$ is the number of "half curves" that could fit between the mean and the nearest specification limit
		- calculated using both the [[dispersion]] and [[mean]], as: $\dfrac{min(USL - \mu, \mu - LSL)}{NT/2}$
	- $C_{pm}$ uses the [[Taguchi loss function]]
		- calculated as $\dfrac{USL - LSL}{6\sqrt{\sigma^2 + (\mu - Nominal)^2}}$
- in [[R]], you can use [[lolcat]]'s `spc.capability.cp.simple()`