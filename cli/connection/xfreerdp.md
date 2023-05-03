`xfreerdp /u:administrator /p:letmein123! /cert:ignore /v:10.10.245.121 /w:1600 /h:600`
`1600x600` gives nice slim&long window on my lap


### set up xrdp server
`sudo apt install xrdp`
`sudo systemctl status xrdp`

it uses `/etc/ssl/private/ssl-cert-snakeoil.key` - readonly for users in `ssl-cert` group
`sudo adduser xrdp ssl-cert`
`sudo systemctl restart xrdp`

listens on port `3389`

config files in `/etc/xrdp`
