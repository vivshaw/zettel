---
tags:: compsci, robotics
---

- a refinement of [[finite state machine]]s to support more complex behaviors.
- nodes representing behaviors are structured in a tree heirarchy.
	- some of those nodes are **sequence nodes**, which require each child node to be executed in order.
	- there may also be **selector nodes**, which are similar, but only require _one_ child node to succeed before proceeding.
	- there may be **parallel nodes**, which run all children in parallel. (or even combinations like parallel selectors)
	- there may be **decorators** that can be applied to modify nodes, like "repeat"
	- there may be a **blackboard** which is a shared data store that all nodes can access