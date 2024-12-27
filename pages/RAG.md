---
tags: machine learning, software engineering
---

- [retrieval-augmented generation](https://research.ibm.com/blog/retrieval-augmented-generation-RAG) is a technique to improve [[LLM]] responses by letting them use data from outside their training set, at response time. e.g., retrieving data form the public Internet, from a library of supplied documents, or from a database.
- initial paper: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401v4)
- has two phases:
	- **retrieval phase:** the model searches through the RAG dataset for useful snippets relevant to the user's query.
	- **generative phase:** the snippets are appended to the user's prompt. then, the LLM generates a response as normal.
	- this lets you augment an LLM relatively simply! just plug in a retrieval algorithm and you're golden.