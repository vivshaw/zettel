---
tags: SRE, performance
---

- [from Brendan Gregg](https://www.brendangregg.com/usemethod.html), a method for analyzing the performance of any system. stands for Underutilization, Saturation, and Errors. for every resource in the system, check those three things.
	- treat it like the emergency checklist for a flight system. the point is to be simple, straightforward, complete, and fast.
	- utilization: how much of the time was your resource servicing work? a percentage
	- saturation: to what degree was the resource unable to service work? as a queue length
	- errors: how many errors were observed? as a count
- it can be helpful to start with a generic list of resources for the sort of system you're working on. e.g., is it a server? OK, computer parts list.
- alternatively, it can be helpful to use a [[functional block diagram]] to inventory your resources.