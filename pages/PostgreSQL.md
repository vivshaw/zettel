---
tags: SQL, db
alias: Postgres
---

- we can determine the [[SQL data types]] of a table using `INFORMATION_SCHEMA`:
	- ```SQL
	  SELECT column_name, data_type
	  FROM INFORMATION_SCHEMA.COLUMNS
	  WHERE table.name = 'baseball';
	  ```