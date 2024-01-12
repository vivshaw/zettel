tags:: aws, cloud, vm

- an Amazon Machine Image is a VM image for use on AWS.
	- not so different from a QEMU image, etc. etc.
- you can create an AMI from an [[AWS/EC2]] instance, or vice-versa
- permissions options:
	- **public:** anyone can launch it
	- **implicitly private:** owner can implicitly launch it
	- **explicit allow:** let specific AWS accounts launch it
- image contains:
	- root volume
	- block device mapping