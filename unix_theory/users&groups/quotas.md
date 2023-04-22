`quota` - kwota of hard drive that user/group can use
	`soft limit` - warning "you've gone over limit" by email
	`hard limit` - you can't write to disk anymore

`vi /etc/fstab`
```
/dev/sdb1 /mnt/disk ext4 default,usrquota,grpquota 0 0
```
add `<options>`
	`usrquota` management for user quota
	`grpquota`  management for group quota
`reboot` - for changes to take effect
`mount` - to check if options are as expected (compulsively)

`sudo quotacheck -aug` - scan drive for files own by user/group
-> updates `aquota.user` & `aquota.group`
	- important to run initially
	`-a` all partitions supporting quotas
	`-u` user own files
	`-g` group own files
`ls /mnt/disk/`
```
aquota.user  # shows files on a drive and who owns them
aquota.group  # as above, in groups context
```
`sudo quotaon -a`
	`-a` for all partitions supporting quotas

`tune2fs -l /dev/sdb1 | grep "Block size"` - to check how many **[bytes] are in one block**
	e.g. 4096 [bytes] = 4 KiB [kibibytes]
`sudo edquota arco` - shows all fs supporting quotas
	we can set up quotas for:
		`inodes` - how many files a user can store (not really usefull)
		`blocks` - how many blocks of data
```
Disk quotas for user arco (uid 1000):
Filesystem         blocks    soft    hard    inodes    soft    hard
/dev/sdb1               0     500    1000         0       0       0
```

