---
tags: python, data, dataviz, software engineering
---

- a common Python library for data visualization
- build a [[line plot]] with `plt.plot()`
- build a [[scatter plot]] with `plt.scatter()`
- build a [[histogram]] with `plt.hist(values, bins=num_bins)`
- you can change the scales of the axes like: `plt.xscale('log')`
- you can label the plot with `plt.xlabel()`, `.ylabel()`, and `.title()`. or `ax.set_xlabel()`, etc
- ticks can be customized with `.xtick(tick_values, tick_labels)` or `.ytick()`
- points can be configured with the `s` param for size, `c` or `color` param for color, `linstyle`, etc.
- you can add a grid with `.grid(True)`
- subplots can be created with `fig, ax = plt.subplots(3,2)` for 3 rows of 2 columns. then index with `ax[0,2]` etc.
	- the `ax.twinx()` method can be used for multiple y-axes sharing the same x-axis