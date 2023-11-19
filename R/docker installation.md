`docker run --name rstudio --restart=always -v ~/github/projects/:/home/rstudio/projects/ -e PASSWORD=yourpassword123 -dp 8899:8787 rocker/ml`
	Rstudio with CUDA
	rstudio/yourpassword - initial creds

`docker commit -a "Ultrabob Master " -m "added pak&renv" 88ffebedcbc2 ml:pak_renv`
`docker run --name rstudio --restart=always -v /:/twardovsky -e PASSWORD=password -dp 8899:8787 ml:pak_renv`



```shell
docker run --rm -e USERID=$(id -u) -e GROUPID=$(id -g) wodajo/rstudio:4.4.0
```

### Dockerfile
user settings
```
COPY --chown=rstudio:rstudio rstudio/rstudio-prefs.json /home/rstudio/.config/rstudio
```

.Rprofile
```
COPY --chown=rstudio:rstudio rstudio/.Rprofile /home/rstudio/
```
przykład (lepiej zamontować pakiety via renv cache -> patrz "start" header)
``` Rprofile
.libPaths("/packages/")
```


### start
Cache powinien miec osobną, montowalą do kontenerów lokalizację.
`renv::paths$cache()` - shows current cache
Można podać ścieżkę podczas odpalania kontenera
```
# the location of the renv cache on the host machine
RENV_PATHS_CACHE_HOST=/opt/local/renv/cache

# where the cache should be mounted in the container
RENV_PATHS_CACHE_CONTAINER=/renv/cache

# run the container with the host cache mounted in the container
docker run --rm \
	-d \
    -e "RENV_PATHS_CACHE=${RENV_PATHS_CACHE_CONTAINER}" \
    -v "${RENV_PATHS_CACHE_HOST}:${RENV_PATHS_CACHE_CONTAINER}" \
    -e USERID=$(id -u) -e GROUPID=$(id -g) \
	--name rstudio_server \
	-e PASSWORD=password \
    -p 14618:14618 \
    R -s -e 'renv::restore(); shiny::runApp(host = "0.0.0.0", port = 14618)'
    wodajo/rstudio:4.3.3
```
or export `RENV_PATHS_CACHE` via `Renviron.site` (R installation's site-wide) during docker image building

### ssh forwarding

```bash
# -N Do not execute a remote command. This is useful for just forwarding ports
# -f Requests ssh to go to background just before command execution
# -Y Enables trusted X11 forwarding
# -L Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port

ssh -N -f -Y -L localhost:8888:192.168.1.3:8080 wodajo@44.11.22.33
```
`ssh -L 8888:192.168.1.3:8080 kali@44.11.22.33`
	forward from localhost:8888 (because there is nothing before 8888 - localhost assumed) (client) -> 44.11.22.33 (server) -de-encapsulation-> forward -> 192.168.1.3:8080
![local forward](local_forward.png)
firefox
	about:config
	network.security.ports.banned.override
	select port for override (otherwise it will be blocked)
### new user
```bash
# docker ps -a
docker exec -it rstudio_wodajo /bin/bash

my_user=$1
# once you are inside the container
useradd ${my_user}

# enter password when prompted
passwd ${my_user}

mkdir /home/${my_user}
chown ${my_user}:${my_user} /home/${my_user}

exit
```