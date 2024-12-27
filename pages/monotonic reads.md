---
tags: distsys, db
---

- we want to guarantee that if a user sees something in a read, no future reads come from a previous time when that thing didn't exist. e.g., if I see a comment from User A, it should still be there when I refresh, even if not all replicas have caught up with it yet
- can achieve this by ensuring all of a user's reads come from the same replica