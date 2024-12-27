---
tags: safety, robotics
---

- **active safety** involves controlling the robot in ways that avoid harm.
	- you might do this by controlling the voltage of all actuators, combined with a dynamic model of how much force the robot _should_ be applying
	- or, you might apply a load sensor at each joint, to measure the force directly
	- you'll need to combine this with estimates of the force the robot should be applying in normal operation
- **passive safety** involves steps to limit unsafe behavior **without** controlling the robot
	- for example, cushioning the robot
	- or using actuators that _can't_ apply too much force
	- or, failsafe braking mechanisms that will still stop the robot safely during power failure