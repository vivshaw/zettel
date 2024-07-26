tags:: langs, software engineering

- #nuggets
	- since 3.1, we can pun hash names:
		- ```Ruby
		  a = 1
		  b = 2
		  
		  { a:, b: } # => { a: 1, b: 2 }
		  ```
		- this will also call getter methods!
		- the same can be done for keyword arguments, not just hashes
	- the English `or` has an extra-low precedence, lower even than assignment. this is usefu for one-liners that short-circuit. e.g.:
		- ```Ruby
		  response = Net::HTTP.get_response(URI("https://foo.bar/")) in Net::HTTPSuccess or abort "Error: #{response.message}"
		  ```
	- `===`, in Ruby, checks class equality, same as `is_a?`.
		- `in` _also_ checks this when you have a class on the right side!