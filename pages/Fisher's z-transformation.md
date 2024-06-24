tags:: stats

- a tool to transform the skewed distribution of $r$ into something approximally [[normal]], making it easier to use the [[one-sample test]]s and [[two-sample test]]s we might wish to use.
- calculated as:
	- $r_{tr} = \operatorname{atanh}(r)$
	- equivalently, $r_{tr} = 0.5 \operatorname{log}(\dfrac{1 + r}{1 - r})$