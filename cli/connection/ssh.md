user-specific config:
- `~/.ssh/config`
```
Host MyServer
	Hostname 192.168.1.109
	Port 2222
	User kali
```
That way I can ssh usint `ssh MyServer` instead `ssh -p 2222 kali@192.168.1.109`

public key has username of its owner:>

#### tunneling
`ssh -L 127.0.0.1:8888:192.168.1.3:8080 kali@44.11.22.33`
`-L` local forward
`127.0.0.1:8080` local machine IP and port (if no IP - localhost assumed)
`192.168.1.3:8080` target to send data to
`kali@44.11.22.33` username and IP of ssh server
a.k.a
`ssh -L 8888:192.168.1.3:8080 kali@44.11.22.33`
forward from localhost:8888 (because there is nothing before 8888 - localhost assumed) (client) -> 44.11.22.33 (server) -de-encapsulation-> forward -> 192.168.1.3:8080
![local forward](local_forward.png)
ISP sees `ssh` traffic, just as 44.11.22.33. After de-encapsulation at 44.11.22.33 she'll see packets for 192.168.1.3:8080 and forward them there. 192.168.1.3 might respond, and response will be send back via `ssh`

`ssh -L 8080:localhost:80 kali@192.168.1.109`
forward from localhost:8080 (cilent) -> kali@192.168.1.109:80 (localhost:80) (server) 
e.g.
- access remote resources out of reach of client (but not out of reach for server)
- RDP job (client) -> home (server)


`ssh -R 8888:10.0.2.3:8080 kali@44.11.22.33`
`-R` remote forward
forward from 44.11.22.33:8888 (server) -> 10.0.2.2 (client) -de-encapsulation-> forward -> 10.0.2.3:8080 
![remote_forwarding](remote_forward.png)
10.0.2.3 might respond back

`ssh -R 31337:localhost:22 kali@192.168.1.109`
`-R` remote forward
forward from kali@192.168.1.109:31337 (localhost:31337) (server) -> localhost:22 (client)
e.g.
- give access to local resources (via client) to the server
- RDP home (server) -> job (client)


`ssh -D 9999 kali@192.168.1.109`
`-D` dynamic forward (creates SOCKS proxy server) - proxy server's programs require configuration  
listen on 9999 (client). When connection to this port -forward-> application protocol determine which port to connect (server)
e.g.
set up localhost:9999 SOCKS proxy on firefox (client) -> web requests are forwarded to server, answers are sent back to via ssh tunnel (to 9999)



`ssh -J 192.168.1.101,192.168.1.102,192.168.1.103 192.168.1.109`
`-J` jump, a chain of connections.


#### scp - source -> dest
##### "pushing" (sending to) 
`scp *.html xubuntu@192.168.1.109:directory`
copy files to a directory inside default directory we log into

`scp -r directory-with-sth xubuntu@192.168.1.109:`
`-r` recursively send whole directory


##### "pulling" (copying from)
`scp xubuntu@192.168.1.109:webpage-ssh/index.html .`

`scp -r xubuntu@192.168.1.109:webpage-ssh/ .`
`-r` recursively copy whole directory