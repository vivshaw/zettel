tags:: db
aliases:: schema-on-read, schema-on-write

- **schema-on-read vs schema-on-write:**
	- in schema-on-read, no format is enforced on data as it's written to DB. instead, it's assumed at write time.
		- [[document DB]]s and [[graph DB]]s are like this
		- similar to [[dynamically typed]] PLs
		- best when your data is heterogenous
	- in schema-on-write, a format is enforced on what data can be added at write time
		- most [[relational DB]]s are like this
		- similar to [[statically typed]] PLs