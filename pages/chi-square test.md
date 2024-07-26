tags:: stats, statistical tests

- a test that uses the [[chi-square distribution]]
- assumptions:
	- the population is normally distributed
	- the specimens are independent
- calculated as $\chi^2=\sum{\dfrac{(O_i-E_i)^2}{E_i}}$, where $O_i$ is the observed value, and $E_i$ is the expected value
- in [[R]], you can use `chisq.test()` for this.
- commonly used for testing [[variance]]. in [[R]], can use [[lolcat]] 's `variance.test.onesample.simple()` for that.