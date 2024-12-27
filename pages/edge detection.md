tags:: computer vision, math

- we can detect edges via convolution, using what's called a Sobel [[kernel]]:
	- $s_x(x, y) = \begin{pmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{pmatrix}$ (for vertical edge detection)
	- $s_x(x, y) = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & 1 \end{pmatrix}$ (for horizontal edge detection)
	- conceptually, this works because if the pixels in the region have similar values, they'll largely cancel out. but if they differ a lot across the axis where the kernel differs, they'll create large values