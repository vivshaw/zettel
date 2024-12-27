---
tags: aws, cloud
---

- an Amazon Resource Identifier is a unique identifier for a particular AWS resource
- valid formats
	- `arn:partition:service:region:account-id:resource-id`
	- `arn:partition:service:region:account-id:resource-type/resource-id`
	- `arn:partition:service:region:account-id:resource-type:resource-id`
- you can use wildcards, but they can be sneaky:
	- `arn:aws:s3:::catgifs`
		- this refers to just the S3 bucket, not the objects
	- `arn:aws:s3:::catgifs/*`
		- this refers to just the objects, not the buckets