tags:: db

- databases that store their data in a [[graph]] format
- examples: [[Neo4j]], [[Datomic]], [[RethinkDB]]
- [[schema-on-read]]
- two types of data model:
	- **property model:** stores data in edge and node objects:
		- a node contains a unique ID, a collection of properties, and a set of incoming and outgoing edges
		- an edge contains a unique ID, a collection of properties, a tail and head (from and to) vertex, and a label to describe what type of relation it is
		- this lets you store several types of relation in the same DB while keeping the data clean
		- [[Neo4j]] is a DB like this, and [[Cypher]] a query lang like this
	- **triple-store model:** stores data in a triple format like: `subject, predicate, object`
		- in this way, kinda related to [[logic programming]] like [[Prolog]]!
		- the [[semantic web]]/[[RDF]] is like this, and [[Turtle]] and [[SPARQL]] are query langs like this
		- [[Datalog]] is also _kinda_ like this