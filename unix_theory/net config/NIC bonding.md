`network bonding` aka `NIC bonding` - combine multiple NIC interfaces into a single logical one.
Allow to utilise full bandwidth of all cables connecting hosts & increase redundancy
	switch support - needed switch with `link aggregation`/`LACP` (link aggregation control protocol)/`EtherChannel` (different "brand" names for he same function)
	generic - no need for switch support

`NetworkManager` DOESN'T support `NIC bonding`
`networkd` does (`systemd-networkd` service)

#### recommendation
- if "dumb" switch - mode 6
- if switch supports `link aggregation` - mode 4 (802.3ad)
- if connecting multiple servers with just cables - mode 0



### testing
###### Debian
`NetworkManager` DOESN'T support `NIC bonding`
`networkd` does (set it as renderer in `/etc/netplan/`)
```yaml
network:
 version: 2
 renderer: networkd
 ethernets:
  eth0:
   dhcp4: false
 bonds:
  bond0:
   dhcp4: false
   interfaces:
    - eth0                  # kinda silly to bond one interface, only for example sake
   addresses: [192.168.1.1/24]
   gateway4: 192.168.1.1
   parameters:
    mode: active-backup
   nameservers:
    addresses: [1.1.1.1]
```
`sudo netplan apply`
`/proc/net/bonding/` - info about `bond0`
	i.a. currently active slave, speed, duplex, status, permanent hw MAC

###### CentOS
`/etc/sysconfig/netowrk-scripts/ifcfg-eth0`
```
# notice - no IP info in slave config
TYPE=Ethernet
BOOTPROTO=none
DEFROUTE=yes
NAME=eth0
DEVICE=eth0
ONBOOT=yes
MASTER=bond0         # change to default
SLAVE=yes            # change to default
```
`/etc/sysconfig/networking-scripts/ifcfg-bond0`
```
DEVICE=bond0
NAME=bond0
BONDING_MASTER=yes
IPADDRES=192.168.1.2
PREFIX=24
ONBOOT=yes
BOOTPROTO=none
BONDING_OPTS="mode=6 miimon=100"  #miimon option - specify frequency of MII (Media Independent Interface) link monitoring [ms].
# MII - process that the bonding driver uses to detect when a slave interface goes down
```
`systemctl restart network`
check setup in `/proc/net/bonding/bond0` (like in debian)


#### modes description
1.  Mode 0 (round-robin) - each frame sent from different interface
   if connecting with switch - switch support needed 
   if connecting without switch - **you can connect hosts with crossover cables**
   
2.  Mode 1 (active-backup) - one interface is active at a time
   other interfaces remain in a standby state, ready to take over if the active interface fails. 
   
3.  Mode 2 (balance-XOR) - use a hashes of both sides MAC addresses to identify which interfaces are connected to the other side
   logical interfaces are always communicating with the same NICs
	   `Require switch support`
	   The specific algorithm used will depend on the bonding driver being used.
	   The algorithm is based on XOR operation, which helps to distribute the traffic evenly among the interfaces
   
4.  Mode 3 (broadcast) - sends the same traffic to all available interfaces
	  `Require switch support`

5.  Mode 4 (**802.3ad**) - aka `LACP` (Link Aggregation Control Protocol)
   allows the NICs to automatically negotiate aggregation with the switch to which they are connected
      `Require switch support`
	  **Industry standard**
	 (suitable for high-availability environment where multiple NICs are connected to different switches)

6.  Mode 5 (balance-TLB)  - uses adaptive `transmit load balancing`
   transmit from interface that is currently least busy
   incoming always go to one active port

7.  Mode 6 (balance-ALB) - `adaptive load balancing` mode
   similar to mode 5, but transmit&incoming go to least busy interface
	   works by constantly changing MAC addresses of interfaces


