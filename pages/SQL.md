---
tags: db, data
---

- we can create **views**, which are queryable like tables, using `CREATE VIEW`:
	- ```SQL
	  CREATE VIEW my_library AS
	  SELECT *
	  FROM books
	  WHERE owned 
	  ```
- the syntax for combining `SELECT DISTINCT` and `COUNT` requires you to shuffle the commands a smidge:
	- ```SQL
	  SELECT COUNT(DISTINCT author)
	  FROM books;
	  ```
- the order operations are written in is pretty different from the order they execute!
	- semantic:
		- ```
		  SELECT
		  WHERE
		  FROM
		  GROUP BY
		  ORDER BY
		  LIMIT
		  ```
	- operations:
		- ```
		  FROM
		  GROUP BY
		  WHERE
		  SELECT
		  ORDER BY
		  LIMIT
		  ```
- `WHERE` vs `HAVING` - you can't use `WHERE` to operate on groups from `GROUP BY`. so, use `HAVING` instead.
	- this is about order of operations. grouping happens very early! `HAVING` operates _on the groups_, not on the records.
	- we also can't use aliases in `HAVING` clauses for that reason.
- set-theoretic operations vs. `JOIN`s:
	- the set operators like `UNION` work at the row level. you'll get all the rows from the first query, ad all the rows from the second.
		- as a result, the tables need to have the same number of columns with the same data types!
	- `JOIN`s work at the column level. they'll glue the columns from the right and left tables together
- we can do case-ofs with `CASE WHEN ... THEN ... ELSE ... END`
	- we can even used these inside a `WHERE` clause!
- we can put **subqueries** inside any part of our query
	- a subquery inside `SELECT` can be useful for aggregation
	- a subquery inside the `FROM` is useful for doing preprocessing on your data before you query it. for example, transforming it into a better format for your actual query. this can be combined with `JOIN`s!
	- a subquery inside the `WHERE` is useful for comparisons- selecting records with a data point above the average, selecting records that match a list from querying some other table, etc
	- we can nest subqueries inside one another!
	- we can also do **correlated subqueries**, where the subquery depends on the row values (and so runs again for each row)
- we can construct **common table expressions** with `WITH ... AS`. this lets us construct a table that we can reference throughout the rest of the query. this can be neater than repeating a subquery over and over again throughout the query
- `ROLLUP()` can be added to `GROUP BY` to add extra rows when you group. it's especially useful for group totals (if you roll up one `GROUP BY` column) or grand totals (if you roll up all of them)
	- `CUBE()` will get you _both_ subtotals and grand totals
- `COALESCE()` lets you replace null values in a column with another value, when you wrap a column you `SELECT` in it
- `STRING_AGG()` is an aggregate function that concatenates all the string values in a column, with a separator
- **[[pivot tables]]**
	- you can pivot a column with `CROSSTAB`, but you'll first need to `CREATE EXTENSION`:
		- ```SQL
		  CREATE EXTENSION IF NOT EXISTS tablefunc;
		  
		  SELECT * FROM CROSSTAB($$
		                         ...[your whole query here]...
		  $$) AS ct (...[your column names]...)
		  ```