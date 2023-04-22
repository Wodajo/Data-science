CentOS uses `LVM` by default

Logical Volume Manager -	abstract your storage and have "virtual partitions", making extending/shrinking easier
	 - combine several `physical volumes` into  `volume group` -> slice into `logical volume` (virtual/logical partition) that can be fromatted with a fs
	 - you can create small partition and "dynamically" resize them as they get filled up, or add new hard drive and extend logical partiton easly

`physical volume` (`PV`) - e.g. hard drive, `RAID` device, partition
	- holds `LVM header`

`volume group` (`VG`) - simply a bucket of storage (provided by `PV`)
	**NO PROTECTION** - if sth happens with `PV` it could corrupt `VG` -> `LV` !!!
		set up `PV`s as `RAID-1`, `RAID-5` or `RAID-6`

`logical volume` (`LV`) - slice of `VG` you formatted with fs


### configuration

###### build
`pvcreate /dev/sdb /dev/sdc /dev/sdd` - create `PV`s from listed devices
`pvdisplay` - `PV`s info
i.a. `PV`s names, size, their `VG`

`vgcreate nameofVG /dev/sdb /dev/sdc /dev/sdd`
`vgdisplay` - `VG`s info
i.a. `VG` name, size, active `PV`s

`lvcreate -L 32G -n SLICE_ONE nameofVG`
`-L` size, `-n` name of `LV`
`lvdisplay` - `LV`s info
i.a. `LV` path, name size, their `VG`

You can now use new `LV` as partiton
	e.g. `mkfs.ext4 /dev/nameofVG/SLICE_ONE` & set up mounting at boot with `/etc/fstab`

###### expand
`lvextend -L+5G /dev/nameofVG/SLICE_ONE`

