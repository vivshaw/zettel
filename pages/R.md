tags:: lang, stats, data

- gotchas: #footguns
	- R is 1-indexed, not 0-indexed!
- useful R snippets:
	- use `?` for manpages!
	- ```R
	  # Round some values to a certain number of decimal places, with nice formatting
	  nqtr <- function(x,d)(noquote(t(round.object(x,d))))
	  ```
	- use `str()` to see the structure of a dataframe
	- ```R
	  # Count the number of NA values in a dataframe
	  countna <- function(df)(sapply(df, function(x) sum(is.na(x))))
	  ```
	- the syntax for adding a linear model to a chart is a little funky, using a `~`:
		- ```R
		  plot(x = Data$foo, y = Data$bar, pch = 15)
		  abline(lm(bar~foo, data = Data), col = "red")
		  ```
	- we can create matrices from vectors like so:
	- ```R
	  matrix(
	  	c(1, 2, 3, 4, 5, 6),
	  	nrow = 2,
	    	ncol = 3,
	    	byrow = T,
	    	dimnames = list(c("Foo1", "Foo2"), c("Bar1", "Bar2", "Bar3"))
	  )
	  ```
	- the `~` operator is spicy! It defines the left and right-hand sides of an abstract function. for example:
	- ```R
	  # "Species is a function of sepal length, sepal width, petal length, and petal width
	  Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width
	  
	  # "Species is a function of all other values in the dataframe"
	  Species ~ .
	  ```
		- `~` is also [[overloaded]] by libraries like ggplot, lattice, and dplyr for their own purposes.
		- the `+` operator is also spicy - when in a formula like the above case, it is [[overloaded]] to mean "calculate a regression coefficient for this stuff"
		- see [this StackOverflow](https://stackoverflow.com/questions/8055508/in-r-formulas-why-do-i-have-to-use-the-i-function-on-power-terms-like-y-i/8055683#8055683) for more on `~` and `+`