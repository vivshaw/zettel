tags:: data, dataviz
alias:: bar chart

- helps to view the dispersion, central tendency, and shape of some data
- can be grouped (values bucketed into class intervals) or ungrouped (one bar per unique value)
- it's best to avoid exceeding 20 bins, for visual clarity
- interpreting a histogram:
	- do you see skew, or symmetry?
	- is the data truncated at its upper or lower bound? that could signify some natural boundary
	- does it look [[uniform]]? [[normal]]?
	- is it multimodal?
	- is it combed? if so, that might signify lack of resolution in measurement?
	- are there any clusters of outliers?
- in [[R]], you can create one with `hist()`