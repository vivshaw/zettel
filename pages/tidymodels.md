tags:: R

- you can create a model like:
	- ```R
	  lm.spec <- linear_reg() %>%  # What sort of thing are we doing?
	    set_mode("regression") %>% # Are wwe regressing or classifying?
	    set_engine("lm")           # What should we use to do it?
	  ```
- then, fit the model:
	- ```R
	  lm.fit <- lm_spec %>% fit(y ~ x, data = Data)
	  ```
- we can access the parameters with `tidy(lm.fit)`, and the model statistics with `glance(lm.fit)`
- we can make predictions with `predict(lm.fit, new_data = new.data)`
- we can also use the `mutate` package to do data transformation. here, we add an `x1^2` term, then add an interaction term `x1^2 * x2`:
	- ```R
	  recipe.spec <- recipe(y ~ x1 + x2, data = Data) %>%
	  	step_mutate(x1.2 = x1 ^ 2) %>%
	  	step_interact(~ x1:x2)
	  
	  lm.workflow <- workflow() %>%
	  	add_model(lm.spec) %>%
	  	add_recipe(recipe.spec)
	  
	  lm.fit.2 <- lm.workflow %>% fit(Data)
	  ```
- we can add predictions to a test set and graph the confusion matrix in a tidy way:
	- ```R
	  augment(lm.fit, new_data = Test) %>%
	  	conf_mat(truth = y, estimate = .pred_class) %>%
	  	autoplot(type = "heatmap")
	  ```
- or assess accuracy!
	- ```R
	  augment(lm.fit, new_data = Test) %>%
	  	accuracy(truth = y, estimate = .pred_class)
	  ```
- you can easily add a normalization step with a workflow:
	- ```R
	   step_normalize(all_numeric_predictors())
	  ```
- you can turn factors into dummy vars:
	- ```R
	  step_dummy(all_nominal_predictors())
	  ```
- you can tune [[hyperparameters]] in a workflow with [tune_grid()](https://tune.tidymodels.org/reference/tune_grid.html)