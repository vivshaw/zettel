---
tags: python, dataviz
---

- a [[declarative]] data visualization library
- we define our viz in terms of a [[pandas]] dataset, a **mark**, and an **encoding**. they are composed by chaining functions. e.g.
	- ```python
	  alt.Chart(cars).mark_point().encode(
	      y='Origin',
	      x='Miles_per_Gallon'
	  )
	  ```
- marks:
	- your choice of mark will determine what sort of chart you get. e.g., `mark_bar()` will get you a [[histogram]], while `mark_point()` will get you a [[scatter plot]], and `mark_rect()` will get a 2D rectangular plot like a [[heatmap]]
- data types:
	- Q: [[quantitative data]]
	- N: [[nominal data]]
	- O: [[ordinal data]]
	- T: [[time-series data]]
	- Altair will automagically choose a sensible default way to represent your data based on type. for example, a Q dimension will get a continuous color mapping, while an N one will get discrete colors
	- Altair can infer the type, but it's better to be explicit by adding the type with `:Q` etc to the end of your field name
- encoding:
	- this is where we put our X and Y
	- we can bin by doing something like: `x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30))`
	- we can aggregate the data as well: `y='mean(Miles_per_Gallon)'`. this works with either explicit of implicit binning
	- we can use a `color` param to add color. this will automatically play nice with other stuff like binning
	- we can use a `column` param to split the plot into separate graphs
	- you can expose a piece of data on a tooltip with a `tooltip` param
	- it's possible to add a confidence interval with something like this:
		- ```python
		  alt.Chart(cars).mark_area().encode(
		      x='Year',
		      y='ci0(Miles_per_Gallon)',
		      y2='ci1(Miles_per_Gallon)'
		  )
		  ```
- interactivity:
	- you can use `.interactive()` to give the ability to zoom and pan around
	- you can use `.add_selection()` to let the suer select data points
		- we can then condition parts of the plot on the selection like so:
			- ```python
			  interval = alt.selection_interval()
			  
			  alt.Chart(cars).mark_point().encode(
			      x='Miles_per_Gallon',
			      y='Horsepower',
			      color=alt.condition(interval, 'Origin', alt.value('lightgray'))
			  ).add_selection(
			      interval
			  )
			  ```
		- selections will carry over across combined plots if you use stuff like `tranform_filter()`! this lets you do things like show a histogram of the currently selected points from a scatterplot
- transforms:
	- Altair supports transforms like filtering, calculation, aggregation, binning, and time unit change. you can specify the calcs using embedded Vega, like so: `men_women='datum.sex == 1 ? "Men" : "Women"'`
- combining plots:
	- plots can be layered via addition:
		- ```python
		  spread = alt.Chart(cars).mark_area(opacity=0.3).encode(
		      x=alt.X('Year', timeUnit='year'),
		      y=alt.Y('ci0(Miles_per_Gallon)', axis=alt.Axis(title='Miles per Gallon')),
		      y2='ci1(Miles_per_Gallon)',
		      color='Origin'
		  ).properties(
		      width=800
		  )
		  
		  lines = alt.Chart(cars).mark_line().encode(
		      x=alt.X('Year', timeUnit='year'),
		      y='mean(Miles_per_Gallon)',
		      color='Origin'
		  ).properties(
		      width=800
		  )
		  
		  spread + lines
		  ```
	- they can be placed horizontally to each other with `|`, and vertically with `&`
	- there is a `.repeat()` operator for batching the creation of lots of related charts:
		- ```python
		  fields = ['petalLength', 'petalWidth', 'sepalLength', 'sepalWidth']
		  
		  alt.Chart(iris).mark_point().encode(
		      alt.X(alt.repeat("column"), type='quantitative'),
		      alt.Y(alt.repeat("row"), type='quantitative'),
		      color='species'
		  ).properties(
		      width=200,
		      height=200
		  ).repeat(
		      row=fields,
		      column=fields[::-1]
		  ).interactive()
		  ```
- Altair deliberately raises an error for datasets over 5000 rows. in these cases, storing the data remotely at a URL is recommended