---
tags: db, data
---

- a group of writes and reads that are batched together. if they all succeed, they're "committed". if any of them fail, they're "aborted" and the whole transaction is rolled back.
- used to achieve [[ACID]] guarantees