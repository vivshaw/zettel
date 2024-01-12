tags:: data, distsys, db

- a [[replication]] strategy:
	- one replica is designated **leader**
	- the others are **followers**.
	- write requests are sent only to the leader
		- whenever the leader writes data to its own storage, it sends the change to all followers as a *replication log* or *change stream*
	- reads can be done via any replica
- built into most [[relational DB]]s
- can be done synchronously or async
	- making _every_ follower sync is not tenable, because the whole system would break if any one node failed
	- so, a *semi-synchronous* approach is often used- make one follower sync, the rest async. if the sync one fails, promote one of the async ones to be the new sync one. that way you get up-to-date data on at least 2 nodes at all times