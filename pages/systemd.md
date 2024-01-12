tags:: linux

- [official docs](https://systemd.io/)
- use [[systemctl]] to control services, and [[journalctl]] to view the logs for a service
- define services in `/etc/systemd/system`
	- services can be configured to restart on failure with the `Restart` directive
	- use a `Unit` block to define a dependency on another service
-