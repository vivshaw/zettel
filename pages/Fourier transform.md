---
tags: math, complex numbers, frequency
alias: discrete Fourier transform, DFT
---

- $F(\omega) = \int_{- \infty}^{\infty} f(t) e^{-i \omega t} dt$, in angular frequency (radians per second). common in physics
	- or $F(f) = \int_{- \infty}^{\infty} f(t) e^{-2 \pi i f t} dt$, in ordinary frequency (cycles per second). common in audio engineering / DSP
- one way to think of a Fourier transform, is of winding a function around the unit circle, then smoothly sliding the frequency of that winding back and forth. when the center of mass of the winding is far from $0$, that frequency is in the function.
	- $e^{ix}$
		- "go in a circle" (in the [[complex plane]], using [[Euler's formula]])
	- $e^{-2 \pi i f t}$
		- "go in a circle at frequency $f$"
	- $g(t) e^{-2 \pi i f t}$
		- "wind $g(t)$ up around the unit circle"
	- $\dfrac{1}{N} \sum^N_k=1 g(t_k) e^{-2 \pi i f t_k}$
		- "sample N points from the graph, and average them to get the center of mass"
		- (this, technically, is the **discrete** Fourier transform)
	- $\dfrac{1}{t_2 - t_1} \int_{t_1}^{t_2}=1 g(t) e^{-2 \pi i f t}$
		- "the exact center of mass of the wound-up graph"
	- $\int_{t_1}^{t_2}=1 g(t) e^{-2 \pi i f t}$
		- "the longer it persists, multiply the center of mass's distance"
- **discrete Fourier transform**:
	- given a sequence $a_0, a_1, a_2, ..., a_{n-1}$, its DFT is the sequence of $n$ complex numbers where $A_k = a_0 + a_1 \omega_n^k + a_2 (\omega_n^k)^2 + ... + a_{n-1} (\omega_n^k)^{n-1}$
		- where the $\omega$s are [[complex roots of unity]]
		- you can think of this as, treat that sequence $a$ as the coefficients of a polynomial. then evaluate it at $x = \omega_k^n$