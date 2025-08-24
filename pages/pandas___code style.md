---
tags: python, pandas, data
---

- let's simplify and improve a few queries!
- first: select some columns, filter according to a condition, then sort.
	- ```python
	  # Naive attempt
	  best_math_schools = schools[["school_name", "average_math"]]
	  best_math_schools = best_math_schools[best_math_schools["average_math"] > 600]
	  best_math_schools = best_math_schools.sort_values("average_math", ascending = False)
	  ```
	- ```python
	  # Improved, with loc syntax
	  best_math_schools = (
	      schools
	        .loc[schools["average_math"] > 640, ["school_name", "average_math"]]
	        .sort_values("average_math", ascending=False)
	  )
	  ```
	- ```python
	  # Improved, with query syntax
	  sat_cols = ["average_math", "average_reading", "average_writing"]
	  
	  best_math_schools = (
	      schools
	        .query("average_math > 640")
	        .loc[:, ["school_name", "average_math"]]
	        .sort_values("average_math", ascending=False)
	  )
	  ```
- second: create a new column from the others, sort on it, select some columns, sort, and limit.
	- ```python
	  # Naive attempt
	  top_10_schools = schools.copy()
	  top_10_schools["total_SAT"] = top_10_schools["average_math"] + top_10_schools["average_reading"] + top_10_schools["average_writing"]
	  top_10_schools = top_10_schools[["school_name", "total_SAT"]]
	  top_10_schools = top_10_schools.sort_values("total_SAT", ascending = False)
	  top_10_schools = top_10_schools[0:10]
	  ```
	- ```python
	  # Improved
	  top_10_schools = (
	      schools
	        .assign(total_SAT=schools[sat_cols].sum(axis=1))
	        .nlargest(10, "total_SAT")
	    	  .loc[:, ["school_name", "total_SAT"]]
	  )
	  ```
- third: create a calculated column, then groupby, then do a summary stat, then sort, then find the
	- ```python
	  # Naive approach
	  largest_std_dev = schools.copy()
	  largest_std_dev["total_SAT"] = largest_std_dev["average_math"] + largest_std_dev["average_reading"] + largest_std_dev["average_writing"]
	  largest_std_dev = largest_std_dev[["borough", "school_name", "total_SAT"]]
	  largest_std_dev = largest_std_dev.groupby("borough").agg(num_schools=("school_name", "count"), std_total_sat=("total_SAT", "std")).sort_values("std_total_sat", ascending = False)
	  ```
	- ```python
	  # Improved, with `.std()`
	  sat_cols = ["average_math", "average_reading", "average_writing"]
	  
	  largest_std_dev = (
	      schools
	        .assign(total_SAT=schools[sat_cols].sum(axis=1))
	        .groupby("borough")
	    	  ["total_SAT"]
	        .std()
	        .nlargest(1)
	        .to_frame(name="std_total_SAT")
	  )
	  ```
	- ```python
	  # Improved, with `.agg()`
	  # which we might want if we want to do more operations at the same time,
	  # like also get a count
	  sat_cols = ["average_math", "average_reading", "average_writing"]
	  
	  largest_std_dev = (
	      schools
	        .assign(total_SAT=schools[sat_cols].sum(axis=1))
	        .groupby("borough")
	        .agg(
	            std_total_SAT=("total_SAT", "std"),
	            n_schools=("school_name", "size"),     # or "count" / "nunique" as needed
	        )
	        .sort_values("std_total_SAT", ascending=False)
	        .head(1)  # drop this if you want all boroughs
	  )
	  ```