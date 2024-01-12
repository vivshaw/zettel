tags:: networking

- the Open Systems Intercommunication model is a conceptual model for how networks work
	- ⚠️this is _not_ a concrete model implemented in code! it's more of a universal pattern language for networks. not every networking stack or application follows this exact structure.
- the OSI model has 7 layers:
	- **Layer 7 - Application**. this is the [[HCI]] layer, where application code accesses the network services.
	- **Layer 6 - Presentation**. this ensures the data is in a usable format. it's also where encryption occurs.
	- **Layer 5 - Session**. this maintains connections and controls ports and sessions.
	- **Layer 4 - Transport**. this transmits data with transmission protocols, such as UDP or TCP.
	- **Layer 3  - Network**. this decides which physical path the data will take.
	- **Layer 2 - Data Link**. this defines the format of data on the network.
		- Ethernet exists at this layer
		- introduces **frames** and **MAC address**
			- Preamble (56 bits), Destination MAC addr, source MAC addr, EtherType (16 bits), payload (56-1500 bytes), frame check sequence (32 bits)
		-
	- **Layer 1 - Physical**. this transmits a raw bit stream over a physical medium.
		- transmits and recieves **raw bitstreams**
		- defines things like: voltage levels, timing, rates, distances, modulation, connectors
		- no such thing as device addressing, collision detection, access control
	- layers 1-3 are called **media layers**. they deal with how data moves from point A to point B. layers 4-7 are called **host layers**. they deal with how data is chopped up, reassembled, and formatted so the other end can understand it.