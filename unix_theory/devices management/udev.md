user-space device manager

physical events of peripheral devices -> kernel -> `sysfs` virtual filesystem -> `udev daemon` gets info about hardware -> match device agains `rules` (how to handle dev?) -> apply rules (determine `name`, `properties`&`attributes`) -> create/remove dev file in `/dev` (based on `rules`, `properties`&`attributes`)
- acts upon `peripheral detection` and `hot-plugging`
(including actions that return control to kernel)
	e.g. loading `kernel modules` or `device firmware`
- adjusting permissions of the device to be accessible to non-root users and groups
- querying dev info & monitor events
	e.g.
	`udevadm info /dev/sr0`
		`info` - query `sysfs` or `udev database`
		`/dev/sr0` DVD drive
	`udevadm monitor --environment` all events & their envs
- triggering events & test `rules`
	force dev to re-enumerate or test udev `rules`
	e.g. `udevadm trigger --action=add --sysname-match=sda` trigger "add" event on device matching "sda" name

`rules` - specify `naming`, `properties`&`attributes` of dev
	Why `naming` matters?
		- kernel module loading order is NOT preserved across boots
		- separate events handed concurrently
	e.g. storage devices are having names NOT based on mounting order, BUT sth more specific


`/etc/udev/rules/rules.d/` - place for `.rules`
`/usr/lib/udev.rules.d/` - other place for `.rules`
	if 2 files with the same name in both -> `/etc/udev/rules.d/` used
	files with lesser nr in name are loaded first

`sudo vim /etc/udev/rules.d/10-arco.rules`
```
KERNEL=="sr0", SUBSYSTEM=="block", SYM_LINK="my_dvd" 
```
`KERNEL` - what kernel knows the device as
`SUBSYSTEM` - we can look it up with `udevadm info /dev/sr0`
	every time kernel has a device `sr0` that is a `block device` rule will create symlink "`my_dvd`" in `/dev` 
`sudo udevadm trigger` or reboot