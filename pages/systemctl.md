tags:: linux, utils

- use `systemctl daemon-reload` after editing a service definition! if you don't, it won't take effect
- wanna know the current runlevel? use `sysetmctl get-default`
- `systemctl list-units --all` will tell you everything that's loaded