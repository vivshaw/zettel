tags:: ml, mlops

- from [[Andrew Ng]], software issues you might confront when taking a model to deployment:
	- do you need realtime inference, or is batch processing OK?
	- will you run in the cloud, or on the edge?
	- how much compute do you need?
		- CPU?
		- GPU?
		- RAM?
	- what are your [[latency]] and [[throughput]] requirements?
	- [[logging]]
	- security and privacy
- common deployment cases:
	- greenfield development, new use case
	- automating or assisting with an existing manual task
	- replacing or upgrading an existing ML system
- common deployment patterns:
	- **[[shadow mode]]** - deploy the model alongside human judgment, and just go with the human's result. use this to gather data on how [[accurate]] the ML system is relative to human judgment. makes sense when automating a manual task or comparing to an older system
	- **[[canary deployment]]** - roll out model to only a small fraction of traffic, and up the ratio if it goes well. lets you spot issues early on.
	- **[[blue-green deployment]]** - two versions are live at a time behind a router. the old version, Blue, is prod. the new one, Green, is not. when you're ready to deploy Green, you just swap the traffic over to it.
- think about degrees of automation: none -> shadow mode -> AI assistance -> partial automation -> full automation. these are all valid solutions for particular purposes.