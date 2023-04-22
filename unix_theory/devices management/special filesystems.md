special filesystem - doesn't reside on a physical storage device & doesn't store actual files
	- provides a way to access&manipulate various system resources
	- aka pseudo fs
	- `VFS`s are special fs BUT not all special fs are `VFS`s

virtual filesystem (`VFS`) is a software layer that allows OS to **`access&manipulate various fs as if they where a single fs`** (it's a special fs)
	info generated in real-time by the kernel & not stored on disk -> not reboot persistent
	- `sysfs` - allows user-space programs to `access`&`manipulate` various `kernel subsystems` and `hardware devices configuration` 
		used by i.a. `udev`, `dmesg`, `lshw`
	- `/proc/`
	- `/sys/` - "flashed" with `sysfs`


`/proc/` - `VFS` with processes&kernel files - contains info about `systems processes` & allow user-space programs to access&control `kernel features`
	historically it was the only one virtual fs -> for backwards compatibility contain stuff that could logically be in `/sys/`

`/sys/` - `VFS` with kernel files - allow user-space programs to access&manipulate `kernel subsytems`&`hardware dev configs`
	e.g. system's power management settings, configuration of network interfaces
	neatly orginized BUT doesn't contain that much
```
block  bus  class  dev  devices  firmware  fs  hypervisor  kernel  module  power
```


`/dev/` - special fs with device files - allow user-space programs to interact with `kernel's device drivers`
	- **NOT** `VFS` (doesn't provide a way to access different file systems)