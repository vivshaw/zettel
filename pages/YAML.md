- 🌶️ YAML is spicy! some of the most [[jacked]] corners are listed here. examples/quotes largely from Ruud van Asseldonk's [The YAML Document from Hell](https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell). #footguns
	- **Sexagesimal numbers:**
	  ```YAML
	  port_mapping:
	    - 22:22
	    - 80:80
	    - 443:443
	  ```
	  ```JSON
	  {"port_mapping": [1342, "80:80", "443:443"]}
	  ```
		- numbers from 0 to 59 separated by colons are [sexagesimal (base 60) number literals](https://yaml.org/spec/1.1/#id858600) in YAML 1.1!
	- **Octal numbers:**
	  ```YAML
	  # `perms` will be the number 511, not the string `0777`
	  perms: 0777
	  ```
		- numeric literals starting with `0` and with no digits `>7` will be parsed as an octal
		- ...and the spec is [fairly non-obvious](https://yaml.org/spec/1.2-old/spec.html#id2805071) about this!
		- (This is _proooobably_ Yaml 1.1 only, but unclear)
	- **Anchors and tags:**
	  ```YAML
	  serve:
	    - /robots.txt
	    - /favicon.ico
	    - *.html
	    - *.png
	    - !.git
	  ```
		- `*` is an [alias for an anchor](https://yaml.org/spec/1.2.2/#3222-anchors-and-aliases), and we have no anchors with those names, so this will error!
		- `!` is a [tag](https://yaml.org/spec/1.2.2/#3212-tags), used to represent types from the host language
			- > A tag starting with `!` is up to the parser to interpret, often by calling a constructor with the given name and providing it the value that follows after the tag. This means that **loading an untrusted yaml document is generally unsafe**, as it may lead to arbitrary code execution.
	- **Boolean literals:**
	  ```YAML
	  geoblock_regions:
	    - dk
	    - fi
	    - is
	    - no
	    - se
	  ```
	  ```JSON
	  {"geoblock_regions": ["dk", "fi", "is", false, "se"]}
	  ```
		- > The literals `off`, `no`, and `n`, in various capitalizations ([but not any capitalization](https://yaml.org/type/bool.html)!), are all `false` in yaml 1.1, while `on`, `yes`, and `y` are true. In yaml 1.2 these alternative spellings of the boolean literals are no longer allowed, but they are so pervasive in the wild that a compliant parser would have a hard time reading many documents.
	- **Non-string keys:**
	  ```YAML
	  flush_cache:
	    on: [push, memory_pressure]
	    priority: background
	  ```
	  ```JSON
	  {
	    "flush_cache": {
	      "True": ["push", "memory_pressure"],
	      "priority": "background"
	    }
	  }
	  ```
		- > While keys in json are always strings, in yaml they can be any value, including booleans. Combined with the previous feature of interpreting `on` as a boolean, this leads to a dictionary with `true` as one of the keys.
	- **Surprise numbers:**
	  ```YAML
	  allow_postgres_versions:
	    - 9.5.25
	    - 9.6.24
	    - 10.23
	    - 12.13
	  ```
	  ```JSON
	  {"allow_postgres_versions": ["9.5.25", "9.6.24", 10.23, 12.13]}
	  ```
		- whoops! half of these are now numbers instead of version strings
	- **Directives:**
	  ```YAML
	  %FOO bar baz 
	  ```
		- the `%` makes this a [directive](https://yaml.org/spec/1.2.2/#68-directives), so it will be ignored with a warning
		- there are two directives that actually do something, boh rather esoteric:
			- [`%YAML` directives](https://yaml.org/spec/1.2.2/#681-yaml-directives) specify the YAML version
			- [`%TAG` directives](https://yaml.org/spec/1.2.2/#682-tag-directives) establish a shorthand name for specifying [node tags](https://yaml.org/spec/1.2.2/#node-tags)
	- **Nulls:**
		- [`~` is a valid way to spell `null`](https://yaml.org/spec/1.2-old/spec.html#id2805071). (so are `Null` and `NULL`)
	- **Complex mapping keys:**
	  ```YAML
	  # I, uh, _what_?
	  ? - Detroit Tigers
	    - Chicago cubs
	  : - 2001-07-23
	  
	  ? [ New York Yankees,
	      Atlanta Braves ]
	  : [ 2001-07-02, 2001-08-12,
	      2001-08-14 ]
	  ```
		- the what does this do? [the spec](https://yaml.org/spec/1.2.2/#example-mapping-between-sequences) is not exactly helpful... well, it lets you use stuff other than strings as mapping keys. [see StackOverflow](https://stackoverflow.com/questions/33987316/what-is-a-complex-mapping-key-in-yaml).
	- **Version dependence:**
		- almost all of these footguns depend on which YAML version, which platform, and which YAML library you're working with! [here's a case](https://stackoverflow.com/questions/33168329/why-does-yaml-interpret-0777-as-511) where a correctly defined `string` is nevertheless interpreted as an octal literal... sometimes!