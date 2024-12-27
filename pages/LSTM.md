---
tags: machine learning, software engineering, data science, neural network
alias: long short-term memory
---

- a **long short-term memory** model is a type of [[recurrent neural network]] that is designed to retain memory of the information it processes for a long time.
	- this is particularly useful when working with [[time-series data]]. e.g., speech recognition, text-to-speech, machine language
	- basic RNNS aren't great for this because of the [[vanishing gradient problem]]
- ref:
	- [Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) via colah
	- [Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf), Hochreiter & Shmidhuber (1997)
- it does this by having a more complex cell structure than a basic RNN. this contains **gates:**
	- a **forget gate**, which decides what to throw away from the cell state (using a [[sigmoid]])
	- an **input gate**, which decides what new information should be stored in the cell state (using a sigmoid and a [[tanh]])
	- an **output gate**, which determines which parts of the cell state to output (using a sigmoid)
	- ![A LSTM neural network.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png){:height 232, :width 427}