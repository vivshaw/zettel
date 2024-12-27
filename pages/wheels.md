---
tags: kinematics, robotics, engineering
alias: wheeled robot
---

- in a two-wheeled system:
	- if a wheel is not in motion and the other is, the stationary wheel acts as a pivot
	- we can define the system's x-axis displacement as $\Delta x = \dfrac{r \Phi_l}{2} + \dfrac{r \Phi_r}{2}$, where $r$ is the wheel radius and $\Phi$ is the amount of rotation of each wheel
	- we can calculate the angle the robot rotates as $\omega_z = \dfrac{r \Phi_r - r \Phi_l}{d}$, where $d$ is the distance between the wheels