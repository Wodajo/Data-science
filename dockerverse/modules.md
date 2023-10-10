dynamic modification of the user's environment


### ubuntu:22.04 docker
`docker run -it --rm -w="/usr/local/bin" ubuntu:22.04 /bin/bash`
`apt install environment-modules`
	it's interactive install - asks for location
	important stuff
		/etc/profile.d/modules.sh
		/usr/lib/x86_64-linux-gnu/modulecmd.tcl
		/usr/lib/modulecmd.tcl
`eval "$(/usr/lib/modulecmd.tcl sh autoinit` - automatic setup of `modules` (previously not accessible from cli)

## setup modulefiles
`modulefile`'s can be used to implement site policies regarding the access and use of applications
	by changing envs
	expected to be in `$MODULEPATH` - let it be mounted as external library

```bash
#add local modules to module path in .bashrc:
export MODULEPATH="$MODULEPATH:/media/some_drive/modulefiles"
export MODULEPATH="$MODULEPATH:/usr/local/bin/modulefiles"
```
`. ~/bashrc`


  ```modulefile
#%Module -*- tcl -*-
##
## modulefile
##
proc ModulesHelp { } {
    puts stderr "\t<Text about the program>." 
}

<module load <pre-requisite module>>

module-whatis "<Text about the program>"

prepend-path      PATH              /path/to/apps/program
```

NIE WARTO.



Nextflow
curl
unzip
zip
https://sdkman.io/usage- java


