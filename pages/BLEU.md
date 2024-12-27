---
tags: machine learning, software engineering, papers
---

- [Bleu: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/), Papineni et al. 2002
- uses modified n-gram similarity as a metric. this helps prevent high-precision but bad translations (e.g., sentences stacked with "likely" words)
	- for unigrams (words):
	  > one first counts the maximum number of times a word occurs in any single reference translation. Next, one clips the total count of each candidate word by its maximum reference count, adds these clipped counts up, and divides by the total (unclipped) number of candidate words.
	- now, just do this for all `n`! doing well with shorter n-grams represents *adequacy*. doing well with longer n-grams repesents *fluency*
- BLEU uses *n*-gram similarity up to order 4, over a corpus of multiple human translations of the same sentences. (having multiple translations averages out over possible translation choices). it combines the similarity for each order using a geometric mean. then, it adds a "brevity penalty" based on the average length of sentences in the corpus