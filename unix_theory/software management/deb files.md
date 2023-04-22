`apt`
	search, show, update, upgrade, install, list --upgradable, -y
	autoremove (package,dependecies&orphans)
	purge (package&config files)
	autoremove --purge (package, deps&config files)
	download (download without unpacking&installing)

`dpkg` - low level tool
	- `apt` use it
	- doesn't resolve dependencies
	`-L` list files provided by local package
	`-S` query package which provides file

logs: `/var/log`, `/dpkg.log`