---
tags: data, dataviz
alias: box plot
---

- used to display data corresponding to percentiles of a dataset. it doesn't care about the distribution, so you can use it to compare data with disparate shapes.
	- these are particularly useful when you stack 'em to compare multiple datasets
- based on 5 numerical measures:
	- maximum
	- 3rd [[quartile]]
	- median
	- 1st quartile
	- minimum
- the box is defined by the 1st, 2nd, and 3rd quartile. its width is the intraquartile range (IQR)
- where do the whiskers go?
	- you might put them at the min and max
	- or, you might put a "fence" at 1.5 * the IQR distance from both ends, choose the most extreme value within each fence, and draw the whisker there. then, all values outside that range are considered outliers.
	- or, could choose other methods of determining outliers, like [[SD]], or other percentiles
- in [[R]], you can create one with `boxplot()`