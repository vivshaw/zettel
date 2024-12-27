---
tags: data, distsys, db
---

- src:
	- mostly, [[DDIA]]
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
- how do you create a new follower, and ensure it has accurate data? can't lock the DB- that would mean you lose HA. instead:
	- take a consistent snapshot of the DB at some point in time, associated with a position in the leader's replication log- [[MySQL]]'s "binlog coordinate", [[PostgreSQL]]'s "log sequence number"
	  logseq.order-list-type:: number
	- copy the snapshot to the new follower
	  logseq.order-list-type:: number
	- once the follower spins up, it connects to the leader and requests all data changes since the snapshot was taken
	  logseq.order-list-type:: number
	- when the follower has processed the backlog, it is caught up. it can now process data changes live, as they happen
	  logseq.order-list-type:: number
- how do you maintain availability when there are outages?
	- if a follower fails, *catch-up recovery*- the follower keeps a log of the data change it receives from the leader, so that when it crashes and restarts, it can just catch up from the point it left off
	- if a leader fails, *failover*- determine that the leader has failed, pick a new leader from among the followers, then reconfigure the system to use the new leader.
		- failure modes:
			- if async replication is used, the new leader might not be caught up with the old one! what then happens if the old leader rejoins and has data the rest of the reps don't? most commonly, it gets discarded
			- discarding writes is dangerous if you need to maintain synchronization with systems outside the DB! e.g., losing data when using an autoincrementing ID might lead to duplicate data!
			- if two nodes both think they're the leader, your cluster has a split brain!
			- how long should the timeout be to declare the leader down? if too long, your MTTR drops. if too short, your leader might get killed under normal load spikes, _worsening_ availability!
- how do replication logs work?
	- **statement-based replication:** every SQL statement that is run on the leader gets sent to the followers. [[MySQL]] used to use this. this sounds simple and straightforward, but it ain't:
		- this leads to desync if any of the statements are nondeterministic! `now()`, `rand()`, etc.
		- if you use autoincrementing fields, you need to ensure the statements run in the eact same order on all nodes
		- if the statements trigger side effects, need to make sure _those_ aren't nondeterministic as well
	- **WAL shipping:** many DBs already log their intended writes to disk, in a [[write-ahead log]]. we could just use that! [[PostgreSQL]] and [[Oracle]] do this
		- the log is very low-level though- so it ties the data closely to the storage engine. that can cause problems when doing a version upgrade, if the system can't run multiple versions of the engine in parallel
	- **logical replication** aka **row-based:** use a separate log format for the replication, dedicated to that purpose. describes the data at the granularity of the row insert/update/delete level, not the low level of a WAL. [[MySQL]] works this way now.
		- this is more decoupled from the storage engine, so more easily back-compatible
		- this is also easier for external apps to parse!
	- **trigger-based replication:** maybe you want to replicate just some subset of the data, or otherwise move replication up into the application layer? then you could use [[stored procedures]] to replicate on your command
- problems with leader-based replication:
	- in practice, you can only really scale this if you go async. but in that case, if the application reads from an async follower, they may get outdated data! the cluster is only [[eventually consistent]]- at any given moment, real nodes will be varying degrees of desynced.
		- if a user triggers a write (to the leader) then reads back (from a follower), they may not yet see the data they wrote! so it'll look like it failed! then, we need [[read-after-write consistency]]
		- we also don't want users to see stuff moving backwards in time- so, we need [[monotonic reads]]
		- we also want to ensure that actions happen in temporal order- so, we need [[consistent prefix reads]]
- in some cases, you might want replicas of leaders as well as followers- an [[active-active]] replication. each leader is a leader, but also acts as a follower to the other leaders.
	- e.g. maybe you have multiple datacenters, and want to be able to survive the outage of an entire datacenter.
	- this increases write performance, outage tolerance, and network problem tolerance
	- but it adds the massive problem of conflicting writes!
	- an app that is available offline is effectively just a multi-leader replication where the local DB and the remote backend are both leaders! #nuggets
	- an app with collaborative editing are much like a multi-leader replication where each local document state and the remote backend are all leaders! #nuggets
- one strategy for dealing with conflicts is to avoid them! ensure all writes for a given record go through the same leader