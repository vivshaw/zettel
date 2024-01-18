tags:: distsys, db

- in an eventually-consistent replica set, how can we ensure that when a user writes data and reads back, they see it?
	- could use a principle like "anything the user _can_ edit, read from the leader. everything else, read from a follower". but that only works if only a subset of the data is editable by the user
	- could instead track a timestamp for each item of last update, and ensure that all reads for x amount of time after come directly from the leader
	- could instead have the _client_ remember the timestamp of its most recent write. then, when reading from a follower, can check if it's been update up until that timestamp, and read from the leader if not
	- this gets even harder if you need _cross-client_ consistency- e.g., "something I wrote on mobile should be visible on web". then you need to centralize timestamp metadata if you use an approach with that, or ensure all reads go to the same datacenter if you use a read-from-leader approach