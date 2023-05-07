

### usefull
`docker run -v "$PWD/":/scripts -it <image_name> /bin/bash`  --> `bash /scripts/myscript.sh`
	`-v` mount a dir
	`-it` interactive shell

ctl-p ctl-q to detach `run -it` container :D
`docker attach container_id` to reattach

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
`sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

`sudo systemctl enable docker`
`sudo docker info` - check if  you can connect with daemon
	(sometimes vpn&docker networks overlay - start without vpn)

`sudo docker run -it --rm archlinux bash -c "echo hello world"` - check if you can create containers
	(downloads archlinux and use bash to print hello world)

 `usermod -aG docker username` - if you want to use docker as non-root
	 IT'S ROOT EQUIVALENT bcos `docker run --privileged` can start containers with root priv

`docker` cli is a way of communicating with `daemon` (Docker Engine).
`containers` are processes of that `daemon` (if daemon is down -> containers are down)
`image` is a read-only template with instructions for creating a docker container

`docker build -t my_image .` - build docker image `my_image` in `.` directory
`docker run -dp 3000:3000 my_image`
	`-d` detached (in background)
	`-p 3000:3000` map local port 3000 to container port 3000 (for network access)

`docker ps -a` - info about docker processes (containers)

`docker stop docker_ID` - id from `docker ps`
`docker rm docker_ID` - remove stopped container
`docker rm -f docker_ID` - stop&remove container with one command

`docker start docker_ID`
`docker exec -it docker_ID bash` - interactive mode bash
	This is $#@$# wierd

`docker images` - list available images

### configuration
`/etc/docker/daemon.json` OR adding flags to `docker.service` systemd unit


#### images
`/var/lib/docker` - default location
if you want to move them:
1.  stop `docker.daemon` (will stop all containers!) -> unmount images
2. move image to prefered dst.
3. configure `data-root` in `/etc/docker/daemon.json`:   - or CREATE
```
{
  "data-root": "/mnt/docker"
}
```
4. restart `docker.daemon`

`docker build -t my_image .` - build docker image `my_image` in `.` directory
`docker run my_image`




### not sorted
it creates MEGA SPECIFIC `json.log` files - they eat up storage ridiculusly fast
`docker run --log-driver none <image>` - supress docker logs creation for given container
OR
`docker run --log-driver syslog <image>` - for `syslog` (you can also use `journald`) logging driver

APPEND `--rm` - otherwise it get's messy (in `docker ps -a`) fast 

`docker container prune` - delete all stopped containers
`docker rm -f $(docker ps -aq)` - delete all containers, including running
`docker rmi image_id image_id` - delete images

`docker stats` - cpu/mem of docker containers
`docker inspect my_container` - info about container configuration
`docker history --no-trunc my_image` - history of **image**, including commands used to create it

`-u $(whoami)` - append this flag for easy management of permissions
	won't work e.g. in case of opening privileged port
`docker rename old_name new_name`

by default containers limited only by kernel scheduler:
```
By default, a container has no resource constraints and can use as much of a given resource as the host’s kernel scheduler allows
```
