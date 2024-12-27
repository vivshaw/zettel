---
tags: db
---

- a read-only copy of all the aggregated data from an org's many [[OLTP]] instances
- optimized for [[OLAP]]- get all the data in one place, query it however without impacting prod
- the pipeline of data from OLTP to OLAP is called [[ETL]]
- a common schema is a **star schema**:
	- data is stored in **fact tables**, each row representing an event hat happened at some time
		- some columns are **attributes**, raw values
		- others are key references to **dimension tables**, other tables representing the who/what/where/when/how
		- these tables are typically huge! very wide, and many rows.
	- a variation is the **snowflake schema**, where dimension tables can have subdimensions