---
tags: linux, utils
---

- [bc is `basic calculator`](https://www.gnu.org/software/bc/manual/html_mono/bc.html)- a simple calc language included in GNU
- useful for [[shell]] math
	- unlike shell, you can use good ol' parentheses the way you'd expect
	- unlike shell, supports fp arithmetic
- prefer to pipe stuff into it- `echo "1+1" | bc -l`, not `bc -l "1+1"`