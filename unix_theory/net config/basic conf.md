`/etc/hosts` - first resort DNS lookup
	you can e.g. "ban" some sites by redirecting URLs to 127.0.0.1 (no webserver -> error)
```
google.com     127.0.0.1
```

`/etc/nsswitch.conf` - i.a. DNS resolution order
```
hosts:     files mdns4_minimal [NOTFOUND=return] dns myhostname
```
"files" == `/etc/hosts`

`/etc/resolv.conf` - managed by `systemd-resolved.service`
	you can use it to check which nameserver you're using
```
nameserver 127.0.0.53
```


### Debian
**`/etc/netplan/`** - there should be `.yaml`   (NEW)
``` yaml
network:
 version: 2
 renderer: networkd
 ethernets:
  eth0:
   dhcp4: no
   addresses: [192.168.0.0/24]
   gateway4: 192.168.0.1
   nameservers:
    addresses: [8.8.8.8,8.8.4.4,1.1.1.1]
```
`.yaml` depend on indentation
`sudo netplan apply`

**`/etc/network/interfaces`** - describe/configure network interfaces  (OLD)
``` bash
# describe available network interfaces & how to activate them
source /etc/networ/interfaces.d/*   
# loopback network interface
auto lo
iface lo inet loopback
# primary network interface
auto eth0
iface eth0 inet static
 address 192.168.0.2
 gateway 192.168.0.1
 netmask 255.255.255.0
 dns-nameservers 127.0.0.3
```

or `NetworkManager`


### CentOS & RedHat/Fedora
**`/etc/sysconfig/`** - place for most of the system configuration files:D
`/etc/sysconfig/network-scripts/ifcfg-eth0` - conf file for eth0 interface
	It's fully integrated with `NetworkManager` (changes in config file seen in GUI and vice versa)
`sudo service network restart`