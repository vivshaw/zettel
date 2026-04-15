---
tags: ml, LLMs, neural networks, fine-tuning
---

- **low-rank adaptation**, a technique to tune a model by adjusting only a specific subset of the model's weights.
	- in LoRA, we approximate $\Delta W = AB$, where $A$ and $B$ are two smaller matrices
	- this can reduce the number of weights that have to be trained
	- it also means the LoRA matrices can be kept separate from the model, and applied dynamically at inference time