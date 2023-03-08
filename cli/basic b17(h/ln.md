`hard links` are different "name part" pointing at the same `inode` (data part)
	hard link CANNOT:
		- point at dirs
		- point at different file system
	BUT it will persist when "name part" of original change
`symbolic link` are text pointers to the file/dir
	breaks when file renamed or moved
	"rwxrwxrwx" permissions (likely to came up when using `find` with `-perm` flag)


`ln` - create `hard link`
```
└─$ ln text text-hardlink  
└─$ ls -li
1966240 -rw-r--r--  2 kali kali     0 Jan 11 08:59 text
1966240 -rw-r--r--  2 kali kali     0 Jan 11 08:59 text-hardlink
```
1st field is `inode`, 3rd is the number of hardlinks to that file

`ln -s` - create `symlink`
```
└─$ ln -s text text-symlink
└─$ ls -li
1966240 -rw-r--r--  2 kali kali     0 Jan 11 08:59 text
1970136 lrwxrwxrwx  1 kali kali     4 Jan 11 09:03 text-symlink -> text
```
`symlink` here has 4 bytes bcos it's in the same dir as "text", and "text" is a 4byte-word