tags:: software engineering, software architecture, Mark Richards

- [A treasure trove of bite-sized resources on architecture](https://www.developertoarchitect.com/lessons/)
	- I'm working few this 3-4 vids a week on Wednesdays, to fill out my understanding of architecture!
- **Lesson 1 - Event-Driven Architecture: Request/Reply Processing (posted Jan 22, 2018)** #event-driven #distsys
  collapsed:: true
	- [[request-reply pattern]] is very powerful- but it's asynchronous!
		- you can use a "correlation ID" to know which requests correspond with which replies
		- you can also use a _temporary_ queue, created from a key sent with the request:
			- ![image.png](../assets/image_1705018515144_0.png)
- **Lesson 2 - How Kafka Differs From Standard Messaging (posted Jan 29, 2018)** #event-driven #distsys
  collapsed:: true
	- [[Apache Kafka]] payloads are typically [[key-value pairs]] with atomic values, whereas "standard queues" like [[RabbitMQ]]/ [[ActiveMQ]] are typically more structured
	- Kafka streams a continuous flow of data, others have distinct, bounded messages
	- Kafka can handle throughput up to 1M messages/sec in a tuned instance, 100K/sec on an average instance. standard queues tend to handle 4K-10K throughput
	- Kafka is especially good for *operational data*- about the health of the system. standard queues are good for transactional data
	- Kafka only supports a [[pub-sub model]], standard messaging can additionally do other paradigms like [[point-to-point]] messaging, or [[exchange]] topology
- **Lesson 3 - Soft Skills: Gaining Technical Breadth (posted Feb 5, 2018)** #[[soft skills]]
  collapsed:: true
	- we're expected ti keep up with industry trends... but how?
	- think of a pyramid, topped with the stuff you know, the next level your [[known unknowns]] , and the base (and broadest!) level being [[unknown unknowns]]. *your goal is not primarily to expand the knowns- it's to move the unknown unknowns into known unknowns!*
		- you can think of your knowns as your *technical depth*, and your known unknowns as your *technical breadth*
		- as an architect, breadth becomes more important! you need some core of depth, but breadth makes the difference
	- Mark reads [InfoQ](https://www.infoq.com/), [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar), and [DZone](https://dzone.com/). 20 mins/day is enough to build the breadth. you only need to go deep on the stuff you actually decide to use!
		- don't click any of the stuff to limit it to one language or platform! you _want_ to see stuff you don't know about!
- **Lesson 4 - Microservices: Distributed Logging (posted Feb 12, 2018)** #microservices #logging #distsys
	- microservices makes the flow of an action complex to track- distributed across many logs in different services it flows through
	- even if you use tools like [[Splunk]] or [[Logstash]], that's not enough on its own!
	- two styles:
		- log consolidation: have services log out to something like Splunk, Logstash, etc. which will consolidate it together
		- log streaming: *stream* the logs to something like [[Kafka]], then use a subscriber to consolidate
			- the power is that now you can do any ad-hoc analysis you want!
	- 4 steps you need to take to make either of these work:
		- **define request context ids.** without this, we can't know what the event flow was.
		- **define a context id heirarchy**. ideally a programmatic one! generally, there's a hierarchy of events- e.g. maybe `customer_id`s are more important than `order_id`s
		- **extract the context ids.** you can do that with framework code, interceptors, etc
		- **make context ids consistent.** if different services in the flow for an event care about different IDs, then you'll lose the data you need to trace a request through the services!
			- consider making an explicit, separate `context_id` and placing it at the top of the heirarchy
	- consider a custom logging API wrapper
		- this ensures users always pass the info that's needed for good tracing!
		- also enables using filtering logic- send some stuff out to Kafka, other stuff out to Logstash- all in one place, without affecting users, across the whole org and all its services
-