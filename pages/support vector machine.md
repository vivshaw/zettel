tags:: stats, ml
alias:: SVM

- a tool for [[classification]]. conceptually, it tries to find a line the separates the classes with the **maximum margin** around the boundary line (or hyperplane, in a higher-dimensional space)
- consider:
	- we can define a [[hyperplane]] in a space as the set of points $X$ such that $W \cdot X + b = 0$
	- we want to construct _two_ hyperplanes - one for the positive case, and one for the negative case - and maximize the distance between them (the **margin**)
	- so,  our constraint is: $Y_i [ W \cdot X + b ] - 1 \geq 0$, where
		- $Y_i$ is a dummy variable that is positive in positive cases, and negative in negative cases
		- $W$ is our weights vector
		- $X$ is our data
		- and $b$ is our bias
	- how far apart are the planes? that's $(X_+ - X_-) \cdot \dfrac{W}{||W||}$
		- if we sub in our constraint, we can reduce this to $\dfrac{2}{||W||}$. this is what we want to maximize.
		- equivalently, we need to *minimize* $||W||$. ($\dfrac{1}{2} \cdot ||W||$ will make our lives easier, though)
- SVMs are, by default, for classifying linear boundaries. but we can use the **kernel trick** to use SVMs on non-linear boundaries. we use a [[kernel]] to project the inputs to and from a higher-dimensional space which _is_ linearly separable.
- benefits of SVMs:
	- SVMs can work well even when you have more features than data points!
	- SVMs don't make as many assumptions about the shape of the data than methods like [[Naive Bayes]] or [[logistic regression]]
- we can work with SVMs in [[R]] using the `kernlab` library. for example:
	- ```R
	  svm.spec <- svm_poly(degree = 1) %>%
	    set_mode("classification") %>%
	    set_engine("kernlab", scaled = FALSE)
	  
	  svm.fit <- svm.spec %>% 
	    set_args(cost = 8) %>%
	    fit(y ~ ., data = data)
	  
	  svm.fit %>%
	    extract_fit_engine() %>%
	    plot()
	  ```