---
tags: message queue, distsys, data, Apache
---

- unclear errors and how to solve them:
	- did you get an error like: `error while creating ephemeral at /brokers/ids/1, node already exists`?
		- this is generally caused by not respecting [[Apache ZooKeeper]]'s session expiry time. so, [add a 20 second delay between Zookeeper starting and Kafka starting](https://stackoverflow.com/a/66667725). that should be enough time to ensure everything's up and running, and any dead sessions are reaped
	- did you have trouble sending your first message?
		- make sure `KAFKA_AUTO_CREATE_TOPICS_ENABLE` (or your Kafka distribution equivalent) is `true`