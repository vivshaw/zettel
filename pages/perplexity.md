---
tags: stats, LLM, ml
---

- measures how well the probability distribution predicted by a model matches the real probability distribution
- it's calculated as, $e^{loss}$, where $loss$ is the [[cross entropy loss]]
- it can be interpreted to mean: what's the vocabulary size about which the model is confused? for each token it _should_ generate, how many other tokens is it unsure whether it might be? this is considered more interpretable than the raw loss