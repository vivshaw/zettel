tags:: data, distsys, db

- a [[replication]] strategy in which there are no leaders. writes are given to all nodes directly
- what happens when a node is down while a write is sent? when it comes back up, that data will be missing!
	- **read repair:** a client fetches data from several nodes at once, and relies on version data to determine which is newest
	- **anti-entropy process:** a background process runs to detect node differences, and synchronize them
		- unlike a replication log, there is lo log of writes to compare against. this compares the live data from nodes
- you can set a **quorum** to ensure fresh data is fetched- require at least *w* writes to succeed, and query *r* nodes for each read. if  *w* + *r* > the number of nodes, we guarantee no read will have stale data
	- you can choose lower *w* and *r* for lower latency, but allowing the possibility of stale data
	-