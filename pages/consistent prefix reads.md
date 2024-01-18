tags:: distsys, db

- suppose you say something, and i reply. it would be odd if someone saw my response before the thing i responded to! we want to make sure that never happens, by ensuring that if a sequence of writes happens in a particular order, everyone reading will see them in that same order
	- this gets much harder with [[sharding]]!
- can ensure that writes are applied in a deterministic order
- if sharded, can ensure that related writes happen on the same shard