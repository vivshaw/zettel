---
tags: math, complex numbers
---

- the **complex roots of unity** for a number $n$ are the numbers $z$ for which $z^n = 1$
	- for every integer $n$, the $n$ roots of unity are $z_k = e^{2\pi i k / n}$ for $k = 0, 1, ..., n-1$
	- geometrically, they are evenly spaced points around the complex unit circle. like a regular $n$-gon inscribed in the unit circle.
	- you can also think of $\omega_n = e^{2 \pi i / n}$ as a generator. where the complex roots are $1, \omega_n, \omega_n^2, ..., \omega_n^{n-1}$
	- when even, $\omega_n^2 = \omega_{n/2}$
	- for any $k$, $\overline{\omega_n^k} = \omega_n^{n-k}$. or in English, "reflecting across the real axis is the same as walking $k$ steps backwards"