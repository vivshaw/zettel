---
tags: db
---

- **Atomicity**
	- different from [[atomic operation]]s
	- instead, means that if a write fails, all writes in the transaction can be aborted
- **Consistency**
	- means many things in many places.
	- here, means that if the database is valid according to its intended invariants before a transaction, and any writes during the transaction preserve it, then the db will be valid afterward.
	- but this all depends on the application's definition of what valid data looks like, and its implementation of correct transactions. so... the letter C doesn't really belong, at least according to Kleppmann!
	- different from [[CAP theorem]] consistency
- **Isolation**
	- concurrently executing transactions are isolated from one another, and can't step on each others' toes. the end result is the same as if they ran serially.
- **Durability**
	- once a transaction has been committed, data will not be lost
	- this doesn't exist perfectly!