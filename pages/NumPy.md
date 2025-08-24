---
tags: data, python, software engineering
---

- a Python library for doing [[linear algebra]]
- a NumPy Array is the basic datatype
	- these can be subset much like a Python list. when indexing, the bit before the comma is the rows, and the bit after is the columns
	- they must contain data all of the same type
	- `.shape` will get you the shape of multidimensional arrays. `(2, 5)` means 2 rows, 5 columns
	- you can iterate one with `np.nditer()`
- you can do comparisons or conditionals on either a scalar value, or array of matching length
	- you'll need to use `np.logical_and()` and friends if you need logical operators, though
- NumPy alos provides some basic statistical tools like [[mean]], [[median]], [[standard deviation]] (`np.std()`), [[correlation]] (`np.corrcoef()`) etc.