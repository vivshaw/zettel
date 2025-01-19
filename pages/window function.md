---
tags: SQL, db
---

- **window functions** use values from multiple rows, to calculate a value for one row.
	- in some ways this is a bit like a `GROUP BY`, except that you can mix it with non-grouped stuff, or like correlated subquery, except more compact
	- we add an `OVER()` clause to a query to make it a window function, then we can use aggregates if desired.
		- we can user `ORDER BY` inside the `OVER()` to determine how the data is ordered.
		- we can use `PARTITION BY` inside the `OVER()` to choose how to chunk up the data.
			- ```SQL
			  SELECT team_name, budget, avg(salary) OVER (PARTITION BY team_name) FROM baseball_teams;
			  ```
	- we can use `RANK` to calculate an ordering
		- ```SQL
		  RANK() OVER(ORDER BY hits / at_bats) AS rbi_rank
		  ```
		- `RANK()` will assign the same value to ties, then skip the next number. `DENSE_RANK()` will apply the same value to ties, but _not_ skip the next number.
	- we can use `ROW_NUMBER()` to do what it says on the tin
	- we can use `LAG()` to reference prior rows, and `LEAD()` to reference later rows
	- `FIRST_VALUE()` and `LAST_VALUE()` get you the first and last rows in the whole table
	- `NTILE()` will break up the table into roughly N equal sections.
		- this is useful for [[pagination]]!
		- it's also useful for splitting data into [[quartile]]s, etc.t
	- **frames**/**sliding windows**:
		- we can create a sliding window in `OVER()` using `ROWS BETWEEN ... AND ...`
		- we can reference the current row with `CURRENT ROW`, or use `UNBOUNDED PRECEEDING` / `UNBOUNDED FOLLOWING` to reference the first or last row