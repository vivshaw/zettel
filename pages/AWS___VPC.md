tags:: aws, networking, security

- an AWS Virtual Private Cloud is a virtual private network, by default isolated from the public internet unless you say so
- you can allow a VPC to access the public Internet or the AWS public zone with [[AWS IGW]]
- you can connect a VPC to an on-prem network via VPN or Direct Connect
- VPCs are regionally resilient
- default vs. custom VPCs:
	- **default VPC:**
		- max of 1 per region
		- initially created by AWS, preconfigured
		- CIDR is always `172.31.0.0/16`
			- has one `/20` subnet in each [[AWS/Availability Zone]]
				- the subnets apply a public IPV4 address to things deployed in them!
		- has a default [[AWS IGW]], [[AWS Security Group]], and [[AWS ACL]]
	- **custom VPC:**
-