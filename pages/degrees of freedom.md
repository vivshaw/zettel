tags:: robotics, engineering, kinematics
alias:: DoF

- how many ways can something move? e.g., a jet plane has 6: its x/y/z coordinates, and pitch/yaw/roll
- when it comes to rotations, **order matters**- the same rotations in different sequence may lead you to a different pose
- you can think about degrees of freedom either in **cartesian space** or in **actuator space** (at the joints). these numbers can differ!
	- e.g., there are more ways to bend and move your arm than there are cartesian DoF. there are redundant ways to get you hand into a particular pose
	- or, a robot that can only move forward and turn has only 2 DoF in actuator space, but can move and orient anywhere on the 2D Cartesian plane, so 3 DoF