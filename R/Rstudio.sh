#! /usr/bin/env bash

#MAIN_LOG='Rstudio.log'

if [ "$1" == "" ] || [ "$4" == "" ]
then
	echo 'Syntax: Rstudio.sh /path/to/renv_cache /path/to/projects_home passwd port'
#	echo 'Logfile in Rstudio.log'
else
	echo '[+] docker setup'
	RENV_PATHS_CACHE_HOST=$1
	RENV_PATHS_CACHE_CONTAINER=/renv/cache

	docker run \
	--name rstudio_wodajo --restart=always \
	-e USERID=$(id -u) -e GROUPID=$(id -g) \
       	-v $1:$1 -v $2:/home/rstudio/projects \
	-v "${RENV_PATHS_CACHE_HOST}:${RENV_PATHS_CACHE_CONTAINER}" \
	-e "RENV_PATHS_CACHE"="${RENV_PATHS_CACHE_CONTAINER}" \
	-e PASSWORD=$3 \
	-d \
	-p $4:$4 \
	rstudio_wodajo_test6
fi
echo '[+] done'
