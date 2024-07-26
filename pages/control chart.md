tags:: spc, stats, dataviz

- control charts allow us to distinguish between [[common cause]] and [[special cause]] variation
- these charts typically plot a variable against a centerline, usually the average value, and upper and lower control limits, which show the expected variation
	- they might also highlight **runs** of values above or below target, **outliers** outside the limits, or **trends**
- typically, you might use two charts: one to measure [[location]], the other to measure [[variance]].
	- you might also measure attrributes such as [[proportion]]s or rates.
- what size samples should you draw? you can calculate it as:
	- $n = [\dfrac{(z_{control\ limit} + z_\beta) \sigma}{\Delta}]^2$
		- ⚠️ $z_{control\ limit}$ is the number of [[standard deviation]]s that are within limit. a typical $z_{control\ limit}$ is 3. this is the same as an $\alpha$ of $.0027$.
		- in R, we can use [[lolcat]]'s `sample.size.mean.z.onesample()` for this purpose.
- there are two types:
	- **attribute charts**, for [[discrete data]]. often used for counting defects.
	- **variable charts**, for [[continuous data]].