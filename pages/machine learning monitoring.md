tags:: ml, mlops

- via [[Andrew Ng]], techniques you may use:
	- a monitoring [[dashboard]], to visually track a bunch of metrics you might care about:
		- software metrics: memory, compute, latency, throughput, load
		- input metrics: characteristics of the input values, to ensure the distribution hasn't changed
		- output metrics: how often do you get no result? how do users interact with it? determine whether the outputs are still accurate
		- deployment is iterative, just like the modeling process! it usually takes multiple tries to get the right metrics down.
		- think about how quickly the data can change! user data, like names and addresses, tends to change slowly. enterprise data, like biz purchases, can be faster. but there can always be unexpected change too!
	- pipeline monitoring- you'll want to monitor not just you model, but the other stages that feed into it or take output from it.