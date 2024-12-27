tags:: robotics

	- in order to make our robots useful, we must give them behavior that uses the inputs from their sensors to determine what to do with their actuators
	- a simple version would be **reactive control**
		- here, we tie sensor input directly to actuator output.
		- this was popularized by [[Valentino Braitenberg]]
		- it's difficult to create complex and specific behavior this way!
			- we can combine multiple reactive behaviors with a weighted sum of the inputs
	- we might also use a [[finite state machine]]