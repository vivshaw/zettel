---
tags: data, dataviz
---

- a **density plot** can be thought of like a smooth version of a [[histogram]]
- used for [[discrete data]]
- **density**, calculated on binned data, is the count multiplied by the bin size. you can plot the density to see a smoothed curve. often, you might put this over a regular histogram. but you needn't.
	- (see https://homepage.divms.uiowa.edu/~luke/classes/STAT7400-2023/slides/smooth.html for an extensive discussion of density & smoothing)
- you might combine this with a [[rug plot]] to show the actual values
- in [[R]], you can create one with `plot(density())`