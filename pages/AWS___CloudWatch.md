tags:: aws, cloud

- collects and manages operational data, such as logs
- you can namespace stuff in CloudWatch
- 3 parts:
	- **Metrics**
		- a collection of related data points in time series
		- **dimensions** are key/value pairs for each datapoint
	- **Logs**
		- it is a **regional** service
		- it is an **AWS public** service- can use from AWS, or on-prem
		- you can use it to store, monitor, and access logs
		- can generate metrics by filtering down logs
		- organized into **log streams**, an ordered stream of logs from one particular source. e.g., one specific EC2 instance
		- log streams are organized into **log groups**, a group of log streams from one particular *type* of log source. e.g., EC2 as a whole
			- this level is where set set retention and permission settings
			- it's also where we can filter logs into a metric
	- **Events**
- can use **alarms** to trigger actions in other AWS services