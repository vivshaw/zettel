---
tags: networking
---

- a DNS server exists to convert hostnames to IP addresses.
	- we use this instead of manually specifying hostnames, e.g. in `/etc/host`
- on Linux:
	- we can see DNS config at `/etc/resolv.conf`, in which we specify nameservers
	- we can specify precedence between DNS and local hosts file in `/etc/nsswitch.conf`
- We can query DNS info with [[nslookup]] or [[dig]]
- Record types:
	- An [[A record]] maps a hostname to an IP address
	- A [[CNAME]] maps a hostname to another hostname
- there are 13 DNS root servers in the world!
- [[IANA]] manages he root zone, and 12 large orgs run the root servers