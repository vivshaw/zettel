tags:: aws, cloud, iaas

- [[IaaS]] provider, gives you virtual machine instances. you manage from the OS on upwards
- private by default
- AZ resilient
- on-demand billing, per second or hour
- instances states:
	- **running:** instance is up
		- you are changed for everything: CPU, RAM, storage, and network.
	- **stopped:** instance is termpoarily down, can be brought back up
		- you are still charged for storage!
	- **terminated:** instance is fully deleted
		- no charge
- can be provisioned from [[AWS/AMI]]s