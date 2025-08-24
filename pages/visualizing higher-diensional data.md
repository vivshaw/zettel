---
tags: data, dataviz
---

- some options you might consider for distinguishing datapoints:
	- color
		- use an equal perception palette
		- use a color scale that makes sense:
			- qualitative: different hues, for underordered categories
			- sequential: shades of same hue, for showing ordering
			- diverging: scale between 2 colors, for showing above and below a midpoint
	- transparency, similar to color
	- size, which has the benefit or drawback that larger points tend to look more important
	- shape, useful if categorical, but unfortunately shapes don't have a natural order
	- line type, for a line plot
- or, you could just slap down a lot of smaller plots:
	- [[pair plot]]