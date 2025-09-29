---
tags: math
---

- the **complex conjugate** is the number with equal real part, but inverse imaginary part.
	- you can use this to simplify when dividing complex numbers. multiple the numerator and denominator by the conjugate of the denominator to reduce the denominator to a real
- we still find the distance between two complex numbers using the [[Euclidean norm]], ignoring the $i$.
	- or equivalently, we could say $|z|={\sqrt {z\cdot {\overline {z}}}}$, it's the square root of $z$ multiplied by its complex conjugate
- we can represent in a rectangular form, $a + bi$, or a polar form, $r (\cos \theta + i \sin \theta)$
	- we can convert to polar by calculating $\theta = \tan^{-1} (b/a)$ and $r = |n|$
- we can think of multiplying two complex numbers as multiplying their lengths, and adding the angles. division is the inverse- divide the lengths, subtract the angles
	- in a way, the complex plane is like $\mathbb{R}^2$ with a multiplication operation baked in. [[Euclidean space]] doesn't have a canonical way to multiply two vectors- you can [[dot product]], [[cross product]], [[Hadamard product]]... but in the complex plane, we _do_ have one way
	- this makes $\mathbb{C}$ a [[field]] - you can add, subtract, multiply, divide, etc. that's why complex numbers aren't the same thing as vectors, even though they look similar at a glance