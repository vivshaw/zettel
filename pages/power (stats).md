tags:: stats

- a measure of the ability to detect something
- calculated as `1 - β` (the [[type-2 error]])
- increasing [[sample size]] generally increases power
- in [[R]], you can use:
	- `power.mean.z.onesample()` (or `.t.onesample()` when [[standard deviation]] is unknown) from `lolcat` for [[mean]]s
	- `power.variance.onesample()` for [[variance]]
	- `power.proportions.onesample.exact()` for proportions
	- `power.count.poisson.onesample.exact()` for [[Poisson distribution]] rates