Redundant Array of Independent Disks - combine physical disk drives/partitions into logical storage unit
	- data is distributed across the drives in several ways called `RAID levels`
	- `RAID level` can prevent *data loss*, increase *performance* or sth in between

-   **RAID 0**: data spread across multiple disks -> `increasing performance`
	- BUT if one disk fails, all data is lost.

-   **RAID 1**: data mirrored (copied) across multiple disks -> data `redundancy` & fault tolerance
	- BUT reduced capacity

-   **RAID 5**: data across multiple disks, with distributed parity data that allows for `recovery from a single disk failure`
	- at least 3 drives needed
	- capacity reduced by 1 drive worth of storage

-   **RAID 6**: similar to RAID 5, but uses two sets of parity data, allowing for `recovery from up to 2 disk failures`
	- at least 4 drives
	- capacity reduced by 2 drives worth of storage

-   **RAID 10**: combines the features of `RAID 1` (mirror disk ->` redundancy` but reduced capacity) and `RAID 0` (`performance` increase) 


### configuration
**storage devices might slightly differ in size (despite x GB declaration)**
	->  that's why you should create slightly smaller partitions for sake of RAID
	(instead using raw devices)

###### build
`fdisk /dev/sdb2` - you could use a "Linux raid auto" partition type
	(this is not a format. It's just a hint for system)
create as many devices as you want

`mdadm --create --verbose /dev/md0 --level=5 raid-devices=3 /dev/sdb2 /dev/sdc2 /dev/sdd2`
	`mdadm` - multiple devices administration program, use `md` driver
	`/dev/md0` - RAID partition name aka `RAID array`
	`--level=5` - RAID 5
	`raid-devices=3` - 3 partitions used (and listed behind)
this build `RAID array`

`cat /proc/mdstat` - "multiple devices status" - status info of all Linux RAID devices
`mdadm --detail --scan >> /etc/mdadm.conf` 
	`mdadm --detail --scan` - shows configuration of current `RAID array`
now `md0` is created every time we boot system

You can now use `md0` as any other drive
	e.g. `mkfs.ext4 /dev/md0` -> `lsblk` (just to look at it) -> `/etc/fstab`