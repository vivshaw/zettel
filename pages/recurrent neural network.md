tags:: machine learning, software engineering, data science, neural network
alias:: RNN

- an RNN is a [[neural network]] where the output of a node can influence the input of that same node. it is bidirectional, unlike a basic [[feedforward neural network]]
	- effectively, "a neural network with loops in". per colah:
	- ![LSTM3-SimpleRNN.png](../assets/LSTM3-SimpleRNN_1705013305495_0.png){:height 155, :width 393}
- Andrej Karpathy's [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) is a great introduction to the power of this technique.
- basic RNNs struggle to retain memory for the long term due to the [[vanishing gradient problem]]. [[LSTM]]s were created to solve this.