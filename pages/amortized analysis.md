---
tags: algorithms
---

- sometimes, we can guarantee that _on average_, an algorithm will take a small amount of time even if some individual operations may take a long amount of time.
	- see also [[amortization]]
- in **aggregated analysis**, we look at a sequence of $n$ operations, calculate the worst-case time taken, then divide it by $n$ to get the average cost.
- in the **accounting method**, you do this by assigning "charges" to different operations. when an operation does better than the amortized cost, we give it some credit. worse, we spend some credit.
- in the **potential method**, you do this by thinking of it as [[potential energy]]