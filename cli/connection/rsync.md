file-copying tool
`rsync [options] src dst`

#### locally
`rsync -aAXv /home/arco/documents /backup`
	`-a` archive mode (recursive dir, symlinks, perms, mod time, user&group owners, devices)
	`-A` preserve ACLs (implies perms also)
	`-X` preserve extended attributes
	`-v` verbose


#### remote server
`rsync -avz --exclude={/home/arco/documents/trash/*,/home/arco/documents/sth/*} -e ssh /home/arco/documents user@remote:/backup`
	`-z` enable compression
	`--exclude`
	`-e ssh` connect to remote server using ssh

`rsync -avz --delete -e ssh /home/arco/documents user@remote:/backup`
	`--delete` delete files on remote server that no longer exist in src