---
tags: math, algorithms
---

- a [[divide-and-conquer]] algorithm to calculate the [[discrete Fourier transform]] in $O(n \log n)$ time, developer by Cooley and [[Tukey]]
	- suppose that you're doing a DFT where $N$ is even. split out the even and odd inputs, and recursively call FFT on each half. continue splitting until you have DFTs where $N=2$, which are trivial.
	- then you stitch them back together. you get an even part $E[k]$ and odd part $O[k]$.
		- up to the midpoint, you add them together, multiplying the odd part by a "twiddle factor" $W_N^k = e^{-2 \pi i k / N}$ that rotates it into alignment. so, $F[k] = E[k] + W_N^k O[k]$
		- above the midpoint, we take advantage of the DFT being periodic. so $F[k + N / 2] = E[k] - W_N^k O[k]$
		- that lets us "reuse" $W_N^k O[k]$, adding it in the bottom half, and subtracting it in the top half
	- the base case is trivial because for a DFT of size $N = 2$, the exponent in the DFT will simplify to $1$ when $k=0$, and to $-1$ when $k=0$. so, $F[0] = f[0] + f[1]$, and $F[1] = f[0] - f[1]$. no "twiddle factor" or multiplication required.