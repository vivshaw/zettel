tags:: stats, data, tables
alias:: independent format, dependent format

- in **independent format**, data has a column for the grouping variable, and a column for the value, like so:
	- | Group | Foo |
	  | --- | --- |
	  | 1 | 2.5 |
	  | 1 | 1.2 |
	  | 1 | 3.1 |
	  | 2 | 1.3 |
	  | 2 | 3.2 |
- in **dependent format**, the same data would have an independent column for each group, like so:
	- | Foo_1 | Foo_2 |
	  | --- | --- |
	  | 2.5 | 1.3 |
	  | 1.2 | 3.2 |
	  | 3.1 | NA |
- in [[R]], we can use [[lolcat]]'s `transform.independent.format.to.dependent.format()` and vice-versa to swap from one to the other. when we use `.to.dependent()`, the `fx` param should look something like: `fx = cm ~ group.name`