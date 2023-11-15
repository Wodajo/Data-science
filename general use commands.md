  `vmstat` - info about mem,cpu,io,swap
`  nohup command 2> error.log`

#### so as to pipe
```
 celldweller.xspf
'Imagine Dragons - Bones (Official Lyric Video).mp3'
'The Glitch Mob - Drink the Sea (10 Year Anniversary Full Album Visual).mp3'
'yt1s.com -Celldweller Wish Upon A Blackstar Full Album HD.mp3'
'yt1s.com - Scandroid Scandroid Full Album.mp3'
```
into `file` (program) use:
`find . -print0 | xargs -0 file`

### open ports
`ss -lntu`
	`-l` listening sockets, `-n`  show port nr, `-t` TCP, `-u` UDP

### git
`git config --global user.name "Username"`
`git config --global user.email "your@mail.bycz"`
`git config -l`
`git config --global credential.helper cache`
`git config --global --unset credential.helper`

set `vimdiff` as default merge tool
`git config merge.tool vimdiff`
`git config merge.conflictstyle diff3`
`git config mergetool.prompt false`

``` nottested
`git mergetool`
	LOCAL - file from current branch
	BASE - common ancestor
	REMOTE - file you're merging into your branch
	MERGED - what gets saved in merge commit

`git checkout --ours local_filename` use this
`git checkout --theirs remote_filename` or use this
`git add chosen_filename`
`git commit`
```
### printing settings
`system-config-printer` (gtk gui)
`127.0.0.1:631` CUPS web interface

### Mic & speaker
`alsamixer` - F5 for all devices
`pavucontrol`

### keymaps
list keycodes
`dumpkeys -l`
you can remap keycodes
e.g. switch `CapsLock` with `Escape` (for nvim)
```
keycode 1 = Caps_Lock
keycode 58 = Escape
```
be carefull with gamesxD (it's probably better to just remap nvim keybindings)
`loadkeys /usr/local/share/kbd/keymaps/personal.map`

### tar
`tar -cvf ARCHIVE_NAME WHAT_TO_PUT_THERE`
`-c` create

`tar -rvf ARCHIVE_NAME WHAT_TO_APPEND`

`tar -tf ARCHIVE`
`-t` list

`tar -ztf ARCHIVE`
`-z` passes through gzip -> can list even compressed archives

`tar -xf ARCHIVE`
`-x` extract archive. Autodetect compression type

### 


