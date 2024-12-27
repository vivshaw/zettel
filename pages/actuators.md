tags:: engineering, robotics, electronics

- **motors** tend to rotate
	- electric motors use electromagnetism to force a shaft to rotate
		- AC motors use the alternation of [[AC current]] to do this at the frequency of the current.
		- DC motors are most often **brushed DC motors**- they use **commutators**, brushes that intermittently apply current, to artificially swap the polarity. as the motor rotates, sometimes it is in contact with one brush, sometimes the other. this causes the polarity swap.
			- DC motors are the most common in robotic systems
		- there are also **brushless DC motors**, which instead use sensors to determine the rotor's position, then switch the polarity accordingly.
	- stepper motors can do this in discrete steps!
	- **motor controllers** are needed to make motors useful, by translating the digital control signals into motor current. [[transistors]] are used to boost the control signal, and [[diodes]] are used to ground the reverse voltage from the coils
	- servo motors come packaged with gears, encoders, and control electronics, letting you control them precisely. this makes them more useful for many robotics purposes, especially in [[closed-loop control systems]]
- **linear actuators** apply force in just one direction
- **hydraulic** and **pneumatic** actuators also exist, and are commonly used in legged robots. they are linear actuators that operate by pumping fluid into a container. hydraulics tend to be more powerful, but bulkier.
- exotic actuators like **shape-memory alloys** also exist, which change their shape in response to heat, or **electro-active polymers** which change size or shape in response to electricity. these are very inefficient though