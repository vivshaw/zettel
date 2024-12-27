---
tags: robotics, engineering
---

- a technique where we adjust a control variable proportionally to the error between our target value, and the current value.
- for a mobile robot on a 2D plane, that might be as simple as calculating the angle and distance in a [[Euclidean space]]. then, calculate a velocity $v$ and steering angle $\omega$ by multiplying each by a **gain constant** to each (say, $0.2$).
	- if we have a [[wheeled robot]], we can work backward from there to the desired wheel speed for each wheel: $v_l = v - (\omega * d/2)$, $v_r = v + (\omega * d/2)$
		- we can safely drop the $d$ by factoring it into our gain constant for $\omega$