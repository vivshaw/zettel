---
tags: robotics, engineering
---

- a refinement of [[proportional control]]. PID control factors in not just the current error, but the integral and derivative of the error.
	- given the time $t$, error at that point in time $e(t)$, and weights for each of the PID factors $K_p$, $K_i$, & $K_d$, we calculate:
	- **P** -  a term proportional to error, $K_p\ e(t)$
	- **I** - a term proportional to the integral of error, $K_i\ \int_0^t e(t)dt$
		- in practice, when there's an integral, the robot would have to overshoot to reduce it to 0! we can prevent this with **integral windup prevention**, which is a fancy way to say "only integrating the past short window in time"
	- **D** - a term proportional to the derivative of error, $K_d\ \frac{d e(t)}{dt}$
	- then we sum up, $P + I + D$
- conceptually:
	- P represents how far off we are
	- I represents how that error changed in the past
	- D represents how quickly that error is changing right now
- we tune the PID control by tuning the weights for each factor. one way to do that might look like this:
	- start with *only* the P term. raise $K_p$ until you see the bot start to oscillate. then, reduce it a bit until it's stable again. there will still be steady-state error, though!
	- add in the I term. increase it until any steady-state error is removed. but back off if there's overshoot!
	- add in the D term. increase it to make the system's response faster, but back off if oscillations or overshoot happen.
	- continue to fine-tune in response to the behavior you observe.