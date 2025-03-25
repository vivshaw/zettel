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
	- we can also query for type info about specific types:
		- ```SQL
		  SELECT typname, typcategory
		  FROM pg_type
		  WHERE typname = 'foo'
		  ```
- Postgres has full text search! we have to use some funky syntax, though:
	- `WHERE to_tsvector(my_string) @@ to_tsquery('foo')`
- you can create custom types with `CREATE TYPE`
	- an `ENUM()` might be a common choice for this
- you can add user-defined functions!
	- ```SQL
	  CREATE FUNCTION doubled(i integer) RETURNS integer AS $$
	    BEGIN
	    	RETURN 2 * i;
	    END
	  $$ LANGUAGE plpgsql;
	  ```
- working with extensions:
	- we can check extensions like so:
		- ```SQL
		  -- See all available extensions
		  SELECT name FROM pg_available_extensions;
		  
		  -- See installed extensions
		  SELECT extname FROM pg_extension;
		  ```
	- load extensions with `CREATE EXTENSION IF NOT EXISTS ext_name`