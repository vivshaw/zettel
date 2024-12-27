---
tags: db
---

- online transaction processing involves live, low-latency batches of reads and writes
- small numbers of reads fetched by key, random-access, low-latency writes from user input, primarily used by end users
- disk seek time tends to be the bottleneck
- ex: commercial transactions, actions in a game, comments on a blog
- contrast with [[OLAP]]