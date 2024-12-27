---
tags: db
alias: WAL
---

- an append-only log of [[B-tree]] modifications, to which proposed operations are written before they are applied
- used to make [[relational DB]]s more reliable. if you crash, use the WAL to restore the desired state