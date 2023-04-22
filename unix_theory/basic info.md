`kernel` - program between hardware and software
	- controls all hardware components (e.g. CPU, memory, devices) via `device drivers`
	- start processes and assign resources
	- manage conflicts between processes
	- optimizes the utilization of common resources (e.g. CPU & cache usage, file systems, and network sockets)

`init` - first process started by the kernel
	- create processes
	- determines how the system should be set up in each `runlevel` (`sysV`) aka `boot target` (`systemd`)
	- starts all background process after setting default `boot target` for the system
	- automatically adopts all `orphaned processes`
there was `system-v` than `upstart`. Now `systemd` is the `init`


`kdump` - write all your memory to hard drive - in case of kernel crash.
You might care in cases of custom kernels developing



###### Tings to consider (reealy basic)
- hardware
	- boot installation media (CD ROM, USB, floppy, hard drive)
	- how much RAM and HDD/SSD?
	- devices needing drivers (video card? wifi card? printers? scanners?)
- time
  quartz crystals are piezoelectric -> can oscillate with adjusted frequency BUT each crystal is a little different -> necessity for network time arise
	- localtime (windows) or UTC? (UTC on linux - know where you are -> know what time is there via network)
- software
	- minimal install - for security sake
	- package management
		  "regular" from selected repos
		  build form source code (can be better optimised for given hardware)
		  appimage/flatpak (for many versions of software and stability)
- partition
	- bootloader should be at the beggining part of hard drive
	- SWAP partition - if RAM is full it allows using hard drive as RAM, needed for hibernation
	- RAID (Redundant Array of Independent Disks) - technology that combines multiple disk drive components (typically disk drives or partitions thereof) into a logical unit.
		  Data is distributed across the drives in one of several ways called [RAID levels](https://wiki.archlinux.org/title/RAID#RAID_levels), depending on the level of redundancy and performance required. The RAID level chosen can thus prevent data loss in the event of a hard disk failure, increase performance or be a combination of both
	 - LVM (Logical Volume Manager) - abstract your storage and have "virtual partitions", making extending/shrinking easier.
		 You can combine several hard drives (physical volumes) into one volume group which can be made into logical volume (virtual/logical partition) that can be fromatted with file system.
		 That way you can create small partition and "dynamically" resize them as they get filled up, or add new hard drive and extend logical partiton easly
	- file systems - controls how data is stored and retrieved
		journaling - logging changes before committed to fs -> can **automatically** rapair the folders/files on disk using info stored in a log
			Copy-on-write fs (like Btrfs and ZFS) have no need to use traditional journal to protect metadata, because they are never updated in-place
			Although Btrfs still has a journal-like log tree, it is only used to speed-up `fdatasync/fsync`
		- btrfs - modern copy on write (CoW) filesystem for Linux, not really stable
		- ext4 - Linux fs
		- ZFS - owned by Oracle
			- pooled storage (integrated volume management – zpool)
			- [Copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write "wikipedia:Copy-on-write")  [snapshots](https://en.wikipedia.org/wiki/Snapshot_(computer_storage) "wikipedia:Snapshot (computer storage)")
			- data integrity verification and automatic repair (scrubbing)
			- [RAID-Z](https://en.wikipedia.org/wiki/RAID-Z "wikipedia:RAID-Z")
			- a maximum [16 exabyte](https://en.wikipedia.org/wiki/Exabyte "wikipedia:Exabyte") file size, and a maximum 256 quadrillion [zettabyte](https://en.wikipedia.org/wiki/Zettabyte "wikipedia:Zettabyte") storage with no limit on number of filesystems (datasets) or files
		- FAT - family of fs supported by nearly all systems - good for data exchange
			- `mkfs.fat` supports creating FAT12, FAT16 and FAT32
		- NILFS2 - raw flash devices, e.g. SD card
		- NTFS - Microsoft fs
		- XFS - high-performance fs
	- networking
		- DHCP for client
		- manual config for servers (AD, DHCP, DNS needs manual config)
	- Users
		- root & administrators (wheel or sudo group)
		- 
	- 

