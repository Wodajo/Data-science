### usefull
`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-name OR id>` - to get IP address of running container

`/etc/hosts` - for local resolution of docker container IP :D
```
#!/usr/bin/env sh
for ID in $(docker ps -q | awk '{print $1}'); do
    IP=$(docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" "$ID")
    NAME=$(docker ps | grep "$ID" | awk '{print $NF}')
    printf "%s %s\n" "$IP" "$NAME"
done
```


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


#### images
`/var/lib/docker` - default location
if you want to move them:
1.  stop `docker.daemon` (will stop all containers!) -> unmount images
2. move image to prefered dst.
3. configure `data-root` in `/etc/docker/daemon.json`:
```
{
  "data-root": "/mnt/docker"
}
```
4. restart `docker.daemon`

`docker build -t my_image` - to build docker image
`docker run my_image`