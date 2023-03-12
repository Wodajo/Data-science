### Docker Engine installation
`sudo pacman -S docker`
`sudo systemctl enable docker`
`sudo docker info` - check if  you can connect with daemon
	(sometimes vpn&docker networks overlay - start without vpn)

`sudo docker run -it --rm archlinux bash -c "echo hello world"` - check if you can create containers
	(downloads archlinux and use bash to print hello world)

 `usermod -aG docker username` - if you want to use docker as non-root
	 IT'S ROOT EQUIVALENT bcos `docker run --privileged` can start containers with root priv

`docker` cli is a way of communicating with `daemon` (Docker Engine).
`containers` are processes of that daemon (if daemon is down -> containers are down)

### configuration
`/etc/docker/daemon.json` OR adding flags to `docker.service` systemd unit

`storage driver` - 