---
tags: sensors, robotics, electronics
---

- we might start with simple **reflection**
	- a common way to do this is with a light emitter-receiver pair, relying on the nonlinear reduction in intensity we'll have as a light moves farther away.
	- we could also project a known visual pattern, then measure the amount of bending we see in that pattern to determine not just how far away the structure is but what type of structure it is. the Kinect does something like this
- we can also use **phase shift** - we modulate the amplitude of a light with a wavelength greater than the maximum distance we want to measure, then compare the phase of the light emitted with the light returned
- or, **time-of-flight** - measuring how long it actually takes the light to reach the destination
- we can also measure distance with sound, using an ultrasound emitter-receiver pair
	- ultrasound is generally less accurate, measuring distance in a 20-degree or more arc. this can be desirable, as it allows one to detect small objects without directly moving a beam over them
- or with a laser, relying on the phase shift in a sweeping laser beam. this is what [[LIDAR]] does.
- [[radar]] may also be used. this has the advantage of penetrating through clouds, fog, rain, and other conditions that limit visibility