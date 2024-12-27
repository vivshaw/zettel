---
tags: aws, networking
---

- **3 networking zones:**
	- the public Internet
		- accessible to all!
	- [[AWS/VPC]]s- the AWS private zone, where AWS private services like [[AWS/EC2]] operate
		- accessible from the same VPC, or other VPCs and on-prem if AWS private networking is configured
	- the AWS public zone- where AWS public services like [[AWS/S3]] operate
		- anyone can connect, but permissions are required to access