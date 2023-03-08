file-copying tool
`rsync [options] src dst`

#### locally
`rsync -av /home/arco/documents /backup`
	`-a` archive mode (recursive dir, symlinks, perms, mod time, user&group owners, devices)
	`-v` verbose


#### remote server
`rsync -avz -e ssh /home/arco/documents user@remote:/backup`
	`-z` enable compression
	`-e ssh` connect to remote server using ssh

`rsync -avz --delete -e ssh /home/arco/documents user@remote:/backup`
	`--delete` delete files on remote server that no longer exist in src