tags:: machine learning, software engineering, data science
alias:: neural networks

- a **neuron** is generally composed of two parts- a linear portion, and an activation function. common choice for activation are the [[sigmoid]] or [[ReLU]].
- in [[R]], we can use the `neuralnet` library:
	- ```R
	  net <- neuralnet(Species ~ ., iris, hidden = c(6,6,3))
	  ```