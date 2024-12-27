---
tags: aws, software engineering, cloud
---

- an **AWS account** is a container for **identities** and **resources**
- each account has a root user, which has access to everything.
	- the root user cannot be restricted!
	- practice good security by: #nuggets #security
		- securing the root user with [[MFA]]
		- not using it! create an [[AWS/IAM]] user with admin privileges, and use that for day-to-day work
- a company might have multiple AWS accounts. if so, they can combine them within an [[AWS/Organization]]
- you can set up an [[AWS Budget]] on an account to alert you of spending crossing overall thresholds