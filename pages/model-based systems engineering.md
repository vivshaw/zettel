---
tags: systems engineering
alias: MBSE
---

- what is it?
	- > A paradigm that uses formalized representations of systems, known as models, to support and facilitate the performance of SE tasks throughout a system's lifecycle.
	  — Caitlyn Singnam, from [[SEBoK]]
	- effectively, we move from a document-based approach to SE, to a model-based one. this gives us greater standardization and centralization. we got one complete model, that every subcomponent and subsystem can be plugged into.
	- in MBSE, we will model the system at a very high level abstraction- that of the [[functions (SE)]], [[requirements (SE)]] etc. of systems engineering
- terminology:
	- a **model** is a physical, mathematical, or other representation of a system, some part of the system, or an event or process related to it
	- a **simulation** implements a model over time
- why do we model?
	- it can give us results much faster and more simply than physical testing
	- we can leverage existing modeling tools, rather than build our own custom stuff
- models should go through [[verification (SE)]] and [[validation (SE)]], to ensure they do the thing we want and do it correctly! ()failure to do this, for example, was part of the cause of the Mars lander disaster)
- MBSE tends to use specific object-oriented modeling languages, like SysML, that provide standard modeling objects. tools like Cameo support this.
	- similar to [[UML]] and diagrams for [[object-oriented programming]]!
- MBSE is a great tool to remove "stovepiping". without MBSE, different domains of SE (reqs, behaviors, verification...) will all probably live in different places. that means they can get out of sync! with MBSE, they're all part of on single source of truth.
	- one and the same model might have many different views. this lets you re-establish nice interfaces for the domains you care about, within the model.