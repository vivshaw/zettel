tags:: AI, ml, LLMs

- a transformer has two parts:
	- an **encoder**, which converts text into embedding vectors in the model's [[latent space]], capturing the context of the text
	- a **decoder**, which receives the embedding vectors and converts them into output text
- the layers inside the encoder and decoder are connected via the **self-attention mechanism**
- different network architectures can be built with this general model.
	- for example, [[BERT]] specializes in word prediction due to its encoder-only architecture & training on masked-word modeling and next-sentence prediction.
	- conversely, [[GPT]] is *decoder*-only and can be used for [[generative AI]] tasks.