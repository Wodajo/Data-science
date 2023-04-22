
`ps aux` == `ps -ef` - print all processes on the system
`top`

#### background processes
`jobs` show processes running background
```
[1]  + running    xlogo
```
`fg $1` foreground job 1 & send `CONT 18`
ctl-z -> `TSTP 20` + &
`bg $1` background job 1 & send `CONT 18`


#### log-out persistence
When logging out `HUP 1` (hang up) signal is sent
to keep background jobs running use `nohup`

`nohup program &`


#### kill
`HUP 1` - hang up signal to process
`INT` `2` - interruption request to process (`ctl+c`)
`QUIT` `3` - quit request to process (`ctl+d`)
`KILL` `9` - immediate termination to **kernel** (cannot be ignored)

`TSTP` (terminal stop) `20` - stop request to process (`ctr+z` -> `TSTP` + &)
`STOP` `19` - stop request to **kernel**

`CONT` `18`- restore process request after `TSTP` or `STOP` to **kernel** (80% sure) (sent by `fg` and `bg`)