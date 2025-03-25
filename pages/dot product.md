---
tags: math, linear algebra
---

- a dot product is basically multiplying the elements of two vectors elementwise, then summing.
	- $u \cdot v = \sum^{n}_{i=i} x_iy_i$
- in a Euclidean space, we think about the angle $\theta$ between those vectors
	- $u \cdot v = \lvert\lvert u \rvert\rvert\ \lvert\lvert v \rvert\rvert\ cos(\theta)$
	- this can be interpreted as projecting $u$ onto $v$, then multiplying their lengths
- in a sense, [you can also think of the dot product as a measure of similarity](https://tivadardanka.com/blog/how-the-dot-product-measures-similarity).
	- if the two vectors are orthogonal, it will be 0. if the two vectors are identical, it will be the square of the vector's magnitude.
	- think of the geometric interpretation! the closer to 0 the angle distance is, the closer to 1 the $cos$ is. then, we multiply in the magnitudes.
	- if your dataset is normalized, this is identical to [[cosine similarity]]