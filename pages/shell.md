tags:: linux, software engineering

- shell gotchas: #footguns
	- you need to escape `*` whenever you use it! it is, by default, reserved for globbing.
	- spacing!
		- when not parenthesized, you must separate mathematical operands with a space
		- but you must _not_ have spaces around the `=` when assigning variables!
	- parentheses
		- using regular parentheses to group mathematical exprs won't cut it, you need [the double-parentheses construct](https://tldp.org/LDP/abs/html/dblparens.html)
			- ```shell
			  a=$(( 5 + 3 ))    # `a` is now `8`
			  ```
		- but it's not _really_ a parens construct... it's a C-style math construct!
			- ```shell
			  echo $(( t = a<45?7:11 ))   # C-style trinary operator!
			  ```
	- floating-point
		- shell math is integer only! if you want fp math, you need to call out to `bc -l` or `awk`!
	- `=`
		- with spaces and inside `[]`, i's used to test equality.
		- but without spaces, it sets a variable!
	- `>` / `<`
		- in Bash, this is *not*  gt / lt- use `-gt`/`-lt` for that.
		- `>`/`<` compares strings by alphabetical sort order!