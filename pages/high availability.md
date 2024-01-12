tags:: cloud, sre, distsys

- "an aim to ensure an agreed level of operational performance, usually uptime, for a higher than normal period"
- typically measured in 9's- 99.9% (3 9's), 99.999% (5 9's), etc
- from this perspective, user-facing disruption is OK as long as there is no outage/downtime
	- consider a 4x4 traveling through the desert. you might achieve HA with a spare tire and repair tools. it's OK that the journey is delayed, as long as you get the tire back on and resume travel
- might, for example, use a failover configuration
- contrast: [[fault tolerance]]