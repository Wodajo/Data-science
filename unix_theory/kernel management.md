###### kernel panic
common casues:
	- faulty hardware e.g. overclocked CPU, bad RAM or video card
	- faulty update
		when you upgrade a system, the `old kernel is kept as backup` and you can restore it if things go wrong
		-> In GRUB menu select other kernel, boot and reainstall faulty one
in worse case scenario - boot using usb stick to retrieve data

###### kernel modules
`/etc/modules` - file for manual selecting a module to load **at boot time**
	enter a name of a module there
	it will also load dependencies
`/etc/modprobe.d/` - create a *.conf* file inside with a module to blacklist it (no loading **at boot**)

`lsmod` - list loaded modules
`insmod` - insert modules into running kernel
	- full path to module to install
	- no dependency check
	- fail with no explanation
`modprobe` - insert modules into running kernel
	- only name of dependency need to install
	- check dependencies in dependencies map -> we need to run `depmod` before to create a list of dependencies
	- is a wrapper for `insmod`
`rmmod` - remove modules from runnig kernel


