---
tags: SQL, db
---

- date & time types:
	- `TIMESTAMP` has both a date and a tijme
	- `TIME` is a time. by default, it does not have a timezone
	- `DATE` is a date
	- `INTERVAL` represents a span of time- like `INTERVAL '3 days'`
	- `dow` gets ya the day of the week
	- we can do arithmetic on dates! if we add integers, the implied value will be that of the datatype we're adding to.
	- the `AGE()` function calculates the difference between two timestamps
	- we can use `NOW` to get the current timestamp, with timezone!
		- if we want to strip the TZ,  or remove the date or time, we'll need to cast it.
			- in [[Postgres]], we can do `NOW()::timestamp`
			- otherwise, we can do `CAST(NOW() as timestamp)`
	- in [[Postgres]] we can also do `CURRENT_TIMESTAMP()`, which allows us to round to specified places
	- `CURRENT_DATE` and `CURRENT_TIME` will get the date and time respectively
	- we can extract bits of a timestamp with `EXTRACT(year FROM my_date)` or equivalently `DATE_PART('year', my_date)`
	- we can truncate timestamps or intervals with `DATE_TRUNC('year', my_timestamp)`
- `ARRAY`s can be indexed into with brackets
	- there are array-specific functions, like `'foo' = ANY(my_array)` or `my_array @> ARRAY['foo']` ("contains")
- strings
	- we can concatenate with `||`
		- in [[Postgres]], we can use `CONCAT()` with an arbitrary number of string params
	- `UPPER()` and `LOWER()` can manipulate the case
	- `INITCAP()` will put a string in title case
	- `REPLACE(field, 'foo', 'bar')` replaces a substring with another
	- `REVERSE()` does what it says on the tin!
	- `CHAR_LENGTH()` or `LENGTH()` can count the length
	- you can find the position of a substring with `POSITION('foo' IN my_string)` or `STRPOS(my_string, 'foo')`
	- `RIGHT(my_string, 50)` and `LEFT(my_string, 50)` let you extract substrings from the left or right side
	- `SUBSTRING(my_string, 10, 50)` gets you a specified substring
		- we can also do dynamic stuff with `FROM ... FOR` like, `SUBSTRING(email, FROM 0 FOR POSITION('@' IN email))`
		- `SUBSTR()` is a simplified substring function that doesn't allow the from-for stuff
	- `TRIM(leading | trailing | both [characters] FROM my_string)` lets you remove stuff from the ends of strings. when called without params, it trims whitespace
		- `LTRIM()` and `RTRIM()` do the same for just one end of the string
	- `LPAD(my_string, 10, '*')` will expand the string up to a given size using a given char. `RPAD()` will do the same for the other side of the string. space is the default
- numbers
	- we can truncate with `TRUNC()`, or round with `ROUND()`
	- we can use `generate_series(start, end, step)` to create a column with a range prefilled