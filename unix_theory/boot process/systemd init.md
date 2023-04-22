`boot target`
	poweroff
		- stops all running services
		- unmounts all file system -> shut down
		- `runlevel 0` in `SysV` init
	rescue
		- single-user mode
		- only the essential services started
		- file systems are mounted in read-only
		- `runlevel 1` in `SysV` init
	multi-user
		- non-graphical interface
		- networking support (network, ssh)
		- `runlevel 3` in `SysV` init
	graphical
		- starts display manager, window manager and/or desktop environment
		`runlevel 5` in `SysV` init
	reboot
		`runlevel 6` in `SysV` init

`systemd-analyze critical-chain` - check which services are started at boot + how much time it took

`systemctl get-default` - print default `boot target`
`sudo systemctl set-default multi-user.target`

`sudo systemctl isolate multi-user` - immediately switch target

### services
`.service` files are located in several folders across the system (weak)
	BUT we can still query then with `systemctl status SERVICE`

`systemctl list-units --type=service --state=running`

the rest is `sudo systemctl start/stop/enable/disable SERVICE`