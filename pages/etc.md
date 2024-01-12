tags:: linux, FHS

- `/etc` stores host-specific system-wide configuration files.
- It should contain static config files, and no binaries.
- some particular files of interest:
	- `/etc/hosts` - used to configure hostnames
	- `/etc/resolve.conf` - used to configure DNS
	- `/etc/nsswitch.conf` - used to configure name resolution priority
	- `/etc/network/interfaces` - used to configure how your system connects to the network
	- `/etc/fstab` - holds info on static filesystems
	- `/etc/machine-id` - holds a stable identifier for the machine
		- [per docs](https://www.freedesktop.org/software/systemd/man/latest/machine-id.html) on machine images, this file should be blank!