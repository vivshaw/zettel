---
tags: os, software engineering, software architecture, persistence, complex systems, computer engineering
---

- ## 1 - The Way Houyhnhnms Compute
	- > The fundamental difference between Human computer systems and Houyhnhnm computing systems is one of point of view. [...] Whereas Humans view computers as tools below them to which they give orders and that do their bidding, Houyhnhnms view computing as an interaction within a system around them that extends their consciousness. [...] Humans articulate their plans primarily in terms of things [...] Houyhnhnms weave their conversations foremost in terms of processes [...] In short, Humans have *computer* systems, Houyhnhnms have *computing* systems.
	- what is simplicity, in programming?
		- to a human, it's when the programming language is small and well-defined. like C.
		- to a houyhnhnm, it's when the description of the _entire computing system_ is small and well-defined.
			- that includes not just the language, but compiler, OS, hardware, libraries, and everything else involved in the computation.
		- perhaps the simplest human computing system, from a houyhnhnm perspective, would be [[Smalltalk]], where the entire system is part of one pretty small specification- graphics,
- # 2 - Save Our Souls
	- to a houyhnhnm, the concept of "saving a file" is baffling. why is that? well, houyhnhnm systems automatically save data as it is changed, universally.
	- when you think about it, even human systems have automated saving, if you consider the whole system (including the human operator). it's just a highly imperfect and failure-prone automation
		- > I object to doing things that computers can do.
		  — Olin Shivers
	- why is ephemerality the default for data? why not persistence?
	- for houyhnhnms, this works via massive global backup systems and advanced cryptography.
	- what about the stuff you _don't_ want saved? this introduces unique complexity it thus has to be possible to set domain-based privacy policies about your persistence, and the UI needs to constantly make you aware of this and integrate it into normal actions.
		- programs themselves don't and can't know in which domains they run. the most they can do is create strictly-weaker domains. it is the system's job to ensure that components run in the appropriate domain. domains can be hotswapped while the program is running.
		- in fact, programs should hold so much orthogonal that a running program could be migrated to other machines! this also lets the system decide how best to run commands- what to log and what to skip, which bits of code need to be low-level optimized, etc.
	- deletion also gets more complicated. a [[soft delete]] via deindexing is simple. a true deletion requires verifying that nothing would break with the data gone, plus scrubbing all manner of logs and indexes, etc.
	- human systems have started adding an _appearance_ of persistence- autosave, tab views, history... but it's an illusion. because persistence is not at the foundation, there are huge gaps
		- in fact, the transience is fractal! each and every layer, from the operator to the programmer to the OS dev, all have to assume that data is transient, fragile, and targeted at a single computing domain. then they in turn expose the same sort of interface to the next level up.